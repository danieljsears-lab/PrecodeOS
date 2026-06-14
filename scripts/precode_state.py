#!/usr/bin/env python3
# Version: v0.1.0
# Last updated: 2026-06-14
# Owner: PrecodeOS
# Created by Dan Sears / Recode.
# SPDX-License-Identifier: Apache-2.0
from __future__ import annotations

from dataclasses import dataclass
import json
import re
import subprocess
from pathlib import Path
from typing import Any

from os_parser import (
    MarkdownDocument,
    bullet_items,
    colon_bullets,
    first_bullet,
    read_text,
    split_frontmatter,
    strip_inline_code,
)


FRONTMATTER_EMPTY_MARKERS = {"", "none", "n/a", "na", "null", "not applicable"}


@dataclass
class BeadRecord:
    rel_path: str
    title: str
    bead_id: str
    status: str
    execution_mode: str
    bead_kind: str
    primary_authority: str
    depends_on: list[str]
    parent_prd: str
    requirement_ids: list[str]
    files_in_play: list[str]
    checks: list[str]
    verification_type: list[str]
    delegation_mode: str
    test_strategy: str
    review_context: str
    complexity: str
    required_planning_depth: str
    autonomy_level: str
    run_contract: dict[str, Any]
    closeout: dict[str, str]
    handback: str
    frontmatter: dict[str, Any]
    sections: dict[str, str]


def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def rel_path(path: Path, root: Path) -> str:
    return path.relative_to(root).as_posix()


def normalize_status(value: str) -> str:
    return value.lower().strip().replace("-", "_").replace(" ", "_")


def normalize_optional(value: str | None) -> str:
    cleaned = strip_inline_code(value or "")
    return "" if cleaned.lower() in FRONTMATTER_EMPTY_MARKERS else cleaned


def normalize_list(items: list[Any] | None) -> list[str]:
    values: list[str] = []
    for item in items or []:
        value = strip_inline_code(str(item))
        if not value or value.lower() in FRONTMATTER_EMPTY_MARKERS:
            continue
        values.append(value)
    return values


def split_list_value(value: Any) -> list[str]:
    if isinstance(value, list):
        return normalize_list(value)
    text = strip_inline_code(str(value or ""))
    if not text or text.lower() in FRONTMATTER_EMPTY_MARKERS:
        return []
    if "\n" in text:
        return normalize_list([line.strip().removeprefix("-").strip() for line in text.splitlines()])
    return normalize_list([item.strip() for item in re.split(r",|;", text)])


def normalize_bool(value: Any) -> bool:
    if isinstance(value, bool):
        return value
    return str(value or "").strip().lower() in {"true", "yes", "required", "enabled"}


def number_or_none(value: Any) -> float | None:
    if value is None or value == "":
        return None
    if isinstance(value, (int, float)):
        return float(value)
    try:
        return float(str(value))
    except ValueError:
        return None


def int_or_none(value: Any) -> int | None:
    number = number_or_none(value)
    return int(number) if number is not None else None


def normalize_inline_status_value(value: str) -> str:
    if value.startswith("not needed while status is `") and not value.endswith("`"):
        return value + "`"
    return value


def heading_title(text: str) -> str:
    _, body = split_frontmatter(text)
    for line in body.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return ""


def parse_next_bead_reference(value: str, root: Path) -> str | None:
    if not value:
        return None

    path_match = re.search(r"`?(tasks/beads/[^`\s)]+\.md)`?", value)
    if path_match:
        candidate = path_match.group(1)
        if (root / candidate).is_file():
            return candidate

    id_match = re.search(r"\b(B\d{3})\b", value)
    if not id_match:
        return None

    bead_id = id_match.group(1).lower()
    matches = [
        path for path in (root / "tasks" / "beads").glob("*.md")
        if path.name.lower().startswith(f"{bead_id}-")
    ]
    if not matches:
        return None
    return rel_path(sorted(matches)[0], root)


def bead_paths(root: Path) -> list[Path]:
    return sorted(path for path in (root / "tasks" / "beads").glob("*.md") if path.name != "BEAD-SCHEMA.md")


def parse_closeout_values(section: str) -> dict[str, str]:
    return colon_bullets(section)


def normalize_run_contract(raw: Any, section: str, bead_defaults: dict[str, Any]) -> dict[str, Any]:
    section_values = colon_bullets(section)
    data = raw if isinstance(raw, dict) else {}

    def field(name: str, *aliases: str) -> Any:
        for key in (name, *aliases):
            if key in data:
                return data.get(key)
            normalized = re.sub(r"[^a-z0-9]+", "_", key.strip().lower()).strip("_")
            if normalized in section_values:
                return section_values.get(normalized)
        return None

    allowed_paths = split_list_value(field("allowed_paths", "allowed files", "allowed actions")) or list(
        bead_defaults.get("files_in_play") or []
    )
    proof_needed = split_list_value(field("proof_needed", "proof lanes", "proof required"))
    allowed_tool_classes = split_list_value(field("allowed_tool_classes", "allowed tool classes"))
    approval_required_before = split_list_value(field("approval_required_before", "approval gates"))
    stop_if = split_list_value(field("stop_if", "stop conditions")) or split_list_value(bead_defaults.get("stop_if"))
    forbidden_actions = split_list_value(field("forbidden_actions", "forbidden commands", "forbidden"))

    required_raw = field("required")
    required = normalize_bool(required_raw) if required_raw is not None else False

    has_contract = bool(data or section.strip() or required or proof_needed or allowed_tool_classes or approval_required_before)
    return {
        "present": has_contract,
        "required": required,
        "required_reasons": [],
        "allowed_paths": allowed_paths,
        "allowed_tool_classes": allowed_tool_classes,
        "forbidden_actions": forbidden_actions,
        "approval_required_before": approval_required_before,
        "proof_needed": [item.lower() for item in proof_needed],
        "stop_if": stop_if,
        "rollback_or_blocked_escape": normalize_optional(
            str(field("rollback_or_blocked_escape", "rollback", "blocked escape") or "")
        ),
        "expires_when": normalize_optional(str(field("expires_when", "expiration", "lease expires when") or "")),
        "advisory_only": True,
    }


def read_bead(path: Path, root: Path) -> BeadRecord:
    text = read_text(path)
    doc = MarkdownDocument.load(path)
    state_values = colon_bullets(doc.sections.get("State", ""))

    bead_id = normalize_optional(str(doc.frontmatter.get("bead_id") or state_values.get("id") or path.stem.split("-", 1)[0]))
    status = normalize_status(
        normalize_optional(str(doc.frontmatter.get("status") or state_values.get("status") or "missing"))
    )
    execution_mode = normalize_optional(str(doc.frontmatter.get("execution_mode") or state_values.get("execution_mode") or ""))
    bead_kind = normalize_optional(str(doc.frontmatter.get("bead_kind") or "implementation")) or "implementation"
    primary_authority = normalize_optional(
        str(doc.frontmatter.get("primary_authority") or first_bullet(doc.sections.get("Primary Authority", "")) or "")
    )
    depends_on = normalize_list(doc.frontmatter.get("depends_on")) or normalize_list(bullet_items(doc.sections.get("Depends On", "")))
    parent_prd = normalize_optional(
        str(doc.frontmatter.get("parent_prd") or first_bullet(doc.sections.get("Parent PRD", "")) or "")
    )
    requirement_ids = normalize_list(doc.frontmatter.get("requirement_ids")) or normalize_list(
        bullet_items(doc.sections.get("Requirement IDs", ""))
    )
    files_in_play = normalize_list(doc.frontmatter.get("files_in_play")) or normalize_list(
        bullet_items(doc.sections.get("Files In Play", ""))
    )
    checks = normalize_list(doc.frontmatter.get("checks")) or normalize_list(bullet_items(doc.sections.get("Checks", "")))
    verification_type = normalize_list(doc.frontmatter.get("verification_type")) or normalize_list(
        bullet_items(doc.sections.get("Verification Type", ""))
    )
    delegation_mode = normalize_optional(
        str(doc.frontmatter.get("delegation_mode") or first_bullet(doc.sections.get("Delegation Mode", "")) or "")
    )
    test_strategy = normalize_optional(
        str(doc.frontmatter.get("test_strategy") or first_bullet(doc.sections.get("Test Strategy", "")) or "")
    )
    review_context = normalize_optional(
        str(doc.frontmatter.get("review_context") or first_bullet(doc.sections.get("Review Context", "")) or "")
    )
    complexity = normalize_optional(
        str(doc.frontmatter.get("complexity") or first_bullet(doc.sections.get("Complexity", "")) or "")
    )
    required_planning_depth = normalize_optional(
        str(
            doc.frontmatter.get("required_planning_depth")
            or first_bullet(doc.sections.get("Required Planning Depth", ""))
            or ""
        )
    )
    autonomy_level = normalize_optional(
        str(doc.frontmatter.get("autonomy_level") or first_bullet(doc.sections.get("Autonomy Level", "")) or "")
    )
    run_contract = normalize_run_contract(
        doc.frontmatter.get("run_contract"),
        doc.sections.get("Run Contract", ""),
        {
            "files_in_play": files_in_play,
            "stop_if": doc.sections.get("Stop If", ""),
        },
    )

    return BeadRecord(
        rel_path=rel_path(path, root),
        title=heading_title(text),
        bead_id=bead_id,
        status=status,
        execution_mode=execution_mode,
        bead_kind=bead_kind,
        primary_authority=primary_authority,
        depends_on=depends_on,
        parent_prd=parent_prd,
        requirement_ids=requirement_ids,
        files_in_play=files_in_play,
        checks=checks,
        verification_type=verification_type,
        delegation_mode=delegation_mode,
        test_strategy=test_strategy,
        review_context=review_context,
        complexity=complexity,
        required_planning_depth=required_planning_depth,
        autonomy_level=autonomy_level,
        run_contract=run_contract,
        closeout=parse_closeout_values(doc.sections.get("Closeout Evidence", "")),
        handback=doc.sections.get("Handback", ""),
        frontmatter=doc.frontmatter,
        sections=doc.sections,
    )


def read_todo_state(root: Path) -> dict[str, Any]:
    todo_path = root / "tasks" / "todo.md"
    doc = MarkdownDocument.load(todo_path)
    current_bead = normalize_optional(
        str(doc.frontmatter.get("current_bead") or first_bullet(doc.sections.get("Current Bead", "")) or "")
    )
    primary_authority = normalize_optional(
        str(doc.frontmatter.get("primary_authority") or first_bullet(doc.sections.get("Primary Authority File", "")) or "")
    )
    state_values = colon_bullets(doc.sections.get("Current Bead", ""))
    return {
        "path": "tasks/todo.md",
        "frontmatter": doc.frontmatter,
        "sections": doc.sections,
        "current_bead": current_bead,
        "current_state": normalize_status(str(doc.frontmatter.get("current_state") or state_values.get("state") or "")),
        "build_lane": normalize_optional(str(doc.frontmatter.get("build_lane") or state_values.get("build_lane") or "")),
        "active_feature_window": normalize_optional(
            str(doc.frontmatter.get("active_feature_window") or state_values.get("active_feature_window") or "")
        ),
        "primary_authority": primary_authority,
    }


def goal_frame_candidate_paths(root: Path) -> list[Path]:
    paths: list[Path] = []
    for rel in ("PRODUCT.md", "DECISIONS.md"):
        path = root / rel
        if path.is_file():
            paths.append(path)
    paths.extend(sorted((root / "tasks" / "prds").glob("*.md")))
    paths.extend(bead_paths(root))
    return paths


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    if not path.is_file():
        return []
    rows: list[dict[str, Any]] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        try:
            rows.append(json.loads(line))
        except json.JSONDecodeError:
            continue
    return rows


def run_git(args: list[str], root: Path) -> str:
    result = subprocess.run(
        ["git", *args],
        cwd=root,
        check=False,
        capture_output=True,
        text=True,
    )
    return result.stdout.strip()


def parse_check_command(raw: str) -> dict[str, str]:
    cwd = "."
    cwd_match = re.search(r"--cwd\s+([^\s]+)", raw)
    if cwd_match:
        cwd = cwd_match.group(1)

    command = raw
    if " -- " in raw:
        command = raw.split(" -- ", 1)[1]
    return {"command": command.strip(), "cwd": cwd, "source": raw.strip()}


def latest_by_command(rows: list[dict[str, Any]], bead: str | None) -> dict[tuple[str, str], dict[str, Any]]:
    latest: dict[tuple[str, str], dict[str, Any]] = {}
    for row in rows:
        if bead and row.get("bead") != bead:
            continue
        command = str(row.get("command") or "")
        cwd = str(row.get("cwd") or ".")
        if command:
            latest[(command, cwd)] = row
            latest[(command, ".")] = row
    return latest
