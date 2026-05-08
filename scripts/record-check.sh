#!/usr/bin/env bash
# Version: v0.1.0
# Last updated: 2026-04-26
# Owner: Precode OS
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo_root"

cwd="$repo_root"
label=""
declare -a command=()

usage() {
  cat <<'EOF'
usage:
  bash scripts/record-check.sh [--cwd DIR] [--label LABEL] -- COMMAND [ARGS...]

Runs a verification command, records exit code/output metadata in
logs/check-results.jsonl, updates the active bead Closeout Evidence, and exits
with the wrapped command's exit code.
EOF
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --cwd)
      cwd="$repo_root/${2:-}"
      shift 2
      ;;
    --label)
      label="${2:-}"
      shift 2
      ;;
    --)
      shift
      command=("$@")
      break
      ;;
    --help|-h)
      usage
      exit 0
      ;;
    *)
      command+=("$1")
      shift
      ;;
  esac
done

if [[ ${#command[@]} -eq 0 ]]; then
  usage
  exit 1
fi

if [[ ! -d "$cwd" ]]; then
  echo "record-check: cwd does not exist: $cwd" >&2
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
branch="$(git rev-parse --abbrev-ref HEAD 2>/dev/null || echo "unknown")"
timestamp="$(date -u +"%Y%m%dT%H%M%SZ")"
command_text="$(printf '%q ' "${command[@]}")"
command_text="${command_text% }"
label="${label:-$command_text}"
safe_label="$(printf '%s' "$label" | tr -cs 'A-Za-z0-9._-' '-' | sed 's/^-//; s/-$//')"
safe_label="${safe_label:-check}"
output_dir="$repo_root/logs/check-output"
mkdir -p "$output_dir"
output_path="$output_dir/${timestamp}-${safe_label}.log"
rel_output_path="${output_path#"$repo_root/"}"
rel_cwd="${cwd#"$repo_root/"}"
if [[ "$cwd" == "$repo_root" ]]; then
  rel_cwd="."
fi
start_epoch="$(date +%s)"

echo "record-check: running $command_text"
echo "record-check: cwd $rel_cwd"

set +e
(
  cd "$cwd"
  "${command[@]}"
) >"$output_path" 2>&1
exit_code=$?
set -e

end_epoch="$(date +%s)"
duration_seconds=$((end_epoch - start_epoch))
status="pass"
if [[ "$exit_code" -ne 0 ]]; then
  status="fail"
fi

cat "$output_path"

python3 - "$repo_root" "$timestamp" "$current_bead" "$branch" "$status" "$exit_code" "$duration_seconds" "$command_text" "$rel_cwd" "$rel_output_path" <<'PY'
from __future__ import annotations

from datetime import datetime, timezone
import json
from pathlib import Path
import sys

repo_root = Path(sys.argv[1])
timestamp, bead, branch, status, exit_code, duration, command, cwd, output_path = sys.argv[2:]
log_path = repo_root / "logs" / "check-results.jsonl"
log_path.parent.mkdir(parents=True, exist_ok=True)

entry = {
    "timestamp": datetime.now(timezone.utc).isoformat(),
    "run_id": timestamp,
    "bead": bead or None,
    "branch": branch,
    "status": status,
    "exit_code": int(exit_code),
    "duration_seconds": int(duration),
    "command": command,
    "cwd": cwd or ".",
    "output": output_path,
}

with log_path.open("a", encoding="utf-8") as handle:
    handle.write(json.dumps(entry, separators=(",", ":")) + "\n")
PY

python3 scripts/update-bead-closeout.py || true
python3 scripts/os-health.py || echo "record-check: warning: os-health refresh failed" >&2

echo "record-check: $status exit=$exit_code output=$rel_output_path"
exit "$exit_code"
