#!/usr/bin/env python3
# Version: v0.1.0
# Last updated: 2026-09-06
# Owner: PrecodeOS
# Created by Dan Sears / Recode.
# SPDX-License-Identifier: Apache-2.0
"""Enforce the v1 npm distribution boundary without publishing a package."""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import tempfile
from pathlib import Path
from typing import Any

from os_compiler import repo_root


REQUIRED = {
    "AGENT.md",
    "DECISIONS.md",
    "tasks/templates/PRECODE-TODO-TEMPLATE.md",
    "tasks/beads/BEAD-SCHEMA.md",
    "tasks/prds/PRD-000-template.md",
    "tasks/prds/PRD-SHARD-SCHEMA.md",
    "docs/PRECODE-GUIDED-SETUP.md",
    "adapters/ADAPTER-INDEX.md",
    "scripts/bootstrap-check.py",
    "bin/precodeos.mjs",
}


def evaluate(files: set[str]) -> dict[str, Any]:
    missing = sorted(REQUIRED - files)
    forbidden = sorted(
        path
        for path in files
        if path.startswith("tasks/prds-html/")
        or path == "tasks/todo.md"
        or re.match(r"tasks/prds/PRD-(?!000-template\.md|SHARD-SCHEMA\.md).+\.md$", path)
        or re.match(r"tasks/beads/(?!BEAD-SCHEMA\.md).+\.md$", path)
    )
    return {
        "tool": "npm-package-check",
        "status": "pass" if not missing and not forbidden else "fail",
        "file_count": len(files),
        "missing_required": missing,
        "forbidden_package_development_artifacts": forbidden,
        "generated_evidence_only": True,
        "publishes_package": False,
    }


def inspect(root: Path) -> dict[str, Any]:
    with tempfile.TemporaryDirectory(prefix="precode-npm-cache-") as cache:
        env = dict(os.environ)
        env["npm_config_cache"] = cache
        result = subprocess.run(
            ["npm", "pack", "--dry-run", "--json", "--ignore-scripts"],
            cwd=root,
            env=env,
            check=False,
            capture_output=True,
            text=True,
            timeout=60,
        )
    if result.returncode != 0:
        return {
            "tool": "npm-package-check",
            "status": "fail",
            "error": (result.stderr or result.stdout or "npm pack dry-run failed").strip(),
            "publishes_package": False,
        }
    try:
        payload = json.loads(result.stdout)
        files = {str(item["path"]) for item in payload[0]["files"]}
    except (json.JSONDecodeError, KeyError, IndexError, TypeError) as exc:
        return {"tool": "npm-package-check", "status": "fail", "error": f"could not parse npm pack output: {exc}", "publishes_package": False}
    return evaluate(files)


def self_test() -> dict[str, Any]:
    passing = evaluate(set(REQUIRED))
    failing = evaluate(
        set(REQUIRED)
        | {
            "tasks/todo.md",
            "tasks/prds/PRD-041-package-dev.md",
            "tasks/beads/B001-package-dev.md",
            "tasks/prds-html/index.html",
        }
    )
    failures = []
    if passing["status"] != "pass":
        failures.append({"scenario": "bounded package", "actual": passing})
    if failing["status"] != "fail" or len(failing["forbidden_package_development_artifacts"]) != 4:
        failures.append({"scenario": "package-development artifacts", "actual": failing})
    return {"tool": "npm-package-check", "mode": "self-test", "status": "pass" if not failures else "fail", "failures": failures}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    payload = self_test() if args.self_test else inspect(repo_root())
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0 if payload["status"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
