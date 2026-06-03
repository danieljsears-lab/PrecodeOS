#!/usr/bin/env bash
set -euo pipefail

if [[ "${1:-}" != "--" ]]; then
  echo "Usage: bash scripts/record-check.sh -- <command>"
  exit 2
fi
shift

mkdir -p logs/check-output
timestamp="$(date -u +"%Y%m%dT%H%M%SZ")"
safe_command="$(printf "%s-" "$@" | tr -cd '[:alnum:]._-' | sed 's/-$//')"
log_path="logs/check-output/${timestamp}-${safe_command}.log"

set +e
"$@" >"$log_path" 2>&1
status=$?
set -e

if [[ "$status" -eq 0 ]]; then
  result="pass"
else
  result="fail"
fi

printf '{"timestamp":"%s","status":"%s","exit_code":%s,"command":"%s","log":"%s"}\n' "$timestamp" "$result" "$status" "$*" "$log_path" >> logs/check-results.jsonl

cat "$log_path"
echo
echo "Recorded check: $result (exit $status)"
echo "Log: $log_path"
exit "$status"
