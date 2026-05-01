#!/usr/bin/env bash
# Version: v0.1.0
# Last updated: 2026-04-26
# Owner: Precode OS
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo_root"

bash scripts/validate-memory.sh

branch="$(git rev-parse --abbrev-ref HEAD 2>/dev/null || echo "unknown")"
state_json="$(python3 scripts/execution-state.py "$repo_root")"
current_bead="$(python3 - "$state_json" <<'PY'
import json
import sys

state = json.loads(sys.argv[1])
print(state.get("current_bead") or "")
PY
)"

echo "Precode OS Checkpoint"
echo "Branch: $branch"
echo "Current bead: ${current_bead:-unknown}"
echo
echo "Modified files:"
git status --short || true
echo

python3 - "$state_json" <<'PY'
import json
import sys

state = json.loads(sys.argv[1])
todo_sections = state["todo_sections"]
bead_sections = state["bead_sections"]

for heading in ("Current Bead", "Files In Play", "Checks To Run", "Next Up"):
    print(f"{heading}:")
    print(todo_sections.get(heading, "").strip() or "- (missing)")
    print()
print("Bead State:")
print(bead_sections.get("State", "").strip() or "- (missing)")
print()
print("Bead Handback:")
print(bead_sections.get("Handback", "").strip() or "- (missing)")
PY

bash scripts/log-loop-event.sh --log loop-runs --event checkpoint --bead "$current_bead" --branch "$branch" --status pass
python3 scripts/os-health.py
