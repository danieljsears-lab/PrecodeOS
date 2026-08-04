#!/usr/bin/env python3
# Version: v0.1.0
# Last updated: 2026-08-04
# Owner: PrecodeOS
# Created by Dan Sears / Recode.
# SPDX-License-Identifier: Apache-2.0
from __future__ import annotations

import argparse
from collections import Counter
from datetime import datetime, timezone
import json
from pathlib import Path
from typing import Any

from os_compiler import compile_state, repo_root, session_friction_review
from precode_state import load_jsonl


USAGE_EVIDENCE_FORBIDDEN_USES = [
    "adoption proof",
    "product validation",
    "task selection",
    "PRD approval",
    "bead activation",
    "implementation acceptance",
    "review acceptance",
    "release approval",
    "support record creation",
    "contributor scoring",
    "productivity ranking",
    "external submission",
    "telemetry authorization",
    "package-manager behavior",
]

SOURCE_LEDGER_PATHS = {
    "tool_runs": "logs/tool-runs.jsonl",
    "check_results": "logs/check-results.jsonl",
    "loop_runs": "logs/loop-runs.jsonl",
    "agent_spend": "logs/agent-spend.jsonl",
}

GENERATED_FRESHNESS_PATHS = [
    "OS-HEALTH.md",
    "PROGRESS.md",
    "logs/learning-diary.md",
    "logs/memory-index.md",
    "logs/scheduled-audit.md",
    "logs/scheduled-audit.json",
    "logs/session-friction-review.json",
]


def iso_mtime(path: Path) -> str:
    if not path.exists():
        return "missing"
    return datetime.fromtimestamp(path.stat().st_mtime, tz=timezone.utc).isoformat()


def safe_ref(value: object, *, limit: int = 120) -> str:
    text = " ".join(str(value or "").split())
    if len(text) <= limit:
        return text
    return text[: limit - 3] + "..."


def safe_refs(values: list[Any]) -> list[str]:
    return [safe_ref(value) for value in values[:8]]


def status_counts(rows: list[dict[str, Any]]) -> dict[str, int]:
    return dict(sorted(Counter(str(row.get("status") or "unknown").lower() for row in rows).items()))


def class_counts(rows: list[dict[str, Any]]) -> dict[str, int]:
    return dict(sorted(Counter(str(row.get("class") or "unknown").lower() for row in rows).items()))


def failure_category_counts(rows: list[dict[str, Any]]) -> dict[str, int]:
    failed = [
        row
        for row in rows
        if str(row.get("status") or "").lower() in {"fail", "failed", "blocked"}
    ]
    return dict(sorted(Counter(str(row.get("failure_category") or "missing").lower() for row in failed).items()))


def latest_timestamp(rows: list[dict[str, Any]]) -> str:
    timestamps = sorted(str(row.get("timestamp") or "") for row in rows if row.get("timestamp"))
    return timestamps[-1] if timestamps else "unknown"


def source_summary(root: Path, rows_by_name: dict[str, list[dict[str, Any]]]) -> dict[str, Any]:
    summary: dict[str, Any] = {}
    for name, rel in SOURCE_LEDGER_PATHS.items():
        path = root / rel
        rows = rows_by_name.get(name) or []
        summary[name] = {
            "path": rel,
            "present": path.exists(),
            "row_count": len(rows),
            "latest_timestamp": latest_timestamp(rows),
        }
    return summary


def generated_freshness(root: Path) -> dict[str, dict[str, str | bool]]:
    return {
        rel: {"present": (root / rel).exists(), "modified_at": iso_mtime(root / rel)}
        for rel in GENERATED_FRESHNESS_PATHS
    }


def spend_presence(rows: list[dict[str, Any]], state: dict[str, Any]) -> dict[str, Any]:
    spend = state.get("spend") if isinstance(state.get("spend"), dict) else {}
    return {
        "present": bool(rows),
        "row_count": len(rows),
        "latest_timestamp": latest_timestamp(rows),
        "known_summary_available": bool(spend),
        "unknown_token_entries": spend.get("unknown_token_entries", "unknown"),
        "unknown_cost_entries": spend.get("unknown_cost_entries", "unknown"),
    }


def build_findings(
    root: Path,
    rows_by_name: dict[str, list[dict[str, Any]]],
    state: dict[str, Any],
    friction: dict[str, Any],
) -> list[dict[str, Any]]:
    findings: list[dict[str, Any]] = []
    tool_rows = rows_by_name["tool_runs"]
    check_rows = rows_by_name["check_results"]
    loop_rows = rows_by_name["loop_runs"]
    spend_rows = rows_by_name["agent_spend"]

    missing_ledgers = [rel for rel in SOURCE_LEDGER_PATHS.values() if not (root / rel).exists()]
    if missing_ledgers:
        findings.append(
            {
                "category": "missing_safe_local_ledgers",
                "summary": "One or more safe local evidence ledgers are absent; absence is unknown, not zero usage.",
                "source_refs": missing_ledgers,
                "confidence": "high",
                "freshness": "unknown",
                "recommended_destination": "human support or maintainer review",
                "suggested_next_step": "Do not infer usage or adoption from absent local ledgers; inspect the project history or ask the user if evidence matters.",
            }
        )

    if not tool_rows:
        findings.append(
            {
                "category": "tool_use_unknown",
                "summary": "No local tool-run rows were available for usage-evidence review.",
                "source_refs": ["logs/tool-runs.jsonl"],
                "confidence": "medium",
                "freshness": "unknown",
                "recommended_destination": "none unless tool-use friction is being investigated",
                "suggested_next_step": "Treat tool-use signals as unknown rather than as no tool friction.",
            }
        )

    failed_or_blocked = [
        row
        for row in tool_rows
        if str(row.get("status") or "").lower() in {"fail", "failed", "blocked"}
    ]
    if failed_or_blocked:
        findings.append(
            {
                "category": "tool_friction_present",
                "summary": f"{len(failed_or_blocked)} failed or blocked tool runs are present in the local ledger.",
                "source_refs": [
                    f"logs/tool-runs.jsonl:{row.get('timestamp') or 'unknown'}:{safe_ref(row.get('tool') or row.get('command'), limit=72)}"
                    for row in failed_or_blocked[:8]
                ],
                "confidence": "medium",
                "freshness": latest_timestamp(failed_or_blocked),
                "recommended_destination": "Session Friction Review or Tool Execution Protocol follow-up",
                "suggested_next_step": "Run or inspect Session Friction Review before promoting a repeated command lesson.",
            }
        )

    if not check_rows:
        findings.append(
            {
                "category": "check_freshness_unknown",
                "summary": "No local check-result rows were available for usage-evidence review.",
                "source_refs": ["logs/check-results.jsonl"],
                "confidence": "medium",
                "freshness": "unknown",
                "recommended_destination": "completion or verification review",
                "suggested_next_step": "Do not treat missing checks as passing checks; record relevant validation if proof matters.",
            }
        )

    if not loop_rows:
        findings.append(
            {
                "category": "workflow_moments_unknown",
                "summary": "No local loop-run rows were available to infer workflow moments used.",
                "source_refs": ["logs/loop-runs.jsonl"],
                "confidence": "low",
                "freshness": "unknown",
                "recommended_destination": "none unless workflow usage is being investigated",
                "suggested_next_step": "Ask the user or inspect approved artifacts before claiming which workflow moments were used.",
            }
        )

    if not spend_rows:
        findings.append(
            {
                "category": "spend_import_unknown",
                "summary": "No local agent-spend rows were available; token or cost evidence is unknown.",
                "source_refs": ["logs/agent-spend.jsonl"],
                "confidence": "medium",
                "freshness": "unknown",
                "recommended_destination": "Scheduled Audit or spend telemetry dry-run review",
                "suggested_next_step": "Do not infer cost or usage intensity from missing spend rows.",
            }
        )

    if not (root / "logs" / "scheduled-audit.md").exists() and not (root / "logs" / "scheduled-audit.json").exists():
        findings.append(
            {
                "category": "scheduled_audit_unknown",
                "summary": "No scheduled-audit generated output was found.",
                "source_refs": ["logs/scheduled-audit.md", "logs/scheduled-audit.json"],
                "confidence": "low",
                "freshness": "unknown",
                "recommended_destination": "Scheduled Audit Protocol review only if recurring audit evidence is needed",
                "suggested_next_step": "Do not infer recurring use or non-use from missing scheduled-audit output.",
            }
        )

    friction_findings = (friction.get("details") or {}).get("findings") if isinstance(friction.get("details"), dict) else []
    actionable_friction = [
        finding
        for finding in (friction_findings or [])
        if finding.get("category") != "no_safe_evidence_found"
    ]
    if actionable_friction:
        findings.append(
            {
                "category": "session_friction_findings_present",
                "summary": f"{len(actionable_friction)} Session Friction Review findings are available as local evidence.",
                "source_refs": safe_refs(
                    [
                        ref
                        for finding in actionable_friction
                        for ref in (finding.get("source_refs") or [])
                    ]
                ),
                "confidence": "medium",
                "freshness": friction.get("status", "unknown"),
                "recommended_destination": "Session Friction Review human promotion path",
                "suggested_next_step": "Inspect Session Friction Review findings before promoting any protocol, memory, or support change.",
            }
        )

    if not findings:
        findings.append(
            {
                "category": "no_actionable_safe_usage_evidence",
                "summary": "No actionable safe local usage-evidence findings were found.",
                "source_refs": list(SOURCE_LEDGER_PATHS.values()),
                "confidence": "low",
                "freshness": "unknown",
                "recommended_destination": "none",
                "suggested_next_step": "Do not create roadmap, support, or protocol follow-up work without cited evidence.",
            }
        )

    for finding in findings:
        finding["forbidden_uses"] = USAGE_EVIDENCE_FORBIDDEN_USES
    return findings


def build_payload_from_inputs(
    root: Path,
    rows_by_name: dict[str, list[dict[str, Any]]],
    state: dict[str, Any],
    friction: dict[str, Any],
) -> dict[str, Any]:
    source_counts = source_summary(root, rows_by_name)
    findings = build_findings(root, rows_by_name, state, friction)
    unknowns = [
        f"{name} missing or empty"
        for name, details in source_counts.items()
        if not details["present"] or details["row_count"] == 0
    ]
    if not friction.get("details"):
        unknowns.append("session friction review unavailable")
    if not (root / "logs" / "scheduled-audit.md").exists() and not (root / "logs" / "scheduled-audit.json").exists():
        unknowns.append("scheduled audit output missing")

    return {
        "tool": "usage-evidence-review",
        "status": "warning" if any(f["category"] != "no_actionable_safe_usage_evidence" for f in findings) else "pass",
        "advisory_only": True,
        "read_only": True,
        "mutates_files": False,
        "writes_generated_report": False,
        "submits_externally": False,
        "network_calls": False,
        "evidence_only": True,
        "owner_prd": "tasks/prds/PRD-048-precode-usage-evidence-review.md",
        "owner_protocols": [
            "tasks/reference/TOOL-EXECUTION-PROTOCOL.md",
            "tasks/reference/EXTENSION-PROTOCOL.md",
            "tasks/reference/SCHEDULED-AUDIT-PROTOCOL.md",
        ],
        "source_counts": source_counts,
        "workflow_signals": {
            "loop_events": len(rows_by_name["loop_runs"]),
            "latest_loop_timestamp": latest_timestamp(rows_by_name["loop_runs"]),
            "loop_actions": dict(sorted(Counter(str(row.get("action") or "unknown") for row in rows_by_name["loop_runs"]).items())),
        },
        "tool_run_signals": {
            "tool_runs": len(rows_by_name["tool_runs"]),
            "status_counts": status_counts(rows_by_name["tool_runs"]),
            "class_counts": class_counts(rows_by_name["tool_runs"]),
            "failure_category_counts": failure_category_counts(rows_by_name["tool_runs"]),
        },
        "check_freshness_signals": {
            "check_results": len(rows_by_name["check_results"]),
            "latest_check_timestamp": latest_timestamp(rows_by_name["check_results"]),
            "status_counts": status_counts(rows_by_name["check_results"]),
        },
        "spend_import_presence": spend_presence(rows_by_name["agent_spend"], state),
        "generated_freshness": generated_freshness(root),
        "session_friction_review": {
            "status": friction.get("status", "unknown"),
            "finding_categories": [
                finding.get("category")
                for finding in ((friction.get("details") or {}).get("findings") or [])
                if isinstance(finding, dict)
            ],
            "warnings": friction.get("warnings") or [],
        },
        "unknown_because_not_logged": unknowns,
        "findings": findings,
        "boundary": (
            "Local Usage Evidence Review is opt-in generated evidence only. It does not collect telemetry, "
            "write reports, submit evidence, create issues, store identity, prove adoption, choose roadmap work, "
            "approve PRDs or beads, accept implementation, approve release, or mutate external systems."
        ),
    }


def build_payload(root: Path) -> dict[str, Any]:
    rows_by_name = {
        "tool_runs": load_jsonl(root / "logs" / "tool-runs.jsonl"),
        "check_results": load_jsonl(root / "logs" / "check-results.jsonl"),
        "loop_runs": load_jsonl(root / "logs" / "loop-runs.jsonl"),
        "agent_spend": load_jsonl(root / "logs" / "agent-spend.jsonl"),
    }
    state = compile_state(root)
    friction = session_friction_review(
        root,
        rows_by_name["tool_runs"],
        rows_by_name["check_results"],
        rows_by_name["loop_runs"],
        state.get("tool_execution") or {},
        state.get("completion_handoff") or {},
        state.get("memory") or {},
    )
    return build_payload_from_inputs(root, rows_by_name, state, friction)


def render_plain(payload: dict[str, Any]) -> str:
    lines = [
        "Local Opt-In Usage Evidence Review",
        f"Status: {payload['status']}",
        "Boundary: opt-in, read-only, local generated evidence only; no telemetry collection or submission.",
        "",
        "Sources:",
    ]
    for name, details in payload["source_counts"].items():
        present = "present" if details["present"] else "missing"
        lines.append(f"- {name}: {present}, rows={details['row_count']}, latest={details['latest_timestamp']}")

    lines.extend(["", "Signals:"])
    lines.append(f"- tool runs: {payload['tool_run_signals']['tool_runs']} {payload['tool_run_signals']['status_counts']}")
    lines.append(f"- check results: {payload['check_freshness_signals']['check_results']} {payload['check_freshness_signals']['status_counts']}")
    lines.append(f"- loop events: {payload['workflow_signals']['loop_events']}")
    spend = payload["spend_import_presence"]
    lines.append(f"- spend import: rows={spend['row_count']}, unknown_tokens={spend['unknown_token_entries']}, unknown_costs={spend['unknown_cost_entries']}")

    unknowns = payload.get("unknown_because_not_logged") or []
    if unknowns:
        lines.extend(["", "Unknown Because Not Logged:"])
        lines.extend(f"- {unknown}" for unknown in unknowns)

    lines.extend(["", "Findings:"])
    for finding in payload["findings"]:
        lines.append(f"- {finding['category']}: {finding['summary']}")
        lines.append(f"  Destination: {finding['recommended_destination']}")
        lines.append(f"  Next: {finding['suggested_next_step']}")

    lines.extend(["", str(payload["boundary"])])
    return "\n".join(lines) + "\n"


def self_test() -> dict[str, Any]:
    root = repo_root()
    rows_by_name = {
        "tool_runs": [
            {
                "timestamp": "2026-08-04T10:00:00+00:00",
                "tool": "shell",
                "class": "read_only",
                "status": "blocked",
                "failure_category": "permission_or_sandbox_blocked",
                "command": "very long command that should not become an authority surface or raw command excerpt",
            }
        ],
        "check_results": [{"timestamp": "2026-08-04T10:02:00+00:00", "status": "pass", "command": "python3 scripts/example.py"}],
        "loop_runs": [{"timestamp": "2026-08-04T10:03:00+00:00", "action": "session-start"}],
        "agent_spend": [],
    }
    state = {"spend": {"unknown_token_entries": 1, "unknown_cost_entries": 1}}
    friction = {
        "status": "warning",
        "warnings": [],
        "details": {
            "findings": [
                {
                    "category": "sandbox_or_approval_block",
                    "source_refs": ["logs/tool-runs.jsonl:2026-08-04T10:00:00+00:00:very long command"],
                }
            ]
        },
    }
    payload = build_payload_from_inputs(root, rows_by_name, state, friction)
    failures: list[str] = []
    if not payload["read_only"] or payload["mutates_files"] or payload["submits_externally"] or payload["network_calls"]:
        failures.append("boundary flags must stay read-only/no-submit/no-network")
    if "spend_import_unknown" not in {finding["category"] for finding in payload["findings"]}:
        failures.append("missing spend rows should be explicit unknown evidence")
    if "session_friction_findings_present" not in {finding["category"] for finding in payload["findings"]}:
        failures.append("session friction findings should be surfaced")
    plain = render_plain(payload)
    if "telemetry collection or submission" not in plain:
        failures.append("plain output must state no telemetry collection or submission")
    if "adoption proof" not in " ".join(payload["findings"][0]["forbidden_uses"]):
        failures.append("findings must carry forbidden uses")
    return {"tool": "usage-evidence-review", "mode": "self-test", "status": "pass" if not failures else "fail", "failures": failures}


def main() -> int:
    parser = argparse.ArgumentParser(description="Show read-only Local Opt-In Usage Evidence Review findings.")
    parser.add_argument("--json", action="store_true", help="Print JSON output.")
    parser.add_argument("--self-test", action="store_true", help="Run deterministic self-tests.")
    args = parser.parse_args()

    if args.self_test:
        result = self_test()
        print(json.dumps(result, indent=2, sort_keys=True))
        return 0 if result.get("status") == "pass" else 1

    payload = build_payload(repo_root())
    if args.json:
        print(json.dumps(payload, indent=2, sort_keys=True))
    else:
        print(render_plain(payload), end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
