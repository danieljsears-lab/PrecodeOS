#!/usr/bin/env python3
# Version: v0.1.3
# Last updated: 2026-08-06
# Owner: PrecodeOS
# Created by Dan Sears / Recode.
# SPDX-License-Identifier: Apache-2.0
from __future__ import annotations

import json
from pathlib import Path
import re
from typing import Any

from os_compiler import repo_root


CONTRACT_FIELDS = ("AUTHORITY", "NOT_AUTHORITY", "LOAD_WHEN", "CLASS")
ACTIVE_MEMORY = {"AGENT.md", "DECISIONS.md", "tasks/todo.md"}


def rel(path: Path, root: Path) -> str:
    return path.relative_to(root).as_posix()


def contract(text: str) -> dict[str, str]:
    values: dict[str, str] = {}
    for key in CONTRACT_FIELDS:
        match = re.search(rf"^>\s*{key}:\s*(.+)$", text, re.MULTILINE)
        if match:
            values[key] = match.group(1).strip()
    return values


def anchor(text: str) -> str:
    match = re.search(r"<!--\s*ANCHOR:\s*([a-z0-9-]+)\s*-->", text)
    return match.group(1) if match else ""


def add_issue(issues: list[dict[str, Any]], path: str, message: str, severity: str = "warning") -> None:
    issues.append({"path": path, "severity": severity, "message": message})


def is_checkpoint_source_snapshot(name: str) -> bool:
    return name.startswith("logs/os-checkpoints/") and "/files/" in name


def check_markdown(path: Path, root: Path, issues: list[dict[str, Any]]) -> None:
    text = path.read_text(encoding="utf-8")
    name = rel(path, root)
    if is_checkpoint_source_snapshot(name):
        return
    values = contract(text)
    anchor_required = name.startswith("tasks/reference/") or (name.startswith("logs/") and name != "logs/LOG-EVIDENCE-TAXONOMY.md")
    if anchor_required and not anchor(text):
        add_issue(issues, name, "missing canonical anchor")
    for field in CONTRACT_FIELDS:
        if field not in values:
            add_issue(issues, name, f"missing authority contract field: {field}")
    if (name.startswith("logs/") and name != "logs/LOG-EVIDENCE-TAXONOMY.md") or values.get("CLASS") == "generated":
        if values.get("CLASS") != "generated":
            add_issue(issues, name, "generated markdown under logs should use CLASS: generated")
        demotion_text = text.lower()
        if "active memory" not in demotion_text or ("not" not in demotion_text and "never" not in demotion_text):
            add_issue(issues, name, "generated markdown should clearly say it is not active memory")


def check_release_readiness_curated_pack_exemplar(root: Path, issues: list[dict[str, Any]]) -> None:
    path = root / "tasks/templates/RELEASE-READINESS-CURATED-PACK-EXEMPLAR.md"
    name = rel(path, root)
    if not path.is_file():
        add_issue(issues, name, "missing official release-readiness curated pack exemplar", "error")
        return
    text = path.read_text(encoding="utf-8")
    values = contract(text)
    for field in CONTRACT_FIELDS:
        if field not in values:
            add_issue(issues, name, f"missing authority contract field: {field}", "error")
    if not anchor(text):
        add_issue(issues, name, "missing canonical anchor", "error")

    required_terms = [
        "status: exemplar-review-shape",
        "distribution_behavior: none",
        "registry_or_marketplace_behavior: none",
        "install_update_package_manager_behavior: none",
        "active_memory_changes: none",
        "external_systems_touched: none",
        "read_only_by_default: true",
        "tasks/reference/RELEASE-READINESS-PROTOCOL.md",
        "tasks/reference/VERIFICATION-GUARDRAIL-PROTOCOL.md",
        "tasks/reference/SESSION-COMPLETION-HANDOFF-PROTOCOL.md",
        "tasks/reference/SKILL-PLAYBOOK-PROTOCOL.md",
        ".agents/skills/release-readiness/SKILL.md",
    ]
    for term in required_terms:
        if term not in text:
            add_issue(issues, name, f"release-readiness exemplar missing required boundary term: {term}", "error")


def main() -> int:
    root = repo_root()
    issues: list[dict[str, Any]] = []

    for folder in ("tasks/reference", "adapters", "logs"):
        base = root / folder
        if not base.is_dir():
            continue
        for path in sorted(base.rglob("*.md")):
            check_markdown(path, root, issues)

    agent = root / "AGENT.md"
    if agent.is_file():
        text = agent.read_text(encoding="utf-8")
        section = text.split("## Active Memory", 1)[1].split("\n## ", 1)[0] if "## Active Memory" in text else text
        active = re.findall(r"^- `([^`]+)`", section, re.MULTILINE)
        if active[:3] != ["AGENT.md", "DECISIONS.md", "tasks/todo.md"]:
            add_issue(issues, "AGENT.md", "active-memory list does not start with the canonical three files", "error")
        extra = [item for item in active if item not in ACTIVE_MEMORY and item.endswith(".md")]
        if extra:
            add_issue(issues, "AGENT.md", f"possible extra active-memory markdown files: {', '.join(extra)}")

    check_release_readiness_curated_pack_exemplar(root, issues)

    payload = {
        "tool": "extension-check",
        "status": "pass" if not issues else "warning",
        "issues": issues,
    }
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
