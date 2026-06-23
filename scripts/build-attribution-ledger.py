#!/usr/bin/env python3
# Version: v0.1.0
# Last updated: 2026-06-23
# Owner: PrecodeOS
# Created by Dan Sears / Recode.
# SPDX-License-Identifier: Apache-2.0
from __future__ import annotations

import argparse
import json
from dataclasses import dataclass, field
from pathlib import Path
import sys
import tempfile
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parent))

from os_compiler import build_attribution_ledger, read_bead, repo_root
from precode_state import bead_paths


@dataclass
class FixtureBead:
    rel_path: str
    bead_id: str
    title: str
    status: str = "done"
    primary_authority: str = "tasks/prds/PRD-028-build-attribution-ledger.md"
    closeout: dict[str, str] = field(default_factory=dict)


def current_beads(root: Path) -> list[Any]:
    return [read_bead(path, root) for path in bead_paths(root)]


def print_json(payload: dict[str, Any]) -> None:
    print(json.dumps(payload, indent=2, sort_keys=True))


def self_test() -> int:
    failures: list[dict[str, str]] = []
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        (root / "logs").mkdir()
        commit = "0123456789abcdef0123456789abcdef01234567"
        (root / "logs" / "bead-build-journal.jsonl").write_text(
            json.dumps(
                {
                    "bead": "tasks/beads/B003-git-hint.md",
                    "timestamp": "2026-06-23T00:00:00+00:00",
                    "git": {"end_commit": commit},
                    "changes": {"implementation": [{"path": "app/example.py", "status": "M"}]},
                }
            )
            + "\n",
            encoding="utf-8",
        )
        beads = [
            FixtureBead(
                rel_path="tasks/beads/B001-reviewed.md",
                bead_id="B001",
                title="Reviewed attribution",
                closeout={
                    "human_contributor": "Dan Sears",
                    "contributor_role": "Coordinator",
                    "agent_tool_surface": "Codex",
                    "attribution_reviewed_by": "Dan Sears",
                    "attribution_uncertainty": "none recorded",
                },
            ),
            FixtureBead(
                rel_path="tasks/beads/B002-partial.md",
                bead_id="B002",
                title="Partial attribution",
                closeout={"human_contributor": "Sam Contributor"},
            ),
            FixtureBead(
                rel_path="tasks/beads/B003-git-hint.md",
                bead_id="B003",
                title="Git hint only",
                closeout={},
            ),
            FixtureBead(
                rel_path="tasks/beads/B004-missing.md",
                bead_id="B004",
                title="Missing attribution",
                closeout={},
            ),
        ]
        payload = build_attribution_ledger(root, beads)
        entries = payload.get("details", {}).get("entries", [])

    if payload.get("status") != "warning":
        failures.append({"scenario": "status", "message": "missing and partial attribution should warn"})
    if payload.get("generated_report_warning", "").find("generated evidence only") == -1:
        failures.append({"scenario": "generated_warning", "message": "generated evidence warning missing"})
    if payload.get("details", {}).get("reviewed_closeout_count") != 1:
        failures.append({"scenario": "reviewed_count", "message": "reviewed closeout count should be 1"})
    if payload.get("details", {}).get("partial_closeout_count") != 1:
        failures.append({"scenario": "partial_count", "message": "partial closeout count should be 1"})
    if payload.get("details", {}).get("missing_attribution_count") < 1:
        failures.append({"scenario": "missing_count", "message": "missing attribution should be counted"})
    forbidden = payload.get("details", {}).get("forbidden_uses", [])
    for term in ("task selection", "implementation acceptance", "merge approval", "contributor scoring", "registry behavior"):
        if term not in forbidden:
            failures.append({"scenario": "forbidden_uses", "message": f"missing forbidden use: {term}"})
    reviewed = next((entry for entry in entries if entry.get("bead_id") == "B001"), {})
    if reviewed.get("human_contributor") != "Dan Sears" or reviewed.get("agent_tool_surface") != "Codex":
        failures.append({"scenario": "reviewed_entry", "message": "reviewed human and agent attribution not preserved"})

    print_json({"tool": "build-attribution-ledger", "mode": "self-test", "status": "fail" if failures else "pass", "scenario_count": 6, "failures": failures})
    return 1 if failures else 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Print generated Build Attribution Ledger evidence.")
    parser.add_argument("--self-test", action="store_true", help="run deterministic fixture coverage")
    args = parser.parse_args()
    if args.self_test:
        return self_test()

    root = repo_root()
    payload = build_attribution_ledger(root, current_beads(root))
    print_json(payload)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
