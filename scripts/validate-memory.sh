#!/usr/bin/env bash
# Version: v0.1.2
# Last updated: 2026-05-07
# Owner: Precode OS
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
json_output=false
strict=false
session_start=false
declare -a paths=()

while [[ $# -gt 0 ]]; do
  case "$1" in
    --json)
      json_output=true
      shift
      ;;
    --strict)
      strict=true
      shift
      ;;
    --session-start)
      session_start=true
      shift
      ;;
    --changed-only)
      shift
      ;;
    *)
      paths+=("$1")
      shift
      ;;
  esac
done

python3 - "$repo_root" "$json_output" "$strict" "$session_start" "${paths[@]-}" <<'PY'
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

root = Path(sys.argv[1])
json_output = sys.argv[2] == "true"
strict = sys.argv[3] == "true"
session_start = sys.argv[4] == "true"
raw_paths = sys.argv[5:]

issues: list[dict[str, object]] = []


def add(path: str, line: int, message: str) -> None:
    issues.append({"path": path, "line": line, "message": message})


def rel(path: Path) -> str:
    return path.relative_to(root).as_posix()


def read(path: str) -> str:
    target = root / path
    return target.read_text(encoding="utf-8") if target.is_file() else ""


def contract(text: str) -> dict[str, str]:
    values: dict[str, str] = {}
    for key in ("AUTHORITY", "NOT_AUTHORITY", "LOAD_WHEN", "CLASS"):
        match = re.search(rf"^>\s*{key}:\s*(.+)$", text, re.MULTILINE)
        if match:
            values[key] = match.group(1).strip()
    return values


def anchor(text: str) -> str:
    match = re.search(r"<!--\s*ANCHOR:\s*([a-z0-9-]+)\s*-->", text)
    return match.group(1) if match else ""


def frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---", 4)
    if end == -1:
        return {}
    values: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if ":" in line and not line.startswith(" "):
            key, value = line.split(":", 1)
            values[key.strip()] = value.strip().strip("'\"")
    return values


def h2s(text: str) -> set[str]:
    return {m.group(1).strip() for m in re.finditer(r"^##\s+(.+)$", text, re.MULTILINE)}


expected_anchors = {
    "AGENT.md": "agent",
    "AGENTS.md": "agents-shim",
    "GEMINI.md": "gemini-shim",
    "CLAUDE.md": "claude-shim",
    ".github/copilot-instructions.md": "copilot-shim",
    "DECISIONS.md": "decisions",
    "tasks/todo.md": "active-work",
    "README.md": "readme",
    "PRECODE-OS-README.md": "os-readme",
    "PRECODE-FILE-INVENTORY.md": "file-inventory",
    "tasks/reference/PRECODE-BMAD-GSTACK-COMPARISON.md": "precode-bmad-gstack-comparison",
    "PROJECT-CONTEXT.md": "project-context",
    "OPERATING-CONSTRAINTS.md": "operating-constraints",
    "FEATURES.md": "features",
    "ACCEPTANCE.md": "acceptance",
    "ARCHITECTURE.md": "architecture",
    "DATA-MODELS.md": "data-models",
    "API.md": "api",
    "SECURITY.md": "security",
    "CODEBASE-GUIDE.md": "codebase-guide",
    "PROGRESS.md": "progress",
    "OS-HEALTH.md": "os-health",
}

for path, expected in expected_anchors.items():
    text = read(path)
    if not text:
        add(path, 1, "required Precode document is missing")
        continue
    if anchor(text) != expected:
        add(path, 1, f"expected canonical anchor '{expected}'")
    values = contract(text)
    for key in ("AUTHORITY", "NOT_AUTHORITY", "LOAD_WHEN", "CLASS"):
        if key not in values:
            add(path, 1, f"missing authority contract field: {key}")

agent = read("AGENT.md")
active_claims = re.findall(r"^- `([^`]+)`", agent, re.MULTILINE)
expected_active = ["AGENT.md", "DECISIONS.md", "tasks/todo.md"]
if active_claims[:3] != expected_active:
    add("AGENT.md", 1, "active memory must begin with AGENT.md, DECISIONS.md, and tasks/todo.md")
if "PROJECT-CONTEXT.md" in active_claims or "PRECODE-OS-README.md" in active_claims:
    add("AGENT.md", 1, "reference docs must not be promoted into active memory")

todo_text = read("tasks/todo.md")
todo_fm = frontmatter(todo_text)
for key in ("current_bead", "current_state", "build_lane", "active_feature_window", "primary_authority"):
    if key not in todo_fm:
        add("tasks/todo.md", 1, f"todo frontmatter missing required key: {key}")

bead_required = {
    "State",
    "Primary Authority",
    "Depends On",
    "Parent PRD",
    "Requirement IDs",
    "Objective",
    "Done When",
    "Files In Play",
    "Checks",
    "Verification Type",
    "Stop If",
    "Closeout Evidence",
    "Handback",
}
closeout_markers = [
    "Checks run",
    "Result",
    "Manual verification",
    "Files changed",
    "Next bead",
    "Review decision",
    "Drift observed",
    "Lesson to promote",
    "Follow-up bead needed",
    "Evidence source",
]

in_progress: list[str] = []
for bead_path in sorted((root / "tasks" / "beads").glob("*.md")):
    if bead_path.name == "BEAD-SCHEMA.md":
        continue
    path = rel(bead_path)
    text = bead_path.read_text(encoding="utf-8")
    fm = frontmatter(text)
    status = (fm.get("status") or "").strip()
    if status == "in_progress":
        in_progress.append(path)
    sections = h2s(text)
    for heading in sorted(bead_required - sections):
        add(path, 1, f"bead missing required section: {heading}")
    for marker in closeout_markers:
        if marker.lower() not in text.lower():
            add(path, 1, f"bead Closeout Evidence missing marker: {marker}")

if len(in_progress) != 1:
    add("tasks/beads/BEAD-SCHEMA.md", 1, f"exactly one bead must be in_progress; found {in_progress or 'none'}")
elif todo_fm.get("current_bead") != in_progress[0]:
    add("tasks/todo.md", 1, f"current_bead must match in_progress bead {in_progress[0]}")

if strict:
    for path in ("PROGRESS.md", "OS-HEALTH.md"):
        text = read(path)
        if "> CLASS: generated" not in text:
            add(path, 1, "generated reports must use CLASS: generated")
        if "Do not use this file" not in text:
            add(path, 1, "generated reports must demote themselves from active memory")

if json_output:
    print(json.dumps({"ok": not issues, "issues": issues}, indent=2))
else:
    if issues:
        print("DOC SYSTEM VALIDATION FAILED")
        for issue in issues:
            print(f"{issue['path']}:{issue['line']}: {issue['message']}")
    else:
        print("DOC SYSTEM VALIDATION PASSED")
    print(f"\n{len(issues)} error(s), 0 warning(s)")

raise SystemExit(1 if issues else 0)
PY
