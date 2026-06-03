#!/usr/bin/env bash
set -euo pipefail

for file in AGENT.md DECISIONS.md tasks/todo.md; do
  if [[ ! -f "$file" ]]; then
    echo "Missing active memory file: $file"
    exit 1
  fi
done

current_bead="$(python3 -c 'from scripts.precode_demo import todo_data; print(todo_data().get("current_bead", ""))')"
current_state="$(python3 -c 'from scripts.precode_demo import todo_data; print(todo_data().get("current_state", ""))')"

if [[ -z "$current_bead" || ! -f "$current_bead" ]]; then
  echo "Invalid current_bead in tasks/todo.md: $current_bead"
  exit 1
fi

if [[ "$current_state" != "in_progress" ]]; then
  echo "Expected current_state to be in_progress, found: $current_state"
  exit 1
fi

active_count="$(python3 - <<'PY'
from pathlib import Path
count = 0
for path in Path("tasks/beads").glob("*.md"):
    if "status: in_progress" in path.read_text(encoding="utf-8"):
        count += 1
print(count)
PY
)"

if [[ "$active_count" != "1" ]]; then
  echo "Expected exactly one in-progress bead, found: $active_count"
  exit 1
fi

echo "DOC SYSTEM VALIDATION PASSED"
echo "Active memory: AGENT.md, DECISIONS.md, tasks/todo.md"
echo "Current bead: $current_bead"
