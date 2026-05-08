#!/usr/bin/env python3
# Version: v0.1.1
# Last updated: 2026-05-07
# Owner: Precode OS
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from os_compiler import ACTIVE_MEMORY, GENERATED_REPORTS, compile_state, repo_root
from os_parser import bullet_items, read_text


VAGUE_QUESTION_TERMS = {"maybe", "later", "todo", "tbd", "consider", "sometime", "nice to have"}
BLOCKER_TERMS = {"block", "blocked", "blocking", "depends", "decision", "waiting", "needs", "must choose"}
BROAD_FILE_MARKERS = {".", "./", "*", "/*", "tasks", "tasks/", "scripts", "scripts/", "logs", "logs/"}


def add_warning(warnings: list[str], message: str) -> None:
    if message not in warnings:
        warnings.append(message)


def rel_exists(root: Path, value: str) -> bool:
    cleaned = value.strip().strip("`")
    return bool(cleaned) and (root / cleaned).exists()


def current_bead_record(state: dict[str, Any]) -> dict[str, Any] | None:
    current = state.get("current_bead")
    for bead in state.get("beads", []):
        if bead.get("rel_path") == current:
            return bead
    return None


def generated_execution_sources(root: Path, state: dict[str, Any], bead: dict[str, Any] | None) -> list[str]:
    hits: list[str] = []
    generated = set(GENERATED_REPORTS)
    todo = state.get("todo", {})
    todo_sources = []
    todo_sources.append(str(todo.get("primary_authority") or ""))
    todo_sources.extend(bullet_items((todo.get("sections") or {}).get("Primary Authority File", "")))
    todo_sources.extend(bullet_items((todo.get("sections") or {}).get("Files In Play", "")))
    todo_sources.extend(bullet_items((todo.get("sections") or {}).get("Checks To Run", "")))

    bead_sources = []
    if bead:
        bead_sources.append(str(bead.get("primary_authority") or ""))
        bead_sources.extend(bead.get("files_in_play") or [])
        bead_sources.extend(bead.get("checks") or [])

    for source in todo_sources + bead_sources:
        cleaned = source.strip().strip("`")
        for report in generated:
            if report in cleaned:
                hits.append(cleaned)

    return sorted(set(hits))


def broad_files(files_in_play: list[str]) -> list[str]:
    broad: list[str] = []
    for item in files_in_play:
        cleaned = item.strip().strip("`")
        if cleaned in BROAD_FILE_MARKERS:
            broad.append(cleaned)
            continue
        if cleaned.endswith("/") or cleaned.endswith("/*"):
            broad.append(cleaned)
            continue
        if "/" not in cleaned and "." not in Path(cleaned).name:
            broad.append(cleaned)
    return sorted(set(broad))


def vague_open_questions(todo_sections: dict[str, str]) -> list[str]:
    section = todo_sections.get("Open Questions", "")
    lines = [line.strip() for line in section.splitlines() if line.strip().startswith("- ")]
    vague: list[str] = []
    for line in lines:
        lowered = line.lower()
        if any(term in lowered for term in VAGUE_QUESTION_TERMS) and not any(term in lowered for term in BLOCKER_TERMS):
            vague.append(line)
    return vague


def prds_missing_context_contract(root: Path) -> list[str]:
    missing: list[str] = []
    prd_dir = root / "tasks" / "prds"
    if not prd_dir.is_dir():
        return missing
    for path in sorted(prd_dir.glob("*.md")):
        if path.name == "PRD-SHARD-SCHEMA.md":
            continue
        text = read_text(path)
        if "## Agent Context Contract" not in text:
            missing.append(path.relative_to(root).as_posix())
    return missing


def requirement_prd_warnings(root: Path, bead: dict[str, Any] | None) -> list[str]:
    if not bead:
        return []
    requirement_ids = bead.get("requirement_ids") or []
    if not requirement_ids:
        return []
    parent_prd = str(bead.get("parent_prd") or "").strip().strip("`")
    if not parent_prd:
        return [f"{bead.get('rel_path')} has requirement IDs but no parent PRD"]
    if not (root / parent_prd).is_file():
        return [f"{bead.get('rel_path')} points to missing parent PRD {parent_prd}"]
    return []


def main() -> int:
    root = repo_root()
    state = compile_state(root)
    warnings: list[str] = []
    details: dict[str, Any] = {}

    active_memory = state.get("active_memory") or []
    details["active_memory"] = active_memory
    if active_memory != ACTIVE_MEMORY:
        add_warning(warnings, "active memory drift: expected AGENT.md, DECISIONS.md, and tasks/todo.md only")

    bead = current_bead_record(state)
    details["current_bead"] = state.get("current_bead") or ""
    if not bead:
        add_warning(warnings, "no active bead record found for current_bead")
    else:
        primary_authority = str(bead.get("primary_authority") or "").strip()
        details["primary_authority"] = primary_authority
        if not primary_authority:
            add_warning(warnings, f"{bead.get('rel_path')} is missing a primary authority")
        elif not rel_exists(root, primary_authority):
            add_warning(warnings, f"{bead.get('rel_path')} primary authority does not exist: {primary_authority}")

        files = [str(item) for item in bead.get("files_in_play") or []]
        details["files_in_play_count"] = len(files)
        details["broad_files_in_play"] = broad_files(files)
        if len(files) > 8:
            add_warning(warnings, f"{bead.get('rel_path')} has more than eight files in play")
        if details["broad_files_in_play"]:
            add_warning(warnings, f"{bead.get('rel_path')} has broad files in play: {', '.join(details['broad_files_in_play'])}")

    generated_hits = generated_execution_sources(root, state, bead)
    details["generated_execution_sources"] = generated_hits
    if generated_hits:
        add_warning(warnings, "generated reports appear in execution sources; they should remain audit-only")

    missing_prd_contracts = prds_missing_context_contract(root)
    details["prds_missing_agent_context_contract"] = missing_prd_contracts
    for path in missing_prd_contracts:
        add_warning(warnings, f"{path} is missing an Agent Context Contract")

    requirement_warnings = requirement_prd_warnings(root, bead)
    details["requirement_prd_warnings"] = requirement_warnings
    for warning in requirement_warnings:
        add_warning(warnings, warning)

    todo_sections = (state.get("todo") or {}).get("sections") or {}
    vague_questions = vague_open_questions(todo_sections)
    details["vague_open_questions"] = vague_questions
    if vague_questions:
        add_warning(warnings, "tasks/todo.md has vague open questions that may not be current execution blockers")

    payload = {
        "tool": "context-check",
        "status": "warn" if warnings else "pass",
        "warnings": warnings,
        "details": details,
    }
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
