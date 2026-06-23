#!/usr/bin/env python3
# Version: v0.1.0
# Last updated: 2026-06-23
# Owner: PrecodeOS
# Created by Dan Sears / Recode.
# SPDX-License-Identifier: Apache-2.0
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from os_compiler import compile_state, repo_root, session_friction_review
from precode_state import load_jsonl


def build_payload(root: Path) -> dict[str, Any]:
    state = compile_state(root)
    return session_friction_review(
        root,
        load_jsonl(root / "logs" / "tool-runs.jsonl"),
        load_jsonl(root / "logs" / "check-results.jsonl"),
        load_jsonl(root / "logs" / "loop-runs.jsonl"),
        state.get("tool_execution") or {},
        state.get("completion_handoff") or {},
        state.get("memory") or {},
    )


def self_test(root: Path) -> dict[str, Any]:
    failures: list[dict[str, str]] = []
    tool_rows = [
        {
            "timestamp": "2026-06-23T10:00:00+00:00",
            "tool": "shell",
            "class": "read_only",
            "status": "fail",
            "command": "missing-tool --version",
            "task": "tasks/beads/B000-install-precode-kernel.md",
            "failure_category": "unavailable_command",
            "output_ref": "safe summary",
        },
        {
            "timestamp": "2026-06-23T10:01:00+00:00",
            "tool": "shell",
            "class": "read_only",
            "status": "fail",
            "command": "missing-helper --help",
            "task": "tasks/beads/B000-install-precode-kernel.md",
            "failure_category": "unavailable_command",
        },
        {
            "timestamp": "2026-06-23T10:02:00+00:00",
            "tool": "shell",
            "class": "read_only",
            "status": "blocked",
            "command": "network command",
            "task": "tasks/beads/B000-install-precode-kernel.md",
            "failure_category": "permission_or_sandbox_blocked",
        },
        {
            "timestamp": "2026-06-23T10:03:00+00:00",
            "tool": "shell",
            "class": "read_only",
            "status": "fail",
            "command": "unknown failure",
            "task": "tasks/beads/B000-install-precode-kernel.md",
        },
    ]
    payload = session_friction_review(
        root,
        tool_rows,
        [{"timestamp": "2026-06-23T09:00:00+00:00", "status": "pass", "command": "python3 old-check.py"}],
        [{"timestamp": "2026-06-23T08:00:00+00:00", "action": "session-close"}],
        {
            "status": "warning",
            "warnings": ["generated reports were refreshed for active work but no verification evidence exists"],
            "details": {"latest_failure": tool_rows[-1]},
        },
        {"status": "warning", "warnings": ["session close evidence is stale"], "details": {}},
        {
            "status": "warning",
            "warnings": ["reviewed memory card is over token budget"],
            "details": {"memory_card_count": 2},
        },
    )
    findings = payload.get("details", {}).get("findings") or []
    categories = {finding.get("category") for finding in findings}
    expected_categories = {
        "repeated_failure_category",
        "missing_failure_category",
        "unavailable_command_or_dependency",
        "sandbox_or_approval_block",
        "stale_check_or_closeout_evidence",
        "generated_refresh_without_verification",
        "over_broad_context_or_memory_pressure",
    }
    for category in expected_categories:
        if category not in categories:
            failures.append({"scenario": "fixture category", "expected": category, "actual": str(sorted(categories))})
    for finding in findings:
        for field in [
            "category",
            "source_refs",
            "confidence",
            "freshness",
            "recommended_destination",
            "suggested_next_step",
            "forbidden_uses",
        ]:
            if field not in finding:
                failures.append({"scenario": f"finding field: {finding.get('category')}", "expected": field, "actual": "missing"})
        forbidden = " ".join(finding.get("forbidden_uses") or [])
        for term in ["task selection", "memory promotion", "owner-file edits"]:
            if term not in forbidden:
                failures.append({"scenario": f"forbidden use: {finding.get('category')}", "expected": term, "actual": forbidden})

    empty_payload = session_friction_review(root, [], [], [], {}, {}, {})
    empty_categories = {finding.get("category") for finding in empty_payload.get("details", {}).get("findings") or []}
    if "no_safe_evidence_found" not in empty_categories:
        failures.append({"scenario": "empty evidence", "expected": "no_safe_evidence_found", "actual": str(sorted(empty_categories))})

    return {
        "tool": "session-friction-check",
        "mode": "self-test",
        "status": "pass" if not failures else "fail",
        "scenario_count": len(expected_categories) + 1,
        "failures": failures,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Show read-only Session Friction Review advisory findings.")
    parser.add_argument("--self-test", action="store_true", help="run deterministic session-friction fixture checks")
    args = parser.parse_args()

    root = repo_root()
    payload = self_test(root) if args.self_test else {"tool": "session-friction-check", **build_payload(root)}
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0 if payload.get("status") == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
