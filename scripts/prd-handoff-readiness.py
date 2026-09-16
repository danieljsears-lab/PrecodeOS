#!/usr/bin/env python3
# Version: v0.2.0
# Last updated: 2026-09-06
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

from os_parser import colon_bullets, extract_contract_values, parse_sections, split_frontmatter

ROOT = Path(__file__).resolve().parents[1]
VALID_TARGETS = {"general", "decomposition", "design", "engineering", "review"}
GENERATED_WARNING = (
    "PRD handoff readiness packets are generated evidence only; they do not approve PRDs, "
    "choose tasks, activate beads, accept implementation, certify production readiness, mutate external tools, "
    "or replace Markdown PRD and owner-file authority."
)

INACTIVE_VALUES = {"", "none", "no", "not applicable", "not needed", "n/a", "na", "skipped", "tbd", "unknown"}

OWNER_LABELS = {
    "architecture": "ARCHITECTURE.md",
    "api": "API.md",
    "data": "DATA-MODELS.md",
    "security": "SECURITY.md",
    "codebase": "CODEBASE-GUIDE.md",
    "verification": "ACCEPTANCE.md",
}


def meaningful(value: Any) -> bool:
    normalized = str(value or "").strip().strip("`").strip().lower()
    if normalized in INACTIVE_VALUES:
        return False
    return re.match(r"^(?:none|no|not applicable|not needed|n/a|na|skipped|tbd|unknown)(?:\b|[.;:])", normalized) is None


def non_placeholder_rows(section: str) -> list[list[str]]:
    _, rows = first_table(section)
    return [row for row in rows if any(meaningful(cell) for cell in row)]


def production_readiness_activation(frontmatter: dict[str, Any], sections: dict[str, str]) -> dict[str, Any]:
    """Map explicit PRD risk and impact fields to existing owner files without certifying readiness."""
    risk = colon_bullets(sections.get("Risk And Permission Model", ""))
    impact = colon_bullets(sections.get("Architecture / Project Context Impact", ""))
    risk_level = str(frontmatter.get("risk_level") or "").strip().lower()
    surfaces: set[str] = set()
    source_signals: set[str] = set()

    sensitive_keys = {"auth", "payments", "user_data", "personal_data", "uploads", "secrets", "destructive_actions"}
    for key in sensitive_keys:
        if meaningful(risk.get(key)):
            surfaces.add("security")
            source_signals.add(f"Risk And Permission Model:{key}")

    if meaningful(risk.get("external_services")):
        surfaces.update({"architecture", "api", "security"})
        source_signals.add("Risk And Permission Model:external_services")

    if meaningful(risk.get("dependency_changes")) or meaningful(risk.get("dashboard_manual_steps")):
        surfaces.add("architecture")
        source_signals.add("Risk And Permission Model:tool_and_environment_boundary")

    if str(impact.get("project_context_impact") or "").strip().lower() in {"minor", "material"}:
        surfaces.add("architecture")
        source_signals.add("Architecture / Project Context Impact:project_context_impact")
    if str(impact.get("architecture_shaping") or "").strip().lower() in {"needed", "completed"}:
        surfaces.add("architecture")
        source_signals.add("Architecture / Project Context Impact:architecture_shaping")

    impact_owner_keys = {
        "architecture_authority_updates_needed": "architecture",
        "route_api_authority_updates_needed": "api",
        "schema_authority_updates_needed": "data",
        "security_authority_updates_needed": "security",
    }
    for key, surface in impact_owner_keys.items():
        if meaningful(impact.get(key)):
            surfaces.add(surface)
            source_signals.add(f"Architecture / Project Context Impact:{key}")

    if non_placeholder_rows(sections.get("Module / Interface Candidates", "")):
        surfaces.add("codebase")
        source_signals.add("Module / Interface Candidates:declared_boundary")

    acceptance = acceptance_summary(sections, requirement_ids(sections.get("Requirements", "")))
    if surfaces:
        surfaces.add("verification")
        source_signals.add("Acceptance Oracle Matrix:risk_triggered_proof")

    missing: list[str] = []
    impact_keys_by_surface = {
        "architecture": "architecture_authority_updates_needed",
        "api": "route_api_authority_updates_needed",
        "data": "schema_authority_updates_needed",
        "security": "security_authority_updates_needed",
    }
    for surface, key in impact_keys_by_surface.items():
        if surface in surfaces and not meaningful(impact.get(key)):
            missing.append(f"{OWNER_LABELS[surface]} impact is missing or unclear")
    if "verification" in surfaces and (not acceptance["present"] or not acceptance["has_proof_columns"]):
        missing.append("ACCEPTANCE.md evidence mapping is missing or unclear")

    if surfaces:
        status = "activated"
    elif risk_level in {"medium", "high"}:
        status = "needs_clarification"
        missing.append("medium/high-risk PRD has no explicit production-readiness owner signals")
    else:
        status = "not_triggered"

    expectations: list[str] = []
    if surfaces:
        expectations.append("record observable behavior, evidence lanes, and remaining uncertainty in ACCEPTANCE.md")
    if surfaces & {"api", "data", "security"}:
        expectations.append("use integration or structured manual evidence for connected or sensitive boundaries")
    if surfaces & {"architecture", "data", "security"}:
        expectations.append("name rollback or blocked escape before irreversible or production-facing action")

    if status == "not_triggered":
        next_action = "continue normal PRD handoff; record the low-risk Architecture Shaping skip reason before decomposition"
    elif missing:
        next_action = "review the named owner impacts and unresolved gaps before risky decomposition; do not treat this packet as approval"
    else:
        next_action = "promote reviewed durable decisions into the named owner files before risky decomposition"

    return {
        "status": status,
        "triggering_risk_surfaces": sorted(surfaces),
        "source_signals": sorted(source_signals),
        "recommended_owner_files": [OWNER_LABELS[surface] for surface in OWNER_LABELS if surface in surfaces],
        "missing_or_unclear_owner_impacts": sorted(set(missing)),
        "verification_expectations": expectations,
        "remaining_uncertainty": [
            "This routing is derived from explicit PRD fields, not application-code inspection or external production evidence."
        ],
        "recommended_next_safe_action": next_action,
        "advisory_only": True,
    }


def read_prd(path: Path) -> tuple[dict[str, Any], dict[str, str], dict[str, str], str]:
    text = path.read_text(encoding="utf-8")
    frontmatter, _ = split_frontmatter(text)
    return frontmatter, extract_contract_values(text), parse_sections(text), text


def first_table(section: str) -> tuple[list[str], list[list[str]]]:
    lines = [line.strip() for line in section.splitlines() if line.strip()]
    for index, line in enumerate(lines[:-1]):
        if not line.startswith("|") or not re.match(r"^\|?\s*:?-{3,}:?\s*(\|\s*:?-{3,}:?\s*)+\|?$", lines[index + 1]):
            continue
        headers = [cell.strip() for cell in line.strip("|").split("|")]
        rows: list[list[str]] = []
        cursor = index + 2
        while cursor < len(lines) and lines[cursor].startswith("|"):
            row = [cell.strip() for cell in lines[cursor].strip("|").split("|")]
            if len(row) < len(headers):
                row.extend([""] * (len(headers) - len(row)))
            rows.append(row[: len(headers)])
            cursor += 1
        return headers, rows
    return [], []


def requirement_ids(text: str) -> list[str]:
    return sorted(set(re.findall(r"\bPRD-\d{3}-[A-Z]+[0-9]+\b", text)))


def open_question_blockers(open_questions: str) -> list[str]:
    if not open_questions.strip():
        return []
    lower = open_questions.lower()
    blockers: list[str] = []
    if "| yes |" in lower or "blocking: yes" in lower:
        blockers.append("open questions include a blocking yes signal")
    for marker in ["implementation-changing", "must decide", "needs decision", "blocked", "tbd"]:
        if marker in lower:
            blockers.append(f"open questions include {marker}")
    if lower.count("blocking") > 1:
        blockers.append("open questions include repeated blocking signals")
    return blockers


def acceptance_summary(sections: dict[str, str], ids: list[str]) -> dict[str, Any]:
    acceptance = sections.get("Acceptance Oracle Matrix", "")
    headers, rows = first_table(acceptance)
    row_text = "\n".join(" | ".join(row) for row in rows)
    covered_ids = requirement_ids(row_text)
    missing_ids = [req_id for req_id in ids if req_id not in covered_ids]
    header_text = " ".join(headers).lower()
    proof_terms = ["evidence", "automated", "manual", "check", "source", "proof"]
    return {
        "present": bool(rows),
        "row_count": len(rows),
        "covered_requirement_ids": covered_ids,
        "missing_requirement_ids": missing_ids,
        "has_proof_columns": any(term in header_text for term in proof_terms),
    }


def candidate_bead_summary(sections: dict[str, str]) -> dict[str, Any]:
    bead_section = sections.get("Bead Proposals", "")
    _, rows = first_table(bead_section)
    lower = bead_section.lower()
    return {
        "present": bool(bead_section.strip()),
        "row_count": len(rows),
        "mentions_decomposition": "decomposition" in lower or "candidate bead" in lower or "bead" in lower,
    }


def owner_protocols(sections: dict[str, str]) -> list[str]:
    context = sections.get("Agent Context Contract", "")
    return sorted(set(re.findall(r"tasks/reference/[A-Z0-9-]+\.md", context)))


def forbidden_authority_markers(text: str) -> list[str]:
    lower = text.lower()
    markers = {
        "generated packet is authority": ["generated packet is authority", "packet is authority"],
        "packet approves work": ["packet approves", "packet can approve", "approves the prd"],
        "packet activates work": ["packet activates", "activates beads", "activate beads from this packet"],
        "permission to code": ["permission to code", "authorizes implementation"],
        "external mutation": ["mutate external tools", "external mutation is allowed"],
    }
    found = []
    for label, phrases in markers.items():
        if any(phrase in lower for phrase in phrases):
            found.append(label)
    return found


def next_safe_action(status: str, target: str, blockers: list[str]) -> str:
    normalized = status.lower()
    if normalized != "approved":
        return "continue PRD shaping and approval review before handoff, decomposition, or implementation"
    if blockers:
        return "resolve PRD handoff blockers through PRD amendment, Architecture Shaping, or unblocker planning before activation"
    if target == "decomposition":
        return "use the Decomposition Protocol to propose candidate beads; do not activate them from this packet"
    if target in {"design", "engineering"}:
        return f"use this packet as {target} handoff orientation; reload the Markdown PRD before planning work"
    if target == "review":
        return "use this packet as PRD review evidence; it does not approve the PRD or accept implementation"
    return "ready for advisory PRD handoff review; human approval and normal bead gates still apply"


def build_payload(path: Path, target: str = "general") -> dict[str, Any]:
    frontmatter, contract, sections, text = read_prd(path)
    status = str(frontmatter.get("status") or "unknown")
    ids = requirement_ids(sections.get("Requirements", ""))
    acceptance = acceptance_summary(sections, ids)
    bead_summary = candidate_bead_summary(sections)
    open_blockers = open_question_blockers(sections.get("Open Questions", ""))
    protocols = owner_protocols(sections)
    warnings: list[str] = []

    if status.lower() != "approved":
        warnings.append(f"PRD status is not approved: {status}")
    if not ids:
        warnings.append("no requirement IDs found in Requirements")
    if not acceptance["present"]:
        warnings.append("Acceptance Oracle Matrix is missing or not parseable")
    if acceptance["missing_requirement_ids"]:
        warnings.append("Acceptance Oracle Matrix does not cover requirement IDs: " + ", ".join(acceptance["missing_requirement_ids"]))
    if acceptance["present"] and not acceptance["has_proof_columns"]:
        warnings.append("Acceptance Oracle Matrix does not expose proof, check, source, or evidence columns")
    warnings.extend(open_blockers)
    if target == "decomposition" and not bead_summary["present"]:
        warnings.append("decomposition target needs candidate bead or bead proposal visibility")
    if not sections.get("Risk And Permission Model", "").strip():
        warnings.append("Risk And Permission Model is missing")
    if not protocols:
        warnings.append("Agent Context Contract does not name owner protocols")
    forbidden = forbidden_authority_markers(text)
    if forbidden:
        warnings.append("forbidden authority wording found: " + ", ".join(forbidden))

    blockers = list(warnings)
    packet = {
        "target": target,
        "prd": str(path.relative_to(ROOT) if path.is_relative_to(ROOT) else path),
        "prd_status": status,
        "requirement_ids": ids,
        "open_questions": "present" if sections.get("Open Questions", "").strip() else "none recorded",
        "acceptance_oracle_coverage": acceptance,
        "candidate_bead_or_decomposition_readiness": bead_summary,
        "proof_expectations": {
            "acceptance_oracle_has_proof_columns": acceptance["has_proof_columns"],
            "risk_permission_model_present": bool(sections.get("Risk And Permission Model", "").strip()),
        },
        "risks_and_permissions": "present" if sections.get("Risk And Permission Model", "").strip() else "missing",
        "owner_protocols": protocols,
        "production_readiness_activation": production_readiness_activation(frontmatter, sections),
        "blockers": blockers,
        "recommended_next_safe_action": next_safe_action(status, target, blockers),
        "forbidden_uses": [
            "PRD approval",
            "owner-file edit approval",
            "bead activation",
            "task selection",
            "implementation acceptance",
            "production-readiness certification",
            "external mutation",
            "export automation",
            "MCP behavior",
            "registry behavior",
            "optional-pack behavior",
            "package-manager behavior",
        ],
    }
    return {
        "status": "warning" if warnings else "pass",
        "warnings": warnings,
        "details": {"packet": packet},
        "generated_report_warning": GENERATED_WARNING,
    }


def self_test() -> dict[str, Any]:
    fixtures = {
        "ready": {
            "status": "pass",
            "text": fixture_prd(status="approved"),
            "target": "general",
        },
        "unapproved": {
            "status": "warning",
            "text": fixture_prd(status="draft"),
            "target": "general",
            "warning": "PRD status is not approved",
        },
        "missing acceptance oracle": {
            "status": "warning",
            "text": fixture_prd(acceptance=False),
            "target": "general",
            "warning": "Acceptance Oracle Matrix is missing",
        },
        "implementation-changing questions": {
            "status": "warning",
            "text": fixture_prd(open_questions="| Q | Blocking? |\n|---|---|\n| Must decide API shape before implementation-changing handoff. | Yes |"),
            "target": "general",
            "warning": "open questions include",
        },
        "missing proof expectations": {
            "status": "warning",
            "text": fixture_prd(acceptance_headers="| Requirement ID | Expected behavior |\n|---|---|"),
            "target": "general",
            "warning": "does not expose proof",
        },
        "forbidden authority wording": {
            "status": "warning",
            "text": fixture_prd(extra="This generated packet is authority and packet approves the PRD."),
            "target": "general",
            "warning": "forbidden authority wording",
        },
        "low-risk placeholders do not activate": {
            "status": "pass",
            "text": fixture_prd(
                status="approved",
                risk_level="low",
                extra="Background prose mentions payments, APIs, migrations, secrets, and production without declaring a structured risk.",
            ),
            "target": "general",
            "activation": "not_triggered",
            "owners": [],
        },
        "medium-risk ambiguity needs clarification": {
            "status": "pass",
            "text": fixture_prd(status="approved", risk_level="medium"),
            "target": "general",
            "activation": "needs_clarification",
            "owners": [],
        },
        "architecture owner activates": {
            "status": "pass",
            "text": fixture_prd(
                risk_level="medium",
                architecture_impact="- Project context impact: material\n- Architecture Shaping: needed\n- Architecture authority updates needed: system boundary\n- Route/API authority updates needed: none\n- Schema authority updates needed: none\n- Security authority updates needed: none",
            ),
            "target": "general",
            "activation": "activated",
            "owners": ["ARCHITECTURE.md", "ACCEPTANCE.md"],
        },
        "api owner activates": {
            "status": "pass",
            "text": fixture_prd(
                risk_level="medium",
                architecture_impact="- Project context impact: none\n- Architecture Shaping: skipped\n- Architecture authority updates needed: none\n- Route/API authority updates needed: webhook contract\n- Schema authority updates needed: none\n- Security authority updates needed: none",
            ),
            "target": "general",
            "activation": "activated",
            "owners": ["API.md", "ACCEPTANCE.md"],
        },
        "data owner activates": {
            "status": "pass",
            "text": fixture_prd(
                risk_level="medium",
                architecture_impact="- Project context impact: none\n- Architecture Shaping: skipped\n- Architecture authority updates needed: none\n- Route/API authority updates needed: none\n- Schema authority updates needed: migration boundary\n- Security authority updates needed: none",
            ),
            "target": "general",
            "activation": "activated",
            "owners": ["DATA-MODELS.md", "ACCEPTANCE.md"],
        },
        "security owner activates": {
            "status": "pass",
            "text": fixture_prd(
                risk_level="medium",
                risk_model="- Auth: role boundary",
                architecture_impact="- Project context impact: none\n- Architecture Shaping: skipped\n- Architecture authority updates needed: none\n- Route/API authority updates needed: none\n- Schema authority updates needed: none\n- Security authority updates needed: access policy",
            ),
            "target": "general",
            "activation": "activated",
            "owners": ["SECURITY.md", "ACCEPTANCE.md"],
        },
        "codebase owner activates": {
            "status": "pass",
            "text": fixture_prd(
                risk_level="medium",
                module_candidates="| Candidate module or boundary | Public interface / caller expectation | Behavior contract | Test boundary | Owner file |\n|---|---|---|---|---|\n| Adapter | one caller | local boundary | static | CODEBASE-GUIDE.md |",
            ),
            "target": "general",
            "activation": "activated",
            "owners": ["CODEBASE-GUIDE.md", "ACCEPTANCE.md"],
        },
        "verification owner follows activated risk": {
            "status": "pass",
            "text": fixture_prd(
                risk_level="medium",
                architecture_impact="- Project context impact: none\n- Architecture Shaping: skipped\n- Architecture authority updates needed: none\n- Route/API authority updates needed: API contract\n- Schema authority updates needed: none\n- Security authority updates needed: none",
            ),
            "target": "general",
            "activation": "activated",
            "owners": ["API.md", "ACCEPTANCE.md"],
        },
        "all six owners activate from explicit fields": {
            "status": "pass",
            "text": fixture_prd(
                status="approved",
                risk_level="high",
                risk_model="""### Sensitive Surfaces

- Auth: role-gated account access
- Payments:
- User data: private account records
- Uploads:
- External services: fulfillment provider
- Secrets: SYNTHETIC-SECRET-MUST-NOT-ECHO
- Destructive actions: migration rollback

### Human Approval Gates

- Approval required before: external mutation
""",
                architecture_impact="""- Project context impact: material
- Architecture Shaping: completed
- Architecture authority updates needed: state and recovery boundary
- Route/API authority updates needed: webhook contract
- Schema authority updates needed: migration and retention
- Security authority updates needed: access and secret boundary
""",
                module_candidates="""| Candidate module or boundary | Public interface / caller expectation | Behavior contract | Test boundary | Owner file |
|---|---|---|---|---|
| Fulfillment adapter | Approved calls only | Isolate provider behavior | integration | CODEBASE-GUIDE.md |
""",
            ),
            "target": "general",
            "activation": "activated",
            "owners": list(OWNER_LABELS.values()),
            "not_echo": "SYNTHETIC-SECRET-MUST-NOT-ECHO",
        },
    }
    failures: list[dict[str, str]] = []
    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = Path(tmp)
        for name, fixture in fixtures.items():
            path = tmp_path / f"{name.replace(' ', '-')}.md"
            path.write_text(str(fixture["text"]), encoding="utf-8")
            payload = build_payload(path, str(fixture["target"]))
            if payload.get("status") != fixture["status"]:
                failures.append({"scenario": name, "expected": str(fixture["status"]), "actual": str(payload.get("status"))})
            expected_warning = fixture.get("warning")
            if expected_warning and expected_warning not in " ".join(payload.get("warnings") or []):
                failures.append({"scenario": name, "expected": str(expected_warning), "actual": str(payload.get("warnings"))})
            packet = (payload.get("details") or {}).get("packet") or {}
            for key in ["prd_status", "requirement_ids", "acceptance_oracle_coverage", "blockers", "recommended_next_safe_action"]:
                if key not in packet:
                    failures.append({"scenario": f"{name} packet key", "expected": key, "actual": "missing"})
            activation = packet.get("production_readiness_activation") or {}
            for key in [
                "status",
                "triggering_risk_surfaces",
                "recommended_owner_files",
                "missing_or_unclear_owner_impacts",
                "verification_expectations",
                "remaining_uncertainty",
                "recommended_next_safe_action",
                "advisory_only",
            ]:
                if key not in activation:
                    failures.append({"scenario": f"{name} activation key", "expected": key, "actual": "missing"})
            expected_activation = fixture.get("activation")
            if expected_activation and activation.get("status") != expected_activation:
                failures.append({"scenario": f"{name} activation", "expected": str(expected_activation), "actual": str(activation.get("status"))})
            expected_owners = fixture.get("owners")
            if expected_owners is not None and activation.get("recommended_owner_files") != expected_owners:
                failures.append({"scenario": f"{name} owners", "expected": str(expected_owners), "actual": str(activation.get("recommended_owner_files"))})
            if activation.get("advisory_only") is not True:
                failures.append({"scenario": f"{name} advisory", "expected": "true", "actual": str(activation.get("advisory_only"))})
            not_echo = fixture.get("not_echo")
            if not_echo and str(not_echo) in json.dumps(payload):
                failures.append({"scenario": f"{name} sensitive echo", "expected": "redacted", "actual": str(not_echo)})
            forbidden = " ".join(packet.get("forbidden_uses") or [])
            for term in [
                "PRD approval",
                "owner-file edit approval",
                "bead activation",
                "implementation acceptance",
                "production-readiness certification",
                "MCP behavior",
            ]:
                if term not in forbidden:
                    failures.append({"scenario": f"{name} forbidden uses", "expected": term, "actual": forbidden})

    return {
        "tool": "prd-handoff-readiness",
        "mode": "self-test",
        "status": "pass" if not failures else "fail",
        "scenario_count": len(fixtures),
        "failures": failures,
    }


def fixture_prd(
    *,
    status: str = "approved",
    acceptance: bool = True,
    acceptance_headers: str = "| Requirement ID | Expected behavior | Automated check | Manual check | Evidence location |\n|---|---|---|---|---|",
    open_questions: str = "| Question | Blocking? |\n|---|---|\n| None. | No |",
    risk_level: str = "low",
    risk_model: str = "- Approval required before: none",
    architecture_impact: str = "- Project context impact: none\n- Architecture Shaping: skipped\n- Architecture Shaping skip reason: low-risk fixture\n- Architecture authority updates needed: none\n- Route/API authority updates needed: none\n- Schema authority updates needed: none\n- Security authority updates needed: none",
    module_candidates: str = "| Candidate module or boundary | Public interface / caller expectation | Behavior contract | Test boundary | Owner file |\n|---|---|---|---|---|",
    extra: str = "",
) -> str:
    acceptance_section = ""
    if acceptance:
        acceptance_section = f"""## Acceptance Oracle Matrix

{acceptance_headers}
| PRD-999-FR01 | Packet is advisory. | self-test | inspect JSON | command output |
"""
    return f"""---
prd_id: PRD-999
status: {status}
risk_level: {risk_level}
feature_link: Fixture
---

# PRD-999 -- Fixture

> AUTHORITY: Fixture PRD.
> NOT_AUTHORITY: Active memory, PRD approval, bead activation, task selection, implementation acceptance, external mutation, MCP behavior, registry behavior, optional-pack behavior, or package-manager behavior.
> LOAD_WHEN: Testing PRD handoff readiness.
> CLASS: reference

Creator: Dan Sears / Recode
Document version: v0.1.0
Last updated: 2026-06-24

## Requirements

| ID | Requirement | Priority | Notes |
|---|---|---|---|
| PRD-999-FR01 | Packet is advisory. | P0 | No authority. |

## Open Questions

{open_questions}

{acceptance_section}
## Risk And Permission Model

{risk_model}

## Architecture / Project Context Impact

{architecture_impact}

## Module / Interface Candidates

{module_candidates}

## Agent Context Contract

- Owner protocol: `tasks/reference/PRD-PROTOCOL.md`

## Bead Proposals

| Candidate | Purpose |
|---|---|
| B999 | Fixture bead proposal only. |

{extra}
"""


def main() -> int:
    parser = argparse.ArgumentParser(description="Show read-only PRD Handoff Readiness Packet advisory JSON.")
    parser.add_argument("--prd", help="path to a canonical Markdown PRD shard")
    parser.add_argument("--target", choices=sorted(VALID_TARGETS), default="general", help="handoff target lens")
    parser.add_argument("--self-test", action="store_true", help="run deterministic PRD handoff readiness fixture checks")
    args = parser.parse_args()

    if args.self_test:
        payload = self_test()
        print(json.dumps(payload, indent=2, sort_keys=True))
        return 0 if payload.get("status") == "pass" else 1

    if not args.prd:
        parser.error("--prd is required unless --self-test is used")

    path = Path(args.prd)
    if not path.is_absolute():
        path = ROOT / path
    if not path.is_file():
        parser.error(f"PRD file not found: {path}")

    payload = {"tool": "prd-handoff-readiness", **build_payload(path, args.target)}
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0 if payload.get("status") == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
