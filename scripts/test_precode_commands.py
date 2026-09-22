#!/usr/bin/env python3
# Version: v0.1.0
# Last updated: 2026-09-21
# Owner: PrecodeOS
# Created by Dan Sears / Recode.
# SPDX-License-Identifier: Apache-2.0
"""Focused regression coverage for Git status paths used by Precode guardrails."""

from __future__ import annotations

import subprocess
import tempfile
import unittest
from pathlib import Path

from precode_commands import git_status_changed_paths


def git(root: Path, *args: str) -> None:
    result = subprocess.run(["git", *args], cwd=root, check=False, capture_output=True, text=True)
    if result.returncode:
        raise AssertionError(result.stderr or result.stdout)


class GitStatusChangedPathsTests(unittest.TestCase):
    def test_nested_root_rebases_paths_and_top_level_root_still_works(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            git(root, "init", "-q")
            (root / "precode").mkdir()
            (root / "frontend").mkdir()
            (root / "precode" / "DECISIONS.md").write_text("changed\n", encoding="utf-8")
            (root / "frontend" / "page.tsx").write_text("changed\n", encoding="utf-8")
            git(root, "add", ".")
            git(root, "-c", "user.name=Test", "-c", "user.email=test@example.com", "commit", "-qm", "baseline")
            (root / "precode" / "DECISIONS.md").write_text("changed again\n", encoding="utf-8")
            (root / "frontend" / "page.tsx").write_text("changed again\n", encoding="utf-8")

            nested_paths, nested_error = git_status_changed_paths(root / "precode")
            top_level_paths, top_level_error = git_status_changed_paths(root)

            self.assertIsNone(nested_error)
            self.assertIsNone(top_level_error)
            self.assertIn("DECISIONS.md", nested_paths)
            self.assertIn("../frontend/page.tsx", nested_paths)
            self.assertIn("precode/DECISIONS.md", top_level_paths)
            self.assertIn("frontend/page.tsx", top_level_paths)

    def test_non_git_root_reports_unavailable_status(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            paths, error = git_status_changed_paths(Path(directory))
            self.assertEqual(paths, [])
            self.assertEqual(error, "git status unavailable: workspace root is not inside a git checkout")


if __name__ == "__main__":
    unittest.main()
