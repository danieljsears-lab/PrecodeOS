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
import shutil
import subprocess
from typing import Any

from os_compiler import TEAM_COLLABORATION_GENERATED_WARNING, team_collaboration_preview
from precode_state import bead_paths, read_bead, read_todo_state, repo_root


def run(args: list[str], root: Path, timeout: int = 20) -> tuple[int, str]:
    try:
        result = subprocess.run(args, cwd=root, check=False, capture_output=True, text=True, timeout=timeout)
    except (OSError, subprocess.TimeoutExpired) as exc:
        return 1, str(exc)
    return result.returncode, (result.stdout or result.stderr).strip()


def json_run(args: list[str], root: Path) -> tuple[int, Any, str]:
    code, text = run(args, root)
    if code != 0:
        return code, None, text
    try:
        return 0, json.loads(text or "null"), ""
    except json.JSONDecodeError as exc:
        return 1, None, f"invalid JSON: {exc}"


def read_current_state(root: Path) -> tuple[dict[str, Any], Any, list[Any]]:
    todo = read_todo_state(root)
    beads = [read_bead(path, root) for path in bead_paths(root)]
    bead_map = {bead.rel_path: bead for bead in beads}
    current_bead = bead_map.get(str(todo.get("current_bead") or ""))
    return todo, current_bead, beads


def github_team_evidence(root: Path, branch: str) -> dict[str, Any]:
    gh = shutil.which("gh")
    if not gh:
        return {
            "status": "not_configured",
            "advisory_only": True,
            "summary": "`gh` CLI not found; GitHub team evidence not collected.",
        }
    auth_code, auth_text = run(["gh", "auth", "status"], root)
    if auth_code != 0:
        return {
            "status": "not_configured",
            "advisory_only": True,
            "summary": "`gh` CLI is not authenticated; GitHub team evidence not collected.",
            "details": {"auth_status": auth_text},
        }

    warnings: list[str] = []
    _, repo_data, repo_error = json_run(["gh", "repo", "view", "--json", "nameWithOwner,url,defaultBranchRef"], root)
    _, current_prs, current_pr_error = json_run(
        [
            "gh",
            "pr",
            "list",
            "--head",
            branch,
            "--state",
            "open",
            "--json",
            "number,title,url,state,reviewDecision,mergeStateStatus,statusCheckRollup,updatedAt,headRefName,baseRefName",
        ],
        root,
    )
    _, open_prs, open_pr_error = json_run(
        ["gh", "pr", "list", "--state", "open", "--limit", "50", "--json", "number,title,url,updatedAt,headRefName,baseRefName"],
        root,
    )
    _, runs, run_error = json_run(
        ["gh", "run", "list", "--branch", branch, "--limit", "5", "--json", "status,conclusion,workflowName,displayTitle,url,createdAt"],
        root,
    )

    for error in (repo_error, current_pr_error, open_pr_error, run_error):
        if error:
            warnings.append(error)

    details: dict[str, Any] = {
        "repository": repo_data if isinstance(repo_data, dict) else None,
        "current_branch_prs": current_prs if isinstance(current_prs, list) else [],
        "open_pull_requests": open_prs if isinstance(open_prs, list) else [],
        "recent_runs": runs if isinstance(runs, list) else [],
        "forbidden_uses": [
            "task selection",
            "PRD approval",
            "bead activation",
            "implementation acceptance",
            "merge approval",
            "release approval",
            "GitHub mutation",
        ],
    }
    return {
        "status": "warning" if warnings else "pass",
        "advisory_only": True,
        "summary": "read-only GitHub team evidence collected" if not warnings else "read-only GitHub team evidence is incomplete",
        "warnings": warnings,
        "details": details,
    }


def build_preview(root: Path, *, integration_branch: str = "", include_github: bool = False) -> dict[str, Any]:
    todo, current_bead, beads = read_current_state(root)
    branch_code, branch = run(["git", "rev-parse", "--abbrev-ref", "HEAD"], root)
    github_evidence = github_team_evidence(root, branch if branch_code == 0 else "") if include_github else None
    return team_collaboration_preview(
        root,
        todo,
        current_bead,
        beads,
        integration_branch=integration_branch,
        github_evidence=github_evidence,
    )


def assert_terms(path: Path, terms: list[str], failures: list[dict[str, str]], scenario: str) -> None:
    text = path.read_text(encoding="utf-8")
    for term in terms:
        if term not in text:
            failures.append({"scenario": scenario, "expected": term, "actual": "missing"})


def self_test(root: Path) -> dict[str, Any]:
    failures: list[dict[str, str]] = []
    scenario_terms = {
        "coordinator invocation": [
            "coordinator invokes the lane first",
            "team members and roles",
            "product decision owner",
            "stop conditions",
        ],
        "teammate startup": [
            "Each teammate must confirm the lane from repo state before editing",
            "branch/worktree",
            "primary authority",
            "what requires coordinator approval before editing",
        ],
        "isolated parallel bead": [
            "one branch or worktree per contributor bead",
            "one active bead per checkout",
            "can run in parallel",
            "branch/worktree-isolated teammate context",
        ],
        "PR conflict review": [
            "owner-file impacts",
            "conflicts with the integration branch",
            "Team Merge And Re-entry Review Pack",
            "Review and merge evidence",
        ],
        "stale branch re-entry": [
            "re-entry starts by checking",
            "whether checks or manual verification are stale",
            "integration branch",
            "stop and ask the coordinator before editing",
        ],
        "GitHub evidence demotion": [
            "GitHub branches, pull requests, reviews, checks, labels, comments, and project-board status are external evidence",
            "must not choose tasks",
            "approve merge",
            "GitHub mutation",
        ],
    }
    protocol_path = root / "tasks" / "reference" / "TEAM-COLLABORATION-PROTOCOL.md"
    prompt_path = root / "tasks" / "reference" / "PROMPT-PATTERNS.md"
    github_path = root / "tasks" / "reference" / "GITHUB-INTEGRATION-PROTOCOL.md"
    for scenario, terms in scenario_terms.items():
        assert_terms(protocol_path, terms[:2], failures, scenario)
        assert_terms(prompt_path, terms[2:3], failures, scenario)
        assert_terms(github_path if "GitHub" in scenario else protocol_path, terms[3:], failures, scenario)

    payload = build_preview(root)
    details = payload.get("details") or {}
    required_fields = [
        "owner_protocol",
        "current_branch",
        "integration_branch",
        "current_bead",
        "one_active_bead_per_checkout",
        "owner_file_impacts",
        "re_entry_risks",
        "delegation_reentry",
        "merge_review_packet_fields",
        "assignment_packet_fields",
        "github_evidence",
        "forbidden_uses",
    ]
    for field in required_fields:
        if field not in details:
            failures.append({"scenario": "preview payload field", "expected": field, "actual": "missing"})
    if payload.get("generated_report_warning") != TEAM_COLLABORATION_GENERATED_WARNING:
        failures.append({"scenario": "generated warning", "expected": TEAM_COLLABORATION_GENERATED_WARNING, "actual": str(payload.get("generated_report_warning"))})
    if details.get("advisory_only") is not True:
        failures.append({"scenario": "advisory boundary", "expected": "advisory_only true", "actual": str(details.get("advisory_only"))})
    forbidden = " ".join(details.get("forbidden_uses") or [])
    for term in ["task selection", "merge approval", "GitHub mutation"]:
        if term not in forbidden:
            failures.append({"scenario": "forbidden uses", "expected": term, "actual": forbidden})
    reentry = details.get("delegation_reentry") or {}
    for field in ["scope_returned", "changed_files", "approval_still_required", "external_status_evidence", "recommended_next_human_action"]:
        if field not in reentry:
            failures.append({"scenario": "delegation re-entry field", "expected": field, "actual": "missing"})

    return {
        "tool": "team-collaboration-check",
        "mode": "self-test",
        "status": "pass" if not failures else "fail",
        "scenario_count": len(scenario_terms) + 1,
        "failures": failures,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Show read-only Small Team Collaboration Lane preview evidence.")
    parser.add_argument("--github", action="store_true", help="include optional read-only GitHub branch, PR, review, and check evidence")
    parser.add_argument("--integration-branch", default="", help="integration branch to compare against; defaults to origin HEAD or upstream when available")
    parser.add_argument("--self-test", action="store_true", help="run deterministic team-collaboration scenario fixture checks")
    args = parser.parse_args()

    root = repo_root()
    if args.self_test:
        payload = self_test(root)
        print(json.dumps(payload, indent=2, sort_keys=True))
        return 0 if payload["status"] == "pass" else 1

    payload = build_preview(root, integration_branch=args.integration_branch, include_github=args.github)
    print(json.dumps({"tool": "team-collaboration-check", **payload}, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
