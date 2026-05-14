#!/usr/bin/env bash
# Version: v0.1.0
# Last updated: 2026-04-26
# Owner: PrecodeOS
# Created by Dan Sears / Recode.
# SPDX-License-Identifier: Apache-2.0
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo_root"

mode="post"
use_staged="false"
declare -a raw_paths=()

while [[ $# -gt 0 ]]; do
  case "$1" in
    --pre)
      mode="pre"
      shift
      ;;
    --post)
      mode="post"
      shift
      ;;
    --mark-read)
      mode="mark-read"
      shift
      ;;
    --staged)
      use_staged="true"
      shift
      ;;
    *)
      raw_paths+=("$1")
      shift
      ;;
  esac
done

if [[ "$use_staged" == "true" && ${#raw_paths[@]} -eq 0 ]]; then
  while IFS= read -r path; do
    [[ -n "$path" ]] && raw_paths+=("$path")
  done < <(git diff --cached --name-only --diff-filter=ACMR)
fi

case "$mode" in
  mark-read)
    echo "write-guard: generic scaffold has no read marker requirement"
    ;;
  pre)
    echo "write-guard: pre-check ok"
    ;;
  post)
    if [[ ${#raw_paths[@]} -gt 0 ]]; then
      bash scripts/validate-memory.sh "${raw_paths[@]}"
    else
      bash scripts/validate-memory.sh
    fi
    ;;
  *)
    echo "write-guard: unknown mode $mode" >&2
    exit 2
    ;;
esac
