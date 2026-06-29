#!/usr/bin/env python3
# Version: v0.1.0
# Last updated: 2026-06-13
# Owner: PrecodeOS
# Created by Dan Sears / Recode.
# SPDX-License-Identifier: Apache-2.0
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import json
from pathlib import Path
import shlex
import subprocess
import sys
from typing import Any

from os_compiler import compile_state, repo_root
from os_parser import MarkdownDocument


DEFAULT_VALIDATORS = [
    "bash scripts/validate-memory.sh",
    "python3 scripts/files-in-play-check.py",
    "python3 scripts/run-contract-check.py",
    "python3 scripts/tool-execution-check.py",
    "python3 scripts/loop-health.py --json",
    "python3 scripts/completion-check.py",
]

NONE_MARKERS = {"", "none", "null", "false", "no", "off", "0", "[]"}
PASS_DECISION = "review"


def parse_bool(value: Any) -> bool:
    if isinstance(value, bool):
        return value
    return str(value or "").strip().lower() in {"true", "yes", "on", "1", "enabled"}


def parse_positive_int(value: Any, default: int) -> int:
    try:
        parsed = int(str(value).strip())
    except (TypeError, ValueError):
        return default
    return parsed if parsed > 0 else default


def normalize_list(value: Any) -> list[str]:
    if isinstance(value, list):
        return [str(item).strip() for item in value if str(item).strip()]
    raw = str(value or "").strip()
    if raw.lower() in NONE_MARKERS:
        return []
    return [item.strip() for item in raw.split(",") if item.strip()]


def run_command(command: str, root: Path) -> dict[str, Any]:
    started = datetime.now(timezone.utc)
    try:
        parts = shlex.split(command)
    except ValueError as error:
        return {
            "command": command,
            "status": "fail",
            "exit_code": 2,
            "stdout_excerpt": "",
            "stderr_excerpt": str(error),
        }
    if not parts:
        return {
            "command": command,
            "status": "fail",
            "exit_code": 2,
            "stdout_excerpt": "",
            "stderr_excerpt": "empty command",
        }
    completed = subprocess.run(
        parts,
        cwd=root,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    duration = (datetime.now(timezone.utc) - started).total_seconds()
    return {
        "command": command,
        "status": "pass" if completed.returncode == 0 else "fail",
        "exit_code": completed.returncode,
        "duration_seconds": round(duration, 3),
        "stdout_excerpt": completed.stdout[-1200:],
        "stderr_excerpt": completed.stderr[-1200:],
    }


def classify_guardrail(command: str, root: Path) -> dict[str, Any]:
    if not command:
        return {}
    result = run_command(f"python3 scripts/files-in-play-check.py --command {shlex.quote(command)}", root)
    parsed: dict[str, Any] = {}
    try:
        parsed = json.loads(result.get("stdout_excerpt") or "{}")
    except json.JSONDecodeError:
        parsed = {}
    details = parsed.get("details") or {}
    return {
        "raw_result": result,
        "user_decision": details.get("user_decision") or "unknown",
        "summary": details.get("plain_english_summary") or "",
        "approval_prompt": details.get("approval_prompt") or "",
    }


def load_prior_attempts(root: Path, bead: str) -> list[dict[str, Any]]:
    path = root / "logs" / "ralph-attempts.jsonl"
    if not path.is_file():
        return []
    rows: list[dict[str, Any]] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        try:
            item = json.loads(line)
        except json.JSONDecodeError:
            continue
        if item.get("bead") == bead:
            rows.append(item)
    return rows


def write_jsonl(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(payload, separators=(",", ":")) + "\n")


def render_summary(root: Path, payload: dict[str, Any], prior_count: int) -> None:
    path = root / "logs" / "ralph-summary.md"
    validators = payload.get("validators") or []
    lines = [
        "# Ralph Attempt Summary",
        "<!-- ANCHOR: ralph-summary -->",
        "",
        "> AUTHORITY: Generated Ralph loop evidence summary for the active PrecodeOS bead.",
        "> NOT_AUTHORITY: Active memory, task selection, product decisions, implementation plans, review acceptance, bead transition approval, command approval, or proof by itself.",
        "> LOAD_WHEN: Reviewing Ralph attempts, bounded retry history, or current bead failure evidence.",
        "> CLASS: generated",
        "",
        f"Generated: {payload['timestamp']}",
        "",
        "## Current Attempt",
        "",
        f"- Bead: `{payload.get('bead') or 'missing'}`",
        f"- Attempt: {payload.get('attempt_number')} of {payload.get('max_attempts')}",
        f"- Prior attempts for bead: {prior_count}",
        f"- Attempt command: `{payload.get('attempt_command') or 'none'}`",
        f"- Failure category: `{payload.get('failure_category')}`",
        f"- Decision: `{payload.get('decision')}`",
        f"- Another attempt allowed: {payload.get('another_attempt_allowed')}",
        f"- Stop reason: {payload.get('stop_reason') or 'none'}",
        "",
        "## Validator Results",
        "",
    ]
    for item in validators:
        lines.append(f"- `{item.get('command')}` -> {item.get('status')} exit={item.get('exit_code')}")
    if not validators:
        lines.append("- No validators were run.")
    lines.extend(
        [
            "",
            "## Boundary",
            "",
            "Ralph output is generated evidence. It may support review, debugging, split decisions, or handoff, but it does not accept work or approve a bead transition.",
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def active_bead_doc(root: Path, current_bead: str) -> MarkdownDocument | None:
    if not current_bead:
        return None
    path = root / current_bead
    if not path.is_file():
        return None
    return MarkdownDocument.load(path)


def decide(
    *,
    active_bead: str,
    enabled: bool,
    force: bool,
    prior_count: int,
    max_attempts: int,
    guardrail: dict[str, Any],
    attempt_result: dict[str, Any] | None,
    validators: list[dict[str, Any]],
    retry_policy: str,
) -> tuple[str, str, bool, str]:
    if not active_bead:
        return "missing_active_bead", "stop", False, "Ralph needs one active bead."
    if not enabled and not force:
        return "not_enabled", "stop", False, "Active bead has not opted into Ralph; pass --force only for an explicit one-off run."
    if prior_count >= max_attempts:
        return "retry_budget_exhausted", "stop", False, "Ralph retry budget is exhausted for this bead."

    guardrail_decision = str(guardrail.get("user_decision") or "").lower()
    if guardrail_decision in {"approval needed", "stop"}:
        return "approval_required", "ask", False, guardrail.get("summary") or "Attempt command needs approval."
    if attempt_result and attempt_result.get("status") != "pass":
        another = retry_policy != "stop_on_first_failure" and prior_count + 1 < max_attempts
        return "attempt_failed", "retry" if another else "stop", another, "Attempt command failed."
    failed_validators = [item for item in validators if item.get("status") != "pass"]
    if failed_validators:
        another = retry_policy == "bounded" and prior_count + 1 < max_attempts
        return "validator_failed", "retry" if another else "ask", another, "One or more validators failed."
    return "pass", PASS_DECISION, False, "Validators passed; request human review before acceptance or transition."


def main() -> int:
    parser = argparse.ArgumentParser(description="Run one bounded Ralph retry attempt for one active Precode bead.")
    parser.add_argument("--attempt-command", default="", help="explicit command to run as the attempt before validators")
    parser.add_argument("--validator", action="append", default=[], help="validator command; repeat to override the default set")
    parser.add_argument("--max-attempts", type=int, default=0, help="override active bead Ralph max attempts")
    parser.add_argument("--force", action="store_true", help="allow a one-off Ralph run even when the bead does not opt in")
    parser.add_argument("--dry-run", action="store_true", help="run checks and print payload without writing Ralph logs")
    parser.add_argument("--json", action="store_true", help="print JSON payload")
    args = parser.parse_args()

    root = repo_root()
    state = compile_state(root)
    active_bead = str(state.get("current_bead") or "")
    doc = active_bead_doc(root, active_bead)
    frontmatter = doc.frontmatter if doc else {}

    enabled = parse_bool(frontmatter.get("ralph_enabled"))
    max_attempts = args.max_attempts or parse_positive_int(frontmatter.get("ralph_max_attempts") or frontmatter.get("max_attempts"), 3)
    retry_policy = str(frontmatter.get("ralph_retry_policy") or "bounded").strip() or "bounded"
    bead_validators = normalize_list(frontmatter.get("ralph_validator_set"))
    validators_to_run = args.validator or bead_validators or DEFAULT_VALIDATORS
    prior = load_prior_attempts(root, active_bead)

    preflight_category = ""
    preflight_decision = ""
    preflight_stop = ""
    if not active_bead:
        preflight_category = "missing_active_bead"
        preflight_decision = "stop"
        preflight_stop = "Ralph needs one active bead."
    elif not enabled and not args.force:
        preflight_category = "not_enabled"
        preflight_decision = "stop"
        preflight_stop = "Active bead has not opted into Ralph; pass --force only for an explicit one-off run."
    elif len(prior) >= max_attempts:
        preflight_category = "retry_budget_exhausted"
        preflight_decision = "stop"
        preflight_stop = "Ralph retry budget is exhausted for this bead."

    guardrail: dict[str, Any] = {}
    attempt_result = None
    validator_results: list[dict[str, Any]] = []
    if not preflight_category:
        guardrail = classify_guardrail(args.attempt_command, root) if args.attempt_command else {}
        if args.attempt_command and str(guardrail.get("user_decision") or "").lower() not in {"approval needed", "stop"}:
            attempt_result = run_command(args.attempt_command, root)
        validator_results = [run_command(command, root) for command in validators_to_run]

    failure_category, decision, another_allowed, stop_reason = decide(
        active_bead=active_bead,
        enabled=enabled,
        force=args.force,
        prior_count=len(prior),
        max_attempts=max_attempts,
        guardrail=guardrail,
        attempt_result=attempt_result,
        validators=validator_results,
        retry_policy=retry_policy,
    )
    if preflight_category:
        failure_category = preflight_category
        decision = preflight_decision
        another_allowed = False
        stop_reason = preflight_stop

    payload = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "tool": "ralph-loop",
        "bead": active_bead or None,
        "attempt_number": len(prior) + 1,
        "max_attempts": max_attempts,
        "ralph_enabled": enabled,
        "force": args.force,
        "retry_policy": retry_policy,
        "attempt_command": args.attempt_command or None,
        "command_guardrail": guardrail,
        "attempt_result": attempt_result,
        "validators": validator_results,
        "failure_category": failure_category,
        "decision": decision,
        "another_attempt_allowed": another_allowed,
        "stop_reason": stop_reason,
        "generated_evidence_only": True,
        "dry_run": args.dry_run,
    }

    if not args.dry_run:
        write_jsonl(root / "logs" / "ralph-attempts.jsonl", payload)
        render_summary(root, payload, len(prior))

    if args.json:
        print(json.dumps(payload, indent=2, sort_keys=True))
    else:
        print(f"Ralph decision: {decision}")
        print(f"Failure category: {failure_category}")
        print(f"Another attempt allowed: {another_allowed}")
        print(f"Stop reason: {stop_reason}")
        if args.dry_run:
            print("Dry run: no Ralph logs written.")

    return 0 if decision in {"review", "retry"} else 1


if __name__ == "__main__":
    raise SystemExit(main())
