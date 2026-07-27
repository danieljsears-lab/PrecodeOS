#!/usr/bin/env python3
# Version: v0.1.0
# Last updated: 2026-07-27
# Owner: PrecodeOS
# Created by Dan Sears / Recode.
# SPDX-License-Identifier: Apache-2.0
from __future__ import annotations

from fnmatch import fnmatch
import subprocess
from pathlib import Path
from typing import Any

from precode_state import BeadRecord


SENSITIVE_SURFACE_TERMS = {
    "auth",
    "authorization",
    "payment",
    "billing",
    "personal data",
    "upload",
    "migration",
    "deploy",
    "deployment",
    "rollback",
    "environment variable",
    "secret",
    "token",
    "credential",
    "github mutation",
    "merge",
    "destructive",
    "security",
    "external dashboard",
}
TOOL_CLASSES = {"read_only", "verification", "generated_refresh", "local_mutation", "external_mutation", "destructive", "secret_bearing"}
TOOL_FAILURE_CATEGORIES = {
    "code_failure",
    "unavailable_command",
    "missing_dependency",
    "missing_credentials",
    "network_unavailable",
    "permission_or_sandbox_blocked",
    "user_approval_required",
    "destructive_action_blocked",
    "unknown",
}
TOOL_APPROVAL_CLASSES = {"external_mutation", "destructive", "secret_bearing"}
TOOL_ACCESS_LEVEL_BY_CLASS = {
    "read_only": "inspect",
    "verification": "verify",
    "generated_refresh": "inspect",
    "local_mutation": "local-change",
    "external_mutation": "external-change",
    "destructive": "destructive",
    "secret_bearing": "sensitive",
}
TOOL_ACCESS_LEVELS = {"inspect", "verify", "local-change", "sensitive", "external-change", "destructive"}
COMMAND_DESTRUCTIVE_TERMS = {
    "rm -r",
    "rm ",
    "rm -rf",
    "rmdir ",
    "remove ",
    "delete ",
    "git restore ",
    "git checkout --",
    "reset --hard",
    "git reset --hard",
    "git clean",
    "git clean -fd",
    "drop table",
    "drop database",
    "drop schema",
    "truncate table",
    "delete production",
    "destroy",
    "force push",
    "push --force",
    "git push --force",
    "rollback production",
    "prisma migrate reset",
    "supabase db reset",
}
COMMAND_SENSITIVE_TERMS = {
    "secret",
    "token",
    "credential",
    "password",
    "api key",
    "private key",
    "env ",
    ".env",
    "dotenv",
    "vault",
    "auth",
    "oauth",
    "permission",
    "permissions",
    "session",
    "cookie",
    "payment",
    "billing",
    "stripe",
    "migration",
    "migrate",
    "database",
    "personal data",
    "private data",
    "customer data",
    "pii",
    "deploy",
    "production",
    "--prod",
    "dashboard",
    "github",
    "gh ",
    "workflow",
}
COMMAND_EXTERNAL_MUTATION_TERMS = {
    "deploy",
    "push",
    "git push",
    "merge",
    "release",
    "publish",
    "npm publish",
    "gh release",
    "gh pr merge",
    "gh issue edit",
    "gh issue close",
    "gh pr comment",
    "gh label",
    "gh workflow run",
    "gh api",
    "vercel",
    "fly deploy",
    "railway",
    "supabase",
    "supabase db push",
    "stripe",
    "firebase deploy",
    "gcloud",
    "aws ",
}
COMMAND_REPO_TOPOLOGY_MUTATION_TERMS = {
    "git remote add",
    "git remote rename",
    "git remote remove",
    "git remote set-url",
    "git branch --set-upstream-to",
    "git config remote.",
    "git config branch.",
}
COMMAND_LOCAL_MUTATION_TERMS = {
    "apply_patch",
    "write",
    "edit",
    "mv ",
    "cp ",
    "touch ",
    "mkdir ",
    "npm install",
    "npm i ",
    "npm add",
    "pnpm add",
    "yarn add",
    "bun add",
    "pip install",
    "python -m pip install",
    "poetry add",
    "bundle add",
    "cargo add",
    "migration",
    "migrate",
}
COMMAND_VERIFICATION_TERMS = {"test", "check", "validate", "lint", "py_compile", "typecheck", "pytest", "vitest", "jest"}
COMMAND_GENERATED_REFRESH_TERMS = {"os-health", "next-step", "file-inventory", "memory-index", "scheduled-audit"}


def git_status_changed_paths(root: Path) -> tuple[list[str], str | None]:
    if not (root / ".git").exists():
        return [], "git status unavailable: workspace root is not a git checkout"
    result = subprocess.run(["git", "status", "--short"], cwd=root, check=False, capture_output=True, text=True)
    if result.returncode != 0:
        message = (result.stderr or result.stdout or "git status unavailable").strip()
        return [], message
    paths: list[str] = []
    for line in result.stdout.splitlines():
        if not line.strip():
            continue
        value = line[3:].strip() if len(line) > 3 else line.strip()
        if " -> " in value:
            value = value.split(" -> ", 1)[1]
        paths.append(value)
    return paths, None


def path_matches_scope(path: str, allowed: str) -> bool:
    cleaned_path = path.strip().strip('"')
    cleaned_allowed = allowed.strip().strip('"').rstrip("/")
    if not cleaned_path or not cleaned_allowed:
        return False
    if any(char in cleaned_allowed for char in "*?[]"):
        return fnmatch(cleaned_path, cleaned_allowed)
    return cleaned_path == cleaned_allowed or cleaned_path.startswith(f"{cleaned_allowed}/")


def generated_guardrail_allowed(path: str) -> bool:
    return (
        path in {"OS-HEALTH.md", "PRECODE-HELP.md", "PROGRESS.md"}
        or path.startswith("logs/")
        or path.endswith(".pyc")
        or "/__pycache__/" in path
    )


def command_classification(command: str, bead: BeadRecord | None) -> dict[str, Any]:
    command_text = command.strip()
    lower = command_text.lower()
    if not command_text:
        return {}

    bead_text = ""
    if bead:
        bead_text = " ".join(
            [
                bead.title,
                bead.bead_kind,
                bead.primary_authority,
                " ".join(bead.files_in_play),
                bead.sections.get("Objective", ""),
                bead.sections.get("Done When", ""),
                bead.sections.get("Stop If", ""),
            ]
        ).lower()
    sensitive_surface = any(term in lower or term in bead_text for term in SENSITIVE_SURFACE_TERMS | COMMAND_SENSITIVE_TERMS)

    if any(term in lower for term in COMMAND_REPO_TOPOLOGY_MUTATION_TERMS):
        tool_class = "local_mutation"
        user_decision = "approval needed"
        summary = "Ask before running this. It changes repository topology, remotes, or upstream tracking."
        approval_prompt = "Ask the user to approve the exact repo-topology change, canonical remote, rollback or blocked escape path, and validation plan."
    elif any(term in lower for term in COMMAND_DESTRUCTIVE_TERMS):
        tool_class = "destructive"
        user_decision = "stop"
        summary = "Stop before running this. It may delete, reset, drop, force-push, or otherwise cause hard-to-reverse damage."
        approval_prompt = "Ask the user to approve the exact destructive command, expected effect, rollback or blocked escape path, and evidence plan."
    elif any(term in lower for term in COMMAND_SENSITIVE_TERMS):
        tool_class = "secret_bearing" if any(term in lower for term in ("secret", "token", "credential", "password", ".env")) else "external_mutation"
        user_decision = "approval needed"
        summary = "Ask before running this. It appears to touch secrets, auth, data, payments, deployment, or another sensitive surface."
        approval_prompt = "Ask the user to approve the exact sensitive action, intended scope, risk, rollback or blocked escape path, and proof plan."
    elif any(term in lower for term in COMMAND_EXTERNAL_MUTATION_TERMS):
        tool_class = "external_mutation"
        user_decision = "approval needed"
        summary = "Ask before running this. It may mutate an external service, hosted environment, issue tracker, release, or shared branch."
        approval_prompt = "Ask the user to approve the exact external mutation, affected system, recovery plan, and evidence to record afterward."
    elif any(term in lower for term in COMMAND_GENERATED_REFRESH_TERMS):
        tool_class = "generated_refresh"
        user_decision = "continue"
        summary = "This command looks like a generated Precode refresh. It can continue, but it is not proof by itself."
        approval_prompt = "No special approval suggested; record separate checks if this is evidence for done."
    elif any(term in lower for term in COMMAND_VERIFICATION_TERMS):
        tool_class = "verification"
        user_decision = "continue"
        summary = "This command looks like verification. It is safe to run as evidence if it stays inside the current bead."
        approval_prompt = "No special approval suggested."
    elif any(term in lower for term in COMMAND_LOCAL_MUTATION_TERMS):
        tool_class = "local_mutation"
        if sensitive_surface:
            access_level = "sensitive"
            user_decision = "approval needed"
            summary = "Ask before running this. It may change local files while the bead involves a sensitive surface."
            approval_prompt = "Ask the user to approve the sensitive local mutation, expected files, rollback or escape path, and proof plan."
        else:
            access_level = TOOL_ACCESS_LEVEL_BY_CLASS[tool_class]
            user_decision = "continue"
            summary = "This may change local project files. Continue only if the expected paths stay inside files_in_play."
            approval_prompt = "Ask for approval first if the command widens scope, installs dependencies, changes generated authority-like files, or touches sensitive surfaces."
    else:
        tool_class = "read_only"
        access_level = TOOL_ACCESS_LEVEL_BY_CLASS[tool_class]
        user_decision = "continue"
        summary = "This command does not look destructive or sensitive from its summary."
        approval_prompt = "No special approval suggested."

    if "access_level" not in locals():
        access_level = TOOL_ACCESS_LEVEL_BY_CLASS.get(tool_class, "inspect")
    access_level_warning = (
        "Access levels are advisory routing language over existing tool-call classes, files_in_play, Run Contracts, approval gates, "
        "and stop conditions; they do not approve commands, enforce permissions, add sandbox behavior, or create schema-backed access metadata."
    )

    return {
        "command": command_text,
        "class": tool_class,
        "access_level": access_level,
        "user_decision": user_decision,
        "plain_english_summary": summary,
        "why_this_matters": "Non-technical builders need command risk translated before a tool mutates files, services, secrets, or production state.",
        "stop_if": "Stop if the command deletes, force-resets, migrates, deploys, exposes secrets, or touches production without explicit approval.",
        "approval_prompt": approval_prompt,
        "access_level_warning": access_level_warning,
        "sensitive_surface_detected": sensitive_surface,
        "advisory_only": True,
    }


def files_in_play_guardrail(root: Path, bead: BeadRecord | None, command: str = "", edit_lock: bool = False) -> dict[str, Any]:
    warnings: list[str] = []
    changed_paths, git_warning = git_status_changed_paths(root)
    if git_warning:
        warnings.append(git_warning)

    allowed = bead.files_in_play if bead else []
    out_of_scope = [
        path
        for path in changed_paths
        if not generated_guardrail_allowed(path) and not any(path_matches_scope(path, item) for item in allowed)
    ]
    if out_of_scope:
        warnings.append(f"changed paths outside active bead files_in_play: {out_of_scope[:12]}")
    if bead and not allowed:
        warnings.append("active bead has no files_in_play for mutation guardrail comparison")
    command_state = command_classification(command, bead) if command else {}
    if command_state and command_state.get("user_decision") in {"approval needed", "stop"}:
        warnings.append(str(command_state.get("plain_english_summary")))

    edit_lock_state = {
        "enabled": edit_lock,
        "allowed_paths": allowed,
        "generated_outputs_allowed": ["logs/*", "OS-HEALTH.md", "PRECODE-HELP.md", "PROGRESS.md"],
        "advisory_only": True,
    }
    if edit_lock and out_of_scope:
        edit_lock_state["user_decision"] = "stop"
        edit_lock_state["plain_english_summary"] = "The optional edit lock found changed paths outside this bead. Stop and ask whether this is a separate bead."
    elif edit_lock:
        edit_lock_state["user_decision"] = "continue"
        edit_lock_state["plain_english_summary"] = "The optional edit lock did not find changed paths outside this bead."

    if out_of_scope:
        user_decision = "stop"
        summary = "Changed paths appear outside this bead. Stop and classify each path before continuing."
        stop_if = "Stop if any changed path is outside files_in_play and is not generated Precode output."
        approval_prompt = "Ask whether each path is generated evidence, current-bead work that needs explicit scope approval, follow-up bead work, or user-owned revert work."
    elif command_state:
        user_decision = str(command_state.get("user_decision") or "continue")
        summary = str(command_state.get("plain_english_summary") or "Command risk was classified.")
        stop_if = str(command_state.get("stop_if") or "Stop if command scope or risk is unclear.")
        approval_prompt = str(command_state.get("approval_prompt") or "No special approval suggested.")
    else:
        user_decision = "continue"
        summary = "No out-of-scope changed files were detected by this advisory guardrail."
        stop_if = "Stop if future edits touch files outside files_in_play, sensitive surfaces, or generated reports as if they were task authority."
        approval_prompt = "No extra approval suggested by files-in-play."

    return {
        "status": "warning" if warnings else "pass",
        "warnings": warnings,
        "details": {
            "current_bead": bead.rel_path if bead else "missing",
            "advisory_only": True,
            "changed_paths": changed_paths,
            "allowed_paths": allowed,
            "out_of_scope_paths": out_of_scope,
            "generated_outputs_allowed": ["logs/*", "OS-HEALTH.md", "PRECODE-HELP.md", "PROGRESS.md"],
            "git_status_available": git_warning is None,
            "plain_english_summary": summary,
            "user_decision": user_decision,
            "why_this_matters": "Files in play are the beginner-readable boundary for what the agent is allowed to change during this bead.",
            "stop_if": stop_if,
            "approval_prompt": approval_prompt,
            "command_classification": command_state,
            "edit_lock": edit_lock_state,
        },
    }
