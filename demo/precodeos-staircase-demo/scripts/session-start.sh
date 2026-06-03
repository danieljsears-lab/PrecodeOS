#!/usr/bin/env bash
set -euo pipefail

bash scripts/validate-memory.sh

python3 - <<'PY'
from scripts.precode_demo import current_bead_data, current_bead_text, section, todo_data

todo = todo_data()
bead = current_bead_data()
text = current_bead_text()

print()
print("PrecodeOS Demo Session Start")
print("Active memory: AGENT.md, DECISIONS.md, tasks/todo.md")
print()
print("Context Pack:")
print(f"Current bead file: {todo.get('current_bead')}")
print(f"State: {todo.get('current_state')}")
print(f"Primary authority: {todo.get('primary_authority')}")
print()
print("Current Bead:")
print(f"- ID: `{bead.get('bead_id')}`")
print(f"- Status: `{bead.get('status')}`")
print(f"- Kind: `{bead.get('bead_kind')}`")
print()
for title in ["Done When", "Files In Play", "Checks", "Stop If"]:
    display = "Stop Conditions" if title == "Stop If" else title
    print(f"{display}:")
    for item in section(text, title):
        print(f"- {item}")
    print()
PY

python3 scripts/next-step.py
