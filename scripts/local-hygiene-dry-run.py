#!/usr/bin/env python3
# Version: v0.2.0
# Last updated: 2026-06-14
# Owner: PrecodeOS
# Created by Dan Sears / Recode.
# SPDX-License-Identifier: Apache-2.0
from __future__ import annotations

import argparse
import json
from pathlib import Path
from tempfile import TemporaryDirectory

from os_compiler import (
    compile_state,
    local_hygiene_summary,
    local_hygiene_preview_from_summary,
    render_local_hygiene_preview_markdown,
    repo_root,
    write_json,
)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def run_self_test() -> int:
    synthetic_summary = {
        "status": "warning",
        "warnings": ["synthetic local hygiene warning"],
        "details": {
            "bulky_log_candidates": [
                {
                    "path": "logs/check-output/old.log",
                    "bytes": 11,
                    "rule": "bulky generated output older than 90 days",
                }
            ],
            "bulky_log_candidate_bytes": 11,
            "cache_candidates": [
                {
                    "path": ".pytest_cache",
                    "bytes": 22,
                    "rule": "known cache/build/dependency directory that is ignored or untracked",
                }
            ],
            "cache_candidate_bytes": 22,
            "protected_evidence_outputs": ["logs/check-output/protected.log"],
            "protected_bulky_outputs": [
                {
                    "path": "logs/check-output/current.log",
                    "bytes": 33,
                    "rule": "bulky generated output older than 90 days",
                    "reason": "referenced by current or unaccepted bead evidence",
                }
            ],
            "protected_generated_outputs": [
                {
                    "path": "logs/os-checkpoints/fixture/manifest.json",
                    "bytes": 44,
                    "rule": "logs/os-checkpoints is generated evidence, not cleanup clutter",
                    "reason": "expected protected generated evidence family",
                }
            ],
            "unexpected_logs": ["logs/.DS_Store"],
            "cache_observed_not_candidate": [
                {
                    "path": "tracked-cache",
                    "bytes": 55,
                    "rule": "known cache/build/dependency directory that is ignored or untracked",
                    "reason": "not proven ignored or untracked",
                }
            ],
            "generated_preview_files": ["logs/local-hygiene-preview.json", "logs/local-hygiene-preview.md"],
            "next_safe_action": "review candidates only",
        },
    }
    preview = local_hygiene_preview_from_summary(synthetic_summary)
    actions = preview["actions"]
    require(all(action.get("mutates_now") is False for action in actions), "preview action mutates_now must stay false")
    require(all(action.get("candidate_id") for action in actions), "preview actions must include candidate_id")
    classifications = {action.get("classification") for action in actions}
    require({"candidate", "protected", "unexpected_review", "not_candidate"}.issubset(classifications), "missing v2 classifications")
    require(any(action.get("path") == "logs/.DS_Store" and action.get("classification") == "unexpected_review" for action in actions), ".DS_Store must be unexpected_review")
    require(any(action.get("path") == "tracked-cache" and action.get("classification") == "not_candidate" for action in actions), "tracked or unproven cache must be not_candidate")
    require(any(action.get("approval_required") is True for action in actions if action.get("classification") == "candidate"), "candidates must require approval")
    require(all(action.get("approval_required") is False for action in actions if action.get("classification") != "candidate"), "non-candidates must not request cleanup approval")
    rendered = render_local_hygiene_preview_markdown(preview)
    require("| Candidate ID | Classification | Action | Path |" in rendered, "rendered preview must include v2 table headers")

    with TemporaryDirectory() as tmp:
        root = Path(tmp)
        checkpoint = root / "logs" / "os-checkpoints" / "fixture" / "manifest.json"
        checkpoint.parent.mkdir(parents=True)
        checkpoint.write_text("{}", encoding="utf-8")
        ds_store = root / "logs" / ".DS_Store"
        ds_store.write_text("metadata", encoding="utf-8")
        summary = local_hygiene_summary(root, [], [], None)
        details = summary["details"]
        require("logs/.DS_Store" in details["unexpected_logs"], ".DS_Store should remain an unexpected review item")
        require(
            any(item.get("path") == "logs/os-checkpoints/fixture/manifest.json" for item in details["protected_generated_outputs"]),
            "os-checkpoints files must be protected generated outputs",
        )
        require(
            "logs/os-checkpoints/fixture/manifest.json" not in details["unexpected_logs"],
            "os-checkpoints files must not be unexpected clutter",
        )

    print(json.dumps({"tool": "local-hygiene-dry-run", "mode": "self-test", "status": "pass"}, indent=2, sort_keys=True))
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Preview Local Hygiene candidates without mutating files.")
    parser.add_argument("--self-test", action="store_true", help="Run deterministic Local Hygiene v2 preview classification tests.")
    args = parser.parse_args()
    if args.self_test:
        return run_self_test()

    root = repo_root()
    state = compile_state(root)
    summary = state.get("local_hygiene") or {
        "status": "missing",
        "warnings": ["local hygiene summary unavailable"],
        "details": {},
    }
    preview = local_hygiene_preview_from_summary(summary)
    write_json(root / "logs" / "local-hygiene-preview.json", preview)
    (root / "logs" / "local-hygiene-preview.md").write_text(
        render_local_hygiene_preview_markdown(preview),
        encoding="utf-8",
    )
    print(json.dumps({"tool": "local-hygiene-dry-run", **preview}, indent=2, sort_keys=True))
    print("local-hygiene-dry-run: wrote logs/local-hygiene-preview.json and logs/local-hygiene-preview.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
