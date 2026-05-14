#!/usr/bin/env python3
# Version: v0.1.1
# Last updated: 2026-05-12
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
MANIFEST = ROOT / "_maintainer" / "PUBLIC-REPO-IGNORE-MANIFEST.md"


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


def read_manifest_patterns() -> tuple[list[str], bool]:
    if not MANIFEST.is_file():
        return [], False

    patterns: list[str] = []
    in_patterns = False
    for raw_line in MANIFEST.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if line == "## Ignore Patterns":
            in_patterns = True
            continue
        if in_patterns and line.startswith("## "):
            break
        if in_patterns and line.startswith("- `") and line.endswith("`"):
            patterns.append(line.removeprefix("- `").removesuffix("`"))
    return patterns, True


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
    manifest_patterns, manifest_present = read_manifest_patterns()
    authoritative_patterns = manifest_patterns if manifest_present else gitignore_patterns

    missing_from_gitignore = [
        pattern for pattern in authoritative_patterns if pattern not in gitignore_patterns
    ]

    tracked_paths = git_lines("ls-files")
    tracked_ignored = [path for path in tracked_paths if is_ignored(path)]

    untracked_public_candidates = git_lines("ls-files", "--others", "--exclude-standard")

    warnings: list[str] = []
    if not manifest_present:
        warnings.append(
            "_maintainer/PUBLIC-REPO-IGNORE-MANIFEST.md is missing; falling back to .gitignore only"
        )
    if missing_from_gitignore:
        warnings.append("private ignore manifest contains patterns missing from .gitignore")
    if tracked_ignored:
        warnings.append("tracked files match private/public ignore rules and should be untracked")
    if untracked_public_candidates:
        warnings.append("untracked files are not ignored; commit them or add them to the private manifest")

    return {
        "tool": "public-repo-check",
        "status": "warning" if warnings else "pass",
        "private_manifest": {
            "path": "_maintainer/PUBLIC-REPO-IGNORE-MANIFEST.md",
            "present": manifest_present,
            "committable": False,
        },
        "gitignore": {
            "path": ".gitignore",
            "patterns": gitignore_patterns,
            "missing_manifest_patterns": missing_from_gitignore,
        },
        "rules": {
            "manifest_patterns": authoritative_patterns,
            "manifest_is_authority_when_present": True,
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
