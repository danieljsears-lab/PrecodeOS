#!/usr/bin/env python3
# Version: v0.1.0
# Last updated: 2026-05-19
# Owner: PrecodeOS
# Created by Dan Sears / Recode.
# SPDX-License-Identifier: Apache-2.0
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from os_compiler import CODE_EXTENSIONS, compile_state, repo_root
from os_parser import MarkdownDocument, colon_bullets


STATUSES = ["Clear", "Watch", "Drift Risk", "Recenter", "Stop and Review"]
SEVERITY = {status: index for index, status in enumerate(STATUSES)}
DIMENSION_NAMES = ["Focus", "Stop Condition", "Closure", "Evidence", "Leverage"]
IMPLEMENTATION_PREFIXES = ("app/", "src/", "lib/", "components/", "scripts/")
VAGUE_DONE_TERMS = {"improve", "better", "clean up", "polish", "etc", "and then", "as needed", "various"}
EXPLORATION_TERMS = {
    "question",
    "explore",
    "investigate",
    "discover",
    "learn whether",
    "decide whether",
    "determine",
    "validate whether",
    "evidence packet",
    "candidate",
}
NONE_MARKERS = {"", "none", "- none", "not recorded", "missing", "n/a", "not applicable"}


def status_at_least(status: str, minimum: str) -> bool:
    return SEVERITY.get(status, 0) >= SEVERITY[minimum]


def dimension(status: str, reason: str, next_move: str) -> dict[str, str]:
    return {"status": status, "reason": reason, "next_move": next_move}


def first_active_bead(state: dict[str, Any]) -> dict[str, Any] | None:
    current = state.get("current_bead")
    for bead in state.get("beads") or []:
        if bead.get("rel_path") == current:
            return bead
    return None


def active_bead_doc(root: Path, state: dict[str, Any]) -> MarkdownDocument | None:
    current = state.get("current_bead")
    if not current:
        return None
    path = root / str(current)
    if not path.is_file():
        return None
    return MarkdownDocument.load(path)


def active_bead_context(root: Path, state: dict[str, Any]) -> dict[str, Any]:
    bead = first_active_bead(state)
    doc = active_bead_doc(root, state)
    sections = doc.sections if doc else {}
    frontmatter = doc.frontmatter if doc else {}
    current = state.get("current_bead") or ""
    execution_mode = str(frontmatter.get("execution_mode") or "").strip().lower()
    status = str(frontmatter.get("status") or state.get("current_bead_status") or "").strip().lower()
    if not status and sections.get("State"):
        status = str(colon_bullets(sections["State"]).get("status") or "").strip().lower()
    return {
        "bead": bead,
        "doc": doc,
        "sections": sections,
        "frontmatter": frontmatter,
        "current_bead": current,
        "status": status,
        "execution_mode": execution_mode,
        "bead_kind": str((bead or {}).get("bead_kind") or frontmatter.get("bead_kind") or "").strip().lower(),
        "done_when": str(sections.get("Done When", "")),
        "objective": str(sections.get("Objective", "")),
        "stop_if": str(sections.get("Stop If", "")),
        "open_questions": str((state.get("todo") or {}).get("sections", {}).get("Open Questions", "")),
        "next_up": str((state.get("todo") or {}).get("sections", {}).get("Next Up", "")),
    }


def looks_implementation_path(path: str) -> bool:
    cleaned = path.strip()
    suffix = Path(cleaned).suffix
    if suffix not in CODE_EXTENSIONS:
        return False
    return cleaned.startswith(IMPLEMENTATION_PREFIXES) or suffix != ".md"


def implementation_changes(state: dict[str, Any]) -> list[str]:
    return [
        str(path)
        for path in state.get("changed_paths") or []
        if looks_implementation_path(str(path))
    ]


def is_noneish(text: str) -> bool:
    return text.strip().lower() in NONE_MARKERS


def bullet_count(text: str) -> int:
    return len([line for line in text.splitlines() if line.strip().startswith("-")])


def done_when_is_vague(text: str) -> bool:
    lowered = text.lower()
    return any(term in lowered for term in VAGUE_DONE_TERMS)


def explorer_has_question(context: dict[str, Any]) -> bool:
    text = f"{context['objective']}\n{context['done_when']}".strip().lower()
    if not text:
        return False
    if "?" in text:
        return True
    return any(term in text for term in EXPLORATION_TERMS)


def open_questions_present(text: str) -> bool:
    return bool(text.strip()) and "none" not in text.lower()


def focus_dimension(state: dict[str, Any], context: dict[str, Any]) -> dict[str, str]:
    bead = context["bead"]
    changed_code = implementation_changes(state)
    integrity = state.get("state_integrity") or {}
    integrity_warnings = integrity.get("warnings") or []
    guardrail = state.get("files_in_play_guardrail") or {}
    out_of_scope = (guardrail.get("details") or {}).get("out_of_scope_paths") or []
    in_progress = ((integrity.get("details") or {}).get("in_progress_beads") or [])

    if not bead:
        if changed_code:
            return dimension(
                "Recenter",
                "No active bead is selected while implementation-looking files have changed.",
                "Stop and select or create one active bead before continuing implementation.",
            )
        return dimension(
            "Watch",
            "No active bead is selected, so Precode cannot fully evaluate the current work.",
            "If you are exploring, create or select an explorer bead with one question and one stopping condition.",
        )

    if len(in_progress) != 1:
        return dimension(
            "Recenter",
            "Precode does not have exactly one in-progress bead.",
            "Recenter on one active bead before continuing.",
        )
    if any("todo current_bead does not match" in str(warning) for warning in integrity_warnings):
        return dimension(
            "Recenter",
            "tasks/todo.md and the active bead disagree about current work.",
            "Repair active state before continuing.",
        )
    if out_of_scope:
        return dimension(
            "Drift Risk",
            "Changed files appear outside the active bead files in play.",
            "Pick one active goal and park the rest. Which one should stay active?",
        )

    if context["execution_mode"] == "explorer":
        if explorer_has_question(context):
            return dimension(
                "Clear",
                "Explorer mode has a named question or outcome.",
                "Keep exploration bounded, then capture findings and converge on one next move.",
            )
        return dimension(
            "Watch",
            "Explorer mode is active but the exploration question is not explicit.",
            "Name the question this exploration is trying to answer.",
        )

    return dimension(
        "Clear",
        "One active bead is selected and no scope split is visible.",
        "Continue inside the current work boundary.",
    )


def stop_condition_dimension(context: dict[str, Any]) -> dict[str, str]:
    done_when = context["done_when"]
    if not context["bead"]:
        return dimension(
            "Watch",
            "No active bead is selected, so no stopping condition is available to inspect.",
            "If you are exploring, create or select an explorer bead with one question and one stopping condition.",
        )
    if not done_when.strip():
        status = "Watch" if context["execution_mode"] == "explorer" else "Drift Risk"
        return dimension(
            status,
            "The current work has no Done When section.",
            "Add one observable stopping condition before continuing.",
        )
    if done_when_is_vague(done_when):
        return dimension(
            "Watch",
            "Done When language may be too vague to tell when to stop.",
            "Tighten the done-when so it is clear when to stop.",
        )
    if bullet_count(done_when) > 5:
        return dimension(
            "Watch",
            "Done When has many bullets, which may hide more than one loop.",
            "Confirm this is one current loop or split the extra work into follow-up beads.",
        )
    return dimension(
        "Clear",
        "The current work has a visible stopping condition.",
        "Use the done-when as the stop line for this loop.",
    )


def closure_dimension(state: dict[str, Any], context: dict[str, Any]) -> dict[str, str]:
    status = context["status"]
    completion = state.get("completion_handoff") or {}
    details = completion.get("details") or {}
    readiness = state.get("readiness") or {}
    promotion = readiness.get("current_promotion") or {}

    if promotion.get("eligible"):
        return dimension(
            "Stop and Review",
            "The active bead appears eligible for transition review.",
            "Review evidence before activating any next bead.",
        )
    if status in {"review", "done"}:
        return dimension(
            "Stop and Review",
            "The active bead is already in review or done state.",
            "Review evidence before continuing or approving transition.",
        )
    if details.get("closeout_status") == "complete" and status == "in_progress":
        return dimension(
            "Stop and Review",
            "The current loop appears ready for closeout while the bead is still in progress.",
            "This loop appears ready for closeout. Review evidence before continuing.",
        )
    if open_questions_present(context["open_questions"]):
        return dimension(
            "Watch",
            "Open questions are present in active work.",
            "Route or resolve the open question before treating this loop as closed.",
        )
    return dimension(
        "Clear",
        "No closure blocker is visible.",
        "Close, park, or route new work before widening the loop.",
    )


def evidence_dimension(state: dict[str, Any], context: dict[str, Any]) -> dict[str, str]:
    bead = context["bead"] or {}
    if not bead:
        return dimension(
            "Watch",
            "No active bead is selected, so no proof path is available to inspect.",
            "Select or create a bead before relying on implementation evidence.",
        )
    checks = bead.get("checks") or []
    rows = state.get("active_bead_checks") or []
    failing = [row for row in rows if row.get("status") == "fail"]
    missing = [row for row in rows if row.get("status") == "missing"]
    completion = state.get("completion_handoff") or {}
    closeout_blockers = (completion.get("details") or {}).get("closeout_blockers") or []
    near_closeout = context["status"] in {"review", "done"} or (completion.get("details") or {}).get("closeout_status") == "complete"

    if failing:
        return dimension(
            "Drift Risk",
            "A recorded check is failing.",
            "Fix or route the failing evidence before accepting the loop.",
        )
    if near_closeout and (missing or closeout_blockers):
        return dimension(
            "Stop and Review",
            "The loop is near closeout but proof or review evidence is missing.",
            "Stop and review the missing evidence before continuing.",
        )
    if not checks:
        return dimension(
            "Watch",
            "The active bead does not list checks.",
            "Name the proof path before relying on this work.",
        )
    if missing:
        return dimension(
            "Watch",
            "Some declared checks have not been recorded yet.",
            "Run and record the declared checks before acceptance.",
        )
    return dimension(
        "Clear",
        "No evidence gap is visible for the current phase.",
        "Keep recording checks when proof is due.",
    )


def leverage_dimension(state: dict[str, Any], context: dict[str, Any]) -> dict[str, str]:
    workflow = state.get("workflow_planning") or {}
    intent = state.get("intent_orchestration") or {}
    state_integrity = state.get("state_integrity") or {}
    warnings = [
        *(workflow.get("warnings") or []),
        *(intent.get("warnings") or []),
        *(state_integrity.get("warnings") or []),
    ]
    next_up_count = bullet_count(context["next_up"])

    if any("generated reports" in str(warning).lower() for warning in warnings):
        return dimension(
            "Watch",
            "Generated reports appear close to active intent or workflow surfaces.",
            "Use generated reports as evidence only; keep active direction in owner files.",
        )
    if next_up_count > 3:
        return dimension(
            "Watch",
            "Next Up contains several items, which can make Precode feel like a backlog.",
            "Keep Next Up short and route extra ideas to a PRD, bead proposal, or long-horizon review.",
        )
    if open_questions_present(context["open_questions"]):
        return dimension(
            "Watch",
            "Open questions are still active, so steering may get harder.",
            "Park, route, or answer open questions before widening work.",
        )
    return dimension(
        "Clear",
        "Precode is keeping the current work easy to steer.",
        "Use checkpoint or closeout when the loop changes state.",
    )


def overall_status(dimensions: dict[str, dict[str, str]]) -> str:
    focus_status = dimensions["Focus"]["status"]
    if status_at_least(focus_status, "Drift Risk"):
        return focus_status
    if any(item["status"] == "Stop and Review" for item in dimensions.values()):
        return "Stop and Review"
    return max((item["status"] for item in dimensions.values()), key=lambda status: SEVERITY[status])


def top_dimension(status: str, dimensions: dict[str, dict[str, str]]) -> dict[str, str]:
    if status_at_least(dimensions["Focus"]["status"], "Drift Risk"):
        item = dimensions["Focus"]
        return {"name": "Focus", **item}
    for name in DIMENSION_NAMES:
        item = dimensions[name]
        if item["status"] == status:
            return {"name": name, **item}
    name, item = max(dimensions.items(), key=lambda pair: SEVERITY[pair[1]["status"]])
    return {"name": name, **item}


def build_payload(root: Path) -> dict[str, Any]:
    state = compile_state(root)
    context = active_bead_context(root, state)
    dimensions = {
        "Focus": focus_dimension(state, context),
        "Stop Condition": stop_condition_dimension(context),
        "Closure": closure_dimension(state, context),
        "Evidence": evidence_dimension(state, context),
        "Leverage": leverage_dimension(state, context),
    }
    status = overall_status(dimensions)
    top = top_dimension(status, dimensions)
    mode = context["execution_mode"] or "unspecified"

    return {
        "tool": "loop-health",
        "status": status,
        "dimensions": dimensions,
        "top_risk": top["reason"],
        "top_dimension": top["name"],
        "next_move": top["next_move"],
        "mode": mode,
        "current_bead": context["current_bead"] or "missing",
        "advisory_only": True,
    }


def render_compact(payload: dict[str, Any]) -> str:
    return "\n".join(
        [
            f"Build Loop Health: {payload['status']}",
            "",
            "Top risk:",
            str(payload["top_risk"]),
            "",
            "Next move:",
            str(payload["next_move"]),
        ]
    )


def render_verbose(payload: dict[str, Any]) -> str:
    lines = [f"Build Loop Health: {payload['status']}", ""]
    dimensions = payload.get("dimensions") or {}
    for name in DIMENSION_NAMES:
        item = dimensions.get(name) or {}
        lines.append(f"{name}: {item.get('status', 'Watch')}")
    lines.extend(["", "Top risk:", str(payload["top_risk"]), "", "Next move:", str(payload["next_move"])])
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Show Build Loop Health for the current Precode workspace.")
    parser.add_argument("--json", action="store_true", help="print machine-readable Build Loop Health")
    parser.add_argument("--verbose", action="store_true", help="print dimension-level Build Loop Health")
    args = parser.parse_args()

    payload = build_payload(repo_root())
    if args.json:
        print(json.dumps(payload, indent=2, sort_keys=True))
    elif args.verbose:
        print(render_verbose(payload))
    else:
        print(render_compact(payload))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
