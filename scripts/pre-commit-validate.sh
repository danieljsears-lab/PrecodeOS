#!/usr/bin/env bash
# Version: v0.1.0
# Last updated: 2026-04-26
# Owner: Precode OS
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo_root"

declare -a staged_paths=()
while IFS= read -r path; do
  [[ -n "$path" ]] && staged_paths+=("$path")
done < <(git diff --cached --name-only --diff-filter=ACMR)

if [[ ${#staged_paths[@]} -eq 0 ]]; then
  echo "pre-commit: no staged files to validate"
  exit 0
fi

echo "pre-commit: running shared write guard"
bash scripts/write-guard.sh --staged "${staged_paths[@]}"

declare -a staged_shell=()
declare -a staged_python=()
for path in "${staged_paths[@]}"; do
  case "$path" in
    *.sh)
      [[ -f "$path" ]] && staged_shell+=("$path")
      ;;
    *.py)
      [[ -f "$path" ]] && staged_python+=("$path")
      ;;
  esac
done

for path in "${staged_shell[@]}"; do
  bash -n "$path"
done

if [[ ${#staged_python[@]} -gt 0 ]]; then
  python3 -m py_compile "${staged_python[@]}"
fi

echo "pre-commit: running full memory validation"
bash scripts/validate-memory.sh

echo "pre-commit: validation passed"
