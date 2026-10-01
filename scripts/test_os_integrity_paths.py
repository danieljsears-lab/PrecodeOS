#!/usr/bin/env python3
# Version: v0.1.0
# Last updated: 2026-10-01
# Owner: PrecodeOS
# Created by Dan Sears / Recode.
# SPDX-License-Identifier: Apache-2.0
"""Regression coverage for package-relative Git paths in nested installs."""

from __future__ import annotations

import importlib.util
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def load_script(name: str, filename: str):
    spec = importlib.util.spec_from_file_location(name, ROOT / "scripts" / filename)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


CHECKPOINT = load_script("os_checkpoint", "os-checkpoint.py")
INTEGRITY = load_script("os_integrity", "os-integrity-check.py")


def git(cwd: Path, *args: str) -> None:
    result = subprocess.run(["git", *args], cwd=cwd, capture_output=True, text=True)
    if result.returncode:
        raise AssertionError(result.stderr or result.stdout)


class NestedPackagePathTests(unittest.TestCase):
    def make_repo(self) -> tuple[Path, Path]:
        directory = Path(tempfile.mkdtemp()).resolve()
        package = directory / "repo" / "precode"
        package.mkdir(parents=True)
        (package / "scripts").mkdir()
        (package / "scripts" / "guard.py").write_text("print('ok')\n", encoding="utf-8")
        (package / "scripts" / "guard.sh").write_text("#!/usr/bin/env bash\necho ok\n", encoding="utf-8")
        repository = directory / "repo"
        git(repository, "init", "-q")
        git(repository, "config", "user.name", "Test")
        git(repository, "config", "user.email", "test@example.com")
        git(repository, "add", ".")
        git(repository, "commit", "-qm", "baseline")
        return repository, package

    def test_nested_paths_rebase_for_integrity_and_checkpoint(self) -> None:
        repository, package = self.make_repo()
        (package / "scripts" / "guard.py").write_text("print('changed')\n", encoding="utf-8")
        (repository / "frontend").mkdir()
        (repository / "frontend" / "page.tsx").write_text("changed\n", encoding="utf-8")
        git(repository, "add", ".")

        self.assertEqual(INTEGRITY.git_paths(package, staged=True), ["../frontend/page.tsx", "scripts/guard.py"])
        self.assertIn("scripts/guard.py", CHECKPOINT.git_dirty_paths(package))

    def test_top_level_paths_remain_unchanged(self) -> None:
        repository, _ = self.make_repo()
        self.assertEqual(INTEGRITY.git_paths(repository, staged=True), [])


if __name__ == "__main__":
    unittest.main()
