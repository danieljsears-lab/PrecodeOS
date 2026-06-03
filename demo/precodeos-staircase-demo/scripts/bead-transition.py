#!/usr/bin/env python3
import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from scripts.precode_demo import ROOT, current_bead_data, current_bead_path, replace_status, set_active_bead

parser = argparse.ArgumentParser()
parser.add_argument("--approve", action="store_true")
args = parser.parse_args()

bead_id = current_bead_data().get("bead_id")

if bead_id == "B001":
    next_bead = "tasks/beads/B002-add-difficulty-filter.md"
elif bead_id == "B002":
    next_bead = "tasks/beads/B003-mark-staircase-visited.md"
else:
    next_bead = "not recorded"

if not args.approve:
    print(f"Current bead: {current_bead_path().relative_to(ROOT)}")
    print(f"Proposed next bead: {next_bead}")
    print("Transition approval required: python3 scripts/bead-transition.py --approve")
    raise SystemExit(0)

if bead_id != "B001":
    print("This demo only approves transition from B001 to B002.")
    print(f"Current bead is {bead_id}; leaving state unchanged.")
    raise SystemExit(1)

replace_status(current_bead_path(), "accepted", "active-task")
replace_status(ROOT / "tasks/beads/B002-add-difficulty-filter.md", "in_progress", "active-task")
set_active_bead("tasks/beads/B002-add-difficulty-filter.md")

print("Transition approved.")
print("Active bead is now: tasks/beads/B002-add-difficulty-filter.md")
