#!/usr/bin/env python3
# Version: v0.1.1
# Last updated: 2026-07-04
# Owner: PrecodeOS
# Created by Dan Sears / Recode.
# SPDX-License-Identifier: Apache-2.0
from __future__ import annotations

import argparse
import fnmatch
import json
import re
import subprocess
import tempfile
from pathlib import Path
from typing import Any

from os_parser import parse_sections, split_frontmatter


ROOT = Path(__file__).resolve().parents[1]
CONTRACT = (
    "Engineering Quality Text-Contract Checker inspects Precode artifact text for quality-risk, "
    "simplest-shape, boundary, proof, stop-condition, and routing signals only."
)
GENERATED_WARNING = (
    "engineering-quality-check output is advisory only; it does not approve implementation, "
    "activate beads, accept review, score code quality, certify production readiness, inspect app code, "
    "or create proof."
)
DOES_NOT = [
    "read maintainer-private files as public package authority",
    "inspect app code deeply",
    "run linters",
    "run tests",
    "approve implementation",
    "activate beads",
    "accept review",
    "score code quality",
    "certify production readiness, security, compliance, scalability, reliability, or accessibility",
    "create generated proof",
    "create a checker gate",
    "inspect Engineering Quality Review Lane output",
    "create repo heuristics or language-aware analysis",
    "create registry, optional-pack, install/update, release-channel, or package-manager behavior",
]
REPO_HEURISTICS_CONTRACT = (
    "Engineering Quality Repo Heuristics Preview inspects declared files in play and read-only git "
    "changed-file summaries for repo-shape risk only."
)
OWNER_PROTOCOL_ROUTES = {
    "architecture": "tasks/reference/ARCHITECTURE-SHAPING-PROTOCOL.md",
    "auth": "tasks/reference/ARCHITECTURE-SHAPING-PROTOCOL.md",
    "data": "tasks/reference/ARCHITECTURE-SHAPING-PROTOCOL.md",
    "api": "tasks/reference/ARCHITECTURE-SHAPING-PROTOCOL.md",
    "integration": "tasks/reference/ARCHITECTURE-SHAPING-PROTOCOL.md",
    "dependency": "tasks/reference/ARCHITECTURE-SHAPING-PROTOCOL.md",
    "migration": "tasks/reference/ARCHITECTURE-SHAPING-PROTOCOL.md",
    "workflow": "tasks/reference/ARCHITECTURE-SHAPING-PROTOCOL.md",
    "multi-system": "tasks/reference/ARCHITECTURE-SHAPING-PROTOCOL.md",
    "system design": "tasks/reference/SYSTEM-DESIGN-PATTERN-PROTOCOL.md",
    "business rule": "tasks/reference/SYSTEM-DESIGN-PATTERN-PROTOCOL.md",
    "provider": "tasks/reference/SYSTEM-DESIGN-PATTERN-PROTOCOL.md",
    "state flow": "tasks/reference/SYSTEM-DESIGN-PATTERN-PROTOCOL.md",
    "proof": "tasks/reference/VERIFICATION-GUARDRAIL-PROTOCOL.md",
    "test strategy": "tasks/reference/VERIFICATION-GUARDRAIL-PROTOCOL.md",
    "rollback": "tasks/reference/VERIFICATION-GUARDRAIL-PROTOCOL.md",
    "command": "tasks/reference/TOOL-EXECUTION-PROTOCOL.md",
    "destructive": "tasks/reference/TOOL-EXECUTION-PROTOCOL.md",
    "secret": "tasks/reference/TOOL-EXECUTION-PROTOCOL.md",
    "external mutation": "tasks/reference/TOOL-EXECUTION-PROTOCOL.md",
    "review": "tasks/reference/REVIEW-LANES-PROTOCOL.md",
    "release": "tasks/reference/RELEASE-READINESS-PROTOCOL.md",
    "deployment": "tasks/reference/RELEASE-READINESS-PROTOCOL.md",
    "shipping": "tasks/reference/RELEASE-READINESS-PROTOCOL.md",
}
REQUIRED_TERMS_BY_PATH = {
    "tasks/reference/ENGINEERING-QUALITY-STANDARDS-PROTOCOL.md": [
        "Engineering Quality Text-Contract Checker",
        "python3 scripts/engineering-quality-check.py --check",
        "python3 scripts/engineering-quality-check.py --check --repo-heuristics-preview",
        "advisory only",
        "quality-risk, simplest-shape, boundary, proof, stop-condition, and routing signals",
        "repo-shape risk only",
        "does not inspect app code",
        "does not approve implementation",
        "does not create a scorecard",
        "Engineering Quality Review Lane",
        "tasks/prds/PRD-038-engineering-quality-review-lane.md",
        "does not accept implementation",
        "does not inspect app code",
        "does not add repo heuristics",
        "does not add language-aware analysis",
        "Standards Taxonomy remains deferred",
    ],
    "tasks/reference/PROMPT-PATTERNS.md": [
        "Engineering Quality Text-Contract Checker",
        "python3 scripts/engineering-quality-check.py --check",
        "python3 scripts/engineering-quality-check.py --check --repo-heuristics-preview",
        "advisory only",
        "does not approve implementation",
        "does not create proof",
        "Engineering Quality Review Lane",
        "Run exactly one lane: Engineering Quality Review Lane",
        "Do not accept implementation",
        "create checker authority",
    ],
    "docs/PRECODE-DAILY-COCKPIT.md": [
        "Check quality text contract",
        "python3 scripts/engineering-quality-check.py --check",
        "advisory only",
        "does not approve coding, review, release, or generated proof",
    ],
    "docs/PRECODE-USER-GUIDE.md": [
        "Check The Engineering Quality Text Contract",
        "python3 scripts/engineering-quality-check.py --check",
        "python3 scripts/engineering-quality-check.py --check --repo-heuristics-preview",
        "advisory only",
        "does not inspect app code",
        "does not approve implementation",
        "Engineering Quality Review Lane",
        "does not certify code quality",
        "does not certify production readiness",
    ],
    "docs/PRECODE-PACKAGE-FILE-INVENTORY.md": [
        "scripts/engineering-quality-check.py",
        "Engineering Quality Text-Contract Checker",
        "--repo-heuristics-preview",
        "Engineering Quality Review Lane",
        "PRD-038",
        "quality-risk, simplest-shape, boundary, proof, stop-condition, and routing signals",
        "no app-code parsing",
        "no scorecard",
    ],
    "llms.txt": [
        "scripts/engineering-quality-check.py",
        "Engineering Quality Text-Contract Checker",
        "--repo-heuristics-preview",
        "Engineering Quality Review Lane",
        "advisory only",
    ],
    "tasks/prds/PRD-038-engineering-quality-review-lane.md": [
        "Engineering Quality Review Lane",
        "completed or nearly completed active bead",
        "scope discipline",
        "simplest acceptable implementation shape",
        "owner-file and boundary integrity",
        "proof quality",
        "configuration or dependency handling",
        "sensitive-surface routing",
        "stop-condition observance",
        "does not broaden the quality floor into repo heuristics",
        "language-aware analysis",
        "No app-code parser",
        "No implementation acceptance",
    ],
}


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8") if path.is_file() else ""


def todo_current_bead(root: Path) -> str:
    text = read_text(root / "tasks" / "todo.md")
    frontmatter, _ = split_frontmatter(text)
    value = str(frontmatter.get("current_bead") or "").strip()
    if value:
        return value
    match = re.search(r"^- `([^`]+)`", text, re.MULTILINE)
    return match.group(1).strip() if match else ""


def list_value(frontmatter: dict[str, Any], key: str) -> list[str]:
    value = frontmatter.get(key)
    if isinstance(value, list):
        return [str(item).strip() for item in value if str(item).strip()]
    if isinstance(value, str) and value.strip():
        return [value.strip()]
    return []


def active_bead_summary(root: Path) -> tuple[list[str], dict[str, Any]]:
    warnings: list[str] = []
    rel_path = todo_current_bead(root)
    details: dict[str, Any] = {"path": rel_path or "not recorded"}
    if not rel_path:
        warnings.append("active bead is not recorded in tasks/todo.md")
        return warnings, details
    if rel_path.startswith("_maintainer/"):
        warnings.append("active bead path points at maintainer-private material")
        return warnings, details
    path = root / rel_path
    if not path.is_file():
        warnings.append(f"active bead file is missing: {rel_path}")
        return warnings, details

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
            "files_in_play": files_in_play,
            "files_in_play_count": len(files_in_play),
            "checks": checks,
            "checks_count": len(checks),
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
    return warnings, details


def git_changed_paths(root: Path) -> tuple[list[str], list[str]]:
    warnings: list[str] = []
    try:
        result = subprocess.run(
            ["git", "-C", str(root), "status", "--porcelain", "--untracked-files=all"],
            check=False,
            capture_output=True,
            text=True,
            timeout=5,
        )
    except (OSError, subprocess.TimeoutExpired) as exc:
        return [], [f"repo heuristics preview could not read git status: {exc}"]
    if result.returncode != 0:
        reason = result.stderr.strip() or result.stdout.strip() or f"exit {result.returncode}"
        return [], [f"repo heuristics preview could not read git status: {reason}"]

    paths: list[str] = []
    for line in result.stdout.splitlines():
        if not line.strip():
            continue
        path = line[3:].strip()
        if " -> " in path:
            path = path.rsplit(" -> ", 1)[1].strip()
        if path:
            paths.append(path)
    return sorted(dict.fromkeys(paths)), warnings


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


def check_mentions(checks: list[str], terms: list[str]) -> bool:
    lower_checks = " ".join(checks).lower()
    return any(term in lower_checks for term in terms)


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


def repo_heuristics_preview(root: Path, active_bead: dict[str, Any]) -> dict[str, Any]:
    changed_paths, git_warnings = git_changed_paths(root)
    files_in_play = [str(item) for item in active_bead.get("files_in_play", []) if str(item).strip()]
    primary_authority = str(active_bead.get("primary_authority") or "").strip()
    declared = set(files_in_play)
    if primary_authority and primary_authority != "missing":
        declared.add(primary_authority)
    checks = [str(item) for item in active_bead.get("checks", []) if str(item).strip()]
    warnings: list[str] = list(git_warnings)

    changed_not_declared = [
        path
        for path in changed_paths
        if not path_is_declared(path, declared)
        and not path.startswith(("docs-html/", "tasks/prds-html/", "logs/"))
    ]
    if changed_not_declared:
        warnings.append(
            "repo heuristics preview found changed files not declared in files_in_play or primary_authority"
        )

    categories: dict[str, list[str]] = {}
    for path in changed_paths:
        categories.setdefault(path_category(path), []).append(path)

    if len([category for category, paths in categories.items() if category != "generated-evidence" and paths]) >= 4:
        warnings.append("repo heuristics preview found broad cross-surface changes")
    if categories.get("config-or-dependency") and not check_mentions(
        checks, ["version-check", "file-inventory", "dependency", "test", "pytest", "npm", "pnpm"]
    ):
        warnings.append("repo heuristics preview found config or dependency changes without a matching check")
    if categories.get("script") and not check_mentions(checks, ["self-test", "clarity-scenario", "version-check", "pytest"]):
        warnings.append("repo heuristics preview found script changes without a script or scenario check")
    if (categories.get("docs") or categories.get("protocol-or-prd")) and not check_mentions(
        checks, ["docs-html", "prd-html", "clarity-scenario", "file-inventory"]
    ):
        warnings.append("repo heuristics preview found docs, protocol, or PRD changes without docs/reference validation")
    if categories.get("generated-evidence") and not checks:
        warnings.append("repo heuristics preview found generated evidence changes but no recorded check")

    return {
        "enabled": True,
        "advisory_only": True,
        "contract": REPO_HEURISTICS_CONTRACT,
        "changed_paths": changed_paths,
        "changed_paths_count": len(changed_paths),
        "declared_files_in_play": sorted(declared),
        "changed_not_declared": changed_not_declared,
        "changed_not_declared_count": len(changed_not_declared),
        "categories": {key: sorted(value) for key, value in sorted(categories.items())},
        "warnings": warnings,
        "does_not": [
            "parse application code deeply",
            "run linters",
            "run tests",
            "score code quality",
            "approve implementation",
            "accept review",
            "certify production readiness",
            "create generated proof",
            "create a checker gate",
        ],
    }


def missing_contract_terms(root: Path) -> list[str]:
    warnings: list[str] = []
    for rel_path, terms in REQUIRED_TERMS_BY_PATH.items():
        path = root / rel_path
        text = read_text(path)
        if not text:
            warnings.append(f"{rel_path} is missing")
            continue
        for term in terms:
            if term not in text:
                warnings.append(f"{rel_path} is missing engineering-quality contract term: {term}")
    return warnings


def analyze_quality_floor_text(text: str) -> list[str]:
    lower = text.lower()
    warnings: list[str] = []
    if "engineering quality floor" not in lower and "quality risk" not in lower:
        warnings.append("quality-floor answer is missing the Engineering quality floor / Quality risk signal")
    for label, terms in {
        "quality risk": ["quality risk"],
        "simplest acceptable shape": ["simplest acceptable shape", "simplest shape"],
        "boundary or owner file": ["boundary", "owner file", "primary authority"],
        "evidence to prove it": ["evidence", "proof", "prove"],
        "stop or approval trigger": ["stop", "approval"],
        "routing": ["routing", "route to", "use architecture", "use system design", "use verification", "use tool execution", "use review lanes", "use release readiness"],
    }.items():
        if not any(term in lower for term in terms):
            warnings.append(f"quality-floor answer is missing {label}")

    for forbidden in ["certified", "certifies", "certification", "production-ready", "production ready"]:
        if forbidden in lower:
            warnings.append("quality-floor answer uses forbidden certification or production-readiness wording")
            break
    for forbidden in ["scorecard", "score:", "quality score", "code-quality rating", "checker gate"]:
        if forbidden in lower:
            warnings.append("quality-floor answer suggests forbidden scorecard or checker-gate behavior")
            break

    risk_routes = {
        term: route
        for term, route in OWNER_PROTOCOL_ROUTES.items()
        if term in lower
    }
    route_labels = [
        "architecture shaping",
        "system design pattern",
        "verification guardrail",
        "tool execution",
        "review lanes",
        "release readiness",
    ]
    if risk_routes and not any(route.lower() in lower for route in set(risk_routes.values())) and not any(label in lower for label in route_labels):
        warnings.append("quality-floor answer names high-risk terms without routing to an owner protocol")
    return warnings


def recommended_next_safe_action(warnings: list[str]) -> str:
    if not warnings:
        return "continue inside the active bead; normal approval and proof gates still apply"
    if any(
        "high-risk terms" in warning
        or "missing primary_authority" in warning
        or "uses maintainer-private primary_authority" in warning
        or "primary_authority does not exist" in warning
        for warning in warnings
    ):
        return "stop and route through the relevant owner protocol before coding"
    return "revise the quality-floor text contract before treating it as implementation orientation"


def build_payload(root: Path, quality_text: str = "", repo_heuristics: bool = False) -> dict[str, Any]:
    warnings = missing_contract_terms(root)
    bead_warnings, active_bead = active_bead_summary(root)
    warnings.extend(bead_warnings)
    quality_floor_warnings: list[str] = []
    if quality_text:
        quality_floor_warnings = analyze_quality_floor_text(quality_text)
        warnings.extend(quality_floor_warnings)
    repo_preview: dict[str, Any] | None = None
    if repo_heuristics:
        repo_preview = repo_heuristics_preview(root, active_bead)
        warnings.extend(str(item) for item in repo_preview.get("warnings", []))
        warnings.append("repo heuristics preview is enabled; treat changed-file findings as advisory only")
    details: dict[str, Any] = {
        "checked_paths": sorted(REQUIRED_TERMS_BY_PATH) + ([active_bead["path"]] if active_bead.get("path") else []),
        "contract": CONTRACT,
        "active_bead": active_bead,
        "quality_floor_warnings": quality_floor_warnings,
        "does_not": DOES_NOT,
    }
    if repo_preview is not None:
        details["repo_heuristics_preview"] = repo_preview
    return {
        "tool": "engineering-quality-check",
        "status": "pass" if not warnings else "warning",
        "warnings": warnings,
        "advisory_only": True,
        "details": details,
        "recommended_next_safe_action": recommended_next_safe_action(warnings),
        "generated_report_warning": GENERATED_WARNING,
    }


def write_fixture(root: Path, quality_text: str) -> None:
    (root / "tasks" / "reference").mkdir(parents=True)
    (root / "tasks" / "beads").mkdir(parents=True)
    (root / "docs").mkdir(parents=True)
    (root / "scripts").mkdir(parents=True)
    (root / "tasks" / "todo.md").write_text(
        """---
current_bead: tasks/beads/B999-fixture.md
---
""",
        encoding="utf-8",
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
    (root / "PROJECT-CONTEXT.md").write_text("# Fixture\n", encoding="utf-8")
    for rel_path, terms in REQUIRED_TERMS_BY_PATH.items():
        path = root / rel_path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("\n".join(terms) + "\n" + quality_text + "\n", encoding="utf-8")


def self_test() -> dict[str, Any]:
    fixtures = {
        "complete": {
            "status": "pass",
            "text": """Engineering quality floor:
- Quality risk: low
- Standard I am applying: keep the change inside the active bead.
- Simplest acceptable shape: one docs update.
- Boundary or owner file: PROJECT-CONTEXT.md
- Evidence to prove it: python3 scripts/version-check.py
- Stop or approval trigger: stop if scope expands.
- Routing: continue
""",
        },
        "missing proof": {
            "status": "warning",
            "text": """Engineering quality floor:
- Quality risk: low
- Simplest acceptable shape: one docs update.
- Boundary or owner file: PROJECT-CONTEXT.md
- Stop or approval trigger: stop if scope expands.
- Routing: continue
""",
            "warning": "evidence to prove it",
        },
        "missing stop": {
            "status": "warning",
            "text": """Engineering quality floor:
- Quality risk: medium
- Simplest acceptable shape: one local logic change.
- Boundary or owner file: PROJECT-CONTEXT.md
- Evidence to prove it: python3 scripts/version-check.py
- Routing: continue
""",
            "warning": "stop or approval trigger",
        },
        "high risk without route": {
            "status": "warning",
            "text": """Engineering quality floor:
- Quality risk: high because auth and data change.
- Simplest acceptable shape: one API update.
- Boundary or owner file: API.md
- Evidence to prove it: tests and review.
- Stop or approval trigger: stop before coding.
- Routing: continue
""",
            "warning": "high-risk terms",
        },
        "forbidden certification": {
            "status": "warning",
            "text": """Engineering quality floor:
- Quality risk: low
- Simplest acceptable shape: one docs update.
- Boundary or owner file: PROJECT-CONTEXT.md
- Evidence to prove it: check output.
- Stop or approval trigger: stop if scope expands.
- Routing: continue
- This certifies production-ready code quality.
""",
            "warning": "forbidden certification",
        },
        "scorecard gate": {
            "status": "warning",
            "text": """Engineering quality floor:
- Quality risk: low
- Simplest acceptable shape: one docs update.
- Boundary or owner file: PROJECT-CONTEXT.md
- Evidence to prove it: check output.
- Stop or approval trigger: stop if scope expands.
- Routing: continue
- Quality score: 98
""",
            "warning": "scorecard",
        },
        "review lane reference": {
            "status": "pass",
            "text": """Engineering quality floor:
- Quality risk: medium
- Standard I am applying: review completed work against the Engineering Quality Review Lane after proof is recorded.
- Simplest acceptable shape: one advisory review using the Review Lanes Protocol.
- Boundary or owner file: tasks/prds/PRD-038-engineering-quality-review-lane.md
- Evidence to prove it: recorded checks, manual verification, and closeout evidence.
- Stop or approval trigger: stop if the review would accept implementation, certify code quality, or create follow-up tasks.
- Routing: use Review Lanes
""",
        },
        "repo heuristics preview git unavailable": {
            "status": "warning",
            "repo_heuristics": True,
            "text": """Engineering quality floor:
- Quality risk: low
- Standard I am applying: keep the change inside the active bead.
- Simplest acceptable shape: one docs update.
- Boundary or owner file: PROJECT-CONTEXT.md
- Evidence to prove it: python3 scripts/version-check.py
- Stop or approval trigger: stop if scope expands.
- Routing: continue
""",
            "warning": "repo heuristics preview could not read git status",
        },
    }
    failures: list[dict[str, str]] = []
    for name, fixture in fixtures.items():
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_fixture(root, str(fixture["text"]))
            payload = build_payload(
                root,
                quality_text=str(fixture["text"]),
                repo_heuristics=bool(fixture.get("repo_heuristics")),
            )
            if payload["status"] != fixture["status"]:
                failures.append({"scenario": name, "expected": str(fixture["status"]), "actual": str(payload["status"])})
            warning = str(fixture.get("warning") or "")
            if warning and not any(warning in item for item in payload["warnings"]):
                failures.append({"scenario": name, "expected": warning, "actual": "; ".join(payload["warnings"])})
            if payload["advisory_only"] is not True:
                failures.append({"scenario": name, "expected": "advisory_only true", "actual": str(payload["advisory_only"])})
            if "approve implementation" not in payload["details"]["does_not"]:
                failures.append({"scenario": name, "expected": "forbidden authority list", "actual": str(payload["details"]["does_not"])})
            if fixture.get("repo_heuristics") and "repo_heuristics_preview" not in payload["details"]:
                failures.append({"scenario": name, "expected": "repo heuristics preview details", "actual": "missing"})
    return {
        "tool": "engineering-quality-check",
        "mode": "self-test",
        "status": "pass" if not failures else "fail",
        "scenario_count": len(fixtures),
        "failures": failures,
        "advisory_only": True,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="check engineering quality text contracts without writing files")
    parser.add_argument("--quality-text", help="optional quality-floor answer text to inspect")
    parser.add_argument("--repo-heuristics-preview", action="store_true", help="include advisory changed-file repo-shape heuristics")
    parser.add_argument("--self-test", action="store_true", help="run deterministic fixture coverage")
    args = parser.parse_args()

    if args.self_test:
        payload = self_test()
        print(json.dumps(payload, indent=2, sort_keys=True))
        return 0 if payload["status"] == "pass" else 1
    if not args.check:
        parser.error("choose --check or --self-test")
    payload = build_payload(ROOT, quality_text=args.quality_text or "", repo_heuristics=args.repo_heuristics_preview)
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
