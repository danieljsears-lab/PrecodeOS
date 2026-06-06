#!/usr/bin/env python3
# Version: v0.1.0
# Last updated: 2026-06-06
# Owner: PrecodeOS
# Created by Dan Sears / Recode.
# SPDX-License-Identifier: Apache-2.0
from __future__ import annotations

import argparse
import json
import os
import tempfile
from pathlib import Path
from typing import Any


SOURCE_REQUIRED_PATHS = ["AGENT.md", "DECISIONS.md", "tasks/todo.md", "docs/PRECODE-GUIDED-SETUP.md"]
MINIMAL_TARGET_NAMES = {".git", ".gitignore", "README.md", "LICENSE"}
SKIP_DIRS = {
    ".git",
    ".hg",
    ".svn",
    ".next",
    ".nuxt",
    ".svelte-kit",
    ".turbo",
    ".cache",
    ".venv",
    "venv",
    "env",
    "node_modules",
    "dist",
    "build",
    "coverage",
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
    ".ruff_cache",
    "target",
}
SENSITIVE_NAMES = {
    ".env",
    ".env.local",
    ".env.development",
    ".env.production",
    "secrets",
    "credentials",
    "private.key",
    "id_rsa",
    "id_ed25519",
}
SECRET_EXTENSIONS = {".pem", ".key", ".crt", ".p12", ".pfx"}
OWNER_FILES = [
    "PRODUCT.md",
    "PROJECT-CONTEXT.md",
    "FEATURES.md",
    "ACCEPTANCE.md",
    "ARCHITECTURE.md",
    "API.md",
    "DATA-MODELS.md",
    "SECURITY.md",
    "CODEBASE-GUIDE.md",
]
PRECODE_ACTIVE_MEMORY = ["AGENT.md", "DECISIONS.md", "tasks/todo.md"]
DOC_CANDIDATES = [
    "README.md",
    "ARCHITECTURE.md",
    "API.md",
    "DATA-MODELS.md",
    "SECURITY.md",
    "CONTRIBUTING.md",
    "docs",
]
CI_DEPLOY_CANDIDATES = [
    ".github/workflows",
    ".gitlab-ci.yml",
    "bitbucket-pipelines.yml",
    "vercel.json",
    "netlify.toml",
    "render.yaml",
    "fly.toml",
    "Procfile",
    "Dockerfile",
    "docker-compose.yml",
]
APP_DIR_HINTS = ["app", "src", "pages", "frontend", "backend", "web", "client", "server", "api", "packages", "apps"]
STOP_CONDITIONS = [
    "source and target are unclear",
    "source and target resolve to the same folder",
    "target is empty and should use the fresh install path instead",
    "existing project docs conflict with Precode owner files",
    "current app directory or repo topology is unclear",
    "secrets, production access, auth, payments, deployment settings, or private dashboards are needed",
    "CI, Git hooks, package files, migrations, or external systems would need mutation",
    "existing active work is uncommitted or unclear",
    "generated intake output is treated as authority or install permission",
]


def resolve_candidate(raw: str) -> Path:
    return Path(raw).expanduser().resolve(strict=False)


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
    if all((target / name).exists() for name in PRECODE_ACTIVE_MEMORY):
        return "existing_precode"
    return "existing_project"


def rel(path: Path, root: Path) -> str:
    return path.relative_to(root).as_posix()


def safe_read_json(path: Path) -> dict[str, Any]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError):
        return {}
    return data if isinstance(data, dict) else {}


def safe_read_text(path: Path, limit: int = 8192) -> str:
    try:
        return path.read_text(encoding="utf-8")[:limit]
    except (OSError, UnicodeDecodeError):
        return ""


def bounded_files(root: Path, max_depth: int = 4, max_files: int = 2500) -> list[Path]:
    if not root.is_dir():
        return []
    files: list[Path] = []
    for current, dirs, names in os.walk(root):
        current_path = Path(current)
        depth = len(current_path.relative_to(root).parts)
        dirs[:] = [name for name in dirs if name not in SKIP_DIRS and depth < max_depth]
        for name in sorted(names):
            files.append(current_path / name)
            if len(files) >= max_files:
                return sorted(files)
    return sorted(files)


def path_exists(target: Path, relative: str) -> bool:
    return (target / relative).exists()


def manifest_paths(files: list[Path], target: Path) -> set[str]:
    return {rel(path, target) for path in files}


def package_json_findings(target: Path, paths: set[str]) -> dict[str, Any]:
    package_paths = [item for item in sorted(paths) if item.endswith("package.json")]
    package_managers: set[str] = set()
    frameworks: set[str] = set()
    runtimes: set[str] = set()
    build_tools: set[str] = set()
    likely_checks: list[dict[str, str]] = []
    for relative in package_paths:
        base = str(Path(relative).parent)
        prefix = "" if base == "." else f"{base}: "
        package = safe_read_json(target / relative)
        scripts = package.get("scripts") if isinstance(package.get("scripts"), dict) else {}
        deps: dict[str, Any] = {}
        for key in ("dependencies", "devDependencies", "peerDependencies"):
            value = package.get(key)
            if isinstance(value, dict):
                deps.update(value)
        for name in deps:
            if name in {"next", "react", "react-dom"}:
                frameworks.add("React/Next.js" if name == "next" else "React")
            if name in {"vue", "nuxt"}:
                frameworks.add("Vue/Nuxt" if name == "nuxt" else "Vue")
            if name in {"svelte", "@sveltejs/kit"}:
                frameworks.add("Svelte/SvelteKit")
            if name in {"express", "fastify", "koa", "hono"}:
                frameworks.add(f"Node {name}")
            if name in {"vite", "webpack", "turbo", "typescript", "eslint", "jest", "vitest", "playwright", "cypress"}:
                build_tools.add(name)
        runtimes.add("Node.js")
        package_managers.add("npm/yarn/pnpm candidate")
        for script_name in ("test", "lint", "build", "typecheck"):
            if script_name in scripts:
                likely_checks.append(
                    {
                        "command": f"{prefix}npm run {script_name}",
                        "reason": f"`{relative}` defines a `{script_name}` script; future hint only, not run during intake",
                    }
                )
    if any(path_exists(target, name) for name in ("pnpm-lock.yaml", "pnpm-workspace.yaml")):
        package_managers.add("pnpm")
    if path_exists(target, "yarn.lock"):
        package_managers.add("yarn")
    if path_exists(target, "package-lock.json"):
        package_managers.add("npm")
    return {
        "package_managers": sorted(package_managers),
        "frameworks": sorted(frameworks),
        "runtimes": sorted(runtimes),
        "build_tools": sorted(build_tools),
        "likely_checks": likely_checks,
    }


def python_findings(target: Path, paths: set[str]) -> dict[str, Any]:
    package_managers: set[str] = set()
    frameworks: set[str] = set()
    runtimes: set[str] = set()
    build_tools: set[str] = set()
    likely_checks: list[dict[str, str]] = []
    has_python = any(path in paths for path in ("pyproject.toml", "requirements.txt", "setup.py", "Pipfile", "poetry.lock"))
    if not has_python:
        return {
            "package_managers": [],
            "frameworks": [],
            "runtimes": [],
            "build_tools": [],
            "likely_checks": [],
        }
    runtimes.add("Python")
    if "pyproject.toml" in paths:
        package_managers.add("pyproject")
        text = safe_read_text(target / "pyproject.toml").lower()
        for name in ("pytest", "ruff", "mypy", "black"):
            if name in text:
                build_tools.add(name)
        if "django" in text:
            frameworks.add("Django")
        if "fastapi" in text:
            frameworks.add("FastAPI")
        if "flask" in text:
            frameworks.add("Flask")
    if "requirements.txt" in paths:
        package_managers.add("pip requirements")
        text = safe_read_text(target / "requirements.txt").lower()
        if "django" in text:
            frameworks.add("Django")
        if "fastapi" in text:
            frameworks.add("FastAPI")
        if "flask" in text:
            frameworks.add("Flask")
        if "pytest" in text:
            build_tools.add("pytest")
    if "poetry.lock" in paths:
        package_managers.add("poetry")
    if "Pipfile" in paths:
        package_managers.add("pipenv")
    if "pytest" in build_tools or "pytest.ini" in paths:
        likely_checks.append({"command": "pytest", "reason": "Python test configuration or dependency detected; future hint only"})
    if "ruff" in build_tools or ".ruff.toml" in paths:
        likely_checks.append({"command": "ruff check .", "reason": "Ruff configuration or dependency detected; future hint only"})
    if "mypy" in build_tools or "mypy.ini" in paths:
        likely_checks.append({"command": "mypy .", "reason": "Mypy configuration or dependency detected; future hint only"})
    return {
        "package_managers": sorted(package_managers),
        "frameworks": sorted(frameworks),
        "runtimes": sorted(runtimes),
        "build_tools": sorted(build_tools),
        "likely_checks": likely_checks,
    }


def other_stack_findings(target: Path, paths: set[str]) -> dict[str, Any]:
    package_managers: set[str] = set()
    frameworks: set[str] = set()
    runtimes: set[str] = set()
    build_tools: set[str] = set()
    likely_checks: list[dict[str, str]] = []
    if "Cargo.toml" in paths:
        package_managers.add("cargo")
        runtimes.add("Rust")
        build_tools.add("cargo")
        likely_checks.append({"command": "cargo test", "reason": "`Cargo.toml` detected; future hint only"})
    if "go.mod" in paths:
        package_managers.add("go modules")
        runtimes.add("Go")
        build_tools.add("go")
        likely_checks.append({"command": "go test ./...", "reason": "`go.mod` detected; future hint only"})
    if "Gemfile" in paths:
        package_managers.add("bundler")
        runtimes.add("Ruby")
        text = safe_read_text(target / "Gemfile").lower()
        if "rails" in text:
            frameworks.add("Rails")
        likely_checks.append({"command": "bundle exec rspec", "reason": "`Gemfile` detected; future hint only"})
    return {
        "package_managers": sorted(package_managers),
        "frameworks": sorted(frameworks),
        "runtimes": sorted(runtimes),
        "build_tools": sorted(build_tools),
        "likely_checks": likely_checks,
    }


def merge_findings(*items: dict[str, Any]) -> dict[str, Any]:
    merged: dict[str, Any] = {
        "package_managers": set(),
        "frameworks": set(),
        "runtimes": set(),
        "build_tools": set(),
        "likely_checks": [],
    }
    for item in items:
        for key in ("package_managers", "frameworks", "runtimes", "build_tools"):
            merged[key].update(item.get(key, []))
        merged["likely_checks"].extend(item.get("likely_checks", []))
    return {
        "package_managers": sorted(merged["package_managers"]),
        "frameworks": sorted(merged["frameworks"]),
        "runtimes": sorted(merged["runtimes"]),
        "build_tools": sorted(merged["build_tools"]),
        "likely_checks": merged["likely_checks"],
    }


def repo_topology(target: Path, paths: set[str]) -> str:
    if "pnpm-workspace.yaml" in paths or "turbo.json" in paths:
        return "workspace_or_monorepo"
    if any(item.startswith("apps/") or item.startswith("packages/") for item in paths):
        return "workspace_or_monorepo"
    if any((target / name).is_dir() for name in ("frontend", "backend", "client", "server")):
        return "multi_app_or_split_dirs"
    return "single_repo_or_unknown"


def likely_app_dirs(target: Path, paths: set[str]) -> list[dict[str, str]]:
    hints: list[dict[str, str]] = []
    seen: set[str] = set()
    for name in APP_DIR_HINTS:
        candidate = target / name
        if candidate.is_dir() and name not in seen:
            hints.append({"path": name, "reason": "common app or package directory name"})
            seen.add(name)
    for marker in ("package.json", "pyproject.toml", "Cargo.toml", "go.mod", "Gemfile"):
        for item in sorted(paths):
            if item.endswith(marker):
                parent = str(Path(item).parent)
                label = "." if parent == "." else parent
                if label not in seen:
                    hints.append({"path": label, "reason": f"`{marker}` found here"})
                    seen.add(label)
    return hints


def doc_hints(target: Path) -> list[str]:
    docs: list[str] = []
    for item in DOC_CANDIDATES:
        if (target / item).exists():
            docs.append(item)
    return docs


def ci_deploy_hints(target: Path) -> list[str]:
    return [item for item in CI_DEPLOY_CANDIDATES if (target / item).exists()]


def generated_ignored_surfaces(target: Path) -> list[str]:
    surfaces: list[str] = []
    for item in sorted(SKIP_DIRS):
        if (target / item).exists():
            surfaces.append(item)
    if (target / ".gitignore").exists():
        surfaces.append(".gitignore")
    return surfaces


def sensitive_path_patterns(files: list[Path], target: Path) -> list[dict[str, str]]:
    findings: list[dict[str, str]] = []
    for path in files:
        name = path.name
        lowered = name.lower()
        if lowered in SENSITIVE_NAMES or path.suffix.lower() in SECRET_EXTENSIONS or "secret" in lowered or "credential" in lowered:
            findings.append({"path": rel(path, target), "reason": "sensitive path pattern detected; contents not read"})
    for dirname in ("secrets", "credentials"):
        if (target / dirname).exists() and all(item["path"] != dirname for item in findings):
            findings.append({"path": dirname, "reason": "sensitive directory pattern detected; contents not read"})
    return findings[:50]


def owner_file_gaps(target: Path) -> list[dict[str, str]]:
    gaps: list[dict[str, str]] = []
    for item in OWNER_FILES:
        if not (target / item).exists():
            gaps.append({"path": item, "reason": "Precode owner file not present; propose adaptation only after user review"})
    return gaps


def conflicts(target: Path) -> list[dict[str, str]]:
    found: list[dict[str, str]] = []
    for item in ["README.md", *OWNER_FILES, ".github/workflows", ".githooks"]:
        if (target / item).exists():
            found.append({"path": item, "reason": "existing project path; do not overwrite without explicit review"})
    return found


def recommended_next_step(kind: str, missing_source: list[str], conflict_items: list[dict[str, str]]) -> str:
    if missing_source:
        return "Stop and use a clean PrecodeOS package checkout before intake."
    if kind == "missing":
        return "Stop and identify the existing repo target folder before intake."
    if kind == "same_as_source":
        return "Stop; do not treat the PrecodeOS package checkout as the target app."
    if kind in {"empty", "nearly_empty"}:
        return "Use the fresh install path instead of Existing Repo Intake."
    if kind == "existing_precode":
        return "Validate Precode active memory, then decide whether this is setup, repair, update, or source intake."
    if conflict_items:
        return "Review existing project conflicts and proposed owner-file adaptations before copying anything."
    return "Review the intake summary with the user, then choose setup adaptation, Local Source Intake, PRD shaping, or an unblocker."


def build_payload(source_raw: str, target_raw: str) -> dict[str, Any]:
    source = resolve_candidate(source_raw)
    target = resolve_candidate(target_raw)
    source_exists = source.is_dir()
    target_exists = target.is_dir()
    missing_source_paths = source_missing_paths(source) if source_exists else SOURCE_REQUIRED_PATHS.copy()
    kind = target_kind(source, target, source_exists, target_exists)
    files = bounded_files(target) if target_exists and kind != "same_as_source" else []
    paths = manifest_paths(files, target) if target_exists and kind != "same_as_source" else set()
    stack = merge_findings(package_json_findings(target, paths), python_findings(target, paths), other_stack_findings(target, paths))
    conflict_items = conflicts(target) if target_exists and kind not in {"same_as_source", "empty", "nearly_empty"} else []
    sensitive = sensitive_path_patterns(files, target)
    owner_gaps = owner_file_gaps(target) if target_exists and kind not in {"same_as_source", "empty", "nearly_empty"} else []

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
    if kind in {"empty", "nearly_empty"}:
        blockers.append("target is empty or nearly empty; use fresh install path instead")
    if kind == "existing_precode":
        warnings.append("target already has Precode active memory; validate before intake or update")
    if conflict_items:
        warnings.append("target has existing project paths that must not be overwritten")
    if sensitive:
        warnings.append("sensitive path patterns detected; contents were not read")
    if not stack["likely_checks"] and kind == "existing_project":
        warnings.append("no likely checks detected from manifests or config files")

    status = "blocked" if blockers else "warning" if warnings else "pass"
    return {
        "tool": "existing-repo-intake",
        "status": status,
        "warnings": warnings,
        "blockers": blockers,
        "source_root": source.as_posix(),
        "target_root": target.as_posix(),
        "source_missing_paths": missing_source_paths,
        "target_kind": kind,
        "repo_topology": repo_topology(target, paths) if target_exists and kind != "same_as_source" else "unknown",
        "likely_app_dirs": likely_app_dirs(target, paths) if target_exists and kind != "same_as_source" else [],
        "package_managers": stack["package_managers"],
        "frameworks": stack["frameworks"],
        "runtimes": stack["runtimes"],
        "build_tools": stack["build_tools"],
        "docs": doc_hints(target) if target_exists and kind != "same_as_source" else [],
        "ci_deploy_hints": ci_deploy_hints(target) if target_exists and kind != "same_as_source" else [],
        "generated_ignored_surfaces": generated_ignored_surfaces(target) if target_exists and kind != "same_as_source" else [],
        "sensitive_path_patterns": sensitive,
        "owner_file_gaps": owner_gaps,
        "likely_checks": stack["likely_checks"],
        "conflicts": conflict_items,
        "recommended_next_step": recommended_next_step(kind, missing_source_paths, conflict_items),
        "stop_conditions": STOP_CONDITIONS,
        "writes_by_default": False,
        "generated_evidence_only": True,
        "target_mutation_allowed": False,
        "app_commands_run": False,
        "likely_checks_are_future_hints_only": True,
        "preserve_existing_project_files": True,
        "deferred": [
            "file copying",
            "owner-file adaptation",
            "Git hook installation",
            "CI mutation",
            "dependency installation",
            "lint/test/build/typecheck execution",
            "app-code edits",
            "PRD approval",
            "bead activation",
        ],
    }


def render_plain(payload: dict[str, Any]) -> str:
    lines = [
        f"Existing Repo Intake: {payload['status']}",
        f"- Source: `{payload['source_root']}`",
        f"- Target: `{payload['target_root']}`",
        f"- Target kind: `{payload['target_kind']}`",
        f"- Repo topology: `{payload['repo_topology']}`",
        f"- Recommended next step: {payload['recommended_next_step']}",
        "- Read-only default: yes; this command does not copy, edit, install hooks, change CI, run app commands, or write app code.",
        "- Preservation: existing project code, docs, package files, CI, env files, and app structure stay untouched unless the user approves a narrow adaptation.",
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
    if payload["likely_app_dirs"]:
        lines.append("\nLikely app directories:")
        for item in payload["likely_app_dirs"]:
            lines.append(f"- `{item['path']}`: {item['reason']}")
    for heading, key in (
        ("Package managers", "package_managers"),
        ("Frameworks", "frameworks"),
        ("Runtimes", "runtimes"),
        ("Build tools", "build_tools"),
        ("Docs", "docs"),
        ("CI/deploy hints", "ci_deploy_hints"),
        ("Generated or ignored surfaces", "generated_ignored_surfaces"),
    ):
        if payload[key]:
            lines.append(f"\n{heading}:")
            lines.extend(f"- `{item}`" for item in payload[key])
    if payload["likely_checks"]:
        lines.append("\nLikely checks (future hints only; not run):")
        for item in payload["likely_checks"]:
            lines.append(f"- `{item['command']}`: {item['reason']}")
    if payload["sensitive_path_patterns"]:
        lines.append("\nSensitive path patterns (contents not read):")
        for item in payload["sensitive_path_patterns"]:
            lines.append(f"- `{item['path']}`: {item['reason']}")
    if payload["conflicts"]:
        lines.append("\nExisting project conflicts:")
        for item in payload["conflicts"]:
            lines.append(f"- `{item['path']}`: {item['reason']}")
    if payload["owner_file_gaps"]:
        lines.append("\nOwner-file gaps:")
        for item in payload["owner_file_gaps"]:
            lines.append(f"- `{item['path']}`: {item['reason']}")
    lines.append("\nStop if:")
    lines.extend(f"- {item}" for item in payload["stop_conditions"])
    lines.append("\nGenerated-report warning: existing repo intake output is evidence only, not authority, install permission, PRD approval, bead activation, or proof that likely checks passed.")
    return "\n".join(lines)


def write_evidence(payload: dict[str, Any]) -> None:
    source = Path(str(payload["source_root"]))
    logs = source / "logs"
    logs.mkdir(parents=True, exist_ok=True)
    (logs / "existing-repo-intake.json").write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    (logs / "existing-repo-intake.md").write_text(render_plain(payload) + "\n", encoding="utf-8")


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
        assert empty_payload["status"] == "blocked"
        assert not (source / "logs" / "existing-repo-intake.json").exists()

        node_target = base / "node-target"
        node_target.mkdir()
        (node_target / "package.json").write_text(
            json.dumps({"dependencies": {"next": "latest"}, "scripts": {"test": "vitest", "build": "next build", "lint": "next lint"}}),
            encoding="utf-8",
        )
        (node_target / "README.md").write_text("Existing app\n", encoding="utf-8")
        (node_target / ".github" / "workflows").mkdir(parents=True)
        (node_target / ".github" / "workflows" / "ci.yml").write_text("name: ci\n", encoding="utf-8")
        (node_target / ".env.local").write_text("SECRET=value\n", encoding="utf-8")
        node_payload = build_payload(source.as_posix(), node_target.as_posix())
        assert node_payload["target_kind"] == "existing_project"
        assert "React/Next.js" in node_payload["frameworks"]
        assert any(item["command"] == "npm run test" for item in node_payload["likely_checks"])
        assert any(item["path"] == ".env.local" for item in node_payload["sensitive_path_patterns"])
        assert any(item["path"] == "README.md" for item in node_payload["conflicts"])

        python_target = base / "python-target"
        python_target.mkdir()
        (python_target / "pyproject.toml").write_text('[project]\ndependencies = ["fastapi", "pytest", "ruff"]\n', encoding="utf-8")
        python_payload = build_payload(source.as_posix(), python_target.as_posix())
        assert "Python" in python_payload["runtimes"]
        assert "FastAPI" in python_payload["frameworks"]
        assert any(item["command"] == "pytest" for item in python_payload["likely_checks"])

        mono_target = base / "mono-target"
        mono_target.mkdir()
        (mono_target / "pnpm-workspace.yaml").write_text("packages:\n  - apps/*\n", encoding="utf-8")
        (mono_target / "apps" / "web").mkdir(parents=True)
        (mono_target / "apps" / "web" / "package.json").write_text('{"scripts":{"typecheck":"tsc --noEmit"}}\n', encoding="utf-8")
        mono_payload = build_payload(source.as_posix(), mono_target.as_posix())
        assert mono_payload["repo_topology"] == "workspace_or_monorepo"
        assert any(item["command"] == "apps/web: npm run typecheck" for item in mono_payload["likely_checks"])

        missing_source_payload = build_payload((base / "missing-source").as_posix(), node_target.as_posix())
        assert missing_source_payload["status"] == "blocked"
        assert "source path does not exist or is not a directory" in missing_source_payload["blockers"]

        missing_target_payload = build_payload(source.as_posix(), (base / "missing-target").as_posix())
        assert missing_target_payload["target_kind"] == "missing"
        assert missing_target_payload["status"] == "blocked"

        same_payload = build_payload(source.as_posix(), source.as_posix())
        assert same_payload["target_kind"] == "same_as_source"
        assert same_payload["status"] == "blocked"

        json.dumps(node_payload, sort_keys=True)
        write_evidence(node_payload)
        assert (source / "logs" / "existing-repo-intake.json").is_file()
        assert (source / "logs" / "existing-repo-intake.md").is_file()
        assert not (node_target / "logs").exists()

    print(json.dumps({"tool": "existing-repo-intake-self-test", "status": "pass"}, indent=2, sort_keys=True))
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Read-only PrecodeOS existing repo intake check.")
    parser.add_argument("--source", help="PrecodeOS package source checkout")
    parser.add_argument("--target", help="existing target project folder")
    parser.add_argument("--json", action="store_true", help="print machine-readable existing repo intake output")
    parser.add_argument("--write-evidence", action="store_true", help="write generated evidence under the source logs directory")
    parser.add_argument("--self-test", action="store_true", help="run fixture-style existing repo intake checks")
    args = parser.parse_args()

    if args.self_test:
        return self_test()

    if not args.source or not args.target:
        parser.error("--source and --target are required unless --self-test is used")

    payload = build_payload(args.source, args.target)
    if args.write_evidence:
        if payload["source_root"] == payload["target_root"]:
            raise SystemExit("existing-repo-intake: refusing to write evidence when source and target are the same")
        if "source path does not exist or is not a directory" in payload["blockers"]:
            raise SystemExit("existing-repo-intake: refusing to write evidence because source is missing")
        write_evidence(payload)
    if args.json:
        print(json.dumps(payload, indent=2, sort_keys=True))
    else:
        print(render_plain(payload))
        if args.write_evidence:
            print("existing-repo-intake: wrote logs/existing-repo-intake.json and logs/existing-repo-intake.md in the source workspace")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
