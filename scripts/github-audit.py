#!/usr/bin/env python3
# Version: v0.1.1
# Last updated: 2026-07-11
# Owner: PrecodeOS
# Created by Dan Sears / Recode.
# SPDX-License-Identifier: Apache-2.0
from __future__ import annotations

from datetime import datetime, timezone
import json
from pathlib import Path
import shutil
import subprocess
from typing import Any

from os_compiler import discover_git_remote_context, repo_root


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


def item(name: str, status: str, summary: str, details: dict[str, Any] | None = None) -> dict[str, Any]:
    return {"name": name, "status": status, "summary": summary, "details": details or {}}


def main() -> int:
    root = repo_root()
    gh = shutil.which("gh")
    audits: list[dict[str, Any]] = []
    warnings: list[str] = []
    context: dict[str, Any] = {"repository_root": str(root)}

    git_code, _ = run(["git", "rev-parse", "--is-inside-work-tree"], root)
    if git_code != 0 or not (root / ".git").exists():
        audits.append(item("GitHub Repository Audit", "not_configured", "not a git checkout or .git directory is unavailable"))
        audits.append(item("CI Status Audit", "not_configured", "requires git checkout and configured provider"))
        payload = {
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "tool": "github-audit",
            "configured": False,
            "context": context,
            "audits": audits,
            "warnings": warnings,
        }
        print(json.dumps(payload, indent=2, sort_keys=True))
        return 0

    branch_code, branch = run(["git", "rev-parse", "--abbrev-ref", "HEAD"], root)
    remote_context, remote_warnings = discover_git_remote_context(root)
    status_code, worktree_status = run(["git", "status", "--porcelain=v1"], root)
    upstream_code, upstream_counts = run(["git", "rev-list", "--left-right", "--count", "@{u}...HEAD"], root)

    context.update(
        {
            "branch": branch if branch_code == 0 else "unknown",
            "worktree_dirty": bool(worktree_status) if status_code == 0 else None,
            **remote_context,
        }
    )
    warnings.extend(remote_warnings)
    if upstream_code == 0 and upstream_counts:
        parts = upstream_counts.split()
        if len(parts) == 2:
            context["behind"] = int(parts[0])
            context["ahead"] = int(parts[1])

    if not gh:
        audits.append(
            item(
                "GitHub Repository Audit",
                "not_configured",
                "`gh` CLI not found; local git metadata only",
                context,
            )
        )
        audits.append(item("CI Status Audit", "not_configured", "`gh` CLI not found"))
    else:
        auth_code, auth_text = run(["gh", "auth", "status"], root)
        if auth_code != 0:
            audits.append(item("GitHub Repository Audit", "not_configured", "`gh` CLI is not authenticated", {"auth_status": auth_text, **context}))
            audits.append(item("CI Status Audit", "not_configured", "`gh` CLI is not authenticated"))
        else:
            _, repo_data, repo_error = json_run(["gh", "repo", "view", "--json", "nameWithOwner,url,defaultBranchRef"], root)
            _, prs, pr_error = json_run(
                [
                    "gh",
                    "pr",
                    "list",
                    "--head",
                    context.get("branch") or "",
                    "--state",
                    "open",
                    "--json",
                    "number,title,url,state,reviewDecision,mergeStateStatus,statusCheckRollup,updatedAt",
                ],
                root,
            )
            _, open_prs, open_pr_error = json_run(["gh", "pr", "list", "--state", "open", "--limit", "50", "--json", "number,title,url,updatedAt"], root)
            _, runs, run_error = json_run(["gh", "run", "list", "--branch", context.get("branch") or "", "--limit", "1", "--json", "status,conclusion,workflowName,displayTitle,url,createdAt"], root)

            details = dict(context)
            if isinstance(repo_data, dict):
                details["repository"] = repo_data
            if isinstance(prs, list):
                details["current_branch_pr"] = prs[0] if prs else None
            if isinstance(open_prs, list):
                details["open_pull_request_count"] = len(open_prs)

            repo_warnings = [value for value in (repo_error, pr_error, open_pr_error) if value]
            audits.append(
                item(
                    "GitHub Repository Audit",
                    "warning" if repo_warnings else "info",
                    "read-only GitHub repository status collected" if not repo_warnings else "; ".join(repo_warnings),
                    details,
                )
            )

            ci_details: dict[str, Any] = {}
            if isinstance(runs, list) and runs:
                ci_details["latest_run"] = runs[0]
                conclusion = runs[0].get("conclusion") or runs[0].get("status") or "unknown"
                ci_status = "pass" if conclusion == "success" else "warning"
                audits.append(item("CI Status Audit", ci_status, f"latest workflow result: {conclusion}", ci_details))
            else:
                audits.append(item("CI Status Audit", "not_configured" if run_error else "info", run_error or "no workflow runs found for current branch", ci_details))

    if context.get("worktree_dirty"):
        warnings.append("local working tree has uncommitted changes")
    if int(context.get("behind") or 0) > 0:
        warnings.append("local branch is behind its upstream")
    if int(context.get("ahead") or 0) > 0:
        warnings.append("local branch is ahead of its upstream")

    payload = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "tool": "github-audit",
        "configured": any(audit["status"] not in {"not_configured"} for audit in audits),
        "context": context,
        "audits": audits,
        "warnings": warnings,
    }
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
