#!/usr/bin/env python3
# Version: v0.1.0
# Last updated: 2026-06-10
# Owner: PrecodeOS
# Created by Dan Sears / Recode.
# SPDX-License-Identifier: Apache-2.0
from __future__ import annotations

from contextlib import redirect_stdout, redirect_stderr
import importlib.util
import io
import json
from pathlib import Path
import subprocess
import sys
import tempfile
from typing import Any


def load_bead_transition_module() -> Any:
    path = Path(__file__).with_name("bead-transition.py")
    spec = importlib.util.spec_from_file_location("bead_transition", path)
    if spec is None or spec.loader is None:
        raise RuntimeError("Could not load bead-transition.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[str(spec.name)] = module
    spec.loader.exec_module(module)
    return module


def make_fixture(root: Path, *, include_next: bool = True, include_log: bool = True) -> dict[str, Path]:
    current = root / "tasks" / "beads" / "B001-current.md"
    next_bead = root / "tasks" / "beads" / "B002-next.md"
    todo = root / "tasks" / "todo.md"
    log = root / "logs" / "bead-transitions.jsonl"
    current.parent.mkdir(parents=True, exist_ok=True)
    todo.parent.mkdir(parents=True, exist_ok=True)
    log.parent.mkdir(parents=True, exist_ok=True)

    current.write_text("status: review\n", encoding="utf-8")
    if include_next:
        next_bead.write_text("status: ready\n", encoding="utf-8")
    todo.write_text("current_bead: tasks/beads/B001-current.md\n", encoding="utf-8")
    if include_log:
        log.write_text('{"event":"previous"}\n', encoding="utf-8")

    return {"current": current, "next": next_bead, "todo": todo, "log": log}


def install_fixture_mutators(module: Any, validation_returncode: int) -> None:
    def update_bead_status(path: Path, new_status: str, root: Path) -> None:
        path.write_text(f"status: {new_status}\n", encoding="utf-8")

    def rewrite_todo(root: Path, current_rel: str, next_rel: str) -> None:
        (root / "tasks" / "todo.md").write_text(f"current_bead: {next_rel}\ncurrent_state: in_progress\n", encoding="utf-8")

    def run(*args: Any, **kwargs: Any) -> subprocess.CompletedProcess[str]:
        return subprocess.CompletedProcess(args=args[0] if args else [], returncode=validation_returncode)

    module.update_bead_status = update_bead_status
    module.rewrite_todo = rewrite_todo
    module.subprocess.run = run


def read_optional(path: Path) -> str | None:
    if not path.exists():
        return None
    return path.read_text(encoding="utf-8")


def approval_assessment() -> dict[str, object]:
    return {
        "eligible": True,
        "blockers": [],
        "current": "tasks/beads/B001-current.md",
        "next": "tasks/beads/B002-next.md",
        "next_summary": {},
        "latest_results": [],
    }


def run_success_scenario(module: Any, failures: list[dict[str, str]]) -> None:
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        paths = make_fixture(root)
        install_fixture_mutators(module, 0)

        stdout = io.StringIO()
        with redirect_stdout(stdout):
            code = module.approve_transition(root, approval_assessment())
        combined = paths["current"].read_text(encoding="utf-8") + paths["next"].read_text(encoding="utf-8")
        log_lines = paths["log"].read_text(encoding="utf-8").splitlines()

        if code != 0:
            failures.append({"scenario": "success exit", "expected": "0", "actual": str(code)})
        if combined.count("status: in_progress") != 1:
            failures.append({"scenario": "success active bead count", "expected": "one in_progress", "actual": combined})
        if "current_bead: tasks/beads/B002-next.md" not in paths["todo"].read_text(encoding="utf-8"):
            failures.append({"scenario": "success todo rewrite", "expected": "next bead", "actual": paths["todo"].read_text(encoding="utf-8")})
        if len(log_lines) != 2:
            failures.append({"scenario": "success log append", "expected": "2 lines", "actual": str(len(log_lines))})


def run_rollback_scenario(module: Any, failures: list[dict[str, str]]) -> None:
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        paths = make_fixture(root)
        originals = {name: read_optional(path) for name, path in paths.items()}
        install_fixture_mutators(module, 7)

        stderr = io.StringIO()
        with redirect_stderr(stderr):
            code = module.approve_transition(root, approval_assessment())
        restored = {name: read_optional(path) for name, path in paths.items()}

        if code != 7:
            failures.append({"scenario": "rollback exit", "expected": "7", "actual": str(code)})
        if restored != originals:
            failures.append({"scenario": "rollback restoration", "expected": str(originals), "actual": str(restored)})
        if "rolled back" not in stderr.getvalue():
            failures.append({"scenario": "rollback message", "expected": "rolled back", "actual": stderr.getvalue()})


def run_missing_next_scenario(module: Any, failures: list[dict[str, str]]) -> None:
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        paths = make_fixture(root, include_next=False)
        originals = {name: read_optional(path) for name, path in paths.items()}
        install_fixture_mutators(module, 0)

        stdout = io.StringIO()
        with redirect_stdout(stdout):
            code = module.approve_transition(root, approval_assessment())
        restored = {name: read_optional(path) for name, path in paths.items()}

        if code != 1:
            failures.append({"scenario": "missing next exit", "expected": "1", "actual": str(code)})
        if restored != originals:
            failures.append({"scenario": "missing next no mutation", "expected": str(originals), "actual": str(restored)})
        if "next bead file is missing" not in stdout.getvalue():
            failures.append({"scenario": "missing next blocker", "expected": "next bead file is missing", "actual": stdout.getvalue()})


def run_ineligible_scenario(module: Any, failures: list[dict[str, str]]) -> None:
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        paths = make_fixture(root)
        originals = {name: read_optional(path) for name, path in paths.items()}
        install_fixture_mutators(module, 0)
        assessment = dict(approval_assessment())
        assessment["eligible"] = False
        assessment["blockers"] = ["review decision is not accepted"]

        stdout = io.StringIO()
        with redirect_stdout(stdout):
            code = module.approve_transition(root, assessment)
        restored = {name: read_optional(path) for name, path in paths.items()}

        if code != 1:
            failures.append({"scenario": "ineligible exit", "expected": "1", "actual": str(code)})
        if restored != originals:
            failures.append({"scenario": "ineligible no mutation", "expected": str(originals), "actual": str(restored)})
        if "review decision is not accepted" not in stdout.getvalue():
            failures.append({"scenario": "ineligible blockers", "expected": "printed blocker", "actual": stdout.getvalue()})


def main() -> int:
    module = load_bead_transition_module()
    failures: list[dict[str, str]] = []

    run_success_scenario(module, failures)
    run_rollback_scenario(module, failures)
    run_missing_next_scenario(module, failures)
    run_ineligible_scenario(module, failures)

    payload = {
        "tool": "bead-transition-scenario-check",
        "status": "pass" if not failures else "fail",
        "scenario_count": 4,
        "failures": failures,
    }
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
