#!/usr/bin/env python3
# Version: v0.5.4
# Last updated: 2026-07-24
# Owner: PrecodeOS
# Created by Dan Sears / Recode.
# SPDX-License-Identifier: Apache-2.0
from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import tempfile
from pathlib import Path
from typing import Any


PUBLIC_FILE_GROUPS: list[dict[str, Any]] = [
    {"group": "active_memory", "paths": ["AGENT.md", "DECISIONS.md", "OPERATING-CONSTRAINTS.md"]},
    {"group": "active_work_state", "paths": ["tasks/todo.md"]},
    {"group": "candidate_queue", "paths": ["CANDIDATE-QUEUE.md"]},
    {
        "group": "product_and_project_owner_files",
        "paths": [
            "PRODUCT.md",
            "PROJECT-CONTEXT.md",
            "FEATURES.md",
            "ACCEPTANCE.md",
            "ARCHITECTURE.md",
            "API.md",
            "DATA-MODELS.md",
            "SECURITY.md",
            "CODEBASE-GUIDE.md",
        ],
    },
    {
        "group": "public_orientation_docs",
        "paths": [
            "README.md",
            "docs/",
            "docs-html/",
            "CONTRIBUTING.md",
            "GOVERNANCE.md",
            "TRADEMARK.md",
            "NOTICE",
            "LICENSE",
        ],
    },
    {
        "group": "agent_shims_and_adapters",
        "paths": ["AGENTS.md", "CLAUDE.md", "GEMINI.md", ".github/copilot-instructions.md", "adapters/"],
    },
    {
        "group": "work_structure",
        "paths": [
            "tasks/beads/BEAD-SCHEMA.md",
            "tasks/prds/PRD-000-template.md",
            "tasks/prds/PRD-SHARD-SCHEMA.md",
            "tasks/reference/",
            "tasks/templates/",
            "modes/",
            "memory/",
        ],
    },
    {"group": "project_evidence_guide", "paths": ["project-evidence/PROJECT-EVIDENCE-GUIDE.md"]},
    {"group": "scripts_and_checks", "paths": ["scripts/", ".githooks/", ".github/workflows/"]},
    {"group": "public_generated_log_guide", "paths": ["logs/LOG-EVIDENCE-TAXONOMY.md"]},
]

EXCLUDED_PATHS = [
    "private local planning material",
    "OS-HEALTH.md",
    "PRECODE-HELP.md",
    "PROGRESS.md",
    "logs/*.json",
    "logs/*.jsonl",
    "logs/*.yaml",
    "generated logs/*.md except logs/LOG-EVIDENCE-TAXONOMY.md",
    "logs/check-output/",
    "logs/scheduled-audit-output/",
    ".agent-state/",
    ".claude/",
    ".codex/",
    ".cursor/",
    ".vscode/",
    ".idea/",
    ".env",
    ".env.*",
    "secrets/",
    "credentials/",
    "key and certificate files",
    "__pycache__/",
    "test caches",
    "coverage output",
    "local virtual environments",
]

SOURCE_REQUIRED_PATHS = [
    "AGENT.md",
    "DECISIONS.md",
    "OPERATING-CONSTRAINTS.md",
    "tasks/todo.md",
    "docs/PRECODE-GUIDED-SETUP.md",
]
CONFLICT_PATHS = [
    "README.md",
    "CANDIDATE-QUEUE.md",
    "PRODUCT.md",
    "PROJECT-CONTEXT.md",
    "FEATURES.md",
    "ACCEPTANCE.md",
    "ARCHITECTURE.md",
    "API.md",
    "DATA-MODELS.md",
    "SECURITY.md",
    "CODEBASE-GUIDE.md",
    "AGENT.md",
    "DECISIONS.md",
    "tasks/todo.md",
    ".github/workflows",
    ".githooks",
]
MINIMAL_TARGET_NAMES = {".git", ".gitignore", "README.md", "LICENSE"}
STOP_CONDITIONS = [
    "source and target are unclear",
    "source and target resolve to the same folder",
    "source is not a plausible PrecodeOS package checkout",
    "target is missing",
    "target conflicts are present and unnamed",
    "the user has not approved any copying, hook installation, CI change, or owner-file adaptation",
    "generated bootstrap output is treated as permission to mutate",
]
ACTION_CATEGORIES = [
    "copy_candidate",
    "adapt_candidate",
    "preserve_existing",
    "exclude",
    "blocked",
    "deferred",
]
SETUP_PLAN_CATEGORIES = [
    "review_copy_candidate",
    "review_adaptation_candidate",
    "preserve_existing",
    "exclude",
    "blocked",
    "deferred",
]
DEFERRED_SETUP_PATHS = {
    ".githooks/",
    ".github/workflows/",
}
APPLY_ALLOWED_TARGET_KINDS = {"empty", "nearly_empty"}
OWNER_GROUPS = {"active_memory", "active_work_state", "product_and_project_owner_files"}
UPGRADE_DEFERRED_PATHS = {".githooks/", ".github/workflows/"}
SECRET_OR_LOCAL_PARTS = {
    ".agent-state",
    ".claude",
    ".codex",
    ".cursor",
    ".idea",
    ".vscode",
    "__pycache__",
}
SECRET_OR_LOCAL_NAMES = {
    ".env",
    "credentials",
    "secrets",
}
IDENTITY_FILE_RULES = {
    "tasks/prds/": {"field": "prd_id", "template": "tasks/prds/PRD-000-template.md", "schema": "tasks/prds/PRD-SHARD-SCHEMA.md"},
    "tasks/beads/": {"field": "bead_id", "schema": "tasks/beads/BEAD-SCHEMA.md"},
}


def resolve_candidate(raw: str) -> Path:
    return Path(raw).expanduser().resolve(strict=False)


def rel(path: Path, root: Path) -> str:
    return path.relative_to(root).as_posix()


def source_missing_paths(source: Path) -> list[str]:
    return [name for name in SOURCE_REQUIRED_PATHS if not (source / name).exists()]


def immediate_children(path: Path) -> list[Path]:
    if not path.is_dir():
        return []
    return sorted(path.iterdir(), key=lambda candidate: candidate.name)


def target_kind(source: Path, target: Path, source_exists: bool, target_exists: bool) -> str:
    if not target_exists:
        return "missing"
    if source_exists and source == target:
        return "same_as_source"
    children = immediate_children(target)
    names = {child.name for child in children}
    if not children:
        return "empty"
    if all(name in MINIMAL_TARGET_NAMES for name in names):
        return "nearly_empty"
    if all((target / name).exists() for name in ["AGENT.md", "DECISIONS.md", "tasks/todo.md"]):
        return "existing_precode"
    return "existing_project"


def target_conflicts(target: Path) -> list[dict[str, str]]:
    if not target.is_dir():
        return []
    conflicts: list[dict[str, str]] = []
    for name in CONFLICT_PATHS:
        candidate = target / name
        if candidate.exists():
            conflicts.append(
                {
                    "path": name,
                    "reason": "target already has this path; do not overwrite without explicit review",
                }
            )
    return conflicts


def dependency_status() -> list[str]:
    missing: list[str] = []
    if shutil.which("git") is None:
        missing.append("git")
    return missing


def file_digest(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---", 4)
    if end == -1:
        return {}
    values: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if ":" in line and not line.startswith(" "):
            key, value = line.split(":", 1)
            values[key.strip()] = value.strip().strip("'\"")
    return values


def identity_rule(relative_path: str) -> dict[str, str] | None:
    for prefix, rule in IDENTITY_FILE_RULES.items():
        if relative_path.startswith(prefix):
            return rule
    return None


def file_identity(root: Path, relative_path: str) -> tuple[str, str] | None:
    rule = identity_rule(relative_path)
    if rule is None:
        return None
    path = root / relative_path
    if not path.is_file():
        return None
    field = rule["field"]
    item_id = frontmatter(path.read_text(encoding="utf-8")).get(field, "").strip()
    if not item_id:
        return None
    return field, item_id


def identity_index(root: Path) -> dict[tuple[str, str], list[str]]:
    indexed: dict[tuple[str, str], list[str]] = {}
    for prefix in IDENTITY_FILE_RULES:
        directory = root / prefix.rstrip("/")
        if not directory.is_dir():
            continue
        for path in sorted(directory.glob("*.md")):
            if not path.is_file():
                continue
            relative_path = rel(path, root)
            identity = file_identity(root, relative_path)
            if identity is None:
                continue
            indexed.setdefault(identity, []).append(relative_path)
    return indexed


def upgrade_identity_collision(
    source_root: Path,
    target_identity: dict[tuple[str, str], list[str]],
    relative_path: str,
) -> dict[str, str] | None:
    identity = file_identity(source_root, relative_path)
    if identity is None:
        return None
    existing_paths = [path for path in target_identity.get(identity, []) if path != relative_path]
    if not existing_paths:
        return None
    field, item_id = identity
    return {
        "identity_field": field,
        "incoming_id": item_id,
        "incoming_path": relative_path,
        "existing_target_path": existing_paths[0],
    }


def is_package_dev_identity_path(relative_path: str) -> bool:
    if relative_path.startswith("tasks/prds/"):
        rule = IDENTITY_FILE_RULES["tasks/prds/"]
        return relative_path not in {rule["template"], rule["schema"]}
    if relative_path.startswith("tasks/beads/"):
        rule = IDENTITY_FILE_RULES["tasks/beads/"]
        return relative_path != rule["schema"]
    return False


def is_secret_or_local_path(relative_path: str) -> bool:
    parts = Path(relative_path).parts
    if any(part in SECRET_OR_LOCAL_PARTS for part in parts):
        return True
    return any(part in SECRET_OR_LOCAL_NAMES or part.startswith(".env") for part in parts)


def is_generated_log_path(relative_path: str) -> bool:
    if not relative_path.startswith("logs/"):
        return False
    return relative_path != "logs/LOG-EVIDENCE-TAXONOMY.md"


def is_deferred_setup_path(relative_path: str) -> bool:
    normalized = relative_path.rstrip("/") + ("/" if relative_path.endswith("/") else "")
    return any(normalized == path or normalized.startswith(path) for path in UPGRADE_DEFERRED_PATHS)


def iter_source_group_files(source_root: Path, group: dict[str, Any]) -> list[str]:
    files: list[str] = []
    for raw_path in group["paths"]:
        relative_path = str(raw_path)
        source_path = source_root / relative_path.rstrip("/")
        if relative_path.endswith("/"):
            if not source_path.is_dir():
                continue
            for candidate in sorted(source_path.rglob("*")):
                if not candidate.is_file():
                    continue
                candidate_relative = rel(candidate, source_root)
                if (
                    is_secret_or_local_path(candidate_relative)
                    or is_generated_log_path(candidate_relative)
                    or is_deferred_setup_path(candidate_relative)
                ):
                    continue
                files.append(candidate_relative)
        elif source_path.is_file():
            if (
                is_secret_or_local_path(relative_path)
                or is_generated_log_path(relative_path)
                or is_deferred_setup_path(relative_path)
            ):
                continue
            files.append(relative_path)
    return sorted(set(files))


def recommended_next_step(kind: str, source_missing: list[str], conflicts: list[dict[str, str]]) -> str:
    if source_missing:
        return "Stop and use a clean PrecodeOS package checkout before setup."
    if kind == "missing":
        return "Stop and identify or create the target project folder before setup."
    if kind == "same_as_source":
        return "Stop; do not treat the PrecodeOS package checkout as the target app."
    if kind in {"empty", "nearly_empty"}:
        return "Proceed to the new-project guided setup checklist after user approval."
    if kind == "existing_precode":
        return "Run memory validation in the target before deciding whether this is setup, repair, or update work."
    if conflicts:
        return "Review conflicts and proposed owner-file adaptations before copying anything."
    return "Proceed to existing-project guided setup review before copying anything."


def preview_action(category: str, path: str, reason: str, group: str | None = None) -> dict[str, str]:
    action = {"category": category, "path": path, "reason": reason}
    if group:
        action["group"] = group
    return action


def path_has_conflict(path: str, conflicts: list[dict[str, str]]) -> bool:
    normalized = path.rstrip("/")
    for conflict in conflicts:
        conflict_path = conflict["path"].rstrip("/")
        if normalized == conflict_path or normalized.startswith(f"{conflict_path}/"):
            return True
    return False


def build_manifest_preview(payload: dict[str, Any]) -> dict[str, Any]:
    kind = str(payload["target_kind"])
    blockers = list(payload["blockers"])
    conflicts = list(payload["conflicts"])
    source_missing = list(payload["source_missing_paths"])
    actions: list[dict[str, str]] = []

    if source_missing:
        actions.append(
            preview_action(
                "blocked",
                "<precode-package-root>",
                "source is not a plausible PrecodeOS checkout; use a clean package source before setup preview",
            )
        )
    if kind == "missing":
        actions.append(
            preview_action(
                "blocked",
                "<target-project-root>",
                "target path is missing; identify or create the target folder before setup preview",
            )
        )
    if kind == "same_as_source":
        actions.append(
            preview_action(
                "blocked",
                "<target-project-root>",
                "source and target are identical; never treat the package checkout as the target app",
            )
        )

    for excluded in payload["excluded_paths"]:
        actions.append(preview_action("exclude", str(excluded), "excluded from setup preview and copy plans"))

    for group in payload["public_file_groups"]:
        group_name = str(group["group"])
        for path in group["paths"]:
            path = str(path)
            if path in DEFERRED_SETUP_PATHS:
                actions.append(
                    preview_action(
                        "deferred",
                        path,
                        "hooks and CI require separate explicit approval and are not part of manifest preview setup",
                        group_name,
                    )
                )
                continue
            if kind == "existing_project":
                if path_has_conflict(path, conflicts):
                    actions.append(
                        preview_action(
                            "adapt_candidate",
                            path,
                            "target already has related material; preserve existing project truth and review adaptation after Existing Repo Intake",
                            group_name,
                        )
                    )
                else:
                    actions.append(
                        preview_action(
                            "deferred",
                            path,
                            "existing projects must run Existing Repo Intake before copy candidates become actionable",
                            group_name,
                        )
                    )
                continue
            if kind == "existing_precode":
                actions.append(
                    preview_action(
                        "preserve_existing",
                        path,
                        "target already appears to contain Precode active memory; validate before setup, repair, or update decisions",
                        group_name,
                    )
                )
                continue
            if kind in {"missing", "same_as_source"} or blockers:
                actions.append(preview_action("blocked", path, "blocked until source and target are valid", group_name))
                continue
            if path_has_conflict(path, conflicts):
                actions.append(
                    preview_action(
                        "adapt_candidate",
                        path,
                        "target already has this path; review before adapting or preserving",
                        group_name,
                    )
                )
            elif group_name == "product_and_project_owner_files":
                actions.append(
                    preview_action(
                        "adapt_candidate",
                        path,
                        "owner files need project-specific adaptation before first use",
                        group_name,
                    )
                )
            elif group_name == "active_work_state":
                actions.append(
                    preview_action(
                        "adapt_candidate",
                        path,
                        "fresh target active-work state must be created for this project, not copied from the package source",
                        group_name,
                    )
                )
            else:
                actions.append(
                    preview_action(
                        "copy_candidate",
                        path,
                        "candidate for supervised file-group copy after user approval",
                        group_name,
                    )
                )

    if kind == "existing_project":
        actions.append(
            preview_action(
                "deferred",
                "scripts/existing-repo-intake.py",
                "run Existing Repo Intake before copying, adapting owner files, changing CI, installing hooks, or editing app code",
            )
        )

    return {
        "manifest_kind": "install_update_dry_run_preview",
        "status": payload["status"],
        "source_root": payload["source_root"],
        "target_root": payload["target_root"],
        "target_kind": kind,
        "action_categories": ACTION_CATEGORIES,
        "actions": actions,
        "writes_by_default": False,
        "target_mutation_allowed": False,
        "generated_evidence_only": True,
        "not_authority_for": [
            "copying files",
            "overwriting target material",
            "installing hooks",
            "changing CI",
            "editing active memory",
            "running app commands",
            "writing app code",
            "release channels",
            "package-manager updates",
            "rollback automation",
        ],
        "next_setup_gate": "User must approve a separate supervised setup plan before any target mutation.",
    }


def setup_plan_action(
    action_id: str,
    category: str,
    path: str,
    reason: str,
    requires_user_approval: bool = True,
    group: str | None = None,
) -> dict[str, Any]:
    action: dict[str, Any] = {
        "id": action_id,
        "category": category,
        "path": path,
        "reason": reason,
        "requires_user_approval": requires_user_approval,
    }
    if group:
        action["group"] = group
    return action


def numbered_action(prefix: str, index: int, category: str, path: str, reason: str, group: str | None = None) -> dict[str, Any]:
    action: dict[str, Any] = {
        "id": f"{prefix}-{index:03d}",
        "category": category,
        "path": path,
        "reason": reason,
        "requires_user_approval": category.startswith("review_"),
    }
    if group:
        action["group"] = group
    return action


def build_existing_project_adaptation_plan(payload: dict[str, Any]) -> dict[str, Any]:
    kind = str(payload["target_kind"])
    target_root = Path(str(payload["target_root"]))
    blockers = list(payload["blockers"])
    if kind != "existing_project":
        blockers.append("existing-project adaptation planning applies only to existing project targets")

    actions: list[dict[str, Any]] = []
    action_index = 1
    for group in payload["public_file_groups"]:
        group_name = str(group["group"])
        for raw_path in group["paths"]:
            path = str(raw_path)
            target_path = target_root / path.rstrip("/")
            if group_name in OWNER_GROUPS:
                if target_path.exists():
                    category = "review_owner_adaptation_candidate"
                    reason = "target already owns this project surface; preserve project truth and adapt manually after Existing Repo Intake"
                else:
                    category = "review_owner_creation_candidate"
                    reason = "owner surface is missing; draft from Existing Repo Intake evidence and user confirmation before first implementation"
            elif path in DEFERRED_SETUP_PATHS:
                category = "deferred"
                reason = "hooks and CI require separate explicit approval and are not part of adaptation planning"
            elif target_path.exists() or path_has_conflict(path, payload["conflicts"]):
                category = "preserve_existing"
                reason = "target material exists; preserve it until the user approves a package/setup decision"
            else:
                category = "deferred"
                reason = "existing projects must complete intake and owner-file review before package copying becomes actionable"
            actions.append(numbered_action("EA", action_index, category, path, reason, group_name))
            action_index += 1

    return {
        "plan_kind": "existing_project_adaptation_plan",
        "status": "blocked" if blockers else payload["status"],
        "source_root": payload["source_root"],
        "target_root": payload["target_root"],
        "target_kind": kind,
        "actions": actions,
        "approval_gates": [
            "Run Existing Repo Intake and review its evidence before editing owner files.",
            "User confirms which existing project facts belong in Precode owner files.",
            "User approves each owner-file creation or adaptation separately.",
            "Package file copying, hooks, CI, app commands, and app-code edits remain separate decisions.",
        ],
        "blockers": blockers,
        "target_mutation_allowed": False,
        "generated_evidence_only": True,
        "not_authority_for": [
            "copying files",
            "overwriting target material",
            "owner-file edits",
            "installing hooks",
            "changing CI",
            "running app commands",
            "writing app code",
            "package updates",
            "rollback automation",
        ],
        "next_manual_gate": "User must approve specific owner-file adaptation work after Existing Repo Intake.",
    }


def build_upgrade_preview(payload: dict[str, Any]) -> dict[str, Any]:
    source_root = Path(str(payload["source_root"]))
    target_root = Path(str(payload["target_root"]))
    kind = str(payload["target_kind"])
    blockers = list(payload["blockers"])
    if kind != "existing_precode":
        blockers.append("upgrade preview applies only to targets that already contain Precode active memory")

    actions: list[dict[str, Any]] = []
    dirty_package: list[str] = []
    dirty_owner: list[str] = []
    missing_package: list[str] = []
    identity_collisions: list[dict[str, str]] = []
    deferred_identity_paths: list[str] = []
    target_identity = identity_index(target_root)
    action_paths: set[str] = set()
    action_index = 1

    for group in payload["public_file_groups"]:
        group_name = str(group["group"])
        if group_name in OWNER_GROUPS:
            candidate_paths = [str(path) for path in group["paths"]]
        else:
            candidate_paths = iter_source_group_files(source_root, group)
        for path in candidate_paths:
            source_path = source_root / path.rstrip("/")
            target_path = target_root / path.rstrip("/")
            if group_name in OWNER_GROUPS:
                if not target_path.exists():
                    dirty_owner.append(path)
                    category = "review_owner_creation_candidate"
                    reason = "owner or active-memory surface is missing; create only after user confirms target project truth"
                elif source_path.is_file() and target_path.is_file() and file_digest(source_path) != file_digest(target_path):
                    dirty_owner.append(path)
                    category = "preserve_owner_edit"
                    reason = "target owner or active-memory surface differs from package template; preserve and review manually"
                else:
                    category = "preserve_existing"
                    reason = "target owner or active-memory surface is present; preserve during package upgrade"
            elif not source_path.exists():
                continue
            elif is_deferred_setup_path(path):
                category = "deferred"
                reason = "hooks and CI require separate explicit approval and are not part of upgrade preview"
            elif not target_path.exists():
                identity_collision = upgrade_identity_collision(source_root, target_identity, path)
                if identity_collision:
                    identity_collisions.append(identity_collision)
                    category = "blocked_identity_collision"
                    reason = (
                        f"incoming {identity_collision['identity_field']} {identity_collision['incoming_id']} "
                        f"already exists at {identity_collision['existing_target_path']}; preserve target identity and do not copy"
                    )
                elif is_package_dev_identity_path(path):
                    deferred_identity_paths.append(path)
                    category = "deferred_package_dev_identity"
                    reason = (
                        "package dev PRD/bead files are not upgrade-copy candidates for existing Precode targets; "
                        "preserve target PRDs/beads"
                    )
                else:
                    missing_package.append(path)
                    category = "review_package_copy_candidate"
                    reason = "package-owned file is missing in the target and may be copied after explicit action approval"
            elif not source_path.is_file() or not target_path.is_file():
                dirty_package.append(path)
                category = "manual_package_review"
                reason = "source and target path types differ; review manually before any package update"
            elif file_digest(source_path) == file_digest(target_path):
                category = "current"
                reason = "target package-owned file matches the source package"
            else:
                dirty_package.append(path)
                category = "manual_package_review"
                reason = "target package-owned file differs from source; do not overwrite without a separate reviewed update decision"
            action = numbered_action("UP", action_index, category, path, reason, group_name)
            if category == "blocked_identity_collision":
                action.update(identity_collision)
            actions.append(action)
            action_paths.add(path)
            action_index += 1

    for source_identity_paths in identity_index(source_root).values():
        for path in sorted(source_identity_paths):
            if path in action_paths or not is_package_dev_identity_path(path):
                continue
            source_path = source_root / path
            target_path = target_root / path
            if not source_path.exists():
                continue
            if not target_path.exists():
                identity_collision = upgrade_identity_collision(source_root, target_identity, path)
                if identity_collision:
                    identity_collisions.append(identity_collision)
                    category = "blocked_identity_collision"
                    reason = (
                        f"incoming {identity_collision['identity_field']} {identity_collision['incoming_id']} "
                        f"already exists at {identity_collision['existing_target_path']}; preserve target identity and do not copy"
                    )
                else:
                    deferred_identity_paths.append(path)
                    category = "deferred_package_dev_identity"
                    reason = (
                        "package dev PRD/bead files are not upgrade-copy candidates for existing Precode targets; "
                        "preserve target PRDs/beads"
                    )
            else:
                category = "preserve_existing"
                reason = "target package development PRD/bead identity path is present; preserve during package upgrade"
            action = numbered_action("UP", action_index, category, path, reason, "package_dev_identity")
            if category == "blocked_identity_collision":
                action.update(identity_collision)
            actions.append(action)
            action_paths.add(path)
            action_index += 1

    if blockers:
        classification = "blocked"
    elif dirty_package and dirty_owner:
        classification = "mixed_or_unknown"
    elif dirty_package:
        classification = "dirty_package_edits"
    elif dirty_owner:
        classification = "dirty_project_or_owner_edits"
    else:
        classification = "clean"

    return {
        "preview_kind": "package_upgrade_preview",
        "status": (
            "blocked"
            if blockers
            else "warning"
            if dirty_package or dirty_owner or missing_package or identity_collisions or deferred_identity_paths
            else "pass"
        ),
        "source_root": payload["source_root"],
        "target_root": payload["target_root"],
        "target_kind": kind,
        "package_state_classification": classification,
        "actions": actions,
        "dirty_package_paths": dirty_package,
        "dirty_project_or_owner_paths": dirty_owner,
        "missing_package_paths": missing_package,
        "identity_collisions": identity_collisions,
        "deferred_package_dev_identity_paths": deferred_identity_paths,
        "blockers": blockers,
        "writes_by_default": False,
        "target_mutation_allowed": False,
        "generated_evidence_only": True,
        "not_authority_for": [
            "package update permission",
            "overwriting target material",
            "owner-file adaptation",
            "installing hooks",
            "changing CI",
            "release channels",
            "package-manager updates",
            "rollback automation",
        ],
        "next_setup_gate": "Only missing package-owned files marked review_package_copy_candidate may be copied with explicit action approval; dirty files require manual review and identity collisions block copying.",
    }


def build_recovery_guidance(payload: dict[str, Any]) -> dict[str, Any]:
    kind = str(payload["target_kind"])
    blockers = list(payload["blockers"])
    if kind == "existing_precode":
        path = "Validate active memory, run upgrade preview, then decide whether this is repair, package update, or normal Precode work."
    elif kind == "existing_project":
        path = "Run Existing Repo Intake, preserve current project truth, and plan owner-file adaptation before any setup mutation."
    elif kind in {"empty", "nearly_empty"}:
        path = "Use supervised setup plan and apply only explicitly approved fresh-target copy actions."
    elif kind == "same_as_source":
        path = "Stop; source and target are the same folder. Pick the target project before any setup or recovery work."
    elif kind == "missing":
        path = "Stop; identify or create the target folder before recovery continues."
    else:
        path = "Stop and clarify source, target, and target state before recovery continues."
    return {
        "guidance_kind": "bootstrap_recovery_guidance",
        "status": "blocked" if blockers else payload["status"],
        "source_root": payload["source_root"],
        "target_root": payload["target_root"],
        "target_kind": kind,
        "likely_recovery_path": path,
        "support_steps": [
            "Confirm source and target folders before interpreting setup state.",
            "Inspect target git status before approving any mutation.",
            "Use preview or intake evidence to name the smallest safe next action.",
            "Ask for explicit approval before copying, adapting, deleting, overwriting, installing hooks, or changing CI.",
        ],
        "validation_next_steps": [
            "Run `bash scripts/validate-memory.sh` in an existing Precode target when active memory is present.",
            "Run `python3 scripts/file-inventory.py --check` only after package files exist in the installed Precode root.",
            "Run target-specific checks only after owner files name them.",
        ],
        "forbidden_actions": [
            "do not automate rollback",
            "do not run destructive cleanup",
            "do not overwrite dirty package or owner files",
            "do not install hooks or change CI silently",
            "do not treat generated preview output as authority",
        ],
        "target_mutation_allowed": False,
        "generated_evidence_only": True,
    }


def validation_steps_for_plan(kind: str) -> list[str]:
    if kind in {"empty", "nearly_empty"}:
        return [
            "After approved manual setup, inspect target git status.",
            "After Precode files exist, run `bash scripts/validate-memory.sh` from the installed Precode root.",
            "When package files are present, run `python3 scripts/file-inventory.py --check` from the installed Precode root.",
            "Run target-specific project checks only after owner files name them.",
        ]
    if kind == "existing_project":
        return [
            "Run `python3 scripts/existing-repo-intake.py --source <precode-package-root> --target <target-project-root>` before copying or adapting Precode files.",
            "Review conflicts, owner-file gaps, likely checks, sensitive surfaces, and stop conditions before proposing setup mutation.",
        ]
    if kind == "existing_precode":
        return [
            "Run `bash scripts/validate-memory.sh` in the target before deciding whether this is setup, repair, or update work.",
            "Use troubleshooting or recovery guidance if active memory is invalid.",
        ]
    return [
        "Resolve blockers before setup planning continues.",
    ]


def build_supervised_setup_plan(payload: dict[str, Any]) -> dict[str, Any]:
    kind = str(payload["target_kind"])
    preview = payload.get("install_update_preview") or build_manifest_preview(payload)
    blockers = list(payload["blockers"])
    actions: list[dict[str, Any]] = []
    action_index = 1

    if kind == "existing_project":
        blockers.append("existing projects must run Existing Repo Intake before setup actions become actionable")
    if kind == "existing_precode":
        blockers.append("target already appears to contain Precode active memory; validate before setup, repair, or update decisions")

    for preview_item in preview["actions"]:
        category = str(preview_item["category"])
        path = str(preview_item["path"])
        group = preview_item.get("group")
        reason = str(preview_item["reason"])

        plan_category = {
            "copy_candidate": "review_copy_candidate",
            "adapt_candidate": "review_adaptation_candidate",
            "preserve_existing": "preserve_existing",
            "exclude": "exclude",
            "blocked": "blocked",
            "deferred": "deferred",
        }[category]

        if kind == "existing_project" and plan_category in {"review_copy_candidate", "review_adaptation_candidate"}:
            plan_category = "deferred"
            reason = "existing projects must run Existing Repo Intake and conflict review before this setup action becomes actionable"

        if kind == "existing_precode" and plan_category in {"review_copy_candidate", "review_adaptation_candidate"}:
            plan_category = "preserve_existing"
            reason = "existing Precode material should be preserved until memory validation determines setup, repair, or update scope"

        action_id = f"SP-{action_index:03d}"
        action_index += 1
        actions.append(
            setup_plan_action(
                action_id=action_id,
                category=plan_category,
                path=path,
                reason=reason,
                requires_user_approval=plan_category not in {"exclude", "blocked", "deferred"},
                group=str(group) if group else None,
            )
        )

    approval_gates = [
        "User confirms the PrecodeOS package source and target project folder.",
        "User reviews excluded paths and secret boundaries.",
        "User approves each file group before any manual copying.",
        "User approves each owner-file adaptation before editing.",
        "Git hooks and CI changes require separate explicit approval and remain deferred in this slice.",
        "Active memory is validated before first implementation work.",
    ]
    if kind == "existing_project":
        approval_gates.insert(2, "Existing Repo Intake runs and conflicts are reviewed before copy or adaptation is proposed.")
    if kind == "existing_precode":
        approval_gates.insert(2, "Target memory validation runs before setup, repair, or update is chosen.")

    return {
        "plan_kind": "supervised_setup_plan",
        "status": "blocked" if blockers else payload["status"],
        "source_root": payload["source_root"],
        "target_root": payload["target_root"],
        "target_kind": kind,
        "actions": actions,
        "approval_gates": approval_gates,
        "excluded_paths": payload["excluded_paths"],
        "blockers": blockers,
        "validation_steps": validation_steps_for_plan(kind),
        "target_mutation_allowed": False,
        "generated_evidence_only": True,
        "not_authority_for": [
            "copying files",
            "overwriting target material",
            "owner-file adaptation",
            "installing hooks",
            "changing CI",
            "editing active memory",
            "running app commands",
            "writing app code",
            "release channels",
            "package-manager updates",
            "rollback automation",
            "installable precode CLI",
        ],
        "next_manual_gate": "User must approve a separate manual setup action before any target mutation.",
    }


def safe_copy_path(source_root: Path, target_root: Path, relative_path: str) -> dict[str, str]:
    source_path = source_root / relative_path.rstrip("/")
    target_path = target_root / relative_path.rstrip("/")

    if not source_path.exists():
        return {"path": relative_path, "reason": "source path is missing"}
    if target_path.exists():
        return {"path": relative_path, "reason": "target path already exists; refusing to overwrite"}

    target_path.parent.mkdir(parents=True, exist_ok=True)
    if source_path.is_dir():
        shutil.copytree(source_path, target_path)
    else:
        shutil.copy2(source_path, target_path)
    return {"path": relative_path, "reason": "copied approved setup action"}


def apply_supervised_setup(payload: dict[str, Any], approved_action_ids: list[str]) -> dict[str, Any]:
    if "supervised_setup_plan" not in payload:
        raise ValueError("supervised setup apply requires --supervised-setup-plan")

    source_root = Path(str(payload["source_root"]))
    target_root = Path(str(payload["target_root"]))
    plan = payload["supervised_setup_plan"]
    approved = set(approved_action_ids)
    copied: list[dict[str, str]] = []
    skipped: list[dict[str, str]] = []
    blocked: list[dict[str, str]] = []

    if not approved:
        blocked.append({"path": "<approval>", "reason": "at least one --approve-action ID is required"})

    if payload["target_kind"] not in APPLY_ALLOWED_TARGET_KINDS:
        blocked.append(
            {
                "path": "<target-project-root>",
                "reason": "supervised setup apply is limited to empty or nearly empty targets",
            }
        )

    if payload["blockers"] or plan["blockers"]:
        for blocker in payload["blockers"] + plan["blockers"]:
            blocked.append({"path": "<setup>", "reason": str(blocker)})

    plan_actions = {str(action["id"]): action for action in plan["actions"]}
    for action_id in sorted(approved):
        action = plan_actions.get(action_id)
        if action is None:
            blocked.append({"path": action_id, "reason": "approved action ID is not present in the setup plan"})
            continue
        if action["category"] != "review_copy_candidate":
            blocked.append(
                {
                    "path": str(action["path"]),
                    "reason": f"{action_id} is {action['category']}; apply only supports review_copy_candidate actions",
                }
            )

    if not blocked:
        for action_id in sorted(approved):
            action = plan_actions[action_id]
            path = str(action["path"])
            source_path = source_root / path.rstrip("/")
            target_path = target_root / path.rstrip("/")
            if not source_path.exists():
                blocked.append({"path": path, "reason": "source path is missing"})
            if target_path.exists():
                blocked.append({"path": path, "reason": "target path already exists; refusing to overwrite"})

    apply_allowed = not blocked
    for action in plan["actions"]:
        action_id = str(action["id"])
        path = str(action["path"])
        if action_id not in approved:
            skipped.append({"path": path, "reason": f"{action_id} was not approved"})
            continue
        if action["category"] != "review_copy_candidate":
            continue
        if not apply_allowed:
            skipped.append({"path": path, "reason": "apply blocked before mutation"})
            continue
        result = safe_copy_path(source_root, target_root, path)
        if result["reason"].startswith("copied"):
            copied.append(result)
        else:
            blocked.append(result)

    status = "blocked" if blocked else "applied"
    return {
        "apply_kind": "supervised_setup_apply",
        "status": status,
        "source_root": payload["source_root"],
        "target_root": payload["target_root"],
        "target_kind": payload["target_kind"],
        "approved_actions": sorted(approved),
        "copied": copied,
        "skipped": skipped,
        "blocked": blocked,
        "validation_next_step": (
            "Inspect target git status, then run `bash scripts/validate-memory.sh` from the installed Precode root after copied files are present."
            if status == "applied"
            else "Resolve blockers and rerun the supervised setup plan before applying setup actions."
        ),
        "target_mutation_allowed": status == "applied",
        "not_authority_for": [
            "owner-file adaptation",
            "overwriting target material",
            "installing hooks",
            "changing CI",
            "running app commands",
            "writing app code",
            "release channels",
            "package-manager updates",
            "rollback automation",
            "installable precode CLI",
        ],
    }


def apply_upgrade_preview(payload: dict[str, Any], approved_action_ids: list[str]) -> dict[str, Any]:
    if "package_upgrade_preview" not in payload:
        raise ValueError("upgrade apply requires --upgrade-preview")

    source_root = Path(str(payload["source_root"]))
    target_root = Path(str(payload["target_root"]))
    preview = payload["package_upgrade_preview"]
    approved = set(approved_action_ids)
    copied: list[dict[str, str]] = []
    skipped: list[dict[str, str]] = []
    blocked: list[dict[str, str]] = []

    if not approved:
        blocked.append({"path": "<approval>", "reason": "at least one --approve-action ID is required"})
    if payload["target_kind"] != "existing_precode":
        blocked.append({"path": "<target-project-root>", "reason": "upgrade apply is limited to existing Precode targets"})
    if preview["package_state_classification"] in {"dirty_package_edits", "mixed_or_unknown", "blocked"}:
        blocked.append(
            {
                "path": "<upgrade>",
                "reason": f"upgrade apply refuses dirty or unknown package state: {preview['package_state_classification']}",
            }
        )
    if payload["blockers"] or preview["blockers"]:
        for blocker in payload["blockers"] + preview["blockers"]:
            blocked.append({"path": "<upgrade>", "reason": str(blocker)})

    preview_actions = {str(action["id"]): action for action in preview["actions"]}
    for action_id in sorted(approved):
        action = preview_actions.get(action_id)
        if action is None:
            blocked.append({"path": action_id, "reason": "approved action ID is not present in the upgrade preview"})
            continue
        if action["category"] == "blocked_identity_collision":
            blocked.append(
                {
                    "path": str(action["path"]),
                    "reason": (
                        f"{action_id} has identity collision {action.get('incoming_id', '')}; "
                        "upgrade apply refuses incoming PRD/bead IDs that already exist in the target"
                    ),
                }
            )
            continue
        if action["category"] != "review_package_copy_candidate":
            blocked.append(
                {
                    "path": str(action["path"]),
                    "reason": f"{action_id} is {action['category']}; upgrade apply only supports review_package_copy_candidate actions",
                }
            )

    if not blocked:
        for action_id in sorted(approved):
            action = preview_actions[action_id]
            path = str(action["path"])
            source_path = source_root / path.rstrip("/")
            target_path = target_root / path.rstrip("/")
            if not source_path.is_file():
                blocked.append({"path": path, "reason": "source package file is missing or is not a file"})
            if target_path.exists():
                blocked.append({"path": path, "reason": "target path already exists; refusing to overwrite during upgrade apply"})

    apply_allowed = not blocked
    for action in preview["actions"]:
        action_id = str(action["id"])
        path = str(action["path"])
        if action_id not in approved:
            skipped.append({"path": path, "reason": f"{action_id} was not approved"})
            continue
        if action["category"] != "review_package_copy_candidate":
            continue
        if not apply_allowed:
            skipped.append({"path": path, "reason": "upgrade apply blocked before mutation"})
            continue
        result = safe_copy_path(source_root, target_root, path)
        if result["reason"].startswith("copied"):
            copied.append(result)
        else:
            blocked.append(result)

    status = "blocked" if blocked else "applied"
    return {
        "apply_kind": "package_upgrade_apply",
        "status": status,
        "source_root": payload["source_root"],
        "target_root": payload["target_root"],
        "target_kind": payload["target_kind"],
        "approved_actions": sorted(approved),
        "copied": copied,
        "skipped": skipped,
        "blocked": blocked,
        "validation_next_step": (
            "Inspect target git status, run `bash scripts/validate-memory.sh`, and rerun package upgrade preview."
            if status == "applied"
            else "Resolve blockers and rerun package upgrade preview before applying package copy actions."
        ),
        "target_mutation_allowed": status == "applied",
        "not_authority_for": [
            "overwriting target material",
            "dirty package-file replacement",
            "owner-file adaptation",
            "installing hooks",
            "changing CI",
            "release channels",
            "package-manager updates",
            "rollback automation",
        ],
    }


def build_payload(source_raw: str, target_raw: str) -> dict[str, Any]:
    source = resolve_candidate(source_raw)
    target = resolve_candidate(target_raw)
    source_exists = source.is_dir()
    target_exists = target.is_dir()
    missing_source_paths = source_missing_paths(source) if source_exists else SOURCE_REQUIRED_PATHS.copy()
    kind = target_kind(source, target, source_exists, target_exists)
    conflicts = target_conflicts(target)
    missing_dependencies = dependency_status()

    blockers: list[str] = []
    warnings: list[str] = []

    if not source_exists:
        blockers.append("source path does not exist or is not a directory")
    elif missing_source_paths:
        blockers.append("source is not a plausible PrecodeOS package checkout")
    if not target_exists:
        blockers.append("target path does not exist or is not a directory")
    if kind == "same_as_source":
        blockers.append("source and target resolve to the same folder")
    if conflicts and kind != "existing_precode":
        warnings.append("target has files that may conflict with Precode setup")
    if missing_dependencies:
        warnings.append("recommended local dependencies are missing")

    status = "blocked" if blockers else "warning" if warnings else "pass"
    payload = {
        "tool": "bootstrap-check",
        "status": status,
        "warnings": warnings,
        "blockers": blockers,
        "source_root": source.as_posix(),
        "target_root": target.as_posix(),
        "source_missing_paths": missing_source_paths,
        "target_kind": kind,
        "public_file_groups": PUBLIC_FILE_GROUPS,
        "excluded_paths": EXCLUDED_PATHS,
        "conflicts": conflicts,
        "missing_dependencies": missing_dependencies,
        "recommended_next_step": recommended_next_step(kind, missing_source_paths, conflicts),
        "stop_conditions": STOP_CONDITIONS,
        "writes_by_default": False,
        "generated_evidence_only": True,
        "target_mutation_allowed": False,
        "deferred": [
            "mutating installer",
            "installable precode CLI",
            "package-manager release channels",
            "full install/update manifest",
            "Git hook installation",
            "CI mutation",
            "app-code edits",
        ],
    }
    return payload


def render_plain(payload: dict[str, Any]) -> str:
    lines = [
        f"Bootstrap Confidence: {payload['status']}",
        f"- Source: `{payload['source_root']}`",
        f"- Target: `{payload['target_root']}`",
        f"- Target kind: `{payload['target_kind']}`",
        f"- Recommended next step: {payload['recommended_next_step']}",
        "- Read-only default: yes; this command does not copy, edit, install hooks, change CI, or write app code.",
    ]
    if payload["blockers"]:
        lines.append("\nBlockers:")
        lines.extend(f"- {item}" for item in payload["blockers"])
    if payload["warnings"]:
        lines.append("\nWarnings:")
        lines.extend(f"- {item}" for item in payload["warnings"])
    if payload["source_missing_paths"]:
        lines.append("\nSource missing paths:")
        lines.extend(f"- `{item}`" for item in payload["source_missing_paths"])
    if payload["conflicts"]:
        lines.append("\nTarget conflicts:")
        for conflict in payload["conflicts"]:
            lines.append(f"- `{conflict['path']}`: {conflict['reason']}")
    if payload["missing_dependencies"]:
        lines.append("\nMissing dependencies:")
        lines.extend(f"- `{item}`" for item in payload["missing_dependencies"])
    lines.append("\nPublic file groups:")
    for group in payload["public_file_groups"]:
        lines.append(f"- {group['group']}: {', '.join(group['paths'])}")
    lines.append("\nExcluded paths:")
    lines.extend(f"- `{item}`" for item in payload["excluded_paths"])
    lines.append("\nStop if:")
    lines.extend(f"- {item}" for item in payload["stop_conditions"])
    lines.append("\nGenerated-report warning: bootstrap output is evidence only, not permission to mutate.")
    return "\n".join(lines)


def render_preview_plain(payload: dict[str, Any]) -> str:
    preview = payload["install_update_preview"]
    lines = [
        render_plain(payload),
        "\nInstall/Update Manifest Dry-Run Preview:",
        f"- Preview kind: `{preview['manifest_kind']}`",
        "- Target mutation allowed: no",
        "- Writes by default: no",
        "- This preview is not a release channel, package-manager update, rollback plan, CLI contract, or install permission.",
        f"- Next setup gate: {preview['next_setup_gate']}",
        "\nPreview actions:",
    ]
    for action in preview["actions"]:
        group = f" ({action['group']})" if "group" in action else ""
        lines.append(f"- {action['category']}: `{action['path']}`{group} -- {action['reason']}")
    lines.append(
        "\nPreview warning: dry-run actions are evidence only; they do not approve copying, overwriting, hooks, CI, active-memory edits, app commands, or app-code edits."
    )
    return "\n".join(lines)


def render_setup_plan_plain(payload: dict[str, Any]) -> str:
    plan = payload["supervised_setup_plan"]
    lines = [
        render_preview_plain(payload),
        "\nSupervised Setup Plan:",
        f"- Plan kind: `{plan['plan_kind']}`",
        f"- Plan status: `{plan['status']}`",
        "- Target mutation allowed: no",
        "- Generated evidence only: yes",
        "- This plan is not an installer, update command, release channel, package-manager operation, rollback plan, CLI contract, copy approval, or edit approval.",
        f"- Next manual gate: {plan['next_manual_gate']}",
    ]
    if plan["blockers"]:
        lines.append("\nSetup-plan blockers:")
        lines.extend(f"- {item}" for item in plan["blockers"])
    lines.append("\nApproval gates:")
    lines.extend(f"- {item}" for item in plan["approval_gates"])
    lines.append("\nSetup-plan actions:")
    for action in plan["actions"]:
        group = f" ({action['group']})" if "group" in action else ""
        approval = "approval required" if action["requires_user_approval"] else "not actionable"
        lines.append(f"- {action['id']} {action['category']}: `{action['path']}`{group} -- {action['reason']} [{approval}]")
    lines.append("\nValidation steps:")
    lines.extend(f"- {item}" for item in plan["validation_steps"])
    lines.append(
        "\nSetup-plan warning: this checklist is evidence only; it does not approve copying, overwriting, owner-file edits, hooks, CI, active-memory edits, app commands, or app-code edits."
    )
    return "\n".join(lines)


def render_apply_plain(payload: dict[str, Any]) -> str:
    summary = payload["supervised_setup_apply"]
    lines = [
        render_setup_plan_plain(payload),
        "\nSupervised Setup Apply Summary:",
        f"- Apply kind: `{summary['apply_kind']}`",
        f"- Apply status: `{summary['status']}`",
        "- Scope: approved setup-plan copy actions for empty or nearly empty targets only.",
        "- This apply mode does not adapt owner files, overwrite target material, install hooks, change CI, run app commands, write app code, define release channels, provide rollback automation, install a CLI, or provide package-manager behavior.",
    ]
    if summary["copied"]:
        lines.append("\nCopied:")
        lines.extend(f"- `{item['path']}`: {item['reason']}" for item in summary["copied"])
    if summary["skipped"]:
        lines.append("\nSkipped:")
        lines.extend(f"- `{item['path']}`: {item['reason']}" for item in summary["skipped"])
    if summary["blocked"]:
        lines.append("\nBlocked:")
        lines.extend(f"- `{item['path']}`: {item['reason']}" for item in summary["blocked"])
    lines.append(f"\nValidation next step: {summary['validation_next_step']}")
    return "\n".join(lines)


def render_existing_project_adaptation_plain(payload: dict[str, Any]) -> str:
    plan = payload["existing_project_adaptation_plan"]
    lines = [
        render_setup_plan_plain(payload) if "supervised_setup_plan" in payload else render_preview_plain(payload) if "install_update_preview" in payload else render_plain(payload),
        "\nExisting Project Adaptation Plan:",
        f"- Plan kind: `{plan['plan_kind']}`",
        f"- Plan status: `{plan['status']}`",
        "- Target mutation allowed: no",
        "- Generated evidence only: yes",
        "- This plan is not copy approval, owner-file edit approval, package update permission, hook/CI setup, app-code permission, or rollback approval.",
        f"- Next manual gate: {plan['next_manual_gate']}",
    ]
    if plan["blockers"]:
        lines.append("\nAdaptation-plan blockers:")
        lines.extend(f"- {item}" for item in plan["blockers"])
    lines.append("\nApproval gates:")
    lines.extend(f"- {item}" for item in plan["approval_gates"])
    lines.append("\nAdaptation-plan actions:")
    for action in plan["actions"]:
        group = f" ({action['group']})" if "group" in action else ""
        approval = "approval required" if action["requires_user_approval"] else "not actionable"
        lines.append(f"- {action['id']} {action['category']}: `{action['path']}`{group} -- {action['reason']} [{approval}]")
    return "\n".join(lines)


def render_upgrade_preview_plain(payload: dict[str, Any]) -> str:
    preview = payload["package_upgrade_preview"]
    lines = [
        render_plain(payload),
        "\nPackage Upgrade Preview:",
        f"- Preview kind: `{preview['preview_kind']}`",
        f"- Preview status: `{preview['status']}`",
        f"- Package state classification: `{preview['package_state_classification']}`",
        "- Target mutation allowed: no",
        "- Writes by default: no",
        "- This preview is not package update permission, overwrite approval, owner-file adaptation, release-channel metadata, package-manager behavior, hook/CI setup, or rollback automation.",
        f"- Next setup gate: {preview['next_setup_gate']}",
    ]
    if preview["blockers"]:
        lines.append("\nUpgrade-preview blockers:")
        lines.extend(f"- {item}" for item in preview["blockers"])
    if preview["dirty_package_paths"]:
        lines.append("\nDirty package paths requiring manual review:")
        lines.extend(f"- `{item}`" for item in preview["dirty_package_paths"])
    if preview["dirty_project_or_owner_paths"]:
        lines.append("\nProject or owner paths to preserve/review:")
        lines.extend(f"- `{item}`" for item in preview["dirty_project_or_owner_paths"])
    if preview["identity_collisions"]:
        lines.append("\nIdentity collisions blocking copy:")
        for item in preview["identity_collisions"]:
            lines.append(
                f"- `{item['incoming_path']}` declares `{item['incoming_id']}`, already present at `{item['existing_target_path']}`"
            )
    if preview["deferred_package_dev_identity_paths"]:
        lines.append("\nPackage dev PRDs/beads deferred:")
        lines.extend(f"- `{item}`" for item in preview["deferred_package_dev_identity_paths"])
    lines.append("\nUpgrade-preview actions:")
    for action in preview["actions"]:
        group = f" ({action['group']})" if "group" in action else ""
        approval = "approval required" if action["requires_user_approval"] else "not actionable"
        lines.append(f"- {action['id']} {action['category']}: `{action['path']}`{group} -- {action['reason']} [{approval}]")
    lines.append(
        "\nUpgrade warning: only missing package-owned files marked review_package_copy_candidate can be copied by apply mode; dirty files require manual review."
    )
    return "\n".join(lines)


def render_upgrade_apply_plain(payload: dict[str, Any]) -> str:
    summary = payload["package_upgrade_apply"]
    lines = [
        render_upgrade_preview_plain(payload),
        "\nPackage Upgrade Apply Summary:",
        f"- Apply kind: `{summary['apply_kind']}`",
        f"- Apply status: `{summary['status']}`",
        "- Scope: approved missing package-owned files only.",
        "- This apply mode does not overwrite dirty files, adapt owner files, install hooks, change CI, define release channels, provide rollback automation, or provide package-manager behavior.",
    ]
    if summary["copied"]:
        lines.append("\nCopied:")
        lines.extend(f"- `{item['path']}`: {item['reason']}" for item in summary["copied"])
    if summary["skipped"]:
        lines.append("\nSkipped:")
        lines.extend(f"- `{item['path']}`: {item['reason']}" for item in summary["skipped"])
    if summary["blocked"]:
        lines.append("\nBlocked:")
        lines.extend(f"- `{item['path']}`: {item['reason']}" for item in summary["blocked"])
    lines.append(f"\nValidation next step: {summary['validation_next_step']}")
    return "\n".join(lines)


def render_recovery_guidance_plain(payload: dict[str, Any]) -> str:
    guidance = payload["bootstrap_recovery_guidance"]
    lines = [
        render_plain(payload),
        "\nBootstrap Recovery Guidance:",
        f"- Guidance kind: `{guidance['guidance_kind']}`",
        f"- Guidance status: `{guidance['status']}`",
        f"- Likely recovery path: {guidance['likely_recovery_path']}",
        "- Target mutation allowed: no",
        "- Generated evidence only: yes",
        "\nSupport steps:",
    ]
    lines.extend(f"- {item}" for item in guidance["support_steps"])
    lines.append("\nValidation next steps:")
    lines.extend(f"- {item}" for item in guidance["validation_next_steps"])
    lines.append("\nForbidden actions:")
    lines.extend(f"- {item}" for item in guidance["forbidden_actions"])
    return "\n".join(lines)


def write_evidence(payload: dict[str, Any]) -> None:
    source = Path(str(payload["source_root"]))
    logs = source / "logs"
    logs.mkdir(parents=True, exist_ok=True)
    (logs / "bootstrap-check.json").write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    if "package_upgrade_apply" in payload:
        renderer = render_upgrade_apply_plain
    elif "package_upgrade_preview" in payload:
        renderer = render_upgrade_preview_plain
    elif "existing_project_adaptation_plan" in payload:
        renderer = render_existing_project_adaptation_plain
    elif "bootstrap_recovery_guidance" in payload:
        renderer = render_recovery_guidance_plain
    elif "supervised_setup_plan" in payload:
        renderer = render_apply_plain if "supervised_setup_apply" in payload else render_setup_plan_plain
    elif "install_update_preview" in payload:
        renderer = render_preview_plain
    else:
        renderer = render_plain
    (logs / "bootstrap-check.md").write_text(renderer(payload) + "\n", encoding="utf-8")


def make_source(root: Path) -> None:
    for name in SOURCE_REQUIRED_PATHS:
        path = root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("fixture\n", encoding="utf-8")


def make_secret_local_and_generated_fixture_paths(root: Path) -> list[str]:
    fixture_paths = [
        ".env",
        ".env.local",
        "secrets/api-token.txt",
        "credentials/service-account.json",
        ".codex/session.jsonl",
        "docs/.env.private",
        "logs/work-graph.json",
        "logs/check-output/secret-output.txt",
    ]
    for name in fixture_paths:
        path = root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("fixture secret or local state\n", encoding="utf-8")
    return fixture_paths


def self_test() -> int:
    with tempfile.TemporaryDirectory() as tmp:
        base = Path(tmp)
        source = base / "source"
        source.mkdir()
        make_source(source)
        excluded_fixture_paths = make_secret_local_and_generated_fixture_paths(source)

        empty_target = base / "empty-target"
        empty_target.mkdir()
        (source / "tasks" / "prds").mkdir(parents=True, exist_ok=True)
        (source / "tasks" / "beads").mkdir(parents=True, exist_ok=True)
        (source / "tasks" / "prds" / "PRD-000-template.md").write_text("fixture template\n", encoding="utf-8")
        (source / "tasks" / "prds" / "PRD-SHARD-SCHEMA.md").write_text("fixture schema\n", encoding="utf-8")
        (source / "tasks" / "beads" / "BEAD-SCHEMA.md").write_text("fixture schema\n", encoding="utf-8")
        (source / "tasks" / "prds" / "PRD-001-package-dev.md").write_text(
            "---\nprd_id: PRD-001\n---\n# Package Dev PRD\n",
            encoding="utf-8",
        )
        (source / "tasks" / "beads" / "B000-package-dev.md").write_text(
            "---\nbead_id: B000\n---\n# Package Dev Bead\n",
            encoding="utf-8",
        )
        (source / "docs-html").mkdir(parents=True, exist_ok=True)
        (source / "docs-html" / "index.html").write_text("<h1>PrecodeOS Docs</h1>\n", encoding="utf-8")
        (source / "docs-html" / "PRECODE-GUIDED-SETUP.html").write_text(
            "<h1>PrecodeOS Guided Setup</h1>\n",
            encoding="utf-8",
        )
        empty_payload = build_payload(source.as_posix(), empty_target.as_posix())
        assert empty_payload["target_kind"] == "empty"
        assert empty_payload["status"] == "pass"
        assert not (source / "logs" / "bootstrap-check.json").exists()

        existing_target = base / "existing-target"
        existing_target.mkdir()
        (existing_target / "README.md").write_text("Existing README\n", encoding="utf-8")
        (existing_target / "package.json").write_text("{}\n", encoding="utf-8")
        existing_payload = build_payload(source.as_posix(), existing_target.as_posix())
        assert existing_payload["target_kind"] == "existing_project"
        assert existing_payload["status"] == "warning"
        assert any(item["path"] == "README.md" for item in existing_payload["conflicts"])

        nearly_empty_target = base / "nearly-empty-target"
        nearly_empty_target.mkdir()
        (nearly_empty_target / "README.md").write_text("Existing README\n", encoding="utf-8")
        nearly_empty_payload = build_payload(source.as_posix(), nearly_empty_target.as_posix())
        nearly_empty_payload["install_update_preview"] = build_manifest_preview(nearly_empty_payload)
        nearly_empty_payload["supervised_setup_plan"] = build_supervised_setup_plan(nearly_empty_payload)
        assert nearly_empty_payload["target_kind"] == "nearly_empty"
        assert any(
            action["category"] == "adapt_candidate" and action["path"] == "README.md"
            for action in nearly_empty_payload["install_update_preview"]["actions"]
        )
        assert any(
            action["category"] == "review_adaptation_candidate" and action["path"] == "README.md"
            for action in nearly_empty_payload["supervised_setup_plan"]["actions"]
        )

        existing_payload["install_update_preview"] = build_manifest_preview(existing_payload)
        existing_payload["supervised_setup_plan"] = build_supervised_setup_plan(existing_payload)
        existing_payload["existing_project_adaptation_plan"] = build_existing_project_adaptation_plan(existing_payload)
        assert any(
            action["category"] == "deferred" and action["path"] == "scripts/existing-repo-intake.py"
            for action in existing_payload["install_update_preview"]["actions"]
        )
        assert existing_payload["supervised_setup_plan"]["status"] == "blocked"
        assert any(
            "Existing Repo Intake" in blocker for blocker in existing_payload["supervised_setup_plan"]["blockers"]
        )
        assert not any(
            action["category"] in {"review_copy_candidate", "review_adaptation_candidate"}
            for action in existing_payload["supervised_setup_plan"]["actions"]
        )
        assert existing_payload["existing_project_adaptation_plan"]["status"] == "warning"
        assert any(
            action["category"] in {"review_owner_adaptation_candidate", "review_owner_creation_candidate"}
            for action in existing_payload["existing_project_adaptation_plan"]["actions"]
        )

        missing_source_payload = build_payload((base / "missing-source").as_posix(), empty_target.as_posix())
        assert missing_source_payload["status"] == "blocked"
        assert "source path does not exist or is not a directory" in missing_source_payload["blockers"]
        missing_source_payload["install_update_preview"] = build_manifest_preview(missing_source_payload)
        missing_source_payload["supervised_setup_plan"] = build_supervised_setup_plan(missing_source_payload)
        assert any(action["category"] == "blocked" for action in missing_source_payload["install_update_preview"]["actions"])
        assert any(action["category"] == "blocked" for action in missing_source_payload["supervised_setup_plan"]["actions"])

        missing_target_payload = build_payload(source.as_posix(), (base / "missing-target").as_posix())
        assert missing_target_payload["target_kind"] == "missing"
        assert missing_target_payload["status"] == "blocked"
        missing_target_payload["install_update_preview"] = build_manifest_preview(missing_target_payload)
        missing_target_payload["supervised_setup_plan"] = build_supervised_setup_plan(missing_target_payload)
        assert any(action["path"] == "<target-project-root>" for action in missing_target_payload["install_update_preview"]["actions"])
        assert any(action["path"] == "<target-project-root>" for action in missing_target_payload["supervised_setup_plan"]["actions"])

        same_payload = build_payload(source.as_posix(), source.as_posix())
        assert same_payload["target_kind"] == "same_as_source"
        assert same_payload["status"] == "blocked"
        same_payload["install_update_preview"] = build_manifest_preview(same_payload)
        same_payload["supervised_setup_plan"] = build_supervised_setup_plan(same_payload)
        assert any(action["category"] == "blocked" for action in same_payload["install_update_preview"]["actions"])
        assert any(action["category"] == "blocked" for action in same_payload["supervised_setup_plan"]["actions"])

        existing_precode_target = base / "existing-precode-target"
        make_source(existing_precode_target)
        existing_precode_payload = build_payload(source.as_posix(), existing_precode_target.as_posix())
        existing_precode_payload["install_update_preview"] = build_manifest_preview(existing_precode_payload)
        existing_precode_payload["supervised_setup_plan"] = build_supervised_setup_plan(existing_precode_payload)
        (source / "docs" / "NEW-PACKAGE-DOC.md").write_text("new package doc\n", encoding="utf-8")
        (source / "tasks" / "prds").mkdir(parents=True, exist_ok=True)
        (source / "tasks" / "beads").mkdir(parents=True, exist_ok=True)
        (existing_precode_target / "tasks" / "prds").mkdir(parents=True)
        (existing_precode_target / "tasks" / "beads").mkdir(parents=True)
        (source / "tasks" / "prds" / "PRD-002-bootstrap-confidence-lane.md").write_text(
            "---\nprd_id: PRD-002\n---\n# Bootstrap Confidence Lane\n",
            encoding="utf-8",
        )
        (source / "tasks" / "prds" / "PRD-003-existing-repo-intake.md").write_text(
            "---\nprd_id: PRD-003\n---\n# Existing Repo Intake\n",
            encoding="utf-8",
        )
        (source / "tasks" / "beads" / "B001-ubiquitous-language-glossary-hardening.md").write_text(
            "---\nbead_id: B001\n---\n# Ubiquitous Language Glossary Hardening\n",
            encoding="utf-8",
        )
        (existing_precode_target / "tasks" / "prds" / "PRD-002-backend-foundation.md").write_text(
            "---\nprd_id: PRD-002\n---\n# Backend Foundation\n",
            encoding="utf-8",
        )
        (existing_precode_target / "tasks" / "beads" / "B001-backend-scaffold.md").write_text(
            "---\nbead_id: B001\n---\n# Backend Scaffold\n",
            encoding="utf-8",
        )
        existing_precode_payload["package_upgrade_preview"] = build_upgrade_preview(existing_precode_payload)
        existing_precode_payload["bootstrap_recovery_guidance"] = build_recovery_guidance(existing_precode_payload)
        assert existing_precode_payload["target_kind"] == "existing_precode"
        assert any(
            action["category"] == "preserve_existing"
            for action in existing_precode_payload["install_update_preview"]["actions"]
        )
        assert existing_precode_payload["supervised_setup_plan"]["status"] == "blocked"
        assert any(
            action["category"] == "preserve_existing"
            for action in existing_precode_payload["supervised_setup_plan"]["actions"]
        )
        assert existing_precode_payload["package_upgrade_preview"]["package_state_classification"] == "dirty_project_or_owner_edits"
        prd_collision_actions = [
            action
            for action in existing_precode_payload["package_upgrade_preview"]["actions"]
            if action["category"] == "blocked_identity_collision"
            and action["path"] == "tasks/prds/PRD-002-bootstrap-confidence-lane.md"
        ]
        bead_collision_actions = [
            action
            for action in existing_precode_payload["package_upgrade_preview"]["actions"]
            if action["category"] == "blocked_identity_collision"
            and action["path"] == "tasks/beads/B001-ubiquitous-language-glossary-hardening.md"
        ]
        assert len(prd_collision_actions) == 1
        assert prd_collision_actions[0]["incoming_id"] == "PRD-002"
        assert prd_collision_actions[0]["existing_target_path"] == "tasks/prds/PRD-002-backend-foundation.md"
        assert len(bead_collision_actions) == 1
        assert bead_collision_actions[0]["incoming_id"] == "B001"
        assert bead_collision_actions[0]["existing_target_path"] == "tasks/beads/B001-backend-scaffold.md"
        assert not any(
            action["category"] == "review_package_copy_candidate"
            and action["path"] in {
                "tasks/prds/PRD-002-bootstrap-confidence-lane.md",
                "tasks/beads/B001-ubiquitous-language-glossary-hardening.md",
            }
            for action in existing_precode_payload["package_upgrade_preview"]["actions"]
        )
        assert any(
            action["category"] == "deferred_package_dev_identity"
            and action["path"] == "tasks/prds/PRD-003-existing-repo-intake.md"
            for action in existing_precode_payload["package_upgrade_preview"]["actions"]
        )
        upgrade_copy_ids = [
            action["id"]
            for action in existing_precode_payload["package_upgrade_preview"]["actions"]
            if action["category"] == "review_package_copy_candidate" and action["path"] == "docs/NEW-PACKAGE-DOC.md"
        ]
        assert len(upgrade_copy_ids) == 1
        collision_apply = apply_upgrade_preview(existing_precode_payload, [prd_collision_actions[0]["id"]])
        assert collision_apply["status"] == "blocked"
        assert any("identity collision" in item["reason"] for item in collision_apply["blocked"])
        upgrade_apply = apply_upgrade_preview(existing_precode_payload, upgrade_copy_ids)
        assert upgrade_apply["status"] == "applied"
        assert (existing_precode_target / "docs" / "NEW-PACKAGE-DOC.md").is_file()
        assert "Validate active memory" in existing_precode_payload["bootstrap_recovery_guidance"]["likely_recovery_path"]

        dirty_precode_target = base / "dirty-precode-target"
        make_source(dirty_precode_target)
        (dirty_precode_target / "docs" / "PRECODE-GUIDED-SETUP.md").write_text("target edit\n", encoding="utf-8")
        dirty_precode_payload = build_payload(source.as_posix(), dirty_precode_target.as_posix())
        dirty_precode_payload["package_upgrade_preview"] = build_upgrade_preview(dirty_precode_payload)
        assert dirty_precode_payload["package_upgrade_preview"]["package_state_classification"] == "mixed_or_unknown"
        dirty_apply = apply_upgrade_preview(dirty_precode_payload, upgrade_copy_ids)
        assert dirty_apply["status"] == "blocked"
        assert any("refuses dirty or unknown package state" in item["reason"] for item in dirty_apply["blocked"])

        empty_payload["install_update_preview"] = build_manifest_preview(empty_payload)
        empty_payload["supervised_setup_plan"] = build_supervised_setup_plan(empty_payload)
        assert any(
            action["category"] == "copy_candidate" for action in empty_payload["install_update_preview"]["actions"]
        )
        assert any(
            action["category"] == "review_copy_candidate" for action in empty_payload["supervised_setup_plan"]["actions"]
        )
        assert empty_payload["supervised_setup_plan"]["target_mutation_allowed"] is False
        preview_copy_paths = {
            action["path"]
            for action in empty_payload["install_update_preview"]["actions"]
            if action["category"] == "copy_candidate"
        }
        setup_copy_paths = {
            action["path"]
            for action in empty_payload["supervised_setup_plan"]["actions"]
            if action["category"] == "review_copy_candidate"
        }
        setup_adaptation_paths = {
            action["path"]
            for action in empty_payload["supervised_setup_plan"]["actions"]
            if action["category"] == "review_adaptation_candidate"
        }
        assert "OPERATING-CONSTRAINTS.md" in preview_copy_paths
        assert "OPERATING-CONSTRAINTS.md" in setup_copy_paths
        assert "docs-html/" in preview_copy_paths
        assert "docs-html/" in setup_copy_paths
        assert "tasks/todo.md" not in preview_copy_paths
        assert "tasks/todo.md" not in setup_copy_paths
        assert "tasks/todo.md" in setup_adaptation_paths
        assert "tasks/prds/PRD-000-template.md" in setup_copy_paths
        assert "tasks/prds/PRD-SHARD-SCHEMA.md" in setup_copy_paths
        assert "tasks/beads/BEAD-SCHEMA.md" in setup_copy_paths
        assert "tasks/prds/PRD-001-package-dev.md" not in setup_copy_paths
        assert "tasks/beads/B000-package-dev.md" not in setup_copy_paths
        for excluded_path in excluded_fixture_paths:
            assert excluded_path not in preview_copy_paths
            assert excluded_path not in setup_copy_paths
        assert any(
            action["category"] == "exclude" and action["path"] == ".env"
            for action in empty_payload["install_update_preview"]["actions"]
        )
        rendered_setup_plan = render_setup_plan_plain(empty_payload)
        assert "evidence only" in rendered_setup_plan
        assert "does not approve copying" in rendered_setup_plan
        json.dumps(empty_payload, sort_keys=True)

        write_evidence(empty_payload)
        assert (source / "logs" / "bootstrap-check.json").is_file()
        assert (source / "logs" / "bootstrap-check.md").is_file()
        assert "Install/Update Manifest Dry-Run Preview" in (source / "logs" / "bootstrap-check.md").read_text(
            encoding="utf-8"
        )
        assert "Supervised Setup Plan" in (source / "logs" / "bootstrap-check.md").read_text(encoding="utf-8")
        assert not (empty_target / "logs").exists()

        approved_copy_ids = [
            action["id"]
            for action in empty_payload["supervised_setup_plan"]["actions"]
            if action["category"] == "review_copy_candidate" and action["path"] == "AGENT.md"
        ]
        assert len(approved_copy_ids) == 1
        apply_target = base / "apply-target"
        apply_target.mkdir()
        apply_payload = build_payload(source.as_posix(), apply_target.as_posix())
        apply_payload["install_update_preview"] = build_manifest_preview(apply_payload)
        apply_payload["supervised_setup_plan"] = build_supervised_setup_plan(apply_payload)
        apply_payload["supervised_setup_apply"] = apply_supervised_setup(apply_payload, approved_copy_ids)
        assert apply_payload["supervised_setup_apply"]["status"] == "applied"
        assert (apply_target / "AGENT.md").is_file()
        assert not (apply_target / "DECISIONS.md").exists()

        docs_html_copy_ids = [
            action["id"]
            for action in apply_payload["supervised_setup_plan"]["actions"]
            if action["category"] == "review_copy_candidate" and action["path"] == "docs-html/"
        ]
        assert len(docs_html_copy_ids) == 1
        docs_apply_target = base / "docs-html-apply-target"
        docs_apply_target.mkdir()
        docs_apply_payload = build_payload(source.as_posix(), docs_apply_target.as_posix())
        docs_apply_payload["install_update_preview"] = build_manifest_preview(docs_apply_payload)
        docs_apply_payload["supervised_setup_plan"] = build_supervised_setup_plan(docs_apply_payload)
        docs_apply_payload["supervised_setup_apply"] = apply_supervised_setup(docs_apply_payload, docs_html_copy_ids)
        assert docs_apply_payload["supervised_setup_apply"]["status"] == "applied"
        assert (docs_apply_target / "docs-html" / "index.html").is_file()
        assert (docs_apply_target / "docs-html" / "PRECODE-GUIDED-SETUP.html").is_file()
        assert not (docs_apply_target / "docs").exists()

        blocked_no_approval = apply_supervised_setup(apply_payload, [])
        assert blocked_no_approval["status"] == "blocked"
        assert any("at least one" in item["reason"] for item in blocked_no_approval["blocked"])

        blocked_unknown = apply_supervised_setup(apply_payload, ["SP-999"])
        assert blocked_unknown["status"] == "blocked"
        assert any("not present in the setup plan" in item["reason"] for item in blocked_unknown["blocked"])

        adapt_ids = [
            action["id"]
            for action in nearly_empty_payload["supervised_setup_plan"]["actions"]
            if action["category"] == "review_adaptation_candidate"
        ]
        assert adapt_ids
        blocked_adapt = apply_supervised_setup(nearly_empty_payload, [adapt_ids[0]])
        assert blocked_adapt["status"] == "blocked"
        assert any("review_adaptation_candidate" in item["reason"] for item in blocked_adapt["blocked"])

        existing_blocked_apply = apply_supervised_setup(existing_payload, ["SP-001"])
        assert existing_blocked_apply["status"] == "blocked"
        assert any("empty or nearly empty" in item["reason"] for item in existing_blocked_apply["blocked"])

        conflict_copy_ids = [
            action["id"]
            for action in nearly_empty_payload["supervised_setup_plan"]["actions"]
            if action["category"] == "review_copy_candidate" and action["path"] == "AGENT.md"
        ]
        (nearly_empty_target / "AGENT.md").write_text("existing\n", encoding="utf-8")
        blocked_conflict = apply_supervised_setup(nearly_empty_payload, conflict_copy_ids)
        assert blocked_conflict["status"] == "blocked"
        assert any("refusing to overwrite" in item["reason"] for item in blocked_conflict["blocked"])

        blocked_upgrade_no_approval = apply_upgrade_preview(existing_precode_payload, [])
        assert blocked_upgrade_no_approval["status"] == "blocked"
        assert any("at least one" in item["reason"] for item in blocked_upgrade_no_approval["blocked"])

        blocked_upgrade_unknown = apply_upgrade_preview(existing_precode_payload, ["UP-999"])
        assert blocked_upgrade_unknown["status"] == "blocked"
        assert any("not present in the upgrade preview" in item["reason"] for item in blocked_upgrade_unknown["blocked"])

        blocked_upgrade_existing = apply_upgrade_preview(existing_precode_payload, upgrade_copy_ids)
        assert blocked_upgrade_existing["status"] == "blocked"
        assert any("refusing to overwrite" in item["reason"] for item in blocked_upgrade_existing["blocked"])

    print(json.dumps({"tool": "bootstrap-check-self-test", "status": "pass"}, indent=2, sort_keys=True))
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Read-only PrecodeOS bootstrap confidence check.")
    parser.add_argument("--source", help="PrecodeOS package source checkout")
    parser.add_argument("--target", help="target project folder")
    parser.add_argument("--json", action="store_true", help="print machine-readable bootstrap confidence output")
    parser.add_argument(
        "--preview-manifest",
        action="store_true",
        help="include non-mutating install/update manifest dry-run preview output",
    )
    parser.add_argument(
        "--supervised-setup-plan",
        action="store_true",
        help="include non-mutating supervised setup-plan output; implies --preview-manifest",
    )
    parser.add_argument(
        "--existing-project-adaptation-plan",
        action="store_true",
        help="include non-mutating existing-project owner-file adaptation planning output",
    )
    parser.add_argument(
        "--upgrade-preview",
        action="store_true",
        help="include non-mutating package upgrade preview output for existing Precode targets",
    )
    parser.add_argument(
        "--recovery-guidance",
        action="store_true",
        help="include non-mutating bootstrap recovery guidance output",
    )
    parser.add_argument(
        "--apply-supervised-setup",
        action="store_true",
        help="apply explicitly approved supervised setup copy actions for empty or nearly empty targets",
    )
    parser.add_argument(
        "--apply-upgrade-preview",
        action="store_true",
        help="apply explicitly approved missing package-file copy actions from --upgrade-preview",
    )
    parser.add_argument(
        "--approve-action",
        action="append",
        default=[],
        help="approve one supervised setup action ID for --apply-supervised-setup; repeat for multiple actions",
    )
    parser.add_argument("--write-evidence", action="store_true", help="write generated evidence under the source logs directory")
    parser.add_argument("--self-test", action="store_true", help="run fixture-style bootstrap confidence checks")
    args = parser.parse_args()

    if args.self_test:
        return self_test()

    if not args.source or not args.target:
        parser.error("--source and --target are required unless --self-test is used")
    if args.apply_supervised_setup and not args.supervised_setup_plan:
        parser.error("--apply-supervised-setup requires --supervised-setup-plan")
    if args.apply_upgrade_preview and not args.upgrade_preview:
        parser.error("--apply-upgrade-preview requires --upgrade-preview")

    payload = build_payload(args.source, args.target)
    if args.preview_manifest or args.supervised_setup_plan:
        payload["install_update_preview"] = build_manifest_preview(payload)
    if args.supervised_setup_plan:
        payload["supervised_setup_plan"] = build_supervised_setup_plan(payload)
    if args.existing_project_adaptation_plan:
        payload["existing_project_adaptation_plan"] = build_existing_project_adaptation_plan(payload)
    if args.upgrade_preview:
        payload["package_upgrade_preview"] = build_upgrade_preview(payload)
    if args.recovery_guidance:
        payload["bootstrap_recovery_guidance"] = build_recovery_guidance(payload)
    if args.apply_supervised_setup:
        payload["supervised_setup_apply"] = apply_supervised_setup(payload, args.approve_action)
    if args.apply_upgrade_preview:
        payload["package_upgrade_apply"] = apply_upgrade_preview(payload, args.approve_action)
    if args.write_evidence:
        if payload["source_root"] == payload["target_root"]:
            raise SystemExit("bootstrap-check: refusing to write evidence when source and target are the same")
        if "source path does not exist or is not a directory" in payload["blockers"]:
            raise SystemExit("bootstrap-check: refusing to write evidence because source is missing")
        write_evidence(payload)
    if args.json:
        print(json.dumps(payload, indent=2, sort_keys=True))
    else:
        if args.apply_upgrade_preview:
            print(render_upgrade_apply_plain(payload))
        elif args.upgrade_preview:
            print(render_upgrade_preview_plain(payload))
        elif args.existing_project_adaptation_plan:
            print(render_existing_project_adaptation_plain(payload))
        elif args.recovery_guidance:
            print(render_recovery_guidance_plain(payload))
        elif args.supervised_setup_plan:
            print(render_apply_plain(payload) if args.apply_supervised_setup else render_setup_plan_plain(payload))
        elif args.preview_manifest:
            print(render_preview_plain(payload))
        else:
            print(render_plain(payload))
        if args.write_evidence:
            print("bootstrap-check: wrote logs/bootstrap-check.json and logs/bootstrap-check.md in the source workspace")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
