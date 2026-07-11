#!/usr/bin/env python3
# Version: v0.1.0
# Last updated: 2026-07-11
# Owner: PrecodeOS
# Created by Dan Sears / Recode.
# SPDX-License-Identifier: Apache-2.0
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import ipaddress
import json
from pathlib import Path
import re
import shutil
import subprocess
import urllib.error
import urllib.parse
import urllib.request
from typing import Any

from os_compiler import repo_root


FORBIDDEN_USES = [
    "task selection",
    "PRD approval",
    "bead activation",
    "implementation acceptance",
    "review approval",
    "release approval",
    "merge approval",
    "transition approval",
    "deployment approval",
    "external mutation",
    "owner-file mutation",
]
PLACEHOLDER_PROVIDERS = [
    ("deployment", "Deployment Status Audit", "no deployment provider audit configured"),
    ("monitoring", "Monitoring / Observability Audit", "no monitoring provider audit configured"),
    ("dependency_security", "Dependency / Security Advisory Audit", "no read-only dependency or advisory source configured"),
    ("issue_tracker", "Issue Tracker Audit", "no non-GitHub issue tracker audit configured"),
    ("dashboard", "External Dashboard Setup Audit", "manual dashboard setup status should be documented in PROJECT-CONTEXT.md when needed"),
]
NONE_TERMS = {"", "none", "none.", "not configured", "not configured.", "n/a"}


def checked_at() -> str:
    return datetime.now(timezone.utc).isoformat()


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


def row(
    provider: str,
    check_name: str,
    status: str,
    summary: str,
    *,
    configured: bool = False,
    details: dict[str, Any] | None = None,
    warnings: list[str] | None = None,
    source: str = "",
) -> dict[str, Any]:
    return {
        "provider": provider,
        "check_name": check_name,
        "status": status,
        "configured": configured,
        "advisory_only": True,
        "summary": summary,
        "details": details or {},
        "warnings": warnings or [],
        "checked_at": checked_at(),
        "source": source,
        "forbidden_uses": FORBIDDEN_USES,
    }


def github_rows(root: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    context: dict[str, Any] = {"repository_root": str(root)}
    git_code, _ = run(["git", "rev-parse", "--is-inside-work-tree"], root)
    if git_code != 0 or not (root / ".git").exists():
        return [
            row("github", "GitHub Repository Audit", "not_configured", "not a git checkout or .git directory is unavailable", source="git"),
            row("github", "CI Status Audit", "not_configured", "requires git checkout and configured provider", source="git"),
        ]

    branch_code, branch = run(["git", "rev-parse", "--abbrev-ref", "HEAD"], root)
    remote_code, remote_url = run(["git", "remote", "get-url", "origin"], root)
    default_code, default_ref = run(["git", "symbolic-ref", "--quiet", "--short", "refs/remotes/origin/HEAD"], root)
    status_code, worktree_status = run(["git", "status", "--porcelain=v1"], root)
    upstream_code, upstream_counts = run(["git", "rev-list", "--left-right", "--count", "@{u}...HEAD"], root)
    context.update(
        {
            "branch": branch if branch_code == 0 else "unknown",
            "remote_url": remote_url if remote_code == 0 else None,
            "default_branch": default_ref.removeprefix("origin/") if default_code == 0 else None,
            "worktree_dirty": bool(worktree_status) if status_code == 0 else None,
        }
    )
    if upstream_code == 0 and upstream_counts:
        parts = upstream_counts.split()
        if len(parts) == 2:
            context["behind"] = int(parts[0])
            context["ahead"] = int(parts[1])

    gh = shutil.which("gh")
    if not gh:
        return [
            row("github", "GitHub Repository Audit", "not_configured", "`gh` CLI not found; local git metadata only", configured=False, details=context, source="git"),
            row("github", "CI Status Audit", "not_configured", "`gh` CLI not found", source="gh"),
        ]

    auth_code, auth_text = run(["gh", "auth", "status"], root)
    if auth_code != 0:
        return [
            row("github", "GitHub Repository Audit", "not_configured", "`gh` CLI is not authenticated", details={"auth_status": auth_text, **context}, source="gh"),
            row("github", "CI Status Audit", "not_configured", "`gh` CLI is not authenticated", source="gh"),
        ]

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
    rows.append(
        row(
            "github",
            "GitHub Repository Audit",
            "warning" if repo_warnings else "info",
            "read-only GitHub repository status collected" if not repo_warnings else "; ".join(repo_warnings),
            configured=True,
            details=details,
            warnings=repo_warnings,
            source="gh",
        )
    )

    ci_details: dict[str, Any] = {}
    if isinstance(runs, list) and runs:
        ci_details["latest_run"] = runs[0]
        conclusion = runs[0].get("conclusion") or runs[0].get("status") or "unknown"
        rows.append(
            row(
                "github",
                "CI Status Audit",
                "pass" if conclusion == "success" else "warning",
                f"latest workflow result: {conclusion}",
                configured=True,
                details=ci_details,
                source="gh",
            )
        )
    else:
        rows.append(
            row(
                "github",
                "CI Status Audit",
                "not_configured" if run_error else "info",
                run_error or "no workflow runs found for current branch",
                configured=not bool(run_error),
                details=ci_details,
                warnings=[run_error] if run_error else [],
                source="gh",
            )
        )
    return rows


def health_url_candidates(project_context: Path) -> list[str]:
    if not project_context.is_file():
        return []
    lines = project_context.read_text(encoding="utf-8").splitlines()
    candidates: list[str] = []
    collecting = False
    for line in lines:
        stripped = line.strip()
        lower = stripped.lower()
        if lower.startswith("- safe health urls for read-only uptime checks:"):
            collecting = True
            after = stripped.split(":", 1)[1].strip()
            if after.lower() not in NONE_TERMS:
                candidates.extend(re.findall(r"https?://[^\s,`<>]+", after))
            continue
        if collecting:
            if stripped.startswith("- ") and not line.startswith("  "):
                break
            if stripped.startswith("- "):
                value = stripped[2:].strip()
                if value.lower() not in NONE_TERMS:
                    candidates.extend(re.findall(r"https?://[^\s,`<>]+", value))
    return candidates


def safe_url_issue(url: str) -> str:
    parsed = urllib.parse.urlparse(url)
    if parsed.scheme not in {"http", "https"}:
        return "health URL must use http or https"
    if not parsed.netloc or not parsed.hostname:
        return "health URL is missing a hostname"
    if parsed.username or parsed.password:
        return "health URL must not contain credentials"
    if parsed.query or parsed.fragment:
        return "health URL must not contain query strings or fragments"
    host = parsed.hostname.lower()
    if host in {"localhost", "127.0.0.1", "::1"} or host.endswith(".local"):
        return "health URL must not target localhost or local-only names"
    try:
        ip = ipaddress.ip_address(host)
    except ValueError:
        ip = None
    if ip and (ip.is_private or ip.is_loopback or ip.is_link_local or ip.is_reserved):
        return "health URL must not target private, loopback, link-local, or reserved IP addresses"
    return ""


def health_rows(root: Path) -> list[dict[str, Any]]:
    urls = health_url_candidates(root / "PROJECT-CONTEXT.md")
    if not urls:
        return [
            row(
                "health_url",
                "Uptime / Endpoint Audit",
                "not_configured",
                "no safe health URL configured in PROJECT-CONTEXT.md",
                source="PROJECT-CONTEXT.md",
            )
        ]

    rows: list[dict[str, Any]] = []
    for url in urls:
        issue = safe_url_issue(url)
        details = {"url": url, "method": "GET"}
        if issue:
            rows.append(row("health_url", "Uptime / Endpoint Audit", "warning", issue, configured=True, details=details, warnings=[issue], source="PROJECT-CONTEXT.md"))
            continue
        request = urllib.request.Request(url, method="GET", headers={"User-Agent": "PrecodeOS external-status/0.1"})
        try:
            with urllib.request.urlopen(request, timeout=10) as response:
                details["status_code"] = response.status
                details["final_url"] = response.geturl()
                rows.append(
                    row(
                        "health_url",
                        "Uptime / Endpoint Audit",
                        "pass" if 200 <= response.status < 400 else "warning",
                        f"safe GET returned HTTP {response.status}",
                        configured=True,
                        details=details,
                        source="PROJECT-CONTEXT.md",
                    )
                )
        except urllib.error.HTTPError as exc:
            details["status_code"] = exc.code
            rows.append(row("health_url", "Uptime / Endpoint Audit", "warning", f"safe GET returned HTTP {exc.code}", configured=True, details=details, warnings=[str(exc)], source="PROJECT-CONTEXT.md"))
        except (urllib.error.URLError, TimeoutError, OSError) as exc:
            rows.append(row("health_url", "Uptime / Endpoint Audit", "warning", f"safe GET failed: {exc}", configured=True, details=details, warnings=[str(exc)], source="PROJECT-CONTEXT.md"))
    return rows


def placeholder_rows() -> list[dict[str, Any]]:
    return [row(provider, check_name, "not_configured", summary, source="PROJECT-CONTEXT.md") for provider, check_name, summary in PLACEHOLDER_PROVIDERS]


def build_payload(root: Path) -> dict[str, Any]:
    rows = [*github_rows(root), *health_rows(root), *placeholder_rows()]
    warnings = [warning for item in rows for warning in item.get("warnings", [])]
    return {
        "tool": "external-status",
        "generated_at": checked_at(),
        "advisory_only": True,
        "row_shape": [
            "provider",
            "check_name",
            "status",
            "configured",
            "advisory_only",
            "summary",
            "details",
            "warnings",
            "checked_at",
            "source",
            "forbidden_uses",
        ],
        "rows": rows,
        "warnings": warnings,
        "forbidden_uses": FORBIDDEN_USES,
    }


def self_test(root: Path) -> dict[str, Any]:
    failures: list[dict[str, str]] = []
    payload = build_payload(root)
    required = set(payload["row_shape"])
    for item in payload["rows"]:
        missing = sorted(required.difference(item))
        if missing:
            failures.append({"scenario": "row shape", "expected": ",".join(missing), "actual": str(item)})
        if item.get("advisory_only") is not True:
            failures.append({"scenario": "advisory boundary", "expected": "advisory_only true", "actual": str(item.get("advisory_only"))})
        forbidden = " ".join(item.get("forbidden_uses") or [])
        for term in ("task selection", "release approval", "external mutation", "owner-file mutation"):
            if term not in forbidden:
                failures.append({"scenario": "forbidden uses", "expected": term, "actual": forbidden})
    statuses = {item.get("status") for item in payload["rows"]}
    if "not_configured" not in statuses:
        failures.append({"scenario": "missing configuration", "expected": "at least one not_configured row", "actual": ",".join(sorted(str(status) for status in statuses))})
    protocol_path = root / "tasks" / "reference" / "EXTERNAL-STATUS-INTEGRATION-PROTOCOL.md"
    if not protocol_path.is_file():
        failures.append({"scenario": "protocol owner", "expected": str(protocol_path.relative_to(root)), "actual": "missing"})
    else:
        text = protocol_path.read_text(encoding="utf-8")
        for term in ("External status is evidence only", "Safe health URLs", "Forbidden Uses", "Promotion Path"):
            if term not in text:
                failures.append({"scenario": "protocol term", "expected": term, "actual": "missing"})
    return {
        "tool": "external-status",
        "mode": "self-test",
        "status": "pass" if not failures else "fail",
        "scenario_count": len(payload["rows"]) + 2,
        "failures": failures,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Show provider-neutral read-only external status evidence.")
    parser.add_argument("--self-test", action="store_true", help="run deterministic external status contract checks")
    args = parser.parse_args()
    root = repo_root()
    payload = self_test(root) if args.self_test else build_payload(root)
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0 if payload.get("status") != "fail" else 1


if __name__ == "__main__":
    raise SystemExit(main())
