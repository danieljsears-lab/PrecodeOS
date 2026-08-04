#!/usr/bin/env python3
# Version: v0.1.0
# Last updated: 2026-08-04
# Owner: PrecodeOS
# Created by Dan Sears / Recode.
# SPDX-License-Identifier: Apache-2.0
from __future__ import annotations

import argparse
import fnmatch
import json
import subprocess
import tempfile
from pathlib import Path
from typing import Any

from os_parser import parse_sections, split_frontmatter


ROOT = Path(__file__).resolve().parents[1]
ADVISORY_WARNING = (
    "Product Code Quality Snapshot is advisory evidence only; it does not run lint or tests, "
    "inspect app code deeply, score code quality, certify decent code, approve implementation, "
    "accept review, approve release, or create generated proof."
)
DOES_NOT = [
    "run linters",
    "run tests",
    "run typechecks",
    "run package managers",
    "install dependencies",
    "mutate lint configuration",
    "auto-fix code",
    "parse application code deeply",
    "perform AST analysis",
    "make framework-specific correctness claims",
    "score code quality",
    "certify decent code",
    "certify production readiness, security, compliance, scalability, reliability, or accessibility",
    "approve implementation",
    "accept review",
    "approve release",
    "create generated proof",
    "create a checker gate",
    "choose tasks",
    "create follow-up tasks",
    "mutate GitHub or external systems",
    "create command-wrapper, registry, optional-pack, install/update, release-channel, or package-manager behavior",
]


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8") if path.is_file() else ""


def todo_current_bead(root: Path) -> str:
    text = read_text(root / "tasks" / "todo.md")
    frontmatter, _ = split_frontmatter(text)
    value = str(frontmatter.get("current_bead") or "").strip()
    if value:
        return value
    for line in text.splitlines():
        clean = line.strip()
        if clean.startswith("- `") and "`" in clean[3:]:
            return clean.split("`", 2)[1].strip()
    return ""


def list_value(frontmatter: dict[str, Any], key: str) -> list[str]:
    value = frontmatter.get(key)
    if isinstance(value, list):
        return [str(item).strip() for item in value if str(item).strip()]
    if isinstance(value, str) and value.strip():
        return [value.strip()]
    return []


def active_bead_details(root: Path) -> tuple[dict[str, Any], list[str]]:
    warnings: list[str] = []
    rel_path = todo_current_bead(root)
    details: dict[str, Any] = {
        "path": rel_path or "not recorded",
        "primary_authority": "missing",
        "declared_files_in_play": [],
        "declared_checks": [],
        "stop_if_present": False,
    }
    if not rel_path:
        warnings.append("active bead is not recorded in tasks/todo.md")
        return details, warnings
    if rel_path.startswith("_maintainer/"):
        warnings.append("active bead path points at maintainer-private material")
        return details, warnings
    path = root / rel_path
    if not path.is_file():
        warnings.append(f"active bead file is missing: {rel_path}")
        return details, warnings

    text = read_text(path)
    frontmatter, _ = split_frontmatter(text)
    sections = parse_sections(text)
    primary_authority = str(frontmatter.get("primary_authority") or "").strip()
    files_in_play = list_value(frontmatter, "files_in_play")
    checks = list_value(frontmatter, "checks")
    stop_if = sections.get("Stop If", "")
    details.update(
        {
            "primary_authority": primary_authority or "missing",
            "declared_files_in_play": files_in_play,
            "declared_checks": checks,
            "stop_if_present": bool(stop_if.strip()),
        }
    )
    if not primary_authority:
        warnings.append(f"{rel_path} is missing primary_authority")
    elif primary_authority.startswith("_maintainer/"):
        warnings.append(f"{rel_path} uses maintainer-private primary_authority")
    elif not (root / primary_authority).exists():
        warnings.append(f"{rel_path} primary_authority does not exist: {primary_authority}")
    if not files_in_play:
        warnings.append(f"{rel_path} does not declare files_in_play")
    if not checks:
        warnings.append(f"{rel_path} does not declare checks or proof path")
    if not stop_if.strip():
        warnings.append(f"{rel_path} does not declare Stop If conditions")
    return details, warnings


def git_changed_paths(root: Path) -> tuple[list[str], list[str]]:
    try:
        result = subprocess.run(
            ["git", "-C", str(root), "status", "--porcelain", "--untracked-files=all"],
            check=False,
            capture_output=True,
            text=True,
            timeout=5,
        )
    except (OSError, subprocess.TimeoutExpired) as exc:
        return [], [f"could not read git status: {exc}"]
    if result.returncode != 0:
        reason = result.stderr.strip() or result.stdout.strip() or f"exit {result.returncode}"
        return [], [f"could not read git status: {reason}"]

    paths: list[str] = []
    for line in result.stdout.splitlines():
        if not line.strip():
            continue
        path = line[3:].strip()
        if " -> " in path:
            path = path.rsplit(" -> ", 1)[1].strip()
        if path:
            paths.append(path)
    return sorted(dict.fromkeys(paths)), []


def path_category(path: str) -> str:
    name = Path(path).name
    suffix = Path(path).suffix.lower()
    if path.startswith(("docs/", "docs-html/")) or name in {"README.md", "llms.txt"}:
        return "docs"
    if path.startswith(("tasks/reference/", "tasks/prds/", "tasks/prds-html/")):
        return "protocol-or-prd"
    if path.startswith((".github/", "adapters/", "modes/")) or name in {
        ".gitignore",
        "pyproject.toml",
        "package.json",
        "package-lock.json",
        "pnpm-lock.yaml",
        "yarn.lock",
        "requirements.txt",
        "requirements-dev.txt",
        "tsconfig.json",
        "vite.config.js",
        "vite.config.ts",
        "next.config.js",
        "next.config.mjs",
    }:
        return "config-or-dependency"
    if path.startswith("scripts/"):
        return "script"
    if path.startswith("logs/"):
        return "generated-evidence"
    if path.startswith("tests/") or name.startswith("test_") or name.endswith("_test.py") or suffix in {".spec", ".test"}:
        return "test"
    if path.startswith("_maintainer/"):
        return "maintainer-private"
    return "source-or-other"


def path_is_declared(path: str, declared: set[str]) -> bool:
    for item in declared:
        clean = item.rstrip("/")
        if not clean:
            continue
        if path == clean or path.startswith(f"{clean}/"):
            return True
        if any(char in clean for char in "*?[]") and fnmatch.fnmatch(path, clean):
            return True
    return False


def changed_file_summary(changed_paths: list[str], active_bead: dict[str, Any]) -> dict[str, Any]:
    declared = set(str(item) for item in active_bead.get("declared_files_in_play", []) if str(item).strip())
    primary_authority = str(active_bead.get("primary_authority") or "").strip()
    if primary_authority and primary_authority != "missing":
        declared.add(primary_authority)
    undeclared = [
        path
        for path in changed_paths
        if not path_is_declared(path, declared)
        and not path.startswith(("docs-html/", "tasks/prds-html/", "logs/"))
    ]
    categories: dict[str, list[str]] = {}
    for path in changed_paths:
        categories.setdefault(path_category(path), []).append(path)
    return {
        "changed_files": changed_paths,
        "changed_files_count": len(changed_paths),
        "declared_scope": sorted(declared),
        "undeclared_changed_files": undeclared,
        "undeclared_changed_files_count": len(undeclared),
        "categories": {key: sorted(value) for key, value in sorted(categories.items())},
    }


def manifest_scripts(root: Path) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    package_json = root / "package.json"
    if package_json.is_file():
        try:
            data = json.loads(read_text(package_json))
        except json.JSONDecodeError:
            data = {}
        scripts = data.get("scripts") if isinstance(data, dict) else {}
        if isinstance(scripts, dict):
            for name in ("lint", "typecheck", "test", "check", "build"):
                command = scripts.get(name)
                if isinstance(command, str) and command.strip():
                    rows.append(
                        {
                            "source": "package.json",
                            "kind": name,
                            "command": f"npm run {name}",
                            "discovery_only": "true",
                            "execution_note": "Run only after separate user approval under Tool Execution Protocol.",
                        }
                    )
    pyproject = root / "pyproject.toml"
    if pyproject.is_file():
        text = read_text(pyproject)
        for tool, command in {
            "[tool.ruff": "python3 -m ruff check .",
            "[tool.pytest": "python3 -m pytest",
            "[tool.mypy": "python3 -m mypy .",
            "[tool.pyright": "python3 -m pyright",
        }.items():
            if tool in text:
                rows.append(
                    {
                        "source": "pyproject.toml",
                        "kind": command.split()[-2] if command.endswith(" .") else command.split()[-1],
                        "command": command,
                        "discovery_only": "true",
                        "execution_note": "Run only after separate user approval under Tool Execution Protocol.",
                    }
                )
    return rows


def config_command_hints(root: Path) -> list[dict[str, str]]:
    hints: list[dict[str, str]] = []
    config_map = {
        ".eslintrc": "npx eslint .",
        ".eslintrc.json": "npx eslint .",
        ".eslintrc.js": "npx eslint .",
        "eslint.config.js": "npx eslint .",
        "eslint.config.mjs": "npx eslint .",
        "tsconfig.json": "npx tsc --noEmit",
        "pytest.ini": "python3 -m pytest",
        "ruff.toml": "python3 -m ruff check .",
        "mypy.ini": "python3 -m mypy .",
    }
    for filename, command in config_map.items():
        if (root / filename).exists():
            hints.append(
                {
                    "source": filename,
                    "kind": "config-hint",
                    "command": command,
                    "discovery_only": "true",
                    "execution_note": "Run only after separate user approval under Tool Execution Protocol.",
                }
            )
    seen: set[tuple[str, str]] = set()
    unique: list[dict[str, str]] = []
    for row in manifest_scripts(root) + hints:
        key = (row["source"], row["command"])
        if key not in seen:
            unique.append(row)
            seen.add(key)
    return unique


def repo_shape_risks(summary: dict[str, Any], checks: list[str], mode: str) -> list[str]:
    risks: list[str] = []
    categories = summary.get("categories") or {}
    undeclared_count = int(summary.get("undeclared_changed_files_count") or 0)
    lower_checks = " ".join(checks).lower()
    if mode == "active-bead" and undeclared_count:
        risks.append("changed files exist outside the active bead's declared files in play or primary authority")
    broad_categories = [
        category
        for category, paths in categories.items()
        if category != "generated-evidence" and paths
    ]
    if len(broad_categories) >= 4:
        risks.append("changed files span four or more non-generated package/source categories")
    if categories.get("config-or-dependency") and not any(
        term in lower_checks for term in ("dependency", "version-check", "test", "lint", "typecheck", "npm", "pnpm")
    ):
        risks.append("configuration or dependency files changed without a declared matching check")
    if categories.get("script") and not any(
        term in lower_checks for term in ("self-test", "clarity-scenario", "version-check", "pytest", "test")
    ):
        risks.append("script files changed without a declared script or scenario check")
    if (categories.get("docs") or categories.get("protocol-or-prd")) and not any(
        term in lower_checks for term in ("docs-html", "prd-html", "clarity-scenario", "file-inventory")
    ):
        risks.append("docs, protocol, or PRD files changed without docs/reference validation")
    if not summary.get("changed_files"):
        risks.append("no changed files were visible from git status")
    return risks


def missing_proof(active_bead: dict[str, Any], risks: list[str], linter_rows: list[dict[str, str]]) -> list[str]:
    missing: list[str] = []
    checks = active_bead.get("declared_checks") or []
    if not checks:
        missing.append("active bead does not declare checks or proof path")
    if active_bead.get("stop_if_present") is False:
        missing.append("active bead does not declare Stop If conditions")
    if risks and not checks:
        missing.append("repo-shape risks are present but no active-bead checks are declared")
    if linter_rows:
        missing.append("likely project-owned lint/check commands were discovered but not run by this snapshot")
    return missing


def review_questions(mode: str, risks: list[str], linter_rows: list[dict[str, str]]) -> list[str]:
    questions = [
        "Do the changed files match the active bead, primary authority, and declared files in play?",
        "Do the declared checks prove the changed behavior without pretending to prove more?",
        "Is any configuration, dependency, generated output, or sensitive surface change intentional and reviewed?",
    ]
    if mode == "whole-codebase":
        questions[0] = "Are the visible changed files a coherent bounded review set, or should the work be split before acceptance?"
    if risks:
        questions.append("Which repo-shape risks need Closeout Evidence, an owner-file update, Release Readiness, or another Review Lane?")
    if linter_rows:
        questions.append("Should a human approve running one of the discovered project-owned lint/check commands under Tool Execution Protocol?")
    return questions


def recommended_next_action(risks: list[str], missing: list[str], mode: str) -> str:
    if not risks and not missing:
        return "use normal human review; the snapshot adds no quality certification"
    if any("outside the active bead" in risk for risk in risks):
        return "pause acceptance and reconcile changed files against the active bead before review"
    if mode == "whole-codebase":
        return "use the snapshot as triage evidence, then choose a bounded active bead or review lane if work should continue"
    return "use Product Code Quality Snapshot as evidence for Engineering Quality Review Lane before acceptance"


def build_payload(root: Path, mode: str) -> dict[str, Any]:
    active_bead, bead_warnings = active_bead_details(root)
    changed_paths, git_warnings = git_changed_paths(root)
    summary = changed_file_summary(changed_paths, active_bead)
    linter_rows = config_command_hints(root)
    risks = repo_shape_risks(summary, active_bead.get("declared_checks", []), mode)
    missing = missing_proof(active_bead, risks, linter_rows)
    warnings = bead_warnings + git_warnings + risks + missing
    return {
        "tool": "product-code-quality-snapshot",
        "snapshot_mode": mode,
        "status": "pass" if not warnings else "warning",
        "advisory_only": True,
        "active_bead": active_bead,
        "changed_file_summary": summary,
        "repo_shape_risk_signals": risks,
        "project_linter_evidence": {
            "discovery_only": True,
            "runs_commands": False,
            "normal_tool_approval_required_before_execution": True,
            "likely_commands": linter_rows,
        },
        "missing_proof": missing,
        "review_questions": review_questions(mode, risks, linter_rows),
        "recommended_next_action": recommended_next_action(risks, missing, mode),
        "warnings": warnings,
        "advisory_warning": ADVISORY_WARNING,
        "does_not": DOES_NOT,
    }


def render_plain(payload: dict[str, Any]) -> str:
    active = payload["active_bead"]
    changed = payload["changed_file_summary"]
    lines = [
        "Product Code Quality Snapshot",
        f"Mode: {payload['snapshot_mode']}",
        f"Status: {payload['status']}",
        "",
        "Active bead:",
        f"- Path: {active.get('path')}",
        f"- Primary authority: {active.get('primary_authority')}",
        f"- Declared files in play: {', '.join(active.get('declared_files_in_play') or []) or 'none'}",
        f"- Declared checks: {', '.join(active.get('declared_checks') or []) or 'none'}",
        "",
        "Changed files:",
        f"- Count: {changed.get('changed_files_count')}",
        f"- Undeclared count: {changed.get('undeclared_changed_files_count')}",
    ]
    for path in changed.get("undeclared_changed_files", []):
        lines.append(f"  - {path}")
    lines.extend(["", "Repo-shape risk signals:"])
    risks = payload.get("repo_shape_risk_signals") or []
    lines.extend(f"- {risk}" for risk in risks) if risks else lines.append("- none")
    lines.extend(["", "Project Linter Evidence:"])
    commands = payload["project_linter_evidence"]["likely_commands"]
    if commands:
        for row in commands:
            lines.append(f"- {row['command']} ({row['source']}; discovery only, requires separate approval)")
    else:
        lines.append("- no likely lint/check commands discovered")
    lines.extend(["", "Missing proof:"])
    missing = payload.get("missing_proof") or []
    lines.extend(f"- {item}" for item in missing) if missing else lines.append("- none")
    lines.extend(["", "Review questions:"])
    lines.extend(f"- {item}" for item in payload.get("review_questions") or [])
    lines.extend(["", f"Recommended next action: {payload['recommended_next_action']}", payload["advisory_warning"]])
    return "\n".join(lines) + "\n"


def self_test() -> dict[str, Any]:
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        (root / "tasks" / "beads").mkdir(parents=True)
        (root / "scripts").mkdir()
        (root / "tasks" / "todo.md").write_text(
            "---\ncurrent_bead: tasks/beads/B999-fixture.md\n---\n", encoding="utf-8"
        )
        (root / "tasks" / "beads" / "B999-fixture.md").write_text(
            """---
bead_id: B999
status: in_progress
primary_authority: PROJECT-CONTEXT.md
files_in_play:
  - PROJECT-CONTEXT.md
checks:
  - python3 scripts/version-check.py
---

# B999 -- Fixture

## Stop If

- Scope or proof becomes unclear.
""",
            encoding="utf-8",
        )
        (root / "PROJECT-CONTEXT.md").write_text("# Project Context\n", encoding="utf-8")
        (root / "package.json").write_text(
            json.dumps({"scripts": {"lint": "eslint .", "test": "vitest run"}}), encoding="utf-8"
        )
        subprocess.run(["git", "init"], cwd=root, check=True, capture_output=True, text=True)
        subprocess.run(["git", "config", "user.email", "fixture@example.com"], cwd=root, check=True)
        subprocess.run(["git", "config", "user.name", "Fixture"], cwd=root, check=True)
        subprocess.run(["git", "add", "."], cwd=root, check=True)
        subprocess.run(["git", "commit", "-m", "fixture"], cwd=root, check=True, capture_output=True, text=True)
        (root / "src").mkdir()
        (root / "src" / "app.js").write_text("console.log('changed')\n", encoding="utf-8")

        active_payload = build_payload(root, "active-bead")
        whole_payload = build_payload(root, "whole-codebase")
        failures: list[str] = []
        if active_payload["snapshot_mode"] != "active-bead":
            failures.append("active mode mismatch")
        if whole_payload["snapshot_mode"] != "whole-codebase":
            failures.append("whole-codebase mode mismatch")
        if not active_payload["changed_file_summary"]["undeclared_changed_files"]:
            failures.append("undeclared changed file was not reported")
        if not active_payload["project_linter_evidence"]["likely_commands"]:
            failures.append("likely lint/check command was not discovered")
        if active_payload["project_linter_evidence"]["runs_commands"]:
            failures.append("snapshot claims to run commands")
        forbidden = " ".join(active_payload["does_not"]).lower()
        for term in ("run linters", "score code quality", "certify decent code", "approve implementation"):
            if term not in forbidden:
                failures.append(f"missing forbidden boundary: {term}")
        return {
            "tool": "product-code-quality-snapshot",
            "status": "pass" if not failures else "fail",
            "failures": failures,
            "advisory_only": True,
        }


def main() -> int:
    parser = argparse.ArgumentParser(description="Build an advisory Product Code Quality Snapshot.")
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--active-bead", action="store_true", help="Gather active-bead-first changed-code evidence.")
    mode.add_argument("--whole-codebase", action="store_true", help="Gather explicit whole-codebase changed-file health evidence.")
    parser.add_argument("--json", action="store_true", help="Print JSON instead of plain text.")
    parser.add_argument("--self-test", action="store_true", help="Run deterministic fixture coverage.")
    args = parser.parse_args()

    if args.self_test:
        payload = self_test()
        print(json.dumps(payload, indent=2, sort_keys=True))
        return 0 if payload["status"] == "pass" else 1
    if not args.active_bead and not args.whole_codebase:
        parser.error("choose --active-bead, --whole-codebase, or --self-test")
    payload = build_payload(ROOT, "whole-codebase" if args.whole_codebase else "active-bead")
    if args.json:
        print(json.dumps(payload, indent=2, sort_keys=True))
    else:
        print(render_plain(payload), end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
