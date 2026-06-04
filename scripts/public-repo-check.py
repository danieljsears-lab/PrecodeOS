#!/usr/bin/env python3
# Version: v0.1.2
# Last updated: 2026-06-04
# Owner: PrecodeOS
# Created by Dan Sears / Recode.
# SPDX-License-Identifier: Apache-2.0
from __future__ import annotations

import json
import subprocess
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
GITIGNORE = ROOT / ".gitignore"


def run_git(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", *args],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )


def read_gitignore_patterns() -> list[str]:
    if not GITIGNORE.is_file():
        return []
    patterns: list[str] = []
    for raw_line in GITIGNORE.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if line and not line.startswith("#"):
            patterns.append(line)
    return patterns


def git_lines(*args: str) -> list[str]:
    result = run_git(*args)
    if result.returncode != 0:
        return []
    return [line for line in result.stdout.splitlines() if line]


def is_ignored(path: str) -> bool:
    result = run_git("check-ignore", "--no-index", "-q", "--", path)
    return result.returncode == 0


def public_repo_status() -> dict[str, Any]:
    gitignore_patterns = read_gitignore_patterns()

    tracked_paths = git_lines("ls-files")
    tracked_ignored = [path for path in tracked_paths if is_ignored(path)]

    untracked_public_candidates = git_lines("ls-files", "--others", "--exclude-standard")

    warnings: list[str] = []
    if tracked_ignored:
        warnings.append("tracked files match git ignore rules and should be untracked")
    if untracked_public_candidates:
        warnings.append("untracked files are not ignored; commit them or add them to .gitignore")

    return {
        "tool": "public-repo-check",
        "status": "warning" if warnings else "pass",
        "gitignore": {
            "path": ".gitignore",
            "patterns": gitignore_patterns,
        },
        "rules": {
            "gitignore_is_boundary_authority": True,
            "anything_not_ignored_is_public_candidate": True,
            "generated_reports_are_evidence_only": True,
        },
        "tracked_ignored": tracked_ignored,
        "untracked_public_candidates": untracked_public_candidates,
        "warnings": warnings,
    }


def main() -> int:
    print(json.dumps(public_repo_status(), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
