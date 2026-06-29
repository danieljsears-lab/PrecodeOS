#!/usr/bin/env python3
# Version: v0.1.0
# Last updated: 2026-06-29
# Owner: PrecodeOS
# Created by Dan Sears / Recode.
# SPDX-License-Identifier: Apache-2.0
from __future__ import annotations

import argparse
import json
import re
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
    "activate beads, accept review, score code quality, certify production readiness, or create proof."
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
    "create registry, optional-pack, install/update, release-channel, or package-manager behavior",
]
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
        "advisory only",
        "quality-risk, simplest-shape, boundary, proof, stop-condition, and routing signals",
        "does not inspect app code",
        "does not approve implementation",
        "does not create a scorecard",
        "Standards Taxonomy remains deferred",
    ],
    "tasks/reference/PROMPT-PATTERNS.md": [
        "Engineering Quality Text-Contract Checker",
        "python3 scripts/engineering-quality-check.py --check",
        "advisory only",
        "does not approve implementation",
        "does not create proof",
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
        "advisory only",
        "does not inspect app code",
        "does not approve implementation",
    ],
    "docs/PRECODE-PACKAGE-FILE-INVENTORY.md": [
        "scripts/engineering-quality-check.py",
        "Engineering Quality Text-Contract Checker",
        "quality-risk, simplest-shape, boundary, proof, stop-condition, and routing signals",
        "no app-code parsing",
        "no scorecard",
    ],
    "llms.txt": [
        "scripts/engineering-quality-check.py",
        "Engineering Quality Text-Contract Checker",
        "advisory only",
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
            "files_in_play_count": len(files_in_play),
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
    if risk_routes and not any(route.lower() in lower for route in set(risk_routes.values())):
        warnings.append("quality-floor answer names high-risk terms without routing to an owner protocol")
    return warnings


def recommended_next_safe_action(warnings: list[str]) -> str:
    if not warnings:
        return "continue inside the active bead; normal approval and proof gates still apply"
    if any("high-risk terms" in warning or "primary_authority" in warning for warning in warnings):
        return "stop and route through the relevant owner protocol before coding"
    return "revise the quality-floor text contract before treating it as implementation orientation"


def build_payload(root: Path, quality_text: str = "") -> dict[str, Any]:
    warnings = missing_contract_terms(root)
    bead_warnings, active_bead = active_bead_summary(root)
    warnings.extend(bead_warnings)
    quality_floor_warnings: list[str] = []
    if quality_text:
        quality_floor_warnings = analyze_quality_floor_text(quality_text)
        warnings.extend(quality_floor_warnings)
    return {
        "tool": "engineering-quality-check",
        "status": "pass" if not warnings else "warning",
        "warnings": warnings,
        "advisory_only": True,
        "details": {
            "checked_paths": sorted(REQUIRED_TERMS_BY_PATH) + ([active_bead["path"]] if active_bead.get("path") else []),
            "contract": CONTRACT,
            "active_bead": active_bead,
            "quality_floor_warnings": quality_floor_warnings,
            "does_not": DOES_NOT,
        },
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
    }
    failures: list[dict[str, str]] = []
    for name, fixture in fixtures.items():
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_fixture(root, str(fixture["text"]))
            payload = build_payload(root, quality_text=str(fixture["text"]))
            if payload["status"] != fixture["status"]:
                failures.append({"scenario": name, "expected": str(fixture["status"]), "actual": str(payload["status"])})
            warning = str(fixture.get("warning") or "")
            if warning and not any(warning in item for item in payload["warnings"]):
                failures.append({"scenario": name, "expected": warning, "actual": "; ".join(payload["warnings"])})
            if payload["advisory_only"] is not True:
                failures.append({"scenario": name, "expected": "advisory_only true", "actual": str(payload["advisory_only"])})
            if "approve implementation" not in payload["details"]["does_not"]:
                failures.append({"scenario": name, "expected": "forbidden authority list", "actual": str(payload["details"]["does_not"])})
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
    parser.add_argument("--self-test", action="store_true", help="run deterministic fixture coverage")
    args = parser.parse_args()

    if args.self_test:
        payload = self_test()
        print(json.dumps(payload, indent=2, sort_keys=True))
        return 0 if payload["status"] == "pass" else 1
    if not args.check:
        parser.error("choose --check or --self-test")
    payload = build_payload(ROOT, quality_text=args.quality_text or "")
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
