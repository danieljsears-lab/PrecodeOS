#!/usr/bin/env bash
# Version: v0.1.0
# Last updated: 2026-04-26
# Owner: Precode OS
set -uo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo_root"

output_dir="$repo_root/logs/scheduled-audit-output"
mkdir -p "$output_dir"
timestamp="$(date -u +"%Y%m%dT%H%M%SZ")"

validate_output="$output_dir/${timestamp}-validate-memory.log"
spend_output="$output_dir/${timestamp}-import-agent-spend-dry-run.log"
github_output="$output_dir/${timestamp}-github-audit.json"

bash scripts/validate-memory.sh >"$validate_output" 2>&1
validate_exit=$?

python3 scripts/os-health.py
health_exit=$?

python3 scripts/update-learning-diary.py
diary_exit=$?

python3 scripts/import-agent-spend.py --dry-run >"$spend_output" 2>&1
spend_exit=$?

python3 scripts/github-audit.py >"$github_output" 2>&1
github_exit=$?

python3 scripts/scheduled-audit.py \
  --validate-exit "$validate_exit" \
  --validate-output "${validate_output#"$repo_root/"}" \
  --health-exit "$health_exit" \
  --diary-exit "$diary_exit" \
  --spend-exit "$spend_exit" \
  --spend-output "${spend_output#"$repo_root/"}" \
  --github-exit "$github_exit" \
  --github-output "${github_output#"$repo_root/"}"
audit_exit=$?

if [[ "$health_exit" -ne 0 || "$diary_exit" -ne 0 || "$audit_exit" -ne 0 ]]; then
  exit 1
fi

exit 0
