#!/usr/bin/env python3
# Version: v0.1.0
# Last updated: 2026-04-26
# Owner: Precode OS
from __future__ import annotations

import json
import subprocess
from pathlib import Path

from os_compiler import close_readiness, follow_up_suggestion, latest_by_command, load_jsonl, read_bead, read_todo_state, repo_root
from os_parser import replace_labeled_bullets


CLOSEOUT_LABELS = [
    ("Checks run", "checks_run"),
    ("Result", "result"),
    ("Manual verification", "manual_verification"),
    ("Files changed", "files_changed"),
    ("Next bead", "next_bead"),
    ("Review decision", "review_decision"),
    ("Drift observed", "drift_observed"),
    ("Lesson to promote", "lesson_to_promote"),
    ("Follow-up bead needed", "follow_up_bead_needed"),
    ("Blocked escape", "blocked_escape"),
    ("Evidence source", "evidence_source"),
]


def current_bead_path(root: Path) -> Path | None:
    todo = read_todo_state(root)
    current = todo.get("current_bead") or ""
    if not current:
        return None
    path = root / current
    return path if path.is_file() else None


def git_changed_summary(root: Path) -> str:
    try:
        result = subprocess.run(
            ["git", "status", "--short"],
            cwd=root,
            check=False,
            capture_output=True,
            text=True,
        )
    except OSError:
        return "unknown"
    lines = [line for line in result.stdout.splitlines() if line.strip()]
    if not lines:
        return "none"
    return f"{len(lines)} changed path(s)"


def render_check_summary(results: list[dict[str, object]]) -> str:
    if not results:
        return "no recorded command results yet; use `bash scripts/record-check.sh -- <command>`"

    summaries: list[str] = []
    for entry in results[-8:]:
        command = str(entry.get("command") or "")
        check_status = str(entry.get("status") or "unknown")
        exit_code = entry.get("exit_code")
        timestamp = str(entry.get("timestamp") or "")
        output = str(entry.get("output") or "")
        summaries.append(f"`{command}` -> {check_status} (exit {exit_code}) at {timestamp}; log `{output}`")
    return " | ".join(summaries)


def normalize_blocked_escape(value: str) -> str:
    if value.startswith("not needed while status is `") and not value.endswith("`"):
        return value + "`"
    return value


def main() -> int:
    root = repo_root()
    bead_path = current_bead_path(root)
    if bead_path is None:
        print("update-bead-closeout: no current bead found")
        return 0

    bead = read_bead(bead_path, root)
    current_text = bead_path.read_text(encoding="utf-8")
    check_results = load_jsonl(root / "logs" / "check-results.jsonl")
    bead_results = [row for row in check_results if row.get("bead") == bead.rel_path]
    close_state = close_readiness(bead, latest_by_command(check_results, bead.rel_path))

    blocked_fallback = (
        "name an unblocker bead, safe parallel bead, or exact manual input"
        if bead.status in {"needs_info", "manual_testing"}
        else f"not needed while status is `{bead.status}`"
    )

    values = {
        "checks_run": render_check_summary(bead_results),
        "result": (
            f"latest recorded command status is {bead_results[-1].get('status')} (exit {bead_results[-1].get('exit_code')})"
            if bead_results
            else "no recorded command results yet"
        ),
        "manual_verification": bead.closeout.get("manual_verification", "not recorded"),
        "files_changed": f"{git_changed_summary(root)} at last evidence update",
        "next_bead": bead.closeout.get("next_bead", "not evaluated"),
        "review_decision": bead.closeout.get("review_decision", "not reviewed"),
        "drift_observed": bead.closeout.get("drift_observed", "none recorded"),
        "lesson_to_promote": bead.closeout.get("lesson_to_promote", "none"),
        "follow_up_bead_needed": follow_up_suggestion(bead, close_state),
        "blocked_escape": normalize_blocked_escape(bead.closeout.get("blocked_escape", blocked_fallback)),
        "evidence_source": "`logs/check-results.jsonl`",
    }

    ordered_items = [(label, values[key]) for label, key in CLOSEOUT_LABELS]
    updated = replace_labeled_bullets(current_text, "Closeout Evidence", ordered_items)
    if updated != current_text:
        bead_path.write_text(updated, encoding="utf-8")
        print(f"update-bead-closeout: updated {bead.rel_path}")
    else:
        print(f"update-bead-closeout: {bead.rel_path} already current")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
