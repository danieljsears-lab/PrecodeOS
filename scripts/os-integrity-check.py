#!/usr/bin/env python3
# Version: v0.1.0
# Last updated: 2026-06-14
# Owner: PrecodeOS
# Created by Dan Sears / Recode.
# SPDX-License-Identifier: Apache-2.0
from __future__ import annotations

import argparse
from dataclasses import dataclass
from datetime import datetime, timezone
import json
from pathlib import Path
import subprocess
from typing import Any

from os_compiler import repo_root


CHECKPOINT_ROOT = Path("logs/os-checkpoints")
HIGH_RISK_CLASSES = {
    "active_memory",
    "execution_state",
    "protocols_templates",
    "validation_hooks_scripts",
    "adapters_shims",
    "public_private_boundary",
}
GENERATED_EXACT = {"OS-HEALTH.md", "PRECODE-HELP.md", "PROGRESS.md"}
LOG_SOURCE_EXCEPTIONS = {"logs/LOG-EVIDENCE-TAXONOMY.md"}
APPEND_ONLY_PREFIXES = {"logs/check-output/", "logs/scheduled-audit-output/"}
APPEND_ONLY_SUFFIXES = {".jsonl"}


@dataclass(frozen=True)
class Surface:
    surface_class: str
    protected: bool
    reason: str


def run_git(root: Path, *args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", *args],
        cwd=root,
        text=True,
        capture_output=True,
        check=False,
    )


def git_head(root: Path) -> str:
    result = run_git(root, "rev-parse", "HEAD")
    return result.stdout.strip() if result.returncode == 0 else ""


def git_paths(root: Path, *, staged: bool) -> list[str]:
    if staged:
        result = run_git(root, "diff", "--cached", "--name-only", "--diff-filter=ACMR")
        return sorted(line for line in result.stdout.splitlines() if line) if result.returncode == 0 else []

    paths: set[str] = set()
    for args in (
        ("diff", "--name-only", "--diff-filter=ACMR"),
        ("diff", "--cached", "--name-only", "--diff-filter=ACMR"),
        ("ls-files", "--others", "--exclude-standard"),
    ):
        result = run_git(root, *args)
        if result.returncode == 0:
            paths.update(line for line in result.stdout.splitlines() if line)
    return sorted(paths)


def normalize(path: str) -> str:
    path = path.strip().replace("\\", "/")
    while path.startswith("./"):
        path = path[2:]
    return path


def is_generated(path: str) -> bool:
    if path in GENERATED_EXACT:
        return True
    if path in LOG_SOURCE_EXCEPTIONS:
        return False
    if path.startswith("docs-html/"):
        return True
    if path.startswith("logs/"):
        return True
    return False


def is_append_only_evidence(path: str) -> bool:
    return any(path.startswith(prefix) for prefix in APPEND_ONLY_PREFIXES) or Path(path).suffix in APPEND_ONLY_SUFFIXES


def classify(path: str) -> Surface:
    path = normalize(path)
    if path in {"AGENT.md", "DECISIONS.md", "tasks/todo.md"}:
        return Surface("active_memory", True, "active memory is part of the always-loaded OS kernel")
    if path == ".gitignore" or path == ".github/PULL_REQUEST_TEMPLATE.md":
        return Surface("public_private_boundary", True, "public/private or contribution boundary file")
    if path.startswith(".githooks/"):
        return Surface("validation_hooks_scripts", True, "local hook behavior can change package validation")
    if path.startswith(".github/workflows/"):
        return Surface("validation_hooks_scripts", True, "GitHub workflow behavior can change package validation")
    if path == ".github/copilot-instructions.md":
        return Surface("adapters_shims", True, "AI coding tool shim can change agent behavior")
    if path.startswith("scripts/") and Path(path).suffix in {".py", ".sh"}:
        return Surface("validation_hooks_scripts", True, "maintained script can change package checks or generated evidence")
    if path.startswith("tasks/reference/") or path.startswith("tasks/templates/"):
        return Surface("protocols_templates", True, "protocol or template can change package workflow rules")
    if path.startswith("tasks/beads/") or path.startswith("tasks/prds/"):
        return Surface("execution_state", True, "bead, schema, or PRD surface can change execution contracts")
    if path.startswith("adapters/") or path in {"AGENTS.md", "CLAUDE.md", "GEMINI.md"}:
        return Surface("adapters_shims", True, "adapter or shim can change host-agent behavior")
    if is_generated(path):
        return Surface("generated_evidence", False, "generated evidence is not protected source truth")
    if path == "README.md" or path.startswith("docs/") or path in {
        "CONTRIBUTING.md",
        "GOVERNANCE.md",
        "LICENSE",
        "NOTICE",
        "TRADEMARK.md",
    }:
        return Surface("package_docs_surface", False, "public package documentation surface")
    return Surface("other", False, "not classified as a protected PrecodeOS source surface")


def checkpoint_manifests(root: Path) -> list[dict[str, Any]]:
    base = root / CHECKPOINT_ROOT
    if not base.is_dir():
        return []
    manifests: list[dict[str, Any]] = []
    for path in sorted(base.glob("*/manifest.json")):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        data["_manifest_path"] = path.relative_to(root).as_posix()
        manifests.append(data)
    return manifests


def checkpoint_covers(path: str, manifest: dict[str, Any], head: str) -> bool:
    if manifest.get("git_head") != head:
        return False
    if not manifest.get("clean"):
        return False
    files = manifest.get("files")
    if not isinstance(files, list):
        return False
    covered = {normalize(str(item.get("path", ""))) for item in files if isinstance(item, dict)}
    return normalize(path) in covered


def analyze(paths: list[str], root: Path) -> dict[str, Any]:
    head = git_head(root)
    manifests = checkpoint_manifests(root)
    findings: list[dict[str, Any]] = []
    missing_checkpoint: list[str] = []

    for raw_path in paths:
        path = normalize(raw_path)
        surface = classify(path)
        checkpoint_ids = [
            str(manifest.get("id", ""))
            for manifest in manifests
            if checkpoint_covers(path, manifest, head)
        ]
        has_checkpoint = bool([item for item in checkpoint_ids if item])
        strict_required = surface.surface_class in HIGH_RISK_CLASSES
        if strict_required and not has_checkpoint:
            missing_checkpoint.append(path)
        findings.append(
            {
                "path": path,
                "surface_class": surface.surface_class,
                "protected_source": surface.protected,
                "strict_checkpoint_required": strict_required,
                "valid_checkpoint": has_checkpoint,
                "checkpoint_ids": checkpoint_ids,
                "append_only_evidence": is_append_only_evidence(path),
                "reason": surface.reason,
            }
        )

    warnings: list[str] = []
    if missing_checkpoint:
        warnings.append("protected PrecodeOS source edits lack a valid scoped checkpoint")

    return {
        "tool": "os-integrity-check",
        "status": "warning" if warnings else "pass",
        "git_head": head,
        "checked_paths": len(paths),
        "checkpoint_root": CHECKPOINT_ROOT.as_posix(),
        "rules": {
            "advisory_unless_strict": True,
            "protects_precodeos_source_not_target_app": True,
            "generated_evidence_is_not_source_truth": True,
            "append_only_evidence_not_restored": True,
        },
        "findings": findings,
        "missing_checkpoint": missing_checkpoint,
        "warnings": warnings,
    }


def render_text(payload: dict[str, Any], *, strict: bool) -> str:
    lines = [
        f"os-integrity-check: {payload['status']} ({payload['checked_paths']} paths)",
    ]
    for finding in payload["findings"]:
        label = "checkpoint required" if finding["strict_checkpoint_required"] else "advisory"
        checkpoint = "has checkpoint" if finding["valid_checkpoint"] else "no checkpoint"
        lines.append(f"- {finding['path']}: {finding['surface_class']} ({label}, {checkpoint})")
    for warning in payload["warnings"]:
        lines.append(f"warning: {warning}")
    if strict and payload["missing_checkpoint"]:
        lines.append("strict mode: create a scoped checkpoint before committing protected OS source edits")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Check PrecodeOS-owned surface integrity for changed paths.")
    parser.add_argument("--staged", action="store_true", help="inspect staged files instead of all changed public files")
    parser.add_argument("--strict", action="store_true", help="exit nonzero when protected source edits lack a valid checkpoint")
    parser.add_argument("--json", action="store_true", help="print machine-readable JSON")
    parser.add_argument("paths", nargs="*", help="optional explicit paths to inspect")
    args = parser.parse_args()

    root = repo_root()
    paths = [normalize(path) for path in args.paths] if args.paths else git_paths(root, staged=args.staged)
    payload = analyze(paths, root)
    payload["mode"] = "staged" if args.staged else "changed"
    payload["strict"] = args.strict

    if args.json:
        print(json.dumps(payload, indent=2, sort_keys=True))
    else:
        print(render_text(payload, strict=args.strict))

    if args.strict and payload["missing_checkpoint"]:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
