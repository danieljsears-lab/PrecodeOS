#!/usr/bin/env bash
set -euo pipefail

mkdir -p logs
timestamp="$(date -u +"%Y-%m-%dT%H:%M:%SZ")"
current_bead="$(python3 -c 'from scripts.precode_demo import current_bead_path, ROOT; print(current_bead_path().relative_to(ROOT))')"

{
  echo "# Session Close"
  echo
  echo "- Timestamp: $timestamp"
  echo "- Current bead: $current_bead"
  echo "- Loop health:"
  python3 scripts/loop-health.py | sed 's/^/  /'
  echo
  echo "- Recent checks:"
  if [[ -f logs/check-results.jsonl ]]; then
    tail -n 5 logs/check-results.jsonl | sed 's/^/  /'
  else
    echo "  No recorded checks yet."
  fi
} > logs/session-close.md

cat logs/session-close.md
echo
echo "Session close recorded: logs/session-close.md"
