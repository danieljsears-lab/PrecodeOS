#!/usr/bin/env python3
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from scripts.precode_demo import ROOT, current_bead_data, git_status_paths, write_json

bead = current_bead_data()
bead_id = bead.get("bead_id", "unknown")
changed = git_status_paths()

if bead_id == "B001":
    status = "Clear"
    top_risk = "The demo is at the first step: B001 readiness validation. The main risk is jumping to B002 before review and transition approval."
    next_move = "Run the B001 checks, review evidence, then approve transition only if accepted."
elif bead_id == "B002" and changed:
    status = "Watch"
    top_risk = "Product files have changed; verify the difficulty filter before accepting B002."
    next_move = "Run app checks and manual verification for All, Easy, Moderate, and Hard."
elif bead_id == "B002":
    status = "Clear"
    top_risk = "B002 is focused; the main risk is adding maps, persistence, or redesign."
    next_move = "Implement only the local difficulty filter."
else:
    status = "Recenter"
    top_risk = "The active bead is not one of the prepared demo beads."
    next_move = "Reload active memory and confirm the current bead."

write_json(ROOT / "logs" / "loop-health.json", {"status": status, "top_risk": top_risk, "next_move": next_move})

print(f"Build Loop Health: {status}")
print()
print("Top risk:")
print(top_risk)
print()
print("Next move:")
print(next_move)
