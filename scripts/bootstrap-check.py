#!/usr/bin/env python3
# Version: v0.5.9
# Last updated: 2026-08-04
# Owner: PrecodeOS
# Created by Dan Sears / Recode.
# SPDX-License-Identifier: Apache-2.0
from __future__ import annotations

import argparse
import hashlib
import json
import shlex
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
            ".gitignore",
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
REQUIRED_SETUP_SUPPORT_PATHS = [
    "tasks/beads/BEAD-SCHEMA.md",
    "tasks/prds/PRD-000-template.md",
    "tasks/prds/PRD-SHARD-SCHEMA.md",
]
CONFLICT_PATHS = [
    "README.md",
    ".gitignore",
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
TARGET_KIND_IGNORED_NAMES = {
    ".agent-state",
    ".claude",
    ".codex",
    ".cursor",
    ".idea",
    ".mypy_cache",
    ".pytest_cache",
    ".ruff_cache",
    ".vscode",
    "__pycache__",
    "coverage",
    "htmlcov",
}
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

RELEASE_TERM_DEFINITIONS = {
    "stable": (
        "the maintainer-reviewed package line that should be treated as the default acquisition reference "
        "once a stable release exists; not overwrite permission"
    ),
    "latest": (
        "the newest package reference a user or support helper may inspect; latest is not safe-to-overwrite "
        "permission for an active Precode project"
    ),
    "pinned": (
        "an explicitly named package version or source checkout used for comparison; pinning does not approve "
        "target mutation"
    ),
}
RELEASE_REFERENCE_BOUNDARY = (
    "Release reference metadata is advisory generated evidence only. No registry lookup, dist-tag resolution, "
    "channel selection, package update permission, dirty-file overwrite, owner-file adaptation approval, "
    "rollback automation, or npm updater behavior is performed."
)
UPDATER_COMPATIBILITY_POLICY = {
    "policy_name": "npm Updater Evidence And Compatibility Policy",
    "policy_prd": "tasks/prds/PRD-041-npm-updater-evidence-and-compatibility-policy.md",
    "evidence_threshold": (
        "Run upgrade preview against the package source and existing Precode target, review package-state "
        "classification, identity collisions, dirty paths, deferred package development identities, release "
        "reference metadata, and action IDs before any package-owned copy action is considered."
    ),
    "compatible_only_when": [
        "target kind is existing_precode",
        "package state is clean for any approved package-owned copy action",
        "the action is a missing package-owned review_package_copy_candidate",
        "the approved UP-ID exists in the current preview",
        "the source file exists and the target path does not exist",
        "target PRDs, beads, owner files, active memory, app code, hooks, CI, and generated evidence are preserved",
    ],
    "blocked_update_cases": [
        "blocked preview state",
        "dirty_package_edits",
        "mixed_or_unknown",
        "blocked_identity_collision",
        "dirty owner or project truth requiring manual review",
        "package development PRD or bead identity copy",
        "existing target path or overwrite request",
        "owner-file adaptation request",
        "hook, CI, app command, app-code, rollback, registry, dist-tag, or package-manager request",
    ],
    "clone_first_support": (
        "For important active work, known local Precode changes, or unclear recovery state, preserve the current "
        "environment and run preview against a fresh clone before any approved copy action."
    ),
    "not_authority_for": [
        "package update permission",
        "npm registry freshness",
        "dist-tag resolution",
        "channel selection",
        "dirty-file overwrite",
        "owner-file adaptation",
        "rollback automation",
        "package-manager behavior",
        "generated-output authority",
    ],
}


def resolve_candidate(raw: str) -> Path:
    return Path(raw).expanduser().resolve(strict=False)


def rel(path: Path, root: Path) -> str:
    return path.relative_to(root).as_posix()


def shell_command_text(command: list[str]) -> str:
    return " ".join(shlex.quote(part) for part in command)


def validation_command(target_root: str) -> str:
    return f"cd {shlex.quote(target_root)} && bash scripts/validate-memory.sh"


def source_missing_paths(source: Path) -> list[str]:
    return [name for name in SOURCE_REQUIRED_PATHS if not (source / name).exists()]


def target_missing_required_setup_support_paths(target: Path, kind: str) -> list[str]:
    if kind != "existing_precode" or not target.is_dir():
        return []
    return [name for name in REQUIRED_SETUP_SUPPORT_PATHS if not (target / name).is_file()]


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
    meaningful_names = {name for name in names if name not in TARGET_KIND_IGNORED_NAMES}
    if not meaningful_names:
        return "nearly_empty"
    if all(name in MINIMAL_TARGET_NAMES for name in meaningful_names):
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


def prerelease_label(version: str) -> str:
    if "-" not in version:
        return "stable"
    suffix = version.split("-", 1)[1]
    label = suffix.split(".", 1)[0].strip()
    return label or "prerelease"


def source_release_reference(source_root: Path) -> dict[str, Any]:
    package_path = source_root / "package.json"
    package_name = "not recorded"
    package_version = "not recorded"
    if package_path.is_file():
        try:
            metadata = json.loads(package_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            metadata = {}
        if isinstance(metadata, dict):
            package_name = str(metadata.get("name") or package_name)
            package_version = str(metadata.get("version") or package_version)
    return {
        "source_package_name": package_name,
        "source_package_version": package_version,
        "inferred_source_release_label": prerelease_label(package_version) if package_version != "not recorded" else "not recorded",
        "registry_lookup_performed": False,
        "dist_tag_resolution_performed": False,
        "term_definitions": RELEASE_TERM_DEFINITIONS,
        "boundary": RELEASE_REFERENCE_BOUNDARY,
    }


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


def setup_diagnosis(
    kind: str,
    source_missing: list[str],
    target_missing_support: list[str],
    conflicts: list[dict[str, str]],
    blockers: list[str],
) -> dict[str, Any]:
    source_target_clarity = "clear"
    target_state = "ready_for_diagnosis"
    partial_setup_classification = "none"
    recommended_route = "guided_setup"
    validation_after_apply = [
        "Inspect target git status after any approved copy action.",
        "Run `bash scripts/validate-memory.sh` from the installed Precode root after package files exist.",
    ]
    forbidden_next_actions = [
        "do not copy files from generated output alone",
        "do not overwrite target material",
        "do not adapt owner files without separate review",
        "do not automate rollback",
        "do not install hooks or change CI silently",
        "do not treat setup diagnosis as product work approval",
        "do not create a new setup command or support-only setup path",
        "do not create package-manager behavior",
    ]

    if source_missing or kind in {"missing", "same_as_source"} or blockers:
        source_target_clarity = "unclear_or_blocked"
    if kind == "same_as_source":
        target_state = "wrong_folder"
        partial_setup_classification = "wrong_source_target"
        recommended_route = "stop_and_choose_target"
    elif kind == "missing":
        target_state = "missing_target"
        partial_setup_classification = "target_missing"
        recommended_route = "stop_and_identify_or_create_target"
    elif source_missing:
        target_state = "source_not_plausible"
        partial_setup_classification = "source_incomplete"
        recommended_route = "stop_and_use_clean_package_source"
    elif target_missing_support:
        target_state = "existing_precode_missing_reusable_setup_support"
        partial_setup_classification = "required_support_files_missing"
        recommended_route = "package_owned_refresh_then_validate"
    elif kind == "existing_precode":
        target_state = "existing_precode"
        partial_setup_classification = "installed_precode"
        recommended_route = "validate_then_choose_repair_refresh_or_work"
    elif kind == "existing_project":
        target_state = "existing_project"
        partial_setup_classification = "existing_project_needs_intake"
        recommended_route = "existing_repo_intake_before_setup_mutation"
    elif kind in {"empty", "nearly_empty"}:
        target_state = "fresh_target"
        partial_setup_classification = "fresh_setup_candidate"
        recommended_route = "supervised_setup_plan_then_validate"
    elif conflicts:
        target_state = "conflict_review_needed"
        partial_setup_classification = "conflicts_present"
        recommended_route = "review_conflicts_before_copying"

    return {
        "diagnosis_kind": "setup_diagnosis_clarity",
        "source_target_clarity": source_target_clarity,
        "target_state": target_state,
        "partial_setup_classification": partial_setup_classification,
        "recommended_route": recommended_route,
        "target_missing_required_setup_support_paths": target_missing_support,
        "validation_after_apply": validation_after_apply,
        "forbidden_next_actions": forbidden_next_actions,
        "generated_evidence_only": True,
        "target_mutation_allowed": False,
        "not_authority_for": [
            "copy approval",
            "repair approval",
            "rollback approval",
            "setup or update mutation",
            "product work approval",
            "PRD approval",
            "bead activation",
            "review acceptance",
            "command approval",
            "package-manager behavior",
        ],
    }


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
            "executable release-channel behavior",
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
    required_setup_support_missing = list(payload.get("target_missing_required_setup_support_paths", []))
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
        "release_reference": source_release_reference(source_root),
        "updater_compatibility_policy": UPDATER_COMPATIBILITY_POLICY,
        "actions": actions,
        "dirty_package_paths": dirty_package,
        "dirty_project_or_owner_paths": dirty_owner,
        "missing_package_paths": missing_package,
        "required_setup_support_missing_paths": required_setup_support_missing,
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
            "executable release-channel behavior",
            "package-manager updates",
            "rollback automation",
            "npm updater behavior",
        ],
        "next_setup_gate": "Only missing package-owned files marked review_package_copy_candidate may be copied with explicit action approval; dirty files require manual review, identity collisions block copying, and latest is not overwrite permission.",
    }


def build_update_plan_preview(payload: dict[str, Any]) -> dict[str, Any]:
    preview = payload.get("package_upgrade_preview") or build_upgrade_preview(payload)
    actions = list(preview["actions"])
    grouped_action_ids: dict[str, list[str]] = {
        "candidate_package_copy": [
            str(action["id"]) for action in actions if action["category"] == "review_package_copy_candidate"
        ],
        "manual_review": [
            str(action["id"])
            for action in actions
            if action["category"] in {"manual_package_review", "preserve_owner_edit", "review_owner_creation_candidate"}
        ],
        "blocked": [str(action["id"]) for action in actions if action["category"] == "blocked_identity_collision"],
        "deferred": [str(action["id"]) for action in actions if action["category"] == "deferred_package_dev_identity"],
    }
    validation_prompts = [
        "Confirm source package root and target existing-Precode root before interpreting this plan.",
        "Review package-state classification, dirty paths, identity collisions, and deferred package-development identities.",
        "Run the plan again in the same session before considering any separately approved package-owned copy action.",
        "Use clone-first support review for important active work, known local package edits, or unclear recovery state.",
    ]
    same_session_requirement = (
        "Action IDs are advisory and must come from the current same-session preview; rerun update-plan preview before "
        "any separate approved package-owned copy action is considered."
    )
    next_manual_gate = (
        "Review the update plan with the user. Missing package-owned action IDs may inform a separate Python "
        "upgrade-preview apply decision, but this update-plan preview does not approve or perform copying."
    )
    if preview["blockers"]:
        next_manual_gate = "Resolve blockers and rerun update-plan preview before considering package refresh work."
    elif preview["package_state_classification"] != "clean":
        next_manual_gate = "Review dirty or unknown package state manually; do not copy package files from this plan."
    elif grouped_action_ids["candidate_package_copy"]:
        next_manual_gate = (
            "If the user explicitly approves a current missing package-owned UP-ID, use the Python upgrade-preview "
            "apply path or the apply-package-owned facade; this preview itself does not approve or perform copying."
        )

    return {
        "plan_kind": "npm_update_plan_preview",
        "status": preview["status"],
        "source_root": preview["source_root"],
        "target_root": preview["target_root"],
        "target_kind": preview["target_kind"],
        "package_state_classification": preview["package_state_classification"],
        "release_reference": preview["release_reference"],
        "updater_compatibility_policy": preview["updater_compatibility_policy"],
        "optional_registry_metadata": {
            "requested": False,
            "registry_lookup_performed": False,
            "dist_tag_resolution_performed": False,
            "status": "not_requested_in_v1",
            "boundary": "V1 update-plan preview uses local package metadata only; registry lookup and dist-tag resolution remain deferred.",
        },
        "action_summary": {
            "total_actions": len(actions),
            "candidate_package_copy_count": len(grouped_action_ids["candidate_package_copy"]),
            "manual_review_count": len(grouped_action_ids["manual_review"]),
            "blocked_count": len(grouped_action_ids["blocked"]),
            "deferred_count": len(grouped_action_ids["deferred"]),
        },
        "grouped_action_ids": grouped_action_ids,
        "actions": actions,
        "blockers": preview["blockers"],
        "dirty_package_paths": preview["dirty_package_paths"],
        "dirty_project_or_owner_paths": preview["dirty_project_or_owner_paths"],
        "missing_package_paths": preview["missing_package_paths"],
        "identity_collisions": preview["identity_collisions"],
        "deferred_package_dev_identity_paths": preview["deferred_package_dev_identity_paths"],
        "same_session_requirement": same_session_requirement,
        "validation_prompts": validation_prompts,
        "next_manual_gate": next_manual_gate,
        "writes_by_default": False,
        "target_mutation_allowed": False,
        "generated_evidence_only": True,
        "not_authority_for": [
            "package update permission",
            "copy approval",
            "overwriting target material",
            "owner-file adaptation",
            "installing hooks",
            "changing CI",
            "registry freshness",
            "dist-tag resolution",
            "executable release-channel behavior",
            "package-manager updates",
            "rollback automation",
            "npm apply behavior",
            "generated-output authority",
        ],
    }


def bootstrap_command(payload: dict[str, Any], *flags: str) -> str:
    command = [
        "python3",
        "scripts/bootstrap-check.py",
        "--source",
        str(payload["source_root"]),
        "--target",
        str(payload["target_root"]),
        *flags,
    ]
    return shell_command_text(command)


def existing_repo_intake_command(payload: dict[str, Any]) -> str:
    command = [
        "python3",
        "scripts/existing-repo-intake.py",
        "--source",
        str(payload["source_root"]),
        "--target",
        str(payload["target_root"]),
    ]
    return shell_command_text(command)


def action_ids(actions: list[dict[str, Any]], category: str) -> list[str]:
    return [str(action["id"]) for action in actions if action["category"] == category]


def approved_action_prefixes(approved_action_ids: list[str]) -> set[str]:
    prefixes: set[str] = set()
    for action_id in approved_action_ids:
        if "-" in action_id:
            prefixes.add(action_id.split("-", 1)[0])
        else:
            prefixes.add(action_id)
    return prefixes


def build_fast_verified_setup_preview(payload: dict[str, Any]) -> dict[str, Any]:
    kind = str(payload["target_kind"])
    blockers = list(payload["blockers"])
    route = "blocked"
    approval_prefix = "none"
    current_action_ids: list[str] = []
    underlying_commands: list[str] = []
    next_manual_gate = "Resolve blockers and rerun fast verified setup preview."

    if kind in {"empty", "nearly_empty"}:
        route = "fresh_or_nearly_empty_setup"
        approval_prefix = "SP"
        plan = payload["supervised_setup_plan"]
        current_action_ids = action_ids(plan["actions"], "review_copy_candidate")
        underlying_commands = [
            bootstrap_command(payload, "--fast-verified-setup-preview"),
            bootstrap_command(payload, "--supervised-setup-plan"),
            bootstrap_command(payload, "--fast-verified-setup-apply", "--approve-action", "<SP-ID>"),
            validation_command(str(payload["target_root"])),
        ]
        next_manual_gate = (
            "Review the supervised setup plan. Apply only current SP-ID review_copy_candidate actions with "
            "--fast-verified-setup-apply, then run validation from the installed target."
        )
    elif kind == "existing_precode":
        route = "existing_precode_refresh"
        approval_prefix = "UP"
        plan = payload["npm_update_plan_preview"]
        current_action_ids = list(plan["grouped_action_ids"]["candidate_package_copy"])
        underlying_commands = [
            bootstrap_command(payload, "--fast-verified-setup-preview"),
            bootstrap_command(payload, "--upgrade-preview"),
            bootstrap_command(payload, "--update-plan-preview"),
            bootstrap_command(payload, "--fast-verified-setup-apply", "--approve-action", "<UP-ID>"),
            validation_command(str(payload["target_root"])),
        ]
        next_manual_gate = (
            "Review upgrade and update-plan evidence. Apply only current UP-ID review_package_copy_candidate "
            "actions with --fast-verified-setup-apply, then run validation from the target."
        )
    elif kind == "existing_project":
        route = "existing_project_intake"
        underlying_commands = [
            bootstrap_command(payload, "--fast-verified-setup-preview"),
            existing_repo_intake_command(payload),
            bootstrap_command(payload, "--existing-project-adaptation-plan"),
        ]
        next_manual_gate = "Run Existing Repo Intake and adaptation planning. This facade has no existing-app apply path."
    else:
        underlying_commands = [bootstrap_command(payload)]

    return {
        "preview_kind": "fast_verified_setup_preview",
        "status": "blocked" if blockers else payload["status"],
        "source_root": payload["source_root"],
        "target_root": payload["target_root"],
        "target_kind": kind,
        "route": route,
        "approval_prefix": approval_prefix,
        "current_action_ids": current_action_ids,
        "underlying_commands": underlying_commands,
        "writes_by_default": False,
        "target_mutation_allowed": False,
        "generated_evidence_only": True,
        "next_manual_gate": next_manual_gate,
        "validation_command_after_apply": validation_command(str(payload["target_root"])),
        "blockers": blockers,
        "not_authority_for": [
            "broad installer behavior",
            "hidden support-only setup",
            "package update permission",
            "dirty-file overwrite",
            "owner-file adaptation approval",
            "hook installation",
            "CI mutation",
            "app commands",
            "app-code edits",
            "registry lookup",
            "dist-tag resolution",
            "release-channel behavior",
            "package-manager behavior",
            "rollback automation",
            "generated-output authority",
            "task selection",
            "PRD approval",
            "bead activation",
        ],
    }


def build_fast_verified_setup_apply(payload: dict[str, Any], approved_action_ids: list[str]) -> dict[str, Any]:
    approved = sorted(set(approved_action_ids))
    prefixes = approved_action_prefixes(approved)
    blocked: list[dict[str, str]] = []
    delegated_apply: dict[str, Any] | None = None
    route = "blocked"

    if not approved:
        blocked.append({"path": "<approval>", "reason": "at least one --approve-action <SP-ID|UP-ID> is required"})
    if len(prefixes) > 1:
        blocked.append({"path": "<approval>", "reason": "do not mix SP-ID and UP-ID approvals in one fast setup apply"})
    elif prefixes and prefixes not in [{"SP"}, {"UP"}]:
        blocked.append({"path": "<approval>", "reason": "fast setup apply accepts only current SP-ID or UP-ID actions"})

    if not blocked and prefixes == {"SP"}:
        route = "fresh_or_nearly_empty_setup"
        delegated_apply = apply_supervised_setup(payload, approved)
    elif not blocked and prefixes == {"UP"}:
        route = "existing_precode_refresh"
        delegated_apply = apply_upgrade_preview(payload, approved)

    status = "blocked"
    copied: list[dict[str, str]] = []
    skipped: list[dict[str, str]] = []
    delegated_blocked: list[dict[str, str]] = []
    if delegated_apply is not None:
        status = str(delegated_apply["status"])
        copied = list(delegated_apply["copied"])
        skipped = list(delegated_apply["skipped"])
        delegated_blocked = list(delegated_apply["blocked"])
    all_blocked = blocked + delegated_blocked
    if all_blocked:
        status = "blocked"

    return {
        "apply_kind": "fast_verified_setup_apply",
        "status": status,
        "source_root": payload["source_root"],
        "target_root": payload["target_root"],
        "target_kind": payload["target_kind"],
        "route": route,
        "approved_actions": approved,
        "copied": copied,
        "skipped": skipped,
        "blocked": all_blocked,
        "delegated_apply": delegated_apply,
        "underlying_commands": [
            bootstrap_command(
                payload,
                "--fast-verified-setup-apply",
                *[part for action_id in approved for part in ("--approve-action", action_id)],
            )
        ],
        "validation_next_step": (
            validation_command(str(payload["target_root"]))
            if status == "applied"
            else "Resolve blockers and rerun fast verified setup preview before applying current approval IDs."
        ),
        "target_mutation_allowed": status == "applied",
        "generated_evidence_only": status != "applied",
        "not_authority_for": [
            "owner-file adaptation",
            "overwriting target material",
            "installing hooks",
            "changing CI",
            "running app commands",
            "writing app code",
            "registry lookup",
            "dist-tag resolution",
            "release-channel behavior",
            "package-manager behavior",
            "rollback automation",
            "task selection",
            "PRD approval",
            "bead activation",
            "generated-output authority",
        ],
    }


def build_recovery_guidance(payload: dict[str, Any]) -> dict[str, Any]:
    kind = str(payload["target_kind"])
    blockers = list(payload["blockers"])
    diagnosis = payload.get("setup_diagnosis") or {}
    missing_support = list(payload.get("target_missing_required_setup_support_paths", []))
    if kind == "existing_precode":
        if missing_support:
            path = "Run package upgrade preview, copy only approved missing reusable setup support UP-IDs, validate memory, then decide whether this is repair, package refresh, or normal Precode work."
        else:
            path = "Validate active memory, run upgrade preview, then decide whether this is repair, package refresh, or normal Precode work."
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
        "setup_diagnosis": diagnosis,
        "likely_recovery_path": path,
        "support_steps": [
            "Confirm source and target folders before interpreting setup state.",
            "Name the setup diagnosis route before proposing setup repair, package refresh, first-session orientation, or product work.",
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
            "do not create a new setup command or support-only setup path",
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
            "executable release-channel behavior",
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
            "executable release-channel behavior",
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
            "executable release-channel behavior",
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
    missing_required_setup_support_paths = target_missing_required_setup_support_paths(target, kind)
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
    if missing_required_setup_support_paths:
        warnings.append("target is missing required reusable setup support files")
    if missing_dependencies:
        warnings.append("recommended local dependencies are missing")

    status = "blocked" if blockers else "warning" if warnings else "pass"
    diagnosis = setup_diagnosis(kind, missing_source_paths, missing_required_setup_support_paths, conflicts, blockers)
    payload = {
        "tool": "bootstrap-check",
        "status": status,
        "warnings": warnings,
        "blockers": blockers,
        "source_root": source.as_posix(),
        "target_root": target.as_posix(),
        "source_missing_paths": missing_source_paths,
        "target_missing_required_setup_support_paths": missing_required_setup_support_paths,
        "target_kind": kind,
        "setup_diagnosis": diagnosis,
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
            "package-manager update mechanics",
            "full install/update manifest",
            "Git hook installation",
            "CI mutation",
            "app-code edits",
        ],
    }
    return payload


def render_plain(payload: dict[str, Any]) -> str:
    diagnosis = payload.get("setup_diagnosis") or {}
    lines = [
        f"Bootstrap Confidence: {payload['status']}",
        f"- Source: `{payload['source_root']}`",
        f"- Target: `{payload['target_root']}`",
        f"- Target kind: `{payload['target_kind']}`",
        f"- Recommended next step: {payload['recommended_next_step']}",
        "- Read-only default: yes; this command does not copy, edit, install hooks, change CI, or write app code.",
    ]
    if diagnosis:
        lines.extend(
            [
                "\nSetup diagnosis:",
                f"- Source/target clarity: `{diagnosis['source_target_clarity']}`",
                f"- Target state: `{diagnosis['target_state']}`",
                f"- Partial setup classification: `{diagnosis['partial_setup_classification']}`",
                f"- Recommended route: `{diagnosis['recommended_route']}`",
                "- Target mutation allowed from diagnosis: no",
                "- Generated evidence only: yes",
            ]
        )
        if diagnosis.get("validation_after_apply"):
            lines.append("\nValidation after approved apply:")
            lines.extend(f"- {item}" for item in diagnosis["validation_after_apply"])
        if diagnosis.get("forbidden_next_actions"):
            lines.append("\nForbidden next actions:")
            lines.extend(f"- {item}" for item in diagnosis["forbidden_next_actions"])
    if payload["blockers"]:
        lines.append("\nBlockers:")
        lines.extend(f"- {item}" for item in payload["blockers"])
    if payload["warnings"]:
        lines.append("\nWarnings:")
        lines.extend(f"- {item}" for item in payload["warnings"])
    if payload["source_missing_paths"]:
        lines.append("\nSource missing paths:")
        lines.extend(f"- `{item}`" for item in payload["source_missing_paths"])
    if payload["target_missing_required_setup_support_paths"]:
        lines.append("\nTarget missing required setup support files:")
        lines.extend(f"- `{item}`" for item in payload["target_missing_required_setup_support_paths"])
        lines.append(
            "These reusable schema/template files are required for setup completeness. They are skipped by ID validation but must still be present."
        )
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
        "- This preview is not executable release-channel behavior, a package-manager update, a rollback plan, a CLI contract, or install permission.",
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
        "- This plan is not an installer, update command, executable release channel, package-manager operation, rollback plan, CLI contract, copy approval, or edit approval.",
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
        "- This apply mode does not adapt owner files, overwrite target material, install hooks, change CI, run app commands, write app code, define executable release channels, provide rollback automation, install a CLI, or provide package-manager behavior.",
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
    release = preview["release_reference"]
    lines = [
        render_plain(payload),
        "\nPackage Upgrade Preview:",
        f"- Preview kind: `{preview['preview_kind']}`",
        f"- Preview status: `{preview['status']}`",
        f"- Package state classification: `{preview['package_state_classification']}`",
        f"- Source package: `{release['source_package_name']}` `{release['source_package_version']}`",
        f"- Inferred source release label: `{release['inferred_source_release_label']}`",
        "- Registry lookup performed: no",
        f"- Compatibility policy: {preview['updater_compatibility_policy']['policy_name']}",
        f"- Compatibility threshold: {preview['updater_compatibility_policy']['evidence_threshold']}",
        f"- Clone-first support case: {preview['updater_compatibility_policy']['clone_first_support']}",
        "- Release terms: stable is the maintainer-reviewed default acquisition reference when available; latest is the newest package reference to inspect, not overwrite permission; pinned is an explicit version or source checkout for comparison.",
        "- Target mutation allowed: no",
        "- Writes by default: no",
        "- This preview is not package update permission, overwrite approval, owner-file adaptation, executable release-channel behavior, package-manager behavior, hook/CI setup, rollback automation, or npm updater behavior.",
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
    if preview["required_setup_support_missing_paths"]:
        lines.append("\nRequired reusable setup support files missing:")
        lines.extend(f"- `{item}`" for item in preview["required_setup_support_missing_paths"])
        lines.append(
            "These files should appear as missing package-owned copy candidates when present in the source package; validation skip-lists do not make them optional."
        )
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


def render_update_plan_preview_plain(payload: dict[str, Any]) -> str:
    plan = payload["npm_update_plan_preview"]
    release = plan["release_reference"]
    summary = plan["action_summary"]
    lines = [
        render_upgrade_preview_plain(payload),
        "\nNpm Update Plan Preview:",
        f"- Plan kind: `{plan['plan_kind']}`",
        f"- Plan status: `{plan['status']}`",
        f"- Package state classification: `{plan['package_state_classification']}`",
        f"- Source package: `{release['source_package_name']}` `{release['source_package_version']}`",
        "- Target mutation allowed: no",
        "- Writes by default: no",
        "- Generated evidence only: yes",
        "- Registry lookup performed: no",
        "- Dist-tag resolution performed: no",
        f"- Same-session requirement: {plan['same_session_requirement']}",
        f"- Next manual gate: {plan['next_manual_gate']}",
        "\nUpdate-plan action summary:",
        f"- Total actions: {summary['total_actions']}",
        f"- Candidate package-copy actions: {summary['candidate_package_copy_count']}",
        f"- Manual-review actions: {summary['manual_review_count']}",
        f"- Blocked actions: {summary['blocked_count']}",
        f"- Deferred actions: {summary['deferred_count']}",
    ]
    if plan["grouped_action_ids"]["candidate_package_copy"]:
        lines.append("\nCandidate package-copy IDs:")
        lines.extend(f"- {item}" for item in plan["grouped_action_ids"]["candidate_package_copy"])
    if plan["grouped_action_ids"]["manual_review"]:
        lines.append("\nManual-review IDs:")
        lines.extend(f"- {item}" for item in plan["grouped_action_ids"]["manual_review"])
    if plan["grouped_action_ids"]["blocked"]:
        lines.append("\nBlocked IDs:")
        lines.extend(f"- {item}" for item in plan["grouped_action_ids"]["blocked"])
    if plan["grouped_action_ids"]["deferred"]:
        lines.append("\nDeferred IDs:")
        lines.extend(f"- {item}" for item in plan["grouped_action_ids"]["deferred"])
    lines.append("\nValidation prompts:")
    lines.extend(f"- {item}" for item in plan["validation_prompts"])
    lines.append(
        "\nUpdate-plan warning: this preview is evidence only; it is not package update permission, copy approval, npm apply behavior, registry freshness, dist-tag resolution, release-channel behavior, package-manager behavior, rollback automation, or generated-output authority."
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
        "- This apply mode does not overwrite dirty files, adapt owner files, install hooks, change CI, define executable release channels, provide rollback automation, or provide package-manager behavior.",
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


def render_fast_verified_setup_preview_plain(payload: dict[str, Any]) -> str:
    preview = payload["fast_verified_setup_preview"]
    lines = [
        render_plain(payload),
        "\nFast Verified Setup Preview:",
        f"- Preview kind: `{preview['preview_kind']}`",
        f"- Preview status: `{preview['status']}`",
        f"- Route: `{preview['route']}`",
        f"- Approval prefix: `{preview['approval_prefix']}`",
        "- Target mutation allowed: no",
        "- Writes by default: no",
        "- Generated evidence only: yes",
        "- Facade boundary: transparent delegate only; not an installer, updater, package manager, rollback helper, support-only hidden setup path, task selector, PRD approval, or bead activation.",
        f"- Next manual gate: {preview['next_manual_gate']}",
        "\nUnderlying command sequence:",
    ]
    lines.extend(f"- `{command}`" for command in preview["underlying_commands"])
    if preview["current_action_ids"]:
        lines.append("\nCurrent candidate approval IDs:")
        lines.extend(f"- `{action_id}`" for action_id in preview["current_action_ids"])
    lines.append(f"\nValidation command after approved apply: `{preview['validation_command_after_apply']}`")
    if "supervised_setup_plan" in payload:
        lines.append("\nFresh-target setup evidence:")
        plan = payload["supervised_setup_plan"]
        lines.append(f"- Plan status: `{plan['status']}`")
        lines.append(f"- Review-copy candidates: {len(action_ids(plan['actions'], 'review_copy_candidate'))}")
    if "npm_update_plan_preview" in payload:
        plan = payload["npm_update_plan_preview"]
        lines.append("\nExisting-Precode refresh evidence:")
        lines.append(f"- Plan status: `{plan['status']}`")
        lines.append(f"- Package state classification: `{plan['package_state_classification']}`")
        lines.append(f"- Candidate package-copy IDs: {len(plan['grouped_action_ids']['candidate_package_copy'])}")
    if "existing_project_adaptation_plan" in payload:
        plan = payload["existing_project_adaptation_plan"]
        lines.append("\nExisting-project intake evidence:")
        lines.append(f"- Plan status: `{plan['status']}`")
        lines.append("- Apply path: none; run Existing Repo Intake before any adaptation or copy decision.")
    lines.append(
        "\nFast setup warning: preview output is evidence only. Apply only current SP-ID or UP-ID values with explicit approval; validation remains required after copying."
    )
    return "\n".join(lines)


def render_fast_verified_setup_apply_plain(payload: dict[str, Any]) -> str:
    summary = payload["fast_verified_setup_apply"]
    lines = [
        render_fast_verified_setup_preview_plain(payload),
        "\nFast Verified Setup Apply Summary:",
        f"- Apply kind: `{summary['apply_kind']}`",
        f"- Apply status: `{summary['status']}`",
        f"- Route: `{summary['route']}`",
        "- Scope: explicit current SP-ID or UP-ID copy actions delegated to the Python Bootstrap source of truth.",
        "- This apply mode does not adapt owner files, overwrite target material, install hooks, change CI, run app commands, write app code, query registries, resolve dist-tags, define release channels, provide rollback automation, provide package-manager behavior, select tasks, approve PRDs, or activate beads.",
        "\nUnderlying command:",
    ]
    lines.extend(f"- `{command}`" for command in summary["underlying_commands"])
    if summary["copied"]:
        lines.append("\nCopied:")
        lines.extend(f"- `{item['path']}`: {item['reason']}" for item in summary["copied"])
    if summary["skipped"]:
        lines.append("\nSkipped:")
        lines.extend(f"- `{item['path']}`: {item['reason']}" for item in summary["skipped"])
    if summary["blocked"]:
        lines.append("\nBlocked:")
        lines.extend(f"- `{item['path']}`: {item['reason']}" for item in summary["blocked"])
    lines.append(f"\nValidation next step: `{summary['validation_next_step']}`")
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
    elif "npm_update_plan_preview" in payload:
        renderer = render_update_plan_preview_plain
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
    (root / ".gitignore").write_text("__pycache__/\n*.py[cod]\n", encoding="utf-8")
    (root / "package.json").write_text(
        json.dumps({"name": "@precodeos/precodeos", "version": "1.0.0-beta.1"}, indent=2) + "\n",
        encoding="utf-8",
    )


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
        assert empty_payload["setup_diagnosis"]["recommended_route"] == "supervised_setup_plan_then_validate"
        assert empty_payload["setup_diagnosis"]["target_mutation_allowed"] is False
        assert "package-manager behavior" in empty_payload["setup_diagnosis"]["not_authority_for"]
        assert not (source / "logs" / "bootstrap-check.json").exists()

        existing_target = base / "existing-target"
        existing_target.mkdir()
        (existing_target / "README.md").write_text("Existing README\n", encoding="utf-8")
        (existing_target / "package.json").write_text("{}\n", encoding="utf-8")
        existing_payload = build_payload(source.as_posix(), existing_target.as_posix())
        assert existing_payload["target_kind"] == "existing_project"
        assert existing_payload["status"] == "warning"
        assert existing_payload["setup_diagnosis"]["recommended_route"] == "existing_repo_intake_before_setup_mutation"
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

        local_tooling_target = base / "local-tooling-target"
        local_tooling_target.mkdir()
        (local_tooling_target / ".git").mkdir()
        (local_tooling_target / ".claude").mkdir()
        (local_tooling_target / ".claude" / "settings.local.json").write_text("{}\n", encoding="utf-8")
        local_tooling_payload = build_payload(source.as_posix(), local_tooling_target.as_posix())
        local_tooling_payload["install_update_preview"] = build_manifest_preview(local_tooling_payload)
        local_tooling_payload["supervised_setup_plan"] = build_supervised_setup_plan(local_tooling_payload)
        assert local_tooling_payload["target_kind"] == "nearly_empty"
        assert local_tooling_payload["supervised_setup_plan"]["status"] == "pass"
        assert any(
            action["category"] == "review_copy_candidate" and action["path"] == ".gitignore"
            for action in local_tooling_payload["supervised_setup_plan"]["actions"]
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
        existing_payload["fast_verified_setup_preview"] = build_fast_verified_setup_preview(existing_payload)
        assert existing_payload["fast_verified_setup_preview"]["route"] == "existing_project_intake"
        assert existing_payload["fast_verified_setup_preview"]["current_action_ids"] == []
        assert any(
            "scripts/existing-repo-intake.py" in command
            for command in existing_payload["fast_verified_setup_preview"]["underlying_commands"]
        )
        assert "no existing-app apply path" in existing_payload["fast_verified_setup_preview"]["next_manual_gate"]

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
        assert missing_target_payload["setup_diagnosis"]["source_target_clarity"] == "unclear_or_blocked"
        assert missing_target_payload["setup_diagnosis"]["partial_setup_classification"] == "target_missing"
        missing_target_payload["install_update_preview"] = build_manifest_preview(missing_target_payload)
        missing_target_payload["supervised_setup_plan"] = build_supervised_setup_plan(missing_target_payload)
        assert any(action["path"] == "<target-project-root>" for action in missing_target_payload["install_update_preview"]["actions"])
        assert any(action["path"] == "<target-project-root>" for action in missing_target_payload["supervised_setup_plan"]["actions"])

        same_payload = build_payload(source.as_posix(), source.as_posix())
        assert same_payload["target_kind"] == "same_as_source"
        assert same_payload["status"] == "blocked"
        assert same_payload["setup_diagnosis"]["target_state"] == "wrong_folder"
        assert same_payload["setup_diagnosis"]["recommended_route"] == "stop_and_choose_target"
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
        (existing_precode_target / "tasks" / "prds" / ".gitkeep").write_text("", encoding="utf-8")
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
        existing_precode_payload["npm_update_plan_preview"] = build_update_plan_preview(existing_precode_payload)
        existing_precode_payload["bootstrap_recovery_guidance"] = build_recovery_guidance(existing_precode_payload)
        assert existing_precode_payload["target_kind"] == "existing_precode"
        assert set(existing_precode_payload["target_missing_required_setup_support_paths"]) == {
            "tasks/beads/BEAD-SCHEMA.md",
            "tasks/prds/PRD-000-template.md",
            "tasks/prds/PRD-SHARD-SCHEMA.md",
        }
        assert existing_precode_payload["setup_diagnosis"]["partial_setup_classification"] == "required_support_files_missing"
        assert existing_precode_payload["setup_diagnosis"]["recommended_route"] == "package_owned_refresh_then_validate"
        assert "Inspect target git status" in " ".join(existing_precode_payload["setup_diagnosis"]["validation_after_apply"])
        assert "do not create a new setup command or support-only setup path" in existing_precode_payload["setup_diagnosis"]["forbidden_next_actions"]
        assert "target is missing required reusable setup support files" in existing_precode_payload["warnings"]
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
        assert set(existing_precode_payload["package_upgrade_preview"]["required_setup_support_missing_paths"]) == {
            "tasks/beads/BEAD-SCHEMA.md",
            "tasks/prds/PRD-000-template.md",
            "tasks/prds/PRD-SHARD-SCHEMA.md",
        }
        required_support_actions = [
            action
            for action in existing_precode_payload["package_upgrade_preview"]["actions"]
            if action["category"] == "review_package_copy_candidate"
            and action["path"] in existing_precode_payload["target_missing_required_setup_support_paths"]
        ]
        assert {action["path"] for action in required_support_actions} == set(
            existing_precode_payload["target_missing_required_setup_support_paths"]
        )
        release_reference = existing_precode_payload["package_upgrade_preview"]["release_reference"]
        compatibility_policy = existing_precode_payload["package_upgrade_preview"]["updater_compatibility_policy"]
        assert release_reference["source_package_name"] == "@precodeos/precodeos"
        assert release_reference["source_package_version"] == "1.0.0-beta.1"
        assert release_reference["inferred_source_release_label"] == "beta"
        assert release_reference["registry_lookup_performed"] is False
        assert release_reference["dist_tag_resolution_performed"] is False
        assert "latest is not safe-to-overwrite permission" in release_reference["term_definitions"]["latest"]
        assert "npm updater behavior" in release_reference["boundary"]
        assert compatibility_policy["policy_name"] == "npm Updater Evidence And Compatibility Policy"
        assert compatibility_policy["policy_prd"] == "tasks/prds/PRD-041-npm-updater-evidence-and-compatibility-policy.md"
        assert "package state is clean" in " ".join(compatibility_policy["compatible_only_when"])
        assert "dirty_package_edits" in compatibility_policy["blocked_update_cases"]
        assert "blocked_identity_collision" in compatibility_policy["blocked_update_cases"]
        assert "package-manager behavior" in compatibility_policy["not_authority_for"]
        update_plan = existing_precode_payload["npm_update_plan_preview"]
        assert update_plan["plan_kind"] == "npm_update_plan_preview"
        assert update_plan["target_mutation_allowed"] is False
        assert update_plan["writes_by_default"] is False
        assert update_plan["generated_evidence_only"] is True
        assert update_plan["optional_registry_metadata"]["registry_lookup_performed"] is False
        assert update_plan["optional_registry_metadata"]["dist_tag_resolution_performed"] is False
        assert "same-session preview" in update_plan["same_session_requirement"]
        assert "npm apply behavior" in update_plan["not_authority_for"]
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
        assert upgrade_copy_ids[0] in update_plan["grouped_action_ids"]["candidate_package_copy"]
        assert update_plan["action_summary"]["candidate_package_copy_count"] >= 1
        rendered_update_plan = render_update_plan_preview_plain(existing_precode_payload)
        assert "Npm Update Plan Preview" in rendered_update_plan
        assert "Registry lookup performed: no" in rendered_update_plan
        assert "not package update permission" in rendered_update_plan
        assert "Dist-tag resolution performed: no" in rendered_update_plan
        fast_precode_target = base / "fast-existing-precode-target"
        make_source(fast_precode_target)
        fast_precode_payload = build_payload(source.as_posix(), fast_precode_target.as_posix())
        fast_precode_payload["install_update_preview"] = build_manifest_preview(fast_precode_payload)
        fast_precode_payload["supervised_setup_plan"] = build_supervised_setup_plan(fast_precode_payload)
        fast_precode_payload["existing_project_adaptation_plan"] = build_existing_project_adaptation_plan(fast_precode_payload)
        fast_precode_payload["package_upgrade_preview"] = build_upgrade_preview(fast_precode_payload)
        fast_precode_payload["npm_update_plan_preview"] = build_update_plan_preview(fast_precode_payload)
        fast_precode_payload["fast_verified_setup_preview"] = build_fast_verified_setup_preview(fast_precode_payload)
        assert fast_precode_payload["fast_verified_setup_preview"]["route"] == "existing_precode_refresh"
        assert fast_precode_payload["fast_verified_setup_preview"]["approval_prefix"] == "UP"
        assert any(
            "--update-plan-preview" in command
            for command in fast_precode_payload["fast_verified_setup_preview"]["underlying_commands"]
        )
        fast_upgrade_copy_ids = [
            action["id"]
            for action in fast_precode_payload["package_upgrade_preview"]["actions"]
            if action["category"] == "review_package_copy_candidate" and action["path"] == "docs/NEW-PACKAGE-DOC.md"
        ]
        assert len(fast_upgrade_copy_ids) == 1
        fast_precode_apply = build_fast_verified_setup_apply(fast_precode_payload, fast_upgrade_copy_ids)
        assert fast_precode_apply["status"] == "applied"
        assert (fast_precode_target / "docs" / "NEW-PACKAGE-DOC.md").is_file()
        assert fast_precode_apply["validation_next_step"] == validation_command(str(fast_precode_payload["target_root"]))
        fast_mixed_apply = build_fast_verified_setup_apply(fast_precode_payload, ["SP-001", fast_upgrade_copy_ids[0]])
        assert fast_mixed_apply["status"] == "blocked"
        assert any("do not mix" in item["reason"] for item in fast_mixed_apply["blocked"])
        collision_apply = apply_upgrade_preview(existing_precode_payload, [prd_collision_actions[0]["id"]])
        assert collision_apply["status"] == "blocked"
        assert any("identity collision" in item["reason"] for item in collision_apply["blocked"])
        upgrade_apply = apply_upgrade_preview(existing_precode_payload, upgrade_copy_ids)
        assert upgrade_apply["status"] == "applied"
        assert (existing_precode_target / "docs" / "NEW-PACKAGE-DOC.md").is_file()
        assert "validate memory" in existing_precode_payload["bootstrap_recovery_guidance"]["likely_recovery_path"]

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
        assert ".gitignore" in preview_copy_paths
        assert ".gitignore" in setup_copy_paths
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
        assert "Setup diagnosis:" in rendered_setup_plan
        assert "Recommended route: `supervised_setup_plan_then_validate`" in rendered_setup_plan
        assert "evidence only" in rendered_setup_plan
        assert "does not approve copying" in rendered_setup_plan
        fast_empty_payload = dict(empty_payload)
        fast_empty_payload["existing_project_adaptation_plan"] = build_existing_project_adaptation_plan(fast_empty_payload)
        fast_empty_payload["package_upgrade_preview"] = build_upgrade_preview(fast_empty_payload)
        fast_empty_payload["npm_update_plan_preview"] = build_update_plan_preview(fast_empty_payload)
        fast_empty_payload["fast_verified_setup_preview"] = build_fast_verified_setup_preview(fast_empty_payload)
        assert fast_empty_payload["fast_verified_setup_preview"]["route"] == "fresh_or_nearly_empty_setup"
        assert fast_empty_payload["fast_verified_setup_preview"]["approval_prefix"] == "SP"
        assert any(
            "--supervised-setup-plan" in command
            for command in fast_empty_payload["fast_verified_setup_preview"]["underlying_commands"]
        )
        rendered_fast_preview = render_fast_verified_setup_preview_plain(fast_empty_payload)
        assert "Fast Verified Setup Preview" in rendered_fast_preview
        assert "Underlying command sequence" in rendered_fast_preview
        fast_no_approval = build_fast_verified_setup_apply(fast_empty_payload, [])
        assert fast_no_approval["status"] == "blocked"
        assert any("at least one" in item["reason"] for item in fast_no_approval["blocked"])
        fast_unknown = build_fast_verified_setup_apply(fast_empty_payload, ["SP-999"])
        assert fast_unknown["status"] == "blocked"
        assert any("not present in the setup plan" in item["reason"] for item in fast_unknown["blocked"])
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
        fast_apply_target = base / "fast-apply-target"
        fast_apply_target.mkdir()
        fast_apply_payload = build_payload(source.as_posix(), fast_apply_target.as_posix())
        fast_apply_payload["install_update_preview"] = build_manifest_preview(fast_apply_payload)
        fast_apply_payload["supervised_setup_plan"] = build_supervised_setup_plan(fast_apply_payload)
        fast_apply_payload["fast_verified_setup_preview"] = build_fast_verified_setup_preview(fast_apply_payload)
        fast_setup_apply = build_fast_verified_setup_apply(fast_apply_payload, approved_copy_ids)
        assert fast_setup_apply["status"] == "applied"
        assert (fast_apply_target / "AGENT.md").is_file()
        assert fast_setup_apply["validation_next_step"] == validation_command(str(fast_apply_payload["target_root"]))
        rendered_fast_apply = render_fast_verified_setup_apply_plain(
            {**fast_apply_payload, "fast_verified_setup_apply": fast_setup_apply}
        )
        assert "Fast Verified Setup Apply Summary" in rendered_fast_apply

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

        gitignore_copy_ids = [
            action["id"]
            for action in apply_payload["supervised_setup_plan"]["actions"]
            if action["category"] == "review_copy_candidate" and action["path"] == ".gitignore"
        ]
        assert len(gitignore_copy_ids) == 1
        gitignore_apply_target = base / "gitignore-apply-target"
        gitignore_apply_target.mkdir()
        gitignore_apply_payload = build_payload(source.as_posix(), gitignore_apply_target.as_posix())
        gitignore_apply_payload["install_update_preview"] = build_manifest_preview(gitignore_apply_payload)
        gitignore_apply_payload["supervised_setup_plan"] = build_supervised_setup_plan(gitignore_apply_payload)
        gitignore_apply_payload["supervised_setup_apply"] = apply_supervised_setup(
            gitignore_apply_payload,
            gitignore_copy_ids,
        )
        assert gitignore_apply_payload["supervised_setup_apply"]["status"] == "applied"
        assert "__pycache__/" in (gitignore_apply_target / ".gitignore").read_text(encoding="utf-8")

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
        "--update-plan-preview",
        action="store_true",
        help="include non-mutating npm update-plan preview output for existing Precode targets; implies --upgrade-preview",
    )
    parser.add_argument(
        "--fast-verified-setup-preview",
        action="store_true",
        help="include transparent fast verified setup command sequencing over existing bootstrap paths",
    )
    parser.add_argument(
        "--fast-verified-setup-apply",
        action="store_true",
        help="apply explicitly approved current SP-ID or UP-ID copy actions through the fast verified setup facade",
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
    if args.fast_verified_setup_apply and not args.approve_action:
        parser.error("--fast-verified-setup-apply requires at least one --approve-action <SP-ID|UP-ID>")

    payload = build_payload(args.source, args.target)
    fast_mode = args.fast_verified_setup_preview or args.fast_verified_setup_apply
    target_route_kind = str(payload["target_kind"])
    fast_apply_prefixes = approved_action_prefixes(args.approve_action) if args.fast_verified_setup_apply else set()
    needs_fresh_setup = (
        args.preview_manifest
        or args.supervised_setup_plan
        or (args.fast_verified_setup_preview and target_route_kind in {"empty", "nearly_empty"})
        or (args.fast_verified_setup_apply and "SP" in fast_apply_prefixes)
    )
    needs_existing_project = (
        args.existing_project_adaptation_plan
        or (args.fast_verified_setup_preview and target_route_kind == "existing_project")
        or (args.fast_verified_setup_apply and target_route_kind == "existing_project")
    )
    needs_existing_precode = (
        args.upgrade_preview
        or args.update_plan_preview
        or (args.fast_verified_setup_preview and target_route_kind == "existing_precode")
        or (args.fast_verified_setup_apply and "UP" in fast_apply_prefixes)
    )
    if needs_fresh_setup:
        payload["install_update_preview"] = build_manifest_preview(payload)
    if args.supervised_setup_plan or needs_fresh_setup:
        payload["supervised_setup_plan"] = build_supervised_setup_plan(payload)
    if needs_existing_project:
        payload["existing_project_adaptation_plan"] = build_existing_project_adaptation_plan(payload)
    if needs_existing_precode:
        payload["package_upgrade_preview"] = build_upgrade_preview(payload)
    if args.update_plan_preview or needs_existing_precode:
        payload["npm_update_plan_preview"] = build_update_plan_preview(payload)
    if args.recovery_guidance:
        payload["bootstrap_recovery_guidance"] = build_recovery_guidance(payload)
    if args.apply_supervised_setup:
        payload["supervised_setup_apply"] = apply_supervised_setup(payload, args.approve_action)
    if args.apply_upgrade_preview:
        payload["package_upgrade_apply"] = apply_upgrade_preview(payload, args.approve_action)
    if args.fast_verified_setup_preview or args.fast_verified_setup_apply:
        payload["fast_verified_setup_preview"] = build_fast_verified_setup_preview(payload)
    if args.fast_verified_setup_apply:
        payload["fast_verified_setup_apply"] = build_fast_verified_setup_apply(payload, args.approve_action)
    if args.write_evidence:
        if payload["source_root"] == payload["target_root"]:
            raise SystemExit("bootstrap-check: refusing to write evidence when source and target are the same")
        if "source path does not exist or is not a directory" in payload["blockers"]:
            raise SystemExit("bootstrap-check: refusing to write evidence because source is missing")
        write_evidence(payload)
    if args.json:
        print(json.dumps(payload, indent=2, sort_keys=True))
    else:
        if args.fast_verified_setup_apply:
            print(render_fast_verified_setup_apply_plain(payload))
        elif args.fast_verified_setup_preview:
            print(render_fast_verified_setup_preview_plain(payload))
        elif args.apply_upgrade_preview:
            print(render_upgrade_apply_plain(payload))
        elif args.update_plan_preview:
            print(render_update_plan_preview_plain(payload))
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
