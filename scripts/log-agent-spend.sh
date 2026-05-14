#!/usr/bin/env bash
# Version: v0.1.0
# Last updated: 2026-04-26
# Owner: PrecodeOS
# Created by Dan Sears / Recode.
# SPDX-License-Identifier: Apache-2.0
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo_root"

tool=""
task=""
tokens=""
input_tokens=""
output_tokens=""
cost=""
model=""
session_id=""
source="manual"
confidence="unknown"
notes=""

while [[ $# -gt 0 ]]; do
  case "$1" in
    --tool)
      tool="${2:-}"
      shift 2
      ;;
    --task)
      task="${2:-}"
      shift 2
      ;;
    --tokens)
      tokens="${2:-}"
      shift 2
      ;;
    --input-tokens)
      input_tokens="${2:-}"
      shift 2
      ;;
    --output-tokens)
      output_tokens="${2:-}"
      shift 2
      ;;
    --cost)
      cost="${2:-}"
      shift 2
      ;;
    --model)
      model="${2:-}"
      shift 2
      ;;
    --session-id|--run-id)
      session_id="${2:-}"
      shift 2
      ;;
    --source)
      source="${2:-}"
      shift 2
      ;;
    --confidence)
      confidence="${2:-}"
      shift 2
      ;;
    --notes)
      notes="${2:-}"
      shift 2
      ;;
    *)
      echo "usage: bash scripts/log-agent-spend.sh --tool TOOL --task TASK [--tokens N] [--input-tokens N] [--output-tokens N] [--cost USD] [--model MODEL] [--session-id ID] [--source SOURCE] [--confidence exact|estimated|unknown] [--notes TEXT]"
      exit 1
      ;;
  esac
done

if [[ -z "$tool" || -z "$task" ]]; then
  echo "usage: bash scripts/log-agent-spend.sh --tool TOOL --task TASK [--tokens N] [--input-tokens N] [--output-tokens N] [--cost USD] [--model MODEL] [--session-id ID] [--source SOURCE] [--confidence exact|estimated|unknown] [--notes TEXT]"
  exit 1
fi

branch="$(git rev-parse --abbrev-ref HEAD 2>/dev/null || echo "unknown")"

python3 - "$repo_root" "$tool" "$task" "$tokens" "$input_tokens" "$output_tokens" "$cost" "$model" "$session_id" "$source" "$confidence" "$notes" "$branch" <<'PY'
from __future__ import annotations

from datetime import datetime, timezone
import json
from pathlib import Path
import sys

repo_root = Path(sys.argv[1])
tool, task, tokens, input_tokens, output_tokens, cost, model, session_id, source, confidence, notes, branch = sys.argv[2:]
log_path = repo_root / "logs" / "agent-spend.jsonl"
log_path.parent.mkdir(parents=True, exist_ok=True)

def parse_int(value: str) -> int | None:
    return int(value) if value else None

total_tokens = parse_int(tokens)
input_value = parse_int(input_tokens)
output_value = parse_int(output_tokens)
if total_tokens is None and input_value is not None and output_value is not None:
    total_tokens = input_value + output_value

entry = {
    "timestamp": datetime.now(timezone.utc).isoformat(),
    "tool": tool,
    "task": task,
    "branch": branch,
    "input_tokens": input_value,
    "output_tokens": output_value,
    "total_tokens": total_tokens,
    "tokens": total_tokens,
    "cost_usd": float(cost) if cost else None,
    "model": model or None,
    "session_id": session_id or None,
    "telemetry_source": source or "manual",
    "confidence": confidence if confidence in {"exact", "estimated", "unknown"} else "unknown",
    "notes": notes or None,
}

with log_path.open("a", encoding="utf-8") as handle:
    handle.write(json.dumps(entry, separators=(",", ":")) + "\n")

print(f"logged spend entry to {log_path.relative_to(repo_root).as_posix()}")
PY
