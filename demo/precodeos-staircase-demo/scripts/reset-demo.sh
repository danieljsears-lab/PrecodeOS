#!/usr/bin/env bash
set -euo pipefail

python3 - <<'PY'
from scripts.precode_demo import ROOT, replace_status, set_active_bead

replace_status(ROOT / "tasks/beads/B001-validate-precode-readiness.md", "in_progress", "active-task")
replace_status(ROOT / "tasks/beads/B002-add-difficulty-filter.md", "proposed", "candidate-task")
replace_status(ROOT / "tasks/beads/B003-mark-staircase-visited.md", "proposed", "candidate-task")
replace_status(ROOT / "tasks/beads/B004-sort-by-climb-time.md", "proposed", "candidate-task")
replace_status(ROOT / "tasks/beads/B005-add-neighborhood-filter.md", "proposed", "candidate-task")
replace_status(ROOT / "tasks/beads/B006-add-staircase-detail-view.md", "proposed", "candidate-task")
replace_status(ROOT / "tasks/beads/B007-share-staircase-route.md", "proposed", "candidate-task")
set_active_bead("tasks/beads/B001-validate-precode-readiness.md")
PY

echo "Demo reset to first step: B001 readiness validation is active; B002 is proposed."
