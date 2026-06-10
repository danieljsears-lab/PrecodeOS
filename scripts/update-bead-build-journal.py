#!/usr/bin/env python3
# Version: v0.1.0
# Last updated: 2026-06-09
# Owner: PrecodeOS
# Created by Dan Sears / Recode.
# SPDX-License-Identifier: Apache-2.0
from __future__ import annotations

import argparse
from collections import defaultdict
from datetime import datetime, timezone
import json
import subprocess
from pathlib import Path
from typing import Any

from os_compiler import load_jsonl, read_bead, read_todo_state, repo_root


JOURNAL_JSONL = "logs/bead-build-journal.jsonl"
JOURNAL_MD = "logs/bead-build-journal.md"
EMPTY_MARKERS = {"", "none", "none recorded", "not recorded", "not evaluated", "missing"}
GENERATED_PATH_PREFIXES = ("logs/", "docs-html/")
GENERATED_PATHS = {"OS-HEALTH.md", "PRECODE-HELP.md", "PROGRESS.md"}


def git(root: Path, args: list[str]) -> subprocess.CompletedProcess[str] | None:
    try:
        return subprocess.run(["git", *args], cwd=root, check=False, capture_output=True, text=True)
    except OSError:
        return None


def git_text(root: Path, args: list[str]) -> str | None:
    result = git(root, args)
    if result is None or result.returncode != 0:
        return None
    return result.stdout.strip()


def current_branch(root: Path) -> str:
    return git_text(root, ["rev-parse", "--abbrev-ref", "HEAD"]) or "unknown"


def current_head(root: Path) -> str | None:
    return git_text(root, ["rev-parse", "HEAD"])


def parse_status_paths(output: str) -> list[dict[str, str]]:
    paths: list[dict[str, str]] = []
    for line in output.splitlines():
        if not line.strip():
            continue
        status = line[:2].strip() or "unknown"
        raw_path = line[3:].strip() if len(line) > 3 else line.strip()
        if " -> " in raw_path:
            raw_path = raw_path.split(" -> ", 1)[1]
        paths.append({"status": status, "path": raw_path})
    return paths


def working_tree_changes(root: Path) -> list[dict[str, str]]:
    result = git(root, ["status", "--short"])
    if result is None or result.returncode != 0:
        return []
    return parse_status_paths(result.stdout.rstrip("\n"))


def committed_changes(root: Path, start: str | None, end: str | None) -> tuple[list[dict[str, str]], str | None]:
    if not start or not end:
        return [], "missing start or end commit"
    if start == end:
        return [], None
    result = git(root, ["diff", "--name-status", f"{start}..{end}"])
    if result is None:
        return [], "git unavailable"
    if result.returncode != 0:
        return [], "git diff failed"

    changes: list[dict[str, str]] = []
    for line in result.stdout.splitlines():
        parts = line.split("\t")
        if not parts:
            continue
        status = parts[0]
        path = parts[-1]
        changes.append({"status": status, "path": path})
    return changes, None


def is_generated_path(path: str) -> bool:
    return path in GENERATED_PATHS or path.startswith(GENERATED_PATH_PREFIXES)


def split_change_paths(paths: list[dict[str, str]]) -> tuple[list[dict[str, str]], list[dict[str, str]]]:
    implementation: list[dict[str, str]] = []
    generated: list[dict[str, str]] = []
    for item in paths:
        path = item.get("path") or ""
        if is_generated_path(path):
            generated.append(item)
        else:
            implementation.append(item)
    return implementation, generated


def format_change(item: dict[str, str]) -> str:
    status = item.get("status") or "changed"
    path = item.get("path") or "unknown"
    return f"`{path}` ({status})"


def compact_change_summary(items: list[dict[str, str]], empty: str) -> str:
    if not items:
        return empty
    shown = ", ".join(format_change(item) for item in items[:12])
    extra = len(items) - 12
    if extra > 0:
        shown += f", and {extra} more"
    return shown


def latest_check_summary(checks: list[dict[str, Any]], bead: str) -> dict[str, Any]:
    bead_checks = [row for row in checks if row.get("bead") == bead]
    if not bead_checks:
        return {
            "count": 0,
            "latest_status": "missing",
            "latest_command": None,
            "latest_exit_code": None,
            "latest_output": None,
            "summary": "No recorded checks for this bead yet.",
        }
    latest = bead_checks[-1]
    command = latest.get("command") or "unknown command"
    status = latest.get("status") or "unknown"
    exit_code = latest.get("exit_code")
    output = latest.get("output")
    return {
        "count": len(bead_checks),
        "latest_status": status,
        "latest_command": command,
        "latest_exit_code": exit_code,
        "latest_output": output,
        "summary": f"{len(bead_checks)} recorded check(s); latest `{command}` -> {status} (exit {exit_code}).",
    }


def latest_loop_event(loop_rows: list[dict[str, Any]], bead: str, event: str) -> dict[str, Any] | None:
    matches = [row for row in loop_rows if row.get("bead") == bead and row.get("event") == event]
    return matches[-1] if matches else None


def previous_journal_entry(entries: list[dict[str, Any]], bead: str) -> dict[str, Any] | None:
    matches = [entry for entry in entries if entry.get("bead") == bead]
    return matches[-1] if matches else None


def build_readiness(bead_status: str, check_status: str, review_decision: str, delta_complete: bool) -> str:
    if check_status == "fail":
        return "checks failing"
    if bead_status in {"needs_info", "manual_testing"}:
        return "blocked or awaiting manual input"
    if "accepted" in review_decision.lower() or "approved" in review_decision.lower():
        return "accepted in closeout"
    if bead_status in {"review", "done"} and check_status == "pass" and delta_complete:
        return "ready for review"
    if check_status == "pass" and not delta_complete:
        return "evidence incomplete"
    if check_status == "missing":
        return "checks missing"
    return "in progress"


def uncertainty_lines(delta_complete: bool, delta_reason: str | None, dirty_paths: list[dict[str, str]]) -> list[str]:
    lines: list[str] = []
    if not delta_complete:
        lines.append(delta_reason or "Git baseline evidence is incomplete.")
    if dirty_paths:
        lines.append("Working tree has uncommitted changes; exact bead attribution may require review before acceptance.")
    return lines or ["No first-pass journal uncertainty recorded."]


def build_entry(root: Path, existing_entries: list[dict[str, Any]]) -> dict[str, Any] | None:
    todo = read_todo_state(root)
    current_bead = todo.get("current_bead") or ""
    if not current_bead:
        return None

    bead_path = root / current_bead
    if not bead_path.is_file():
        return None

    bead = read_bead(bead_path, root)
    checks = load_jsonl(root / "logs" / "check-results.jsonl")
    loop_rows = load_jsonl(root / "logs" / "loop-runs.jsonl")
    tool_rows = load_jsonl(root / "logs" / "tool-runs.jsonl")

    previous = previous_journal_entry(existing_entries, bead.rel_path)
    previous_git = previous.get("git", {}) if previous else {}
    start_commit = str(previous_git.get("end_commit") or "") or None
    end_commit = current_head(root)
    branch = current_branch(root)
    committed, diff_error = committed_changes(root, start_commit, end_commit)
    dirty = working_tree_changes(root)

    delta_complete = bool(start_commit and end_commit and diff_error is None)
    delta_reason = None
    if not start_commit:
        delta_reason = "No previous bead build journal baseline exists for this bead."
    elif not end_commit:
        delta_reason = "Current Git commit could not be resolved."
    elif diff_error:
        delta_reason = f"Git diff baseline could not be evaluated: {diff_error}."

    implementation, generated = split_change_paths(committed)
    possible_implementation, possible_generated = split_change_paths(dirty)
    check_summary = latest_check_summary(checks, bead.rel_path)
    close_event = latest_loop_event(loop_rows, bead.rel_path, "session-close")
    recent_tools = [row for row in tool_rows if row.get("task") == bead.rel_path][-8:]
    review_decision = bead.closeout.get("review_decision", "not reviewed")

    return {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "bead": bead.rel_path,
        "bead_id": bead.bead_id,
        "bead_title": bead.title,
        "bead_status": bead.status,
        "build_lane": todo.get("build_lane") or "",
        "active_feature_window": todo.get("active_feature_window") or "",
        "primary_authority": bead.primary_authority,
        "git": {
            "branch": branch,
            "start_commit": start_commit,
            "end_commit": end_commit,
            "delta_complete": delta_complete,
            "delta_reason": delta_reason,
            "dirty": bool(dirty),
        },
        "changes": {
            "implementation": implementation,
            "generated_evidence": generated,
            "unverified_possible_implementation": possible_implementation,
            "unverified_possible_generated_evidence": possible_generated,
        },
        "checks": check_summary,
        "manual_verification": bead.closeout.get("manual_verification", "not recorded"),
        "review_decision": review_decision,
        "build_readiness": build_readiness(bead.status, str(check_summary.get("latest_status")), review_decision, delta_complete),
        "remaining_uncertainty": uncertainty_lines(delta_complete, delta_reason, dirty),
        "latest_session_close": (close_event or {}).get("timestamp"),
        "recent_tool_runs": [
            {
                "timestamp": row.get("timestamp"),
                "tool": row.get("tool"),
                "class": row.get("class"),
                "status": row.get("status"),
                "command": row.get("command"),
            }
            for row in recent_tools
        ],
    }


def append_jsonl(path: Path, entry: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(entry, separators=(",", ":")) + "\n")


def render_entry(entry: dict[str, Any]) -> str:
    git_info = entry.get("git") if isinstance(entry.get("git"), dict) else {}
    changes = entry.get("changes") if isinstance(entry.get("changes"), dict) else {}
    checks = entry.get("checks") if isinstance(entry.get("checks"), dict) else {}
    uncertainty = entry.get("remaining_uncertainty") if isinstance(entry.get("remaining_uncertainty"), list) else []

    lines = [
        f"### {entry.get('timestamp', 'unknown time')}",
        "",
        f"- Bead: `{entry.get('bead') or 'missing'}`",
        f"- Status: `{entry.get('bead_status') or 'missing'}`",
        f"- Build lane: {entry.get('build_lane') or 'not recorded'}",
        f"- Active feature window: {entry.get('active_feature_window') or 'not recorded'}",
        f"- Primary authority: `{entry.get('primary_authority') or 'missing'}`",
        f"- Build readiness: {entry.get('build_readiness') or 'unknown'}",
        f"- Git baseline: `{git_info.get('start_commit') or 'missing'}` -> `{git_info.get('end_commit') or 'missing'}` on `{git_info.get('branch') or 'unknown'}`",
        f"- Implementation changes: {compact_change_summary(changes.get('implementation') or [], 'none recorded from committed baseline')}",
        f"- Generated evidence changes: {compact_change_summary(changes.get('generated_evidence') or [], 'none recorded from committed baseline')}",
        f"- Checks: {checks.get('summary') or 'No recorded checks for this bead yet.'}",
        f"- Manual verification: {entry.get('manual_verification') or 'not recorded'}",
        f"- Review decision: {entry.get('review_decision') or 'not reviewed'}",
        f"- Remaining uncertainty: {'; '.join(str(item) for item in uncertainty) if uncertainty else 'none recorded'}",
    ]

    possible_impl = changes.get("unverified_possible_implementation") or []
    possible_generated = changes.get("unverified_possible_generated_evidence") or []
    if possible_impl or possible_generated:
        lines.extend(
            [
                "",
                "#### Unverified Possible Related Changes",
                "",
                "These paths are recovery hints only because they are uncommitted or the committed Git baseline is incomplete.",
                "",
                f"- Possible implementation changes: {compact_change_summary(possible_impl, 'none')}",
                f"- Possible generated evidence changes: {compact_change_summary(possible_generated, 'none')}",
            ]
        )
    return "\n".join(lines)


def render_markdown(entries: list[dict[str, Any]]) -> str:
    if not entries:
        body = "- No bead build journal entries recorded yet."
    else:
        by_bead: dict[str, list[dict[str, Any]]] = defaultdict(list)
        for entry in entries:
            by_bead[str(entry.get("bead") or "unknown bead")].append(entry)

        blocks: list[str] = []
        for bead, bead_entries in sorted(by_bead.items()):
            recent = bead_entries[-6:]
            title = recent[-1].get("bead_title") or bead
            blocks.append(f"## {title}\n\n" + "\n\n".join(render_entry(entry) for entry in reversed(recent)))
        body = "\n\n".join(blocks)

    return f"""# PrecodeOS -- Bead Build Journal
<!-- ANCHOR: bead-build-journal -->

> AUTHORITY: Generated bead-level build-change journal and evidence-backed implementation snapshot.
> NOT_AUTHORITY: Active memory, task selection, product decisions, feature requirements, implementation plans, route structure, schema definitions, bead activation, implementation acceptance, or generated progress state.
> LOAD_WHEN: Reviewing what implementation-relevant work changed for a bead; never as active session memory.
> CLASS: generated
>
> Generated from `scripts/update-bead-build-journal.py`.
> Do not use this file as active memory, task authority, or acceptance.

Generated at: `{datetime.now(timezone.utc).isoformat()}`

## Reading Rule

Use this journal to understand what changed and what evidence supports the current build state. To continue work, load `AGENT.md`, `DECISIONS.md`, `tasks/todo.md`, the active bead, and the bead's primary authority file.

{body}
"""


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--append", action="store_true", help="append a new bead build entry before rendering markdown")
    args = parser.parse_args()

    root = repo_root()
    jsonl_path = root / JOURNAL_JSONL
    entries = load_jsonl(jsonl_path)

    if args.append:
        entry = build_entry(root, entries)
        if entry is None:
            print("bead-build-journal: no active bead found; skipped append")
        else:
            append_jsonl(jsonl_path, entry)
            entries.append(entry)
            print(f"bead-build-journal: appended {JOURNAL_JSONL}")

    md_path = root / JOURNAL_MD
    md_path.parent.mkdir(parents=True, exist_ok=True)
    md_path.write_text(render_markdown(entries), encoding="utf-8")
    print(f"bead-build-journal: wrote {JOURNAL_MD}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
