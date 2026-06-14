#!/usr/bin/env python3
# Version: v0.1.0
# Last updated: 2026-06-14
# Owner: PrecodeOS
# Created by Dan Sears / Recode.
# SPDX-License-Identifier: Apache-2.0
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from os_parser import bullet_items


def render_memory_index_markdown(memory: dict[str, Any]) -> str:
    details = memory.get("details") if isinstance(memory.get("details"), dict) else {}
    cards = details.get("cards") if isinstance(details.get("cards"), list) else []
    warnings = memory.get("warnings") if isinstance(memory.get("warnings"), list) else []

    def cell(value: Any) -> str:
        return str(value or "missing").replace("|", "\\|")

    def card_table(selected: list[dict[str, Any]]) -> str:
        rows: list[str] = []
        for card in selected:
            if not isinstance(card, dict):
                continue
            notes = "; ".join(card.get("warnings") or [])
            rows.append(
                "| "
                + " | ".join(
                    [
                        f"`{cell(card.get('path'))}`",
                        cell(card.get("title")),
                        cell(card.get("category")),
                        cell(card.get("freshness")),
                        cell(card.get("status")),
                        cell(card.get("authority_owner_if_promoted") or "none"),
                        cell(notes or "none"),
                        cell(card.get("summary")),
                    ]
                )
                + " |"
            )
        return "\n".join(
            [
                "| Card | Title | Category | Freshness | Status | Promotion owner | Warnings | Summary |",
                "| --- | --- | --- | --- | --- | --- | --- | --- |",
                *rows,
            ]
        ) if rows else "- No matching reviewed memory cards."

    def citation_list(selected: list[dict[str, Any]]) -> str:
        lines: list[str] = []
        for card in selected:
            citation = card.get("citation") if isinstance(card.get("citation"), dict) else {}
            sources = citation.get("source_pointers") or []
            source_text = ", ".join(str(source) for source in sources) if sources else "none"
            lines.append(
                "- "
                + f"`{citation.get('path', 'missing')}`: {citation.get('title', 'missing')} "
                + f"[{citation.get('category', 'missing')}, {citation.get('freshness', 'missing')}, {citation.get('status', 'missing')}] "
                + f"sources: {source_text}; promotion owner: {citation.get('authority_owner_if_promoted', 'none')}"
            )
        return "\n".join(lines) if lines else "- No citations available."

    current_cards = details.get("current_cards") if isinstance(details.get("current_cards"), list) else []
    promotion_needed_cards = details.get("promotion_needed_cards") if isinstance(details.get("promotion_needed_cards"), list) else []
    stale_or_superseded_cards = details.get("stale_or_superseded_cards") if isinstance(details.get("stale_or_superseded_cards"), list) else []
    low_confidence_cards = details.get("low_confidence_cards") if isinstance(details.get("low_confidence_cards"), list) else []
    glossary_terms = details.get("glossary_terms") if isinstance(details.get("glossary_terms"), list) else []

    return f"""# PrecodeOS -- Memory Index
<!-- ANCHOR: memory-index -->

> AUTHORITY: Generated index of reviewed Precode filesystem memory cards.
> NOT_AUTHORITY: Active memory, task selection, product decisions, feature requirements, implementation plans, route structure, schema definitions, bead state, or generated progress state.
> LOAD_WHEN: Searching or auditing reviewed memory; never as active session memory or a task plan.
> CLASS: generated
>
> Generated from reviewed memory cards and `scripts/update-memory-index.py` or `scripts/os-health.py`.
> Do not use this file as active memory.
> Working memory lives in `AGENT.md`, `DECISIONS.md`, and `tasks/todo.md`.

Generated at: `{datetime.now(timezone.utc).isoformat()}`

## Reading Rule

Use this index to find reviewed memory cards. Before acting, return to active memory, the active bead, and the primary authority file.

Use this prompt when asking an agent to search memory:

```text
{details.get('safe_usage_prompt', 'Search reviewed memory, cite matching cards, and treat memory as evidence only.')}
```

## Summary

- Status: {memory.get('status', 'missing')}
- Reviewed memory cards: {details.get('card_count', 0)}
- Project glossary cards: {len(details.get('glossary_terms') or [])}
- Promotion-needed cards: {len(details.get('promotion_needed') or [])}
- Stale or superseded cards: {len(details.get('stale_or_superseded') or [])}
- Generated-evidence warning: {memory.get('generated_report_warning', MEMORY_GENERATED_WARNING)}

## Current Reviewed Cards

{card_table(current_cards)}

## Promotion Needed

{card_table(promotion_needed_cards)}

## Stale, Superseded, Or Archived

{card_table(stale_or_superseded_cards)}

## Low Confidence

{card_table(low_confidence_cards)}

## Project Glossary Cards

{card_table([card for card in cards if isinstance(card, dict) and card.get('category') == 'project_glossary'])}

## Citation List

{citation_list(cards)}

## Warnings

{chr(10).join(f"- {warning}" for warning in warnings) if warnings else "- No first-pass memory warnings."}
"""


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def render_simple_yaml(value: Any, indent: int = 0) -> str:
    pad = " " * indent
    if isinstance(value, dict):
        lines: list[str] = []
        for key, item in value.items():
            if isinstance(item, (dict, list)):
                lines.append(f"{pad}{key}:")
                lines.append(render_simple_yaml(item, indent + 2))
            else:
                lines.append(f"{pad}{key}: {json.dumps(item)}")
        return "\n".join(lines)
    if isinstance(value, list):
        if not value:
            return f"{pad}[]"
        lines = []
        for item in value:
            if isinstance(item, (dict, list)):
                lines.append(f"{pad}-")
                lines.append(render_simple_yaml(item, indent + 2))
            else:
                lines.append(f"{pad}- {json.dumps(item)}")
        return "\n".join(lines)
    return f"{pad}{json.dumps(value)}"


def write_yaml(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(render_simple_yaml(payload) + "\n", encoding="utf-8")


def write_events_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, separators=(",", ":")) + "\n")


def render_handoff_packet(payload: dict[str, Any]) -> str:
    completion = payload.get("completion_handoff") or {}
    details = completion.get("details") or {}
    packet = details.get("handoff_packet") or {}
    warnings = completion.get("warnings") or []

    def item(name: str) -> str:
        return str(packet.get(name) or "not recorded")

    return f"""# PrecodeOS -- Handoff Packet
<!-- ANCHOR: handoff-packet -->

> AUTHORITY: Generated handoff orientation snapshot for the current PrecodeOS session.
> NOT_AUTHORITY: Active memory, task selection, product decisions, review acceptance, transition approval, implementation plans, or external mutations.
> LOAD_WHEN: Preparing an agent handoff or reviewing completion state; never as active session memory.
> CLASS: generated
>
> Generated from `scripts/os_compiler.py`.
> Generated by PrecodeOS, created by Dan Sears / Recode.
> Do not use this file as active memory.
> Working memory lives in `AGENT.md`, `DECISIONS.md`, and `tasks/todo.md`.

Generated at: `{payload.get('generated_at')}`

## Context Pack

- Active bead: `{item('active bead')}`
- State: `{item('state')}`
- Primary authority: `{item('primary authority')}`
- Next safe action: {item('next safe action')}
- Generated-report warning: {item('generated-report warning')}

## Done When

{item('done-when')}

## Files In Play

{item('files in play')}

## Out Of Scope

{item('out of scope')}

## Checks

{item('checks')}

## Allowed Actions

{item('allowed actions')}

## Proof Needed

{item('proof needed')}

## Stop Conditions

{item('stop conditions')}

## Open Questions

{item('open questions')}

## Latest Evidence

{item('latest evidence')}

## Blockers

{item('blockers')}

## Completion Warnings

{chr(10).join(f"- {warning}" for warning in warnings) if warnings else "- No first-pass completion or handoff warnings."}
"""


def render_precode_help(payload: dict[str, Any]) -> str:
    next_step = payload.get("next_step") or {}
    next_details = next_step.get("details") or {}
    depth = payload.get("bead_depth") or {}
    depth_details = depth.get("details") or {}
    guardrail = payload.get("files_in_play_guardrail") or {}
    guardrail_details = guardrail.get("details") or {}
    run_contract = payload.get("run_contract") or {}
    run_details = run_contract.get("details") or {}
    goal_frame = payload.get("goal_frame") or {}
    goal_details = goal_frame.get("details") or {}
    current_goal = goal_details.get("current") or {}
    stable_fix = payload.get("stable_fix_eligibility") or {}
    stable_fix_details = stable_fix.get("details") or {}
    blockers = next_details.get("blockers") or []
    load_plan = next_details.get("load_plan") or {}
    context_footprint = next_details.get("context_footprint") or {}

    return f"""# Precode Help
<!-- ANCHOR: precode-help -->

> AUTHORITY: Generated next-step guidance for the current PrecodeOS workspace.
> NOT_AUTHORITY: Active memory, task selection authority, product decisions, implementation plans, review acceptance, bead transition approval, or command approval.
> LOAD_WHEN: A user wants a quick generated hint about what Precode expects next; never as active session memory.
> CLASS: generated
>
> Generated from `scripts/os_compiler.py`.
> Generated by PrecodeOS, created by Dan Sears / Recode.
> Do not use this file as active memory.
> Working memory lives in `AGENT.md`, `DECISIONS.md`, and `tasks/todo.md`.

Generated at: `{payload.get('generated_at')}`

## Next Step

- What to do now: {next_details.get('plain_english_summary', next_details.get('recommended_action', 'repair active state before continuing'))}
- User decision: `{next_details.get('user_decision', 'repair state')}`
- Active bead: `{next_details.get('current_bead', 'missing')}`
- State: `{next_details.get('current_bead_status', 'missing')}`
- Recommended action: {next_details.get('recommended_action', 'repair active state before continuing')}
- Action category: `{next_details.get('action_category', 'unknown')}`
- Single next protocol: `{next_details.get('single_next_protocol', 'not recorded')}`
- Why not more context: {next_details.get('why_not_more_context', 'Load only what the active bead proves is needed.')}
- Stop if: {next_details.get('stop_if', 'stop if workflow, scope, evidence, or approval is unclear')}
- Approval prompt: {next_details.get('approval_prompt', 'No approval prompt compiled.')}
- Needs review: {next_details.get('needs_review', False)}
- Needs transition approval: {next_details.get('needs_transition', False)}
- Next bead: `{next_details.get('next_bead', 'not recorded')}`

## Load Plan

- Router owner: `{load_plan.get('router_owner', 'scripts/next-step.py')}`
- Required first: `{', '.join(load_plan.get('required_first') or [])}`
- Then load: `{', '.join(load_plan.get('then_load') or [])}`
- Single next protocol: `{load_plan.get('single_next_protocol', 'not recorded')}`
- Why not more context: {load_plan.get('why_not_more_context', 'Load only what the active bead proves is needed.')}

## Context Footprint

- Active memory: `{', '.join(context_footprint.get('active_memory') or [])}`
- Active bead: `{context_footprint.get('active_bead', 'missing')}`
- Primary authority: `{context_footprint.get('primary_authority', 'missing')}`
- Required context: `{', '.join(context_footprint.get('required_context') or [])}`
- Conditional references: `{', '.join(context_footprint.get('conditional_references') or []) or 'none'}`
- Generated reports touched: `{', '.join(context_footprint.get('generated_reports_touched') or [])}`
- Approx document lines: `{context_footprint.get('approx_document_lines', 'unknown')}`
- Budget rule: {context_footprint.get('budget_rule', 'Prepare a checkpoint, compaction, restart, or handoff around 80% context usage.')}

## Goal Frame

- Status: {current_goal.get('status', 'none')}
- Owner file: `{current_goal.get('path', 'not recorded')}`
- Horizon: `{current_goal.get('horizon', 'not recorded')}`
- Workflow guidance: `{current_goal.get('workflow_guidance', 'not recorded')}`
- Goal: {current_goal.get('goal', 'not recorded')}
- Reaffirmation trigger: {current_goal.get('reaffirmation_trigger', 'not recorded')}
- Advisory warning: {next_details.get('goal_frame_advisory', 'Goal Frames are advisory only.')}

{chr(10).join(f"- Warning: {warning}" for warning in (goal_frame.get('warnings') or [])) if goal_frame.get('warnings') else "- No Goal Frame warnings."}

## Blockers

{chr(10).join(f"- {blocker}" for blocker in blockers) if blockers else "- No compiled next-step blockers."}

## Stable-Fix Eligibility

- Status: {stable_fix.get('status', 'missing')}
- Classification: `{stable_fix_details.get('classification', 'unknown')}`
- Eligible: {stable_fix_details.get('eligible', False)}
- Required route: `{stable_fix_details.get('required_route', 'PRD/bead')}`
- Advisory only: {stable_fix_details.get('advisory_only', True)}
- Why this matters: {stable_fix_details.get('why_this_matters', 'Stable-fix eligibility is advisory and does not approve mutation.')}

{chr(10).join(f"- Warning: {warning}" for warning in (stable_fix.get('warnings') or [])) if stable_fix.get('warnings') else "- No stable-fix eligibility warnings."}

## Adaptive Depth

- Status: {depth.get('status', 'missing')}
- Complexity: `{depth_details.get('complexity', 'unspecified')}`
- Required planning depth: `{depth_details.get('required_planning_depth', 'unspecified')}`
- Autonomy level: `{depth_details.get('autonomy_level', 'unspecified')}`
- User decision: `{depth_details.get('user_decision', 'continue')}`
- Shortest next action: {depth_details.get('shortest_next_action', 'Continue inside the active bead and record its declared checks.')}
- Why this matters: {depth_details.get('why_this_matters', 'Adaptive depth keeps planning proportional to risk.')}
- Stop if: {depth_details.get('stop_if', 'Stop if risk and planning depth do not match.')}
- Inferred defaults used: {depth_details.get('inferred_defaults_used', False)}

{chr(10).join(f"- Warning: {warning}" for warning in (depth.get('warnings') or [])) if depth.get('warnings') else "- No adaptive-depth warnings."}
{chr(10).join(f"- Reason: {reason}" for reason in (depth_details.get('decision_reasons') or [])) if depth_details.get('decision_reasons') else "- No adaptive-depth decision reasons."}

## Files In Play Guardrail

- Status: {guardrail.get('status', 'missing')}
- Git status available: {guardrail_details.get('git_status_available', False)}
- Changed paths: {len(guardrail_details.get('changed_paths') or [])}
- Out-of-scope paths: {len(guardrail_details.get('out_of_scope_paths') or [])}
- User decision: `{guardrail_details.get('user_decision', 'continue')}`
- Why this matters: {guardrail_details.get('why_this_matters', 'Files in play keep edits inside the approved bead.')}
- Stop if: {guardrail_details.get('stop_if', 'Stop if changed paths are outside files_in_play.')}

{chr(10).join(f"- Warning: {warning}" for warning in (guardrail.get('warnings') or [])) if guardrail.get('warnings') else "- No files-in-play guardrail warnings."}

## Run Contract

- Status: {run_contract.get('status', 'missing')}
- Present: {run_details.get('present', False)}
- Required: {run_details.get('required', False)}
- User decision: `{run_details.get('user_decision', 'continue')}`
- Why this matters: {run_details.get('why_this_matters', 'Run contracts clarify allowed actions and proof needed when risk rises.')}
- Stop if: {run_details.get('stop_if', 'Stop if allowed actions, proof needed, approval gates, or rollback path are unclear.')}

{chr(10).join(f"- Warning: {warning}" for warning in (run_contract.get('warnings') or [])) if run_contract.get('warnings') else "- No run-contract warnings."}
"""


def markdown_table(rows: list[list[str]]) -> str:
    if not rows:
        return ""
    escaped = [[str(cell).replace("|", "\\|") for cell in row] for row in rows]
    header = "| " + " | ".join(escaped[0]) + " |"
    divider = "| " + " | ".join("---" for _ in escaped[0]) + " |"
    body = ["| " + " | ".join(row) + " |" for row in escaped[1:]]
    return "\n".join([header, divider, *body])


def first_bullets(text: str, limit: int = 4) -> list[str]:
    items = bullet_items(text)
    return items[:limit]


def progress_payload(payload: dict[str, Any]) -> dict[str, Any]:
    todo = payload.get("todo") or {}
    todo_sections = todo.get("sections") or {}
    current_checks = payload.get("active_bead_checks") or []
    missing_checks = sum(1 for row in current_checks if row.get("status") == "missing")
    failing_checks = sum(1 for row in current_checks if row.get("status") == "fail")
    passing_checks = sum(1 for row in current_checks if row.get("status") == "pass")
    readiness = payload.get("readiness") or {}
    promotion = readiness.get("current_promotion") or {}
    next_step = payload.get("next_step") or {}
    next_details = next_step.get("details") or {}
    state = payload.get("state_integrity") or {}

    attention: list[str] = []
    if missing_checks:
        attention.append(f"{missing_checks} declared check(s) have no recorded evidence.")
    if failing_checks:
        attention.append(f"{failing_checks} declared check(s) are currently failing.")
    for blocker in (promotion.get("blockers") or [])[:4]:
        attention.append(str(blocker))
    for warning in (next_step.get("warnings") or []):
        text = str(warning)
        if "adaptive depth" in text:
            message = "Planning and proof depth need review before continuing."
        elif "run contract" in text:
            message = "Run contract details may be needed before this bead is accepted."
        else:
            message = text
        if message not in attention:
            attention.append(message)
        if len(attention) >= 7:
            break

    stale_reports = [
        str(warning).split(":", 1)[1].strip()
        for warning in (state.get("warnings") or [])
        if str(warning).startswith("generated report may be stale relative to latest evidence:")
        and "PROGRESS.md" not in str(warning)
    ]
    if stale_reports:
        attention.append("Some generated reports may be stale; refresh generated reports before reviewing them.")
    for warning in (state.get("warnings") or []):
        text = str(warning)
        if text.startswith("generated report may be stale relative to latest evidence:"):
            continue
        if text not in attention:
            attention.append(text)
        if len(attention) >= 8:
            break

    return {
        "generated_at": payload.get("generated_at"),
        "source": "scripts/progress.py or scripts/os-health.py via scripts/os_compiler.py",
        "current_work": {
            "current_bead": payload.get("current_bead") or "missing",
            "status": payload.get("current_bead_status") or "missing",
            "build_lane": todo.get("build_lane") or "not recorded",
            "active_feature_window": todo.get("active_feature_window") or "not recorded",
            "primary_authority": todo.get("primary_authority") or "not recorded",
            "done_when": first_bullets(str(todo_sections.get("Done When", ""))),
            "next_step": next_details.get("plain_english_summary", next_details.get("recommended_action", "repair active state before continuing")),
            "user_decision": next_details.get("user_decision", "repair state"),
            "stop_if": next_details.get("stop_if", "stop if workflow, scope, evidence, or approval is unclear"),
        },
        "completion": {
            "bead_status_counts": payload.get("bead_status_counts") or {},
            "beads": [
                {
                    "bead_id": bead.get("bead_id") or "",
                    "title": bead.get("title") or bead.get("rel_path") or "untitled",
                    "status": bead.get("status") or "missing",
                    "path": bead.get("rel_path") or "",
                }
                for bead in (payload.get("beads") or [])
            ],
        },
        "proof": {
            "declared_checks": len(current_checks),
            "passing_checks": passing_checks,
            "missing_checks": missing_checks,
            "failing_checks": failing_checks,
            "checks": current_checks,
        },
        "needs_attention": attention,
        "boundaries": [
            "Generated reports are evidence only.",
            "Repair owner files first, then regenerate this report.",
            "Active memory remains AGENT.md, DECISIONS.md, and tasks/todo.md.",
        ],
    }


def render_progress_markdown(payload: dict[str, Any]) -> str:
    progress = progress_payload(payload)
    current = progress["current_work"]
    completion = progress["completion"]
    proof = progress["proof"]
    counts = completion.get("bead_status_counts") or {}
    checks = proof.get("checks") or []

    status_rows = [["Status", "Count"]] + [[f"`{status}`", str(count)] for status, count in sorted(counts.items())]
    bead_rows = [["Bead", "Status", "Path"]] + [
        [
            str(bead.get("title") or bead.get("bead_id") or "untitled"),
            f"`{bead.get('status', 'missing')}`",
            f"`{bead.get('path', '')}`",
        ]
        for bead in completion.get("beads", [])
    ]
    check_rows = [["Command", "Status", "Evidence"]] + [
        [
            f"`{row.get('command', 'missing')}`",
            str(row.get("status", "missing")),
            f"`{row.get('output')}`" if row.get("output") else "missing",
        ]
        for row in checks
    ]
    done_when = current.get("done_when") or []
    attention = progress.get("needs_attention") or []

    return f"""# PrecodeOS -- Generated Progress
<!-- ANCHOR: progress -->

> AUTHORITY: Generated user-facing progress snapshot for the current PrecodeOS workspace.
> NOT_AUTHORITY: Active memory, task selection, product decisions, implementation plans, roadmap authority, review acceptance, bead transition approval, or proof by itself.
> LOAD_WHEN: A user wants a short generated answer to where the work is and what appears complete; never as active session memory.
> CLASS: generated
>
> Generated from `scripts/progress.py` or `scripts/os-health.py`.
> Generated by PrecodeOS, created by Dan Sears / Recode.
> Do not use this file as active memory.
> Working memory lives in `AGENT.md`, `DECISIONS.md`, and `tasks/todo.md`.

Generated at: `{progress.get('generated_at')}`

## Where You Are

- Current bead: `{current.get('current_bead')}`
- State: `{current.get('status')}`
- Build lane: {current.get('build_lane')}
- Active feature window: {current.get('active_feature_window')}
- Primary authority: `{current.get('primary_authority')}`
- What to do now: {current.get('next_step')}
- User decision: `{current.get('user_decision')}`
- Stop if: {current.get('stop_if')}

## Done When

{chr(10).join(f"- {item}" for item in done_when) if done_when else "- No current Done When bullets found."}

## Completion Picture

{markdown_table(status_rows) if len(status_rows) > 1 else "- No bead status counts found."}

{markdown_table(bead_rows) if len(bead_rows) > 1 else "- No beads found."}

## Proof Status

- Declared checks: {proof.get('declared_checks', 0)}
- Passing checks: {proof.get('passing_checks', 0)}
- Missing checks: {proof.get('missing_checks', 0)}
- Failing checks: {proof.get('failing_checks', 0)}

{markdown_table(check_rows) if len(check_rows) > 1 else "- No declared active-bead checks found."}

## Needs Attention

{chr(10).join(f"- {item}" for item in attention) if attention else "- No compiled progress blockers or warnings."}

## Boundaries

- Generated reports are evidence only.
- Repair owner files first, then regenerate this report.
- Active memory remains `AGENT.md`, `DECISIONS.md`, and `tasks/todo.md`.
"""


def render_work_graph_markdown(payload: dict[str, Any]) -> str:
    graph = payload.get("work_graph") or {}
    details = graph.get("details") or {}
    nodes = details.get("nodes") or []
    edges = details.get("edges") or []
    warnings = graph.get("warnings") or []
    node_counts = details.get("node_counts") or {}
    edge_counts = details.get("edge_counts") or {}

    node_rows = [["Type", "Count"]] + [[f"`{key}`", str(value)] for key, value in node_counts.items()]
    edge_rows = [["Relation", "Count"]] + [[f"`{key}`", str(value)] for key, value in edge_counts.items()]
    bead_rows = [["Bead", "Status", "Kind"]] + [
        [
            f"`{item.get('path')}`",
            f"`{item.get('status', 'missing')}`",
            f"`{item.get('kind', 'unknown')}`",
        ]
        for item in nodes
        if item.get("type") == "bead"
    ]
    relationship_rows = [["Source", "Relation", "Target"]] + [
        [
            f"`{item.get('source')}`",
            f"`{item.get('relation')}`",
            f"`{item.get('target')}`",
        ]
        for item in edges[:40]
    ]

    return f"""# PrecodeOS -- Work Graph Report
<!-- ANCHOR: work-graph -->

> AUTHORITY: Generated evidence-only work graph compiled from PrecodeOS markdown contracts and logs.
> NOT_AUTHORITY: Active memory, task selection, product decisions, implementation plans, review acceptance, bead transition approval, or proof by itself.
> LOAD_WHEN: Inspecting bead, PRD, owner-file, check, blocker, follow-up, and transition relationships; never as active session memory.
> CLASS: generated
>
> Generated from `scripts/os_compiler.py`.
> Generated by PrecodeOS, created by Dan Sears / Recode.
> Do not use this file as active memory.
> Working memory lives in `AGENT.md`, `DECISIONS.md`, and `tasks/todo.md`.

Generated at: `{payload.get('generated_at')}`

## Summary

- Status: {graph.get('status', 'missing')}
- Current bead: `{details.get('current_bead', 'missing')}`
- Advisory only: {details.get('advisory_only', True)}
- Nodes: {len(nodes)}
- Edges: {len(edges)}

## Warnings

{chr(10).join(f"- {warning}" for warning in warnings) if warnings else "- No first-pass work graph warnings."}

## Node Counts

{markdown_table(node_rows) if len(node_rows) > 1 else "- No graph nodes found."}

## Edge Counts

{markdown_table(edge_rows) if len(edge_rows) > 1 else "- No graph edges found."}

## Beads

{markdown_table(bead_rows) if len(bead_rows) > 1 else "- No bead nodes found."}

## Relationship Sample

{markdown_table(relationship_rows) if len(relationship_rows) > 1 else "- No graph relationships found."}

## Boundaries

- Generated work graph reports are evidence only.
- Repair owner files first, then regenerate this report.
- The graph does not choose tasks, approve transitions, accept review, replace beads, or override owner files.
"""


def write_compiled_sidecars(root: Path, payload: dict[str, Any]) -> None:
    write_json(root / "logs" / "authority-map.json", payload["authority_map"])
    write_json(root / "logs" / "adapter-index.json", payload["adapter_index"])
    write_json(root / "logs" / "shim-index.json", payload["shim_index"])
    write_json(root / "logs" / "readiness.json", payload["readiness"])
    write_json(root / "logs" / "orchestration-map.json", payload["intent_orchestration"])
    write_json(root / "logs" / "workflow-map.json", payload["workflow_planning"])
    write_json(root / "logs" / "long-horizon-map.json", payload["long_horizon_planning"])
    write_json(root / "logs" / "goal-frame.json", payload["goal_frame"])
    write_json(root / "logs" / "handoff-packet.json", payload["completion_handoff"])
    write_json(root / "logs" / "next-step.json", payload["next_step"])
    write_json(root / "logs" / "run-contract.json", payload["run_contract"])
    write_yaml(root / "logs" / "run-contract.yaml", payload["run_contract"])
    write_json(root / "logs" / "pattern-guidance.json", payload["pattern_guidance"])
    write_json(root / "logs" / "progress.json", progress_payload(payload))
    write_json(root / "logs" / "memory-index.json", payload["memory"])
    (root / "logs" / "memory-index.md").write_text(render_memory_index_markdown(payload["memory"]), encoding="utf-8")
    write_json(root / "logs" / "file-inventory.json", payload["file_inventory"])
    write_json(root / "logs" / "work-graph.json", payload["work_graph"])
    (root / "logs" / "work-graph.md").write_text(render_work_graph_markdown(payload), encoding="utf-8")
    (root / "logs" / "handoff-packet.md").write_text(render_handoff_packet(payload), encoding="utf-8")
    (root / "PROGRESS.md").write_text(render_progress_markdown(payload), encoding="utf-8")
    (root / "PRECODE-HELP.md").write_text(render_precode_help(payload), encoding="utf-8")
    write_events_jsonl(root / "logs" / "os-events.jsonl", payload["events"])
