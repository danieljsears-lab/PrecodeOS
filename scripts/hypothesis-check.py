#!/usr/bin/env python3
# Version: v0.1.0
# Last updated: 2026-06-23
# Owner: PrecodeOS
# Created by Dan Sears / Recode.
# SPDX-License-Identifier: Apache-2.0
from __future__ import annotations

import argparse
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


REQUIRED_TERMS_BY_PATH = {
    "tasks/reference/PRODUCT-DISCOVERY-VALIDATION-PROTOCOL.md": [
        "## Hypothesis Mechanics",
        "HYPOTHESIS-REVIEW-PROTOCOL.md",
        "hunch",
        "assumption",
        "hypothesis",
        "experiment hypothesis",
        "Primary hypothesis / learning target",
        "Falsifier or what would change our mind",
        "Hypothesis review status",
        "not PRD approval",
        "task activation",
    ],
    "tasks/reference/HYPOTHESIS-REVIEW-PROTOCOL.md": [
        "Hypothesis Review / Learning Loop",
        "Discovery Summary",
        "Candidate Queue entry",
        "Local Source Intake summary",
        "PRD Source Inputs section",
        "Planning Brief",
        "untested",
        "tested",
        "narrowed",
        "killed",
        "promoted",
        "stale",
        "not applicable",
        "Learning outcome",
        "Stale or untested signals",
        "Recommended next Precode workflow",
        "Generated-report warning",
        "does not approve product direction",
        "rank candidates",
        "activate beads",
        "require analytics",
        "experiment database",
        "generated hypothesis status",
    ],
    "tasks/reference/CANDIDATE-QUEUE-PROTOCOL.md": [
        "Primary hypothesis / learning target",
        "Hypothesis review status",
        "Learning outcome",
        "Candidate Queue hypotheses are evidence",
        "do not approve PRDs",
        "rank work",
        "activate beads",
        "select tasks",
        "authorize implementation",
        "HYPOTHESIS-REVIEW-PROTOCOL.md",
    ],
    "CANDIDATE-QUEUE.md": [
        "Primary hypothesis / learning target",
        "Hypothesis review status",
        "Learning outcome",
        "Evidence strength",
        "Weakest assumption",
        "Promotion target",
    ],
    "tasks/reference/PLANNING-PROTOCOL.md": [
        "experiment hypothesis",
        "User or situation",
        "Expected behavior or change",
        "Supporting evidence",
        "Weakest assumption",
        "Falsifier or what would change our mind",
        "Learning Review",
        "Hypothesis review status",
        "does not approve a PRD",
        "activate beads",
    ],
    "tasks/reference/LOCAL-SOURCE-INTAKE-PROTOCOL.md": [
        "Primary hypothesis / learning target",
        "Hypothesis review status",
        "Learning outcome",
        "testable hypothesis",
        "Product Discovery Validation",
        "HYPOTHESIS-REVIEW-PROTOCOL.md",
    ],
    "tasks/reference/PRD-PROTOCOL.md": [
        "Primary hypothesis / learning target",
        "Hypothesis review status",
        "testable belief or learning question",
        "not PRD approval",
        "implementation permission",
    ],
    "tasks/prds/PRD-000-template.md": [
        "Primary hypothesis / learning target",
        "Hypothesis review status",
        "Learning outcome",
        "Discovery Evidence",
        "Source Inputs",
    ],
    "tasks/prds/PRD-022-hypothesis-review-learning-loop.md": [
        "Hypothesis Review And Learning Loop v2",
        "PRD-022-FR01",
        "PRD-022-FR06",
        "untested",
        "tested",
        "narrowed",
        "killed",
        "promoted",
        "stale",
        "not applicable",
        "does not approve product direction",
        "rank candidates",
        "require analytics",
        "experiment database",
        "generated hypothesis status",
    ],
    "tasks/reference/IDEA-TO-PRD-WORKFLOW.md": [
        "primary hypothesis or learning target",
        "Discovery Summary",
        "not PRD approval",
        "task activation",
    ],
    "tasks/reference/PROMPT-PATTERNS.md": [
        "Hypothesis Review / Learning Loop",
        "primary hypothesis or learning target",
        "Candidate Queue Review",
        "Add Candidate Queue Entry",
        "Do not write a PRD",
        "require analytics",
        "create a database",
    ],
    "tasks/templates/PRODUCT-IDEATION-WORKBOOK.md": [
        "primary hypothesis or learning target",
        "Conviction Packet",
        "Product Discovery Validation",
        "evidence only",
    ],
    "docs/PRECODE-USER-GUIDE.md": [
        "Review What A Hypothesis Taught You",
        "Hypothesis Review / Learning Loop",
        "primary hypothesis or learning target",
        "Product Discovery Interview Skill",
        "Do not write a PRD",
        "require analytics",
        "create a database",
    ],
    "docs/PRECODE-DAILY-COCKPIT.md": [
        "Hypothesis Review / Learning Loop",
        "Review hypothesis",
        "untested",
        "tested",
        "narrowed",
        "killed",
        "promoted",
        "stale",
        "not applicable",
        "create a database",
    ],
    "docs/HOW-TO-BUILD-SOFTWARE-WITH-PRECODE.md": [
        "primary hypothesis or learning target",
        "Discovery validation",
        "Do not write a PRD",
    ],
    "docs/PRECODE-PACKAGE-FILE-INVENTORY.md": [
        "scripts/hypothesis-check.py",
        "Hypothesis Guidance",
        "Hypothesis Review / Learning Loop",
        "HYPOTHESIS-REVIEW-PROTOCOL.md",
        "advisory",
    ],
}


def check_required_terms() -> list[dict[str, str]]:
    failures: list[dict[str, str]] = []
    for rel_path, required_terms in REQUIRED_TERMS_BY_PATH.items():
        path = ROOT / rel_path
        if not path.exists():
            failures.append({"path": rel_path, "expected": "file exists", "actual": "missing"})
            continue
        text = path.read_text(encoding="utf-8")
        for term in required_terms:
            if term not in text:
                failures.append({"path": rel_path, "expected": term, "actual": "missing"})
    return failures


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="check canonical Markdown hypothesis contracts without writing files")
    parser.parse_args()

    failures = check_required_terms()
    payload = {
        "tool": "hypothesis-check",
        "status": "pass" if not failures else "fail",
        "advisory_only": True,
        "details": {
            "checked_paths": sorted(REQUIRED_TERMS_BY_PATH),
            "contract": "canonical Markdown hypothesis guidance and review-loop coverage only",
            "does_not": [
                "judge product hypothesis quality",
                "parse generated HTML as authority",
                "rank Candidate Queue entries",
                "approve PRDs",
                "activate beads",
                "choose tasks",
                "require analytics",
                "create an experiment database",
                "make generated hypothesis status authoritative",
                "write files",
            ],
        },
        "failures": failures,
    }
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
