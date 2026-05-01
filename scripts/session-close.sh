#!/usr/bin/env bash
# Version: v0.1.0
# Last updated: 2026-04-26
# Owner: Precode OS
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo_root"

python3 scripts/update-bead-closeout.py
python3 scripts/os-health.py
bash scripts/record-check.sh -- bash scripts/validate-memory.sh
python3 scripts/update-bead-closeout.py
python3 scripts/os-health.py
python3 scripts/bead-transition.py
python3 - <<'PY'
import sys
from pathlib import Path

sys.path.insert(0, str(Path("scripts").resolve()))

from os_compiler import compile_state, repo_root

state = compile_state(repo_root())
completion = state.get("completion_handoff", {})
details = completion.get("details", {})
warnings = completion.get("warnings") or []

print("Completion And Handoff Readiness")
print(f"- Closeout status: {details.get('closeout_status', 'unknown')}")
print(f"- Promotion status: {details.get('promotion_status', 'unknown')}")
print(f"- Manual verification: {details.get('manual_verification', 'unknown')}")
print(f"- Review decision: {details.get('review_decision', 'unknown')}")
print(f"- Next safe action: {details.get('next_safe_action', 'unknown')}")
blockers = details.get("promotion_blockers") or []
if blockers:
    print("- Promotion blockers:")
    for blocker in blockers[:8]:
        print(f"  - {blocker}")
if warnings:
    print("- Completion/handoff warnings:")
    for warning in warnings[:8]:
        print(f"  - {warning}")
PY
branch="$(git rev-parse --abbrev-ref HEAD 2>/dev/null || echo "unknown")"
state_json="$(python3 scripts/execution-state.py "$repo_root")"
current_bead="$(python3 - "$state_json" <<'PY'
import json
import sys

state = json.loads(sys.argv[1])
print(state.get("current_bead") or "")
PY
)"

cat <<'EOF'
Precode OS Session Close
- tasks/todo.md should already be rewritten as the current execution contract
- the active bead should already reflect the current stop state
- the active bead should already include Closeout Evidence generated from recorded command results
- OS-HEALTH.md and logs/os-health.json have been regenerated
- shared memory validation passed
- ready for branch review, handoff, or stop
EOF

bash scripts/log-loop-event.sh --log loop-runs --event session-close --bead "$current_bead" --branch "$branch" --status pass
python3 scripts/update-learning-diary.py --append
python3 scripts/os-health.py
