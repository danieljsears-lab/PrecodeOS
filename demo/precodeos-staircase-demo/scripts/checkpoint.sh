#!/usr/bin/env bash
set -euo pipefail

echo "PrecodeOS Demo Checkpoint"
bash scripts/validate-memory.sh
python3 scripts/loop-health.py
python3 scripts/files-in-play-check.py || true
