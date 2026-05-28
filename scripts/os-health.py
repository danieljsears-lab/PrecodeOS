#!/usr/bin/env python3
# Version: v0.1.9
# Last updated: 2026-05-28
# Owner: PrecodeOS
# Created by Dan Sears / Recode.
# SPDX-License-Identifier: Apache-2.0
from __future__ import annotations

from typing import Any

from os_compiler import compile_state, repo_root, write_compiled_sidecars, write_json


HEALTH_JSON = "logs/os-health.json"
HEALTH_MD = "OS-HEALTH.md"


def markdown_table(rows: list[list[str]]) -> str:
    if not rows:
        return ""
    header = "| " + " | ".join(rows[0]) + " |"
    divider = "| " + " | ".join("---" for _ in rows[0]) + " |"
    body = ["| " + " | ".join(row) + " |" for row in rows[1:]]
    return "\n".join([header, divider, *body])


def fmt_usd(value: object) -> str:
    try:
        return f"${float(value):.4f}"
    except (TypeError, ValueError):
        return "unknown"


def fmt_tokens(value: object) -> str:
    try:
        return f"{int(value):,}"
    except (TypeError, ValueError):
        return "unknown"


def render_markdown(payload: dict[str, Any]) -> str:
    metrics = payload["loop_metrics"]
    latest_validate = metrics.get("latest_validate_memory") or {}
    check_rows = payload["active_bead_checks"]
    missing_checks = sum(1 for row in check_rows if row["status"] == "missing")
    failing_checks = sum(1 for row in check_rows if row["status"] == "fail")
    start_blockers = len(payload["readiness"]["current_promotion"]["blockers"])
    health_status = "green" if missing_checks == 0 and failing_checks == 0 and start_blockers == 0 else "needs attention"

    summary = markdown_table(
        [
            ["Signal", "Value"],
            ["Health", health_status],
            ["App directory", f"`{payload['app_dir']}/`"],
            ["Branch", f"`{payload['branch']}`"],
            ["Changed paths", str(payload["changed_path_count"])],
            ["Current bead", f"`{payload.get('current_bead') or 'missing'}`"],
            ["Current bead status", f"`{payload.get('current_bead_status') or 'missing'}`"],
            ["Latest validator evidence", f"{latest_validate.get('status', 'missing')} (exit {latest_validate.get('exit_code', 'n/a')})"],
        ]
    )

    bead_counts = markdown_table(
        [["Status", "Count"]]
        + [[f"`{status}`", str(count)] for status, count in payload["bead_status_counts"].items()]
    )

    checks = markdown_table(
        [["Command", "cwd", "Status", "Exit", "Evidence"]]
        + [
            [
                f"`{row['command']}`",
                f"`{row['cwd']}`",
                str(row["status"]),
                str(row["exit_code"] if row["exit_code"] is not None else "n/a"),
                f"`{row['output']}`" if row.get("output") else "missing",
            ]
            for row in check_rows
        ]
    )

    loop_metrics = markdown_table(
        [
            ["Metric", "Value"],
            ["Recorded checks", str(metrics["recorded_checks"])],
            ["Passing checks", str(metrics["passing_checks"])],
            ["Failing checks", str(metrics["failing_checks"])],
            ["Tool runs", str(metrics.get("tool_runs", 0))],
            ["Session starts", str(metrics["session_start"])],
            ["Checkpoints", str(metrics["checkpoint"])],
            ["Session closes", str(metrics["session_close"])],
            ["Handoffs", str(metrics["handoffs"])],
            ["Bead transitions", str(metrics["transitions"])],
            ["Event rows", str(metrics["events"])],
            ["Spend entries", str(metrics["spend"]["entries"])],
            ["Known spend", f"${metrics['spend']['known_cost_usd']:.4f}"],
            ["Known tokens", fmt_tokens(metrics["spend"].get("total_tokens"))],
            ["Unknown token entries", str(metrics["spend"].get("unknown_token_entries", 0))],
            ["Unknown cost entries", str(metrics["spend"].get("unknown_cost_entries", 0))],
        ]
    )

    spend = metrics["spend"]
    by_tool = spend.get("by_tool") or {}
    spend_by_agent = (
        markdown_table(
            [["Agent", "Entries", "Known tokens", "Known spend", "Unknown tokens", "Unknown cost"]]
            + [
                [
                    f"`{tool}`",
                    str(values.get("entries", 0)),
                    fmt_tokens(values.get("total_tokens", 0)),
                    fmt_usd(values.get("known_cost_usd", 0)),
                    str(values.get("unknown_token_entries", 0)),
                    str(values.get("unknown_cost_entries", 0)),
                ]
                for tool, values in by_tool.items()
            ]
        )
        if by_tool
        else ""
    )

    by_task = spend.get("by_task") or {}
    spend_by_task = (
        markdown_table(
            [["Task", "Entries", "Known tokens", "Known spend", "Unknown tokens", "Unknown cost"]]
            + [
            [
                f"`{task}`",
                str(values.get("entries", 0)),
                fmt_tokens(values.get("total_tokens", 0)),
                fmt_usd(values.get("known_cost_usd", 0)),
                str(values.get("unknown_token_entries", 0)),
                str(values.get("unknown_cost_entries", 0)),
            ]
            for task, values in by_task.items()
            ]
        )
        if by_task
        else ""
    )

    current_promotion = payload["readiness"]["current_promotion"]
    readiness_lines = [
        f"- Promote current bead: {'eligible' if current_promotion['eligible'] else 'blocked'}",
    ]
    for blocker in current_promotion["blockers"][:6]:
        readiness_lines.append(f"- Blocker: {blocker}")

    indexes = [
        "- `logs/authority-map.json`",
        "- `logs/adapter-index.json`",
        "- `logs/shim-index.json`",
        "- `logs/readiness.json`",
        "- `logs/orchestration-map.json`",
        "- `logs/workflow-map.json`",
        "- `logs/long-horizon-map.json`",
        "- `logs/goal-frame.json`",
        "- `logs/next-step.json`",
        "- `logs/progress.json`",
        "- `logs/handoff-packet.json`",
        "- `logs/handoff-packet.md`",
        "- `logs/memory-index.json`",
        "- `logs/memory-index.md`",
        "- `logs/file-inventory.json`",
        "- `logs/local-hygiene-preview.json`",
        "- `logs/local-hygiene-preview.md`",
        "- `logs/os-events.jsonl`",
        "- `PROGRESS.md`",
        "- `PRECODE-HELP.md`",
    ]

    learning = payload["learning"]
    blocked = payload["blocked_escape"]
    verification = payload.get("verification_quality") or {"status": "missing", "warnings": []}
    verification_warnings = verification.get("warnings") or []
    verification_details = verification.get("details") or {}
    decomposition = payload.get("decomposition_quality") or {"status": "missing", "warnings": []}
    decomposition_warnings = decomposition.get("warnings") or []
    decomposition_details = decomposition.get("details") or {}
    state_integrity = payload.get("state_integrity") or {"status": "missing", "warnings": []}
    state_warnings = state_integrity.get("warnings") or []
    state_details = state_integrity.get("details") or {}
    intent = payload.get("intent_orchestration") or {"status": "missing", "warnings": []}
    intent_warnings = intent.get("warnings") or []
    intent_details = intent.get("details") or {}
    tool_execution = payload.get("tool_execution") or {"status": "missing", "warnings": []}
    tool_warnings = tool_execution.get("warnings") or []
    tool_details = tool_execution.get("details") or {}
    latest_failure = tool_details.get("latest_failure") or {}
    workflow = payload.get("workflow_planning") or {"status": "missing", "warnings": []}
    workflow_warnings = workflow.get("warnings") or []
    workflow_details = workflow.get("details") or {}
    long_horizon = payload.get("long_horizon_planning") or {"status": "missing", "warnings": []}
    long_horizon_warnings = long_horizon.get("warnings") or []
    long_horizon_details = long_horizon.get("details") or {}
    goal_frame = payload.get("goal_frame") or {"status": "missing", "warnings": [], "details": {}}
    goal_frame_warnings = goal_frame.get("warnings") or []
    goal_frame_details = goal_frame.get("details") or {}
    current_goal_frame = goal_frame_details.get("current") or {}
    completion = payload.get("completion_handoff") or {"status": "missing", "warnings": []}
    completion_warnings = completion.get("warnings") or []
    completion_details = completion.get("details") or {}
    next_step = payload.get("next_step") or {"status": "missing", "warnings": []}
    next_step_warnings = next_step.get("warnings") or []
    next_step_details = next_step.get("details") or {}
    bead_depth = payload.get("bead_depth") or {"status": "missing", "warnings": []}
    bead_depth_warnings = bead_depth.get("warnings") or []
    bead_depth_details = bead_depth.get("details") or {}
    guardrail = payload.get("files_in_play_guardrail") or {"status": "missing", "warnings": []}
    guardrail_warnings = guardrail.get("warnings") or []
    guardrail_details = guardrail.get("details") or {}
    pattern = payload.get("pattern_guidance") or {"status": "missing", "warnings": []}
    pattern_warnings = pattern.get("warnings") or []
    pattern_details = pattern.get("details") or {}
    memory = payload.get("memory") or {"status": "missing", "warnings": [], "details": {}}
    memory_warnings = memory.get("warnings") or []
    memory_details = memory.get("details") or {}
    file_inventory = payload.get("file_inventory") or {"status": "missing", "warnings": [], "counts": {}}
    file_inventory_warnings = file_inventory.get("warnings") or []
    file_inventory_counts = file_inventory.get("counts") or {}
    local_hygiene = payload.get("local_hygiene") or {"status": "missing", "warnings": [], "details": {}}
    local_hygiene_warnings = local_hygiene.get("warnings") or []
    local_hygiene_details = local_hygiene.get("details") or {}

    return f"""# PrecodeOS -- OS Health Report
<!-- ANCHOR: os-health -->

> AUTHORITY: Generated OS health snapshot, loop metrics, bead status, and recent check evidence for the PrecodeOS workspace.
> NOT_AUTHORITY: Active memory, product decisions, feature requirements, implementation plans, or task selection.
> LOAD_WHEN: Auditing PrecodeOS health, loop friction, check evidence, or blocked-bead status; never as active session memory.
> CLASS: generated
>
> Generated from `scripts/os-health.py`.
> Generated by PrecodeOS, created by Dan Sears / Recode.
> Do not use this file as active memory.
> Working memory lives in `AGENT.md`, `DECISIONS.md`, and `tasks/todo.md`.

Generated at: `{payload['generated_at']}`

## Summary

{summary}

## Bead Status

{bead_counts or "- No bead files found."}

## Active Bead Check Evidence

{checks or "- No active bead checks are declared."}

## Verification Quality

- Status: {verification.get('status', 'missing')}
- Known tiers: {', '.join(verification_details.get('known_tiers') or []) or 'none recorded'}
- Code-changing bead: {verification_details.get('code_changing', 'unknown')}

{chr(10).join(f"- Warning: {warning}" for warning in verification_warnings) if verification_warnings else "- No first-pass verification quality warnings."}

## Decomposition Quality

- Status: {decomposition.get('status', 'missing')}
- Bead kind: {decomposition_details.get('bead_kind', 'unknown')}
- Files in play: {decomposition_details.get('files_in_play_count', 'unknown')}
- Checks: {decomposition_details.get('checks_count', 'unknown')}

{chr(10).join(f"- Warning: {warning}" for warning in decomposition_warnings) if decomposition_warnings else "- No first-pass decomposition warnings."}

## State Integrity

- Status: {state_integrity.get('status', 'missing')}
- In-progress beads: {', '.join(state_details.get('in_progress_beads') or []) or 'none'}
- Latest event timestamp: {state_details.get('latest_event_timestamp') or 'none'}

{chr(10).join(f"- Warning: {warning}" for warning in state_warnings) if state_warnings else "- No first-pass state integrity warnings."}

## Intent Orchestration

- Status: {intent.get('status', 'missing')}
- Lifecycle state: {intent_details.get('lifecycle_state', 'unknown')}
- Current PRD: {intent_details.get('current_parent_prd') or 'not recorded'}
- Requirement IDs: {', '.join(intent_details.get('current_requirement_ids') or []) or 'none'}
- Recorded evidence rows: {intent_details.get('current_recorded_check_count', 0)}
- Pending approval: {intent_details.get('pending_approval', 'unknown')}

{chr(10).join(f"- Warning: {warning}" for warning in intent_warnings) if intent_warnings else "- No first-pass intent orchestration warnings."}

## Workflow Planning

- Status: {workflow.get('status', 'missing')}
- Current situation: {workflow_details.get('current_situation', 'unknown')}
- Recommended workflow: {workflow_details.get('recommended_workflow', 'unknown')}
- Next artifact: {workflow_details.get('artifact_to_produce_next', 'unknown')}
- Required authority: {workflow_details.get('required_authority_source', 'unknown')}
- User approval needed: {workflow_details.get('user_approval_needed', 'unknown')}

{chr(10).join(f"- Warning: {warning}" for warning in workflow_warnings) if workflow_warnings else "- No first-pass workflow planning warnings."}

## Long-Horizon Planning

- Status: {long_horizon.get('status', 'missing')}
- Approved PRDs: {len(long_horizon_details.get('approved_prds') or [])}
- Ready beads: {len(long_horizon_details.get('ready_beads') or [])}
- Blocked beads: {len(long_horizon_details.get('blocked_beads') or [])}
- Follow-up candidates: {len(long_horizon_details.get('follow_up_candidates') or [])}
- Dependency gaps: {len(long_horizon_details.get('dependency_gaps') or [])}

{chr(10).join(f"- Warning: {warning}" for warning in long_horizon_warnings) if long_horizon_warnings else "- No first-pass long-horizon planning warnings."}

## Goal Frame

- Status: {goal_frame.get('status', 'missing')}
- Current frame status: {current_goal_frame.get('status', 'none')}
- Owner file: `{current_goal_frame.get('path', 'not recorded')}`
- Horizon: {current_goal_frame.get('horizon', 'not recorded')}
- Workflow guidance: {current_goal_frame.get('workflow_guidance', 'not recorded')}
- Goal: {current_goal_frame.get('goal', 'not recorded')}
- Reaffirmation trigger: {current_goal_frame.get('reaffirmation_trigger', 'not recorded')}
- Advisory only: {goal_frame_details.get('advisory_only', True)}

{chr(10).join(f"- Warning: {warning}" for warning in goal_frame_warnings) if goal_frame_warnings else "- No first-pass Goal Frame warnings."}

## Completion And Handoff

- Status: {completion.get('status', 'missing')}
- Closeout status: {completion_details.get('closeout_status', 'unknown')}
- Promotion status: {completion_details.get('promotion_status', 'unknown')}
- Manual verification: {completion_details.get('manual_verification', 'unknown')}
- Review decision: {completion_details.get('review_decision', 'unknown')}
- Next safe action: {completion_details.get('next_safe_action', 'unknown')}

{chr(10).join(f"- Warning: {warning}" for warning in completion_warnings) if completion_warnings else "- No first-pass completion or handoff warnings."}

## Next Step

- Status: {next_step.get('status', 'missing')}
- What to do now: {next_step_details.get('plain_english_summary', next_step_details.get('recommended_action', 'unknown'))}
- User decision: {next_step_details.get('user_decision', 'unknown')}
- Recommended action: {next_step_details.get('recommended_action', 'unknown')}
- Action category: {next_step_details.get('action_category', 'unknown')}
- Stop if: {next_step_details.get('stop_if', 'unknown')}
- Needs review: {next_step_details.get('needs_review', 'unknown')}
- Needs transition approval: {next_step_details.get('needs_transition', 'unknown')}
- Blockers: {len(next_step_details.get('blockers') or [])}

{chr(10).join(f"- Warning: {warning}" for warning in next_step_warnings) if next_step_warnings else "- No first-pass next-step warnings."}

## Adaptive Depth

- Status: {bead_depth.get('status', 'missing')}
- Complexity: {bead_depth_details.get('complexity', 'unspecified')}
- Required planning depth: {bead_depth_details.get('required_planning_depth', 'unspecified')}
- Autonomy level: {bead_depth_details.get('autonomy_level', 'unspecified')}
- User decision: {bead_depth_details.get('user_decision', 'unknown')}
- Stop if: {bead_depth_details.get('stop_if', 'unknown')}
- Advisory only: {bead_depth_details.get('advisory_only', True)}

{chr(10).join(f"- Warning: {warning}" for warning in bead_depth_warnings) if bead_depth_warnings else "- No first-pass adaptive-depth warnings."}

## Files In Play Guardrail

- Status: {guardrail.get('status', 'missing')}
- Git status available: {guardrail_details.get('git_status_available', 'unknown')}
- Changed paths: {len(guardrail_details.get('changed_paths') or [])}
- Out-of-scope paths: {len(guardrail_details.get('out_of_scope_paths') or [])}
- User decision: {guardrail_details.get('user_decision', 'unknown')}
- Stop if: {guardrail_details.get('stop_if', 'unknown')}
- Advisory only: {guardrail_details.get('advisory_only', True)}

{chr(10).join(f"- Warning: {warning}" for warning in guardrail_warnings) if guardrail_warnings else "- No first-pass files-in-play guardrail warnings."}

## System Design Pattern Guidance

- Status: {pattern.get('status', 'missing')}
- Likely shape: {pattern_details.get('likely_project_shape', 'unknown')}
- Recommended pattern: {pattern_details.get('recommended_pattern', 'unknown')}
- Owner hints: {', '.join(pattern_details.get('owner_file_hints') or []) or 'none'}
- Warning count: {pattern_details.get('warning_count', 0)}
- Review prompt: {pattern_details.get('next_human_review_prompt', 'unknown')}

{chr(10).join(f"- Warning: {warning}" for warning in pattern_warnings) if pattern_warnings else "- No first-pass system design pattern warnings."}

## Filesystem Memory

- Status: {memory.get('status', 'missing')}
- Reviewed memory cards: {memory_details.get('card_count', 0)}
- Categories: {', '.join(f"{key}={value}" for key, value in (memory_details.get('by_category') or {}).items()) or 'none'}
- Promotion-needed cards: {len(memory_details.get('promotion_needed') or [])}
- Stale or superseded cards: {len(memory_details.get('stale_or_superseded') or [])}
- Review prompt: {memory_details.get('next_human_review_prompt', 'unknown')}

{chr(10).join(f"- Warning: {warning}" for warning in memory_warnings) if memory_warnings else "- No first-pass filesystem memory warnings."}

## File Inventory

- Status: {file_inventory.get('status', 'missing')}
- Package inventory: `{file_inventory.get('package_inventory', file_inventory.get('canonical_inventory', 'missing'))}`
- Maintainer inventory: `{file_inventory.get('maintainer_inventory', 'missing')}`
- Documented docs: {file_inventory_counts.get('docs', 0)}
- Scripts: {file_inventory_counts.get('scripts', 0)}
- Maintainer docs: {file_inventory_counts.get('maintainer_docs', 0)}
- Docs HTML files: {file_inventory_counts.get('docs_html', 0)}
- Workflows: {file_inventory_counts.get('workflows', 0)}
- Generated outputs tracked: {file_inventory_counts.get('generated_outputs', 0)}

{chr(10).join(f"- Warning: {warning}" for warning in file_inventory_warnings[:8]) if file_inventory_warnings else "- No first-pass file inventory warnings."}

## Local Hygiene

- Status: {local_hygiene.get('status', 'missing')}
- Advisory only: {local_hygiene_details.get('advisory_only', True)}
- Bulky log candidates: {local_hygiene_details.get('bulky_log_candidate_count', 0)}
- Bulky log candidate bytes: {local_hygiene_details.get('bulky_log_candidate_bytes', 0)}
- Cache/build candidates: {local_hygiene_details.get('cache_candidate_count', 0)}
- Cache/build candidate bytes: {local_hygiene_details.get('cache_candidate_bytes', 0)}
- Unexpected logs files: {len(local_hygiene_details.get('unexpected_logs') or [])}
- Missing referenced outputs: {len(local_hygiene_details.get('missing_referenced_outputs') or [])}
- Protected evidence outputs: {len(local_hygiene_details.get('protected_evidence_outputs') or [])}
- Next safe action: {local_hygiene_details.get('next_safe_action', 'review candidates only')}

{chr(10).join(f"- Warning: {warning}" for warning in local_hygiene_warnings) if local_hygiene_warnings else "- No first-pass local hygiene warnings."}

## Tool Execution

- Status: {tool_execution.get('status', 'missing')}
- Tool-run entries: {tool_details.get('entries', 0)}
- Active bead entries: {tool_details.get('active_bead_entries', 0)}
- Approval gaps: {tool_details.get('approval_gap_count', 0)}
- Destructive entries: {tool_details.get('destructive_count', 0)}
- Latest failure category: {latest_failure.get('failure_category') or 'none'}

{chr(10).join(f"- Warning: {warning}" for warning in tool_warnings) if tool_warnings else "- No first-pass tool execution warnings."}

## Compiled Readiness

{chr(10).join(readiness_lines)}

## Loop Metrics

{loop_metrics}

## Spend Rollup

- Latest spend entry: {spend.get('latest_timestamp') or 'none'}
- Known total tokens: {fmt_tokens(spend.get('total_tokens'))}
- Known total spend: {fmt_usd(spend.get('known_cost_usd'))}
- Unknown token entries: {spend.get('unknown_token_entries', 0)}
- Unknown cost entries: {spend.get('unknown_cost_entries', 0)}

### By Agent

{spend_by_agent or "- No spend entries recorded."}

### By Task

{spend_by_task or "- No spend entries recorded."}

## Generated Sidecars

{chr(10).join(indexes)}

## Learning Promotion Queue

- Drift observed: {learning['drift_observed']}
- Lesson to promote: {learning['lesson_to_promote']}
- Follow-up bead needed: {learning['follow_up_bead_needed']}

## Blocked-Bead Escape Snapshot

- Manual verification: {blocked['manual_verification']}
- Next bead: {blocked['next_bead']}
- Blocked escape: {blocked['blocked_escape']}
"""


def main() -> int:
    root = repo_root()
    payload = compile_state(root)
    write_compiled_sidecars(root, payload)
    write_json(root / HEALTH_JSON, payload)
    (root / HEALTH_MD).write_text(render_markdown(payload), encoding="utf-8")
    print(f"os-health: wrote {HEALTH_MD} and {HEALTH_JSON}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
