#!/usr/bin/env python3
# Version: v0.1.0
# Last updated: 2026-06-15
# Owner: PrecodeOS
# Created by Dan Sears / Recode.
# SPDX-License-Identifier: Apache-2.0
from __future__ import annotations

from typing import Any


SEVERITY_ORDER = {
    "clear": 0,
    "watch": 1,
    "drift_risk": 2,
    "recenter": 3,
    "stop_review": 4,
}

SEVERITY_LABELS = {
    "clear": "Clear",
    "watch": "Watch",
    "drift_risk": "Drift risk",
    "recenter": "Recenter",
    "stop_review": "Stop and review",
}

GENERATED_EVIDENCE_WARNING = (
    "Doctor Dashboard is generated diagnostic evidence only. It explains existing warning sources, "
    "but `scripts/next-step.py` owns the next human decision."
)

TRIAGE_LABELS = {
    "Next Step": "Current decision needs attention",
    "State Integrity": "Precode state may be confused",
    "Files In Play": "Changed files may be outside scope",
    "Adaptive Depth": "Planning depth may not match risk",
    "Run Contract": "Risk rules may be missing",
    "Completion And Handoff": "This may be a false-done moment",
    "Verification Quality": "Proof may be too weak",
    "Local Hygiene": "Cleanup needs classification first",
    "Work Graph": "Work relationships need inspection",
    "Tool Execution": "Tool history needs review",
    "Session Friction": "Repeated friction needs review",
}

DO_NOT_APPROVE_BY_SEVERITY = {
    "clear": "No approval warning from this row.",
    "watch": "Do not approve repair or transition from this row alone.",
    "drift_risk": "Do not approve broader scope until the owner warning is resolved.",
    "recenter": "Do not keep building until the owner state is repaired.",
    "stop_review": "Do not approve transition, acceptance, or mutation from health output.",
}


def _details(signal: dict[str, Any]) -> dict[str, Any]:
    return signal.get("details") if isinstance(signal.get("details"), dict) else {}


def _warnings(signal: dict[str, Any]) -> list[str]:
    warnings = signal.get("warnings") if isinstance(signal.get("warnings"), list) else []
    return [str(warning) for warning in warnings]


def _status(signal: dict[str, Any]) -> str:
    return str(signal.get("status") or "missing")


def _row(
    *,
    source: str,
    status: str,
    severity: str,
    why: str,
    owner_command: str,
    owner_protocol: str,
    repair_path: str,
    warnings: list[str] | None = None,
) -> dict[str, Any]:
    triage = _triage_fields(
        source=source,
        severity=severity,
        why=why,
        owner_command=owner_command,
        repair_path=repair_path,
    )
    return {
        "source": source,
        "status": status,
        "severity": severity,
        "severity_label": SEVERITY_LABELS.get(severity, severity),
        "why_it_matters": why,
        "owner_command": owner_command,
        "owner_protocol": owner_protocol,
        "shortest_repair_path": repair_path,
        "next_step_decision_owner": "scripts/next-step.py",
        "warnings": warnings or [],
        **triage,
    }


def _triage_fields(
    *,
    source: str,
    severity: str,
    why: str,
    owner_command: str,
    repair_path: str,
) -> dict[str, str]:
    issue = TRIAGE_LABELS.get(source, f"{source} needs review")
    if severity == "clear":
        issue = f"{source} looks clear"
    return {
        "plain_english_issue": issue,
        "user_facing_meaning": why,
        "safe_ask": (
            f"Ask the agent to inspect `{owner_command}` output and explain the safest next step without approving work."
        ),
        "do_not_approve": DO_NOT_APPROVE_BY_SEVERITY.get(severity, DO_NOT_APPROVE_BY_SEVERITY["watch"]),
        "shortest_validation_path": repair_path,
    }


def _warning_severity(signal: dict[str, Any], warning_severity: str = "watch") -> str:
    if _warnings(signal):
        return warning_severity
    status = _status(signal).lower()
    if status in {"fail", "error", "blocked"}:
        return "recenter"
    if status in {"warning", "warn"}:
        return warning_severity
    return "clear"


def _top_row(rows: list[dict[str, Any]]) -> dict[str, Any] | None:
    if not rows:
        return None
    return max(rows, key=lambda row: SEVERITY_ORDER.get(str(row.get("severity")), 0))


def _status_from_top(top: dict[str, Any] | None) -> str:
    if not top:
        return "clear"
    return str(top.get("severity") or "clear")


def _next_step_row(payload: dict[str, Any]) -> dict[str, Any]:
    signal = payload.get("next_step") or {}
    details = _details(signal)
    warnings = _warnings(signal)
    user_decision = str(details.get("user_decision") or "unknown")
    blockers = details.get("blockers") if isinstance(details.get("blockers"), list) else []
    if user_decision in {"approve transition", "review"} or details.get("needs_review") or details.get("needs_transition"):
        severity = "stop_review"
    elif user_decision in {"repair state", "stop"} or blockers:
        severity = "recenter"
    elif warnings or user_decision in {"ask for missing info", "ask for proof", "ask for reaffirmation", "approval needed"}:
        severity = "watch"
    else:
        severity = "clear"
    return _row(
        source="Next Step",
        status=user_decision,
        severity=severity,
        why="Names the current human decision without granting approval or task selection.",
        owner_command="python3 scripts/next-step.py",
        owner_protocol=str(details.get("single_next_protocol") or "scripts/next-step.py"),
        repair_path=str(details.get("recommended_action") or details.get("plain_english_summary") or "Review next-step guidance."),
        warnings=warnings[:3],
    )


def _state_integrity_row(payload: dict[str, Any]) -> dict[str, Any]:
    signal = payload.get("state_integrity") or {}
    details = _details(signal)
    warnings = _warnings(signal)
    severity = _warning_severity(signal, "recenter")
    return _row(
        source="State Integrity",
        status=_status(signal),
        severity=severity,
        why="Precode needs one coherent active bead and active-memory state before diagnostics are useful.",
        owner_command="python3 scripts/os-health.py",
        owner_protocol="tasks/reference/STATE-MANAGEMENT-PROTOCOL.md",
        repair_path=(
            "Repair active state before continuing."
            if severity != "clear"
            else f"In-progress beads: {', '.join(details.get('in_progress_beads') or []) or 'none'}."
        ),
        warnings=warnings[:3],
    )


def _files_in_play_row(payload: dict[str, Any]) -> dict[str, Any]:
    signal = payload.get("files_in_play_guardrail") or {}
    details = _details(signal)
    out_of_scope = details.get("out_of_scope_paths") if isinstance(details.get("out_of_scope_paths"), list) else []
    severity = "drift_risk" if out_of_scope else _warning_severity(signal, "watch")
    return _row(
        source="Files In Play",
        status=_status(signal),
        severity=severity,
        why="Changed files outside the active bead can turn one loop into hidden scope expansion.",
        owner_command="python3 scripts/files-in-play-check.py",
        owner_protocol="tasks/reference/TOOL-EXECUTION-PROTOCOL.md",
        repair_path=str(details.get("user_decision") or details.get("stop_if") or "Review changed paths against the active bead."),
        warnings=_warnings(signal)[:3],
    )


def _adaptive_depth_row(payload: dict[str, Any]) -> dict[str, Any]:
    signal = payload.get("bead_depth") or {}
    details = _details(signal)
    severity = _warning_severity(signal, "watch")
    return _row(
        source="Adaptive Depth",
        status=_status(signal),
        severity=severity,
        why="Planning depth should match risk so small work does not drown and risky work is not under-specified.",
        owner_command="python3 scripts/bead-depth-check.py",
        owner_protocol="tasks/reference/DECOMPOSITION-PROTOCOL.md",
        repair_path=str(details.get("shortest_next_action") or details.get("user_decision") or "Review bead depth metadata."),
        warnings=_warnings(signal)[:3],
    )


def _run_contract_row(payload: dict[str, Any]) -> dict[str, Any]:
    signal = payload.get("run_contract") or {}
    details = _details(signal)
    required = bool(details.get("required"))
    severity = _warning_severity(signal, "watch")
    return _row(
        source="Run Contract",
        status=_status(signal),
        severity=severity,
        why="Risky beads need explicit allowed actions, proof needed, approval gates, and stop conditions.",
        owner_command="python3 scripts/run-contract-check.py",
        owner_protocol="tasks/reference/RUN-CONTRACT-PROTOCOL.md",
        repair_path=(
            "Add or repair the active bead Run Contract."
            if required and severity != "clear"
            else "Use the generated run-contract profile only as evidence."
        ),
        warnings=_warnings(signal)[:3],
    )


def _completion_row(payload: dict[str, Any]) -> dict[str, Any]:
    signal = payload.get("completion_handoff") or {}
    details = _details(signal)
    promotion_status = str(details.get("promotion_status") or "")
    closeout_status = str(details.get("closeout_status") or "")
    if promotion_status == "eligible" or closeout_status == "complete":
        severity = "stop_review"
    else:
        severity = _warning_severity(signal, "watch")
    return _row(
        source="Completion And Handoff",
        status=_status(signal),
        severity=severity,
        why="Closeout, handoff, and transition-readiness signals are common false-done points.",
        owner_command="bash scripts/session-close.sh",
        owner_protocol="tasks/reference/SESSION-COMPLETION-HANDOFF-PROTOCOL.md",
        repair_path=str(details.get("next_safe_action") or "Review closeout evidence before continuing."),
        warnings=_warnings(signal)[:3],
    )


def _verification_row(payload: dict[str, Any]) -> dict[str, Any]:
    signal = payload.get("verification_quality") or {}
    details = _details(signal)
    severity = _warning_severity(signal, "watch")
    return _row(
        source="Verification Quality",
        status=_status(signal),
        severity=severity,
        why="Acceptance depends on recorded proof, not generated confidence.",
        owner_command="bash scripts/record-check.sh -- <command>",
        owner_protocol="tasks/reference/VERIFICATION-GUARDRAIL-PROTOCOL.md",
        repair_path="Run and record the declared checks before acceptance." if severity != "clear" else "Keep recording checks when proof is due.",
        warnings=_warnings(signal)[:3],
    )


def _local_hygiene_row(payload: dict[str, Any]) -> dict[str, Any]:
    signal = payload.get("local_hygiene") or {}
    details = _details(signal)
    severity = _warning_severity(signal, "watch")
    return _row(
        source="Local Hygiene",
        status=_status(signal),
        severity=severity,
        why="Local clutter, cache, and generated evidence can look alike unless classified before cleanup.",
        owner_command="python3 scripts/local-hygiene-check.py",
        owner_protocol="tasks/reference/LOCAL-HYGIENE-PROTOCOL.md",
        repair_path=str(details.get("next_safe_action") or "Review candidates only; do not delete from health output."),
        warnings=_warnings(signal)[:3],
    )


def _work_graph_row(payload: dict[str, Any]) -> dict[str, Any]:
    signal = payload.get("work_graph") or {}
    warnings = _warnings(signal)
    transition_warning = any(
        term in warning.lower()
        for warning in warnings
        for term in ("near closeout", "promotion", "review or done", "transition")
    )
    severity = "stop_review" if transition_warning else _warning_severity(signal, "watch")
    return _row(
        source="Work Graph",
        status=_status(signal),
        severity=severity,
        why="The graph makes bead, PRD, owner-file, check, blocker, and follow-up relationships inspectable.",
        owner_command="python3 scripts/os-health.py",
        owner_protocol="tasks/reference/INTENT-ORCHESTRATION-PROTOCOL.md",
        repair_path="Inspect `logs/work-graph.md` and repair owner files before treating graph warnings as resolved.",
        warnings=warnings[:3],
    )


def _tool_execution_row(payload: dict[str, Any]) -> dict[str, Any]:
    signal = payload.get("tool_execution") or {}
    details = _details(signal)
    approval_gaps = int(details.get("approval_gap_count") or 0)
    destructive = int(details.get("destructive_count") or 0)
    if destructive:
        severity = "stop_review"
    elif approval_gaps:
        severity = "drift_risk"
    else:
        severity = _warning_severity(signal, "watch")
    return _row(
        source="Tool Execution",
        status=_status(signal),
        severity=severity,
        why="Tool logs are audit history; they are not proof unless also recorded as checks.",
        owner_command="python3 scripts/tool-execution-check.py",
        owner_protocol="tasks/reference/TOOL-EXECUTION-PROTOCOL.md",
        repair_path="Resolve approval gaps or rerun important commands through recorded checks when they are proof.",
        warnings=_warnings(signal)[:3],
    )


def _session_friction_row(payload: dict[str, Any]) -> dict[str, Any]:
    signal = payload.get("session_friction_review") or {}
    details = _details(signal)
    findings = details.get("findings") if isinstance(details.get("findings"), list) else []
    actionable = [finding for finding in findings if finding.get("category") != "no_safe_evidence_found"]
    if _status(signal) == "pass":
        severity = "clear"
    elif len(actionable) >= 3:
        severity = "drift_risk"
    else:
        severity = "watch"
    return _row(
        source="Session Friction",
        status=_status(signal),
        severity=severity,
        why="Session-friction findings are cited review input; they are not memory promotion, task selection, or command approval.",
        owner_command="python3 scripts/session-friction-check.py",
        owner_protocol="tasks/reference/TOOL-EXECUTION-PROTOCOL.md",
        repair_path="Review cited findings, then manually choose whether a protocol note, command-pattern note, or reviewed memory candidate is warranted.",
        warnings=_warnings(signal)[:3],
    )


def build_doctor_dashboard(payload: dict[str, Any]) -> dict[str, Any]:
    rows = [
        _next_step_row(payload),
        _state_integrity_row(payload),
        _files_in_play_row(payload),
        _adaptive_depth_row(payload),
        _run_contract_row(payload),
        _completion_row(payload),
        _verification_row(payload),
        _local_hygiene_row(payload),
        _work_graph_row(payload),
        _tool_execution_row(payload),
        _session_friction_row(payload),
    ]
    top = _top_row(rows)
    return {
        "status": _status_from_top(top),
        "status_label": SEVERITY_LABELS.get(_status_from_top(top), _status_from_top(top)),
        "top_source": top.get("source") if top else "none",
        "top_repair_path": top.get("shortest_repair_path") if top else "No visible doctor action.",
        "top_plain_english_issue": top.get("plain_english_issue") if top else "No visible doctor issue.",
        "top_safe_ask": top.get("safe_ask") if top else "Ask the agent to refresh OS Health and explain any warnings.",
        "top_do_not_approve": top.get("do_not_approve") if top else DO_NOT_APPROVE_BY_SEVERITY["clear"],
        "top_validation_path": top.get("shortest_validation_path") if top else "No visible doctor action.",
        "next_step_decision_owner": "scripts/next-step.py",
        "advisory_only": True,
        "generated_evidence_warning": GENERATED_EVIDENCE_WARNING,
        "rows": rows,
    }


def _cell(value: Any) -> str:
    return str(value if value is not None else "missing").replace("|", "\\|").replace("\n", " ")


def render_doctor_dashboard_markdown(dashboard: dict[str, Any]) -> str:
    rows = dashboard.get("rows") if isinstance(dashboard.get("rows"), list) else []
    table = [
        "| Source | Severity | Plain-English issue | Safe ask | Do not approve |",
        "| --- | --- | --- | --- | --- |",
    ]
    for row in rows:
        table.append(
            "| "
            + " | ".join(
                [
                    _cell(row.get("source")),
                    _cell(row.get("severity_label")),
                    _cell(row.get("plain_english_issue")),
                    _cell(row.get("safe_ask")),
                    _cell(row.get("do_not_approve")),
                ]
            )
            + " |"
        )
    return "\n".join(
        [
            f"- Status: {dashboard.get('status_label', 'missing')}",
            f"- Top source: {dashboard.get('top_source', 'none')}",
            f"- Plain-English issue: {dashboard.get('top_plain_english_issue', 'No visible doctor issue.')}",
            f"- Safe ask: {dashboard.get('top_safe_ask', 'Ask the agent to refresh OS Health and explain any warnings.')}",
            f"- Do not approve: {dashboard.get('top_do_not_approve', DO_NOT_APPROVE_BY_SEVERITY['clear'])}",
            f"- Shortest validation path: {dashboard.get('top_validation_path', dashboard.get('top_repair_path', 'No visible doctor action.'))}",
            f"- Next decision owner: `{dashboard.get('next_step_decision_owner', 'scripts/next-step.py')}`",
            f"- Advisory only: {dashboard.get('advisory_only', True)}",
            f"- Generated-evidence warning: {dashboard.get('generated_evidence_warning', GENERATED_EVIDENCE_WARNING)}",
            "",
            "\n".join(table) if rows else "- No doctor dashboard rows found.",
        ]
    )
