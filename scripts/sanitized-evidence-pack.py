#!/usr/bin/env python3
# Version: v0.1.1
# Last updated: 2026-08-04
# Owner: PrecodeOS
# Created by Dan Sears / Recode.
# SPDX-License-Identifier: Apache-2.0
from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import sys
from typing import Any


PACKET_TEMPLATE = """# Sanitized Submitted Evidence Packet

## Pre-Submit Checklist

- Redactions reviewed: yes | no
- Submission destination chosen: GitHub feedback | package-bug issue | cohort packet | private maintainer channel
- Evidence-only limits understood: yes | no

## Packet

Usage evidence purpose:
PrecodeOS version or package source, if known:
Target context: new project | existing project | cohort | support | maintainer review
Workflow moments used:
Setup or refresh friction:
Setup source/target clarity:
Setup target kind:
Missing reusable setup support files:
Setup approval latency or blocker:
Setup command sequence confusion:
Setup validation failure:
Prepared support artifact used:
Setup next safe route:
Confusing docs, prompts, commands, or templates:
Support intervention type:
What Precode helped the user control:
What remained unclear or too heavy:
Checks or generated evidence reviewed:
Unknown because not logged:
Redactions performed:
Submitted through: GitHub feedback | package-bug issue | cohort packet | private maintainer channel
"""


REQUIRED_FIELDS = [
    "Usage evidence purpose",
    "PrecodeOS version or package source, if known",
    "Target context",
    "Workflow moments used",
    "Setup or refresh friction",
    "Confusing docs, prompts, commands, or templates",
    "Support intervention type",
    "What Precode helped the user control",
    "What remained unclear or too heavy",
    "Checks or generated evidence reviewed",
    "Unknown because not logged",
    "Redactions performed",
    "Submitted through",
]

CHECKLIST_FIELDS = [
    "Redactions reviewed",
    "Submission destination chosen",
    "Evidence-only limits understood",
]

DESTINATIONS = {
    "github feedback",
    "package-bug issue",
    "cohort packet",
    "private maintainer channel",
}

SENSITIVE_PATTERNS = [
    ("secret_like_key", re.compile(r"(?i)\b(api[_ -]?key|secret|token|password|credential|private key)\b")),
    ("dashboard_or_billing", re.compile(r"(?i)\b(dashboard value|billing|payment|customer record|account id)\b")),
    ("raw_private_source", re.compile(r"(?i)\b(raw transcript|app log|private support note|production config)\b")),
    ("identity_or_scoring", re.compile(r"(?i)\b(user id|email address|phone number|support case|productivity|score)\b")),
]


def field_value(text: str, label: str) -> str:
    pattern = re.compile(rf"(?im)^[ \t]*(?:[-*][ \t]*)?{re.escape(label)}[ \t]*:[ \t]*(.*)$")
    match = pattern.search(text)
    if not match:
        return ""
    return match.group(1).strip()


def is_blank_or_placeholder(value: str) -> bool:
    lowered = value.strip().lower()
    return not lowered or lowered in {"yes | no", "new project | existing project | cohort | support | maintainer review"}


def review_packet(text: str) -> dict[str, Any]:
    missing_fields = [label for label in REQUIRED_FIELDS if not field_value(text, label)]
    empty_fields = [label for label in REQUIRED_FIELDS if label not in missing_fields and is_blank_or_placeholder(field_value(text, label))]
    missing_checklist = [label for label in CHECKLIST_FIELDS if not field_value(text, label)]
    checklist_not_confirmed = [
        label
        for label in ("Redactions reviewed", "Evidence-only limits understood")
        if field_value(text, label).lower() not in {"yes", "yes.", "reviewed"}
    ]

    destination_value = field_value(text, "Submitted through") or field_value(text, "Submission destination chosen")
    normalized_destination = destination_value.strip().lower()
    bad_destination = bool(destination_value) and normalized_destination not in DESTINATIONS

    sensitive_hits: list[dict[str, str]] = []
    for name, pattern in SENSITIVE_PATTERNS:
        for match in pattern.finditer(text):
            sensitive_hits.append({"pattern": name, "match": match.group(0)})
            break

    warnings: list[str] = []
    if missing_fields:
        warnings.append("missing required packet fields")
    if empty_fields:
        warnings.append("blank or placeholder packet fields need review")
    if missing_checklist:
        warnings.append("missing pre-submit checklist fields")
    if checklist_not_confirmed:
        warnings.append("pre-submit checklist is not fully confirmed")
    if not field_value(text, "Unknown because not logged"):
        warnings.append("missing explicit unknown-because-not-logged field")
    if not field_value(text, "Redactions performed"):
        warnings.append("missing redactions-performed field")
    if not destination_value:
        warnings.append("missing submission destination")
    elif bad_destination:
        warnings.append("submission destination is not one of the allowed reviewed routes")
    if sensitive_hits:
        warnings.append("sensitive-looking terms need redaction review")

    return {
        "status": "warn" if warnings else "pass",
        "advisory_only": True,
        "mutates_files": False,
        "submits_externally": False,
        "evidence_only": True,
        "warnings": warnings,
        "missing_fields": missing_fields,
        "empty_fields": empty_fields,
        "missing_checklist": missing_checklist,
        "checklist_not_confirmed": checklist_not_confirmed,
        "submission_destination": destination_value,
        "sensitive_hits": sensitive_hits,
        "boundary": (
            "This review is local advisory evidence only. It does not submit evidence, create issues, "
            "approve PRDs or beads, prove adoption, create support records, authorize telemetry, or choose roadmap work."
        ),
    }


def render_plain(result: dict[str, Any]) -> str:
    lines = [
        "Sanitized Submitted Evidence Pack Review",
        f"Status: {result['status']}",
        "Boundary: local advisory review only; no submission or external mutation.",
    ]
    warnings = result.get("warnings") or []
    if warnings:
        lines.append("")
        lines.append("Warnings:")
        for warning in warnings:
            lines.append(f"- {warning}")
    for key, label in (
        ("missing_fields", "Missing fields"),
        ("empty_fields", "Blank or placeholder fields"),
        ("missing_checklist", "Missing checklist fields"),
        ("checklist_not_confirmed", "Checklist not confirmed"),
    ):
        values = result.get(key) or []
        if values:
            lines.append(f"{label}: {', '.join(values)}")
    sensitive_hits = result.get("sensitive_hits") or []
    if sensitive_hits:
        hits = ", ".join(hit["pattern"] for hit in sensitive_hits)
        lines.append(f"Sensitive-looking patterns: {hits}")
    lines.append("")
    lines.append(str(result["boundary"]))
    return "\n".join(lines) + "\n"


def self_test() -> dict[str, Any]:
    good_packet = PACKET_TEMPLATE.replace("yes | no", "yes").replace(
        "Usage evidence purpose:",
        "Usage evidence purpose: explain setup friction safely",
    )
    good_packet = good_packet.replace(
        "PrecodeOS version or package source, if known:",
        "PrecodeOS version or package source, if known: local package source",
    )
    good_packet = good_packet.replace(
        "Target context: new project | existing project | cohort | support | maintainer review",
        "Target context: support",
    )
    for label in REQUIRED_FIELDS:
        if not field_value(good_packet, label):
            good_packet = good_packet.replace(f"{label}:", f"{label}: safe summary")
    good_packet = good_packet.replace(
        "Submitted through: GitHub feedback | package-bug issue | cohort packet | private maintainer channel",
        "Submitted through: GitHub feedback",
    )
    good_packet = good_packet.replace(
        "- Submission destination chosen: GitHub feedback | package-bug issue | cohort packet | private maintainer channel",
        "- Submission destination chosen: GitHub feedback",
    )

    missing_redaction_packet = good_packet.replace("Redactions performed: safe summary", "Redactions performed:")
    sensitive_packet = good_packet + "\nRaw transcript includes API key and dashboard value.\n"

    good = review_packet(good_packet)
    missing = review_packet(missing_redaction_packet)
    sensitive = review_packet(sensitive_packet)

    failures: list[str] = []
    if good["status"] != "pass":
        failures.append(f"good packet should pass: {good['warnings']}")
    if missing["status"] != "warn" or (
        "Redactions performed" not in missing["empty_fields"] and "Redactions performed" not in missing["missing_fields"]
    ):
        failures.append("missing redaction packet should warn about Redactions performed")
    if sensitive["status"] != "warn" or not sensitive["sensitive_hits"]:
        failures.append("sensitive packet should warn about sensitive-looking terms")
    for result in (good, missing, sensitive):
        if result["mutates_files"] or result["submits_externally"] or not result["advisory_only"]:
            failures.append("review result changed boundary flags")

    return {"status": "pass" if not failures else "fail", "failures": failures}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Review or print a sanitized submitted evidence packet.")
    parser.add_argument("--template", action="store_true", help="Print the packet template to stdout.")
    parser.add_argument("--review", metavar="PACKET_FILE", help="Review a packet file locally.")
    parser.add_argument("--json", action="store_true", help="Print JSON output.")
    parser.add_argument("--self-test", action="store_true", help="Run deterministic self-tests.")
    args = parser.parse_args(argv)

    if args.self_test:
        result = self_test()
        print(json.dumps(result, indent=2, sort_keys=True))
        return 0 if result["status"] == "pass" else 1

    if args.template:
        if args.json:
            print(json.dumps({"template": PACKET_TEMPLATE, "mutates_files": False, "submits_externally": False}, indent=2))
        else:
            print(PACKET_TEMPLATE, end="")
        return 0

    if args.review:
        path = Path(args.review)
        text = path.read_text(encoding="utf-8")
        result = review_packet(text)
        if args.json:
            print(json.dumps(result, indent=2, sort_keys=True))
        else:
            print(render_plain(result), end="")
        return 0

    parser.print_help(sys.stderr)
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
