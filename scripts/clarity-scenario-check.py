#!/usr/bin/env python3
# Version: v0.1.29
# Last updated: 2026-06-29
# Owner: PrecodeOS
# Created by Dan Sears / Recode.
# SPDX-License-Identifier: Apache-2.0
from __future__ import annotations

from dataclasses import replace
from datetime import datetime, timezone
from contextlib import redirect_stderr, redirect_stdout
import importlib.util
import io
import json
from pathlib import Path
from typing import Any

from os_compiler import (
    BeadRecord,
    accessibility_advisory_gate_quality,
    bead_depth_quality,
    build_attribution_ledger,
    command_classification,
    completion_session_freshness,
    next_step_guidance,
    reference_followthrough_quality,
    release_evidence_quality,
    reversal_workflow_quality,
    run_contract_quality,
    session_friction_review,
    stable_fix_eligibility,
    team_collaboration_preview,
)
from precode_doctor import build_doctor_dashboard


def load_prd_handoff_module() -> Any:
    path = Path(__file__).resolve().parent / "prd-handoff-readiness.py"
    spec = importlib.util.spec_from_file_location("prd_handoff_readiness", path)
    if spec is None or spec.loader is None:
        raise RuntimeError("Could not load prd-handoff-readiness.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


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
ROUTER_DECISION_CATEGORIES = {
    "state-repair",
    "scope-repair",
    "transition-approval",
    "review",
    "closeout",
    "unblock",
    "execute",
    "depth-review",
    "run-contract-review",
    "goal-reaffirmation",
}
ROUTER_TOP_LEVEL_KEYS = {
    "status",
    "warnings",
    "stable_fix_eligibility",
    "details",
}
ROUTER_DETAILS_KEYS = {
    "current_bead",
    "current_bead_status",
    "recommended_action",
    "action_category",
    "plain_english_summary",
    "user_decision",
    "single_next_protocol",
    "load_plan",
    "context_footprint",
    "stop_if",
    "approval_prompt",
    "needs_review",
    "needs_transition",
    "stable_fix_eligibility",
    "recovery_flow",
    "recovery_protocol",
    "beginner_prompt",
    "advisory_only",
}
ROUTER_LOAD_PLAN_KEYS = {
    "required_first",
    "then_load",
    "single_next_protocol",
    "router_owner",
    "decision_category",
}
ROUTER_CONTEXT_FOOTPRINT_KEYS = {
    "advisory_only",
    "active_memory",
    "required_context",
    "conditional_references",
    "generated_reports_touched",
    "approx_document_lines",
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


def load_script_module(module_name: str, filename: str) -> Any:
    path = Path(__file__).with_name(filename)
    spec = importlib.util.spec_from_file_location(module_name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Could not load {filename}")
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


def assert_required_keys(
    name: str,
    actual: dict[str, Any],
    expected_keys: set[str],
    failures: list[dict[str, str]],
) -> None:
    missing = sorted(key for key in expected_keys if key not in actual)
    if missing:
        failures.append({"scenario": name, "expected": f"required keys: {missing}", "actual": str(sorted(actual.keys()))})


def assert_router_contract(
    name: str,
    payload: dict[str, Any],
    failures: list[dict[str, str]],
    expected_category: str | None = None,
) -> None:
    assert_required_keys(f"{name} top-level shape", payload, ROUTER_TOP_LEVEL_KEYS, failures)
    if payload.get("status") not in {"pass", "warning"}:
        failures.append({"scenario": f"{name} status", "expected": "pass or warning", "actual": str(payload.get("status"))})
    if not isinstance(payload.get("warnings"), list):
        failures.append({"scenario": f"{name} warnings", "expected": "list", "actual": str(type(payload.get("warnings")).__name__)})
    details = payload.get("details") or {}
    assert_required_keys(f"{name} details shape", details, ROUTER_DETAILS_KEYS, failures)
    category = str(details.get("action_category") or "")
    if category not in ROUTER_DECISION_CATEGORIES:
        failures.append({"scenario": f"{name} category", "expected": "stable router category", "actual": category})
    if expected_category and category != expected_category:
        failures.append({"scenario": f"{name} category", "expected": expected_category, "actual": category})
    if details.get("advisory_only") is not True:
        failures.append({"scenario": f"{name} details advisory", "expected": "advisory_only true", "actual": str(details.get("advisory_only"))})
    if str(details.get("user_decision") or "") not in STABLE_DECISIONS:
        failures.append({"scenario": f"{name} user decision", "expected": "stable decision value", "actual": str(details.get("user_decision"))})
    if payload.get("stable_fix_eligibility") is None or details.get("stable_fix_eligibility") is None:
        failures.append({"scenario": f"{name} stable fix shape", "expected": "top-level and details stable_fix_eligibility", "actual": str(payload)})
    if not details.get("single_next_protocol"):
        failures.append({"scenario": f"{name} single protocol", "expected": "single_next_protocol", "actual": "missing"})
    load_plan = details.get("load_plan") or {}
    assert_required_keys(f"{name} load plan shape", load_plan, ROUTER_LOAD_PLAN_KEYS, failures)
    if load_plan.get("router_owner") != "scripts/next-step.py":
        failures.append({"scenario": f"{name} router owner", "expected": "scripts/next-step.py", "actual": str(load_plan.get("router_owner"))})
    if load_plan.get("single_next_protocol") != details.get("single_next_protocol"):
        failures.append({"scenario": f"{name} load plan protocol", "expected": str(details.get("single_next_protocol")), "actual": str(load_plan.get("single_next_protocol"))})
    if load_plan.get("decision_category") != category:
        failures.append({"scenario": f"{name} load plan category", "expected": category, "actual": str(load_plan.get("decision_category"))})
    footprint = details.get("context_footprint") or {}
    assert_required_keys(f"{name} context footprint shape", footprint, ROUTER_CONTEXT_FOOTPRINT_KEYS, failures)
    if "AGENT.md" not in (footprint.get("active_memory") or []):
        failures.append({"scenario": f"{name} footprint", "expected": "active memory footprint", "actual": str(footprint)})
    if footprint.get("advisory_only") is not True:
        failures.append({"scenario": f"{name} advisory", "expected": "advisory_only true", "actual": str(footprint.get("advisory_only"))})
    if "logs/next-step.json" not in (footprint.get("generated_reports_touched") or []):
        failures.append({"scenario": f"{name} generated reports", "expected": "logs/next-step.json", "actual": str(footprint.get("generated_reports_touched"))})


def assert_session_start_router_delegation(failures: list[dict[str, str]]) -> None:
    text = Path("scripts/session-start.sh").read_text(encoding="utf-8")
    router_label = text.find('echo "Router Decision:"')
    next_step_call = text.find("python3 scripts/next-step.py")
    if router_label == -1:
        failures.append({"scenario": "session-start router display", "expected": "Router Decision label", "actual": "missing"})
    if next_step_call == -1:
        failures.append({"scenario": "session-start router delegation", "expected": "python3 scripts/next-step.py", "actual": "missing"})
    elif router_label != -1 and next_step_call < router_label:
        failures.append({"scenario": "session-start router delegation order", "expected": "next-step after Router Decision label", "actual": text[router_label:next_step_call]})


def assert_daily_prompt_alias_contract(failures: list[dict[str, str]]) -> int:
    required_terms_by_path = {
        Path("docs/PRECODE-DAILY-COCKPIT.md"): [
            "Quick Daily Loop",
            "Lean prompt alias",
            "active memory and owner files stay authoritative",
            "generated reports stay evidence only",
            "explicit approval is still required",
            "Start: run the Precode session start",
            "Choose: use Workflow Selection",
            "Confirm: name the active bead",
            "Build: work only on the active bead",
            "Prove: show recorded evidence",
            "Close: run session close",
            "I am stuck, help me.",
            "Fallback: use the No-Engineer Fallback Prompt Pack",
        ],
        Path("tasks/reference/PROMPT-PATTERNS.md"): [
            "Daily Prompt Aliases",
            "Alias guardrail floor",
            "must not become command-wrapper behavior",
            "Treat generated reports, logs, source notes, screenshots, transcripts, imported issues, handoffs, journals, ledgers, and previews as evidence only",
            "Start: run the Precode session start",
            "Choose: use Workflow Selection",
            "Build: work only on the active bead",
            "Close: run session close",
            "No-Engineer Fallback Prompt Pack",
        ],
        Path("tasks/reference/SKILL-PLAYBOOK-PROTOCOL.md"): [
            "Daily Prompt Alias Boundary",
            "Start, Choose, Confirm, Build, Prove, Close, Recover, and Fallback",
            "not command wrappers",
            "v1 remains prompt playbook first",
        ],
        Path("docs/PRECODE-PACKAGE-FILE-INVENTORY.md"): [
            "Daily Prompt Alias Boundary",
            "Daily Prompt Aliases",
            "compact invocation shorthand",
            "expanded backing catalog",
        ],
    }
    for path, required_terms in required_terms_by_path.items():
        text = path.read_text(encoding="utf-8")
        for term in required_terms:
            if term not in text:
                failures.append({"scenario": f"daily prompt alias contract: {path}", "expected": term, "actual": "missing"})
    return len(required_terms_by_path)


def assert_artifact_chooser_contract(failures: list[dict[str, str]]) -> int:
    required_terms_by_path = {
        Path("tasks/reference/PROMPT-PATTERNS.md"): [
            "Artifact Chooser",
            "Use this chooser when the user knows the kind of moment they are in",
            "If the next step depends on active memory, the active bead, current repo state, generated reports, local errors, or what work should happen next, use Workflow Selection before choosing an artifact.",
            "First PRD Walkthrough",
            "Local Source Intake",
            "PRD Shaping",
            "Candidate Queue",
            "Bugfix Spec Lane",
            "Review Lanes",
            "PRD Handoff Readiness Packet",
            "Release Candidate Evidence Profile",
            "Small Team Collaboration Lane",
            "Recovery Protocol or No-Engineer Fallback Prompt Pack",
            "Do not create a template registry, marketplace, optional pack, package-manager behavior, hidden task selector, automatic artifact generator",
        ],
        Path("docs/PRECODE-USER-GUIDE.md"): [
            "Choose The Right Artifact",
            "start with the Artifact Chooser",
            "Use it as an index, not as task approval.",
            "If the choice depends on active memory, the active bead, current repo state, generated reports, local errors, or what work should happen next, ask for Workflow Selection instead.",
        ],
        Path("docs/PRECODE-DAILY-COCKPIT.md"): [
            "Which artifact or prompt do I need?",
            "Choose artifact",
            "Use the Precode Artifact Chooser",
            "Artifact or prompt routing without task approval, artifact generation, PRD approval, bead activation, or implementation permission.",
        ],
        Path("tasks/reference/SKILL-PLAYBOOK-PROTOCOL.md"): [
            "Artifact Chooser Boundary",
            "prompt-catalog index",
            "not a skill playbook, command wrapper, template registry, marketplace, optional pack, package manager, hidden task selector, automatic artifact generator",
            "does not approve PRDs, activate beads, accept review, approve release, choose work, or promote generated prompt output into authority",
        ],
        Path("tasks/reference/EXTENSION-PROTOCOL.md"): [
            "The Artifact Chooser in `tasks/reference/PROMPT-PATTERNS.md` is an index over existing prompts and artifacts, not an extension type.",
            "Do not treat it as a template registry, marketplace, optional pack, package manager, hidden task selector, automatic artifact generator, skill playbook, command wrapper, or approval surface.",
        ],
        Path("docs/PRECODE-PACKAGE-FILE-INVENTORY.md"): [
            "Artifact Chooser Boundary",
            "Product Artifact Template / Prompt Catalog requirements",
            "prompt-catalog navigation",
            "does not choose tasks, approve PRDs, activate beads, accept implementation, generate artifacts automatically, create a template registry or marketplace, install optional packs, or imply package-manager behavior",
        ],
    }
    for path, required_terms in required_terms_by_path.items():
        text = path.read_text(encoding="utf-8")
        for term in required_terms:
            if term not in text:
                failures.append({"scenario": f"artifact chooser contract: {path}", "expected": term, "actual": "missing"})
    return len(required_terms_by_path)


def assert_onboarding_authority_consolidation_contract(failures: list[dict[str, str]]) -> int:
    required_terms_by_path = {
        Path("README.md"): [
            "This README is the public package compass",
            "not the daily operating surface once work has started",
            "use [`PRECODE-DAILY-COCKPIT.md`](docs/PRECODE-DAILY-COCKPIT.md) as the practical first working surface",
            "First PRD: use First PRD Walkthrough for my rough idea.",
        ],
        Path("docs/PRECODE-DAILY-COCKPIT.md"): [
            "Use this cockpit first once PrecodeOS is installed or you are already working inside a PrecodeOS repo.",
            "this cockpit is the beginner-facing operating home base",
            "I only have a rough idea.",
            "The single beginner-facing path through Product Ideation Workbook, Precode Idea Coach, Product Brief, Challenge And Clarity, Conviction Packet, Local Source Intake, and PRD shaping.",
            "These are steps in the path, not competing commands.",
        ],
        Path("docs/PRECODE-OS-README.md"): [
            "This document explains the model.",
            "It is not the daily start page",
            "use `../README.md` as the public compass, `PRECODE-GUIDED-SETUP.md` for setup, and `PRECODE-DAILY-COCKPIT.md` as the first working surface after setup.",
            "First PRD Walkthrough for rough idea to PRD readiness",
            "Treat it as the only user-facing rough-idea route.",
        ],
        Path("docs/PRECODE-USER-GUIDE.md"): [
            "For day-to-day work, start with `docs/PRECODE-DAILY-COCKPIT.md`.",
            "This guide is the deeper operating manual",
            "Do not treat this guide as a second start page.",
            "Rough ideas go to First PRD Walkthrough.",
            "ordered steps, not competing commands",
            "start with First PRD Walkthrough",
        ],
        Path("docs/HOW-TO-BUILD-SOFTWARE-WITH-PRECODE.md"): [
            "Use First PRD Walkthrough when you want the shortest safe route from rough idea to PRD readiness.",
            "Product Ideation Workbook and Precode Idea Coach as ordered steps",
            "Use First PRD Walkthrough for my rough idea. Start with the Product Ideation Workbook and Precode Idea Coach steps",
        ],
        Path("tasks/reference/WORKFLOW-SELECTION-PROTOCOL.md"): [
            "| First-time non-technical builder has a rough idea before repo setup or asks for First PRD Walkthrough | First PRD Walkthrough |",
            "Product Ideation Workbook, Precode Idea Coach, Product Brief, Challenge And Clarity, Conviction Packet, Local Source Intake, and PRD shaping are steps inside that route, not competing commands for the same moment.",
        ],
        Path("tasks/reference/PROMPT-PATTERNS.md"): [
            "| Rough idea before a repo exists | First PRD Walkthrough |",
            "Precode Idea Coach is the guided interview step inside First PRD Walkthrough.",
            "This is the single beginner-facing path name for rough idea to PRD readiness.",
            "Use the Product Ideation Workbook and Precode Idea Coach as ordered steps inside that path.",
        ],
        Path("tasks/reference/PRD-PROTOCOL.md"): [
            "Idea -> Brief -> Packet -> Intake -> PRD -> Bead -> Proof -> Review -> Close",
            "Start with First PRD Walkthrough, using Product Ideation Workbook and Precode Idea Coach as ordered steps",
            "Use \"First PRD Walkthrough\" as the plain-language request for this ramp",
        ],
        Path("tasks/reference/IDEA-TO-PRD-WORKFLOW.md"): [
            "First PRD Walkthrough -> Product Ideation Workbook step -> Precode Idea Coach guided interview",
            "The First PRD Walkthrough is the named beginner route, not a new protocol or shortcut.",
            "Use First PRD Walkthrough, with Product Ideation Workbook and Precode Idea Coach as ordered steps",
        ],
        Path("tasks/reference/SKILL-PLAYBOOK-PROTOCOL.md"): [
            "Product Conviction Packet Skill is the skill-playbook form of the coaching step inside First PRD Walkthrough.",
            "Use First PRD Walkthrough as the beginner-facing rough-idea path name",
        ],
        Path("docs/PRECODE-PACKAGE-FILE-INVENTORY.md"): [
            "Daily Cockpit as the first working surface",
            "beginner-facing operating home base",
            "Deeper hands-on operating manual",
            "First PRD Walkthrough when a first-time rough idea needs pre-repo product thinking",
            "Product Ideation Workbook, Precode Idea Coach, Product Brief, Challenge And Clarity, Conviction Packet, Local Source Intake, and PRD shaping as ordered support inside that path",
        ],
        Path("llms.txt"): [
            "beginner-facing operating home base, rough-idea entry prompt, first-product spine, and safe next prompts",
            "conceptual Builder OS explainer",
            "deeper operating manual behind the Daily Cockpit",
            "setup-only adoption path before normal work starts",
        ],
    }
    for path, required_terms in required_terms_by_path.items():
        text = path.read_text(encoding="utf-8")
        for term in required_terms:
            if term not in text:
                failures.append({"scenario": f"onboarding authority consolidation: {path}", "expected": term, "actual": "missing"})

    readme = Path("README.md").read_text(encoding="utf-8")
    start_here = readme.split("## Start Here", 1)[1].split("## How PrecodeOS Works", 1)[0]
    ordered_markers = [
        "This README is the public package compass",
        "PRECODE-GUIDED-SETUP.md",
        "PRECODE-DAILY-COCKPIT.md",
        "PRECODE-USER-GUIDE.md",
        "PRECODE-OS-README.md",
    ]
    positions = [start_here.find(marker) for marker in ordered_markers]
    if any(position == -1 for position in positions) or positions != sorted(positions):
        failures.append({"scenario": "onboarding authority consolidation: README order", "expected": "setup -> Daily Cockpit -> User Guide -> OS README", "actual": str(positions)})

    forbidden_terms_by_path = {
        Path("tasks/reference/PROMPT-PATTERNS.md"): [
            "First PRD Walkthrough or Precode Idea Coach",
            "Product Ideation Workbook / Precode Idea Coach",
        ],
        Path("tasks/reference/WORKFLOW-SELECTION-PROTOCOL.md"): [
            "Product Ideation Workbook or Product Conviction Packet Skill",
        ],
        Path("docs/PRECODE-USER-GUIDE.md"): [
            "Rough ideas go to First PRD Walkthrough or Precode Idea Coach",
            "Product Ideation Workbook / Precode Idea Coach",
        ],
        Path("docs/HOW-TO-BUILD-SOFTWARE-WITH-PRECODE.md"): [
            "Product Ideation Workbook or Precode Idea Coach",
            "Product Ideation Workbook / Precode Idea Coach",
        ],
        Path("tasks/reference/IDEA-TO-PRD-WORKFLOW.md"): [
            "Product Ideation Workbook or Precode Idea Coach",
        ],
    }
    for path, forbidden_terms in forbidden_terms_by_path.items():
        text = path.read_text(encoding="utf-8")
        for term in forbidden_terms:
            if term in text:
                failures.append({"scenario": f"onboarding authority consolidation forbidden wording: {path}", "expected": f"remove {term}", "actual": "present"})

    return len(required_terms_by_path) + 1 + len(forbidden_terms_by_path)


def assert_first_product_spine_contract(failures: list[dict[str, str]]) -> int:
    spine = "Idea -> Brief -> Packet -> Intake -> PRD -> Bead -> Proof -> Review -> Close"
    required_terms_by_path = {
        Path("docs/PRECODE-DAILY-COCKPIT.md"): [
            f"First-product spine: `{spine}`",
            "Brief: Product Brief after at most three high-level questions.",
            "Packet: reviewed Conviction Packet / Precode Ingestion Packet.",
            "Intake: Local Source Intake summary.",
            "PRD: human-reviewed PRD shaping and approval.",
            "Bead: candidate decomposition, then approved active bead.",
            "Proof: recorded checks and manual evidence.",
            "Review: human review, with advisory lanes only when needed.",
            "Close: closeout evidence and explicit Close State.",
        ],
        Path("docs/PRECODE-USER-GUIDE.md"): [
            f"The first-product spine is: `{spine}`.",
            "Intake is the Local Source Intake summary",
            "PRD is human-reviewed PRD shaping and approval",
            "Bead is candidate decomposition followed by an approved active bead",
            "Proof is recorded checks and manual evidence",
            "Review is human review with advisory lanes only when needed",
            "Close is closeout evidence and an explicit Close State",
        ],
        Path("docs/HOW-TO-BUILD-SOFTWARE-WITH-PRECODE.md"): [
            f"The first-product spine is: `{spine}`.",
            "rough idea or messy notes become a Product Brief",
            "then Local Source Intake",
            "then human-reviewed PRD shaping and approval",
            "then candidate decomposition and one approved active bead",
            "then recorded proof, human review, and closeout with explicit Close State",
        ],
        Path("docs/CLAUDE-CODE-FIELD-GUIDE.md"): [
            f"First-product spine: `{spine}`.",
            "Product Ideation Workbook and Precode Idea Coach are steps inside that route, not separate commands to choose between.",
            "Bring it through Local Source Intake before PRD shaping",
            "human PRD approval is required before decomposition, bead activation, or implementation",
        ],
        Path("docs/PRECODE-SUPPORT-RUNBOOK.md"): [
            f"First-product spine: `{spine}`.",
            "Do not expose Product Ideation Workbook, Precode Idea Coach, Product Discovery, Candidate Queue, Hypothesis Review, Build-React-Learn, or Review Lanes as peer routes unless the current stage or risk actually calls for one.",
            "then Local Source Intake",
            "then human-reviewed PRD shaping and approval",
            "then candidate decomposition and one approved active bead",
            "then recorded proof, human review, and closeout with explicit Close State",
        ],
        Path("tasks/reference/PROMPT-PATTERNS.md"): [
            f"First-product spine: `{spine}`.",
            "Brief: Product Brief after at most three high-level questions.",
            "Packet: reviewed Conviction Packet / Precode Ingestion Packet.",
            "Intake: Local Source Intake summary.",
            "PRD: human-reviewed PRD shaping and approval.",
            "Bead: candidate decomposition, then approved active bead.",
            "Proof: recorded checks and manual evidence.",
            "Review: human review, with advisory lanes only when needed.",
            "Close: closeout evidence and explicit Close State.",
        ],
        Path("tasks/reference/WORKFLOW-SELECTION-PROTOCOL.md"): [
            f"First-product spine: `{spine}`.",
            "Local Source Intake before PRD shaping",
            "human PRD approval before decomposition or bead activation",
            "recorded proof before review",
            "review before closeout or transition approval",
        ],
        Path("tasks/reference/PRD-PROTOCOL.md"): [
            spine,
            "Brief means Product Brief after at most three high-level questions",
            "Packet means reviewed Conviction Packet / Precode Ingestion Packet",
            "Intake means Local Source Intake before PRD shaping",
        ],
        Path("tasks/reference/LOCAL-SOURCE-INTAKE-PROTOCOL.md"): [
            f"`{spine}`",
            "A Conviction Packet / Precode Ingestion Packet can feed intake",
            "requires user review before PRD shaping, owner-file promotion, decomposition, bead activation, or coding",
        ],
        Path("tasks/reference/DECOMPOSITION-PROTOCOL.md"): [
            f"`{spine}`",
            "after human-reviewed PRD shaping and approval",
            "does not activate them",
            "proof, review, and closeout remain separate later gates",
        ],
        Path("tasks/reference/SESSION-COMPLETION-HANDOFF-PROTOCOL.md"): [
            f"`{spine}`",
            "Proof, Review, and Close",
            "recorded checks and manual evidence come before human review",
            "closeout with explicit Close State comes after review/handback",
            "Closeout does not accept work, approve transition, or activate another bead by itself.",
        ],
        Path("docs/PRECODE-PACKAGE-FILE-INVENTORY.md"): [
            spine,
            "compressed first-product spine",
            "remain steps inside",
        ],
        Path("llms.txt"): [
            spine,
            "visible first-product spine",
        ],
    }
    for path, required_terms in required_terms_by_path.items():
        text = path.read_text(encoding="utf-8")
        for term in required_terms:
            if term not in text:
                failures.append({"scenario": f"first-product spine contract: {path}", "expected": term, "actual": "missing"})

    forbidden_peer_phrases = {
        Path("docs/PRECODE-SUPPORT-RUNBOOK.md"): [
            "Product Ideation Workbook, Product Discovery, Candidate Queue, Hypothesis Review, Build-React-Learn, or Review Lanes as peer routes",
        ],
        Path("tasks/reference/PROMPT-PATTERNS.md"): [
            "Product Ideation Workbook or First PRD Walkthrough",
            "Precode Idea Coach or First PRD Walkthrough",
        ],
        Path("tasks/reference/WORKFLOW-SELECTION-PROTOCOL.md"): [
            "Product Discovery Interview, Product Conviction Packet, Precode Idea Coach, and First PRD Walkthrough as peers.",
        ],
    }
    for path, phrases in forbidden_peer_phrases.items():
        text = path.read_text(encoding="utf-8")
        for phrase in phrases:
            if phrase in text and "do not present" not in text.lower() and "Do not expose" not in text:
                failures.append({"scenario": f"first-product spine forbidden peer phrasing: {path}", "expected": f"remove {phrase}", "actual": "present"})
    return len(required_terms_by_path) + len(forbidden_peer_phrases)


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


def assert_candidate_queue_contract(failures: list[dict[str, str]]) -> int:
    required_terms_by_path = {
        Path("CANDIDATE-QUEUE.md"): [
            "intents we have not lost",
            "What is the active task?",
            "What should the agent build next?",
            "Is this PRD approved?",
            "Is this bead active?",
            "Is this ranked item authorized for implementation?",
            "Candidate ranking is review order only",
            "Product-value ratings `P0`, `P1`, `P2`, and `P3` are product value only",
            "Global Theme Index",
            "Near-bead sketch IDs",
            "CQ-001-owner-dashboard-S01",
            "mutates_now: false",
            "--approve-action",
            "Candidate IDs do not reserve PRD IDs or bead IDs",
            "Do not create `B###` bead IDs here",
        ],
        Path("tasks/reference/CANDIDATE-QUEUE-PROTOCOL.md"): [
            "task selection",
            "PRD approval",
            "bead activation",
            "automatic ranking",
            "permission to code",
            "Product-value ratings are separate from reviewed rank",
            "Near-bead sketches are early decomposition notes",
            "Raw-note import is minimal capture only",
            "must not call an LLM/API",
            "Apply must refuse missing approvals",
            "Local Source Intake",
            "Product Discovery Validation",
            "Decomposition Protocol",
            "Do not reserve PRD IDs or bead IDs",
        ],
        Path("tasks/reference/WORKFLOW-SELECTION-PROTOCOL.md"): [
            "Candidate Queue Protocol",
            "product roadmap",
            "backlog-like list",
            "must not choose next work or authorize implementation",
        ],
        Path("tasks/reference/LONG-HORIZON-PLANNING-PROTOCOL.md"): [
            "Candidate Queue",
            "human-maintained",
            "Neither surface may choose work or activate beads",
            "must not edit the queue, auto-rank candidates",
        ],
        Path("tasks/reference/DECOMPOSITION-PROTOCOL.md"): [
            "Candidate Queue entry",
            "near-bead sketch IDs",
            "does not authorize bead creation or activation",
            "does not replace parent PRD",
        ],
        Path("tasks/reference/LOCAL-SOURCE-INTAKE-PROTOCOL.md"): [
            "Candidate Queue entries",
            "minimal queue capture only",
            "stay queued",
            "Do not activate a bead or start coding",
        ],
        Path("tasks/reference/INTENT-ORCHESTRATION-PROTOCOL.md"): [
            "candidate_queued",
            "Candidate Queue",
            "Do not promote a Candidate Queue entry directly into active work",
        ],
        Path("tasks/reference/PRD-PROTOCOL.md"): [
            "Candidate Queue",
            "near-bead sketch IDs",
            "does not approve the PRD",
            "authorize beads",
        ],
        Path("tasks/prds/PRD-SHARD-SCHEMA.md"): [
            "Candidate Queue ID",
            "near-bead sketch IDs",
            "does not approve the PRD",
            "final bead IDs are assigned only when actual bead files are created",
        ],
        Path("tasks/prds/PRD-000-template.md"): [
            "Candidate Queue ID",
            "Candidate Queue product-value rating",
            "Do not reserve `B###` IDs",
        ],
        Path("docs/PRECODE-USER-GUIDE.md"): [
            "Use The Candidate Queue For Parked Intent",
            "psychological benefit of a backlog",
            "Product-value ratings `P0`, `P1`, `P2`, and `P3` are product value only",
            "preview-shaping",
            "cannot answer",
        ],
        Path("docs/PRECODE-DAILY-COCKPIT.md"): [
            "Review candidates",
            "parked intent, not task authority",
            "Do not update active memory",
        ],
        Path("tasks/reference/PROMPT-PATTERNS.md"): [
            "Candidate Queue Review",
            "Add Candidate Queue Entry",
            "Candidate Queue Shaping Proposal",
            "Candidate Queue Import Preview",
            "Ranking is review order only",
        ],
        Path("docs/PRECODE-PACKAGE-FILE-INVENTORY.md"): [
            "CANDIDATE-QUEUE.md",
            "Candidate Queue states",
            "scripts/candidate-queue.py",
            "product-value ratings",
            "not active memory",
        ],
    }
    for path, required_terms in required_terms_by_path.items():
        text = path.read_text(encoding="utf-8")
        for term in required_terms:
            if term not in text:
                failures.append({"scenario": f"candidate queue contract: {path}", "expected": term, "actual": "missing"})
    return len(required_terms_by_path)


def assert_hypothesis_guidance_contract(failures: list[dict[str, str]]) -> int:
    required_terms_by_path = {
        Path("tasks/reference/PRODUCT-DISCOVERY-VALIDATION-PROTOCOL.md"): [
            "Hypothesis Mechanics",
            "Primary hypothesis / learning target",
            "Hypothesis review status",
            "experiment hypothesis",
            "HYPOTHESIS-REVIEW-PROTOCOL.md",
            "not PRD approval",
            "task activation",
        ],
        Path("tasks/reference/HYPOTHESIS-REVIEW-PROTOCOL.md"): [
            "Hypothesis Review / Learning Loop",
            "Discovery Summary",
            "Candidate Queue entry",
            "Local Source Intake summary",
            "PRD Source Inputs section",
            "Planning Brief",
            "Learning status: untested | tested | narrowed | killed | promoted | stale | not applicable",
            "Learning outcome:",
            "Stale or untested signals:",
            "Recommended next Precode workflow:",
            "Generated-report warning:",
            "does not approve product direction",
            "rank candidates",
            "activate beads",
            "require analytics",
            "experiment database",
            "generated hypothesis status",
        ],
        Path("tasks/reference/CANDIDATE-QUEUE-PROTOCOL.md"): [
            "Primary hypothesis / learning target",
            "Hypothesis review status",
            "Candidate Queue hypotheses are evidence",
            "HYPOTHESIS-REVIEW-PROTOCOL.md",
            "rank work",
            "authorize implementation",
        ],
        Path("tasks/reference/PLANNING-PROTOCOL.md"): [
            "experiment hypothesis",
            "Learning Review",
            "Hypothesis review status",
            "Falsifier or what would change our mind",
            "does not approve a PRD",
        ],
        Path("tasks/reference/LOCAL-SOURCE-INTAKE-PROTOCOL.md"): [
            "Primary hypothesis / learning target",
            "Hypothesis review status",
            "Learning outcome",
            "testable hypothesis",
            "Product Discovery Validation",
            "HYPOTHESIS-REVIEW-PROTOCOL.md",
        ],
        Path("tasks/reference/PRD-PROTOCOL.md"): [
            "Primary hypothesis / learning target",
            "Hypothesis review status",
            "implementation permission",
        ],
        Path("tasks/prds/PRD-022-hypothesis-review-learning-loop.md"): [
            "Hypothesis Review And Learning Loop v2",
            "PRD-022-FR01",
            "PRD-022-FR07",
            "untested",
            "tested",
            "narrowed",
            "killed",
            "promoted",
            "stale",
            "not applicable",
            "generated status authority",
        ],
        Path("tasks/reference/PROMPT-PATTERNS.md"): [
            "Hypothesis Review / Learning Loop",
            "primary hypothesis or learning target",
            "Candidate Queue Review",
            "require analytics",
            "create a database",
        ],
        Path("docs/PRECODE-USER-GUIDE.md"): [
            "Review What A Hypothesis Taught You",
            "Hypothesis Review / Learning Loop",
            "require analytics",
            "create a database",
        ],
        Path("docs/PRECODE-DAILY-COCKPIT.md"): [
            "Review hypothesis",
            "Hypothesis Review / Learning Loop",
            "not applicable",
        ],
        Path("docs/PRECODE-PACKAGE-FILE-INVENTORY.md"): [
            "scripts/hypothesis-check.py",
            "Hypothesis Guidance",
            "Hypothesis Review / Learning Loop",
            "HYPOTHESIS-REVIEW-PROTOCOL.md",
        ],
    }
    for path, required_terms in required_terms_by_path.items():
        text = path.read_text(encoding="utf-8")
        for term in required_terms:
            if term not in text:
                failures.append({"scenario": f"hypothesis guidance contract: {path}", "expected": term, "actual": "missing"})
    return len(required_terms_by_path)


def assert_ears_acceptance_guidance_contract(failures: list[dict[str, str]]) -> int:
    required_terms_by_path = {
        Path("ACCEPTANCE.md"): [
            "Optional EARS-Style Pattern",
            "WHEN [condition or event] THE SYSTEM SHALL [observable expected behavior]",
            "Clear non-EARS acceptance criteria remain valid",
            "not required schema",
            "proof by itself",
            "implementation authority",
        ],
        Path("tasks/reference/PRD-PROTOCOL.md"): [
            "optional EARS-style wording",
            "WHEN [condition/event] THE SYSTEM SHALL [observable expected behavior]",
            "Do not require EARS syntax",
            "reject clear non-EARS acceptance criteria",
            "treat the wording as proof",
            "PRD approval",
            "implementation authority",
        ],
        Path("tasks/prds/PRD-000-template.md"): [
            "Optional EARS-style phrasing",
            "WHEN [condition/event] THE SYSTEM SHALL [observable expected behavior]",
            "Clear non-EARS acceptance criteria remain valid",
            "not required schema",
            "proof by itself",
        ],
        Path("tasks/prds/PRD-SHARD-SCHEMA.md"): [
            "optional EARS-style wording",
            "not required PRD structure",
            "schema enforcement",
            "generated proof",
            "implementation acceptance",
        ],
        Path("tasks/prds/PRD-026-ears-acceptance-guidance.md"): [
            "EARS-Style Acceptance Criteria Guidance",
            "PRD-026-FR01",
            "PRD-026-FR04",
            "optional EARS-style acceptance guidance",
            "not required syntax",
            "dedicated EARS checker",
            "generated report field",
            "Kiro integration",
        ],
        Path("tasks/reference/PROMPT-PATTERNS.md"): [
            "Make Acceptance Criteria Testable",
            "Review Acceptance Criteria For Vague Behavior",
            "optional EARS-style wording",
            "Keep clear non-EARS criteria",
            "Do not require EARS syntax",
            "treat wording as proof",
        ],
        Path("docs/PRECODE-USER-GUIDE.md"): [
            "Make Acceptance Criteria Testable",
            "optional EARS-style wording",
            "Keep clear non-EARS criteria",
            "EARS-style wording is a clarity aid",
            "not required syntax",
            "permission to build",
        ],
        Path("docs/PRECODE-DAILY-COCKPIT.md"): [
            "Clarify acceptance",
            "optional EARS-style wording",
            "Do not require EARS syntax",
            "treat wording as proof",
            "writing guidance only",
        ],
        Path("docs/PRECODE-PACKAGE-FILE-INVENTORY.md"): [
            "optional EARS-style writing guidance",
            "optional EARS-style acceptance-oracle guidance",
            "PRD-026",
            "not required syntax",
            "schema enforcement",
        ],
    }
    for path, required_terms in required_terms_by_path.items():
        text = path.read_text(encoding="utf-8")
        for term in required_terms:
            if term not in text:
                failures.append({"scenario": f"ears acceptance guidance contract: {path}", "expected": term, "actual": "missing"})
    return len(required_terms_by_path)


def assert_ubiquitous_language_contract(failures: list[dict[str, str]]) -> int:
    required_terms_by_path = {
        Path("tasks/reference/UBIQUITOUS-LANGUAGE-PROTOCOL.md"): [
            "Glossary Review Workflow",
            "source pointers",
            "examples",
            "freshness",
            "authority owner",
            "does not approve PRDs",
            "Naming Review",
            "demoted signals",
        ],
        Path("tasks/reference/MEMORY-PROTOCOL.md"): [
            "Project Glossary Cards",
            "Source pointers",
            "Examples",
            "Authority owner if promoted",
            "evidence rather than authority",
        ],
        Path("memory/cards/MEMORY-CARD-FORMAT.md"): [
            "Project Glossary Guidance",
            "Source pointers",
            "Examples",
            "Freshness",
            "evidence only",
        ],
        Path("tasks/reference/PROMPT-PATTERNS.md"): [
            "Glossary Card Proposal",
            "source pointers for each useful term group",
            "do not treat the proposed card as authority",
            "Domain Naming Review",
        ],
        Path("docs/PRECODE-USER-GUIDE.md"): [
            "What is a project glossary?",
            "source pointers",
            "Search results can help naming review",
            "do not rename code",
        ],
        Path("docs/PRECODE-PACKAGE-FILE-INVENTORY.md"): [
            "glossary-card excerpts",
            "generated memory indexes",
            "glossary memory creation while preserving glossary cards as evidence only",
        ],
    }
    for path, required_terms in required_terms_by_path.items():
        text = path.read_text(encoding="utf-8")
        for term in required_terms:
            if term not in text:
                failures.append({"scenario": f"ubiquitous language contract: {path}", "expected": term, "actual": "missing"})
    return len(required_terms_by_path)


def assert_plan_loop_contract(failures: list[dict[str, str]]) -> int:
    required_terms_by_path = {
        Path("tasks/reference/WORKFLOW-SELECTION-PROTOCOL.md"): [
            "Plan Loop",
            "Plan Packet",
            "user explicitly asks",
            "evidence only",
            "must not approve a PRD",
            "create or activate beads",
            "choose tasks",
            "backlog authority",
            "authorize implementation",
        ],
        Path("tasks/reference/IDEA-TO-PRD-WORKFLOW.md"): [
            "Plan Loop",
            "Plan Packet",
            "Local Source Intake",
            "no bead proposal",
            "Decomposition must create any candidate bead proposal",
            "must not update `tasks/todo.md`",
        ],
        Path("tasks/reference/PRD-PROTOCOL.md"): [
            "Plan Packet",
            "evidence only",
            "does not approve the PRD",
            "create beads",
            "authorize implementation",
        ],
        Path("tasks/reference/DECOMPOSITION-PROTOCOL.md"): [
            "Plan Packet",
            "evidence only",
            "does not create candidate beads",
            "Bead Decomposition Test",
            "not a bead yet",
        ],
        Path("tasks/reference/PROMPT-PATTERNS.md"): [
            "Use the Plan Loop on this feature angle",
            "Plan Packet",
            "source context used",
            "feature angle or topic explored",
            "Treat the Plan Packet as evidence only",
            "do not update tasks/todo.md",
            "approve a PRD",
            "choose tasks",
            "backlog authority",
            "authorize implementation",
        ],
        Path("docs/PRECODE-USER-GUIDE.md"): [
            "Use The Plan Loop Before Bead Commitment",
            "Plan Packet",
            "Exploration Loop is for pre-PRD thinking",
            "post-intake or post-PRD",
            "evidence only",
            "Do not approve a PRD",
            "create or activate beads",
            "choose tasks",
            "backlog authority",
            "authorize implementation",
        ],
        Path("docs/PRECODE-PACKAGE-FILE-INVENTORY.md"): [
            "Plan Loop",
            "Plan Packet",
            "post-intake or post-PRD feature-angle exploration",
            "evidence only",
            "does not approve PRDs",
            "create or activate beads",
            "choose tasks",
            "backlog authority",
            "authorize implementation",
        ],
    }
    for path, required_terms in required_terms_by_path.items():
        text = path.read_text(encoding="utf-8")
        for term in required_terms:
            if term not in text:
                failures.append({"scenario": f"plan loop contract: {path}", "expected": term, "actual": "missing"})
    return len(required_terms_by_path)


def assert_first_prd_walkthrough_contract(failures: list[dict[str, str]]) -> int:
    required_terms_by_path = {
        Path("tasks/reference/IDEA-TO-PRD-WORKFLOW.md"): [
            "First PRD Walkthrough",
            "Product Brief",
            "Conviction Packet",
            "evidence only",
            "Local Source Intake",
            "before PRD shaping",
            "Human PRD approval",
            "before `FEATURES.md` compilation",
            "bead activation",
            "authorize coding",
        ],
        Path("tasks/reference/PRD-PROTOCOL.md"): [
            "First PRD Walkthrough",
            "Product Ideation Workbook",
            "Precode Idea Coach",
            "does not draft or approve PRDs",
            "Product Briefs",
            "Conviction Packets",
            "evidence only",
            "Local Source Intake",
            "Human PRD approval",
            "before feature compilation",
            "bead activation",
            "coding",
        ],
        Path("tasks/reference/WORKFLOW-SELECTION-PROTOCOL.md"): [
            "First PRD Walkthrough",
            "Local Source Intake",
            "reviewed intake summary before PRD shaping",
            "does not create a new workflow authority",
            "approve PRDs",
            "create or activate beads",
            "choose tasks",
            "create a roadmap or backlog",
            "authorize implementation",
        ],
        Path("tasks/reference/PROMPT-PATTERNS.md"): [
            "Use First PRD Walkthrough for my rough idea",
            "Product Brief",
            "Challenge And Clarity",
            "Conviction Packet",
            "Local Source Intake handoff prompt",
            "evidence only",
            "Do not draft or approve a PRD",
            "create a roadmap or backlog",
            "create or activate beads",
            "choose tasks",
            "Human PRD approval",
        ],
        Path("docs/PRECODE-USER-GUIDE.md"): [
            "First PRD Walkthrough",
            "shortest safe path from rough idea to PRD readiness",
            "Product Ideation Workbook",
            "Conviction Packet",
            "Local Source Intake",
            "not a PRD approval shortcut",
            "does not authorize coding",
            "evidence only",
            "Do not draft or approve a PRD",
            "create or activate beads",
        ],
        Path("docs/PRECODE-DAILY-COCKPIT.md"): [
            "First PRD walkthrough",
            "Use First PRD Walkthrough for my rough idea",
            "Product Brief",
            "Conviction Packet",
            "Local Source Intake handoff",
            "evidence only",
            "human PRD approval",
        ],
        Path("docs/HOW-TO-BUILD-SOFTWARE-WITH-PRECODE.md"): [
            "First PRD Walkthrough",
            "shortest safe route from rough idea to PRD readiness",
            "Product Ideation Workbook",
            "Precode Idea Coach",
            "Local Source Intake",
            "does not approve a PRD",
            "create beads",
            "authorize coding",
        ],
    }
    for path, required_terms in required_terms_by_path.items():
        text = path.read_text(encoding="utf-8")
        for term in required_terms:
            if term not in text:
                failures.append({"scenario": f"first PRD walkthrough contract: {path}", "expected": term, "actual": "missing"})
    return len(required_terms_by_path)


def assert_bugfix_spec_lane_contract(failures: list[dict[str, str]]) -> None:
    recovery_text = Path("tasks/reference/RECOVERY-PROTOCOL.md").read_text(encoding="utf-8").lower()
    prompt_text = Path("tasks/reference/PROMPT-PATTERNS.md").read_text(encoding="utf-8").lower()
    verification_text = Path("tasks/reference/VERIFICATION-GUARDRAIL-PROTOCOL.md").read_text(encoding="utf-8").lower()
    cockpit_text = Path("docs/PRECODE-DAILY-COCKPIT.md").read_text(encoding="utf-8").lower()
    troubleshooting_text = Path("docs/PRECODE-TROUBLESHOOTING.md").read_text(encoding="utf-8").lower()

    recovery_terms = [
        "bugfix spec lane",
        "current behavior",
        "expected behavior",
        "unchanged behavior",
        "owner file",
        "root cause if known",
        "fix approach",
        "regression proof",
        "route decision",
        "current_bead",
        "needs_evidence",
        "recovery_repair",
        "prd/bead",
        "release_readiness",
        "not repair approval",
        "closeout evidence",
    ]
    for term in recovery_terms:
        if term not in recovery_text:
            failures.append({"scenario": "bugfix spec lane recovery contract", "expected": term, "actual": "missing"})

    prompt_terms = [
        "use the bugfix spec lane before editing this small repair",
        "current behavior:",
        "expected behavior:",
        "unchanged behavior:",
        "owner file:",
        "root cause if known:",
        "fix approach:",
        "regression proof:",
        "route decision:",
        "treat this spec as advisory only",
        "does not approve repair",
        "create implementation tasks",
        "become generated proof",
    ]
    for term in prompt_terms:
        if term not in prompt_text:
            failures.append({"scenario": "bugfix spec lane prompt contract", "expected": term, "actual": "missing"})

    verification_terms = [
        "for bugfix spec lane work",
        "named defect is fixed",
        "named unchanged behavior still holds",
        "failing-first check",
        "characterization check",
        "current behavior, expected behavior, and unchanged behavior",
    ]
    for term in verification_terms:
        if term not in verification_text:
            failures.append({"scenario": "bugfix spec lane verification contract", "expected": term, "actual": "missing"})

    for path, text in (
        ("docs/PRECODE-DAILY-COCKPIT.md", cockpit_text),
        ("docs/PRECODE-TROUBLESHOOTING.md", troubleshooting_text),
    ):
        for term in ("bugfix spec lane", "before editing"):
            if term not in text:
                failures.append({"scenario": f"bugfix spec lane user guidance: {path}", "expected": term, "actual": "missing"})


def assert_accessibility_advisory_gate_contract(failures: list[dict[str, str]]) -> None:
    ui_bead = bead(
        files_in_play=["app/page.tsx"],
        verification_type=["browser"],
        checks=["npx playwright test"],
        sections={
            "Objective": "Update the visible interface.",
            "Done When": "The page renders.",
            "Stop If": "Scope or proof becomes unclear.",
            "Closeout Evidence": "- Recorded checks: pending",
        },
    )
    not_invoked = accessibility_advisory_gate_quality(ui_bead)
    if not_invoked.get("status") != "not_invoked":
        failures.append(
            {
                "scenario": "accessibility advisory not invoked for UI by default",
                "expected": "not_invoked",
                "actual": str(not_invoked.get("status")),
            }
        )
    details = not_invoked.get("details") or {}
    if details.get("ui_default_gate") is not False or details.get("advisory_only") is not True:
        failures.append(
            {
                "scenario": "accessibility advisory default boundaries",
                "expected": "advisory_only true and ui_default_gate false",
                "actual": str(details),
            }
        )

    invoked_incomplete = bead(
        sections={
            "Objective": "Review accessibility advisory output.",
            "Done When": "The advisor evidence is recorded.",
            "Stop If": "Scope or proof becomes unclear.",
            "Closeout Evidence": "\n".join(
                [
                    "Accessibility advisory:",
                    "- Invocation decision: invoke advisor",
                    "- Target:",
                    "- Automated check evidence:",
                    "- Manual review notes:",
                    "- Unresolved findings:",
                    "- Acceptance risk:",
                ]
            ),
        },
    )
    warning = accessibility_advisory_gate_quality(invoked_incomplete)
    if warning.get("status") != "warning":
        failures.append(
            {
                "scenario": "accessibility advisory invoked incomplete warning",
                "expected": "warning",
                "actual": str(warning.get("status")),
            }
        )
    missing = ((warning.get("details") or {}).get("missing_fields") or [])
    for field in ("Target", "Automated check evidence", "Manual review notes", "Unresolved findings", "Acceptance risk"):
        if field not in missing:
            failures.append({"scenario": "accessibility advisory missing field", "expected": field, "actual": str(missing)})

    prompt_text = Path("tasks/reference/PROMPT-PATTERNS.md").read_text(encoding="utf-8").lower()
    skill_text = Path("tasks/reference/SKILL-PLAYBOOK-PROTOCOL.md").read_text(encoding="utf-8").lower()
    verification_text = Path("tasks/reference/VERIFICATION-GUARDRAIL-PROTOCOL.md").read_text(encoding="utf-8").lower()
    for term in (
        "accessibility advisor fit interview",
        "invoke advisor",
        "not needed",
        "defer",
        "do not make accessibility review mandatory for every ui/interface bead",
    ):
        if term not in prompt_text:
            failures.append({"scenario": "accessibility advisor prompt contract", "expected": term, "actual": "missing"})
    for term in ("accessibility advisor fit interview", "legal compliance", "wcag/ada", "not needed | defer"):
        if term not in skill_text:
            failures.append({"scenario": "accessibility advisor skill contract", "expected": term, "actual": "missing"})
    for term in ("accessibility advisory:", "invocation decision:", "automated check evidence:", "acceptance risk:"):
        if term not in verification_text:
            failures.append({"scenario": "accessibility advisor verification contract", "expected": term, "actual": "missing"})


def assert_review_lanes_contract(failures: list[dict[str, str]]) -> None:
    protocol_text = Path("tasks/reference/REVIEW-LANES-PROTOCOL.md").read_text(encoding="utf-8").lower()
    prompt_text = Path("tasks/reference/PROMPT-PATTERNS.md").read_text(encoding="utf-8").lower()
    user_guide_text = Path("docs/PRECODE-USER-GUIDE.md").read_text(encoding="utf-8").lower()
    bead_schema_text = Path("tasks/beads/BEAD-SCHEMA.md").read_text(encoding="utf-8").lower()

    required_terms = [
        "security review lane",
        "release / docs freshness review lane",
        "dependency graph review lane",
        "prd quality review lane",
        "lane:",
        "review target:",
        "authority checked:",
        "evidence reviewed:",
        "findings:",
        "missing proof:",
        "acceptance questions:",
        "recommendation: accepted | revise | split | blocked | stop",
        "approval still required:",
        "promotion path:",
        "does not approve work",
        "approve prds",
        "human prd approval",
        "security certification",
        "compliance approval",
        "create follow-up tasks",
        "create implementation tasks",
        "rewrite prds",
        "scorecard authority",
        "work graph reports are evidence only",
        "repair the markdown owner files",
        "approve parallel execution",
        "choose tasks",
        "task-runner system",
        "mutate github",
        "mutate external systems",
        "persona system",
        "product-quality and handoff-readiness artifact",
        "requirement-to-proof readiness",
        "smallest first slice",
        "requirements gap and conflict review",
    ]
    for term in required_terms:
        if term not in protocol_text:
            failures.append({"scenario": "review lanes protocol contract", "expected": term, "actual": "missing"})

    prompt_terms = [
        "use the review lanes protocol for this active bead or draft prd",
        "run exactly one lane: security review lane, release / docs freshness review lane, dependency graph review lane, or prd quality review lane",
        "run exactly one lane: dependency graph review lane",
        "run exactly one lane: prd quality review lane",
        "findings, missing proof, acceptance questions",
        "missing or non-done dependencies",
        "ambiguous follow-up destination",
        "stale generated graph evidence",
        "user problem clarity",
        "handoff readiness",
        "requirement-to-proof readiness",
        "smallest first slice",
        "do not accept implementation",
        "approve prds",
        "approve transitions",
        "approve parallel execution",
        "certify security or compliance",
        "create follow-up tasks",
        "create implementation tasks",
        "rewrite prds",
        "scorecard authority",
        "treat work graph reports or confidence as proof",
        "mutate github",
        "mutate external systems",
    ]
    for term in prompt_terms:
        if term not in prompt_text:
            failures.append({"scenario": "review lanes prompt contract", "expected": term, "actual": "missing"})

    for term in (
        "use a review lane",
        "security review lane",
        "release / docs freshness review lane",
        "dependency graph review lane",
        "prd quality review lane",
        "stale or misleading work graph output",
        "product quality and handoff readiness",
        "transition approval",
        "parallel execution approval",
        "work graph authority",
        "prd approval",
        "scorecard authority",
        "security sign-off",
    ):
        if term not in user_guide_text:
            failures.append({"scenario": "review lanes user guidance", "expected": term, "actual": "missing"})

    for term in ("review lanes protocol", "not as required frontmatter", "certify security or compliance"):
        if term not in bead_schema_text:
            failures.append({"scenario": "review lanes bead schema", "expected": term, "actual": "missing"})


def assert_team_collaboration_preview_contract(failures: list[dict[str, str]]) -> int:
    required_terms_by_path = {
        Path("tasks/prds/PRD-025-small-team-product-build-support-v2.md"): [
            "Small Team Product Build Support V2 Preview",
            "scripts/team-collaboration-check.py",
            "read-only local and optional GitHub evidence previews",
            "not merge automation",
            "generated preview JSON",
        ],
        Path("tasks/reference/TEAM-COLLABORATION-PROTOCOL.md"): [
            "V2 Read-Only Preview",
            "python3 scripts/team-collaboration-check.py --github",
            "Team Merge And Re-entry Review Pack",
            "Team Owner-File Conflict Preview",
            "one-active-bead-per-checkout",
            "generated evidence only",
            "must not choose work",
            "approve merge",
        ],
        Path("tasks/reference/GITHUB-INTEGRATION-PROTOCOL.md"): [
            "scripts/team-collaboration-check.py --github",
            "read-only aggregation path",
            "not_configured",
            "must not silently infer GitHub state",
            "must not mutate issues",
        ],
        Path("tasks/reference/DECOMPOSITION-PROTOCOL.md"): [
            "scripts/team-collaboration-check.py",
            "branch/worktree state",
            "owner-file impacts",
            "does not approve parallel work",
        ],
        Path("tasks/beads/BEAD-SCHEMA.md"): [
            "scripts/team-collaboration-check.py",
            "owner-file impacts",
            "stale re-entry risk",
            "does not approve parallel work",
            "Team preview output is generated evidence only",
        ],
        Path("tasks/reference/SESSION-COMPLETION-HANDOFF-PROTOCOL.md"): [
            "stale re-entry risks",
            "scripts/team-collaboration-check.py",
            "generated preview output is not acceptance",
            "team collaboration preview output",
        ],
        Path("tasks/reference/SKILL-PLAYBOOK-PROTOCOL.md"): [
            "scripts/team-collaboration-check.py",
            "logs/team-collaboration-preview.json",
            "generated evidence only",
        ],
        Path("tasks/reference/PROMPT-PATTERNS.md"): [
            "Small Team Collaboration Preview",
            "Team Assignment Packet Prompts v2",
            "Team Merge And Re-entry Review Pack",
            "Do not create branches or worktrees",
            "treat generated preview output as authority",
        ],
        Path("tasks/reference/EXTENSION-PROTOCOL.md"): [
            "logs/team-collaboration-preview.json",
            "must not choose work",
            "approve merge",
            "mutate GitHub",
            "package-manager behavior",
        ],
        Path("docs/PRECODE-USER-GUIDE.md"): [
            "Small Team Collaboration Lane preview",
            "python3 scripts/team-collaboration-check.py",
            "generated preview output is evidence only",
        ],
        Path("docs/PRECODE-DAILY-COCKPIT.md"): [
            "Coordinate A Small Team",
            "team-collaboration-check.py",
            "does not approve merge",
        ],
        Path("docs/PRECODE-OS-README.md"): [
            "Small Team Collaboration Lane",
            "team-collaboration-check.py",
            "read-only preview",
        ],
        Path("docs/PRECODE-ARCHITECTURE-OVERVIEW.md"): [
            "Team Collaboration Preview",
            "logs/team-collaboration-preview.json",
            "not a project-management system",
        ],
        Path("docs/PRECODE-PACKAGE-FILE-INVENTORY.md"): [
            "scripts/team-collaboration-check.py",
            "logs/team-collaboration-preview.json",
            "PRD-025",
        ],
    }
    for path, required_terms in required_terms_by_path.items():
        text = path.read_text(encoding="utf-8")
        for term in required_terms:
            if term not in text:
                failures.append({"scenario": f"team collaboration preview contract: {path}", "expected": term, "actual": "missing"})

    preview = team_collaboration_preview(
        Path("."),
        {"current_state": "in_progress", "current_bead": "tasks/beads/B999-team-fixture.md"},
        bead(
            rel_path="tasks/beads/B999-team-fixture.md",
            primary_authority="PROJECT-CONTEXT.md",
            files_in_play=["PROJECT-CONTEXT.md", "src/team.ts"],
        ),
        [
            bead(
                rel_path="tasks/beads/B999-team-fixture.md",
                primary_authority="PROJECT-CONTEXT.md",
                files_in_play=["PROJECT-CONTEXT.md", "src/team.ts"],
            )
        ],
        integration_branch="main",
    )
    details = preview.get("details") or {}
    required_fields = [
        "owner_protocol",
        "github_protocol",
        "current_branch",
        "integration_branch",
        "current_bead",
        "one_active_bead_per_checkout",
        "owner_file_impacts",
        "re_entry_risks",
        "merge_review_packet_fields",
        "assignment_packet_fields",
        "github_evidence",
        "forbidden_uses",
        "next_safe_action",
    ]
    for field in required_fields:
        if field not in details:
            failures.append({"scenario": "team preview payload field", "expected": field, "actual": "missing"})
    if details.get("advisory_only") is not True:
        failures.append({"scenario": "team preview advisory", "expected": "advisory_only true", "actual": str(details.get("advisory_only"))})
    if "generated evidence only" not in str(preview.get("generated_report_warning")):
        failures.append({"scenario": "team preview generated warning", "expected": "generated evidence only", "actual": str(preview.get("generated_report_warning"))})
    forbidden = " ".join(details.get("forbidden_uses") or [])
    for term in ["task selection", "merge approval", "GitHub mutation"]:
        if term not in forbidden:
            failures.append({"scenario": "team preview forbidden use", "expected": term, "actual": forbidden})
    return len(required_terms_by_path) + 1


def assert_github_collaboration_hub_contract(failures: list[dict[str, str]]) -> int:
    required_terms_by_path = {
        Path(".github/ISSUE_TEMPLATE/feedback.yml"): [
            "PrecodeOS feedback",
            "adoption friction",
            "confusing docs",
            "setup friction",
            "workflow questions",
            "source evidence only",
            "does not choose roadmap direction",
            "approve PRDs",
            "activate beads",
            "approve merge",
            "sensitive personal data",
        ],
        Path(".github/ISSUE_TEMPLATE/package-bug.yml"): [
            "PrecodeOS package bug",
            "docs, scripts, protocols",
            "setup/copy helpers",
            "GitHub helper behavior",
            "source evidence only",
            "approve release",
            "authorize GitHub mutation",
            "Reproduction or context",
            "Checks tried",
            "sensitive personal data",
        ],
        Path(".github/ISSUE_TEMPLATE/config.yml"): [
            "blank_issues_enabled: false",
            "CONTRIBUTING.md",
            "SECURITY.md",
            "PRECODE-SUPPORT-RUNBOOK.md",
        ],
        Path("tasks/prds/PRD-032-github-collaboration-hub.md"): [
            "GitHub Collaboration Hub",
            "feedback and package-bug intake",
            "source evidence",
            "No automatic issue creation",
            "No GitHub workflow, bot, labeler",
            "external mutation",
            "PRD-032-FR06",
        ],
        Path("tasks/reference/GITHUB-INTEGRATION-PROTOCOL.md"): [
            "Collaboration Hub Intake Path",
            "feedback and package-bug intake",
            "Labels do not choose work",
            "Project boards are not active project-management authority",
            "Creating, editing, labeling, assigning, commenting on, closing",
        ],
        Path("tasks/reference/LOCAL-SOURCE-INTAKE-PROTOCOL.md"): [
            "Public GitHub feedback issues",
            "package-bug issues",
            "source evidence",
            "approve package release",
            "authorize GitHub mutation",
        ],
        Path("tasks/reference/TOOL-EXECUTION-PROTOCOL.md"): [
            "For GitHub Collaboration Hub work",
            "external mutation includes",
            "creating or editing labels",
            "changing repository settings",
            "source evidence",
        ],
        Path("tasks/reference/PROMPT-PATTERNS.md"): [
            "Triage GitHub Feedback Or Package Bug",
            "GitHub Collaboration Hub intake path",
            "Recommended destination",
            "Do not choose roadmap direction",
            "mutate GitHub",
        ],
        Path("CONTRIBUTING.md"): [
            "Public GitHub Issues are open for narrow feedback and package-bug intake",
            "source evidence only",
            "Project boards are not active project-management authority",
            "requires explicit maintainer approval",
        ],
        Path("GOVERNANCE.md"): [
            "issue participation",
            "do not create governance rights",
            "GitHub Issues, labels, comments",
            "approve package release",
        ],
        Path("PROJECT-CONTEXT.md"): [
            "feedback and package-bug intake only",
            "do not treat GitHub Issues",
            "roadmap, merge, release, or package authority",
        ],
        Path("docs/PRECODE-USER-GUIDE.md"): [
            "Share Feedback Or Package Bugs",
            "Use public GitHub Issues only for narrow PrecodeOS feedback",
            "source evidence only",
            "Stable conclusions must be reviewed",
        ],
        Path("docs/PRECODE-SUPPORT-RUNBOOK.md"): [
            "Public GitHub Issues are available for narrow PrecodeOS feedback",
            "source evidence only",
            "support approval",
            "Local Source Intake and maintainer review",
        ],
        Path("docs/PRECODE-PACKAGE-FILE-INVENTORY.md"): [
            ".github/ISSUE_TEMPLATE/*.yml",
            "PRD-032-github-collaboration-hub.md",
            "feedback and package-bug intake",
            "mutate GitHub",
        ],
    }
    for path, required_terms in required_terms_by_path.items():
        text = path.read_text(encoding="utf-8")
        for term in required_terms:
            if term not in text:
                failures.append({"scenario": f"github collaboration hub contract: {path}", "expected": term, "actual": "missing"})

    workflow_text = Path(".github/workflows/precode-validate.yml").read_text(encoding="utf-8")
    for term in ("issues: write", "pull-requests: write", "contents: write"):
        if term in workflow_text:
            failures.append({"scenario": "github collaboration hub workflow permissions", "expected": f"no {term}", "actual": "found"})

    return len(required_terms_by_path) + 1


def assert_session_friction_review_contract(failures: list[dict[str, str]]) -> int:
    required_terms_by_path = {
        Path("tasks/prds/PRD-027-session-friction-review.md"): [
            "Session Friction Review",
            "scripts/session-friction-check.py",
            "cited failure-pattern findings",
            "generated-evidence boundaries",
            "no safe evidence found",
        ],
        Path("tasks/reference/TOOL-EXECUTION-PROTOCOL.md"): [
            "python3 scripts/session-friction-check.py",
            "repeated failure categories",
            "generated evidence only",
            "must not auto-edit active memory",
            "must not approve commands",
        ],
        Path("tasks/reference/MEMORY-PROTOCOL.md"): [
            "Session Friction Review",
            "manual promotion",
            "must cite the source evidence",
            "must not create memory cards",
        ],
        Path("tasks/reference/SESSION-COMPLETION-HANDOFF-PROTOCOL.md"): [
            "session-friction findings",
            "review input only",
            "do not promote memory",
            "do not approve commands",
        ],
        Path("tasks/reference/EXTENSION-PROTOCOL.md"): [
            "logs/session-friction-review.json",
            "read-only audit",
            "must not choose work",
            "package-manager behavior",
        ],
        Path("tasks/reference/PROMPT-PATTERNS.md"): [
            "Session Friction Review",
            "python3 scripts/session-friction-check.py",
            "Do not create memory cards",
            "Do not edit owner files",
        ],
        Path("docs/PRECODE-USER-GUIDE.md"): [
            "Session Friction Review",
            "python3 scripts/session-friction-check.py",
            "generated evidence only",
        ],
        Path("docs/PRECODE-TROUBLESHOOTING.md"): [
            "Session Friction Review",
            "repeated tool failures",
            "does not repair anything",
        ],
        Path("docs/PRECODE-ARCHITECTURE-OVERVIEW.md"): [
            "Session Friction Review",
            "logs/session-friction-review.json",
            "manual promotion",
        ],
        Path("docs/PRECODE-PACKAGE-FILE-INVENTORY.md"): [
            "scripts/session-friction-check.py",
            "logs/session-friction-review.json",
            "PRD-027",
        ],
    }
    for path, required_terms in required_terms_by_path.items():
        text = path.read_text(encoding="utf-8")
        for term in required_terms:
            if term not in text:
                failures.append({"scenario": f"session friction review contract: {path}", "expected": term, "actual": "missing"})

    preview = session_friction_review(
        Path("."),
        [
            {"timestamp": "fixture-1", "status": "fail", "command": "missing-a", "failure_category": "unavailable_command"},
            {"timestamp": "fixture-2", "status": "blocked", "command": "sandbox", "failure_category": "permission_or_sandbox_blocked"},
            {"timestamp": "fixture-3", "status": "fail", "command": "missing-b", "failure_category": "unavailable_command"},
            {"timestamp": "fixture-4", "status": "fail", "command": "unknown"},
        ],
        [],
        [],
        {"warnings": ["generated reports were refreshed for active work but no verification evidence exists"]},
        {"warnings": ["session close evidence is stale"]},
        {"warnings": ["reviewed memory card has token pressure"], "details": {}},
    )
    details = preview.get("details") or {}
    findings = details.get("findings") if isinstance(details.get("findings"), list) else []
    categories = {finding.get("category") for finding in findings}
    for category in [
        "repeated_failure_category",
        "missing_failure_category",
        "unavailable_command_or_dependency",
        "sandbox_or_approval_block",
        "stale_check_or_closeout_evidence",
        "generated_refresh_without_verification",
        "over_broad_context_or_memory_pressure",
    ]:
        if category not in categories:
            failures.append({"scenario": "session friction category", "expected": category, "actual": str(sorted(categories))})
    if details.get("advisory_only") is not True:
        failures.append({"scenario": "session friction advisory", "expected": "advisory_only true", "actual": str(details.get("advisory_only"))})
    if "generated evidence only" not in str(preview.get("generated_report_warning")):
        failures.append({"scenario": "session friction generated warning", "expected": "generated evidence only", "actual": str(preview.get("generated_report_warning"))})
    forbidden = " ".join((findings[0].get("forbidden_uses") if findings else []) or [])
    for term in ["task selection", "memory promotion", "owner-file edits", "command approval"]:
        if term not in forbidden:
            failures.append({"scenario": "session friction forbidden use", "expected": term, "actual": forbidden})
    return len(required_terms_by_path) + 1


def assert_build_attribution_contract(failures: list[dict[str, str]]) -> int:
    required_terms_by_path = {
        Path("tasks/prds/PRD-028-build-attribution-ledger.md"): [
            "Build Attribution Ledger",
            "scripts/build-attribution-ledger.py",
            "human contributor",
            "agent/tool surface",
            "No contributor scoring",
        ],
        Path("tasks/beads/BEAD-SCHEMA.md"): [
            "Human contributor",
            "Agent/tool surface",
            "Attribution uncertainty",
        ],
        Path("tasks/reference/SESSION-COMPLETION-HANDOFF-PROTOCOL.md"): [
            "Build attribution closeout",
            "scripts/build-attribution-ledger.py",
            "contributor scoring",
        ],
        Path("tasks/reference/BEAD-BUILD-JOURNAL-PROTOCOL.md"): [
            "Build attribution",
            "must not assign blame",
            "score contributors",
        ],
        Path("tasks/reference/EXTENSION-PROTOCOL.md"): [
            "logs/build-attribution-ledger.json",
            "assign blame",
            "registry",
        ],
        Path("tasks/reference/PROMPT-PATTERNS.md"): [
            "Build Attribution Review",
            "human contributor",
            "score contributors",
        ],
        Path("docs/PRECODE-DAILY-COCKPIT.md"): [
            "Build Attribution Ledger",
            "Review attribution",
            "who-built-what",
        ],
        Path("docs/PRECODE-USER-GUIDE.md"): [
            "Review Who Built What",
            "python3 scripts/build-attribution-ledger.py",
            "not a people registry",
        ],
        Path("docs/PRECODE-ARCHITECTURE-OVERVIEW.md"): [
            "build attribution",
            "logs/build-attribution-ledger.md/json",
            "score contributors",
        ],
        Path("docs/PRECODE-PACKAGE-FILE-INVENTORY.md"): [
            "PRD-028",
            "scripts/build-attribution-ledger.py",
            "logs/build-attribution-ledger.md/json",
        ],
    }
    for path, required_terms in required_terms_by_path.items():
        text = path.read_text(encoding="utf-8")
        for term in required_terms:
            if term not in text:
                failures.append({"scenario": f"build attribution contract: {path}", "expected": term, "actual": "missing"})

    payload = build_attribution_ledger(
        Path("."),
        [
            bead(
                rel_path="tasks/beads/B997-reviewed-attribution.md",
                bead_id="B997",
                closeout={
                    "human_contributor": "Dan Sears",
                    "contributor_role": "Coordinator",
                    "agent_tool_surface": "Codex",
                    "attribution_reviewed_by": "Dan Sears",
                    "attribution_uncertainty": "none recorded",
                },
            ),
            bead(rel_path="tasks/beads/B996-missing-attribution.md", bead_id="B996", closeout={}),
        ],
    )
    details = payload.get("details") or {}
    forbidden = " ".join(details.get("forbidden_uses") or [])
    for term in ["task selection", "implementation acceptance", "merge approval", "contributor scoring", "registry behavior"]:
        if term not in forbidden:
            failures.append({"scenario": "build attribution forbidden use", "expected": term, "actual": forbidden})
    if details.get("reviewed_closeout_count") != 1:
        failures.append({"scenario": "build attribution reviewed count", "expected": "1", "actual": str(details.get("reviewed_closeout_count"))})
    if details.get("missing_attribution_count") != 1:
        failures.append({"scenario": "build attribution missing count", "expected": "1", "actual": str(details.get("missing_attribution_count"))})
    if "generated evidence only" not in str(payload.get("generated_report_warning")):
        failures.append({"scenario": "build attribution generated warning", "expected": "generated evidence only", "actual": str(payload.get("generated_report_warning"))})
    return len(required_terms_by_path) + 1


def assert_prd_handoff_readiness_contract(failures: list[dict[str, str]]) -> int:
    required_terms_by_path = {
        Path("tasks/prds/PRD-029-prd-handoff-readiness-packet.md"): [
            "PRD Handoff Readiness Packet",
            "scripts/prd-handoff-readiness.py",
            "details.packet",
            "MCP behavior",
        ],
        Path("tasks/reference/PRD-PROTOCOL.md"): [
            "scripts/prd-handoff-readiness.py --prd <path>",
            "PRD handoff readiness",
            "generated evidence only",
        ],
        Path("tasks/reference/DECOMPOSITION-PROTOCOL.md"): [
            "--target decomposition",
            "PRD handoff blockers",
            "before any bead activation",
        ],
        Path("tasks/reference/REVIEW-LANES-PROTOCOL.md"): [
            "--target review",
            "PRD-review evidence",
            "does not approve the PRD",
        ],
        Path("tasks/reference/SESSION-COMPLETION-HANDOFF-PROTOCOL.md"): [
            "PRD handoff readiness is a separate advisory review",
            "not the active-session Context Pack",
            "not implementation acceptance",
        ],
        Path("tasks/reference/PROMPT-PATTERNS.md"): [
            "PRD Handoff Readiness Packet",
            "details.packet",
            "Do not approve the PRD",
        ],
        Path("docs/PRECODE-USER-GUIDE.md"): [
            "PRD Handoff Readiness Packet",
            "python3 scripts/prd-handoff-readiness.py",
            "Treat the packet as generated evidence only",
        ],
        Path("docs/PRECODE-PACKAGE-FILE-INVENTORY.md"): [
            "PRD-029",
            "scripts/prd-handoff-readiness.py",
            "PRD handoff readiness cues",
        ],
        Path("llms.txt"): [
            "scripts/prd-handoff-readiness.py",
            "PRD Handoff Readiness Packet",
            "do not approve PRDs",
        ],
    }
    for path, required_terms in required_terms_by_path.items():
        text = path.read_text(encoding="utf-8")
        for term in required_terms:
            if term not in text:
                failures.append({"scenario": f"prd handoff readiness contract: {path}", "expected": term, "actual": "missing"})

    module = load_prd_handoff_module()
    self_test = module.self_test()
    if self_test.get("status") != "pass":
        failures.append({"scenario": "prd handoff readiness self-test", "expected": "pass", "actual": str(self_test.get("failures"))})
    payload = module.build_payload(Path("tasks/prds/PRD-029-prd-handoff-readiness-packet.md"), "decomposition")
    packet = (payload.get("details") or {}).get("packet") or {}
    for key in [
        "prd_status",
        "requirement_ids",
        "acceptance_oracle_coverage",
        "candidate_bead_or_decomposition_readiness",
        "proof_expectations",
        "blockers",
        "recommended_next_safe_action",
    ]:
        if key not in packet:
            failures.append({"scenario": "prd handoff packet key", "expected": key, "actual": "missing"})
    forbidden = " ".join(packet.get("forbidden_uses") or [])
    for term in ["PRD approval", "bead activation", "implementation acceptance", "MCP behavior", "package-manager behavior"]:
        if term not in forbidden:
            failures.append({"scenario": "prd handoff forbidden use", "expected": term, "actual": forbidden})
    if "generated evidence only" not in str(payload.get("generated_report_warning")):
        failures.append({"scenario": "prd handoff generated warning", "expected": "generated evidence only", "actual": str(payload.get("generated_report_warning"))})
    return len(required_terms_by_path) + 2


def release_evidence_fixture(closeout_lines: list[str], **overrides: Any) -> BeadRecord:
    closeout = overrides.pop(
        "closeout",
        {
            "manual_verification": "Manual verification: not applicable because release evidence fixture is static.",
            "review_decision": "revise",
        },
    )
    return bead(
        primary_authority="tasks/reference/RELEASE-READINESS-PROTOCOL.md",
        parent_prd="tasks/prds/PRD-020-verification-release-evidence.md",
        requirement_ids=["PRD-020-FR04"],
        files_in_play=["tasks/reference/RELEASE-READINESS-PROTOCOL.md"],
        checks=["python3 scripts/clarity-scenario-check.py"],
        verification_type=["static"],
        closeout=closeout,
        sections={
            "Objective": "Review release evidence traceability.",
            "Done When": "Release evidence warnings are stable.",
            "Stop If": "Release proof becomes approval.",
            "Closeout Evidence": "\n".join(closeout_lines),
        },
        **overrides,
    )


def assert_verification_release_evidence_contract(failures: list[dict[str, str]]) -> int:
    release_protocol = Path("tasks/reference/RELEASE-READINESS-PROTOCOL.md").read_text(encoding="utf-8").lower()
    verification_protocol = Path("tasks/reference/VERIFICATION-GUARDRAIL-PROTOCOL.md").read_text(encoding="utf-8").lower()
    completion_protocol = Path("tasks/reference/SESSION-COMPLETION-HANDOFF-PROTOCOL.md").read_text(encoding="utf-8").lower()
    prompt_text = Path("tasks/reference/PROMPT-PATTERNS.md").read_text(encoding="utf-8").lower()
    user_guide_text = Path("docs/PRECODE-USER-GUIDE.md").read_text(encoding="utf-8").lower()
    bead_schema_text = Path("tasks/beads/BEAD-SCHEMA.md").read_text(encoding="utf-8").lower()

    for term in (
        "verification and release evidence review",
        "requirement or behavior proven",
        "evidence lane used",
        "recorded check, closeout evidence, or manual verification source",
        "missing traceability means `needs evidence`",
        "not release approval",
    ):
        if term not in release_protocol:
            failures.append({"scenario": "verification release evidence protocol contract", "expected": term, "actual": "missing"})
    for term in ("requirement or behavior being shipped", "evidence lane", "recorded source", "needs evidence"):
        if term not in verification_protocol:
            failures.append({"scenario": "verification release evidence guardrail contract", "expected": term, "actual": "missing"})
        if term not in completion_protocol:
            failures.append({"scenario": "verification release evidence completion contract", "expected": term, "actual": "missing"})
    for term in (
        "review verification and release evidence for this release-relevant bead",
        "durable recorded evidence",
        "review input only",
        "missing traceability means needs evidence",
        "ready for human release decision as release approval",
    ):
        if term not in prompt_text:
            failures.append({"scenario": "verification release evidence prompt contract", "expected": term, "actual": "missing"})
    for term in ("review verification and release evidence", "requirement or behavior proven", "completion-check.py", "approval to ship"):
        if term not in user_guide_text:
            failures.append({"scenario": "verification release evidence user guidance", "expected": term, "actual": "missing"})
    for term in ("verification and release evidence", "not as required frontmatter", "does not approve release"):
        if term not in bead_schema_text:
            failures.append({"scenario": "verification release evidence bead schema", "expected": term, "actual": "missing"})

    complete = release_evidence_fixture(
        [
            "Release-readiness note:",
            "- Smoke path and result: Opened changed flow and completed checkout smoke path.",
            "- Docs or support freshness: User guide and support notes reviewed.",
            "- Rollback path or blocked escape: Revert the bead changes before release.",
            "- Approvals still required: Human release approval still required.",
            "- Decision state: ready for human release decision",
            "Release Candidate Evidence Profile:",
            "- Candidate label: Fixture release candidate",
            "- Release target or environment: local fixture",
            "- Changed surfaces: release evidence guidance",
            "- Affected users or workflows: release-relevant beads",
            "- Recorded checks and results: clarity scenario pass",
            "- Smoke path and result: Opened changed flow and completed checkout smoke path.",
            "- Browser or manual verification status: not applicable because static fixture",
            "- Docs or support freshness: User guide and support notes reviewed.",
            "- Rollback path or blocked escape: Revert the bead changes before release.",
            "- Known risks and remaining uncertainty: none for fixture",
            "- Approvals still required: Human release approval still required.",
            "- Decision state: ready for human release decision",
            "Verification and release evidence:",
            "- Requirement or behavior proven: PRD-020-FR04 completion-check advisory details.",
            "- Evidence lane: static",
            "- Recorded source: python3 scripts/clarity-scenario-check.py",
            "- Smoke path and result: Opened changed flow and completed checkout smoke path.",
            "- Docs or support freshness: User guide and support notes reviewed.",
            "- Rollback path or blocked escape: Revert the bead changes before release.",
            "- Approvals still required: Human release approval still required.",
            "- Decision state: ready for human release decision",
            "- Remaining uncertainty: none for fixture",
            "Ready for human release decision is not release approval.",
        ]
    )
    complete_payload = release_evidence_quality(complete, list(passing_checks(complete).values()))
    if complete_payload.get("status") != "pass":
        failures.append({"scenario": "release evidence complete pass", "expected": "pass", "actual": str(complete_payload)})
    if (complete_payload.get("details") or {}).get("decision_state") != "ready for human release decision":
        failures.append({"scenario": "release evidence non-approval state", "expected": "ready for human release decision", "actual": str(complete_payload)})

    incomplete = release_evidence_fixture(
        [
            "Release Candidate Evidence Profile:",
            "- Candidate label: Fixture release candidate",
            "- Decision state: needs evidence",
            "Verification and release evidence:",
            "- Requirement or behavior proven: PRD-020-FR04 completion-check advisory details.",
            "- Evidence lane:",
            "- Recorded source:",
        ]
    )
    incomplete_payload = release_evidence_quality(incomplete, [])
    if incomplete_payload.get("status") != "warning":
        failures.append({"scenario": "release profile missing proof warning", "expected": "warning", "actual": str(incomplete_payload)})
    if not any("missing fields" in warning.lower() for warning in incomplete_payload.get("warnings") or []):
        failures.append({"scenario": "release profile missing fields warning", "expected": "missing fields warning", "actual": str(incomplete_payload)})

    review_input_only = release_evidence_fixture(
        [
            "Release-readiness note:",
            "- Smoke path and result: Screenshot and browser note looked correct.",
            "- Docs or support freshness: pending",
            "- Rollback path or blocked escape: pending",
            "- Approvals still required: pending",
            "- Decision state: needs evidence",
        ],
        closeout={"manual_verification": "pending", "review_decision": "revise"},
    )
    review_payload = release_evidence_quality(review_input_only, [])
    if not any("review input" in warning.lower() for warning in review_payload.get("warnings") or []):
        failures.append({"scenario": "release review input only warning", "expected": "review input warning", "actual": str(review_payload)})

    no_trace = release_evidence_fixture(
        [
            "Release-readiness note:",
            "- Smoke path and result: Local smoke passed.",
            "- Docs or support freshness: current.",
            "- Rollback path or blocked escape: revert the bead.",
            "- Approvals still required: release approval.",
            "- Decision state: needs evidence",
        ]
    )
    no_trace_payload = release_evidence_quality(no_trace, list(passing_checks(no_trace).values()))
    if not any("does not trace" in warning.lower() for warning in no_trace_payload.get("warnings") or []):
        failures.append({"scenario": "release requirement proof trace warning", "expected": "does not trace warning", "actual": str(no_trace_payload)})

    return 4


def assert_requirement_to_proof_contract(failures: list[dict[str, str]]) -> int:
    sources = {
        "verification": Path("tasks/reference/VERIFICATION-GUARDRAIL-PROTOCOL.md").read_text(encoding="utf-8").lower(),
        "completion": Path("tasks/reference/SESSION-COMPLETION-HANDOFF-PROTOCOL.md").read_text(encoding="utf-8").lower(),
        "prd": Path("tasks/reference/PRD-PROTOCOL.md").read_text(encoding="utf-8").lower(),
        "template": Path("tasks/prds/PRD-000-template.md").read_text(encoding="utf-8").lower(),
        "bead": Path("tasks/beads/BEAD-SCHEMA.md").read_text(encoding="utf-8").lower(),
        "review": Path("tasks/reference/REVIEW-LANES-PROTOCOL.md").read_text(encoding="utf-8").lower(),
        "prompts": Path("tasks/reference/PROMPT-PATTERNS.md").read_text(encoding="utf-8").lower(),
        "guide": Path("docs/PRECODE-USER-GUIDE.md").read_text(encoding="utf-8").lower(),
    }
    required_terms = [
        "requirement-to-proof trace",
        "requirement, bug behavior, or acceptance criterion",
        "evidence lane",
        "recorded source",
        "what this proves",
        "what this does not prove",
        "remaining uncertainty",
    ]
    for name, text in sources.items():
        for term in required_terms[:3]:
            if term not in text:
                failures.append({"scenario": f"requirement-to-proof {name}", "expected": term, "actual": "missing"})

    demotion_terms = [
        "generated test",
        "generated propert",
        "trace table",
        "screenshot",
        "browser note",
        "ai critique",
        "generated report",
        "not complete proof",
    ]
    demotion_text = "\n".join(sources.values())
    for term in demotion_terms:
        if term not in demotion_text:
            failures.append({"scenario": "requirement-to-proof demotion", "expected": term, "actual": "missing"})

    prompt_text = sources["prompts"] + "\n" + sources["guide"]
    for term in ["do not accept implementation", "approve review", "activate the next bead", "proof by themselves"]:
        if term not in prompt_text:
            failures.append({"scenario": "requirement-to-proof prompt boundaries", "expected": term, "actual": "missing"})

    return 3


def reversal_fixture(closeout_lines: list[str], **overrides: Any) -> BeadRecord:
    closeout = overrides.pop(
        "closeout",
        {
            "manual_verification": "Who checked: fixture. What was checked: reversal proof and preserved behavior. Environment: synthetic. Result: pass. Remaining uncertainty: none.",
            "review_decision": "accepted",
        },
    )
    return bead(
        title="B023 - Implemented Bead Reversal Workflow Fixture",
        primary_authority="tasks/prds/PRD-023-implemented-bead-reversal-workflow.md",
        parent_prd="tasks/prds/PRD-023-implemented-bead-reversal-workflow.md",
        requirement_ids=["PRD-023-FR05"],
        files_in_play=["tasks/reference/SESSION-COMPLETION-HANDOFF-PROTOCOL.md"],
        checks=["python3 scripts/clarity-scenario-check.py"],
        verification_type=["static"],
        closeout=closeout,
        sections={
            "Objective": "Review implemented bead reversal workflow.",
            "Done When": "Reversal workflow warnings are stable.",
            "Stop If": "Reversal becomes history mutation or rollback automation.",
            "Closeout Evidence": "\n".join(closeout_lines),
        },
        **overrides,
    )


def assert_implemented_bead_reversal_contract(failures: list[dict[str, str]]) -> int:
    prd_text = Path("tasks/prds/PRD-023-implemented-bead-reversal-workflow.md").read_text(encoding="utf-8").lower()
    bead_schema = Path("tasks/beads/BEAD-SCHEMA.md").read_text(encoding="utf-8").lower()
    completion_protocol = Path("tasks/reference/SESSION-COMPLETION-HANDOFF-PROTOCOL.md").read_text(encoding="utf-8").lower()
    recovery_protocol = Path("tasks/reference/RECOVERY-PROTOCOL.md").read_text(encoding="utf-8").lower()
    verification_protocol = Path("tasks/reference/VERIFICATION-GUARDRAIL-PROTOCOL.md").read_text(encoding="utf-8").lower()
    journal_protocol = Path("tasks/reference/BEAD-BUILD-JOURNAL-PROTOCOL.md").read_text(encoding="utf-8").lower()
    prompt_text = Path("tasks/reference/PROMPT-PATTERNS.md").read_text(encoding="utf-8").lower()

    for term in (
        "reversal bead",
        "superseded bead",
        "reversal target",
        "reversal reason",
        "preserved behavior",
        "git revert",
        "not proof",
        "do not reopen",
        "delete evidence",
        "rewrite transition logs",
        "no runtime reversal command",
    ):
        if term not in prd_text:
            failures.append({"scenario": "implemented bead reversal PRD contract", "expected": term, "actual": "missing"})

    for path_name, text in (
        ("bead schema", bead_schema),
        ("completion protocol", completion_protocol),
        ("recovery protocol", recovery_protocol),
        ("verification protocol", verification_protocol),
        ("journal protocol", journal_protocol),
        ("prompt pattern", prompt_text),
    ):
        for term in ("superseded bead", "reversal target", "reversal reason", "preserved behavior"):
            if term not in text:
                failures.append({"scenario": f"implemented bead reversal {path_name}", "expected": term, "actual": "missing"})

    complete = reversal_fixture(
        [
            "Reversal workflow:",
            "- Superseded bead: tasks/beads/B123-old-work.md",
            "- Reversal target: Remove the obsolete generated-output rule.",
            "- Reversal reason: The prior behavior conflicts with current authority.",
            "- Preserved behavior: Existing evidence and transition logs remain unchanged.",
            "- Reversal proof: clarity scenario pass and manual review.",
            "- Approvals still required: none for fixture after review.",
        ]
    )
    complete_payload = reversal_workflow_quality(complete, list(passing_checks(complete).values()))
    if complete_payload.get("status") != "pass":
        failures.append({"scenario": "implemented bead reversal complete pass", "expected": "pass", "actual": str(complete_payload)})

    missing = reversal_fixture(["Reversal workflow:", "- Superseded bead: tasks/beads/B123-old-work.md"])
    missing_payload = reversal_workflow_quality(missing, [])
    if missing_payload.get("status") != "warning":
        failures.append({"scenario": "implemented bead reversal missing warning", "expected": "warning", "actual": str(missing_payload)})
    if not any("missing required fields" in warning.lower() for warning in missing_payload.get("warnings") or []):
        failures.append({"scenario": "implemented bead reversal missing fields", "expected": "missing required fields", "actual": str(missing_payload)})

    git_only = reversal_fixture(
        [
            "Reversal workflow:",
            "- Superseded bead: tasks/beads/B123-old-work.md",
            "- Reversal target: Git revert only.",
            "- Reversal reason: Prior behavior was wrong.",
            "- Preserved behavior: pending",
            "- Approvals still required: pending",
            "Used git revert and considered it done.",
        ],
        closeout={"manual_verification": "pending", "review_decision": "revise"},
    )
    git_payload = reversal_workflow_quality(git_only, [])
    if not any("git revert" in warning.lower() for warning in git_payload.get("warnings") or []):
        failures.append({"scenario": "implemented bead reversal git-only warning", "expected": "git revert warning", "actual": str(git_payload)})

    forbidden = reversal_fixture(
        [
            "Reversal workflow:",
            "- Superseded bead: tasks/beads/B123-old-work.md",
            "- Reversal target: Reopen done bead and rewrite transition logs.",
            "- Reversal reason: Hide mistake.",
            "- Preserved behavior: none.",
            "- Reversal proof: none.",
            "- Approvals still required: none.",
            "Delete evidence and rewrite transition log.",
        ]
    )
    forbidden_payload = reversal_workflow_quality(forbidden, list(passing_checks(forbidden).values()))
    forbidden_markers = (forbidden_payload.get("details") or {}).get("forbidden_history_mutation_markers") or []
    for expected in ("delete_evidence", "rewrite_transition_log"):
        if expected not in forbidden_markers:
            failures.append({"scenario": "implemented bead reversal forbidden marker", "expected": expected, "actual": str(forbidden_payload)})

    journal = load_script_module("bead_build_journal_fixture", "update-bead-build-journal.py")
    rendered = journal.render_entry(
        {
            "timestamp": "2026-06-23T00:00:00+00:00",
            "plain_outcome": "Reversed obsolete behavior.",
            "evidence_state": "ready for review",
            "bead": complete.rel_path,
            "bead_status": "review",
            "checks": {"summary": "1 recorded check(s); latest `python3 scripts/clarity-scenario-check.py` -> pass (exit 0)."},
            "manual_verification": complete.closeout["manual_verification"],
            "review_decision": "accepted",
            "changes": {"implementation": [], "generated_evidence": []},
            "provenance": {"parent_prd": "tasks/prds/PRD-023-implemented-bead-reversal-workflow.md", "requirement_ids": ["PRD-023-FR06"]},
            "reversal": {
                "superseded_bead": "tasks/beads/B123-old-work.md",
                "reversal_target": "obsolete rule",
                "reversal_reason": "wrong behavior",
                "preserved_behavior": "evidence remains",
                "reversal_proof": "clarity scenario pass",
            },
            "remaining_uncertainty": [],
            "git": {},
        }
    )
    if "Reversal/supersession" not in rendered or "Superseded bead" not in rendered:
        failures.append({"scenario": "implemented bead reversal journal rendering", "expected": "reversal provenance", "actual": rendered})

    return 7


def assert_local_command_facade_boundaries(failures: list[dict[str, str]]) -> int:
    precode_cli = load_script_module("precode_cli_fixture", "precode_cli.py")
    parser = precode_cli.build_parser()
    args = parser.parse_args(
        [
            "--dry-run",
            "bootstrap-check",
            "--source",
            "source",
            "--target",
            "target",
            "--preview-manifest",
            "--supervised-setup-plan",
            "--apply-supervised-setup",
            "--approve-action",
            "SP-001",
        ]
    )
    commands = precode_cli.build_commands(args, parser)
    command_text = precode_cli.command_text(commands[0])
    for term in (
        "python3",
        "scripts/bootstrap-check.py",
        "--apply-supervised-setup",
        "--approve-action",
        "SP-001",
    ):
        if term not in command_text:
            failures.append({"scenario": "local command facade delegation", "expected": term, "actual": command_text})

    output = io.StringIO()
    with redirect_stdout(output):
        exit_code = precode_cli.run_commands(commands, root=Path("."), dry_run=True)
    rendered = output.getvalue()
    if exit_code != 0:
        failures.append({"scenario": "local command facade dry run", "expected": "exit 0", "actual": str(exit_code)})
    for term in ("local wrapper over existing PrecodeOS scripts", "Underlying command:"):
        if term not in rendered:
            failures.append({"scenario": "local command facade visible boundary", "expected": term, "actual": rendered})

    missing_approval_args = parser.parse_args(
        [
            "bootstrap-check",
            "--source",
            "source",
            "--target",
            "target",
            "--supervised-setup-plan",
            "--apply-supervised-setup",
        ]
    )
    try:
        with redirect_stderr(io.StringIO()):
            precode_cli.build_commands(missing_approval_args, parser)
    except SystemExit as error:
        if error.code == 0:
            failures.append({"scenario": "local command facade missing approval", "expected": "parser error", "actual": "exit 0"})
    else:
        failures.append({"scenario": "local command facade missing approval", "expected": "parser error", "actual": "accepted"})

    return 3


def assert_ralph_command_boundaries(failures: list[dict[str, str]]) -> int:
    ralph_loop = load_script_module("ralph_loop_fixture", "ralph-loop.py")
    missing_active = ralph_loop.decide(
        active_bead="",
        enabled=True,
        force=False,
        prior_count=0,
        max_attempts=3,
        guardrail={},
        attempt_result=None,
        validators=[],
        retry_policy="bounded",
    )
    if missing_active != ("missing_active_bead", "stop", False, "Ralph needs one active bead."):
        failures.append({"scenario": "ralph missing active bead", "expected": "stop", "actual": str(missing_active)})

    not_enabled = ralph_loop.decide(
        active_bead="tasks/beads/B999-clarity-fixture.md",
        enabled=False,
        force=False,
        prior_count=0,
        max_attempts=3,
        guardrail={},
        attempt_result=None,
        validators=[],
        retry_policy="bounded",
    )
    if not_enabled[0:3] != ("not_enabled", "stop", False):
        failures.append({"scenario": "ralph opt-in boundary", "expected": "not_enabled stop", "actual": str(not_enabled)})

    approval_needed = ralph_loop.decide(
        active_bead="tasks/beads/B999-clarity-fixture.md",
        enabled=True,
        force=False,
        prior_count=0,
        max_attempts=3,
        guardrail={"user_decision": "approval needed", "summary": "Ask before running this."},
        attempt_result=None,
        validators=[],
        retry_policy="bounded",
    )
    if approval_needed[0:3] != ("approval_required", "ask", False):
        failures.append({"scenario": "ralph risky attempt command", "expected": "approval_required ask", "actual": str(approval_needed)})

    summary_source = Path("scripts/ralph-loop.py").read_text(encoding="utf-8")
    for term in ('"generated_evidence_only": True', "if not args.dry_run:", "write_jsonl"):
        if term not in summary_source:
            failures.append({"scenario": "ralph generated evidence and dry-run boundary", "expected": term, "actual": "missing"})

    return 4


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
            "in progress ready for review",
            (
                next_payload(
                    bead(
                        closeout={
                            "manual_verification": "Who checked: fixture. What was checked: acceptance evidence. Environment: synthetic. Result: pass. Remaining uncertainty: none.",
                            "review_decision": "not reviewed",
                        }
                    ),
                    closeout_blockers=["review decision is missing or invalid"],
                )["details"]
                or {}
            ).get("user_decision"),
            "review",
        ),
        (
            "promotion eligible",
            (
                next_payload(
                    bead(status="review"),
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
    router_contract_scenarios = [
        ("state repair", next_payload(None), "state-repair"),
        ("scope repair", next_payload(bead(), guardrail={"status": "warning", "warnings": [], "details": {"out_of_scope_paths": ["app/page.tsx"]}}), "scope-repair"),
        (
            "transition approval",
            next_payload(
                bead(status="review"),
                promotion={"eligible": True, "blockers": [], "next_bead": "tasks/beads/B998-next.md"},
            ),
            "transition-approval",
        ),
        ("review", next_payload(bead(status="review"), promotion={"eligible": False, "blockers": ["review evidence is unclear"], "next_bead": "not recorded"}), "review"),
        ("closeout", next_payload(bead(), closeout_blockers=["manual verification is missing"]), "closeout"),
        ("unblock", next_payload(bead(status="needs_info")), "unblock"),
        ("execute", next_payload(bead()), "execute"),
        (
            "depth review",
            next_payload(bead(), depth={"status": "warning", "warnings": ["bead scope needs stronger proof"], "details": {}}),
            "depth-review",
        ),
        (
            "run contract review",
            next_payload(
                bead(),
                run_contract={
                    "status": "warning",
                    "warnings": ["run contract is required for this bead's risk"],
                    "details": {
                        "user_decision": "ask for proof",
                        "plain_english_summary": "Clarify the run contract before risky work.",
                        "stop_if": "Stop if allowed actions are unclear.",
                        "approval_prompt": "Ask the user before risky work.",
                    },
                },
            ),
            "run-contract-review",
        ),
        (
            "goal reaffirmation",
            next_payload(
                bead(),
                goal_frame={
                    "status": "warning",
                    "warnings": ["PRODUCT.md Goal Frame requires user reaffirmation before guiding workflow"],
                    "details": {"current": {**active_goal, "status": "reaffirm_needed", "requires_reaffirmation": True}},
                },
            ),
            "goal-reaffirmation",
        ),
    ]
    for name, payload, expected_category in router_contract_scenarios:
        assert_router_contract(f"router contract: {name}", payload, failures, expected_category)
    assert_session_start_router_delegation(failures)

    review_trigger_terms = [
        "do you accept these changes",
        "review request",
        "must switch the active bead to `review` first",
    ]
    review_trigger_sources = "\n".join(
        [
            Path("tasks/reference/SESSION-COMPLETION-HANDOFF-PROTOCOL.md").read_text(encoding="utf-8").lower(),
            Path("tasks/reference/PROMPT-PATTERNS.md").read_text(encoding="utf-8").lower(),
            Path("docs/PRECODE-USER-GUIDE.md").read_text(encoding="utf-8").lower(),
        ]
    )
    for term in review_trigger_terms:
        if term not in review_trigger_sources:
            failures.append({"scenario": "review trigger text contract", "expected": term, "actual": "missing"})

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
    daily_prompt_alias_scenario_count = assert_daily_prompt_alias_contract(failures)
    artifact_chooser_scenario_count = assert_artifact_chooser_contract(failures)
    onboarding_authority_scenario_count = assert_onboarding_authority_consolidation_contract(failures)
    first_product_spine_scenario_count = assert_first_product_spine_contract(failures)
    assert_stuck_recovery_contract(failures)
    assert_no_engineer_fallback_prompt_pack(failures)
    candidate_queue_scenario_count = assert_candidate_queue_contract(failures)
    hypothesis_guidance_scenario_count = assert_hypothesis_guidance_contract(failures)
    ears_acceptance_scenario_count = assert_ears_acceptance_guidance_contract(failures)
    ubiquitous_language_scenario_count = assert_ubiquitous_language_contract(failures)
    plan_loop_scenario_count = assert_plan_loop_contract(failures)
    first_prd_walkthrough_scenario_count = assert_first_prd_walkthrough_contract(failures)
    assert_bugfix_spec_lane_contract(failures)
    assert_accessibility_advisory_gate_contract(failures)
    assert_review_lanes_contract(failures)
    team_collaboration_scenario_count = assert_team_collaboration_preview_contract(failures)
    github_collaboration_scenario_count = assert_github_collaboration_hub_contract(failures)
    session_friction_scenario_count = assert_session_friction_review_contract(failures)
    build_attribution_scenario_count = assert_build_attribution_contract(failures)
    prd_handoff_scenario_count = assert_prd_handoff_readiness_contract(failures)
    release_evidence_scenario_count = assert_verification_release_evidence_contract(failures)
    requirement_to_proof_scenario_count = assert_requirement_to_proof_contract(failures)
    reversal_scenario_count = assert_implemented_bead_reversal_contract(failures)

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
        "session_friction_review": {"status": "pass", "warnings": [], "details": {"findings": []}},
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
        ("generated refresh", command_classification("python3 scripts/os-health.py", bead()).get("user_decision"), "continue"),
        ("setup apply", command_classification("python3 scripts/bootstrap-check.py --apply-supervised-setup", bead()).get("user_decision"), "continue"),
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
    generated_refresh = command_classification("python3 scripts/os-health.py", bead())
    if generated_refresh.get("class") != "generated_refresh" or "not proof by itself" not in str(
        generated_refresh.get("plain_english_summary") or ""
    ):
        failures.append(
            {
                "scenario": "generated refresh demotion",
                "expected": "generated_refresh not proof by itself",
                "actual": str(generated_refresh),
            }
        )

    boundary_scenario_count = 1
    boundary_scenario_count += assert_local_command_facade_boundaries(failures)
    boundary_scenario_count += assert_ralph_command_boundaries(failures)

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

    followthrough_base = bead(
        sections={
            "Objective": "Check reference follow-through.",
            "Done When": "The closeout warns when indirect surfaces need review.",
            "Stop If": "Follow-through ownership is unclear.",
            "Closeout Evidence": "- Result: Fixture closeout.",
        },
        closeout={
            "manual_verification": "Who checked: fixture. What was checked: reference follow-through. Environment: synthetic. Result: pass. Remaining uncertainty: none.",
            "review_decision": "accepted",
        },
    )
    followthrough_scenarios = [
        (
            "public protocol/doc change warns",
            reference_followthrough_quality(followthrough_base, [" M tasks/reference/SESSION-COMPLETION-HANDOFF-PROTOCOL.md"]),
            "needs_review",
            True,
            True,
        ),
        (
            "generated-only change prompts freshness without changelog",
            reference_followthrough_quality(followthrough_base, [" M docs-html/PRECODE-USER-GUIDE.html"]),
            "needs_review",
            False,
            True,
        ),
        (
            "public source prompts changelog",
            reference_followthrough_quality(followthrough_base, [" M scripts/os_compiler.py"]),
            "needs_review",
            True,
            True,
        ),
        (
            "roadmap candidate prompts roadmap history",
            reference_followthrough_quality(
                bead(
                    title="B999 - Roadmap Candidate Fixture",
                    parent_prd="tasks/prds/PRD-999-roadmap-candidate.md",
                    sections={
                        "Objective": "Implement maintainer roadmap candidate.",
                        "Done When": "Roadmap history is reviewed.",
                        "Stop If": "Roadmap ownership is unclear.",
                        "Closeout Evidence": "- Result: Fixture closeout.",
                    },
                    closeout=followthrough_base.closeout,
                ),
                [" M docs/PRECODE-PACKAGE-FILE-INVENTORY.md"],
            ),
            "needs_review",
            True,
            True,
        ),
        (
            "deferred note clears missing-note warning",
            reference_followthrough_quality(
                bead(
                    sections={
                        "Objective": "Check reference follow-through.",
                        "Done When": "The closeout records deferral.",
                        "Stop If": "Follow-through ownership is unclear.",
                        "Closeout Evidence": "- Result: Fixture closeout.\n- Reference follow-through: deferred because maintainer review will happen in a follow-up.",
                    },
                    closeout={**followthrough_base.closeout, "reference_followthrough": "deferred because maintainer review will happen in a follow-up"},
                ),
                [" M tasks/reference/SESSION-COMPLETION-HANDOFF-PROTOCOL.md"],
            ),
            "deferred",
            True,
            True,
        ),
        (
            "not applicable note clears missing-note warning",
            reference_followthrough_quality(
                bead(
                    sections={
                        "Objective": "Check reference follow-through.",
                        "Done When": "The closeout records not applicable.",
                        "Stop If": "Follow-through ownership is unclear.",
                        "Closeout Evidence": "- Result: Fixture closeout.\n- Reference follow-through: not applicable because generated-only changes were reviewed.",
                    },
                    closeout={**followthrough_base.closeout, "reference_followthrough": "not applicable because generated-only changes were reviewed"},
                ),
                [" M scripts/os_compiler.py"],
            ),
            "not_applicable",
            True,
            True,
        ),
    ]
    for name, payload, expected_status, expect_changelog, expect_expected in followthrough_scenarios:
        details = payload.get("details") or {}
        if payload.get("status") != expected_status:
            failures.append({"scenario": f"reference follow-through: {name}", "expected": expected_status, "actual": str(payload.get("status"))})
        if bool(details.get("maintainer_changelog_review_expected")) != expect_changelog:
            failures.append(
                {
                    "scenario": f"reference follow-through changelog: {name}",
                    "expected": str(expect_changelog),
                    "actual": str(details.get("maintainer_changelog_review_expected")),
                }
            )
        has_expected = bool(details.get("expected_followthrough"))
        if has_expected != expect_expected:
            failures.append({"scenario": f"reference follow-through expected items: {name}", "expected": str(expect_expected), "actual": str(has_expected)})
        if expected_status in {"deferred", "not_applicable"} and payload.get("warnings"):
            failures.append({"scenario": f"reference follow-through note warning: {name}", "expected": "no missing-note warning", "actual": str(payload.get("warnings"))})

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
        + len(router_contract_scenarios)
        + 1
        + daily_prompt_alias_scenario_count
        + artifact_chooser_scenario_count
        + onboarding_authority_scenario_count
        + first_product_spine_scenario_count
        + len(goal_frame_scenarios)
        + len(recovery_scenarios)
        + len(recovery_fixture_scenarios)
        + candidate_queue_scenario_count
        + hypothesis_guidance_scenario_count
        + ears_acceptance_scenario_count
        + ubiquitous_language_scenario_count
        + plan_loop_scenario_count
        + first_prd_walkthrough_scenario_count
        + 1
        + 2
        + 1
        + len(stable_fix_scenarios)
        + len(depth_scenarios)
        + len(run_contract_scenarios)
        + len(command_scenarios)
        + release_evidence_scenario_count
        + requirement_to_proof_scenario_count
        + reversal_scenario_count
        + team_collaboration_scenario_count
        + github_collaboration_scenario_count
        + session_friction_scenario_count
        + build_attribution_scenario_count
        + prd_handoff_scenario_count
        + boundary_scenario_count
        + len(freshness_scenarios)
        + len(loop_scenarios),
        "stable_decisions": sorted(STABLE_DECISIONS),
        "failures": failures,
    }
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
