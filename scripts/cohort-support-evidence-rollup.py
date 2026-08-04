#!/usr/bin/env python3
# Version: v0.1.1
# Last updated: 2026-08-04
# Owner: PrecodeOS
# Created by Dan Sears / Recode.
# SPDX-License-Identifier: Apache-2.0
from __future__ import annotations

import argparse
from collections import Counter
import glob as globlib
import json
from pathlib import Path
import re
import sys
from typing import Any


FORBIDDEN_USES = [
    "adoption proof",
    "product validation",
    "support case record",
    "user identity record",
    "grading",
    "contributor scoring",
    "productivity ranking",
    "task selection",
    "roadmap selection",
    "PRD approval",
    "bead activation",
    "implementation acceptance",
    "review acceptance",
    "telemetry authorization",
    "external submission",
    "package-manager behavior",
]

SENSITIVE_PATTERNS = [
    ("secret_like_key", re.compile(r"(?i)\b(api[_ -]?key|secret|token|password|credential|private key)\b")),
    ("dashboard_or_billing", re.compile(r"(?i)\b(dashboard value|billing|payment|customer record|account id)\b")),
    ("raw_private_source", re.compile(r"(?i)\b(raw transcript|app log|private support note|production config)\b")),
    ("identity_or_scoring", re.compile(r"(?i)\b(user id|email address|phone number|support case|productivity|score)\b")),
]

FIELD_ALIASES = {
    "target_context": ["Target context"],
    "setup_or_refresh_friction": ["Setup or refresh friction"],
    "setup_source_target_clarity": ["Setup source/target clarity"],
    "setup_target_kind": ["Setup target kind"],
    "missing_reusable_setup_support_files": ["Missing reusable setup support files"],
    "setup_approval_latency_or_blocker": ["Setup approval latency or blocker"],
    "setup_command_sequence_confusion": ["Setup command sequence confusion"],
    "setup_validation_failure": ["Setup validation failure"],
    "prepared_support_artifact_used": ["Prepared support artifact used"],
    "setup_next_safe_route": ["Setup next safe route"],
    "confusing_docs_prompts_commands_or_templates": ["Confusing docs, prompts, commands, or templates"],
    "support_intervention_type": ["Support intervention type"],
    "control_value": ["What Precode helped the user control", "What Precode helped the builder control"],
    "unclear_or_too_heavy": ["What remained unclear or too heavy", "What felt too heavy or unclear"],
    "checks_or_generated_evidence_reviewed": ["Checks or generated evidence reviewed", "How it was checked"],
    "unknown_because_not_logged": ["Unknown because not logged"],
    "redactions_performed": ["Redactions performed"],
}

SOURCE_REF_LIMIT = 20
PACKET_VOLUME_THRESHOLD = 3
SETUP_FRICTION_FIELD_KEYS = (
    "setup_source_target_clarity",
    "setup_target_kind",
    "missing_reusable_setup_support_files",
    "setup_approval_latency_or_blocker",
    "setup_command_sequence_confusion",
    "setup_validation_failure",
    "prepared_support_artifact_used",
    "setup_next_safe_route",
)


def repo_root(start: Path | None = None) -> Path:
    current = (start or Path.cwd()).resolve()
    for candidate in (current, *current.parents):
        if (candidate / "AGENT.md").exists() and (candidate / "tasks").exists() and (candidate / "scripts").exists():
            return candidate
    return current


def normalize_text(value: object) -> str:
    return " ".join(str(value or "").split())


def safe_excerpt(value: object, *, limit: int = 80) -> str:
    text = normalize_text(value)
    if len(text) <= limit:
        return text
    return text[: limit - 3] + "..."


def is_blank_or_placeholder(value: str) -> bool:
    lowered = normalize_text(value).lower()
    return not lowered or lowered in {
        "yes | no",
        "new project | existing project | cohort | support | maintainer review",
        "none | setup | repo state | validation/checks | local runtime | auth/demo blocker | product-routing clarification | other",
    }


def first_field(text: str, labels: list[str]) -> tuple[str, int, str]:
    lines = text.splitlines()
    for idx, line in enumerate(lines, start=1):
        for label in labels:
            pattern = rf"^[ \t]*(?:[-*][ \t]*)?{re.escape(label)}[ \t]*:[ \t]*(.*)$"
            match = re.match(pattern, line)
            if match:
                return match.group(1).strip(), idx, label
    return "", 0, labels[0]


def sensitive_hits(text: str) -> list[dict[str, str]]:
    hits: list[dict[str, str]] = []
    for name, pattern in SENSITIVE_PATTERNS:
        for match in pattern.finditer(text):
            hits.append({"pattern": name, "match": match.group(0)})
            break
    return hits


def packet_kind(text: str) -> str:
    if "Builder Completion Evidence Packet" in text or "Gate 1: Discovery" in text:
        return "builder_completion_packet"
    if "Sanitized Submitted Evidence Packet" in text or "Pre-Submit Checklist" in text:
        return "sanitized_submitted_packet"
    return "unknown_packet_shape"


def read_packet(path: Path, root: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    fields: dict[str, dict[str, Any]] = {}
    for key, labels in FIELD_ALIASES.items():
        value, line, label = first_field(text, labels)
        fields[key] = {
            "value": value,
            "present": not is_blank_or_placeholder(value),
            "line": line,
            "label": label,
        }
    try:
        display_path = str(path.resolve().relative_to(root))
    except ValueError:
        display_path = str(path)
    return {
        "path": display_path,
        "kind": packet_kind(text),
        "fields": fields,
        "sensitive_hits": sensitive_hits(text),
    }


def expand_inputs(root: Path, packets: list[str], globs: list[str]) -> tuple[list[Path], list[str]]:
    warnings: list[str] = []
    paths: list[Path] = []
    for packet in packets:
        path = Path(packet)
        paths.append(path if path.is_absolute() else root / path)
    for pattern in globs:
        if Path(pattern).is_absolute():
            matches = [Path(item) for item in globlib.glob(pattern)]
        else:
            matches = [Path(item) for item in globlib.glob(str(root / pattern))]
        if not matches:
            warnings.append(f"glob matched no packet files: {pattern}")
        paths.extend(matches)
    unique: list[Path] = []
    seen: set[Path] = set()
    for path in paths:
        resolved = path.resolve()
        if resolved not in seen:
            unique.append(resolved)
            seen.add(resolved)
    return unique, warnings


def presence_counts(packets: list[dict[str, Any]], key: str) -> dict[str, int]:
    counts = Counter("present" if packet["fields"][key]["present"] else "unknown_or_blank" for packet in packets)
    return dict(sorted(counts.items()))


def value_counts(packets: list[dict[str, Any]], key: str) -> dict[str, int]:
    values = [
        normalize_text(packet["fields"][key]["value"]).lower()
        for packet in packets
        if packet["fields"][key]["present"]
    ]
    if not values:
        return {"unknown_or_blank": len(packets)}
    counts = Counter(values)
    if len(values) < len(packets):
        counts["unknown_or_blank"] += len(packets) - len(values)
    return dict(sorted(counts.items()))


def source_refs(packets: list[dict[str, Any]]) -> list[str]:
    refs: list[str] = []
    for packet in packets:
        for key, field in packet["fields"].items():
            if field["present"] and field["line"]:
                refs.append(f"{packet['path']}:{field['line']}:{field['label']}")
            if len(refs) >= SOURCE_REF_LIMIT:
                return refs
    return refs


def build_rollup(packets: list[dict[str, Any]], warnings: list[str]) -> dict[str, Any]:
    packet_count = len(packets)
    packet_volume_status = "sufficient_for_pattern_review" if packet_count >= PACKET_VOLUME_THRESHOLD else "unknown_insufficient_packet_volume"
    all_sensitive_hits = [
        {"path": packet["path"], **hit}
        for packet in packets
        for hit in packet["sensitive_hits"]
    ]
    rollup_warnings = list(warnings)
    if packet_count < PACKET_VOLUME_THRESHOLD:
        rollup_warnings.append("fewer than 3 explicit packet files supplied; repeated-pattern evidence is unknown, not zero")
    if all_sensitive_hits:
        rollup_warnings.append("sensitive-looking terms need redaction review before sharing or promotion")
    unknown_required = [
        key
        for key in (
            "setup_or_refresh_friction",
            "confusing_docs_prompts_commands_or_templates",
            "support_intervention_type",
            "control_value",
            "unknown_because_not_logged",
            "redactions_performed",
        )
        if any(not packet["fields"][key]["present"] for packet in packets)
    ]
    if unknown_required:
        rollup_warnings.append("some packet fields are blank or unknown; do not treat missing fields as no friction")

    return {
        "tool": "cohort-support-evidence-rollup",
        "status": "warning" if rollup_warnings else "pass",
        "advisory_only": True,
        "read_only": True,
        "mutates_files": False,
        "writes_generated_report": False,
        "submits_externally": False,
        "network_calls": False,
        "evidence_only": True,
        "owner_prd": "tasks/prds/PRD-048-precode-usage-evidence-review.md",
        "packet_count": packet_count,
        "packet_volume_status": packet_volume_status,
        "packet_kinds": dict(sorted(Counter(packet["kind"] for packet in packets).items())),
        "counts": {
            "target_context": value_counts(packets, "target_context"),
            "setup_or_refresh_friction": presence_counts(packets, "setup_or_refresh_friction"),
            "confusing_docs_prompts_commands_or_templates": presence_counts(
                packets,
                "confusing_docs_prompts_commands_or_templates",
            ),
            "support_intervention_type": value_counts(packets, "support_intervention_type"),
            "control_value": presence_counts(packets, "control_value"),
            "unclear_or_too_heavy": presence_counts(packets, "unclear_or_too_heavy"),
            "checks_or_generated_evidence_reviewed": presence_counts(
                packets,
                "checks_or_generated_evidence_reviewed",
            ),
            "unknown_because_not_logged": presence_counts(packets, "unknown_because_not_logged"),
            "redactions_performed": presence_counts(packets, "redactions_performed"),
        },
        "source_refs": source_refs(packets),
        "sensitive_hits": all_sensitive_hits[:SOURCE_REF_LIMIT],
        "warnings": rollup_warnings,
        "forbidden_uses": FORBIDDEN_USES,
        "boundary": (
            "This rollup aggregates only explicit packet files supplied by path or glob. It is source evidence only: "
            "it does not prove adoption, create support records, score people, choose roadmap work, approve PRDs or beads, "
            "submit externally, collect telemetry, write reports, or mutate files."
        ),
    }


def build_setup_friction_rollup(packets: list[dict[str, Any]], warnings: list[str]) -> dict[str, Any]:
    payload = build_rollup(packets, warnings)
    setup_counts = {
        "setup_or_refresh_friction": presence_counts(packets, "setup_or_refresh_friction"),
        "setup_source_target_clarity": presence_counts(packets, "setup_source_target_clarity"),
        "setup_target_kind": value_counts(packets, "setup_target_kind"),
        "missing_reusable_setup_support_files": presence_counts(packets, "missing_reusable_setup_support_files"),
        "setup_approval_latency_or_blocker": presence_counts(packets, "setup_approval_latency_or_blocker"),
        "setup_command_sequence_confusion": presence_counts(packets, "setup_command_sequence_confusion"),
        "setup_validation_failure": presence_counts(packets, "setup_validation_failure"),
        "prepared_support_artifact_used": presence_counts(packets, "prepared_support_artifact_used"),
        "setup_next_safe_route": presence_counts(packets, "setup_next_safe_route"),
        "unknown_because_not_logged": presence_counts(packets, "unknown_because_not_logged"),
    }
    missing_setup_fields = [
        key
        for key in SETUP_FRICTION_FIELD_KEYS
        if any(not packet["fields"][key]["present"] for packet in packets)
    ]
    setup_warnings = list(payload["warnings"])
    if missing_setup_fields:
        setup_warnings.append(
            "some setup-friction fields are blank or unknown; do not treat missing setup fields as no friction"
        )
    payload.update(
        {
            "tool": "cohort-support-evidence-rollup",
            "mode": "setup_friction",
            "setup_friction_focus": True,
            "status": "warning" if setup_warnings else "pass",
            "setup_friction_counts": setup_counts,
            "warnings": setup_warnings,
            "boundary": (
                "This setup-friction lens aggregates only explicit packet files supplied by path or glob. It is source "
                "evidence only: it does not prove adoption, create support records, choose roadmap work, approve PRDs "
                "or beads, authorize telemetry, submit externally, write reports, or mutate files."
            ),
        }
    )
    return payload


def render_plain(payload: dict[str, Any]) -> str:
    setup_mode = bool(payload.get("setup_friction_focus"))
    lines = [
        "Support Setup Friction Evidence Loop" if setup_mode else "Cohort/Support Evidence Rollup",
        f"Status: {payload['status']}",
        f"Packet files reviewed: {payload['packet_count']}",
        f"Packet volume: {payload['packet_volume_status']}",
        "Boundary: read-only packet-file aggregation; no writes, submissions, telemetry, support records, scoring, or roadmap selection.",
    ]
    warnings = payload.get("warnings") or []
    if warnings:
        lines.append("")
        lines.append("Warnings:")
        for warning in warnings:
            lines.append(f"- {warning}")
    lines.append("")
    lines.append("Counts:")
    for key, counts in payload["counts"].items():
        rendered = ", ".join(f"{name}={count}" for name, count in counts.items())
        lines.append(f"- {key}: {rendered}")
    if setup_mode:
        lines.append("")
        lines.append("Setup friction counts:")
        for key, counts in payload["setup_friction_counts"].items():
            rendered = ", ".join(f"{name}={count}" for name, count in counts.items())
            lines.append(f"- {key}: {rendered}")
    refs = payload.get("source_refs") or []
    if refs:
        lines.append("")
        lines.append("Source refs:")
        for ref in refs:
            lines.append(f"- {ref}")
    lines.append("")
    lines.append(str(payload["boundary"]))
    return "\n".join(lines) + "\n"


def self_test() -> dict[str, Any]:
    support_packet = """# Sanitized Submitted Evidence Packet

## Packet

Usage evidence purpose: review setup friction
Target context: support
Workflow moments used: guided setup
Setup or refresh friction: setup command sequence was unclear
Confusing docs, prompts, commands, or templates: Guided Setup command block
Support intervention type: setup
What Precode helped the user control: copy approval boundaries
What remained unclear or too heavy: where to start after validation
Checks or generated evidence reviewed: bootstrap preview
Unknown because not logged: exact elapsed time
Redactions performed: removed private paths
Submitted through: private maintainer channel
Setup source/target clarity: source and target were initially reversed
Setup target kind: nearly empty target
Missing reusable setup support files: PRD template missing
Setup approval latency or blocker: UP-ID approval needed support explanation
Setup command sequence confusion: fast setup preview path was easier
Setup validation failure: validation not run before handoff
Prepared support artifact used: no
Setup next safe route: validate memory then first-session card
"""
    cohort_packet = """# Builder Completion Evidence Packet

### PrecodeOS Usage Evidence Notes

- Setup or refresh friction: none captured in packet
- Setup source/target clarity:
- Setup target kind:
- Missing reusable setup support files:
- Setup approval latency or blocker:
- Setup command sequence confusion:
- Setup validation failure:
- Prepared support artifact used:
- Setup next safe route:
- Confusing docs, prompts, commands, or templates:
- Support intervention type: validation/checks
- What Precode helped the builder control: proof before continuing
- What felt too heavy or unclear: Daily Cockpit felt large
- Unknown because not logged: exact support intervention count
- Redactions performed: no private data included
"""
    sparse_packet = """# Sanitized Submitted Evidence Packet

## Packet

Target context: cohort
Support intervention type: support case
Redactions performed:
"""
    packets = [
        {
            "path": "support.md",
            "kind": packet_kind(support_packet),
            "fields": {
                key: {
                    "value": first_field(support_packet, labels)[0],
                    "present": not is_blank_or_placeholder(first_field(support_packet, labels)[0]),
                    "line": first_field(support_packet, labels)[1],
                    "label": first_field(support_packet, labels)[2],
                }
                for key, labels in FIELD_ALIASES.items()
            },
            "sensitive_hits": sensitive_hits(support_packet),
        },
        {
            "path": "cohort.md",
            "kind": packet_kind(cohort_packet),
            "fields": {
                key: {
                    "value": first_field(cohort_packet, labels)[0],
                    "present": not is_blank_or_placeholder(first_field(cohort_packet, labels)[0]),
                    "line": first_field(cohort_packet, labels)[1],
                    "label": first_field(cohort_packet, labels)[2],
                }
                for key, labels in FIELD_ALIASES.items()
            },
            "sensitive_hits": sensitive_hits(cohort_packet),
        },
        {
            "path": "sparse.md",
            "kind": packet_kind(sparse_packet),
            "fields": {
                key: {
                    "value": first_field(sparse_packet, labels)[0],
                    "present": not is_blank_or_placeholder(first_field(sparse_packet, labels)[0]),
                    "line": first_field(sparse_packet, labels)[1],
                    "label": first_field(sparse_packet, labels)[2],
                }
                for key, labels in FIELD_ALIASES.items()
            },
            "sensitive_hits": sensitive_hits(sparse_packet),
        },
    ]
    payload = build_rollup(packets, [])
    setup_payload = build_setup_friction_rollup(packets, [])
    sparse_payload = build_rollup(packets[:1], [])
    failures: list[str] = []
    if payload["packet_count"] != 3:
        failures.append("expected three packet fixtures")
    if payload["packet_volume_status"] != "sufficient_for_pattern_review":
        failures.append("three packet fixtures should meet the pattern-review volume threshold")
    if payload["counts"]["support_intervention_type"].get("setup") != 1:
        failures.append("support intervention type counts should include setup")
    if "sensitive-looking terms need redaction review before sharing or promotion" not in payload["warnings"]:
        failures.append("support case wording should trigger sensitive redaction review")
    if not setup_payload["setup_friction_focus"]:
        failures.append("setup friction rollup should report setup_friction_focus")
    if setup_payload["setup_friction_counts"]["setup_source_target_clarity"].get("present") != 1:
        failures.append("setup friction rollup should count setup source/target clarity")
    if setup_payload["setup_friction_counts"]["setup_target_kind"].get("nearly empty target") != 1:
        failures.append("setup friction rollup should count setup target kind values")
    if "some setup-friction fields are blank or unknown; do not treat missing setup fields as no friction" not in setup_payload["warnings"]:
        failures.append("setup friction rollup should warn on missing setup fields")
    if sparse_payload["packet_volume_status"] != "unknown_insufficient_packet_volume":
        failures.append("single packet should report unknown insufficient packet volume")
    for result in (payload, setup_payload, sparse_payload):
        if result["mutates_files"] or result["writes_generated_report"] or result["submits_externally"] or result["network_calls"]:
            failures.append("rollup boundary flags must stay no-write, no-submit, no-network")
        if "roadmap selection" not in result["forbidden_uses"]:
            failures.append("rollup forbidden uses must include roadmap selection")
    return {
        "tool": "cohort-support-evidence-rollup",
        "mode": "self-test",
        "status": "pass" if not failures else "fail",
        "scenario_count": 3,
        "failures": failures,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Roll up explicit cohort/support usage-evidence packet files.")
    parser.add_argument("--packet", action="append", default=[], help="explicit packet file to include; repeatable")
    parser.add_argument("--glob", action="append", default=[], help="explicit packet glob to include; repeatable")
    parser.add_argument(
        "--setup-friction",
        action="store_true",
        help="print the setup-specific friction evidence lens over the explicit packet files",
    )
    parser.add_argument("--json", action="store_true", help="print JSON output")
    parser.add_argument("--self-test", action="store_true", help="run deterministic self-tests")
    args = parser.parse_args(argv)

    if args.self_test:
        result = self_test()
        print(json.dumps(result, indent=2, sort_keys=True))
        return 0 if result["status"] == "pass" else 1

    if not args.packet and not args.glob:
        parser.error("cohort/support rollup requires at least one --packet <path> or --glob <pattern>; no default repo scan is performed")

    root = repo_root()
    paths, warnings = expand_inputs(root, args.packet, args.glob)
    missing = [str(path) for path in paths if not path.exists()]
    readable_paths = [path for path in paths if path.exists()]
    warnings.extend(f"packet file not found: {path}" for path in missing)
    packets = [read_packet(path, root) for path in readable_paths]
    payload = build_setup_friction_rollup(packets, warnings) if args.setup_friction else build_rollup(packets, warnings)
    if args.json:
        print(json.dumps(payload, indent=2, sort_keys=True))
    else:
        print(render_plain(payload), end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
