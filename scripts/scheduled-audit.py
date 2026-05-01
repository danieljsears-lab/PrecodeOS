#!/usr/bin/env python3
# Version: v0.1.2
# Last updated: 2026-04-27
# Owner: Precode OS
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import json
from pathlib import Path
import shutil
import subprocess
from typing import Any

from os_compiler import compile_state, load_jsonl, read_bead, repo_root, write_json


AUDIT_JSON = "logs/scheduled-audit.json"
AUDIT_MD = "logs/scheduled-audit.md"
MISSING = {"", "missing", "not recorded", "not reviewed", "not evaluated", "pending", "blocked"}
APPROVED = {"accepted", "approved", "approve"}


def run_read_only(args: list[str], root: Path) -> tuple[int, str]:
    try:
        result = subprocess.run(args, cwd=root, check=False, capture_output=True, text=True, timeout=15)
    except (OSError, subprocess.TimeoutExpired) as exc:
        return 1, str(exc)
    return result.returncode, (result.stdout or result.stderr).strip()


def status(name: str, state: str, summary: str, details: dict[str, Any] | None = None) -> dict[str, Any]:
    return {"name": name, "status": state, "summary": summary, "details": details or {}}


def is_missing(value: str | None) -> bool:
    return (value or "").strip().lower() in MISSING


def is_accepted(value: str | None) -> bool:
    return (value or "").strip().lower() in APPROVED


def generated_demotion(root: Path) -> dict[str, Any]:
    required_paths = ["PROGRESS.md", "OS-HEALTH.md", "logs/learning-diary.md", "logs/memory-index.md", "logs/scheduled-audit.md"]
    optional_paths = ["logs/github-source-intake.md"]
    results: list[dict[str, Any]] = []
    warnings: list[str] = []
    for rel in required_paths + [path for path in optional_paths if (root / path).is_file()]:
        path = root / rel
        if not path.is_file():
            results.append({"path": rel, "status": "missing"})
            warnings.append(f"{rel} is missing")
            continue
        text = path.read_text(encoding="utf-8")
        ok = "> CLASS: generated" in text and "Do not use this file" in text
        results.append({"path": rel, "status": "pass" if ok else "warning"})
        if not ok:
            warnings.append(f"{rel} does not clearly demote itself as generated output")
    return {"results": results, "warnings": warnings}


def local_audits(root: Path, payload: dict[str, Any], args: argparse.Namespace) -> tuple[list[dict[str, Any]], list[str]]:
    warnings: list[str] = []
    audits: list[dict[str, Any]] = []

    audits.append(
        status(
            "Health Refresh Audit",
            "pass" if args.health_exit == 0 else "fail",
            "OS health refresh completed" if args.health_exit == 0 else "OS health refresh failed",
        )
    )

    audits.append(
        status(
            "Memory Validation Audit",
            "pass" if args.validate_exit == 0 else "fail",
            f"`bash scripts/validate-memory.sh` exited {args.validate_exit}",
            {"output": args.validate_output},
        )
    )
    if args.validate_exit != 0:
        warnings.append("memory validation failed")

    audits.append(
        status(
            "Learning Diary Refresh Audit",
            "pass" if args.diary_exit == 0 else "fail",
            "learning diary refreshed without appending a fake session" if args.diary_exit == 0 else "learning diary refresh failed",
        )
    )

    spend_rows = load_jsonl(root / "logs" / "agent-spend.jsonl")
    spend = payload["loop_metrics"]["spend"]
    audits.append(
        status(
            "Spend Telemetry Audit",
            "pass" if args.spend_exit == 0 else "warning",
            f"{len(spend_rows)} spend entr{'y' if len(spend_rows) == 1 else 'ies'}; known tokens {spend.get('total_tokens', 0)}; known spend ${float(spend.get('known_cost_usd', 0.0)):.4f}",
            {"dry_run_output": args.spend_output, "unknown_token_entries": spend.get("unknown_token_entries", 0), "unknown_cost_entries": spend.get("unknown_cost_entries", 0)},
        )
    )

    current_rel = payload.get("current_bead")
    current_path = root / str(current_rel or "")
    current_bead = read_bead(current_path, root) if current_rel and current_path.is_file() else None
    check_rows = [row for row in load_jsonl(root / "logs" / "check-results.jsonl") if row.get("bead") == current_rel]
    loop_rows = [row for row in load_jsonl(root / "logs" / "loop-runs.jsonl") if row.get("bead") == current_rel]

    if current_bead and current_bead.status == "in_progress" and not check_rows and not loop_rows:
        warnings.append(f"{current_rel} is in_progress with no recorded checks or loop events")
        stale_state = "warning"
        stale_summary = "active bead has no recorded checks or loop events"
    else:
        stale_state = "pass"
        stale_summary = "active bead has recorded evidence or is not stale by first-pass criteria"
    audits.append(status("Stale Bead Audit", stale_state, stale_summary))

    closeout_warnings: list[str] = []
    if current_bead:
        if not check_rows:
            closeout_warnings.append("no recorded checks for active bead")
        if is_missing(current_bead.closeout.get("manual_verification")):
            closeout_warnings.append("manual verification is missing")
        if not is_accepted(current_bead.closeout.get("review_decision")):
            closeout_warnings.append("review decision is not accepted")
        if is_missing(current_bead.closeout.get("next_bead")):
            closeout_warnings.append("next bead safety is not evaluated")
        blocked_escape = current_bead.closeout.get("blocked_escape")
        if current_bead.status in {"needs_info", "manual_testing"} and is_missing(blocked_escape):
            closeout_warnings.append("blocked bead lacks clear escape path")
    else:
        closeout_warnings.append("current bead is missing")
    warnings.extend(closeout_warnings)
    audits.append(status("Closeout Completeness Audit", "warning" if closeout_warnings else "pass", "; ".join(closeout_warnings) if closeout_warnings else "closeout has no first-pass warnings"))

    demotion = generated_demotion(root)
    warnings.extend(demotion["warnings"])
    audits.append(status("Generated Reports Demotion Audit", "warning" if demotion["warnings"] else "pass", "generated reports are demoted" if not demotion["warnings"] else "; ".join(demotion["warnings"]), {"files": demotion["results"]}))

    blocked = [bead for bead in payload.get("beads", []) if bead.get("status") in {"needs_info", "manual_testing"}]
    audits.append(status("Blocked Work Audit", "warning" if blocked else "pass", f"{len(blocked)} blocked bead(s)" if blocked else "no blocked beads found", {"beads": blocked}))

    verification = payload.get("verification_quality") or {}
    verification_warnings = [str(item) for item in verification.get("warnings") or []]
    warnings.extend(verification_warnings)
    audits.append(
        status(
            "Verification Quality Audit",
            "warning" if verification_warnings else "pass",
            "; ".join(verification_warnings) if verification_warnings else "no first-pass verification quality warnings",
            verification.get("details") if isinstance(verification.get("details"), dict) else {},
        )
    )

    decomposition = payload.get("decomposition_quality") or {}
    decomposition_warnings = [str(item) for item in decomposition.get("warnings") or []]
    warnings.extend(decomposition_warnings)
    audits.append(
        status(
            "Decomposition Quality Audit",
            "warning" if decomposition_warnings else "pass",
            "; ".join(decomposition_warnings) if decomposition_warnings else "no first-pass decomposition warnings",
            decomposition.get("details") if isinstance(decomposition.get("details"), dict) else {},
        )
    )

    integrity = payload.get("state_integrity") or {}
    integrity_warnings = [str(item) for item in integrity.get("warnings") or []]
    warnings.extend(integrity_warnings)
    audits.append(
        status(
            "State Integrity Audit",
            "warning" if integrity_warnings else "pass",
            "; ".join(integrity_warnings) if integrity_warnings else "no first-pass state integrity warnings",
            integrity.get("details") if isinstance(integrity.get("details"), dict) else {},
        )
    )

    intent = payload.get("intent_orchestration") or {}
    intent_warnings = [str(item) for item in intent.get("warnings") or []]
    warnings.extend(intent_warnings)
    audits.append(
        status(
            "Intent Orchestration Audit",
            "warning" if intent_warnings else "pass",
            "; ".join(intent_warnings) if intent_warnings else "no first-pass intent orchestration warnings",
            intent.get("details") if isinstance(intent.get("details"), dict) else {},
        )
    )

    tool_execution = payload.get("tool_execution") or {}
    tool_warnings = [str(item) for item in tool_execution.get("warnings") or []]
    warnings.extend(tool_warnings)
    audits.append(
        status(
            "Tool Execution Audit",
            "warning" if tool_warnings else "pass",
            "; ".join(tool_warnings) if tool_warnings else "no first-pass tool execution warnings",
            tool_execution.get("details") if isinstance(tool_execution.get("details"), dict) else {},
        )
    )

    workflow = payload.get("workflow_planning") or {}
    workflow_warnings = [str(item) for item in workflow.get("warnings") or []]
    warnings.extend(workflow_warnings)
    audits.append(
        status(
            "Workflow Planning Audit",
            "warning" if workflow_warnings else "pass",
            "; ".join(workflow_warnings) if workflow_warnings else "no first-pass workflow planning warnings",
            workflow.get("details") if isinstance(workflow.get("details"), dict) else {},
        )
    )

    long_horizon = payload.get("long_horizon_planning") or {}
    long_horizon_warnings = [str(item) for item in long_horizon.get("warnings") or []]
    warnings.extend(long_horizon_warnings)
    audits.append(
        status(
            "Long-Horizon Planning Audit",
            "warning" if long_horizon_warnings else "pass",
            "; ".join(long_horizon_warnings) if long_horizon_warnings else "no first-pass long-horizon planning warnings",
            long_horizon.get("details") if isinstance(long_horizon.get("details"), dict) else {},
        )
    )

    completion = payload.get("completion_handoff") or {}
    completion_warnings = [str(item) for item in completion.get("warnings") or []]
    warnings.extend(completion_warnings)
    audits.append(
        status(
            "Completion And Handoff Audit",
            "warning" if completion_warnings else "pass",
            "; ".join(completion_warnings) if completion_warnings else "no first-pass completion or handoff warnings",
            completion.get("details") if isinstance(completion.get("details"), dict) else {},
        )
    )

    pattern = payload.get("pattern_guidance") or {}
    pattern_warnings = [str(item) for item in pattern.get("warnings") or []]
    warnings.extend(pattern_warnings)
    audits.append(
        status(
            "System Design Pattern Audit",
            "warning" if pattern_warnings else "pass",
            "; ".join(pattern_warnings) if pattern_warnings else "no first-pass system design pattern warnings",
            pattern.get("details") if isinstance(pattern.get("details"), dict) else {},
        )
    )

    memory = payload.get("memory") or {}
    memory_warnings = [str(item) for item in memory.get("warnings") or []]
    warnings.extend(memory_warnings)
    memory_details = memory.get("details") if isinstance(memory.get("details"), dict) else {}
    audits.append(
        status(
            "Filesystem Memory Audit",
            "warning" if memory_warnings else "pass",
            "; ".join(memory_warnings) if memory_warnings else f"{memory_details.get('card_count', 0)} reviewed memory card(s); generated index remains evidence only",
            memory_details,
        )
    )

    file_inventory = payload.get("file_inventory") or {}
    file_inventory_warnings = [str(item) for item in file_inventory.get("warnings") or []]
    warnings.extend(file_inventory_warnings)
    file_inventory_counts = file_inventory.get("counts") if isinstance(file_inventory.get("counts"), dict) else {}
    audits.append(
        status(
            "File Inventory Audit",
            "warning" if file_inventory_warnings else "pass",
            "; ".join(file_inventory_warnings[:6])
            if file_inventory_warnings
            else f"{file_inventory_counts.get('docs', 0)} docs, {file_inventory_counts.get('scripts', 0)} scripts, and {file_inventory_counts.get('generated_outputs', 0)} generated outputs inventoried",
            file_inventory_counts,
        )
    )

    return audits, warnings


def read_github_audit(root: Path, rel_path: str, exit_code: int) -> list[dict[str, Any]]:
    path = root / rel_path
    if exit_code != 0:
        return [status("GitHub Repository Audit", "warning", f"`scripts/github-audit.py` exited {exit_code}", {"output": rel_path})]
    if not path.is_file():
        return [status("GitHub Repository Audit", "not_configured", "GitHub audit output is missing", {"output": rel_path})]
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        return [status("GitHub Repository Audit", "warning", f"GitHub audit output was not valid JSON: {exc}", {"output": rel_path})]

    audits = payload.get("audits")
    if isinstance(audits, list):
        normalized = []
        for audit in audits:
            if isinstance(audit, dict):
                normalized.append(
                    status(
                        str(audit.get("name") or "GitHub Audit"),
                        str(audit.get("status") or "info"),
                        str(audit.get("summary") or "GitHub audit returned status"),
                        dict(audit.get("details") or {}),
                    )
                )
        if normalized:
            return normalized
    return [status("GitHub Repository Audit", "info", "GitHub audit completed with no detailed audit rows", {"output": rel_path})]


def external_audits(root: Path, args: argparse.Namespace) -> list[dict[str, Any]]:
    audits: list[dict[str, Any]] = []
    audits.extend(read_github_audit(root, args.github_output, args.github_exit))

    audits.append(status("Deployment Status Audit", "not_configured", "no deployment provider audit configured"))
    audits.append(status("Issue Tracker Audit", "not_configured", "no issue tracker audit configured"))
    audits.append(status("Dependency/Security Advisory Audit", "not_configured", "no read-only dependency or advisory source configured"))
    audits.append(status("Error Monitoring / Observability Audit", "not_configured", "no monitoring provider audit configured"))
    audits.append(status("Uptime / Endpoint Audit", "not_configured", "no safe health URL configured"))
    audits.append(status("External Dashboard Setup Audit", "not_configured", "manual dashboard setup status should be documented in PROJECT-CONTEXT.md when needed"))
    return audits


def render_markdown(payload: dict[str, Any]) -> str:
    def render_items(items: list[dict[str, Any]]) -> str:
        lines: list[str] = []
        for item in items:
            lines.append(f"- **{item['name']}**: `{item['status']}` - {item['summary']}")
        return "\n".join(lines) if lines else "- None"

    warnings = payload["warnings"]
    prompts = payload["human_review_prompts"]

    return f"""# Precode OS -- Scheduled Audit
<!-- ANCHOR: scheduled-audit -->

> AUTHORITY: Generated scheduled audit snapshot for Precode OS local and external status checks.
> NOT_AUTHORITY: Active memory, task selection, product decisions, implementation plans, bead state, external system mutation, or generated progress state.
> LOAD_WHEN: Reviewing scheduled audit findings; never as active session memory.
> CLASS: generated
>
> Generated from `scripts/scheduled-audit.py`.
> Do not use this file as active memory or as a task plan.

Generated at: `{payload['generated_at']}`

## Reading Rule

This audit is evidence only. A user must promote findings into the correct Precode owner file or approve a follow-up bead before anything changes.

## Local Audits

{render_items(payload['local_audits'])}

## External Audits

{render_items(payload['external_audits'])}

## Warnings

{chr(10).join(f"- {warning}" for warning in warnings) if warnings else "- None"}

## Human Review Prompts

{chr(10).join(f"- {prompt}" for prompt in prompts) if prompts else "- No immediate review prompts."}
"""


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--validate-exit", type=int, required=True)
    parser.add_argument("--validate-output", required=True)
    parser.add_argument("--health-exit", type=int, required=True)
    parser.add_argument("--diary-exit", type=int, required=True)
    parser.add_argument("--spend-exit", type=int, required=True)
    parser.add_argument("--spend-output", required=True)
    parser.add_argument("--github-exit", type=int, required=True)
    parser.add_argument("--github-output", required=True)
    args = parser.parse_args()

    root = repo_root()
    state = compile_state(root)
    local, warnings = local_audits(root, state, args)
    external = external_audits(root, args)
    prompts = [
        "Review warnings before accepting or promoting any bead.",
        "If a finding matters, move it into the owning Precode file or create a proposed follow-up bead.",
        "Do not continue work from this generated audit alone; start from active memory and the active bead.",
    ]
    payload = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "current_bead": state.get("current_bead"),
        "current_bead_status": state.get("current_bead_status"),
        "local_audits": local,
        "external_audits": external,
        "warnings": warnings,
        "human_review_prompts": prompts,
    }
    write_json(root / AUDIT_JSON, payload)
    (root / AUDIT_MD).write_text(render_markdown(payload), encoding="utf-8")
    print(f"scheduled-audit: wrote {AUDIT_MD} and {AUDIT_JSON}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
