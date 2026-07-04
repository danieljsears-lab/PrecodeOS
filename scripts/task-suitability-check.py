#!/usr/bin/env python3
# Version: v0.1.0
# Last updated: 2026-07-04
# Owner: PrecodeOS
# Created by Dan Sears / Recode.
# SPDX-License-Identifier: Apache-2.0
from __future__ import annotations

import argparse
import json
from typing import Any

from os_compiler import _task_suitability_payload_from_values, compile_state, repo_root


def scenario(
    name: str,
    expected: str,
    **overrides: Any,
) -> dict[str, Any]:
    base = {
        "current_bead": "tasks/beads/B999-task-suitability-fixture.md",
        "status": "in_progress",
        "bead_kind": "implementation",
        "primary_authority": "tasks/prds/PRD-999-fixture.md",
        "parent_prd": "tasks/prds/PRD-999-fixture.md",
        "requirement_ids": ["PRD-999-FR01"],
        "files_in_play": ["src/fixture.py", "tests/test_fixture.py"],
        "checks": ["python3 -m pytest tests/test_fixture.py"],
        "verification_type": ["unit"],
        "stop_text": "Stop if proof, scope, or approval becomes unclear.",
        "done_when": "One fixture behavior is implemented and proven.",
        "objective": "Implement one fixture behavior.",
        "depends_on": [],
        "run_contract": {"present": False, "required": False},
    }
    base.update(overrides)
    payload = _task_suitability_payload_from_values(**base)
    actual = payload.get("details", {}).get("suitability_decision")
    return {
        "name": name,
        "expected": expected,
        "actual": actual,
        "pass": actual == expected,
        "warnings": payload.get("warnings", []),
    }


def self_test() -> dict[str, Any]:
    scenarios = [
        scenario("continue ready", "continue"),
        scenario("clarify missing proof", "clarify", checks=[], verification_type=[]),
        scenario(
            "route implementation without PRD",
            "route",
            parent_prd="",
            requirement_ids=[],
        ),
        scenario(
            "split broad done when",
            "split",
            done_when="Build the settings page and then wire billing and then add reports.",
        ),
        scenario("block missing active bead", "block", current_bead="missing", status="missing"),
        scenario(
            "stop generated authority",
            "stop",
            primary_authority="logs/work-graph.md",
        ),
        scenario(
            "route sensitive approval",
            "route",
            primary_authority="SECURITY.md",
            objective="Update auth and payment migration behavior.",
            files_in_play=["SECURITY.md", "src/auth.py"],
            checks=["python3 scripts/version-check.py"],
            stop_text="Stop if scope or proof becomes unclear.",
        ),
    ]
    failures = [item for item in scenarios if not item["pass"]]
    return {
        "tool": "task-suitability-check",
        "mode": "self-test",
        "status": "fail" if failures else "pass",
        "scenario_count": len(scenarios),
        "advisory_only": True,
        "scenarios": scenarios,
        "failures": failures,
        "generated_report_warning": (
            "Task suitability self-test output is generated evidence only; it does not choose work, "
            "approve PRDs, activate beads, authorize implementation, accept review, approve commands, or create proof."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="print advisory task-suitability findings for the current Precode state")
    parser.add_argument("--self-test", action="store_true", help="run deterministic task-suitability fixture checks")
    args = parser.parse_args()

    if args.self_test:
        payload = self_test()
        print(json.dumps(payload, indent=2, sort_keys=True))
        return 0 if payload["status"] == "pass" else 1

    payload = compile_state(repo_root()).get("task_suitability") or {
        "status": "warning",
        "warnings": ["task suitability unavailable"],
        "advisory_only": True,
        "details": {"suitability_decision": "stop"},
        "recommended_next_safe_action": "Stop until task suitability can be inspected.",
        "generated_report_warning": (
            "Task suitability output is generated evidence only; it does not choose work, approve PRDs, "
            "activate beads, authorize implementation, accept review, approve commands, or create proof."
        ),
    }
    print(json.dumps({"tool": "task-suitability-check", **payload}, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
