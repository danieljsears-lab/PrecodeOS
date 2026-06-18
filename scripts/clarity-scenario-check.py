#!/usr/bin/env python3
# Version: v0.1.12
# Last updated: 2026-06-17
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
    stable_fix_eligibility,
)
from precode_doctor import build_doctor_dashboard


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
RECOVERY_FIXTURE_FORBIDDEN_ACTIONS = [
    "edit",
    "delete",
    "overwrite",
    "regenerate",
    "rollback",
    "setup/update mutation",
    "transition approval",
    "repair approval",
    "app-code change approval",
    "external mutation",
    "destructive command",
]


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
    stable_fix: dict[str, Any] | None = None,
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
        stable_fix or {"status": "pass", "warnings": [], "details": {}},
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


def assert_stuck_recovery_contract(failures: list[dict[str, str]]) -> None:
    required_paths = [
        Path("AGENT.md"),
        Path("docs/PRECODE-DAILY-COCKPIT.md"),
        Path("docs/PRECODE-TROUBLESHOOTING.md"),
        Path("tasks/reference/RECOVERY-PROTOCOL.md"),
        Path("docs/PRECODE-SUPPORT-RUNBOOK.md"),
        Path("tasks/reference/PROMPT-PATTERNS.md"),
    ]
    required_terms = [
        "I am stuck, help me",
        "symptom",
        "first safe move",
        "owner surface",
        "read-only or advisory checks",
        "next safe prompt or action",
        "no delete",
        "overwrite",
        "regenerate",
        "transition approval",
        "rollback",
        "setup/update mutation",
        "destructive command",
    ]
    for path in required_paths:
        text = path.read_text(encoding="utf-8")
        lower_text = text.lower()
        for term in required_terms:
            if term.lower() not in lower_text:
                failures.append({"scenario": f"stuck recovery contract: {path}", "expected": term, "actual": "missing"})


def assert_no_engineer_fallback_prompt_pack(failures: list[dict[str, str]]) -> None:
    path = Path("tasks/reference/PROMPT-PATTERNS.md")
    text = path.read_text(encoding="utf-8")
    lower_text = text.lower()
    required_terms = [
        "No-Engineer Fallback Prompt Pack",
        "Agent Is Lost",
        "Checks Failed",
        "App Will Not Start",
        "Approved Too Much",
        "Copied Wrong Files",
        "Decide Whether To Stop",
        "Recovery Protocol",
        "owner surface",
        "read-only or advisory checks",
        "next safe prompt or action",
        "Do not edit",
        "delete",
        "overwrite",
        "regenerate",
        "transition",
        "roll back",
        "setup/update behavior",
        "change app code",
        "touch secrets",
        "mutate external systems",
        "destructive command",
    ]
    for term in required_terms:
        if term.lower() not in lower_text:
            failures.append({"scenario": "no-engineer fallback prompt pack", "expected": term, "actual": "missing"})


def recovery_scenario_fixtures() -> list[dict[str, Any]]:
    base = {
        "owner_protocol": "tasks/reference/RECOVERY-PROTOCOL.md",
        "advisory_only": True,
        "synthetic_fixture": True,
        "generated_evidence_only": True,
        "repair_approval": False,
        "rollback_approval": False,
        "setup_update_approval": False,
        "transition_approval": False,
        "external_mutation_approval": False,
        "first_checks": ["python3 scripts/next-step.py"],
        "forbidden_actions": RECOVERY_FIXTURE_FORBIDDEN_ACTIONS,
    }
    return [
        {
            **base,
            "category": "wrong-folder-or-partial-setup",
            "symptom": "The user may be in the wrong folder or setup is partial.",
            "classification": "setup-confusion",
            "owner_surface": "docs/PRECODE-GUIDED-SETUP.md or tasks/reference/BOOTSTRAP-CLOSEOUT-PROTOCOL.md",
            "first_checks": [
                "python3 scripts/bootstrap-check.py --source <precode-package-root> --target <target-project-root> --recovery-guidance",
                "python3 scripts/version-check.py",
            ],
            "beginner_prompt": "Stop setup work, name the source and target folders, and use recovery guidance before copying or overwriting anything.",
        },
        {
            **base,
            "category": "copied-excluded-private-or-generated-files",
            "symptom": "The user copied private maintainer files, generated reports, logs, or excluded package material.",
            "classification": "copy-boundary-confusion",
            "owner_surface": "docs/PRECODE-PACKAGE-FILE-INVENTORY.md",
            "first_checks": [
                "python3 scripts/file-inventory.py --check",
                "python3 scripts/bootstrap-check.py --preview-manifest --source <precode-package-root> --target <target-project-root>",
            ],
            "beginner_prompt": "Stop copying, classify each path as package source, generated evidence, private maintainer material, or target-project material before repair.",
        },
        {
            **base,
            "category": "stale-or-edited-generated-report",
            "symptom": "A generated report is stale, edited by hand, missing, or being treated as truth.",
            "classification": "generated-report-confusion",
            "owner_surface": "owning source file and report-generating script",
            "first_checks": ["python3 scripts/os-health.py", "python3 scripts/state-check.py"],
            "beginner_prompt": "Repair source state first and refresh the report from its owning script; do not hand-edit generated output or treat it as authority.",
        },
        {
            **base,
            "category": "missing-proof-or-checks-failed",
            "symptom": "The user wants to continue or accept work when checks are missing or failing.",
            "classification": "missing-proof",
            "owner_surface": "tasks/reference/VERIFICATION-GUARDRAIL-PROTOCOL.md",
            "first_checks": ["python3 scripts/completion-check.py"],
            "beginner_prompt": "Name the missing or failing proof, run the declared checks, and do not accept or transition from confidence alone.",
        },
        {
            **base,
            "category": "approval-happened-too-quickly",
            "symptom": "A user may have approved too much, approved the wrong thing, or treated generated output as acceptance.",
            "classification": "approval-confusion",
            "owner_surface": "tasks/reference/SESSION-COMPLETION-HANDOFF-PROTOCOL.md",
            "first_checks": ["python3 scripts/completion-check.py", "python3 scripts/next-step.py"],
            "beginner_prompt": "Pause, review closeout evidence and transition state, then ask for accepted, revise, split, blocked, or stop.",
        },
        {
            **base,
            "category": "app-will-not-start",
            "symptom": "The target app will not start and the user cannot tell whether this is setup, app code, dependency, or environment trouble.",
            "classification": "local-app-blocker",
            "owner_surface": "docs/PRECODE-TROUBLESHOOTING.md",
            "first_checks": ["python3 scripts/next-step.py", "python3 scripts/completion-check.py"],
            "beginner_prompt": "Name the start command and error, classify whether the blocker belongs to setup, app code, dependency, or environment, and do not change app code until the owner is clear.",
        },
        {
            **base,
            "category": "auth-demo-or-support-ownership-blocker",
            "symptom": "Auth, demo, support, or secrets context is blocking progress and ownership is unclear.",
            "classification": "support-ownership-blocker",
            "owner_surface": "docs/PRECODE-SUPPORT-RUNBOOK.md",
            "first_checks": ["python3 scripts/next-step.py"],
            "beginner_prompt": "Name the missing owner, credential, demo step, or support decision; do not touch secrets or external systems while ownership is unclear.",
        },
        {
            **base,
            "category": "stop-or-continue-uncertainty",
            "symptom": "The user cannot decide whether to keep going, stop, split, or ask for help.",
            "classification": "stop-or-continue",
            "owner_surface": "tasks/reference/PROMPT-PATTERNS.md",
            "first_checks": ["python3 scripts/next-step.py", "python3 scripts/files-in-play-check.py"],
            "beginner_prompt": "Ask the agent to summarize the next safe action, forbidden next action, and whether this should continue, stop, split, or wait for approval.",
        },
    ]


def assert_recovery_scenario_harness(fixtures: list[dict[str, Any]], failures: list[dict[str, str]]) -> None:
    expected_categories = {
        "wrong-folder-or-partial-setup",
        "copied-excluded-private-or-generated-files",
        "stale-or-edited-generated-report",
        "missing-proof-or-checks-failed",
        "approval-happened-too-quickly",
        "app-will-not-start",
        "auth-demo-or-support-ownership-blocker",
        "stop-or-continue-uncertainty",
    }
    actual_categories = {str(fixture.get("category")) for fixture in fixtures}
    for category in sorted(expected_categories - actual_categories):
        failures.append({"scenario": "recovery scenario harness category", "expected": category, "actual": "missing"})

    for fixture in fixtures:
        category = str(fixture.get("category") or "unknown")
        if fixture.get("owner_protocol") != "tasks/reference/RECOVERY-PROTOCOL.md":
            failures.append(
                {
                    "scenario": f"recovery fixture protocol: {category}",
                    "expected": "tasks/reference/RECOVERY-PROTOCOL.md",
                    "actual": str(fixture.get("owner_protocol")),
                }
            )
        for key in ("advisory_only", "synthetic_fixture", "generated_evidence_only"):
            if fixture.get(key) is not True:
                failures.append({"scenario": f"recovery fixture {key}: {category}", "expected": "true", "actual": str(fixture.get(key))})
        for key in (
            "repair_approval",
            "rollback_approval",
            "setup_update_approval",
            "transition_approval",
            "external_mutation_approval",
        ):
            if fixture.get(key) is not False:
                failures.append({"scenario": f"recovery fixture {key}: {category}", "expected": "false", "actual": str(fixture.get(key))})
        first_checks = fixture.get("first_checks") if isinstance(fixture.get("first_checks"), list) else []
        if not first_checks or len(first_checks) > 3:
            failures.append({"scenario": f"recovery fixture first checks: {category}", "expected": "1-3 checks", "actual": str(first_checks)})
        for key in ("symptom", "classification", "owner_surface", "beginner_prompt"):
            if not str(fixture.get(key) or "").strip():
                failures.append({"scenario": f"recovery fixture {key}: {category}", "expected": key, "actual": "missing"})
        forbidden_actions = [str(action).lower() for action in (fixture.get("forbidden_actions") or [])]
        for action in RECOVERY_FIXTURE_FORBIDDEN_ACTIONS:
            if action.lower() not in forbidden_actions:
                failures.append({"scenario": f"recovery fixture forbidden action: {category}", "expected": action, "actual": str(forbidden_actions)})


def assert_doctor_dashboard(name: str, payload: dict[str, Any], expected_status: str, failures: list[dict[str, str]]) -> None:
    dashboard = build_doctor_dashboard(payload)
    if dashboard.get("status") != expected_status:
        failures.append({"scenario": f"doctor: {name}", "expected": expected_status, "actual": str(dashboard.get("status"))})
    if dashboard.get("next_step_decision_owner") != "scripts/next-step.py":
        failures.append(
            {
                "scenario": f"doctor owner: {name}",
                "expected": "scripts/next-step.py",
                "actual": str(dashboard.get("next_step_decision_owner")),
            }
        )
    if dashboard.get("advisory_only") is not True:
        failures.append({"scenario": f"doctor advisory: {name}", "expected": "true", "actual": str(dashboard.get("advisory_only"))})
    warning = str(dashboard.get("generated_evidence_warning") or "")
    if "generated diagnostic evidence only" not in warning:
        failures.append({"scenario": f"doctor warning: {name}", "expected": "generated evidence warning", "actual": warning})
    for key in ("top_plain_english_issue", "top_safe_ask", "top_do_not_approve", "top_validation_path"):
        if not dashboard.get(key):
            failures.append({"scenario": f"doctor triage top {key}: {name}", "expected": "plain-English triage field", "actual": "missing"})
    rows = dashboard.get("rows") if isinstance(dashboard.get("rows"), list) else []
    for row in rows:
        source = str(row.get("source") or "unknown")
        for key in (
            "plain_english_issue",
            "user_facing_meaning",
            "safe_ask",
            "do_not_approve",
            "shortest_validation_path",
        ):
            if not row.get(key):
                failures.append({"scenario": f"doctor row triage {source} {key}: {name}", "expected": "plain-English triage field", "actual": "missing"})
        if row.get("next_step_decision_owner") != "scripts/next-step.py":
            failures.append(
                {
                    "scenario": f"doctor row owner {source}: {name}",
                    "expected": "scripts/next-step.py",
                    "actual": str(row.get("next_step_decision_owner")),
                }
            )


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


def passing_checks(current: BeadRecord) -> dict[tuple[str, str], dict[str, Any]]:
    rows: dict[tuple[str, str], dict[str, Any]] = {}
    for raw in current.checks:
        command = raw.split(" -- ", 1)[1] if " -- " in raw else raw
        rows[(command, ".")] = {
            "bead": current.rel_path,
            "command": command,
            "cwd": ".",
            "status": "pass",
            "exit_code": 0,
            "timestamp": "2026-06-14T12:00:00+00:00",
            "output": "fixture",
        }
    return rows


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

    recovery_fixture_scenarios = recovery_scenario_fixtures()
    assert_recovery_scenario_harness(recovery_fixture_scenarios, failures)
    assert_stuck_recovery_contract(failures)
    assert_no_engineer_fallback_prompt_pack(failures)

    doctor_clear_payload = {
        "next_step": next_payload(bead()),
        "state_integrity": {"status": "pass", "warnings": [], "details": {"in_progress_beads": ["tasks/beads/B999-clarity-fixture.md"]}},
        "files_in_play_guardrail": {"status": "pass", "warnings": [], "details": {"out_of_scope_paths": []}},
        "bead_depth": {"status": "pass", "warnings": [], "details": {"shortest_next_action": "continue"}},
        "run_contract": {"status": "pass", "warnings": [], "details": {"required": False}},
        "completion_handoff": {"status": "pass", "warnings": [], "details": {"next_safe_action": "continue"}},
        "verification_quality": {"status": "pass", "warnings": [], "details": {}},
        "local_hygiene": {"status": "pass", "warnings": [], "details": {"next_safe_action": "review candidates only"}},
        "work_graph": {"status": "pass", "warnings": [], "details": {}},
        "tool_execution": {"status": "pass", "warnings": [], "details": {"approval_gap_count": 0, "destructive_count": 0}},
    }
    doctor_review_payload = {
        **doctor_clear_payload,
        "next_step": next_payload(
            bead(status="done"),
            promotion={"eligible": True, "blockers": [], "next_bead": "tasks/beads/B998-next.md"},
        ),
        "completion_handoff": {
            "status": "pass",
            "warnings": [],
            "details": {"promotion_status": "eligible", "closeout_status": "complete", "next_safe_action": "Review evidence before transition."},
        },
    }
    doctor_scope_payload = {
        **doctor_clear_payload,
        "files_in_play_guardrail": {
            "status": "warning",
            "warnings": ["Changed files appear outside the active bead files in play."],
            "details": {"out_of_scope_paths": ["app/page.tsx"], "user_decision": "stop"},
        },
    }
    assert_doctor_dashboard("clear", doctor_clear_payload, "clear", failures)
    assert_doctor_dashboard("transition review", doctor_review_payload, "stop_review", failures)
    assert_doctor_dashboard("scope drift", doctor_scope_payload, "drift_risk", failures)

    stable_fix_fixture = bead(
        title="B999 - Stable Fix Fixture",
        bead_kind="bugfix",
        primary_authority="tasks/reference/RECOVERY-PROTOCOL.md",
        files_in_play=["tasks/reference/RECOVERY-PROTOCOL.md"],
        checks=["bash scripts/validate-memory.sh"],
        verification_type=["static"],
        sections={
            "Objective": "Apply a narrow stable fix to repair a broken link.",
            "Done When": "The narrow fix is validated.",
            "Stop If": "The fix changes behavior or expands beyond the owner file.",
        },
    )
    stable_fix_scenarios = [
        (
            "narrow tested source repair",
            stable_fix_eligibility(stable_fix_fixture, passing_checks(stable_fix_fixture)),
            "eligible_stable_fix",
            "current_bead",
            True,
        ),
        (
            "missing evidence",
            stable_fix_eligibility(stable_fix_fixture, {}),
            "needs_evidence",
            "VERIFICATION-GUARDRAIL-PROTOCOL",
            False,
        ),
        (
            "active-state repair",
            stable_fix_eligibility(
                bead(
                    title="B999 - Active State Repair",
                    bead_kind="unblocker",
                    primary_authority="tasks/reference/RECOVERY-PROTOCOL.md",
                    files_in_play=["tasks/todo.md"],
                    checks=["bash scripts/validate-memory.sh"],
                    sections={
                        "Objective": "Repair broken active state after generated report confusion.",
                        "Done When": "State is coherent.",
                        "Stop If": "Owner file is unclear.",
                    },
                ),
                {},
            ),
            "recovery_repair",
            "RECOVERY-PROTOCOL",
            False,
        ),
        (
            "release relevant",
            stable_fix_eligibility(
                bead(
                    title="B999 - User Facing Stable Fix",
                    bead_kind="bugfix",
                    primary_authority="tasks/reference/RELEASE-READINESS-PROTOCOL.md",
                    files_in_play=["app/page.tsx"],
                    checks=["npm test"],
                    sections={
                        "Objective": "Apply a narrow stable fix to a user-facing page before release.",
                        "Done When": "The page behavior is validated.",
                        "Stop If": "Release evidence is unclear.",
                    },
                ),
                passing_checks(bead(checks=["npm test"])),
            ),
            "broader_change",
            "RELEASE-READINESS-PROTOCOL",
            False,
        ),
        (
            "sensitive mutation",
            stable_fix_eligibility(
                bead(
                    title="B999 - Auth Stable Fix",
                    bead_kind="bugfix",
                    primary_authority="SECURITY.md",
                    files_in_play=["SECURITY.md"],
                    checks=["python3 scripts/version-check.py"],
                    sections={
                        "Objective": "Apply a narrow stable fix to auth permissions.",
                        "Done When": "Security guidance is validated.",
                        "Stop If": "Approval is missing.",
                    },
                ),
                passing_checks(bead(checks=["python3 scripts/version-check.py"])),
            ),
            "broader_change",
            "PRD/bead",
            False,
        ),
    ]
    for name, payload, expected_classification, expected_route, expected_eligible in stable_fix_scenarios:
        details = payload.get("details") or {}
        if details.get("classification") != expected_classification:
            failures.append(
                {
                    "scenario": f"stable-fix: {name}",
                    "expected": expected_classification,
                    "actual": str(details.get("classification")),
                }
            )
        if details.get("required_route") != expected_route:
            failures.append(
                {
                    "scenario": f"stable-fix route: {name}",
                    "expected": expected_route,
                    "actual": str(details.get("required_route")),
                }
            )
        if details.get("eligible") is not expected_eligible:
            failures.append(
                {
                    "scenario": f"stable-fix eligible: {name}",
                    "expected": str(expected_eligible),
                    "actual": str(details.get("eligible")),
                }
            )

    depth_scenarios = [
        (
            "proportional tiny bead",
            bead_depth_quality(
                bead(
                    complexity="trivial",
                    required_planning_depth="none",
                    autonomy_level="supervised",
                    files_in_play=["README.md"],
                    verification_type=["static"],
                )
            )["details"].get("user_decision"),
            "continue",
        ),
        ("omitted fields", bead_depth_quality(bead())["details"].get("user_decision"), "continue"),
        ("invalid fields", bead_depth_quality(bead(complexity="huge"))["details"].get("user_decision"), "ask for proof"),
        (
            "tiny over ceremony",
            bead_depth_quality(
                bead(
                    complexity="trivial",
                    required_planning_depth="PRD+architecture",
                    files_in_play=["README.md"],
                    verification_type=["static"],
                )
            )["details"].get("user_decision"),
            "ask for proof",
        ),
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
            "high risk weak planning",
            bead_depth_quality(bead(complexity="high-risk", required_planning_depth="brief", verification_type=["manual"]))[
                "details"
            ].get("user_decision"),
            "ask for proof",
        ),
        (
            "high risk weak verification",
            bead_depth_quality(bead(complexity="high-risk", required_planning_depth="PRD+architecture"))[
                "details"
            ].get("user_decision"),
            "ask for proof",
        ),
        (
            "multi system weak verification",
            bead_depth_quality(
                bead(
                    complexity="multi-system",
                    required_planning_depth="PRD+architecture+test-plan",
                    files_in_play=[f"file-{i}.md" for i in range(21)],
                    verification_type=["static"],
                )
            )["details"].get("user_decision"),
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
        ("local edit", command_classification("apply_patch update app/page.tsx", bead()).get("user_decision"), "continue"),
        ("dependency install", command_classification("npm install lucide-react", bead()).get("user_decision"), "continue"),
        ("dependency add", command_classification("pnpm add zod", bead()).get("user_decision"), "continue"),
        ("force push", command_classification("git push --force origin main", bead()).get("user_decision"), "stop"),
        ("hard reset", command_classification("git reset --hard HEAD~1", bead()).get("user_decision"), "stop"),
        ("git restore", command_classification("git restore app/page.tsx", bead()).get("user_decision"), "stop"),
        ("delete", command_classification("rm -rf logs/check-output", bead()).get("user_decision"), "stop"),
        ("database drop", command_classification("psql -c 'drop database app'", bead()).get("user_decision"), "stop"),
        ("migration reset", command_classification("prisma migrate reset", bead()).get("user_decision"), "stop"),
        ("database migration", command_classification("prisma migrate deploy", bead()).get("user_decision"), "approval needed"),
        ("production deploy", command_classification("vercel deploy --prod", bead()).get("user_decision"), "approval needed"),
        ("git push", command_classification("git push origin feature-branch", bead()).get("user_decision"), "approval needed"),
        ("release publish", command_classification("npm publish", bead()).get("user_decision"), "approval needed"),
        ("secret access", command_classification("cat .env", bead()).get("user_decision"), "approval needed"),
        ("api key access", command_classification("print API key from dashboard", bead()).get("user_decision"), "approval needed"),
        ("payments", command_classification("stripe listen --forward-to localhost", bead()).get("user_decision"), "approval needed"),
        ("auth", command_classification("edit auth permissions", bead()).get("user_decision"), "approval needed"),
        ("github mutation", command_classification("gh pr merge 12", bead()).get("user_decision"), "approval needed"),
        (
            "sensitive bead local mutation",
            command_classification("npm install auth-helper", bead(primary_authority="SECURITY.md", files_in_play=["SECURITY.md"])).get(
                "user_decision"
            ),
            "approval needed",
        ),
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
        + len(recovery_fixture_scenarios)
        + len(stable_fix_scenarios)
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
