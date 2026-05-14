#!/usr/bin/env python3
# Version: v0.1.1
# Last updated: 2026-04-27
# Owner: PrecodeOS
# Created by Dan Sears / Recode.
# SPDX-License-Identifier: Apache-2.0
from __future__ import annotations

from datetime import datetime, timezone
import argparse
import json
from pathlib import Path
from typing import Any

from os_compiler import load_jsonl, read_bead, read_todo_state, repo_root


DIARY_JSONL = "logs/learning-diary.jsonl"
DIARY_MD = "logs/learning-diary.md"
EMPTY_MARKERS = {"", "none", "none recorded", "not recorded", "not evaluated", "missing"}


def int_value(value: Any) -> int | None:
    if value is None or value == "":
        return None
    try:
        return int(value)
    except (TypeError, ValueError):
        return None


def float_value(value: Any) -> float | None:
    if value is None or value == "":
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def fmt_tokens(value: Any) -> str:
    amount = int_value(value)
    return f"{amount:,}" if amount is not None else "unknown"


def fmt_usd(value: Any) -> str:
    amount = float_value(value)
    return f"${amount:.4f}" if amount is not None else "unknown"


def latest(items: list[dict[str, Any]], key: str | None = None, value: str | None = None) -> dict[str, Any] | None:
    filtered = items
    if key is not None:
        filtered = [item for item in items if item.get(key) == value]
    return filtered[-1] if filtered else None


def compact_check_summary(checks: list[dict[str, Any]], bead: str) -> tuple[str, str]:
    bead_checks = [row for row in checks if row.get("bead") == bead]
    if not bead_checks:
        return "No recorded checks for this bead yet.", "missing"

    latest_check = bead_checks[-1]
    command = latest_check.get("command") or "unknown command"
    status = latest_check.get("status") or "unknown"
    exit_code = latest_check.get("exit_code")
    return f"{len(bead_checks)} recorded check(s); latest `{command}` -> {status} (exit {exit_code}).", str(status)


def spend_rollup(rows: list[dict[str, Any]], task: str | None = None) -> dict[str, Any]:
    filtered = [row for row in rows if task is None or row.get("task") == task]
    total_tokens = 0
    known_token_entries = 0
    known_cost = 0.0
    known_cost_entries = 0
    unknown_token_entries = 0
    unknown_cost_entries = 0
    by_tool: dict[str, dict[str, Any]] = {}

    for row in filtered:
        tool = str(row.get("tool") or "unknown")
        tool_row = by_tool.setdefault(
            tool,
            {
                "entries": 0,
                "total_tokens": 0,
                "known_token_entries": 0,
                "known_cost_usd": 0.0,
                "known_cost_entries": 0,
                "unknown_token_entries": 0,
                "unknown_cost_entries": 0,
            },
        )
        tool_row["entries"] += 1

        tokens = int_value(row.get("total_tokens", row.get("tokens")))
        if tokens is None:
            unknown_token_entries += 1
            tool_row["unknown_token_entries"] += 1
        else:
            total_tokens += tokens
            known_token_entries += 1
            tool_row["total_tokens"] += tokens
            tool_row["known_token_entries"] += 1

        cost = float_value(row.get("cost_usd"))
        if cost is None:
            unknown_cost_entries += 1
            tool_row["unknown_cost_entries"] += 1
        else:
            known_cost += cost
            known_cost_entries += 1
            tool_row["known_cost_usd"] = round(float(tool_row["known_cost_usd"]) + cost, 4)
            tool_row["known_cost_entries"] += 1

    return {
        "entries": len(filtered),
        "total_tokens": total_tokens,
        "known_token_entries": known_token_entries,
        "known_cost_usd": round(known_cost, 4),
        "known_cost_entries": known_cost_entries,
        "unknown_token_entries": unknown_token_entries,
        "unknown_cost_entries": unknown_cost_entries,
        "by_tool": dict(sorted(by_tool.items())),
    }


def spend_summary_text(rollup: dict[str, Any]) -> str:
    if not rollup.get("entries"):
        return "No spend entries recorded."
    warning = ""
    if rollup.get("unknown_token_entries") or rollup.get("unknown_cost_entries"):
        warning = f" Unknown telemetry: {rollup.get('unknown_token_entries', 0)} token entr{'y' if rollup.get('unknown_token_entries') == 1 else 'ies'}, {rollup.get('unknown_cost_entries', 0)} cost entr{'y' if rollup.get('unknown_cost_entries') == 1 else 'ies'}."
    return f"{rollup.get('entries')} entr{'y' if rollup.get('entries') == 1 else 'ies'}; known tokens {fmt_tokens(rollup.get('total_tokens'))}; known cost {fmt_usd(rollup.get('known_cost_usd'))}.{warning}"


def learner_takeaway(closeout: dict[str, str], check_status: str) -> str:
    lesson = closeout.get("lesson_to_promote", "").strip()
    if lesson.lower() not in EMPTY_MARKERS:
        return f"Potential lesson to promote: {lesson}"

    drift = closeout.get("drift_observed", "").strip()
    if drift.lower() not in EMPTY_MARKERS:
        return f"Watch for drift pattern: {drift}"

    if check_status == "pass":
        return "The session produced passing recorded evidence for the active bead."
    if check_status == "fail":
        return "The latest recorded check failed; read the check output before accepting the bead."
    return "The main learning is still evidence hygiene: record checks before treating work as done."


def next_question(closeout: dict[str, str], bead_status: str) -> str:
    follow_up = closeout.get("follow_up_bead_needed", "").strip()
    if follow_up.lower() not in EMPTY_MARKERS:
        return f"Does this follow-up need a separate bead? {follow_up}"

    manual = closeout.get("manual_verification", "").strip()
    if manual.lower() in {"not recorded", "missing", ""}:
        return "What manual verification, if any, is still needed?"

    if bead_status in {"needs_info", "manual_testing"}:
        return "What exact user input or manual test would unblock this bead?"

    return "Is the bead ready to accept, revise, split, or leave blocked?"


def rendered_takeaway(entry: dict[str, Any]) -> str:
    lesson = str(entry.get("lesson_to_promote") or "").strip()
    if lesson.lower() not in EMPTY_MARKERS:
        return f"Potential lesson to promote: {lesson}"

    drift = str(entry.get("drift_observed") or "").strip()
    if drift.lower() not in EMPTY_MARKERS:
        return f"Watch for drift pattern: {drift}"

    check_status = str(entry.get("check_status") or "")
    if check_status == "pass":
        return "The session produced passing recorded evidence for the active bead."
    if check_status == "fail":
        return "The latest recorded check failed; read the check output before accepting the bead."
    return "The main learning is still evidence hygiene: record checks before treating work as done."


def memory_candidate_lines(entries: list[dict[str, Any]]) -> list[str]:
    lines: list[str] = []
    seen: set[str] = set()
    for entry in reversed(entries[-12:]):
        bead = entry.get("bead") or "unknown bead"
        for field, label in (
            ("lesson_to_promote", "Lesson"),
            ("drift_observed", "Drift pattern"),
            ("next_question", "Open theme"),
        ):
            value = str(entry.get(field) or "").strip()
            if value.lower() in EMPTY_MARKERS:
                continue
            key = f"{label}:{value}"
            if key in seen:
                continue
            seen.add(key)
            lines.append(f"- {label}: {value} (source: `{bead}`; requires reviewed memory-card approval)")
    return lines[:8]


def build_entry(root: Path) -> dict[str, Any] | None:
    todo = read_todo_state(root)
    current_bead = todo.get("current_bead") or ""
    if not current_bead:
        return None

    bead_path = root / current_bead
    if not bead_path.is_file():
        return None

    bead = read_bead(bead_path, root)
    checks = load_jsonl(root / "logs" / "check-results.jsonl")
    loop_runs = load_jsonl(root / "logs" / "loop-runs.jsonl")
    spend_rows = load_jsonl(root / "logs" / "agent-spend.jsonl")
    check_summary, check_status = compact_check_summary(checks, bead.rel_path)
    last_checkpoint = latest(loop_runs, "event", "checkpoint")
    bead_spend = spend_rollup(spend_rows, bead.rel_path)
    cumulative_spend = spend_rollup(spend_rows)

    return {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "bead": bead.rel_path,
        "bead_title": bead.title,
        "bead_status": bead.status,
        "primary_authority": bead.primary_authority,
        "check_summary": check_summary,
        "check_status": check_status,
        "spend_for_bead": bead_spend,
        "spend_summary": spend_summary_text(bead_spend),
        "cumulative_spend": cumulative_spend,
        "cumulative_spend_summary": spend_summary_text(cumulative_spend),
        "manual_verification": bead.closeout.get("manual_verification", "not recorded"),
        "review_decision": bead.closeout.get("review_decision", "not reviewed"),
        "drift_observed": bead.closeout.get("drift_observed", "none recorded"),
        "lesson_to_promote": bead.closeout.get("lesson_to_promote", "none"),
        "follow_up_bead_needed": bead.closeout.get("follow_up_bead_needed", "not evaluated"),
        "latest_checkpoint": (last_checkpoint or {}).get("timestamp"),
        "learner_takeaway": learner_takeaway(bead.closeout, check_status),
        "next_question": next_question(bead.closeout, bead.status),
    }


def append_jsonl(path: Path, entry: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(entry, separators=(",", ":")) + "\n")


def render_markdown(entries: list[dict[str, Any]]) -> str:
    recent = entries[-12:]
    if not recent:
        body = "- No learning diary entries recorded yet."
    else:
        blocks: list[str] = []
        for entry in reversed(recent):
            blocks.append(
                "\n".join(
                    [
                        f"### {entry.get('timestamp', 'unknown time')}",
                        "",
                        f"- Bead: `{entry.get('bead') or 'missing'}`",
                        f"- Status: `{entry.get('bead_status') or 'missing'}`",
                        f"- Primary authority: `{entry.get('primary_authority') or 'missing'}`",
                        f"- Checks: {entry.get('check_summary') or 'missing'}",
                        f"- Spend for bead: {entry.get('spend_summary') or 'No spend entries recorded.'}",
                        f"- Cumulative spend: {entry.get('cumulative_spend_summary') or 'No spend entries recorded.'}",
                        f"- Spend by agent: {render_spend_by_agent(entry.get('cumulative_spend'))}",
                        f"- Manual verification: {entry.get('manual_verification') or 'not recorded'}",
                        f"- Review decision: {entry.get('review_decision') or 'not reviewed'}",
                        f"- Drift observed: {entry.get('drift_observed') or 'none recorded'}",
                        f"- Lesson to promote: {entry.get('lesson_to_promote') or 'none'}",
                        f"- Learner takeaway: {rendered_takeaway(entry)}",
                        f"- Question for next time: {entry.get('next_question') or 'missing'}",
                    ]
                )
            )
        body = "\n\n".join(blocks)

    memory_candidates = memory_candidate_lines(entries)

    return f"""# PrecodeOS -- Learning Diary
<!-- ANCHOR: learning-diary -->

> AUTHORITY: Generated learner-facing digest of recent Precode sessions and task evidence.
> NOT_AUTHORITY: Active memory, task selection, product decisions, feature requirements, implementation plans, route structure, schema definitions, or generated progress state.
> LOAD_WHEN: Reviewing what a user can learn from recent sessions; never as active session memory.
> CLASS: generated
>
> Generated from `scripts/update-learning-diary.py`.
> Do not use this file as active memory or as a task plan.

Generated at: `{datetime.now(timezone.utc).isoformat()}`

## Reading Rule

Use this diary to understand what happened and what to learn from it. To continue work, load `AGENT.md`, `DECISIONS.md`, `tasks/todo.md`, the active bead, and the bead's primary authority file.

## Recent Sessions

{body}

## Memory Candidates

These are review prompts only. Do not create memory cards automatically from generated diary output.

{chr(10).join(memory_candidates) if memory_candidates else "- No memory candidates found in recent diary evidence."}
"""


def render_spend_by_agent(rollup: Any) -> str:
    if not isinstance(rollup, dict):
        return "No spend entries recorded."
    by_tool = rollup.get("by_tool")
    if not isinstance(by_tool, dict) or not by_tool:
        return "No spend entries recorded."
    parts = []
    for tool, values in by_tool.items():
        if not isinstance(values, dict):
            continue
        parts.append(f"`{tool}` {fmt_tokens(values.get('total_tokens'))} tokens / {fmt_usd(values.get('known_cost_usd'))}")
    return "; ".join(parts) if parts else "No spend entries recorded."


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--append", action="store_true", help="append a new session entry before rendering markdown")
    args = parser.parse_args()

    root = repo_root()
    jsonl_path = root / DIARY_JSONL

    if args.append:
        entry = build_entry(root)
        if entry is None:
            print("learning-diary: no active bead found; skipped append")
        else:
            append_jsonl(jsonl_path, entry)
            print(f"learning-diary: appended {DIARY_JSONL}")

    entries = load_jsonl(jsonl_path)
    md_path = root / DIARY_MD
    md_path.parent.mkdir(parents=True, exist_ok=True)
    md_path.write_text(render_markdown(entries), encoding="utf-8")
    print(f"learning-diary: wrote {DIARY_MD}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
