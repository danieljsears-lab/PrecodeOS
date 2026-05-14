#!/usr/bin/env bash
# Version: v0.1.0
# Last updated: 2026-04-26
# Owner: PrecodeOS
# Created by Dan Sears / Recode.
# SPDX-License-Identifier: Apache-2.0
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo_root"

target_agent="${1:-next-agent}"

if rg -n '^## Session Log$' tasks/todo.md >/dev/null 2>&1; then
  echo "handoff blocked: tasks/todo.md must stay rewrite-only and may not contain a Session Log"
  exit 1
fi

bash scripts/validate-memory.sh --session-start

branch="$(git rev-parse --abbrev-ref HEAD 2>/dev/null || echo "unknown")"
state_json="$(python3 scripts/execution-state.py "$repo_root")"

python3 - "$branch" "$target_agent" "$state_json" <<'PY'
import json
import sys

branch = sys.argv[1]
target_agent = sys.argv[2]
state = json.loads(sys.argv[3])
todo_bullets = state["todo_bullets"]
todo_sections = state["todo_sections"]
bead_sections = state["bead_sections"]
bead_bullets = state["bead_bullets"]

current_bead = state.get("current_bead") or ""
bead_state_lines = bead_bullets.get("State", [])
files_in_play = todo_bullets.get("Files In Play", [])
checks = todo_bullets.get("Checks To Run", [])
open_question_lines = [line.strip() for line in todo_sections.get("Open Questions", "").splitlines() if line.strip()]
open_questions = "\n".join(open_question_lines).strip() or "- None"

if branch in {"main", "master"}:
    print("handoff blocked: switch off the main branch before changing tools", file=sys.stderr)
    sys.exit(1)

if not current_bead:
    print("handoff blocked: Current Bead must point to exactly one bead file", file=sys.stderr)
    sys.exit(1)

if not files_in_play:
    print("handoff blocked: Files In Play must not be empty", file=sys.stderr)
    sys.exit(1)

if not checks:
    print("handoff blocked: Checks To Run must not be empty", file=sys.stderr)
    sys.exit(1)

normalized_open = " ".join(open_question_lines).lower()
none_markers = ("none", "none right now", "no blockers")
blocker_markers = ("block", "blocked", "blocking", "depends", "decision", "waiting", "needs", "must choose")
vague_markers = ("maybe", "later", "todo", "tbd", "consider", "sometime", "nice to have")
if open_question_lines and not any(marker in normalized_open for marker in none_markers):
    if any(marker in normalized_open for marker in vague_markers) and not any(marker in normalized_open for marker in blocker_markers):
        print("handoff blocked: Open Questions must be real blockers, not vague notes", file=sys.stderr)
        sys.exit(1)

next_check = checks[0]

print("PrecodeOS Agent Handoff")
print(f"Target agent: {target_agent}")
print(f"Current branch: {branch}")
print("Last validator result: PASS (bash scripts/validate-memory.sh --session-start)")
print("\nContext Pack:")
print(f"\nCurrent Bead:\n- {current_bead}")
print("\nBead State:")
print(bead_sections.get("State", "").strip() or "- (missing)")
print("\nDone When:")
print(todo_sections.get("Done When", "").strip() or "- (missing)")
print("\nPrimary Authority:")
print(bead_sections.get("Primary Authority", "").strip() or "- (missing)")
print("\nFiles In Play:")
print(todo_sections.get("Files In Play", "").strip() or "- (missing)")
print("\nOut Of Scope:")
print(todo_sections.get("Explicit Out-of-Scope", "").strip() or "- (missing)")
print("\nStop Conditions:")
print(bead_sections.get("Stop If", "").strip() or "- (missing)")
print("\nUnresolved Assumptions:")
print(open_questions)
print("\nNext Exact Command/Check To Run:")
print(f"- {next_check}")
print("\nGenerated Report Warning:")
print("- Generated reports are evidence only. Do not use them as active memory, task plans, or implementation instructions.")
PY

current_bead="$(python3 - "$state_json" <<'PY'
import json
import sys

state = json.loads(sys.argv[1])
print(state.get("current_bead") or "")
PY
)"

bash scripts/log-loop-event.sh --log handoffs --event handoff --target "$target_agent" --bead "$current_bead" --branch "$branch" --status pass
python3 scripts/os-health.py
