#!/usr/bin/env python3
# Version: v0.1.6
# Last updated: 2026-06-14
# Owner: PrecodeOS
# Created by Dan Sears / Recode.
# SPDX-License-Identifier: Apache-2.0
from __future__ import annotations

from dataclasses import replace
from datetime import datetime, timezone
import importlib.util
import json
from pathlib import Path
from typing import Any

from os_compiler import (
    BeadRecord,
    bead_depth_quality,
    command_classification,
    completion_session_freshness,
    next_step_guidance,
    run_contract_quality,
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
    "ask for reaffirmation",
}


def load_loop_health_module() -> Any:
    path = Path(__file__).with_name("loop-health.py")
    spec = importlib.util.spec_from_file_location("loop_health", path)
    if spec is None or spec.loader is None:
        raise RuntimeError("Could not load loop-health.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


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
        run_contract={"present": False, "required": False, "required_reasons": []},
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
    run_contract: dict[str, Any] | None = None,
    goal_frame: dict[str, Any] | None = None,
) -> dict[str, Any]:
    return next_step_guidance(
        Path("."),
        {"sections": {"Open Questions": "- none"}, "current_bead": "tasks/beads/B999-clarity-fixture.md"},
        current,
        promotion or {"eligible": False, "blockers": [], "next_bead": "not recorded"},
        {"details": {"closeout_blockers": closeout_blockers or []}},
        {"details": {}},
        depth or {"status": "pass", "warnings": [], "details": {}},
        guardrail or {"status": "pass", "warnings": [], "details": {"out_of_scope_paths": []}},
        run_contract or {"status": "pass", "warnings": [], "details": {}},
        goal_frame or {"status": "pass", "warnings": [], "details": {}},
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


def assert_router_contract(name: str, payload: dict[str, Any], failures: list[dict[str, str]]) -> None:
    details = payload.get("details") or {}
    if not details.get("single_next_protocol"):
        failures.append({"scenario": f"{name} single protocol", "expected": "single_next_protocol", "actual": "missing"})
    load_plan = details.get("load_plan") or {}
    if load_plan.get("router_owner") != "scripts/next-step.py":
        failures.append({"scenario": f"{name} router owner", "expected": "scripts/next-step.py", "actual": str(load_plan.get("router_owner"))})
    footprint = details.get("context_footprint") or {}
    if "AGENT.md" not in (footprint.get("active_memory") or []):
        failures.append({"scenario": f"{name} footprint", "expected": "active memory footprint", "actual": str(footprint)})
    if footprint.get("advisory_only") is not True:
        failures.append({"scenario": f"{name} advisory", "expected": "advisory_only true", "actual": str(footprint.get("advisory_only"))})


def loop_context(**overrides: Any) -> dict[str, Any]:
    base = {
        "bead": {"checks": ["python3 scripts/version-check.py"]},
        "current_bead": "tasks/beads/B999-clarity-fixture.md",
        "status": "in_progress",
        "execution_mode": "builder",
        "bead_kind": "implementation",
        "done_when": "- One observable outcome is proven.",
        "objective": "Complete one bounded fixture.",
        "stop_if": "- Scope or proof becomes unclear.",
        "open_questions": "- none",
        "next_up": "- none",
    }
    base.update(overrides)
    return base


def loop_state(**overrides: Any) -> dict[str, Any]:
    base = {
        "changed_paths": [],
        "state_integrity": {
            "warnings": [],
            "details": {"in_progress_beads": ["tasks/beads/B999-clarity-fixture.md"]},
        },
        "files_in_play_guardrail": {"details": {"out_of_scope_paths": []}},
        "completion_handoff": {"details": {}},
        "readiness": {"current_promotion": {"eligible": False}},
        "active_bead_checks": [],
        "workflow_planning": {"warnings": []},
        "intent_orchestration": {"warnings": []},
    }
    base.update(overrides)
    return base


def loop_status(loop_health: Any, context: dict[str, Any], state: dict[str, Any]) -> str:
    dimensions = {
        "Focus": loop_health.focus_dimension(state, context),
        "Stop Condition": loop_health.stop_condition_dimension(context),
        "Closure": loop_health.closure_dimension(state, context),
        "Evidence": loop_health.evidence_dimension(state, context),
        "Leverage": loop_health.leverage_dimension(state, context),
    }
    return str(loop_health.overall_status(dimensions))


def main() -> int:
    failures: list[dict[str, str]] = []
    loop_health = load_loop_health_module()

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

    active_goal = {
        "path": "PRODUCT.md",
        "status": "active",
        "horizon": "product",
        "workflow_guidance": "PRD",
        "goal": "Keep the product direction legible before PRD shaping.",
        "requires_reaffirmation": False,
    }
    goal_frame_scenarios = [
        (
            "active current frame",
            next_payload(bead(), goal_frame={"status": "pass", "warnings": [], "details": {"current": active_goal}}),
            "continue",
            "",
        ),
        (
            "reaffirm needed",
            next_payload(
                bead(),
                goal_frame={
                    "status": "warning",
                    "warnings": ["PRODUCT.md Goal Frame requires user reaffirmation before guiding workflow"],
                    "details": {"current": {**active_goal, "status": "reaffirm_needed", "requires_reaffirmation": True}},
                },
            ),
            "ask for reaffirmation",
            "current Goal Frame requires reaffirmation before guiding workflow",
        ),
        (
            "missing fit field",
            next_payload(
                bead(),
                goal_frame={
                    "status": "warning",
                    "warnings": ["PRODUCT.md Goal Frame is missing required fields: success_signal"],
                    "details": {
                        "current": {
                            **active_goal,
                            "status": "reaffirm_needed",
                            "requires_reaffirmation": True,
                            "fit_blockers": ["PRODUCT.md Goal Frame is missing required fields: success_signal"],
                        }
                    },
                },
            ),
            "ask for reaffirmation",
            "PRODUCT.md Goal Frame is missing required fields: success_signal",
        ),
        (
            "task-like frame",
            next_payload(
                bead(),
                goal_frame={
                    "status": "warning",
                    "warnings": ["PRODUCT.md Goal Frame may be acting like a task list or roadmap (next task)"],
                    "details": {
                        "current": {
                            **active_goal,
                            "status": "reaffirm_needed",
                            "requires_reaffirmation": True,
                            "fit_blockers": [
                                "PRODUCT.md Goal Frame may be acting like a task list or roadmap (next task)"
                            ],
                        }
                    },
                },
            ),
            "ask for reaffirmation",
            "PRODUCT.md Goal Frame may be acting like a task list or roadmap",
        ),
        (
            "warnings without current frame",
            next_payload(
                bead(),
                goal_frame={
                    "status": "warning",
                    "warnings": ["PRODUCT.md Goal Frame requires user reaffirmation before guiding workflow"],
                    "details": {"current": {}},
                },
            ),
            "continue",
            "Goal Frame warnings exist, but no current active Goal Frame was selected",
        ),
    ]
    for name, payload, expected_decision, expected_warning in goal_frame_scenarios:
        details = payload.get("details") or {}
        assert_decision(f"goal-frame: {name}", str(details.get("user_decision")), expected_decision, failures)
        if expected_warning and not any(expected_warning in str(warning) for warning in payload.get("warnings") or []):
            failures.append({"scenario": f"goal-frame warning: {name}", "expected": expected_warning, "actual": str(payload.get("warnings") or [])})

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
        assert_router_contract(f"next-step router: {name}", payload, failures)

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

    run_contract_scenarios = [
        ("low risk omitted", run_contract_quality(bead(), [])["details"].get("user_decision"), "continue"),
        (
            "bounded afk missing",
            run_contract_quality(bead(autonomy_level="bounded-afk"), [])["details"].get("user_decision"),
            "stop",
        ),
        (
            "sensitive missing",
            run_contract_quality(bead(primary_authority="SECURITY.md", sections={"Objective": "Update auth.", "Stop If": "none"}), [])[
                "details"
            ].get("user_decision"),
            "stop",
        ),
        (
            "required missing proof",
            run_contract_quality(
                bead(
                    run_contract={
                        "present": True,
                        "required": True,
                        "allowed_paths": ["PROJECT-CONTEXT.md"],
                        "allowed_tool_classes": ["read_only", "verification"],
                        "proof_needed": ["manual"],
                        "approval_required_before": ["external mutation"],
                        "stop_if": ["proof unclear"],
                        "rollback_or_blocked_escape": "not applicable",
                        "expires_when": "review",
                    }
                ),
                [],
            )["details"].get("user_decision"),
            "ask for proof",
        ),
    ]
    for name, actual, expected in run_contract_scenarios:
        assert_decision(f"run-contract: {name}", str(actual), expected, failures)

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

    check_time = datetime(2026, 6, 4, 12, 0, tzinfo=timezone.utc)
    older_close = datetime(2026, 6, 4, 11, 0, tzinfo=timezone.utc)
    newer_close = datetime(2026, 6, 4, 13, 0, tzinfo=timezone.utc)
    freshness_scenarios = [
        ("open in progress", completion_session_freshness("in_progress", check_time, older_close), "open"),
        ("stale review", completion_session_freshness("review", check_time, older_close), "stale"),
        ("stale needs info", completion_session_freshness("needs_info", check_time, None), "stale"),
        ("current done", completion_session_freshness("done", check_time, newer_close), "current"),
        ("no checks", completion_session_freshness("in_progress", None, newer_close), "no-recorded-checks"),
    ]
    for name, actual, expected in freshness_scenarios:
        if actual != expected:
            failures.append({"scenario": f"completion freshness: {name}", "expected": expected, "actual": actual})

    loop_scenarios = [
        ("clear builder", loop_context(), loop_state(), "Clear"),
        ("vague done when", loop_context(done_when="- Improve the thing as needed."), loop_state(), "Watch"),
        (
            "multiple active beads",
            loop_context(),
            loop_state(state_integrity={"warnings": [], "details": {"in_progress_beads": ["B001", "B002"]}}),
            "Recenter",
        ),
        (
            "no active bead with implementation changes",
            loop_context(bead=None, current_bead="", done_when=""),
            loop_state(changed_paths=["app/page.tsx"], state_integrity={"warnings": [], "details": {"in_progress_beads": []}}),
            "Recenter",
        ),
        (
            "bounded explorer",
            loop_context(execution_mode="explorer", objective="Explore the question: which user pain matters first?"),
            loop_state(),
            "Clear",
        ),
        (
            "explorer missing question",
            loop_context(execution_mode="explorer", objective="Look around.", done_when="- Notes exist."),
            loop_state(),
            "Watch",
        ),
        ("review closeout", loop_context(status="review"), loop_state(), "Stop and Review"),
    ]
    for name, context, state, expected in loop_scenarios:
        actual = loop_status(loop_health, context, state)
        if actual != expected:
            failures.append({"scenario": f"loop-health: {name}", "expected": expected, "actual": actual})

    payload = {
        "tool": "clarity-scenario-check",
        "status": "pass" if not failures else "fail",
        "scenario_count": len(next_scenarios)
        + len(goal_frame_scenarios)
        + len(recovery_scenarios)
        + len(depth_scenarios)
        + len(run_contract_scenarios)
        + len(command_scenarios)
        + len(freshness_scenarios)
        + len(loop_scenarios),
        "stable_decisions": sorted(STABLE_DECISIONS),
        "failures": failures,
    }
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
