#!/usr/bin/env bash
# Version: v0.1.1
# Last updated: 2026-06-14
# Owner: PrecodeOS
# Created by Dan Sears / Recode.
# SPDX-License-Identifier: Apache-2.0
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
python3 scripts/os-integrity-check.py --staged --strict "${staged_paths[@]}"
OS_INTEGRITY_CHECKED=1 bash scripts/write-guard.sh --staged "${staged_paths[@]}"

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

if [[ ${#staged_shell[@]} -gt 0 ]]; then
  for path in "${staged_shell[@]}"; do
    bash -n "$path"
  done
fi

if [[ ${#staged_python[@]} -gt 0 ]]; then
  python3 -m py_compile "${staged_python[@]}"
fi

echo "pre-commit: running full memory validation"
bash scripts/validate-memory.sh

echo "pre-commit: running advisory public repo check"
python3 scripts/public-repo-check.py

echo "pre-commit: running advisory file inventory check"
python3 scripts/file-inventory.py --check

echo "pre-commit: running advisory completion check"
python3 scripts/completion-check.py

echo "pre-commit: validation passed"
