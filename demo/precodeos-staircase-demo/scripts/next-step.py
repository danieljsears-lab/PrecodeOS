#!/usr/bin/env python3
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from scripts.precode_demo import ROOT, current_bead_data, todo_data, write_json

todo = todo_data()
bead = current_bead_data()
bead_id = bead.get("bead_id", "unknown")

if bead_id == "B001":
    decision = {
        "user_decision": "ask for proof",
        "what_to_do_now": "Complete the first readiness bead, review evidence, then approve transition only if accepted.",
        "recommended_action": "Run the B001 readiness checks through record-check.sh.",
        "next_bead": "tasks/beads/B002-add-difficulty-filter.md",
        "needs_transition_approval": True,
        "stop_if": "Stop if Claude edits product app files, cannot name B001, or treats this generated hint as approval.",
    }
elif bead_id == "B002":
    decision = {
        "user_decision": "continue",
        "what_to_do_now": "Implement only the B002 local difficulty filter and ask for proof before review.",
        "recommended_action": "Keep work inside index.html and src/**, then run app checks.",
        "next_bead": "tasks/beads/B003-mark-staircase-visited.md",
        "needs_transition_approval": False,
        "stop_if": "Stop if maps, geolocation, APIs, persistence, accounts, or redesign appear.",
    }
else:
    decision = {
        "user_decision": "review",
        "what_to_do_now": "Review the current bead before continuing.",
        "recommended_action": "Run loop health and inspect the active bead.",
        "next_bead": "not recorded",
        "needs_transition_approval": False,
        "stop_if": "Stop if the active task is unclear.",
    }

write_json(ROOT / "logs" / "next-step.json", decision)

print()
print(f"Router Decision: {decision['user_decision'].title()}")
print(f"- What to do now: {decision['what_to_do_now']}")
print(f"- Active bead: `{todo.get('current_bead')}`")
print(f"- State: `{todo.get('current_state')}`")
print(f"- Recommended action: {decision['recommended_action']}")
print(f"- Next bead: `{decision['next_bead']}`")
print(f"- Needs transition approval: {decision['needs_transition_approval']}")
print(f"- Stop if: {decision['stop_if']}")
print()
print("Generated Report Warning:")
print("- This router output is guidance only. It does not approve work or activate beads.")
