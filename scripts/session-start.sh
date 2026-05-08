#!/usr/bin/env bash
# Version: v0.1.1
# Last updated: 2026-05-08
# Owner: Precode OS
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo_root"

bash scripts/validate-memory.sh --session-start

branch="$(git rev-parse --abbrev-ref HEAD 2>/dev/null || echo "unknown")"
state_json="$(python3 scripts/execution-state.py "$repo_root")"

current_bead="$(python3 - "$state_json" <<'PY'
import json
import sys

state = json.loads(sys.argv[1])
print(state.get("current_bead") or "")
PY
)"

python3 - "$branch" "$state_json" <<'PY'
import json
import sys

branch = sys.argv[1]
state = json.loads(sys.argv[2])
todo_sections = state["todo_sections"]
bead_sections = state["bead_sections"]
bead_bullets = state["bead_bullets"]

print("Precode OS Session Start")
print(f"Branch: {branch}")
print("Active memory: AGENT.md, DECISIONS.md, tasks/todo.md")
print("\nContext Pack:")
print(f"Current bead file: {state.get('current_bead') or '(missing)'}")
for heading in ("Current Bead", "Done When", "Files In Play", "Explicit Out-of-Scope", "Open Questions"):
    print(f"\n{heading}:")
    body = todo_sections.get(heading, "").strip() or "- (missing)"
    print(body)
print("\nBead State:")
print(bead_sections.get("State", "").strip() or "- (missing)")
print("\nPrimary Authority:")
print(bead_sections.get("Primary Authority", "").strip() or "- (missing)")
print("\nBead Checks:")
print(bead_sections.get("Checks", "").strip() or "- (missing)")
print("\nStop Conditions:")
print(bead_sections.get("Stop If", "").strip() or "- (missing)")
try:
    from pathlib import Path
    import sys

    sys.path.insert(0, "scripts")
    from os_compiler import compile_state

    goal_frame = (compile_state(Path(".")).get("goal_frame") or {})
    goal_details = goal_frame.get("details") or {}
    current_goal = goal_details.get("current") or {}
except Exception:
    current_goal = {}
print("\nGoal Frame:")
if current_goal:
    print(f"- Status: {current_goal.get('status', 'missing')}")
    print(f"- Owner file: {current_goal.get('path', 'not recorded')}")
    print(f"- Horizon: {current_goal.get('horizon', 'not recorded')}")
    print(f"- Workflow guidance: {current_goal.get('workflow_guidance', 'not recorded')}")
    print(f"- Goal: {current_goal.get('goal', 'not recorded')}")
    print("- Warning: Goal Frames are advisory only; they do not approve work or replace active memory.")
else:
    print("- No current Goal Frame.")
print("\nGenerated Report Warning:")
print("- Generated reports are evidence only. Do not use them as active memory, task plans, or implementation instructions.")
PY

bash scripts/log-loop-event.sh --log loop-runs --event session-start --bead "$current_bead" --branch "$branch" --status pass
python3 scripts/os-health.py
