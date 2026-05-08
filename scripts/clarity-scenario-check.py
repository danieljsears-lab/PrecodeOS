#!/usr/bin/env python3
# Version: v0.1.1
# Last updated: 2026-05-08
# Owner: Precode OS
# Created by Dan Sears / Recode.
# SPDX-License-Identifier: Apache-2.0
from __future__ import annotations

from dataclasses import replace
import json
from typing import Any

from os_compiler import (
    BeadRecord,
    bead_depth_quality,
    command_classification,
    next_step_guidance,
)


STABLE_DECISIONS = {
    "continue",
    "ask for missing info",
    "ask for proof",
    "review",
    "approve transition",
    "repair state",
    "approval needed",
    "stop",
}


def bead(**overrides: Any) -> BeadRecord:
    base = BeadRecord(
        rel_path="tasks/beads/B999-clarity-fixture.md",
        title="B999 - Clarity Fixture",
        bead_id="B999",
        status="in_progress",
        execution_mode="single_agent",
        bead_kind="implementation",
        primary_authority="PROJECT-CONTEXT.md",
        depends_on=[],
        parent_prd="",
        requirement_ids=[],
        files_in_play=["PROJECT-CONTEXT.md"],
        checks=["python3 scripts/version-check.py"],
        verification_type=["static"],
        delegation_mode="human_in_loop",
        test_strategy="static_only",
        review_context="same_session_ok",
        complexity="",
        required_planning_depth="",
        autonomy_level="",
        closeout={},
        handback="",
        frontmatter={},
        sections={
            "Objective": "Check clarity guidance.",
            "Done When": "The decision is plain.",
            "Stop If": "Scope or proof becomes unclear.",
        },
    )
    return replace(base, **overrides)


def next_payload(
    current: BeadRecord | None,
    *,
    promotion: dict[str, Any] | None = None,
    closeout_blockers: list[str] | None = None,
    guardrail: dict[str, Any] | None = None,
    depth: dict[str, Any] | None = None,
) -> dict[str, Any]:
    return next_step_guidance(
        {"sections": {"Open Questions": "- none"}, "current_bead": "tasks/beads/B999-clarity-fixture.md"},
        current,
        promotion or {"eligible": False, "blockers": [], "next_bead": "not recorded"},
        {"details": {"closeout_blockers": closeout_blockers or []}},
        {"details": {}},
        depth or {"status": "pass", "warnings": [], "details": {}},
        guardrail or {"status": "pass", "warnings": [], "details": {"out_of_scope_paths": []}},
        {"status": "pass", "warnings": [], "details": {}},
    )


def assert_decision(name: str, actual: str, expected: str, failures: list[dict[str, str]]) -> None:
    if actual not in STABLE_DECISIONS:
        failures.append({"scenario": name, "expected": "stable decision value", "actual": actual})
    elif actual != expected:
            failures.append({"scenario": name, "expected": expected, "actual": actual})


def assert_recovery_flow(name: str, payload: dict[str, Any], expected: str, failures: list[dict[str, str]]) -> None:
    details = payload.get("details") or {}
    actual = str(details.get("recovery_flow"))
    protocol = str(details.get("recovery_protocol"))
    prompt = str(details.get("beginner_prompt"))
    if actual != expected:
        failures.append({"scenario": name, "expected": expected, "actual": actual})
    if protocol != "tasks/reference/RECOVERY-PROTOCOL.md":
        failures.append({"scenario": f"{name} protocol", "expected": "tasks/reference/RECOVERY-PROTOCOL.md", "actual": protocol})
    if expected != "none" and not prompt:
        failures.append({"scenario": f"{name} prompt", "expected": "beginner prompt", "actual": prompt})


def main() -> int:
    failures: list[dict[str, str]] = []

    next_scenarios = [
        ("missing bead", (next_payload(None)["details"] or {}).get("user_decision"), "repair state"),
        ("in progress", (next_payload(bead())["details"] or {}).get("user_decision"), "continue"),
        (
            "needs info",
            (next_payload(bead(status="needs_info"))["details"] or {}).get("user_decision"),
            "ask for missing info",
        ),
        (
            "manual testing",
            (next_payload(bead(status="manual_testing"))["details"] or {}).get("user_decision"),
            "ask for missing info",
        ),
        ("review", (next_payload(bead(status="review"))["details"] or {}).get("user_decision"), "review"),
        ("done", (next_payload(bead(status="done"))["details"] or {}).get("user_decision"), "review"),
        (
            "promotion eligible",
            (
                next_payload(
                    bead(status="done"),
                    promotion={"eligible": True, "blockers": [], "next_bead": "tasks/beads/B998-next.md"},
                )["details"]
                or {}
            ).get("user_decision"),
            "approve transition",
        ),
        (
            "closeout incomplete",
            (next_payload(bead(), closeout_blockers=["manual verification is missing"])["details"] or {}).get(
                "user_decision"
            ),
            "ask for proof",
        ),
        (
            "files outside scope",
            (
                next_payload(
                    bead(),
                    guardrail={"status": "warning", "warnings": [], "details": {"out_of_scope_paths": ["app/page.tsx"]}},
                )["details"]
                or {}
            ).get("user_decision"),
            "stop",
        ),
    ]
    for name, actual, expected in next_scenarios:
        assert_decision(f"next-step: {name}", str(actual), expected, failures)

    recovery_scenarios = [
        ("missing bead", next_payload(None), "active-state-repair"),
        ("in progress", next_payload(bead()), "none"),
        ("needs info", next_payload(bead(status="needs_info")), "blocked-work"),
        (
            "closeout incomplete",
            next_payload(bead(), closeout_blockers=["manual verification is missing"]),
            "missing-proof",
        ),
        (
            "files outside scope",
            next_payload(
                bead(),
                guardrail={"status": "warning", "warnings": [], "details": {"out_of_scope_paths": ["app/page.tsx"]}},
            ),
            "scope-expansion",
        ),
        (
            "generated report warning",
            next_payload(
                bead(),
                depth={"status": "warning", "warnings": ["generated reports appear in execution sources"], "details": {}},
            ),
            "generated-report-confusion",
        ),
    ]
    for name, payload, expected in recovery_scenarios:
        assert_recovery_flow(f"next-step recovery: {name}", payload, expected, failures)

    depth_scenarios = [
        ("omitted fields", bead_depth_quality(bead())["details"].get("user_decision"), "continue"),
        ("invalid fields", bead_depth_quality(bead(complexity="huge"))["details"].get("user_decision"), "ask for proof"),
        (
            "trivial broad scope",
            bead_depth_quality(bead(complexity="trivial", files_in_play=[f"file-{i}.md" for i in range(6)]))[
                "details"
            ].get("user_decision"),
            "ask for proof",
        ),
        (
            "sensitive weak planning",
            bead_depth_quality(
                bead(
                    title="Auth and payment migration",
                    primary_authority="SECURITY.md",
                    required_planning_depth="brief",
                    files_in_play=["SECURITY.md"],
                )
            )["details"].get("user_decision"),
            "approval needed",
        ),
        (
            "high risk weak verification",
            bead_depth_quality(bead(complexity="high-risk", required_planning_depth="PRD+architecture"))[
                "details"
            ].get("user_decision"),
            "ask for proof",
        ),
        (
            "bounded afk missing stop",
            bead_depth_quality(bead(autonomy_level="bounded-afk", sections={"Objective": "Run work."}))[
                "details"
            ].get("user_decision"),
            "ask for proof",
        ),
        (
            "human only missing gate",
            bead_depth_quality(bead(autonomy_level="human-only", sections={"Objective": "Run work.", "Stop If": "none"}))[
                "details"
            ].get("user_decision"),
            "approval needed",
        ),
    ]
    for name, actual, expected in depth_scenarios:
        assert_decision(f"adaptive-depth: {name}", str(actual), expected, failures)

    command_scenarios = [
        ("verification", command_classification("python3 scripts/version-check.py", bead()).get("user_decision"), "continue"),
        ("force push", command_classification("git push --force origin main", bead()).get("user_decision"), "stop"),
        ("hard reset", command_classification("git reset --hard HEAD~1", bead()).get("user_decision"), "stop"),
        ("delete", command_classification("rm -rf logs/check-output", bead()).get("user_decision"), "stop"),
        ("database drop", command_classification("psql -c 'drop database app'", bead()).get("user_decision"), "stop"),
        ("production deploy", command_classification("vercel deploy --prod", bead()).get("user_decision"), "approval needed"),
        ("secret access", command_classification("cat .env", bead()).get("user_decision"), "approval needed"),
        ("payments", command_classification("stripe listen --forward-to localhost", bead()).get("user_decision"), "approval needed"),
        ("auth", command_classification("edit auth permissions", bead()).get("user_decision"), "approval needed"),
        ("github mutation", command_classification("gh pr merge 12", bead()).get("user_decision"), "approval needed"),
    ]
    for name, actual, expected in command_scenarios:
        assert_decision(f"command: {name}", str(actual), expected, failures)

    payload = {
        "tool": "clarity-scenario-check",
        "status": "pass" if not failures else "fail",
        "scenario_count": len(next_scenarios) + len(recovery_scenarios) + len(depth_scenarios) + len(command_scenarios),
        "stable_decisions": sorted(STABLE_DECISIONS),
        "failures": failures,
    }
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
