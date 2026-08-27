#!/usr/bin/env python3
# Version: v0.1.1
# Last updated: 2026-08-27
# Owner: PrecodeOS
# Created by Dan Sears / Recode.
# SPDX-License-Identifier: Apache-2.0
"""Deterministic regression checks for dependency parsing and promotion readiness."""
from __future__ import annotations

import json
from pathlib import Path
import sys
import tempfile

from os_compiler import promotion_readiness, start_readiness
from precode_state import BeadRecord, parse_dependency_section, read_bead


CHECK = "python3 scripts/validate-memory.sh"


def bead(bead_id: str, status: str, depends_on: list[str], *, closeout: dict[str, str] | None = None) -> BeadRecord:
    return BeadRecord(
        rel_path=f"tasks/beads/{bead_id}-example.md",
        title=f"{bead_id} example",
        bead_id=bead_id,
        status=status,
        execution_mode="builder",
        bead_kind="implementation",
        primary_authority="tasks/prds/PRD-001-example.md",
        depends_on=depends_on,
        parent_prd="tasks/prds/PRD-001-example.md",
        requirement_ids=["FR01"],
        files_in_play=["app/example.py"],
        checks=[CHECK],
        verification_type=["automated"],
        delegation_mode="single_agent",
        test_strategy="automated",
        review_context="same_session_ok",
        complexity="narrow",
        required_planning_depth="brief",
        autonomy_level="supervised",
        run_contract={},
        closeout=closeout or {},
        handback="",
        frontmatter={},
        sections={},
    )


def latest_check() -> dict[tuple[str, str, str], dict[str, object]]:
    return {("raw", CHECK, "."): {"status": "pass", "exit_code": 0}}


def run() -> list[dict[str, str]]:
    failures: list[dict[str, str]] = []

    predecessor = bead("B159", "review", [])
    successor = bead("B160", "ready", ["B159"])
    if not any("dependency is not done" in item for item in start_readiness(successor, {predecessor.rel_path: predecessor, successor.rel_path: successor})["blockers"]):
        failures.append({"scenario": "ordinary start gate", "expected": "review predecessor blocks start", "actual": "no dependency blocker"})

    closeout = {"manual_verification": "pass", "review_decision": "accepted", "next_bead": successor.rel_path}
    current = bead("B159", "review", [], closeout=closeout)
    next_bead = bead("B160", "ready", [current.rel_path])
    bead_map = {current.rel_path: current, next_bead.rel_path: next_bead}
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        (root / next_bead.rel_path).parent.mkdir(parents=True)
        (root / next_bead.rel_path).write_text("status: ready\n", encoding="utf-8")
        promotion = promotion_readiness(root, current, bead_map, latest_check())
    if not promotion["eligible"]:
        failures.append({"scenario": "sequential promotion", "expected": "eligible with projected predecessor done", "actual": str(promotion["blockers"])})
    if current.status != "review":
        failures.append({"scenario": "projection isolation", "expected": "current bead remains review", "actual": current.status})

    unfinished = bead("B158", "in_progress", [])
    blocked = start_readiness(bead("B160", "ready", [unfinished.rel_path]), {unfinished.rel_path: unfinished})
    if not any("dependency is not done" in item for item in blocked["blockers"]):
        failures.append({"scenario": "non-current dependency", "expected": "unfinished dependency blocks", "actual": str(blocked)})

    blocked_next = bead("B160", "ready", [current.rel_path, unfinished.rel_path])
    blocked_map = {
        current.rel_path: current,
        unfinished.rel_path: unfinished,
        blocked_next.rel_path: blocked_next,
    }
    blocked_closeout = dict(closeout)
    blocked_closeout["next_bead"] = blocked_next.rel_path
    blocked_current = bead("B159", "review", [], closeout=blocked_closeout)
    blocked_map[blocked_current.rel_path] = blocked_current
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        (root / blocked_next.rel_path).parent.mkdir(parents=True)
        (root / blocked_next.rel_path).write_text("status: ready\n", encoding="utf-8")
        blocked_promotion = promotion_readiness(root, blocked_current, blocked_map, latest_check())
    if not any(
        unfinished.rel_path in item and "dependency is not done" in item
        for item in blocked_promotion["blockers"]
    ):
        failures.append(
            {
                "scenario": "non-current promotion dependency",
                "expected": "unfinished unrelated dependency blocks promotion",
                "actual": str(blocked_promotion["blockers"]),
            }
        )

    prose = """\n- `tasks/beads/B159-bff-server-side-caller.md`. **Hard prerequisite.** This bead records who owns a\n  scan, which requires naming the caller server-side.\n- B157 must be reviewed first.\n"""
    parsed = parse_dependency_section(prose)
    expected = ["tasks/beads/B159-bff-server-side-caller.md", "B157"]
    if parsed != expected:
        failures.append({"scenario": "prose dependency extraction", "expected": str(expected), "actual": str(parsed)})

    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        path = root / "tasks" / "beads" / "B160-example.md"
        path.parent.mkdir(parents=True)
        path.write_text(
            """---\nbead_id: B160\nstatus: ready\ndepends_on: []\n---\n\n## Depends On\n\n- `tasks/beads/B159-example.md`. Hard prerequisite.\n""",
            encoding="utf-8",
        )
        parsed_fallback = read_bead(path, root).depends_on
    if parsed_fallback != ["tasks/beads/B159-example.md"]:
        failures.append({"scenario": "read_bead prose fallback", "expected": "['tasks/beads/B159-example.md']", "actual": str(parsed_fallback)})

    missing = parse_dependency_section("- `tasks/beads/B999-missing.md`. Required before this bead.\n")
    if missing != ["tasks/beads/B999-missing.md"]:
        failures.append({"scenario": "missing reference preservation", "expected": "['tasks/beads/B999-missing.md']", "actual": str(missing)})

    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        path = root / "tasks" / "beads" / "B160-example.md"
        path.parent.mkdir(parents=True)
        path.write_text(
            """---\nbead_id: B160\nstatus: ready\ndepends_on:\n  - B159\n---\n\n## Depends On\n\n- B157 is also useful context.\n""",
            encoding="utf-8",
        )
        parsed_frontmatter = read_bead(path, root).depends_on
    if parsed_frontmatter != ["B159"]:
        failures.append({"scenario": "frontmatter precedence", "expected": "['B159']", "actual": str(parsed_frontmatter)})

    return failures


def main() -> int:
    failures = run()
    print(json.dumps({"tool": "dependency-gate-check", "status": "pass" if not failures else "fail", "scenario_count": 8, "failures": failures}, indent=2, sort_keys=True))
    return 1 if failures else 0


if __name__ == "__main__":
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    raise SystemExit(main())
