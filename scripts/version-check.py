#!/usr/bin/env python3
# Version: v0.1.0
# Last updated: 2026-04-26
# Owner: Precode OS
from __future__ import annotations

import json
from pathlib import Path
import re
from typing import Any

from os_compiler import repo_root


MARKDOWN_EXCLUDES = {
    "OS-HEALTH.md",
    "PROGRESS.md",
    "logs/handoff-packet.md",
    "logs/learning-diary.md",
    "logs/scheduled-audit.md",
}
SCRIPT_VERSION_RE = re.compile(r"^# Version: v\d+\.\d+\.\d+$", re.MULTILINE)
SCRIPT_UPDATED_RE = re.compile(r"^# Last updated: \d{4}-\d{2}-\d{2}$", re.MULTILINE)
SCRIPT_OWNER_RE = re.compile(r"^# Owner: Precode OS$", re.MULTILINE)
DOC_VERSION_RE = re.compile(r"^Document version: v\d+\.\d+\.\d+$", re.MULTILINE)
DOC_UPDATED_RE = re.compile(r"^Last updated: \d{4}-\d{2}-\d{2}$", re.MULTILINE)
DOC_CREATOR_RE = re.compile(r"^Creator: Dan Sears / Recode$", re.MULTILINE)


def rel(path: Path, root: Path) -> str:
    return path.relative_to(root).as_posix()


def add(issues: list[dict[str, Any]], path: str, message: str) -> None:
    issues.append({"path": path, "severity": "warning", "message": message})


def markdown_files(root: Path) -> list[Path]:
    candidates: list[Path] = []
    for path in root.rglob("*.md"):
        name = rel(path, root)
        if ".git/" in name or name in MARKDOWN_EXCLUDES:
            continue
        if name.startswith("logs/") and name != "logs/README.md":
            continue
        candidates.append(path)
    return sorted(candidates)


def script_files(root: Path) -> list[Path]:
    return sorted((root / "scripts").glob("*.py")) + sorted((root / "scripts").glob("*.sh"))


def workflow_files(root: Path) -> list[Path]:
    base = root / ".github" / "workflows"
    if not base.is_dir():
        return []
    return sorted([*base.glob("*.yml"), *base.glob("*.yaml")])


def check_doc(path: Path, root: Path, issues: list[dict[str, Any]]) -> None:
    text = path.read_text(encoding="utf-8")
    name = rel(path, root)
    if not DOC_CREATOR_RE.search(text):
        add(issues, name, "missing Creator metadata")
    if not DOC_VERSION_RE.search(text):
        add(issues, name, "missing or malformed Document version metadata")
    if not DOC_UPDATED_RE.search(text):
        add(issues, name, "missing or malformed Last updated metadata")


def check_script(path: Path, root: Path, issues: list[dict[str, Any]]) -> None:
    text = path.read_text(encoding="utf-8")
    name = rel(path, root)
    if not SCRIPT_VERSION_RE.search(text):
        add(issues, name, "missing or malformed script Version header")
    if not SCRIPT_UPDATED_RE.search(text):
        add(issues, name, "missing or malformed script Last updated header")
    if not SCRIPT_OWNER_RE.search(text):
        add(issues, name, "missing script Owner header")


def main() -> int:
    root = repo_root()
    issues: list[dict[str, Any]] = []

    for path in markdown_files(root):
        check_doc(path, root, issues)
    for path in script_files(root):
        check_script(path, root, issues)
    for path in workflow_files(root):
        check_script(path, root, issues)

    payload = {
        "tool": "version-check",
        "status": "pass" if not issues else "warning",
        "checked": {
            "markdown": len(markdown_files(root)),
            "scripts": len(script_files(root)),
            "workflows": len(workflow_files(root)),
        },
        "issues": issues,
    }
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
