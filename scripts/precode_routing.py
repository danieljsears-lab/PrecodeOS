#!/usr/bin/env python3
# Version: v0.1.3
# Last updated: 2026-06-23
# Owner: PrecodeOS
# Created by Dan Sears / Recode.
# SPDX-License-Identifier: Apache-2.0
from __future__ import annotations

from pathlib import Path
from typing import Any


ACTIVE_MEMORY = ["AGENT.md", "DECISIONS.md", "tasks/todo.md"]
GENERATED_REPORTS = ["PRECODE-HELP.md", "PROGRESS.md", "OS-HEALTH.md"]
REFERENCE_BY_CATEGORY = {
    "state-repair": "tasks/reference/STATE-MANAGEMENT-PROTOCOL.md",
    "scope-repair": "tasks/reference/CONTEXT-ENGINEERING-PROTOCOL.md",
    "accepted-hold": "tasks/reference/SESSION-COMPLETION-HANDOFF-PROTOCOL.md",
    "transition-approval": "tasks/reference/SESSION-COMPLETION-HANDOFF-PROTOCOL.md",
    "review": "modes/REVIEW.md",
    "closeout": "tasks/reference/SESSION-COMPLETION-HANDOFF-PROTOCOL.md",
    "unblock": "tasks/reference/RECOVERY-PROTOCOL.md",
    "execute": "modes/BUILDER.md",
    "depth-review": "tasks/reference/DECOMPOSITION-PROTOCOL.md",
    "run-contract-review": "tasks/reference/TOOL-EXECUTION-PROTOCOL.md",
    "goal-reaffirmation": "tasks/reference/GOAL-FRAME-PROTOCOL.md",
}


def bead_value(bead: Any, name: str, default: Any = None) -> Any:
    if bead is None:
        return default
    if isinstance(bead, dict):
        return bead.get(name, default)
    return getattr(bead, name, default)


def line_count(root: Path, rel: str) -> int:
    cleaned = str(rel or "").strip().strip("`")
    if not cleaned:
        return 0
    path = root / cleaned
    if not path.is_file():
        return 0
    return len(path.read_text(encoding="utf-8").splitlines())


def compact_unique(items: list[str]) -> list[str]:
    seen: set[str] = set()
    compact: list[str] = []
    for item in items:
        cleaned = str(item or "").strip().strip("`")
        if cleaned and cleaned not in seen:
            seen.add(cleaned)
            compact.append(cleaned)
    return compact


def closeout_blockers_are_review_only(blockers: list[Any]) -> bool:
    if not blockers:
        return False
    normalized = [str(item or "").lower() for item in blockers]
    return all("review decision" in item for item in normalized)


def context_footprint(root: Path, todo: dict[str, Any], bead: Any, single_next_protocol: str) -> dict[str, Any]:
    current_bead = bead_value(bead, "rel_path", todo.get("current_bead") or "missing")
    primary_authority = bead_value(bead, "primary_authority", "") or ""
    parent_prd = bead_value(bead, "parent_prd", "") or ""
    required = compact_unique([*ACTIVE_MEMORY, current_bead, primary_authority])
    conditional = compact_unique([parent_prd, single_next_protocol])
    generated_touched = ["logs/next-step.json", "PRECODE-HELP.md"]
    document_lines = {path: line_count(root, path) for path in compact_unique([*required, *conditional])}
    total_lines = sum(document_lines.values())

    return {
        "advisory_only": True,
        "active_memory": ACTIVE_MEMORY,
        "active_bead": current_bead,
        "primary_authority": primary_authority or "missing",
        "required_context": required,
        "conditional_references": conditional,
        "generated_reports_touched": generated_touched,
        "approx_document_lines": total_lines,
        "document_lines": document_lines,
        "budget_rule": "Prepare a checkpoint, compaction, restart, or handoff around 80% context usage.",
        "why_this_matters": "Precode should route the agent to the smallest useful context instead of loading every protocol.",
    }


def load_plan(category: str, single_next_protocol: str) -> dict[str, Any]:
    return {
        "required_first": ACTIVE_MEMORY,
        "then_load": ["active bead", "primary authority"],
        "single_next_protocol": single_next_protocol,
        "why_not_more_context": (
            "Load only this next protocol or mode unless the active bead, primary authority, or a blocking warning "
            "proves another owner file is needed."
        ),
        "router_owner": "scripts/next-step.py",
        "decision_category": category,
    }


def next_step_guidance(
    root: Path,
    todo: dict[str, Any],
    bead: Any,
    promotion_state: dict[str, Any],
    completion_state: dict[str, Any],
    workflow_state: dict[str, Any],
    depth_state: dict[str, Any],
    guardrail_state: dict[str, Any],
    run_contract_state: dict[str, Any],
    goal_frame_state: dict[str, Any],
    stable_fix_state: dict[str, Any] | None = None,
) -> dict[str, Any]:
    warnings: list[str] = []
    todo_sections = todo.get("sections") or {}
    open_questions = str(todo_sections.get("Open Questions", "")).strip()
    blockers: list[str] = []
    action = "repair active state before continuing"
    category = "state-repair"
    user_decision = "repair state"
    summary = "Repair Precode state before continuing."
    stop_if = "Stop if the agent cannot name the active bead, authority file, files in play, and checks."
    approval_prompt = "Ask the agent to repair active state before editing."
    accepted_hold: dict[str, Any] = {}

    if not bead:
        blockers.append("current bead is missing")
    else:
        closeout_blockers = (completion_state.get("details") or {}).get("closeout_blockers") or []
        accepted_hold = (completion_state.get("details") or {}).get("accepted_hold") or {}
        promotion_blockers = promotion_state.get("blockers") or []
        guard_details = guardrail_state.get("details") or {}
        out_of_scope = guard_details.get("out_of_scope_paths") or []
        bead_status = str(bead_value(bead, "status", "missing"))
        if bead_status in {"needs_info", "manual_testing"}:
            category = "unblock"
            action = "record the missing input, owner, and blocked escape path or create a narrow unblocker bead"
            user_decision = "ask for missing info"
            summary = "Do not code around the blocker. Name the missing input, owner, and safe escape path."
            stop_if = "Stop if the agent proposes a workaround instead of documenting the blocker or creating a narrow unblocker bead."
            approval_prompt = "Ask the user for the missing input or approval to create a narrow unblocker bead."
        elif out_of_scope:
            category = "scope-repair"
            action = "stop and resolve changed files outside the active bead before continuing"
            user_decision = "stop"
            summary = "Stop: changed files appear outside the approved task."
            stop_if = "Stop until each out-of-scope path is explained as generated evidence, current-bead work, or a separate follow-up."
            approval_prompt = "Ask the user whether to revert, split, or explicitly approve the scope change."
        elif accepted_hold.get("eligible"):
            category = "accepted-hold"
            action = "author or propose the next bead before transition; do not continue implementation or repeat acceptance review"
            blockers.extend(str(item) for item in promotion_blockers[:6])
            user_decision = "author next bead"
            summary = "The active bead is accepted and held; scope or author the next bead before asking for transition approval."
            stop_if = "Stop if the agent treats the accepted hold as unfinished implementation, repeats acceptance review, or activates a next bead without approval."
            approval_prompt = "Ask the agent to scope or author the next bead, then show the transition proposal without approving it."
        elif promotion_state.get("eligible"):
            category = "transition-approval"
            action = "review the transition proposal; user approval is required before activating the next bead"
            user_decision = "approve transition"
            summary = "Review the proposed next bead. Do not activate it until the user approves the transition."
            stop_if = "Stop if acceptance evidence or next-bead readiness is unclear."
            approval_prompt = "Ask the user whether to approve the transition with `python3 scripts/bead-transition.py --approve`."
        elif bead_status in {"review", "done"}:
            category = "review"
            action = "resolve promotion blockers before proposing or approving the next bead"
            blockers.extend(str(item) for item in promotion_blockers[:6])
            user_decision = "review"
            summary = "Review the evidence and blockers before accepting, revising, splitting, or blocking the bead."
            stop_if = "Stop if the recommendation relies on confidence instead of recorded evidence."
            approval_prompt = "Ask the user for a review decision: accepted, revise, split, blocked, or stop."
        elif bead_status == "in_progress" and closeout_blockers_are_review_only(closeout_blockers):
            category = "review"
            action = "switch the active bead to review and ask for an acceptance recommendation before any done or transition state"
            blockers.extend(str(item) for item in closeout_blockers[:6])
            user_decision = "review"
            summary = "The bead is ready for acceptance review; do not mark it done or approve transition from review intent alone."
            stop_if = "Stop if a review-request phrase such as `do you accept these changes?` is treated as done, transition approval, or automatic acceptance."
            approval_prompt = "Ask the user for a review decision: accepted, revise, split, blocked, or stop."
        elif closeout_blockers:
            category = "closeout"
            action = "finish active bead evidence, manual verification, and review decision"
            blockers.extend(str(item) for item in closeout_blockers[:6])
            user_decision = "ask for proof"
            summary = "The work may be close, but proof or review evidence is missing."
            stop_if = "Stop if checks, manual verification, or review decision are missing."
            approval_prompt = "Ask the agent to record the missing proof before accepting work."
        else:
            category = "execute"
            action = "work only inside the active bead, then run and record its declared checks"
            user_decision = "continue"
            summary = "Continue inside the active bead only, then record the declared checks."
            stop_if = "Stop if scope widens, sensitive work appears, files drift outside files_in_play, or the proof path becomes unclear."
            approval_prompt = "No new approval is suggested before continuing the current approved bead."

    if open_questions and "none" not in open_questions.lower():
        warnings.append("tasks/todo.md has open questions that may need resolution before implementation")
    if depth_state.get("status") == "warning":
        depth_warnings = depth_state.get("warnings") or []
        if depth_warnings:
            warnings.append(f"adaptive depth affects this decision: {depth_warnings[0]}")
            if category == "execute":
                category = "depth-review"
                user_decision = "ask for proof"
                summary = "Before continuing, ask whether the bead needs more planning, checks, stop conditions, or approval."
                approval_prompt = "Ask the agent to explain the adaptive-depth warning in plain English."
    if run_contract_state.get("status") == "warning":
        contract_warnings = run_contract_state.get("warnings") or []
        contract_details = run_contract_state.get("details") or {}
        if contract_warnings:
            warnings.append(f"run contract affects this decision: {contract_warnings[0]}")
            if category == "execute":
                category = "run-contract-review"
                user_decision = str(contract_details.get("user_decision") or "ask for proof")
                summary = str(
                    contract_details.get("plain_english_summary")
                    or "Before continuing, clarify allowed actions and proof needed."
                )
                action = "clarify allowed actions, proof needed, approval gates, and stop conditions before risky work"
                stop_if = str(
                    contract_details.get("stop_if")
                    or "Stop if allowed actions, proof needed, approval gates, or rollback path are unclear."
                )
                approval_prompt = str(
                    contract_details.get("approval_prompt")
                    or "Ask the user to approve risky work only after the run contract is clear."
                )
    stable_fix_state = stable_fix_state or {}
    stable_fix_details = stable_fix_state.get("details") or {}
    if stable_fix_state.get("status") == "warning":
        stable_fix_warnings = stable_fix_state.get("warnings") or []
        if stable_fix_warnings:
            warnings.append(f"stable-fix eligibility affects this decision: {stable_fix_warnings[0]}")
    guard_details = guardrail_state.get("details") or {}
    if guard_details.get("out_of_scope_paths"):
        warnings.append("files-in-play guardrail found out-of-scope changed files")
    goal_details = goal_frame_state.get("details") or {}
    current_goal = goal_details.get("current") or {}
    if current_goal:
        goal_status = str(current_goal.get("status") or "draft")
        requires_goal_reaffirmation = goal_status == "reaffirm_needed" or bool(current_goal.get("requires_reaffirmation"))
        if requires_goal_reaffirmation:
            warnings.append("current Goal Frame requires reaffirmation before guiding workflow")
            for blocker in (current_goal.get("fit_blockers") or [])[:3]:
                warnings.append(str(blocker))
            if category in {"execute", "depth-review"}:
                category = "goal-reaffirmation"
                user_decision = "ask for reaffirmation"
                summary = "Reaffirm the current Goal Frame before using it to guide workflow."
                action = "ask the user whether the current Goal Frame still applies"
                stop_if = "Stop if the Goal Frame is stale, conflicts with the active bead, or starts acting like a task list."
                approval_prompt = "Ask the user to reaffirm, revise, or retire the Goal Frame before using it for workflow guidance."
        elif goal_status == "active":
            warnings.extend(str(warning) for warning in (goal_frame_state.get("warnings") or [])[:3])
    elif goal_frame_state.get("warnings"):
        warnings.append("Goal Frame warnings exist, but no current active Goal Frame was selected")

    recovery_flow, beginner_prompt = recovery_prompt_for_next_step(category, warnings, blockers)
    single_next_protocol = REFERENCE_BY_CATEGORY.get(category, "tasks/reference/CONTEXT-ENGINEERING-PROTOCOL.md")
    if recovery_flow != "none":
        single_next_protocol = "tasks/reference/RECOVERY-PROTOCOL.md"
    footprint = context_footprint(root, todo, bead, single_next_protocol)

    return {
        "status": "warning" if warnings or blockers else "pass",
        "warnings": warnings,
        "stable_fix_eligibility": stable_fix_state,
        "details": {
            "current_bead": bead_value(bead, "rel_path", todo.get("current_bead") or "missing"),
            "current_bead_status": bead_value(bead, "status", "missing"),
            "recommended_action": action,
            "action_category": category,
            "plain_english_summary": summary,
            "user_decision": user_decision,
            "single_next_protocol": single_next_protocol,
            "load_plan": load_plan(category, single_next_protocol),
            "context_footprint": footprint,
            "why_not_more_context": (
                "More context is useful only when the active bead, authority file, or this router decision points to it."
            ),
            "why_this_matters": (
                "Precode should reduce the beginner's next decision to continue, ask, reaffirm, review, author next bead, approve, "
                "repair, or stop."
            ),
            "stop_if": stop_if,
            "approval_prompt": approval_prompt,
            "blockers": sorted(set(blockers)),
            "open_questions": open_questions or "none",
            "needs_prd": bool((workflow_state.get("details") or {}).get("artifact_to_produce_next") == "PRD shard"),
            "needs_review": category in {"review", "transition-approval", "closeout"},
            "needs_transition": bool(promotion_state.get("eligible")),
            "next_bead": promotion_state.get("next_bead") or "not recorded",
            "accepted_hold": accepted_hold,
            "goal_frame": current_goal or {},
            "goal_frame_advisory": "Goal Frames can guide workflow selection only; they cannot choose tasks, approve transitions, or override active memory.",
            "stable_fix_eligibility": stable_fix_details,
            "stable_fix_advisory": "Stable-fix eligibility is advisory only; it cannot approve edits, recovery, release, rollback, transitions, setup mutation, or package update behavior.",
            "recovery_flow": recovery_flow,
            "recovery_protocol": "tasks/reference/RECOVERY-PROTOCOL.md",
            "beginner_prompt": beginner_prompt,
            "advisory_only": True,
        },
    }


def recovery_prompt_for_next_step(category: str, warnings: list[str], blockers: list[str]) -> tuple[str, str]:
    warning_text = " ".join(warnings).lower()
    blocker_text = " ".join(blockers).lower()
    combined = f"{warning_text} {blocker_text}"
    if "generated report" in combined or "generated-report" in combined:
        return (
            "generated-report-confusion",
            "Use the Recovery Protocol for generated-report confusion. Repair source state first; do not hand-edit generated reports or treat them as authority.",
        )
    prompts = {
        "state-repair": (
            "active-state-repair",
            "Use the Recovery Protocol for active-state repair. Stop before editing, identify the owner file, then validate memory and state.",
        ),
        "scope-repair": (
            "scope-expansion",
            "Use the Recovery Protocol for scope expansion. Explain each out-of-scope path as generated evidence, current-bead work, or separate follow-up before continuing.",
        ),
        "closeout": (
            "missing-proof",
            "Use the Recovery Protocol for missing proof. Name the missing checks or manual verification before accepting the work.",
        ),
        "unblock": (
            "blocked-work",
            "Use the Recovery Protocol for blocked work. Record the missing input, owner, and escape path instead of coding around the blocker.",
        ),
        "depth-review": (
            "planning-or-proof-review",
            "Use the Recovery Protocol for unclear proof or planning depth. Stop and ask whether the work needs stronger checks, stop conditions, or approval.",
        ),
        "run-contract-review": (
            "planning-or-proof-review",
            "Use the Recovery Protocol for unclear allowed actions or proof. Stop and clarify the Run Contract before risky work.",
        ),
        "goal-reaffirmation": (
            "context-reaffirmation",
            "Use the Recovery Protocol for context confusion. Reaffirm the Goal Frame before letting it guide workflow.",
        ),
    }
    return prompts.get(category, ("none", ""))
