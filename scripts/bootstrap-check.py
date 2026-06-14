#!/usr/bin/env python3
# Version: v0.2.0
# Last updated: 2026-06-14
# Owner: PrecodeOS
# Created by Dan Sears / Recode.
# SPDX-License-Identifier: Apache-2.0
from __future__ import annotations

import argparse
import json
import shutil
import tempfile
from pathlib import Path
from typing import Any


PUBLIC_FILE_GROUPS: list[dict[str, Any]] = [
    {"group": "active_memory", "paths": ["AGENT.md", "DECISIONS.md", "tasks/todo.md"]},
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
        "paths": ["README.md", "docs/", "CONTRIBUTING.md", "GOVERNANCE.md", "TRADEMARK.md", "NOTICE", "LICENSE"],
    },
    {
        "group": "agent_shims_and_adapters",
        "paths": ["AGENTS.md", "CLAUDE.md", "GEMINI.md", ".github/copilot-instructions.md", "adapters/"],
    },
    {
        "group": "work_structure",
        "paths": ["tasks/beads/", "tasks/prds/", "tasks/reference/", "tasks/templates/", "modes/", "memory/"],
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

SOURCE_REQUIRED_PATHS = ["AGENT.md", "DECISIONS.md", "tasks/todo.md", "docs/PRECODE-GUIDED-SETUP.md"]
CONFLICT_PATHS = [
    "README.md",
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
DEFERRED_SETUP_PATHS = {
    ".githooks/",
    ".github/workflows/",
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


def write_evidence(payload: dict[str, Any]) -> None:
    source = Path(str(payload["source_root"]))
    logs = source / "logs"
    logs.mkdir(parents=True, exist_ok=True)
    (logs / "bootstrap-check.json").write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    renderer = render_preview_plain if "install_update_preview" in payload else render_plain
    (logs / "bootstrap-check.md").write_text(renderer(payload) + "\n", encoding="utf-8")


def make_source(root: Path) -> None:
    for name in SOURCE_REQUIRED_PATHS:
        path = root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("fixture\n", encoding="utf-8")


def self_test() -> int:
    with tempfile.TemporaryDirectory() as tmp:
        base = Path(tmp)
        source = base / "source"
        source.mkdir()
        make_source(source)

        empty_target = base / "empty-target"
        empty_target.mkdir()
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
        assert nearly_empty_payload["target_kind"] == "nearly_empty"
        assert any(
            action["category"] == "adapt_candidate" and action["path"] == "README.md"
            for action in nearly_empty_payload["install_update_preview"]["actions"]
        )

        existing_payload["install_update_preview"] = build_manifest_preview(existing_payload)
        assert any(
            action["category"] == "deferred" and action["path"] == "scripts/existing-repo-intake.py"
            for action in existing_payload["install_update_preview"]["actions"]
        )

        missing_source_payload = build_payload((base / "missing-source").as_posix(), empty_target.as_posix())
        assert missing_source_payload["status"] == "blocked"
        assert "source path does not exist or is not a directory" in missing_source_payload["blockers"]
        missing_source_payload["install_update_preview"] = build_manifest_preview(missing_source_payload)
        assert any(action["category"] == "blocked" for action in missing_source_payload["install_update_preview"]["actions"])

        missing_target_payload = build_payload(source.as_posix(), (base / "missing-target").as_posix())
        assert missing_target_payload["target_kind"] == "missing"
        assert missing_target_payload["status"] == "blocked"
        missing_target_payload["install_update_preview"] = build_manifest_preview(missing_target_payload)
        assert any(action["path"] == "<target-project-root>" for action in missing_target_payload["install_update_preview"]["actions"])

        same_payload = build_payload(source.as_posix(), source.as_posix())
        assert same_payload["target_kind"] == "same_as_source"
        assert same_payload["status"] == "blocked"
        same_payload["install_update_preview"] = build_manifest_preview(same_payload)
        assert any(action["category"] == "blocked" for action in same_payload["install_update_preview"]["actions"])

        existing_precode_target = base / "existing-precode-target"
        make_source(existing_precode_target)
        existing_precode_payload = build_payload(source.as_posix(), existing_precode_target.as_posix())
        existing_precode_payload["install_update_preview"] = build_manifest_preview(existing_precode_payload)
        assert existing_precode_payload["target_kind"] == "existing_precode"
        assert any(
            action["category"] == "preserve_existing"
            for action in existing_precode_payload["install_update_preview"]["actions"]
        )

        empty_payload["install_update_preview"] = build_manifest_preview(empty_payload)
        assert any(
            action["category"] == "copy_candidate" for action in empty_payload["install_update_preview"]["actions"]
        )
        json.dumps(empty_payload, sort_keys=True)

        write_evidence(empty_payload)
        assert (source / "logs" / "bootstrap-check.json").is_file()
        assert (source / "logs" / "bootstrap-check.md").is_file()
        assert "Install/Update Manifest Dry-Run Preview" in (source / "logs" / "bootstrap-check.md").read_text(
            encoding="utf-8"
        )
        assert not (empty_target / "logs").exists()

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
    parser.add_argument("--write-evidence", action="store_true", help="write generated evidence under the source logs directory")
    parser.add_argument("--self-test", action="store_true", help="run fixture-style bootstrap confidence checks")
    args = parser.parse_args()

    if args.self_test:
        return self_test()

    if not args.source or not args.target:
        parser.error("--source and --target are required unless --self-test is used")

    payload = build_payload(args.source, args.target)
    if args.preview_manifest:
        payload["install_update_preview"] = build_manifest_preview(payload)
    if args.write_evidence:
        if payload["source_root"] == payload["target_root"]:
            raise SystemExit("bootstrap-check: refusing to write evidence when source and target are the same")
        if "source path does not exist or is not a directory" in payload["blockers"]:
            raise SystemExit("bootstrap-check: refusing to write evidence because source is missing")
        write_evidence(payload)
    if args.json:
        print(json.dumps(payload, indent=2, sort_keys=True))
    else:
        print(render_preview_plain(payload) if args.preview_manifest else render_plain(payload))
        if args.write_evidence:
            print("bootstrap-check: wrote logs/bootstrap-check.json and logs/bootstrap-check.md in the source workspace")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
