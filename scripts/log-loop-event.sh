#!/usr/bin/env bash
# Version: v0.1.0
# Last updated: 2026-04-26
# Owner: Precode OS
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo_root"

log_name=""
event=""
tool=""
target=""
bead=""
branch=""
status=""
notes=""

while [[ $# -gt 0 ]]; do
  case "$1" in
    --log)
      log_name="${2:-}"
      shift 2
      ;;
    --event)
      event="${2:-}"
      shift 2
      ;;
    --tool)
      tool="${2:-}"
      shift 2
      ;;
    --target)
      target="${2:-}"
      shift 2
      ;;
    --bead)
      bead="${2:-}"
      shift 2
      ;;
    --branch)
      branch="${2:-}"
      shift 2
      ;;
    --status)
      status="${2:-}"
      shift 2
      ;;
    --notes)
      notes="${2:-}"
      shift 2
      ;;
    *)
      echo "usage: bash scripts/log-loop-event.sh --log loop-runs|handoffs --event NAME [--tool TOOL] [--target TARGET] [--bead PATH] [--branch BRANCH] [--status STATUS] [--notes TEXT]"
      exit 1
      ;;
  esac
done

if [[ -z "$log_name" || -z "$event" ]]; then
  echo "usage: bash scripts/log-loop-event.sh --log loop-runs|handoffs --event NAME [--tool TOOL] [--target TARGET] [--bead PATH] [--branch BRANCH] [--status STATUS] [--notes TEXT]"
  exit 1
fi

python3 - "$repo_root" "$log_name" "$event" "$tool" "$target" "$bead" "$branch" "$status" "$notes" <<'PY'
from __future__ import annotations

from datetime import datetime, timezone
import json
from pathlib import Path
import sys

repo_root = Path(sys.argv[1])
log_name, event, tool, target, bead, branch, status, notes = sys.argv[2:]
log_path = repo_root / "logs" / f"{log_name}.jsonl"
log_path.parent.mkdir(parents=True, exist_ok=True)

entry = {
    "timestamp": datetime.now(timezone.utc).isoformat(),
    "event": event,
    "tool": tool or None,
    "target": target or None,
    "bead": bead or None,
    "branch": branch or None,
    "status": status or None,
    "notes": notes or None,
}

with log_path.open("a", encoding="utf-8") as handle:
    handle.write(json.dumps(entry, separators=(",", ":")) + "\n")
PY
