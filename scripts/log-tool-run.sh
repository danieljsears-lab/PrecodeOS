#!/usr/bin/env bash
# Version: v0.1.0
# Last updated: 2026-04-26
# Owner: Precode OS
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo_root"

tool=""
tool_class=""
status=""
command_summary=""
task=""
failure_category=""
cwd="."
output_ref=""
approval_note=""
side_effects=""
dry_run=false

usage() {
  cat <<'EOF'
usage:
  bash scripts/log-tool-run.sh --tool TOOL --class CLASS --status pass|fail|blocked --command SUMMARY [options]

options:
  --task BEAD_OR_TASK
  --failure-category CATEGORY
  --cwd DIR
  --output-ref PATH_OR_NOTE
  --approval-note NOTE
  --side-effects NOTE
  --dry-run

Records important non-check tool actions in logs/tool-runs.jsonl.
This is evidence of tool use, not passing verification.
EOF
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --tool)
      tool="${2:-}"
      shift 2
      ;;
    --class)
      tool_class="${2:-}"
      shift 2
      ;;
    --status)
      status="${2:-}"
      shift 2
      ;;
    --command)
      command_summary="${2:-}"
      shift 2
      ;;
    --task)
      task="${2:-}"
      shift 2
      ;;
    --failure-category)
      failure_category="${2:-}"
      shift 2
      ;;
    --cwd)
      cwd="${2:-}"
      shift 2
      ;;
    --output-ref)
      output_ref="${2:-}"
      shift 2
      ;;
    --approval-note)
      approval_note="${2:-}"
      shift 2
      ;;
    --side-effects)
      side_effects="${2:-}"
      shift 2
      ;;
    --dry-run)
      dry_run=true
      shift
      ;;
    --help|-h)
      usage
      exit 0
      ;;
    *)
      echo "log-tool-run: unknown argument $1" >&2
      usage
      exit 2
      ;;
  esac
done

if [[ -z "$tool" || -z "$tool_class" || -z "$status" || -z "$command_summary" ]]; then
  usage
  exit 1
fi

state_json="$(python3 scripts/execution-state.py "$repo_root")"
current_bead="$(python3 - "$state_json" <<'PY'
import json
import sys

state = json.loads(sys.argv[1])
print(state.get("current_bead") or "")
PY
)"
task="${task:-$current_bead}"
branch="$(git rev-parse --abbrev-ref HEAD 2>/dev/null || echo "unknown")"

python3 - "$repo_root" "$tool" "$tool_class" "$status" "$command_summary" "$task" "$failure_category" "$cwd" "$output_ref" "$approval_note" "$side_effects" "$branch" "$dry_run" <<'PY'
from __future__ import annotations

from datetime import datetime, timezone
import json
from pathlib import Path
import sys

repo_root = Path(sys.argv[1])
tool, tool_class, status, command, task, failure_category, cwd, output_ref, approval_note, side_effects, branch, dry_run = sys.argv[2:]
entry = {
    "timestamp": datetime.now(timezone.utc).isoformat(),
    "tool": tool,
    "class": tool_class,
    "status": status,
    "command": command,
    "task": task or None,
    "branch": branch,
    "cwd": cwd or ".",
    "failure_category": failure_category or None,
    "output_ref": output_ref or None,
    "approval_note": approval_note or None,
    "side_effects": side_effects or None,
}

if dry_run == "true":
    print(json.dumps({"dry_run": True, "entry": entry}, indent=2, sort_keys=True))
    raise SystemExit(0)

log_path = repo_root / "logs" / "tool-runs.jsonl"
log_path.parent.mkdir(parents=True, exist_ok=True)
with log_path.open("a", encoding="utf-8") as handle:
    handle.write(json.dumps(entry, separators=(",", ":")) + "\n")
print(f"log-tool-run: wrote {log_path.relative_to(repo_root).as_posix()}")
PY
