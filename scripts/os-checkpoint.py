#!/usr/bin/env python3
# Version: v0.1.0
# Last updated: 2026-06-14
# Owner: PrecodeOS
# Created by Dan Sears / Recode.
# SPDX-License-Identifier: Apache-2.0
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
from typing import Any

from os_compiler import repo_root


CHECKPOINT_ROOT = Path("logs/os-checkpoints")
GENERATED_EXACT = {"OS-HEALTH.md", "PRECODE-HELP.md", "PROGRESS.md"}
LOG_SOURCE_EXCEPTIONS = {"logs/LOG-EVIDENCE-TAXONOMY.md"}
APPEND_ONLY_PREFIXES = {"logs/check-output/", "logs/scheduled-audit-output/"}
APPEND_ONLY_SUFFIXES = {".jsonl"}


def run_git(root: Path, *args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", *args],
        cwd=root,
        text=True,
        capture_output=True,
        check=False,
    )


def normalize(path: str) -> str:
    path = path.strip().replace("\\", "/")
    while path.startswith("./"):
        path = path[2:]
    return path


def slug(value: str) -> str:
    chars = [char.lower() if char.isalnum() else "-" for char in value.strip()]
    return "-".join("".join(chars).split("-"))[:48] or "checkpoint"


def now() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def git_head(root: Path) -> str:
    result = run_git(root, "rev-parse", "HEAD")
    return result.stdout.strip() if result.returncode == 0 else ""


def git_dirty_paths(root: Path) -> set[str]:
    result = run_git(root, "status", "--porcelain")
    if result.returncode != 0:
        return set()
    dirty: set[str] = set()
    for line in result.stdout.splitlines():
        if not line:
            continue
        status = line[:2]
        if status == "??":
            continue
        path = line[3:] if len(line) > 3 else ""
        if " -> " in path:
            path = path.split(" -> ", 1)[1]
        if path:
            dirty.add(normalize(path))
    return dirty


def is_tracked(root: Path, path: str) -> bool:
    result = run_git(root, "ls-files", "--error-unmatch", "--", path)
    return result.returncode == 0


def git_blob(root: Path, path: str) -> bytes | None:
    result = subprocess.run(
        ["git", "show", f"HEAD:{path}"],
        cwd=root,
        capture_output=True,
        check=False,
    )
    return result.stdout if result.returncode == 0 else None


def is_generated_or_evidence(path: str) -> bool:
    path = normalize(path)
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
    path = normalize(path)
    return any(path.startswith(prefix) for prefix in APPEND_ONLY_PREFIXES) or Path(path).suffix in APPEND_ONLY_SUFFIXES


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def paths_for_scope(root: Path, scope: str) -> list[str]:
    scope = scope.strip()
    patterns = {
        "active-memory": ["AGENT.md", "DECISIONS.md", "tasks/todo.md"],
        "execution-state": ["tasks/beads", "tasks/prds"],
        "protocols": ["tasks/reference", "tasks/templates"],
        "validation": ["scripts", ".githooks", ".github/workflows"],
        "adapters": ["adapters", "AGENTS.md", "CLAUDE.md", "GEMINI.md", ".github/copilot-instructions.md"],
        "package-surface": ["README.md", "docs", "CONTRIBUTING.md", "GOVERNANCE.md", "NOTICE", "TRADEMARK.md"],
        "boundary": [".gitignore", ".github/PULL_REQUEST_TEMPLATE.md"],
    }
    selected = patterns.get(scope, [])
    paths: list[str] = []
    for item in selected:
        full = root / item
        if full.is_file():
            paths.append(item)
        elif full.is_dir():
            paths.extend(path.relative_to(root).as_posix() for path in sorted(full.rglob("*")) if path.is_file())
    return sorted(set(paths))


def load_manifests(root: Path) -> list[dict[str, Any]]:
    base = root / CHECKPOINT_ROOT
    if not base.is_dir():
        return []
    manifests: list[dict[str, Any]] = []
    for path in sorted(base.glob("*/manifest.json"), reverse=True):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        data["_path"] = path
        manifests.append(data)
    return manifests


def find_manifest(root: Path, checkpoint_id: str) -> dict[str, Any] | None:
    for manifest in load_manifests(root):
        if manifest.get("id") == checkpoint_id:
            return manifest
    return None


def create_checkpoint(root: Path, scope: str, reason: str, paths: list[str], *, from_head: bool) -> dict[str, Any]:
    selected = [normalize(path) for path in paths] if paths else paths_for_scope(root, scope)
    if not selected:
        raise SystemExit(f"os-checkpoint: no files selected for scope '{scope}'")

    dirty = git_dirty_paths(root)
    dirty_selected = sorted(path for path in selected if path in dirty and not (from_head and is_tracked(root, path)))
    if dirty_selected:
        raise SystemExit(
            "os-checkpoint: covered paths are dirty; create checkpoints before mutation: "
            + ", ".join(dirty_selected)
        )

    checkpoint_id = f"{now()}-{slug(scope)}"
    checkpoint_dir = root / CHECKPOINT_ROOT / checkpoint_id
    files_dir = checkpoint_dir / "files"
    files_dir.mkdir(parents=True, exist_ok=False)

    entries: list[dict[str, Any]] = []
    skipped: list[dict[str, str]] = []
    for rel_path in selected:
        source = root / rel_path
        blob = git_blob(root, rel_path) if from_head and is_tracked(root, rel_path) else None
        if blob is None and not source.is_file():
            skipped.append({"path": rel_path, "reason": "missing or not a file"})
            continue
        if is_generated_or_evidence(rel_path):
            skipped.append({"path": rel_path, "reason": "generated evidence is not checkpointed as source truth"})
            continue
        destination = files_dir / rel_path
        destination.parent.mkdir(parents=True, exist_ok=True)
        if blob is not None:
            destination.write_bytes(blob)
            checksum = hashlib.sha256(blob).hexdigest()
            size = len(blob)
            file_source = "git_head"
        else:
            shutil.copy2(source, destination)
            checksum = sha256(source)
            size = source.stat().st_size
            file_source = "working_tree"
        entries.append(
            {
                "path": rel_path,
                "sha256": checksum,
                "bytes": size,
                "source": file_source,
            }
        )

    if not entries:
        raise SystemExit("os-checkpoint: no source files were checkpointed")

    manifest = {
        "id": checkpoint_id,
        "created_at": datetime.now(timezone.utc).isoformat(),
        "tool": "os-checkpoint",
        "scope": scope,
        "reason": reason,
        "git_head": git_head(root),
        "clean": True,
        "from_head": from_head,
        "checkpoint_root": CHECKPOINT_ROOT.as_posix(),
        "files": entries,
        "skipped": skipped,
        "rules": {
            "source_files_only": True,
            "generated_evidence_not_source_truth": True,
            "append_only_evidence_not_restored": True,
            "restore_requires_explicit_apply": True,
        },
    }
    (checkpoint_dir / "manifest.json").write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return manifest


def list_checkpoints(root: Path, scope: str = "") -> list[dict[str, Any]]:
    manifests = load_manifests(root)
    if scope:
        manifests = [manifest for manifest in manifests if manifest.get("scope") == scope]
    result: list[dict[str, Any]] = []
    for manifest in manifests:
        result.append(
            {
                "id": manifest.get("id"),
                "created_at": manifest.get("created_at"),
                "scope": manifest.get("scope"),
                "reason": manifest.get("reason"),
                "git_head": manifest.get("git_head"),
                "files": [item.get("path") for item in manifest.get("files", []) if isinstance(item, dict)],
            }
        )
    return result


def restore_checkpoint(root: Path, checkpoint_id: str, *, apply: bool) -> dict[str, Any]:
    manifest = find_manifest(root, checkpoint_id)
    if manifest is None:
        raise SystemExit(f"os-checkpoint: checkpoint not found: {checkpoint_id}")
    checkpoint_dir = Path(manifest["_path"]).parent
    actions: list[dict[str, str]] = []
    skipped: list[dict[str, str]] = []

    for item in manifest.get("files", []):
        if not isinstance(item, dict):
            continue
        rel_path = normalize(str(item.get("path", "")))
        if not rel_path:
            continue
        if is_generated_or_evidence(rel_path) or is_append_only_evidence(rel_path):
            skipped.append({"path": rel_path, "reason": "generated or append-only evidence is not restored"})
            continue
        source = checkpoint_dir / "files" / rel_path
        destination = root / rel_path
        if not source.is_file():
            skipped.append({"path": rel_path, "reason": "checkpoint copy missing"})
            continue
        actions.append({"path": rel_path, "action": "restore" if apply else "would_restore"})
        if apply:
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, destination)

    return {
        "tool": "os-checkpoint",
        "mode": "restore",
        "id": checkpoint_id,
        "applied": apply,
        "actions": actions,
        "skipped": skipped,
        "rules": {
            "generated_evidence_not_source_truth": True,
            "append_only_evidence_not_restored": True,
        },
    }


def print_text(payload: dict[str, Any]) -> None:
    mode = payload.get("mode", "create")
    if mode == "list":
        checkpoints = payload.get("checkpoints", [])
        if not checkpoints:
            print("os-checkpoint: no checkpoints")
            return
        for item in checkpoints:
            print(f"{item['id']}  {item['scope']}  {item['reason']}")
        return
    if mode == "restore":
        action = "restored" if payload.get("applied") else "dry-run"
        print(f"os-checkpoint: {action} {payload['id']}")
        for item in payload.get("actions", []):
            print(f"- {item['action']}: {item['path']}")
        return
    print(f"os-checkpoint: created {payload['id']}")
    for item in payload.get("files", []):
        print(f"- {item['path']}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Create, list, and restore scoped PrecodeOS source checkpoints.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    create = subparsers.add_parser("create", help="create a scoped source checkpoint")
    create.add_argument("--scope", required=True, help="checkpoint scope such as validation, protocols, or adapters")
    create.add_argument("--reason", required=True, help="human reason for the checkpoint")
    create.add_argument("--paths", nargs="*", default=[], help="explicit source paths to checkpoint")
    create.add_argument("--from-head", action="store_true", help="checkpoint tracked dirty paths from git HEAD instead of the working tree")
    create.add_argument("--json", action="store_true", help="print machine-readable JSON")

    list_cmd = subparsers.add_parser("list", help="list checkpoints")
    list_cmd.add_argument("--scope", default="", help="filter by checkpoint scope")
    list_cmd.add_argument("--json", action="store_true", help="print machine-readable JSON")

    restore = subparsers.add_parser("restore", help="restore files from a checkpoint")
    restore.add_argument("--id", required=True, help="checkpoint id to restore")
    mode = restore.add_mutually_exclusive_group()
    mode.add_argument("--dry-run", action="store_true", help="show restore actions without writing files")
    mode.add_argument("--apply", action="store_true", help="apply restore actions")
    restore.add_argument("--json", action="store_true", help="print machine-readable JSON")

    args = parser.parse_args()
    root = repo_root()

    if args.command == "create":
        payload = create_checkpoint(root, args.scope, args.reason, args.paths, from_head=args.from_head)
    elif args.command == "list":
        payload = {
            "tool": "os-checkpoint",
            "mode": "list",
            "checkpoint_root": CHECKPOINT_ROOT.as_posix(),
            "checkpoints": list_checkpoints(root, args.scope),
        }
    else:
        payload = restore_checkpoint(root, args.id, apply=args.apply)

    if getattr(args, "json", False):
        print(json.dumps(payload, indent=2, sort_keys=True))
    else:
        print_text(payload)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
