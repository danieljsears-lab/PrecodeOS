#!/usr/bin/env bash
# Version: v0.1.1
# Last updated: 2026-05-19
# Owner: PrecodeOS
# Created by Dan Sears / Recode.
# SPDX-License-Identifier: Apache-2.0
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

echo "PrecodeOS Checkpoint"
echo "Branch: $branch"
echo "Current bead: ${current_bead:-unknown}"
loop_health_json="$(python3 scripts/loop-health.py --json)"
python3 - "$loop_health_json" <<'PY'
import json
import sys

payload = json.loads(sys.argv[1])
print(f"Build Loop Health: {payload.get('status', 'Watch')} - {payload.get('next_move', 'Run python3 scripts/loop-health.py --verbose for details.')}")
PY
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
