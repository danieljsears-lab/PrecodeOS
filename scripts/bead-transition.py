#!/usr/bin/env python3
# Version: v0.1.3
# Last updated: 2026-06-23
# Owner: PrecodeOS
# Created by Dan Sears / Recode.
# SPDX-License-Identifier: Apache-2.0
from __future__ import annotations

import argparse
from dataclasses import dataclass
from datetime import datetime, timezone
import json
import subprocess
import sys
from pathlib import Path

from os_compiler import compile_state, read_bead, read_todo_state, repo_root
from os_parser import MarkdownDocument, replace_frontmatter, replace_section


BEAD_FRONTMATTER_ORDER = [
    "bead_id",
    "status",
    "execution_mode",
    "bead_kind",
    "primary_authority",
    "depends_on",
    "parent_prd",
    "requirement_ids",
    "files_in_play",
    "checks",
    "verification_type",
    "delegation_mode",
    "test_strategy",
    "review_context",
    "complexity",
    "required_planning_depth",
    "autonomy_level",
]

TODO_FRONTMATTER_ORDER = [
    "current_bead",
    "current_state",
    "build_lane",
    "active_feature_window",
    "primary_authority",
]


@dataclass
class FileSnapshot:
    path: Path
    existed: bool
    content: str


def transition_assessment(root: Path) -> dict[str, object]:
    payload = compile_state(root)
    readiness = payload["readiness"]["current_promotion"]
    current = payload.get("current_bead")
    next_bead = readiness.get("next_bead")

    next_summary = None
    if isinstance(next_bead, str) and (root / next_bead).is_file():
        bead = read_bead(root / next_bead, root)
        next_summary = {
            "rel_path": bead.rel_path,
            "objective": bead.sections.get("Objective", ""),
            "primary_authority": bead.primary_authority,
            "done_when": bead.sections.get("Done When", ""),
            "checks": bead.checks,
            "complexity": bead.complexity,
            "required_planning_depth": bead.required_planning_depth,
            "autonomy_level": bead.autonomy_level,
            "stop_if": bead.sections.get("Stop If", ""),
        }

    return {
        "eligible": readiness["eligible"],
        "blockers": readiness["blockers"],
        "current": current,
        "current_status": payload.get("current_bead_status"),
        "next": next_bead,
        "next_summary": next_summary,
        "latest_results": payload.get("active_bead_checks", []),
    }


def print_proposal(assessment: dict[str, object]) -> None:
    current = assessment.get("current") or "(missing)"
    next_bead = assessment.get("next") or "(missing)"
    blockers = assessment.get("blockers") or []

    if blockers:
        print("No bead promotion proposal is available yet.")
        print(f"Current bead: {current}")
        print("\nBlockers:")
        for blocker in blockers:
            print(f"- {blocker}")
        return

    next_summary = assessment.get("next_summary") or {}
    latest_results = assessment.get("latest_results") or []
    print("Next Bead Proposal")
    print(f"From: {current}")
    print(f"To: {next_bead}")
    print("\nWhy proposed:")
    print("- Current bead passes the compiled promotion readiness model")
    print("- Review decision is accepted and manual verification is clear")
    print("- Latest recorded command results pass for the active bead")
    print("\nNext bead summary:")
    if next_summary:
        print("\nObjective:")
        print(next_summary.get("objective") or "- (missing)")
        print("\nPrimary Authority:")
        print(f"- `{next_summary.get('primary_authority') or '(missing)'}`")
        print("\nDone When:")
        print(next_summary.get("done_when") or "- (missing)")
        print("\nChecks:")
        for check in next_summary.get("checks") or []:
            print(f"- `{check}`")
        print("\nAdaptive depth:")
        print(f"- Complexity: `{next_summary.get('complexity') or 'unspecified'}`")
        print(f"- Required planning depth: `{next_summary.get('required_planning_depth') or 'unspecified'}`")
        print(f"- Autonomy level: `{next_summary.get('autonomy_level') or 'unspecified'}`")
        print("\nStop If:")
        print(next_summary.get("stop_if") or "- (missing)")
    print("\nRecent recorded checks:")
    for entry in list(latest_results)[-5:]:
        print(f"- `{entry.get('command')}` -> {entry.get('status')} (exit {entry.get('exit_code')})")
    print("\nTo approve task initiation:")
    print("- `python3 scripts/bead-transition.py --approve`")


def update_bead_status(path: Path, new_status: str, root: Path) -> None:
    doc = MarkdownDocument.load(path)
    bead = read_bead(path, root)
    frontmatter = dict(doc.frontmatter)
    frontmatter["status"] = new_status

    state_body = "\n".join(
        [
            f"- ID: `{bead.bead_id}`",
            f"- Status: `{new_status}`",
            f"- Execution mode: `{bead.execution_mode}`",
        ]
    )
    updated = replace_frontmatter(path.read_text(encoding="utf-8"), frontmatter, key_order=BEAD_FRONTMATTER_ORDER)
    updated = replace_section(updated, "State", f"## State\n\n{state_body}\n")
    path.write_text(updated, encoding="utf-8")


def bullet_block(items: list[str], default: str) -> str:
    if not items:
        return default
    return "\n".join(f"- `{item}`" for item in items)


def rewrite_todo(root: Path, current_rel: str, next_rel: str) -> None:
    todo_state = read_todo_state(root)
    next_bead = read_bead(root / next_rel, root)
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    build_lane = todo_state.get("build_lane") or "PrecodeOS adoption"
    active_feature_window = todo_state.get("active_feature_window") or "Features 0-9"

    frontmatter = {
        "current_bead": next_rel,
        "current_state": "in_progress",
        "build_lane": build_lane,
        "active_feature_window": active_feature_window,
        "primary_authority": next_bead.primary_authority,
    }

    explicit_out = next_bead.sections.get("Stop If", "").strip()
    if explicit_out:
        explicit_out = explicit_out + "\n- Stop condition: pause and ask before crossing any stop condition above."
    else:
        explicit_out = "- Stop condition: pause and ask before crossing this bead boundary."

    todo = f"""{replace_frontmatter('', frontmatter, key_order=TODO_FRONTMATTER_ORDER).strip()}
# PrecodeOS — Active Work File
<!-- ANCHOR: active-work -->
> AUTHORITY: Current task, done-when target, primary authority file, files in play, checks to run, immediate next-up queue, open questions, and noticed execution facts.
> NOT_AUTHORITY: Resolved decisions, feature requirements, generated progress, or long-range roadmap commitments.
> LOAD_WHEN: Start and end of every session and whenever task scope materially changes.
> CLASS: active-memory
>
> This file is the active execution pointer inside the active memory set.
> AI coding agents read and update this file at the start and end of meaningful work.
> Active memory set: `AGENT.md`, `DECISIONS.md`, and `tasks/todo.md`.
> `AGENT.md` is the entrypoint. `DECISIONS.md` is the decision log. `PROGRESS.md` is generated output only.
> Detailed execution contracts live in `tasks/beads/*.md`.
> Rewrite, don't append.
> Primary Authority File must be exactly one file.
> Files In Play should stay narrow; if it exceeds 20 entries, split the task.
> Open Questions only contains blockers that can change execution, not general curiosities.
> Noticed is facts only, never directives or hidden backlog.

---

## Current Bead

- `{next_rel}`
- State: `in_progress`
- Build lane: `{build_lane}`
- Active feature window: `{active_feature_window}`

## Done When

{next_bead.sections.get("Done When", "").strip() or "- The active bead Done When section is satisfied."}

## Primary Authority File

- `{next_bead.primary_authority or '(missing)'}`

## Files In Play

{bullet_block(next_bead.files_in_play, "- (missing)")}

## Checks To Run

{bullet_block(next_bead.checks, "- `bash scripts/record-check.sh -- bash scripts/validate-memory.sh`")}

## Explicit Out-of-Scope

{explicit_out}

## Next Up

- Begin `{next_rel}` only within its Done When, Files In Play, and Stop If boundaries.
- If the bead is too broad, split it before implementation.

## Open Questions

- None.

## Noticed

- Promoted from `{current_rel}` to `{next_rel}` by `python3 scripts/bead-transition.py --approve` at {now}.
"""
    (root / "tasks" / "todo.md").write_text(todo + "\n", encoding="utf-8")


def append_transition_log(root: Path, current_rel: str, next_rel: str) -> None:
    log_path = root / "logs" / "bead-transitions.jsonl"
    log_path.parent.mkdir(parents=True, exist_ok=True)
    entry = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "event": "bead-promoted",
        "from": current_rel,
        "to": next_rel,
    }
    with log_path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(entry, separators=(",", ":")) + "\n")


def preflight_approval(root: Path, assessment: dict[str, object]) -> tuple[str, str] | None:
    if not assessment.get("eligible"):
        print_proposal(assessment)
        return None

    current = assessment.get("current")
    next_bead = assessment.get("next")
    blockers: list[str] = []

    if not isinstance(current, str) or not current.strip():
        blockers.append("current bead is missing")
    elif not (root / current).is_file():
        blockers.append(f"current bead file is missing: {current}")
    current_status = str(assessment.get("current_status") or "").strip()
    if current_status and current_status != "review":
        blockers.append(f"current bead status must be review before promotion; found {current_status}")

    if not isinstance(next_bead, str) or not next_bead.strip():
        blockers.append("next bead is missing")
    elif not (root / next_bead).is_file():
        blockers.append(f"next bead file is missing: {next_bead}")

    if blockers:
        blocked_assessment = dict(assessment)
        blocked_assessment["blockers"] = blockers
        print_proposal(blocked_assessment)
        return None

    return current, next_bead


def snapshot_files(paths: list[Path]) -> list[FileSnapshot]:
    snapshots: list[FileSnapshot] = []
    for path in paths:
        if path.is_file():
            snapshots.append(FileSnapshot(path=path, existed=True, content=path.read_text(encoding="utf-8")))
        else:
            snapshots.append(FileSnapshot(path=path, existed=False, content=""))
    return snapshots


def restore_files(snapshots: list[FileSnapshot]) -> None:
    for snapshot in snapshots:
        if snapshot.existed:
            snapshot.path.parent.mkdir(parents=True, exist_ok=True)
            snapshot.path.write_text(snapshot.content, encoding="utf-8")
        elif snapshot.path.exists():
            snapshot.path.unlink()


def approve_transition(root: Path, assessment: dict[str, object]) -> int:
    preflight = preflight_approval(root, assessment)
    if preflight is None:
        return 1

    current_rel, next_rel = preflight
    snapshots = snapshot_files(
        [
            root / current_rel,
            root / next_rel,
            root / "tasks" / "todo.md",
            root / "logs" / "bead-transitions.jsonl",
        ]
    )
    update_bead_status(root / current_rel, "done", root)
    update_bead_status(root / next_rel, "in_progress", root)
    rewrite_todo(root, current_rel, next_rel)
    append_transition_log(root, current_rel, next_rel)

    result = subprocess.run(["bash", "scripts/validate-memory.sh"], cwd=root, check=False)
    if result.returncode != 0:
        restore_files(snapshots)
        print(
            "bead-transition: promotion failed validation and was rolled back; inspect validation output before retrying",
            file=sys.stderr,
        )
        return result.returncode

    print(f"bead-transition: promoted {current_rel} -> {next_rel}")
    return 0


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Propose or approve the next bead transition.")
    parser.add_argument("--approve", action="store_true", help="Mutate bead state and tasks/todo.md after readiness checks pass.")
    parser.add_argument("--json", action="store_true", help="Print machine-readable assessment.")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    root = repo_root()
    assessment = transition_assessment(root)

    if args.json:
        print(json.dumps(assessment, indent=2, default=str))
        return 0 if assessment.get("eligible") else 1

    if args.approve:
        return approve_transition(root, assessment)

    print_proposal(assessment)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
