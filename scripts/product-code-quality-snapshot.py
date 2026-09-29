#!/usr/bin/env python3
# Version: v0.1.0
# Last updated: 2026-08-04
# Owner: PrecodeOS
# Created by Dan Sears / Recode.
# SPDX-License-Identifier: Apache-2.0
from __future__ import annotations

import argparse
from collections import Counter
import fnmatch
import json
import itertools
import subprocess
import tempfile
from datetime import datetime, timezone
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

BEHAVIORAL_SIGNAL_WARNING = (
    "Behavioral repo-shape signals are history-only advisory cues; they identify areas worth a human look, "
    "not bad code, unhealthy code, or approval decisions."
)
INDENTATION_WARNING = (
    "Tier-2 indentation complexity is structural advisory evidence; deep indentation is worth a human look, "
    "not evidence of bad code, unhealthy code, or an approval decision."
)
INDENTATION_REVIEW_DEPTH = 6
NOISE_PREFIXES = (".git/", "node_modules/", "vendor/", "dist/", "build/", "coverage/", "logs/")
NOISE_NAMES = {"package-lock.json", "pnpm-lock.yaml", "yarn.lock", "poetry.lock", "uv.lock"}


def confidence_readout(
    active_bead: dict[str, Any],
    summary: dict[str, Any],
    risks: list[str],
    missing: list[str],
    git_warnings: list[str],
) -> dict[str, Any]:
    """Translate snapshot evidence into advisory, human-readable next questions."""
    rows: list[dict[str, str]] = []
    changed_count = int(summary.get("changed_files_count") or 0)
    undeclared_count = int(summary.get("undeclared_changed_files_count") or 0)

    if git_warnings:
        rows.append(
            {
                "observed": "Git changed-file history was not fully available.",
                "interpretation": "The snapshot cannot honestly judge whether the visible change set stayed in bounds.",
                "uncertainty": "High: repository history or status evidence is incomplete.",
                "human_action": "Inspect the repository state manually before relying on this readout.",
            }
        )
    elif not changed_count:
        rows.append(
            {
                "observed": "No changed files were visible from git status.",
                "interpretation": "There is not enough change evidence for a meaningful code-change readout.",
                "uncertainty": "High: no visible change is not evidence that the code is healthy.",
                "human_action": "Confirm the intended change and repository state before review.",
            }
        )
    else:
        rows.append(
            {
                "observed": f"Git status shows {changed_count} changed file(s).",
                "interpretation": "The readout has a concrete changed-file set to compare with the active bead.",
                "uncertainty": "The snapshot does not inspect application-code correctness.",
                "human_action": "Compare the changed files with the bead, owner file, and declared proof.",
            }
        )

    if undeclared_count:
        rows.append(
            {
                "observed": f"{undeclared_count} changed file(s) fall outside the declared active-bead scope.",
                "interpretation": "The work may be broader than the current bead or its declaration may be stale.",
                "uncertainty": "The signal identifies scope mismatch, not a defect in the code.",
                "human_action": "Pause acceptance and reconcile the files with the bead before review.",
            }
        )
    elif changed_count:
        rows.append(
            {
                "observed": "No undeclared changed files were found in the visible change set.",
                "interpretation": "The visible file scope is consistent with the active-bead declaration.",
                "uncertainty": "Scope alignment does not prove behavior, maintainability, or release readiness.",
                "human_action": "Continue with declared checks and human review of the evidence.",
            }
        )

    if risks:
        rows.append(
            {
                "observed": "Repo-shape risk signals: " + "; ".join(risks) + ".",
                "interpretation": "The change shape deserves a closer human look at boundaries, proof, or review routing.",
                "uncertainty": "These are advisory shape cues and cannot determine code quality.",
                "human_action": "Ask which risk needs Closeout Evidence, an owner-file update, or another Review Lane.",
            }
        )

    if missing:
        rows.append(
            {
                "observed": "Evidence gaps: " + "; ".join(missing) + ".",
                "interpretation": "The available packet does not fully support the claims a human may want to review.",
                "uncertainty": "Unknowns remain; missing evidence must not be interpreted as a positive result.",
                "human_action": "Fill the narrowest proof gap or route the uncertainty to the appropriate human review.",
            }
        )

    if not rows:
        rows.append(
            {
                "observed": "The snapshot found no additional warning or evidence gap.",
                "interpretation": "No extra advisory cue was identified from the available Precode evidence.",
                "uncertainty": "This does not mean the code is healthy or certified.",
                "human_action": "Use normal human review and the declared proof path.",
            }
        )

    return {
        "purpose": "Translate observed Precode evidence into a plain-language human review conversation.",
        "advisory_only": True,
        "rows": rows,
        "does_not": [
            "compute numeric confidence",
            "score or certify code quality",
            "treat missing signals as evidence of health",
            "approve implementation, review, or release",
            "replace tests, linters, or human judgment",
        ],
    }


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8") if path.is_file() else ""


def excluded_behavior_path(path: str) -> bool:
    clean = path.lstrip("./")
    return clean.startswith(NOISE_PREFIXES) or Path(clean).name in NOISE_NAMES


def git_history(root: Path, since: str = "48 hours ago") -> tuple[list[tuple[str, str]], list[str]]:
    """Return (commit timestamp, path) rows without treating history as attribution."""
    try:
        result = subprocess.run(
            ["git", "-C", str(root), "log", "--since", since, "--format=%H%x09%cI", "--name-only", "--diff-filter=AMCR"],
            check=False, capture_output=True, text=True, timeout=5,
        )
    except (OSError, subprocess.TimeoutExpired) as exc:
        return [], [f"could not read git history: {exc}"]
    if result.returncode != 0:
        return [], [f"could not read git history: {result.stderr.strip() or result.stdout.strip() or result.returncode}"]
    rows: list[tuple[str, str]] = []
    timestamp = ""
    for line in result.stdout.splitlines():
        if "\t" in line and len(line.split("\t", 1)[0]) == 40:
            _, timestamp = line.split("\t", 1)
            continue
        path = line.strip()
        if path and timestamp and not excluded_behavior_path(path):
            rows.append((timestamp, path))
    return rows, []


def behavioral_repo_shape_signals(root: Path, changed_paths: list[str]) -> tuple[dict[str, Any], list[str]]:
    rows, warnings = git_history(root)
    usable = [(stamp, path) for stamp, path in rows if not excluded_behavior_path(path)]
    file_counts = Counter(path for _, path in usable)
    commit_paths: dict[str, set[str]] = {}
    # A commit hash is intentionally not exposed; this is a conservative co-occurrence readout.
    try:
        result = subprocess.run(
            ["git", "-C", str(root), "log", "--since", "48 hours ago", "--format=%H", "--name-only", "--diff-filter=AMCR"],
            check=False, capture_output=True, text=True, timeout=5,
        )
        current = ""
        for line in result.stdout.splitlines():
            if len(line.strip()) == 40 and " " not in line.strip():
                current = line.strip()
                commit_paths.setdefault(current, set())
            elif current and line.strip() and not excluded_behavior_path(line.strip()):
                commit_paths[current].add(line.strip())
    except (OSError, subprocess.TimeoutExpired) as exc:
        warnings.append(f"could not read commit co-occurrence history: {exc}")

    signals: list[dict[str, Any]] = []
    changed_set = {path for path in changed_paths if not excluded_behavior_path(path)}
    if len(usable) < 3:
        signals.append({"name": "history", "observed": "fewer than three usable recent file-change observations", "interpretation": "history is too sparse for an honest behavioral readout", "uncertainty": "insufficient history; absence of a signal is not evidence of health", "human_action": "use normal bounded review and gather more history before relying on this lens"})
    else:
        thrash = [path for path, count in file_counts.items() if count >= 3 and (not changed_set or path in changed_set)]
        if thrash:
            signals.append({"name": "agent-thrash", "observed": f"{', '.join(sorted(thrash)[:5])} appears in at least three recent change events", "interpretation": "the same area may be receiving repeated regeneration or repair", "uncertainty": "git history cannot establish agent attribution or a true session boundary", "human_action": "ask the agent to explain the repeated changes or re-scope the work"})
        coupling: list[str] = []
        for paths in commit_paths.values():
            for left, right in itertools.combinations(sorted(paths), 2):
                if sum(left in paths and right in paths for paths in commit_paths.values()) >= 2:
                    coupling.append(f"{left} + {right}")
        if coupling:
            signals.append({"name": "change-coupling", "observed": f"{', '.join(sorted(set(coupling))[:3])} co-occur repeatedly", "interpretation": "these files may be behaviorally coupled", "uncertainty": "bead-shaped or squashed commits can inflate co-occurrence", "human_action": "ask whether the files should remain together or be separated"})
        hotspots = []
        for path, count in file_counts.items():
            candidate = root / path
            if count >= 2 and candidate.is_file() and candidate.stat().st_size >= 500:
                hotspots.append(path)
        if hotspots:
            signals.append({"name": "hotspot", "observed": f"{', '.join(sorted(hotspots)[:5])} combines repeated change history with a larger file", "interpretation": "this area may deserve focused review because change is concentrated here", "uncertainty": "central or frequently used files are not defects; this is a localization hint only", "human_action": "ask whether the file has a bounded owner and whether the change can stay understandable"})
        if changed_set:
            broad = sorted(changed_set)
            if len(broad) >= 8 or len({Path(path).parts[0] for path in broad}) >= 4:
                signals.append({"name": "oversized-change", "observed": f"{len(broad)} non-noise files span {len({Path(path).parts[0] for path in broad})} top-level areas", "interpretation": "the change may be broader than one bounded concern", "uncertainty": "broad scope can be intentional and is not a defect finding", "human_action": "ask whether the work should be split before acceptance"})
    return {"advisory_only": True, "history_window": "48 hours", "signals": signals, "excluded_noise": sorted(set(path for _, path in rows if excluded_behavior_path(path))), "warning": BEHAVIORAL_SIGNAL_WARNING}, warnings


def indentation_complexity(root: Path, changed_paths: list[str]) -> dict[str, Any]:
    """Measure leading indentation shape without interpreting application language."""
    findings: list[dict[str, Any]] = []
    uncertainties: list[str] = []
    scanned = 0
    for relative in changed_paths:
        if excluded_behavior_path(relative):
            continue
        path = root / relative
        if not path.is_file() or path.stat().st_size > 2_000_000:
            continue
        try:
            raw = path.read_bytes()
            if b"\x00" in raw:
                uncertainties.append(f"could not inspect binary-like file: {relative}")
                continue
            text = raw.decode("utf-8")
        except (OSError, UnicodeDecodeError):
            uncertainties.append(f"could not inspect unreadable or non-UTF-8 file: {relative}")
            continue
        scanned += 1
        depths: list[int] = []
        deep_lines: list[int] = []
        saw_tab = saw_space = False
        for number, line in enumerate(text.splitlines(), 1):
            stripped = line.lstrip()
            if not stripped or stripped.startswith(("#", "//", "/*", "*", "<!--")):
                continue
            prefix = line[: len(line) - len(line.lstrip(" \t"))]
            saw_tab = saw_tab or "\t" in prefix
            saw_space = saw_space or " " in prefix
            depth = len(prefix)
            depths.append(depth)
            if depth >= INDENTATION_REVIEW_DEPTH:
                deep_lines.append(number)
        if saw_tab and saw_space:
            uncertainties.append(f"mixed tabs and spaces make indentation shape uncertain: {relative}")
        if depths and max(depths) >= INDENTATION_REVIEW_DEPTH:
            findings.append({
                "path": relative,
                "max_depth": max(depths),
                "deep_line_count": len(deep_lines),
                "sample_lines": deep_lines[:5],
            })
    return {
        "advisory_only": True,
        "tier": "Tier 2 structural read; no language semantics",
        "review_depth": INDENTATION_REVIEW_DEPTH,
        "scanned_file_count": scanned,
        "signals": findings[:10],
        "uncertainties": uncertainties[:10],
        "warning": INDENTATION_WARNING,
    }


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
    behavioral_signals, behavioral_warnings = behavioral_repo_shape_signals(root, changed_paths)
    warnings.extend(behavioral_warnings)
    indentation_signals = indentation_complexity(root, changed_paths)
    readout = confidence_readout(active_bead, summary, risks, missing, git_warnings)
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
        "confidence_readout": readout,
        "behavioral_repo_shape_signals": behavioral_signals,
        "indentation_complexity": indentation_signals,
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
    lines.extend(["", "Confidence readout (advisory):"])
    for row in payload["confidence_readout"]["rows"]:
        lines.extend(
            [
                f"- Observed: {row['observed']}",
                f"  Interpretation: {row['interpretation']}",
                f"  Uncertainty: {row['uncertainty']}",
                f"  Human action: {row['human_action']}",
            ]
        )
    lines.extend(["", "Behavioral repo-shape signals (advisory; human-look only):"])
    for signal in payload["behavioral_repo_shape_signals"]["signals"]:
        lines.extend([f"- {signal['name']}: {signal['observed']}", f"  Interpretation: {signal['interpretation']}", f"  Uncertainty: {signal['uncertainty']}", f"  Human action: {signal['human_action']}"])
    lines.append(f"- {payload['behavioral_repo_shape_signals']['warning']}")
    indentation = payload["indentation_complexity"]
    lines.extend(["", "Tier-2 indentation complexity (advisory; human-look only):"])
    lines.append(f"- Scanned files: {indentation['scanned_file_count']}; review depth: {indentation['review_depth']}")
    for signal in indentation["signals"]:
        lines.append(f"- {signal['path']}: max depth {signal['max_depth']}; {signal['deep_line_count']} line(s) at or beyond review depth; sample lines {signal['sample_lines']}")
    for uncertainty in indentation["uncertainties"]:
        lines.append(f"- Uncertainty: {uncertainty}")
    lines.append(f"- {indentation['warning']}")
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
        behavioral = active_payload["behavioral_repo_shape_signals"]
        if not behavioral["advisory_only"] or "health" not in behavioral["warning"]:
            failures.append("behavioral signals are missing advisory boundary")
        if any("score" in str(signal).lower() or "certif" in str(signal).lower() for signal in behavioral["signals"]):
            failures.append("behavioral signals contain score/certification language")
        readout = active_payload["confidence_readout"]
        if not readout["advisory_only"] or not readout["rows"]:
            failures.append("confidence readout is missing advisory rows")
        row_text = " ".join(" ".join([*row.keys(), *row.values()]) for row in readout["rows"]).lower().replace("_", " ")
        for term in ("observed", "interpretation", "uncertainty", "human action"):
            if term not in row_text:
                failures.append(f"confidence readout missing field: {term}")
        if "healthy" in row_text and "not" not in row_text:
            failures.append("confidence readout implies absence of signal is healthy")
        if any(term in row_text for term in ("score", "certif")):
            failures.append("confidence readout contains score or certification language")
        shallow = active_payload["indentation_complexity"]
        if shallow["signals"]:
            failures.append("shallow fixture unexpectedly reports indentation complexity")
        (root / "src" / "deep.js").write_text("a\n  b\n    c\n      d\n        e\n          f\n", encoding="utf-8")
        deep = indentation_complexity(root, ["src/deep.js"])
        if not deep["signals"] or deep["signals"][0]["max_depth"] != 10:
            failures.append("depth-6 indentation signal missing or incorrect")
        if not deep["advisory_only"] or "human look" not in deep["warning"]:
            failures.append("indentation signal is missing advisory boundary")
        (root / "src" / "mixed.js").write_text("\tvalue\n  other\n", encoding="utf-8")
        mixed = indentation_complexity(root, ["src/mixed.js"])
        if not mixed["uncertainties"]:
            failures.append("mixed indentation uncertainty missing")
        (root / "node_modules").mkdir()
        (root / "node_modules" / "deep.js").write_text("          ignored\n", encoding="utf-8")
        excluded = indentation_complexity(root, ["node_modules/deep.js"])
        if excluded["signals"] or excluded["scanned_file_count"]:
            failures.append("excluded noise file was inspected")
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
