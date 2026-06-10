#!/usr/bin/env python3
# Version: v0.1.24
# Last updated: 2026-06-09
# Owner: PrecodeOS
# Created by Dan Sears / Recode.
# SPDX-License-Identifier: Apache-2.0
from __future__ import annotations

from collections import Counter
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from fnmatch import fnmatch
import json
import re
import subprocess
from pathlib import Path
from typing import Any

from os_parser import (
    MarkdownDocument,
    bullet_items,
    colon_bullets,
    extract_anchor,
    extract_contract_values,
    first_bullet,
    read_text,
    split_frontmatter,
    strip_inline_code,
)
from precode_routing import next_step_guidance


APP_DIR = "app"
ACTIVE_MEMORY = ["AGENT.md", "DECISIONS.md", "tasks/todo.md"]
SHIM_DOCS = ["AGENTS.md", "GEMINI.md", ".github/copilot-instructions.md", "CLAUDE.md"]
ADAPTER_DOCS = [
    "adapters/ADAPTER-INDEX.md",
    "adapters/CLAUDE.md",
    "adapters/CODEX.md",
    "adapters/COPILOT.md",
    "adapters/GEMINI.md",
    "adapters/ANTIGRAVITY.md",
    "adapters/CURSOR.md",
]
FRONTMATTER_EMPTY_MARKERS = {"", "none", "n/a", "na", "null", "not applicable"}
PENDING_MARKERS = {"pending", "blocked", "not recorded", "unavailable", "missing", "fail", "failed", "needs_info", "manual_testing"}
APPROVED_MARKERS = ("accepted", "approve", "approved")
VERIFICATION_TIERS = {"static", "unit", "integration", "browser", "manual", "external"}
DELEGATION_MODES = {"human_in_loop", "afk_candidate", "human_required"}
TEST_STRATEGIES = {"failing_first", "characterization", "static_only", "manual_only", "not_applicable"}
REVIEW_CONTEXTS = {"same_session_ok", "fresh_context_recommended", "fresh_context_required"}
COMPLEXITY_LEVELS = {"trivial", "narrow", "standard", "high-risk", "multi-system"}
REQUIRED_PLANNING_DEPTHS = {"none", "brief", "PRD", "PRD+architecture", "PRD+architecture+test-plan"}
AUTONOMY_LEVELS = {"supervised", "bounded-afk", "human-only"}
CODE_EXTENSIONS = {
    ".py",
    ".sh",
    ".js",
    ".jsx",
    ".ts",
    ".tsx",
    ".css",
    ".scss",
    ".html",
    ".go",
    ".rs",
    ".java",
    ".rb",
    ".php",
    ".sql",
    ".yml",
    ".yaml",
    ".json",
}
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
PLANNING_BEAD_KINDS = {"planning", "review", "prfaq", "challenge", "source_intake"}
IMPLEMENTATION_BEAD_KINDS = {"implementation", "feature"}
VAGUE_DONE_TERMS = {"improve", "better", "clean up", "polish", "etc", "and then", "as needed", "various"}
DEPENDENCY_HINT_TERMS = {"blocked by", "depends on", "waits for", "manual setup", "external status"}
HORIZONTAL_SLICE_TERMS = {
    "schema first",
    "database first",
    "migration first",
    "backend first",
    "api first",
    "service first",
    "frontend first",
    "ui first",
    "tests later",
    "test later",
}
USER_FACING_TERMS = {"user-facing", "dashboard", "screen", "page", "route", "frontend", "ui", "browser", "user can", "visible"}
GENERATED_REPORTS = ["PRECODE-HELP.md", "PROGRESS.md", "OS-HEALTH.md", "logs/bead-build-journal.md", "logs/learning-diary.md", "logs/memory-index.md", "logs/scheduled-audit.md"]
LOOP_FRESHNESS_REPORTS = {"PRECODE-HELP.md", "PROGRESS.md", "OS-HEALTH.md", "logs/bead-build-journal.md", "logs/learning-diary.md", "logs/memory-index.md", "logs/scheduled-audit.md"}
GENERATED_JSON_FAMILIES = {
    "logs/*.json",
    "logs/*.jsonl",
    "logs/check-output/*",
    "logs/scheduled-audit-output/*",
}
LOCAL_HYGIENE_RETENTION_DAYS = 90
LOCAL_HYGIENE_BULKY_LOG_DIRS = {"logs/check-output", "logs/scheduled-audit-output"}
LOCAL_HYGIENE_EXPECTED_LOG_FILES = {
    "logs/LOG-EVIDENCE-TAXONOMY.md",
    "logs/adapter-index.json",
    "logs/agent-spend.jsonl",
    "logs/authority-map.json",
    "logs/bead-build-journal.jsonl",
    "logs/bead-build-journal.md",
    "logs/bead-transitions.jsonl",
    "logs/check-results.jsonl",
    "logs/file-inventory.json",
    "logs/github-source-intake.jsonl",
    "logs/github-source-intake.md",
    "logs/goal-frame.json",
    "logs/handoff-packet.json",
    "logs/handoff-packet.md",
    "logs/handoffs.jsonl",
    "logs/learning-diary.jsonl",
    "logs/learning-diary.md",
    "logs/local-hygiene-preview.json",
    "logs/local-hygiene-preview.md",
    "logs/next-step.json",
    "logs/long-horizon-map.json",
    "logs/loop-runs.jsonl",
    "logs/memory-index.json",
    "logs/memory-index.md",
    "logs/orchestration-map.json",
    "logs/os-events.jsonl",
    "logs/os-health.json",
    "logs/pattern-guidance.json",
    "logs/progress.json",
    "logs/readiness.json",
    "logs/run-contract.json",
    "logs/run-contract.yaml",
    "logs/scheduled-audit.json",
    "logs/scheduled-audit.md",
    "logs/shim-index.json",
    "logs/tool-runs.jsonl",
    "logs/workflow-map.json",
}
LOCAL_HYGIENE_CACHE_NAMES = {
    ".cache",
    ".next",
    ".nuxt",
    ".parcel-cache",
    ".pytest_cache",
    ".ruff_cache",
    ".turbo",
    ".venv",
    ".vite",
    "__pycache__",
    "build",
    "coverage",
    "dist",
    "node_modules",
    "target",
}
LONG_TERM_QUESTION_TERMS = {"roadmap", "someday", "eventually", "long-term", "future", "nice to have", "maybe later"}
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
RUN_CONTRACT_PROOF_LANES = VERIFICATION_TIERS
RUN_CONTRACT_REQUIRED_REASONS = {
    "bounded_afk",
    "sensitive_surface",
    "external_mutation",
    "destructive",
}
COMMAND_DESTRUCTIVE_TERMS = {
    "rm ",
    "rm -rf",
    "remove ",
    "delete ",
    "reset --hard",
    "git reset --hard",
    "git clean",
    "drop table",
    "drop database",
    "truncate table",
    "delete production",
    "destroy",
    "force push",
    "push --force",
    "git push --force",
    "rollback production",
}
COMMAND_SENSITIVE_TERMS = {
    "secret",
    "token",
    "credential",
    "password",
    "env ",
    ".env",
    "auth",
    "oauth",
    "permission",
    "permissions",
    "payment",
    "billing",
    "stripe",
    "migration",
    "migrate",
    "database",
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
    "merge",
    "release",
    "publish",
    "gh pr merge",
    "gh issue edit",
    "gh pr comment",
    "gh label",
    "gh workflow run",
    "vercel",
    "supabase",
    "stripe",
}
COMMAND_LOCAL_MUTATION_TERMS = {"apply_patch", "write", "edit", "mv ", "cp ", "npm install", "pip install", "migration", "migrate"}
COMMAND_VERIFICATION_TERMS = {"test", "check", "validate", "lint", "py_compile", "typecheck", "pytest", "vitest", "jest"}
COMMAND_GENERATED_REFRESH_TERMS = {"os-health", "next-step", "file-inventory", "memory-index", "scheduled-audit"}
WORKFLOW_GENERATED_REPORTS = {"OS-HEALTH.md", "PROGRESS.md", "logs/learning-diary.md", "logs/scheduled-audit.md"}
LONG_HORIZON_TERMS = {"backlog", "roadmap", "milestone", "someday", "future", "later", "nice to have", "parking lot"}
LONG_HORIZON_REVISIT_TERMS = {"revisit", "after", "when", "until", "owner", "decision", "prd", "bead", "manual", "external", "defer", "deferred"}
PATTERN_GENERATED_REPORTS = WORKFLOW_GENERATED_REPORTS | {"logs/pattern-guidance.json"}
PATTERN_TERM_GROUPS = {
    "external_service": {
        "stripe",
        "github",
        "email",
        "resend",
        "ai",
        "openai",
        "api provider",
        "webhook",
        "external service",
        "third-party",
        "external integration",
    },
    "state_flow": {
        "status change",
        "state change",
        "state flow",
        "state machine",
        "step",
        "approval flow",
        "approved state",
        "rejected state",
        "transition",
        "wizard",
        "queue",
        "multi-step",
    },
    "strategy": {
        "mode",
        "provider",
        "rule",
        "policy",
        "variant",
        "pricing rule",
        "routing rule",
        "configuration",
        "interchangeable",
    },
    "audit_trail": {
        "audit",
        "history",
        "who did",
        "irreversible",
        "record action",
        "ledger",
        "audit log",
        "compliance",
    },
    "auth_access": {
        "auth",
        "login",
        "role-based",
        "permission",
        "permissions",
        "permission",
        "access",
        "security",
        "personal data",
    },
    "simple_change": {
        "copy",
        "text",
        "styling",
        "color",
        "css",
        "typo",
        "label",
        "spacing",
    },
}
PATTERN_NAME_TERMS = {
    "factory",
    "builder pattern",
    "provider",
    "adapter",
    "facade",
    "strategy",
    "command pattern",
    "observer",
    "state machine",
    "pipeline",
    "middleware",
}
MEMORY_CATEGORIES = {
    "lesson",
    "user_preference",
    "project_glossary",
    "recurring_risk",
    "tool_agent_note",
    "unresolved_theme",
    "source_pointer",
}
MEMORY_CONFIDENCE = {"high", "medium", "low"}
MEMORY_FRESHNESS = {"current", "watch", "stale", "superseded"}
MEMORY_STATUS = {"reviewed", "needs_promotion", "superseded", "archived"}
MEMORY_SECRET_TERMS = {"api_key", "api key", "token", "password", "secret", "credential", "private key"}
MEMORY_AUTHORITY_TERMS = {"must implement", "next task", "active memory", "approve transition", "decision:"}
GOAL_FRAME_STATUSES = {"draft", "active", "reaffirm_needed", "retired"}
GOAL_FRAME_HORIZONS = {"session", "feature", "product"}
GOAL_FRAME_WORKFLOWS = {"intake", "PRD", "prd", "decomposition", "implementation", "review", "repair", "long-horizon"}
GOAL_FRAME_REQUIRED_FIELDS = {
    "status",
    "last_reaffirmed",
    "horizon",
    "workflow_guidance",
    "goal",
    "why_now",
    "success_signal",
    "out_of_scope",
    "approval_gates",
    "reaffirmation_trigger",
}
GOAL_FRAME_TASKLIKE_TERMS = {
    "backlog",
    "roadmap",
    "task list",
    "next task",
    "activate",
    "approve transition",
    "implement ",
    "build ",
    "ship ",
}


@dataclass
class BeadRecord:
    rel_path: str
    title: str
    bead_id: str
    status: str
    execution_mode: str
    bead_kind: str
    primary_authority: str
    depends_on: list[str]
    parent_prd: str
    requirement_ids: list[str]
    files_in_play: list[str]
    checks: list[str]
    verification_type: list[str]
    delegation_mode: str
    test_strategy: str
    review_context: str
    complexity: str
    required_planning_depth: str
    autonomy_level: str
    run_contract: dict[str, Any]
    closeout: dict[str, str]
    handback: str
    frontmatter: dict[str, Any]
    sections: dict[str, str]


def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def rel_path(path: Path, root: Path) -> str:
    return path.relative_to(root).as_posix()


def normalize_status(value: str) -> str:
    return value.lower().strip().replace("-", "_").replace(" ", "_")


def normalize_optional(value: str | None) -> str:
    cleaned = strip_inline_code(value or "")
    return "" if cleaned.lower() in FRONTMATTER_EMPTY_MARKERS else cleaned


def normalize_list(items: list[Any] | None) -> list[str]:
    values: list[str] = []
    for item in items or []:
        value = strip_inline_code(str(item))
        if not value or value.lower() in FRONTMATTER_EMPTY_MARKERS:
            continue
        values.append(value)
    return values


def split_list_value(value: Any) -> list[str]:
    if isinstance(value, list):
        return normalize_list(value)
    text = strip_inline_code(str(value or ""))
    if not text or text.lower() in FRONTMATTER_EMPTY_MARKERS:
        return []
    if "\n" in text:
        return normalize_list([line.strip().removeprefix("-").strip() for line in text.splitlines()])
    return normalize_list([item.strip() for item in re.split(r",|;", text)])


def normalize_bool(value: Any) -> bool:
    if isinstance(value, bool):
        return value
    return str(value or "").strip().lower() in {"true", "yes", "required", "enabled"}


def number_or_none(value: Any) -> float | None:
    if value is None or value == "":
        return None
    if isinstance(value, (int, float)):
        return float(value)
    try:
        return float(str(value))
    except ValueError:
        return None


def int_or_none(value: Any) -> int | None:
    number = number_or_none(value)
    return int(number) if number is not None else None


def normalize_inline_status_value(value: str) -> str:
    if value.startswith("not needed while status is `") and not value.endswith("`"):
        return value + "`"
    return value


def heading_title(text: str) -> str:
    _, body = split_frontmatter(text)
    for line in body.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return ""


def parse_next_bead_reference(value: str, root: Path) -> str | None:
    if not value:
        return None

    path_match = re.search(r"`?(tasks/beads/[^`\s)]+\.md)`?", value)
    if path_match:
        candidate = path_match.group(1)
        if (root / candidate).is_file():
            return candidate

    id_match = re.search(r"\b(B\d{3})\b", value)
    if not id_match:
        return None

    bead_id = id_match.group(1).lower()
    matches = [
        path for path in (root / "tasks" / "beads").glob("*.md")
        if path.name.lower().startswith(f"{bead_id}-")
    ]
    if not matches:
        return None
    return rel_path(sorted(matches)[0], root)


def bead_paths(root: Path) -> list[Path]:
    return sorted(path for path in (root / "tasks" / "beads").glob("*.md") if path.name != "BEAD-SCHEMA.md")


def parse_closeout_values(section: str) -> dict[str, str]:
    return colon_bullets(section)


def normalize_run_contract(raw: Any, section: str, bead_defaults: dict[str, Any]) -> dict[str, Any]:
    section_values = colon_bullets(section)
    data = raw if isinstance(raw, dict) else {}

    def field(name: str, *aliases: str) -> Any:
        for key in (name, *aliases):
            if key in data:
                return data.get(key)
            normalized = re.sub(r"[^a-z0-9]+", "_", key.strip().lower()).strip("_")
            if normalized in section_values:
                return section_values.get(normalized)
        return None

    allowed_paths = split_list_value(field("allowed_paths", "allowed files", "allowed actions")) or list(
        bead_defaults.get("files_in_play") or []
    )
    proof_needed = split_list_value(field("proof_needed", "proof lanes", "proof required"))
    allowed_tool_classes = split_list_value(field("allowed_tool_classes", "allowed tool classes"))
    approval_required_before = split_list_value(field("approval_required_before", "approval gates"))
    stop_if = split_list_value(field("stop_if", "stop conditions")) or split_list_value(bead_defaults.get("stop_if"))
    forbidden_actions = split_list_value(field("forbidden_actions", "forbidden commands", "forbidden"))

    required_raw = field("required")
    required = normalize_bool(required_raw) if required_raw is not None else False

    has_contract = bool(data or section.strip() or required or proof_needed or allowed_tool_classes or approval_required_before)
    return {
        "present": has_contract,
        "required": required,
        "required_reasons": [],
        "allowed_paths": allowed_paths,
        "allowed_tool_classes": allowed_tool_classes,
        "forbidden_actions": forbidden_actions,
        "approval_required_before": approval_required_before,
        "proof_needed": [item.lower() for item in proof_needed],
        "stop_if": stop_if,
        "rollback_or_blocked_escape": normalize_optional(
            str(field("rollback_or_blocked_escape", "rollback", "blocked escape") or "")
        ),
        "expires_when": normalize_optional(str(field("expires_when", "expiration", "lease expires when") or "")),
        "advisory_only": True,
    }


def read_bead(path: Path, root: Path) -> BeadRecord:
    text = read_text(path)
    doc = MarkdownDocument.load(path)
    state_values = colon_bullets(doc.sections.get("State", ""))

    bead_id = normalize_optional(str(doc.frontmatter.get("bead_id") or state_values.get("id") or path.stem.split("-", 1)[0]))
    status = normalize_status(
        normalize_optional(str(doc.frontmatter.get("status") or state_values.get("status") or "missing"))
    )
    execution_mode = normalize_optional(str(doc.frontmatter.get("execution_mode") or state_values.get("execution_mode") or ""))
    bead_kind = normalize_optional(str(doc.frontmatter.get("bead_kind") or "implementation")) or "implementation"
    primary_authority = normalize_optional(
        str(doc.frontmatter.get("primary_authority") or first_bullet(doc.sections.get("Primary Authority", "")) or "")
    )
    depends_on = normalize_list(doc.frontmatter.get("depends_on")) or normalize_list(bullet_items(doc.sections.get("Depends On", "")))
    parent_prd = normalize_optional(
        str(doc.frontmatter.get("parent_prd") or first_bullet(doc.sections.get("Parent PRD", "")) or "")
    )
    requirement_ids = normalize_list(doc.frontmatter.get("requirement_ids")) or normalize_list(
        bullet_items(doc.sections.get("Requirement IDs", ""))
    )
    files_in_play = normalize_list(doc.frontmatter.get("files_in_play")) or normalize_list(
        bullet_items(doc.sections.get("Files In Play", ""))
    )
    checks = normalize_list(doc.frontmatter.get("checks")) or normalize_list(bullet_items(doc.sections.get("Checks", "")))
    verification_type = normalize_list(doc.frontmatter.get("verification_type")) or normalize_list(
        bullet_items(doc.sections.get("Verification Type", ""))
    )
    delegation_mode = normalize_optional(
        str(doc.frontmatter.get("delegation_mode") or first_bullet(doc.sections.get("Delegation Mode", "")) or "")
    )
    test_strategy = normalize_optional(
        str(doc.frontmatter.get("test_strategy") or first_bullet(doc.sections.get("Test Strategy", "")) or "")
    )
    review_context = normalize_optional(
        str(doc.frontmatter.get("review_context") or first_bullet(doc.sections.get("Review Context", "")) or "")
    )
    complexity = normalize_optional(
        str(doc.frontmatter.get("complexity") or first_bullet(doc.sections.get("Complexity", "")) or "")
    )
    required_planning_depth = normalize_optional(
        str(
            doc.frontmatter.get("required_planning_depth")
            or first_bullet(doc.sections.get("Required Planning Depth", ""))
            or ""
        )
    )
    autonomy_level = normalize_optional(
        str(doc.frontmatter.get("autonomy_level") or first_bullet(doc.sections.get("Autonomy Level", "")) or "")
    )
    run_contract = normalize_run_contract(
        doc.frontmatter.get("run_contract"),
        doc.sections.get("Run Contract", ""),
        {
            "files_in_play": files_in_play,
            "stop_if": doc.sections.get("Stop If", ""),
        },
    )

    return BeadRecord(
        rel_path=rel_path(path, root),
        title=heading_title(text),
        bead_id=bead_id,
        status=status,
        execution_mode=execution_mode,
        bead_kind=bead_kind,
        primary_authority=primary_authority,
        depends_on=depends_on,
        parent_prd=parent_prd,
        requirement_ids=requirement_ids,
        files_in_play=files_in_play,
        checks=checks,
        verification_type=verification_type,
        delegation_mode=delegation_mode,
        test_strategy=test_strategy,
        review_context=review_context,
        complexity=complexity,
        required_planning_depth=required_planning_depth,
        autonomy_level=autonomy_level,
        run_contract=run_contract,
        closeout=parse_closeout_values(doc.sections.get("Closeout Evidence", "")),
        handback=doc.sections.get("Handback", ""),
        frontmatter=doc.frontmatter,
        sections=doc.sections,
    )


def read_todo_state(root: Path) -> dict[str, Any]:
    todo_path = root / "tasks" / "todo.md"
    doc = MarkdownDocument.load(todo_path)
    current_bead = normalize_optional(
        str(doc.frontmatter.get("current_bead") or first_bullet(doc.sections.get("Current Bead", "")) or "")
    )
    primary_authority = normalize_optional(
        str(doc.frontmatter.get("primary_authority") or first_bullet(doc.sections.get("Primary Authority File", "")) or "")
    )
    state_values = colon_bullets(doc.sections.get("Current Bead", ""))
    return {
        "path": "tasks/todo.md",
        "frontmatter": doc.frontmatter,
        "sections": doc.sections,
        "current_bead": current_bead,
        "current_state": normalize_status(str(doc.frontmatter.get("current_state") or state_values.get("state") or "")),
        "build_lane": normalize_optional(str(doc.frontmatter.get("build_lane") or state_values.get("build_lane") or "")),
        "active_feature_window": normalize_optional(
            str(doc.frontmatter.get("active_feature_window") or state_values.get("active_feature_window") or "")
        ),
        "primary_authority": primary_authority,
    }


def goal_frame_candidate_paths(root: Path) -> list[Path]:
    paths: list[Path] = []
    for rel in ("PRODUCT.md", "DECISIONS.md"):
        path = root / rel
        if path.is_file():
            paths.append(path)
    paths.extend(sorted((root / "tasks" / "prds").glob("*.md")))
    paths.extend(bead_paths(root))
    return paths


def normalize_goal_frame_status(value: str) -> str:
    status = normalize_status(value or "draft")
    return status if status in GOAL_FRAME_STATUSES else status or "draft"


def parse_goal_frame(path: Path, root: Path) -> dict[str, Any] | None:
    doc = MarkdownDocument.load(path)
    section = doc.sections.get("Goal Frame", "")
    if not section:
        return None

    values = colon_bullets(section)
    rel = rel_path(path, root)
    status = normalize_goal_frame_status(values.get("status", "draft"))
    frame = {
        "path": rel,
        "title": heading_title(read_text(path)),
        "status": status,
        "last_reaffirmed": normalize_optional(values.get("last_reaffirmed", "")),
        "owner_file": normalize_optional(values.get("owner_file", rel)) or rel,
        "horizon": normalize_optional(values.get("horizon", "")),
        "workflow_guidance": normalize_optional(values.get("workflow_guidance", "")),
        "goal": normalize_optional(values.get("goal", "")),
        "why_now": normalize_optional(values.get("why_now", "")),
        "success_signal": normalize_optional(values.get("success_signal", "")),
        "out_of_scope": normalize_optional(values.get("out_of_scope", "")),
        "approval_gates": normalize_optional(values.get("approval_gates", "")),
        "reaffirmation_trigger": normalize_optional(values.get("reaffirmation_trigger", "")),
        "section": section,
    }
    frame["missing_fields"] = sorted(
        key for key in GOAL_FRAME_REQUIRED_FIELDS
        if not normalize_optional(str(frame.get(key) or ""))
    )
    return frame


def goal_frame_tasklike_warnings(frame: dict[str, Any]) -> list[str]:
    if frame.get("status") not in {"active", "reaffirm_needed"}:
        return []
    text = str(frame.get("section") or "").lower()
    found = sorted(term.strip() for term in GOAL_FRAME_TASKLIKE_TERMS if term in text)
    if not found:
        return []
    return [f"{frame.get('path')} Goal Frame may be acting like a task list or roadmap ({', '.join(found[:4])})"]


def goal_frame_summary(root: Path, current_bead: BeadRecord | None) -> dict[str, Any]:
    frames = [frame for path in goal_frame_candidate_paths(root) if (frame := parse_goal_frame(path, root))]
    warnings: list[str] = []

    for frame in frames:
        status = str(frame.get("status") or "draft")
        if status not in GOAL_FRAME_STATUSES:
            warnings.append(f"{frame.get('path')} Goal Frame has unknown status `{status}`")
        if frame.get("horizon") and frame.get("horizon") not in GOAL_FRAME_HORIZONS:
            warnings.append(f"{frame.get('path')} Goal Frame has unknown horizon `{frame.get('horizon')}`")
        if frame.get("workflow_guidance") and frame.get("workflow_guidance") not in GOAL_FRAME_WORKFLOWS:
            warnings.append(
                f"{frame.get('path')} Goal Frame has unknown workflow guidance `{frame.get('workflow_guidance')}`"
            )
        if status in {"active", "reaffirm_needed"}:
            missing = frame.get("missing_fields") or []
            if missing:
                warnings.append(f"{frame.get('path')} Goal Frame is missing required fields: {', '.join(missing)}")
        if status == "active" and not frame.get("last_reaffirmed"):
            warnings.append(f"{frame.get('path')} Goal Frame is active but has no last reaffirmed date")
        if status == "active" and not frame.get("reaffirmation_trigger"):
            warnings.append(f"{frame.get('path')} Goal Frame is active but has no reaffirmation trigger")
        if status == "reaffirm_needed":
            warnings.append(f"{frame.get('path')} Goal Frame requires user reaffirmation before guiding workflow")
        if current_bead and status == "active" and frame.get("path") == current_bead.rel_path and current_bead.status in {
            "review",
            "done",
            "needs_info",
            "manual_testing",
        }:
            warnings.append(
                f"{frame.get('path')} Goal Frame should be reaffirmed because the active bead is `{current_bead.status}`"
            )
        warnings.extend(goal_frame_tasklike_warnings(frame))

    current: dict[str, Any] | None = None
    active_frames = [frame for frame in frames if frame.get("status") == "active"]
    if current_bead:
        current = next((frame for frame in active_frames if frame.get("path") == current_bead.rel_path), None)
        if not current and current_bead.parent_prd:
            current = next((frame for frame in active_frames if frame.get("path") == current_bead.parent_prd), None)
    if not current:
        current = next((frame for frame in active_frames if frame.get("path") == "PRODUCT.md"), None)
    if not current:
        current = next((frame for frame in active_frames), None)
    if not current:
        current = next((frame for frame in frames if frame.get("status") == "reaffirm_needed"), None)

    if current and current.get("status") == "active" and any(
        warning.startswith(str(current.get("path"))) for warning in warnings
    ):
        current = {**current, "status": "reaffirm_needed"}

    return {
        "status": "warning" if warnings else "pass",
        "warnings": warnings,
        "details": {
            "current": {key: value for key, value in (current or {}).items() if key != "section"},
            "frames": [{key: value for key, value in frame.items() if key != "section"} for frame in frames],
            "frame_count": len(frames),
            "active_count": len(active_frames),
            "advisory_only": True,
            "generated_report_warning": "Goal Frame summaries are generated evidence only; they must not choose tasks, approve PRDs, activate beads, or override active memory.",
        },
    }


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    if not path.is_file():
        return []
    rows: list[dict[str, Any]] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        try:
            rows.append(json.loads(line))
        except json.JSONDecodeError:
            continue
    return rows


def run_git(args: list[str], root: Path) -> str:
    result = subprocess.run(
        ["git", *args],
        cwd=root,
        check=False,
        capture_output=True,
        text=True,
    )
    return result.stdout.strip()


def parse_check_command(raw: str) -> dict[str, str]:
    cwd = "."
    cwd_match = re.search(r"--cwd\s+([^\s]+)", raw)
    if cwd_match:
        cwd = cwd_match.group(1)

    command = raw
    if " -- " in raw:
        command = raw.split(" -- ", 1)[1]
    return {"command": command.strip(), "cwd": cwd, "source": raw.strip()}


def latest_by_command(rows: list[dict[str, Any]], bead: str | None) -> dict[tuple[str, str], dict[str, Any]]:
    latest: dict[tuple[str, str], dict[str, Any]] = {}
    for row in rows:
        if bead and row.get("bead") != bead:
            continue
        command = str(row.get("command") or "")
        cwd = str(row.get("cwd") or ".")
        if command:
            latest[(command, cwd)] = row
            latest[(command, ".")] = row
    return latest


def check_rows_for_bead(bead: BeadRecord, latest: dict[tuple[str, str], dict[str, Any]]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for raw_check in bead.checks:
        check = parse_check_command(raw_check)
        key = (check["command"], check["cwd"])
        result = latest.get(key) or latest.get((check["command"], "."))
        rows.append(
            {
                "source": check["source"],
                "command": check["command"],
                "cwd": check["cwd"],
                "status": result.get("status") if result else "missing",
                "exit_code": result.get("exit_code") if result else None,
                "timestamp": result.get("timestamp") if result else None,
                "output": result.get("output") if result else None,
            }
        )
    return rows


def manual_verification_clear(value: str) -> bool:
    normalized = value.lower().strip()
    if not normalized:
        return False
    if "not applicable" in normalized or normalized == "n/a":
        return True
    return not any(marker in normalized for marker in PENDING_MARKERS)


def review_decision_accepted(value: str) -> bool:
    normalized = value.lower()
    return any(marker in normalized for marker in APPROVED_MARKERS)


def review_decision_valid(value: str) -> bool:
    normalized = normalize_optional(value).lower()
    return any(term in normalized for term in ("accepted", "revise", "split", "blocked"))


def changed_path_name(raw: str) -> str:
    value = raw.strip()
    if not value:
        return ""
    if " -> " in value:
        value = value.split(" -> ", 1)[1]
    parts = value.split(maxsplit=1)
    return parts[1] if len(parts) == 2 else value


def looks_code_path(path: str) -> bool:
    suffix = Path(path).suffix.lower()
    if suffix in CODE_EXTENSIONS:
        return True
    return path.startswith(("scripts/", "app/", "src/", "lib/", "server/", "client/"))


def check_tiers(commands: list[str]) -> set[str]:
    tiers: set[str] = set()
    for command in commands:
        lower = command.lower()
        if any(term in lower for term in ("validate", "lint", "typecheck", "py_compile", "bash -n", "shellcheck", "tsc")):
            tiers.add("static")
        if any(term in lower for term in ("unit", "pytest", "vitest", "jest", "cargo test", "go test")):
            tiers.add("unit")
        if any(term in lower for term in ("integration", "e2e", "api", "db", "database")):
            tiers.add("integration")
        if any(term in lower for term in ("playwright", "browser", "cypress")):
            tiers.add("browser")
    return tiers


def manual_verification_structured(value: str) -> bool:
    normalized = value.lower()
    if not manual_verification_clear(value):
        return False
    if "not applicable" in normalized or normalized.strip() == "n/a":
        return True
    required = ("who checked", "what was checked", "environment", "result", "remaining uncertainty")
    return all(field in normalized for field in required)


def evidence_quality(root: Path, bead: BeadRecord | None, check_results: list[dict[str, Any]], changed: list[str]) -> dict[str, Any]:
    warnings: list[str] = []
    details: dict[str, Any] = {}
    if bead is None:
        return {"status": "warning", "warnings": ["current bead is missing"], "details": details}

    changed_names = [changed_path_name(item) for item in changed]
    changed_names = [item for item in changed_names if item]
    files_in_play = set(bead.files_in_play)
    outside_files = [
        path
        for path in changed_names
        if not any(path_matches_scope(path, item) for item in files_in_play)
        and not path.startswith("logs/")
        and path not in {"OS-HEALTH.md", "PROGRESS.md"}
    ]
    code_changing = any(looks_code_path(path) for path in changed_names + bead.files_in_play)
    bead_rows = [row for row in check_results if row.get("bead") == bead.rel_path]
    passing_commands = [str(row.get("command") or "") for row in bead_rows if row.get("status") == "pass"]
    tier_set = set(tier.lower() for tier in bead.verification_type)
    inferred_tiers = check_tiers(passing_commands)
    known_tiers = sorted((tier_set & VERIFICATION_TIERS) | inferred_tiers)
    kind = bead.bead_kind.lower().strip()
    risk_level = str(bead.frontmatter.get("risk_level") or "").lower().strip()

    if code_changing and passing_commands and set(passing_commands) <= {"bash scripts/validate-memory.sh"}:
        warnings.append("only memory validation is recorded for a code-changing bead")
    if code_changing and not bead.test_strategy:
        warnings.append("code-changing bead should declare test_strategy")
    if bead.test_strategy and bead.test_strategy not in TEST_STRATEGIES:
        warnings.append(f"test_strategy has an unknown value: {bead.test_strategy}")
    if bead.review_context and bead.review_context not in REVIEW_CONTEXTS:
        warnings.append(f"review_context has an unknown value: {bead.review_context}")
    if kind in IMPLEMENTATION_BEAD_KINDS and risk_level == "medium" and bead.review_context not in {"fresh_context_recommended", "fresh_context_required"}:
        warnings.append("medium-risk implementation bead should recommend fresh-context review")
    if kind in IMPLEMENTATION_BEAD_KINDS and risk_level == "high" and bead.review_context != "fresh_context_required":
        warnings.append("high-risk implementation bead should require fresh-context review")
    if not manual_verification_structured(bead.closeout.get("manual_verification", "")):
        warnings.append("manual verification is missing, pending, or does not use the stable format")
    if not review_decision_accepted(bead.closeout.get("review_decision", "")):
        warnings.append("review decision is not accepted")
    if outside_files:
        warnings.append(f"active changes appear outside files_in_play: {outside_files[:8]}")

    combined_text = "\n".join(
        [
            bead.bead_kind,
            bead.primary_authority,
            " ".join(bead.verification_type),
            "\n".join(bead.checks),
            "\n".join(bead.files_in_play),
            " ".join(bead.closeout.values()),
            " ".join(bead.sections.values()),
        ]
    ).lower()
    sensitive = any(term in combined_text for term in SENSITIVE_SURFACE_TERMS)
    if sensitive:
        approval_present = "approval" in combined_text or "approved" in combined_text
        rollback_present = "rollback" in combined_text or "escape" in combined_text or "unblocker" in combined_text
        if not approval_present:
            warnings.append("sensitive-surface work lacks an explicit approval note")
        if not rollback_present:
            warnings.append("sensitive-surface work lacks rollback, blocked escape, or unblocker guidance")

    details = {
        "bead": bead.rel_path,
        "verification_type": bead.verification_type,
        "test_strategy": bead.test_strategy,
        "review_context": bead.review_context,
        "risk_level": risk_level,
        "known_tiers": known_tiers,
        "code_changing": code_changing,
        "recorded_pass_commands": passing_commands,
        "changed_outside_files_in_play": outside_files,
        "sensitive_surface_detected": sensitive,
    }
    return {"status": "warning" if warnings else "pass", "warnings": warnings, "details": details}


def run_contract_required_reasons(bead: BeadRecord) -> list[str]:
    combined_text = " ".join(
        [
            bead.bead_kind,
            bead.primary_authority,
            " ".join(bead.files_in_play),
            " ".join(bead.checks),
            " ".join(bead.verification_type),
            bead.sections.get("Objective", ""),
            bead.sections.get("Done When", ""),
            bead.sections.get("Stop If", ""),
            bead.handback,
        ]
    ).lower()
    reasons: list[str] = []
    if bead.autonomy_level == "bounded-afk" or bead.delegation_mode == "afk_candidate":
        reasons.append("bounded_afk")
    if any(term in combined_text for term in SENSITIVE_SURFACE_TERMS):
        reasons.append("sensitive_surface")
    if any(term in combined_text for term in COMMAND_EXTERNAL_MUTATION_TERMS):
        reasons.append("external_mutation")
    if any(term in combined_text for term in COMMAND_DESTRUCTIVE_TERMS):
        reasons.append("destructive")
    return sorted(set(reasons))


def run_contract_quality(bead: BeadRecord | None, check_results: list[dict[str, Any]]) -> dict[str, Any]:
    warnings: list[str] = []
    if bead is None:
        return {"status": "warning", "warnings": ["current bead is missing"], "details": {"present": False}}

    contract = dict(bead.run_contract or {})
    reasons = run_contract_required_reasons(bead)
    present = bool(contract.get("present"))
    required = bool(reasons or contract.get("required"))
    contract["required"] = required
    contract["required_reasons"] = reasons

    if required and not present:
        warnings.append("run contract is required for this bead's risk, but no Run Contract section or frontmatter exists")

    if present:
        allowed_paths = contract.get("allowed_paths") or []
        too_broad_paths = [
            path
            for path in allowed_paths
            if path.strip() in {".", "./", "*", "/*"}
            or path.strip().endswith("/*")
            or (path.strip().endswith("/") and path.strip().rstrip("/") not in {item.rstrip("/") for item in bead.files_in_play})
        ]
        outside_paths = [
            path
            for path in allowed_paths
            if not any(path_matches_scope(path, item) or path_matches_scope(item, path) for item in bead.files_in_play)
        ]
        if too_broad_paths:
            warnings.append(f"run contract allowed actions are too broad: {too_broad_paths[:6]}")
        if outside_paths:
            warnings.append(f"run contract allowed paths are outside files_in_play: {outside_paths[:6]}")
        if required and not allowed_paths:
            warnings.append("run contract should name allowed actions or paths")
        allowed_tool_classes = contract.get("allowed_tool_classes") or []
        unknown_tool_classes = [item for item in allowed_tool_classes if item not in TOOL_CLASSES]
        if unknown_tool_classes:
            warnings.append(f"run contract has unknown allowed tool classes: {unknown_tool_classes[:6]}")
        approval_required = contract.get("approval_required_before") or []
        if any(reason in reasons for reason in ("sensitive_surface", "external_mutation", "destructive")) and not approval_required:
            warnings.append("run contract should name what requires approval before risky action")
        proof_needed = contract.get("proof_needed") or []
        unknown_proof = [item for item in proof_needed if item not in RUN_CONTRACT_PROOF_LANES]
        if unknown_proof:
            warnings.append(f"run contract has unknown proof needed lanes: {unknown_proof[:6]}")
        bead_rows = [row for row in check_results if row.get("bead") == bead.rel_path]
        passing_commands = [str(row.get("command") or "") for row in bead_rows if row.get("status") == "pass"]
        known_tiers = set(bead.verification_type) | check_tiers(passing_commands)
        if manual_verification_structured(bead.closeout.get("manual_verification", "")):
            known_tiers.add("manual")
        missing_proof = [lane for lane in proof_needed if lane in RUN_CONTRACT_PROOF_LANES and lane not in known_tiers]
        if missing_proof:
            warnings.append(f"run contract proof needed is not reflected in verification type, checks, or closeout: {missing_proof[:6]}")
        rollback = str(contract.get("rollback_or_blocked_escape") or bead.closeout.get("blocked_escape") or "").lower()
        if any(reason in reasons for reason in ("sensitive_surface", "external_mutation", "destructive")) and not any(
            term in rollback for term in ("rollback", "escape", "unblocker", "not applicable")
        ):
            warnings.append("run contract should name rollback, blocked escape, unblocker, or why rollback is not applicable")
        if required and not contract.get("expires_when"):
            warnings.append("run contract should say when the allowed actions expire")

    if warnings:
        if any("approval" in warning or "destructive" in warning for warning in warnings):
            user_decision = "approval needed"
        elif any("required" in warning or "outside" in warning or "too broad" in warning for warning in warnings):
            user_decision = "stop"
        else:
            user_decision = "ask for proof"
        summary = "The bead needs clearer allowed actions, proof, approval, or recovery before risky work continues."
    else:
        user_decision = "continue"
        summary = "No run-contract warnings apply to this bead."

    return {
        "status": "warning" if warnings else "pass",
        "warnings": warnings,
        "details": {
            "current_bead": bead.rel_path,
            "present": present,
            "required": required,
            "required_reasons": reasons,
            "contract": contract,
            "plain_english_summary": summary,
            "user_decision": user_decision,
            "why_this_matters": "Risk-triggered run contracts make allowed actions and proof needed explicit before high-risk work proceeds.",
            "stop_if": "Stop if allowed actions, proof needed, approval gates, or rollback/escape path are unclear.",
            "approval_prompt": "Ask the user to approve the exact risky action only after allowed actions, proof needed, and recovery path are named.",
            "advisory_only": True,
        },
    }


def decomposition_quality(bead: BeadRecord | None) -> dict[str, Any]:
    warnings: list[str] = []
    details: dict[str, Any] = {}
    if bead is None:
        return {"status": "warning", "warnings": ["current bead is missing"], "details": details}

    done_when = bead.sections.get("Done When", "")
    stop_if = bead.sections.get("Stop If", "")
    handback = bead.handback or ""
    kind = bead.bead_kind.lower().strip()
    files = bead.files_in_play
    code_files = [path for path in files if looks_code_path(path)]
    broad_files = [
        path
        for path in files
        if path.strip() in {".", "./", "*", "/*", "tasks", "tasks/", "scripts", "scripts/"}
        or path.strip().endswith("/")
        or path.strip().endswith("/*")
    ]
    supporting_authority_hints = [
        path
        for path in files
        if path in {"ARCHITECTURE.md", "API.md", "DATA-MODELS.md", "SECURITY.md", "ACCEPTANCE.md", "PROJECT-CONTEXT.md"}
        and path != bead.primary_authority
    ]

    if len(files) > 20:
        warnings.append("files_in_play exceeds the 20-file operating limit")
    elif len(files) > 8:
        warnings.append("files_in_play is broad; consider whether the bead should split")
    if not bead.checks:
        warnings.append("checks are missing")
    if not bead.primary_authority:
        warnings.append("primary authority is missing")
    if bead.delegation_mode and bead.delegation_mode not in DELEGATION_MODES:
        warnings.append(f"delegation_mode has an unknown value: {bead.delegation_mode}")
    if bead.review_context and bead.review_context not in REVIEW_CONTEXTS:
        warnings.append(f"review_context has an unknown value: {bead.review_context}")
    if bead.test_strategy and bead.test_strategy not in TEST_STRATEGIES:
        warnings.append(f"test_strategy has an unknown value: {bead.test_strategy}")
    if bead.delegation_mode == "afk_candidate":
        if not files or len(files) > 8 or broad_files:
            warnings.append("afk_candidate bead should have bounded files_in_play")
        if not bead.checks:
            warnings.append("afk_candidate bead should list checks")
        if not stop_if.strip():
            warnings.append("afk_candidate bead should list stop conditions")
    if supporting_authority_hints:
        warnings.append(f"multiple apparent authority surfaces may be involved: {supporting_authority_hints[:6]}")
    if kind in IMPLEMENTATION_BEAD_KINDS and (not bead.parent_prd or bead.parent_prd == "none" or not bead.requirement_ids):
        warnings.append("implementation bead lacks PRD traceability or requirement IDs")
    if kind in PLANNING_BEAD_KINDS and code_files:
        warnings.append(f"planning bead appears to include implementation files: {code_files[:6]}")
    if not done_when.strip():
        warnings.append("Done When section is missing")
    else:
        normalized_done = done_when.lower()
        if any(term in normalized_done for term in VAGUE_DONE_TERMS):
            warnings.append("Done When language may be vague or contain multiple steps")
        if len([line for line in done_when.splitlines() if line.strip().startswith("-")]) > 5:
            warnings.append("Done When has many bullets; consider whether this is more than one outcome")
    dependency_text = "\n".join([stop_if, handback]).lower()
    if not bead.depends_on and any(term in dependency_text for term in DEPENDENCY_HINT_TERMS):
        warnings.append("dependency hints appear in Stop If or Handback but depends_on is empty")
    slice_text = "\n".join(
        [
            bead.title,
            bead.primary_authority,
            bead.sections.get("Objective", ""),
            done_when,
            handback,
        ]
    ).lower()
    if kind in IMPLEMENTATION_BEAD_KINDS and any(term in slice_text for term in USER_FACING_TERMS) and any(term in slice_text for term in HORIZONTAL_SLICE_TERMS):
        warnings.append("user-facing feature bead appears horizontal; prefer a first vertical slice with observable feedback")

    details = {
        "bead": bead.rel_path,
        "bead_kind": bead.bead_kind,
        "delegation_mode": bead.delegation_mode,
        "test_strategy": bead.test_strategy,
        "review_context": bead.review_context,
        "primary_authority": bead.primary_authority,
        "files_in_play_count": len(files),
        "broad_files_in_play": broad_files,
        "checks_count": len(bead.checks),
        "depends_on": bead.depends_on,
        "code_files_in_play": code_files,
        "supporting_authority_hints": supporting_authority_hints,
    }
    return {"status": "warning" if warnings else "pass", "warnings": warnings, "details": details}


def parse_iso_timestamp(value: Any) -> datetime | None:
    if not value:
        return None
    try:
        return datetime.fromisoformat(str(value).replace("Z", "+00:00"))
    except ValueError:
        return None


def file_mtime(path: Path) -> datetime | None:
    if not path.is_file():
        return None
    return datetime.fromtimestamp(path.stat().st_mtime, timezone.utc)


def active_memory_claims(root: Path) -> list[str]:
    agent = read_text(root / "AGENT.md")
    if "## Active Memory" not in agent:
        return []
    section = agent.split("## Active Memory", 1)[1].split("\n## ", 1)[0]
    return re.findall(r"^- `([^`]+)`", section, re.MULTILINE)


def generated_report_ok(path: Path) -> bool:
    text = read_text(path)
    return "> CLASS: generated" in text and "Do not use this file" in text


def state_integrity(root: Path, todo: dict[str, Any], bead: BeadRecord | None, beads: list[BeadRecord], events: list[dict[str, Any]]) -> dict[str, Any]:
    warnings: list[str] = []
    details: dict[str, Any] = {}

    in_progress = [item.rel_path for item in beads if item.status == "in_progress"]
    if len(in_progress) != 1:
        warnings.append(f"expected exactly one in_progress bead; found {in_progress or 'none'}")
    if todo.get("current_bead") not in in_progress:
        warnings.append(f"todo current_bead does not match in_progress bead: {todo.get('current_bead')} vs {in_progress or 'none'}")

    claims = active_memory_claims(root)
    if claims[:3] != ACTIVE_MEMORY:
        warnings.append("active-memory claims do not begin with the canonical three files")
    extra_claims = [item for item in claims if item.endswith(".md") and item not in ACTIVE_MEMORY]
    if extra_claims:
        warnings.append(f"possible extra active-memory markdown files: {extra_claims}")

    todo_sections = todo.get("sections") or {}
    todo_files = set(strip_inline_code(item) for item in bullet_items(str(todo_sections.get("Files In Play", ""))))
    todo_checks = set(strip_inline_code(item) for item in bullet_items(str(todo_sections.get("Checks To Run", ""))))
    todo_primary = str(todo.get("primary_authority") or "")

    if bead:
        if todo.get("current_state") != bead.status:
            warnings.append(f"todo current_state `{todo.get('current_state')}` does not match bead status `{bead.status}`")
        if todo_primary != bead.primary_authority:
            warnings.append(f"todo primary_authority `{todo_primary}` does not match bead primary authority `{bead.primary_authority}`")
        missing_files = [item for item in bead.files_in_play if item not in todo_files]
        missing_checks = [item for item in bead.checks if item not in todo_checks]
        if missing_files:
            warnings.append(f"todo Files In Play is missing active bead files: {missing_files[:8]}")
        if missing_checks:
            warnings.append(f"todo Checks To Run is missing active bead checks: {missing_checks[:8]}")

    open_questions = str(todo_sections.get("Open Questions", "")).lower()
    if any(term in open_questions for term in LONG_TERM_QUESTION_TERMS):
        warnings.append("tasks/todo.md Open Questions may contain long-term planning notes instead of current execution blockers")

    latest_event = None
    for event in events:
        event_time = parse_iso_timestamp(event.get("timestamp"))
        if event_time and (latest_event is None or event_time > latest_event):
            latest_event = event_time

    report_details: dict[str, Any] = {}
    for rel in GENERATED_REPORTS:
        path = root / rel
        mtime = file_mtime(path)
        status = "pass"
        if not path.is_file():
            status = "missing"
            warnings.append(f"generated report is missing: {rel}")
        elif not generated_report_ok(path):
            status = "warning"
            warnings.append(f"generated report lacks demotion language: {rel}")
        elif rel in LOOP_FRESHNESS_REPORTS and latest_event and mtime and mtime < latest_event:
            status = "stale"
            warnings.append(f"generated report may be stale relative to latest evidence: {rel}")
        report_details[rel] = {
            "status": status,
            "mtime": mtime.isoformat() if mtime else None,
        }

    details = {
        "current_bead": todo.get("current_bead"),
        "in_progress_beads": in_progress,
        "active_memory_claims": claims,
        "generated_reports": report_details,
        "latest_event_timestamp": latest_event.isoformat() if latest_event else None,
    }
    return {"status": "warning" if warnings else "pass", "warnings": warnings, "details": details}


def prd_records(root: Path) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    prd_dir = root / "tasks" / "prds"
    if not prd_dir.is_dir():
        return records
    for path in sorted(prd_dir.glob("*.md")):
        if path.name == "PRD-SHARD-SCHEMA.md":
            continue
        doc = MarkdownDocument.load(path)
        rel = rel_path(path, root)
        status = normalize_status(str(doc.frontmatter.get("status") or ""))
        proposals = doc.sections.get("Bead Proposals", "")
        source_inputs = doc.sections.get("Source Inputs", "")
        records.append(
            {
                "path": rel,
                "status": status,
                "has_bead_proposals": bool(re.search(r"\bB\d{3}\b|tasks/beads/", proposals)),
                "has_source_inputs": bool(source_inputs.strip()),
                "has_approval_path": bool(
                    doc.sections.get("Approval")
                    or doc.sections.get("Definition Of Ready")
                    or doc.sections.get("Open Questions")
                    or re.search(r"\bapproved\b|\bapproval\b|status:\s*(draft|needs_info|approved)", read_text(path), re.IGNORECASE)
                ),
            }
        )
    return records


def is_missing_or_none(value: str | None) -> bool:
    normalized = normalize_optional(value or "").lower()
    return normalized in {"", "none", "not recorded", "not evaluated", "missing", "n/a", "not applicable"}


def generated_or_source_intent_sources(todo: dict[str, Any], bead: BeadRecord | None) -> list[str]:
    suspect_terms = [
        *GENERATED_REPORTS,
        "logs/github-source-intake",
        "logs/source",
        "logs/learning-diary",
        "logs/scheduled-audit",
        "OS-HEALTH.md",
        "PROGRESS.md",
    ]
    sources: list[str] = []
    todo_sections = todo.get("sections") or {}
    candidates = [
        str(todo.get("primary_authority") or ""),
        *bullet_items(str(todo_sections.get("Primary Authority File", ""))),
        *bullet_items(str(todo_sections.get("Files In Play", ""))),
        *bullet_items(str(todo_sections.get("Next Up", ""))),
    ]
    if bead:
        candidates.extend([bead.primary_authority, *bead.files_in_play, bead.handback, *bead.closeout.values()])

    for candidate in candidates:
        cleaned = strip_inline_code(str(candidate))
        if any(term in cleaned for term in suspect_terms):
            sources.append(cleaned)
    return sorted(set(item for item in sources if item))


def intent_lifecycle_state(current_bead: BeadRecord | None, current_checks: dict[tuple[str, str], dict[str, Any]], prds: list[dict[str, Any]]) -> str:
    if current_bead:
        if review_decision_accepted(current_bead.closeout.get("review_decision", "")):
            return "accepted"
        if any(row.get("status") in {"pass", "fail"} for row in current_checks.values()):
            return "evidence_recorded"
        if current_bead.status == "in_progress":
            return "bead_active"
        if current_bead.status == "ready":
            return "beads_proposed"
    if any(prd.get("status") == "approved" for prd in prds):
        return "prd_approved"
    if any(prd.get("status") in {"draft", "needs_info"} for prd in prds):
        return "prd_draft"
    return "raw"


def intent_orchestration(
    root: Path,
    todo: dict[str, Any],
    current_bead: BeadRecord | None,
    beads: list[BeadRecord],
    check_results: list[dict[str, Any]],
    current_checks: dict[tuple[str, str], dict[str, Any]],
) -> dict[str, Any]:
    warnings: list[str] = []
    prds = prd_records(root)
    current_rel = current_bead.rel_path if current_bead else todo.get("current_bead")

    for bead in beads:
        kind = bead.bead_kind.lower().strip()
        if kind in IMPLEMENTATION_BEAD_KINDS and (not bead.parent_prd or not bead.requirement_ids):
            warnings.append(f"{bead.rel_path} is a feature/implementation bead without PRD traceability")

        bead_rows = [row for row in check_results if row.get("bead") == bead.rel_path]
        if bead.requirement_ids and not bead.checks and not bead_rows:
            warnings.append(f"{bead.rel_path} has requirement IDs but no recorded evidence or acceptance path")

        if bead.status in {"needs_info", "manual_testing"}:
            escape_text = " ".join(
                [
                    bead.closeout.get("blocked_escape", ""),
                    bead.handback,
                    bead.closeout.get("follow_up_bead_needed", ""),
                ]
            ).lower()
            if is_missing_or_none(bead.closeout.get("blocked_escape")) and not any(term in escape_text for term in ("unblocker", "escape", "manual", "wait", "blocked")):
                warnings.append(f"{bead.rel_path} is blocked without a clear escape path or unblocker signal")

        follow_up = normalize_optional(bead.closeout.get("follow_up_bead_needed", ""))
        next_bead = normalize_optional(bead.closeout.get("next_bead", ""))
        if follow_up and not is_missing_or_none(follow_up) and follow_up.lower() not in {"none", "not needed"}:
            combined = f"{follow_up} {next_bead} {bead.handback}".lower()
            has_destination = bool(parse_next_bead_reference(combined, root)) or any(term in combined for term in ("defer", "deferred", "decision", "prd", "authority"))
            if not has_destination:
                warnings.append(f"{bead.rel_path} mentions follow-up work without a next bead, owner, or defer decision")

    for prd in prds:
        if prd["status"] == "approved" and not prd["has_bead_proposals"]:
            warnings.append(f"{prd['path']} is approved but has no bead proposals")

    next_up = str((todo.get("sections") or {}).get("Next Up", ""))
    next_up_lower = next_up.lower()
    if any(term in next_up_lower for term in ("create", "build", "implement", "add")) and any(term in next_up_lower for term in ("prd", "bead", "feature", "requirement")):
        warnings.append("tasks/todo.md Next Up contains work-like intent; confirm it is only a queue and not active work")

    suspect_sources = generated_or_source_intent_sources(todo, current_bead)
    if suspect_sources:
        warnings.append("generated reports or source-intake outputs appear in active intent surfaces")

    current_prd = current_bead.parent_prd if current_bead else ""
    current_requirement_ids = current_bead.requirement_ids if current_bead else []
    current_recorded_checks = [row for row in check_results if current_bead and row.get("bead") == current_bead.rel_path]
    lifecycle = intent_lifecycle_state(current_bead, current_checks, prds)
    promotion = promotion_readiness(root, current_bead, {bead.rel_path: bead for bead in beads}, current_checks) if current_bead else {
        "eligible": False,
        "blockers": ["current bead is missing"],
        "next_bead": None,
    }

    details = {
        "lifecycle_state": lifecycle,
        "current_bead": current_rel or "",
        "current_parent_prd": current_prd,
        "current_requirement_ids": current_requirement_ids,
        "current_recorded_check_count": len(current_recorded_checks),
        "pending_approval": not bool(promotion.get("eligible")),
        "promotion_blockers": promotion.get("blockers", []),
        "next_bead": promotion.get("next_bead"),
        "prd_count": len(prds),
        "approved_prds": [prd["path"] for prd in prds if prd["status"] == "approved"],
        "generated_or_source_intent_sources": suspect_sources,
        "trace": {
            "source": "partial" if current_prd else "not recorded",
            "prd": current_prd or "not recorded",
            "requirements": current_requirement_ids,
            "bead": current_rel or "not recorded",
            "evidence": len(current_recorded_checks),
            "review_decision": current_bead.closeout.get("review_decision", "not recorded") if current_bead else "not recorded",
        },
    }
    return {"status": "warning" if warnings else "pass", "warnings": warnings, "details": details}


def workflow_for_bead(bead: BeadRecord | None) -> tuple[str, str]:
    if not bead:
        return "state repair", "restore or select one active bead through tasks/todo.md and bead state"

    kind = bead.bead_kind.lower().strip()
    status = bead.status.lower().strip()
    authority = bead.primary_authority

    if status in {"needs_info", "manual_testing"}:
        return "blocked work / unblocker", "blocked escape path, manual setup note, or unblocker bead"
    if status in {"review", "done"}:
        return "review / closeout", "recorded evidence, review decision, and next-bead safety"
    if kind in PLANNING_BEAD_KINDS or authority.endswith("IDEA-TO-PRD-WORKFLOW.md") or authority.endswith("LOCAL-SOURCE-INTAKE-PROTOCOL.md"):
        return "planning", "source summary, PRD draft, challenge notes, or candidate bead proposal"
    if kind in IMPLEMENTATION_BEAD_KINDS:
        return "execution", "scoped implementation evidence and closeout"
    if kind in {"bugfix", "refactor", "setup", "external_integration", "manual_dashboard", "unblocker"}:
        return f"{kind} bead", "narrow bead evidence and closeout"
    return "bead template review", "confirm matching bead template before continuing"


def workflow_planning(
    root: Path,
    todo: dict[str, Any],
    current_bead: BeadRecord | None,
    beads: list[BeadRecord],
) -> dict[str, Any]:
    warnings: list[str] = []
    details: dict[str, Any] = {}
    prds = prd_records(root)
    current_workflow, next_artifact = workflow_for_bead(current_bead)

    if current_bead:
        kind = current_bead.bead_kind.lower().strip()
        full_text = " ".join(
            [
                current_bead.primary_authority,
                current_bead.sections.get("Objective", ""),
                current_bead.sections.get("Done When", ""),
                current_bead.sections.get("Stop If", ""),
                current_bead.handback,
            ]
        ).lower()
        implementation_files = [item for item in current_bead.files_in_play if Path(item).suffix in CODE_EXTENSIONS and item.startswith((APP_DIR, "src/", "lib/", "components/"))]

        if kind in IMPLEMENTATION_BEAD_KINDS and any(term in full_text for term in ("define the product", "shape the prd", "clarify requirements", "prfaq", "source intake")):
            warnings.append(f"{current_bead.rel_path} may be using an execution bead for product-definition work")
        if kind in PLANNING_BEAD_KINDS and implementation_files:
            warnings.append(f"{current_bead.rel_path} is a planning bead with implementation-looking files in play: {implementation_files[:6]}")
        if current_bead.status in {"needs_info", "manual_testing"}:
            escape_text = " ".join(
                [
                    current_bead.closeout.get("blocked_escape", ""),
                    current_bead.handback,
                    current_bead.closeout.get("follow_up_bead_needed", ""),
                ]
            ).lower()
            if not any(term in escape_text for term in ("unblocker", "manual setup", "escape", "wait", "blocked", "user")):
                warnings.append(f"{current_bead.rel_path} is blocked without an unblocker or manual setup path")
        if current_bead.primary_authority in WORKFLOW_GENERATED_REPORTS or current_bead.primary_authority.startswith("logs/"):
            warnings.append(f"{current_bead.rel_path} appears to use generated evidence as primary authority")

    for prd in prds:
        if prd["status"] in {"draft", "needs_info"} and not prd.get("has_approval_path"):
            warnings.append(f"{prd['path']} is a draft PRD without a visible approval path")
        if prd["status"] == "approved" and not prd["has_bead_proposals"]:
            warnings.append(f"{prd['path']} is approved but has no bead proposals")

    todo_sections = todo.get("sections") or {}
    active_text = "\n".join(
        str(todo_sections.get(section, ""))
        for section in ("Current Bead", "Next Up", "Open Questions", "Files In Play")
    )
    active_lower = active_text.lower()
    if any(term in active_lower for term in ("backlog", "roadmap", "someday", "nice to have", "future")):
        warnings.append("tasks/todo.md active execution fields may contain backlog-like work")
    if any(report.lower() in active_lower for report in (item.lower() for item in WORKFLOW_GENERATED_REPORTS)):
        warnings.append("generated reports appear in active workflow-selection surfaces")

    suspect_sources = generated_or_source_intent_sources(todo, current_bead)
    if suspect_sources:
        warnings.append("generated reports or source-intake outputs appear to drive workflow selection")

    blocked_gates: list[str] = []
    if current_bead:
        if current_bead.status in {"needs_info", "manual_testing"}:
            blocked_gates.append("blocked bead needs escape path or manual setup")
        if current_bead.bead_kind.lower().strip() in IMPLEMENTATION_BEAD_KINDS and (not current_bead.parent_prd or not current_bead.requirement_ids):
            blocked_gates.append("implementation bead lacks PRD traceability")
        if not current_bead.checks:
            blocked_gates.append("verification path missing")
    else:
        blocked_gates.append("current bead missing")

    details = {
        "current_situation": current_workflow,
        "recommended_workflow": current_workflow,
        "artifact_to_produce_next": next_artifact,
        "required_authority_source": current_bead.primary_authority if current_bead else "tasks/todo.md and active bead state",
        "user_approval_needed": "yes" if blocked_gates or (current_bead and current_bead.status in {"review", "done"}) else "not before continuing current approved bead",
        "stop_condition": "; ".join(blocked_gates) if blocked_gates else "stop if workflow, authority, verification, or approval gate becomes unclear",
        "generated_report_warning": "Generated workflow maps and OS Health are evidence only; do not use them as active memory or task selection.",
        "current_bead": current_bead.rel_path if current_bead else todo.get("current_bead"),
        "related_prd": current_bead.parent_prd if current_bead else "",
        "pending_approvals": blocked_gates,
        "blocked_gates": blocked_gates,
        "prd_count": len(prds),
        "approved_prds_without_beads": [prd["path"] for prd in prds if prd["status"] == "approved" and not prd["has_bead_proposals"]],
        "generated_or_source_workflow_sources": suspect_sources,
        "human_review_prompt": "Ask: Is this the right workflow, and what owner file must approve or record the next artifact?",
    }
    return {"status": "warning" if warnings else "pass", "warnings": warnings, "details": details}


def pattern_matches(text: str) -> dict[str, list[str]]:
    lowered = text.lower()
    matches: dict[str, list[str]] = {}
    for group, terms in PATTERN_TERM_GROUPS.items():
        found = sorted(term for term in terms if term in lowered)
        if found:
            matches[group] = found
    return matches


def recommended_pattern_shape(matches: dict[str, list[str]], current_bead: BeadRecord | None) -> tuple[str, str, list[str]]:
    owner_hints: list[str] = []
    if "auth_access" in matches:
        owner_hints.extend(["SECURITY.md", "ARCHITECTURE.md"])
        return (
            "auth/access boundary",
            "Put login, roles, permissions, and sensitive data rules behind a clear access boundary before coding.",
            sorted(set(owner_hints)),
        )
    if "external_service" in matches:
        owner_hints.extend(["API.md", "ARCHITECTURE.md", "PROJECT-CONTEXT.md"])
        return (
            "adapter or facade",
            "Wrap the external service in one boundary so provider details do not leak across the app.",
            sorted(set(owner_hints)),
        )
    if "state_flow" in matches:
        owner_hints.extend(["ARCHITECTURE.md", "USER-FLOWS.md", "tasks/prds/*.md"])
        return (
            "state flow",
            "Name statuses, allowed transitions, approval points, and blocked states before implementation.",
            sorted(set(owner_hints)),
        )
    if "strategy" in matches:
        owner_hints.extend(["ARCHITECTURE.md", "PROJECT-CONTEXT.md"])
        return (
            "strategy-style boundary",
            "Keep interchangeable rules, modes, or providers behind one decision point.",
            sorted(set(owner_hints)),
        )
    if "audit_trail" in matches:
        owner_hints.extend(["DATA-MODELS.md", "SECURITY.md", "ARCHITECTURE.md"])
        return (
            "audit trail",
            "Record who did what, when, and why for actions that must be explainable later.",
            sorted(set(owner_hints)),
        )
    if "simple_change" in matches and current_bead and len(current_bead.files_in_play) <= 3:
        return (
            "direct change",
            "This looks simple enough to implement directly; avoid adding a named pattern unless new variation appears.",
            ["active bead"],
        )
    return (
        "existing project convention",
        "Start with the repo's current framework and naming conventions, then introduce a pattern only if it reduces real risk or repetition.",
        ["PROJECT-CONTEXT.md", "CODEBASE-GUIDE.md", "active bead"],
    )


def system_design_pattern_guidance(
    root: Path,
    todo: dict[str, Any],
    current_bead: BeadRecord | None,
    beads: list[BeadRecord],
) -> dict[str, Any]:
    warnings: list[str] = []
    todo_sections = todo.get("sections") or {}
    active_text = "\n".join(str(todo_sections.get(section, "")) for section in ("Current Bead", "Next Up", "Open Questions", "Files In Play"))
    bead_text = ""
    if current_bead:
        bead_text = "\n".join(
            [
                current_bead.title,
                current_bead.bead_kind,
                current_bead.primary_authority,
                current_bead.parent_prd,
                " ".join(current_bead.requirement_ids),
                " ".join(current_bead.files_in_play),
                current_bead.sections.get("Objective", ""),
                current_bead.sections.get("Done When", ""),
                current_bead.sections.get("Out Of Scope", ""),
                current_bead.sections.get("Stop If", ""),
                current_bead.handback,
                " ".join(current_bead.closeout.values()),
            ]
        )
    combined_text = "\n".join([active_text, bead_text])
    lowered = combined_text.lower()
    matches = pattern_matches(combined_text)
    likely_shape, recommendation, owner_hints = recommended_pattern_shape(matches, current_bead)

    if current_bead:
        authority = current_bead.primary_authority
        code_files = [item for item in current_bead.files_in_play if Path(item).suffix in CODE_EXTENSIONS]
        broad_architecture_terms = any(term in lowered for term in ("architecture", "system design", "state machine", "adapter", "facade", "strategy", "provider"))
        if ("external_service" in matches or "auth_access" in matches) and not any(owner in authority for owner in ("API.md", "ARCHITECTURE.md", "SECURITY.md", "PROJECT-CONTEXT.md", "tasks/prds/")):
            warnings.append(f"{current_bead.rel_path} mentions integration or access-boundary work without an obvious owner file for the boundary")
        if "state_flow" in matches and not any(owner in authority for owner in ("ARCHITECTURE.md", "USER-FLOWS.md", "tasks/prds/")):
            warnings.append(f"{current_bead.rel_path} mentions statuses, steps, or approvals without a state-flow owner")
        if "strategy" in matches and not any(owner in authority for owner in ("ARCHITECTURE.md", "PROJECT-CONTEXT.md", "tasks/prds/")):
            warnings.append(f"{current_bead.rel_path} mentions modes, providers, or rules without a strategy/configuration owner")
        if "audit_trail" in matches and not any(owner in authority for owner in ("DATA-MODELS.md", "SECURITY.md", "ARCHITECTURE.md", "tasks/prds/")):
            warnings.append(f"{current_bead.rel_path} mentions audit/history needs without a data or security owner")
        if broad_architecture_terms and current_bead.bead_kind.lower().strip() in IMPLEMENTATION_BEAD_KINDS and not any(owner in authority for owner in ("ARCHITECTURE.md", "PROJECT-CONTEXT.md", "tasks/prds/")):
            warnings.append(f"{current_bead.rel_path} may be doing architecture-shaping work inside an implementation bead")
        if any(term in lowered for term in PATTERN_NAME_TERMS) and not any(term in lowered for term in ("why", "because", "risk", "boundary", "owner", "simpler")):
            warnings.append(f"{current_bead.rel_path} names a design pattern without recording the problem, risk, or owner")
        if likely_shape != "direct change" and not current_bead.checks:
            warnings.append(f"{current_bead.rel_path} has pattern-shaped work but no checks listed")
        if likely_shape == "direct change" and any(term in lowered for term in ("factory", "strategy", "state machine", "adapter")) and len(code_files) <= 2:
            warnings.append(f"{current_bead.rel_path} may be adding unnecessary abstraction for a simple change")
        if current_bead.primary_authority in PATTERN_GENERATED_REPORTS or current_bead.primary_authority.startswith("logs/"):
            warnings.append(f"{current_bead.rel_path} appears to use generated pattern guidance as primary authority")
    else:
        warnings.append("current bead is missing; pattern guidance cannot inspect scoped work")

    details = {
        "current_bead": current_bead.rel_path if current_bead else todo.get("current_bead"),
        "likely_project_shape": likely_shape,
        "recommended_pattern": likely_shape if likely_shape != "direct change" else "none",
        "recommendation": recommendation,
        "simpler_alternative": "Build directly inside the existing project convention when the work is one-off, low-risk, and has no repeated variation.",
        "owner_file_hints": owner_hints,
        "detected_terms": matches,
        "warning_count": len(warnings),
        "next_human_review_prompt": "Ask: Is this simple enough to build directly, or does it need an adapter, state flow, strategy boundary, access boundary, or audit trail?",
        "generated_report_warning": "Generated pattern guidance is evidence only; it must not choose tasks, approve transitions, or replace PRDs, beads, architecture docs, or decisions.",
        "known_pattern_families": ["creation", "structure", "behavior", "product workflow"],
    }
    return {"status": "warning" if warnings else "pass", "warnings": warnings, "details": details}


def dependency_lookup(beads: list[BeadRecord]) -> dict[str, BeadRecord]:
    lookup: dict[str, BeadRecord] = {}
    for bead in beads:
        lookup[bead.rel_path] = bead
        if bead.bead_id:
            lookup[bead.bead_id] = bead
    return lookup


def closeout_follow_up_destination(root: Path, bead: BeadRecord) -> bool:
    follow_up = normalize_optional(bead.closeout.get("follow_up_bead_needed", ""))
    if not follow_up or is_missing_or_none(follow_up) or follow_up.lower() in {"none", "not needed"}:
        return True
    combined = " ".join(
        [
            follow_up,
            normalize_optional(bead.closeout.get("next_bead", "")),
            bead.handback,
            bead.closeout.get("blocked_escape", ""),
        ]
    ).lower()
    return bool(parse_next_bead_reference(combined, root)) or any(term in combined for term in ("defer", "deferred", "decision", "prd", "authority", "superseded"))


def long_horizon_planning(
    root: Path,
    todo: dict[str, Any],
    current_bead: BeadRecord | None,
    beads: list[BeadRecord],
) -> dict[str, Any]:
    warnings: list[str] = []
    prds = prd_records(root)
    bead_lookup = dependency_lookup(beads)
    todo_sections = todo.get("sections") or {}
    active_text = "\n".join(
        str(todo_sections.get(section, ""))
        for section in ("Current Bead", "Next Up", "Open Questions", "Noticed")
    )
    active_lower = active_text.lower()

    if any(term in active_lower for term in LONG_HORIZON_TERMS):
        warnings.append("future or roadmap language appears in tasks/todo.md active execution fields")
    if any(report.lower() in active_lower for report in (item.lower() for item in WORKFLOW_GENERATED_REPORTS)):
        warnings.append("generated reports appear in active long-horizon planning surfaces")

    approved_prds_without_beads: list[str] = []
    prd_drafts: list[str] = []
    for prd in prds:
        if prd["status"] == "approved" and not prd["has_bead_proposals"]:
            approved_prds_without_beads.append(prd["path"])
            warnings.append(f"{prd['path']} is approved but has no bead proposals")
        if prd["status"] in {"draft", "needs_info"}:
            prd_drafts.append(prd["path"])

    ready_beads: list[str] = []
    blocked_beads: list[str] = []
    follow_up_candidates: list[str] = []
    deferred_or_superseded: list[str] = []
    dependency_gaps: list[str] = []
    proposed_readiness_gaps: list[str] = []

    for bead in beads:
        status = bead.status.lower().strip()
        closeout_text = " ".join([*bead.closeout.values(), bead.handback]).lower()
        if status == "ready":
            ready_beads.append(bead.rel_path)
            missing = []
            if not bead.primary_authority:
                missing.append("primary authority")
            if not bead.checks:
                missing.append("checks")
            if not bead.verification_type:
                missing.append("verification type")
            if missing:
                proposed_readiness_gaps.append(f"{bead.rel_path} missing {', '.join(missing)}")
        if status in {"needs_info", "manual_testing"}:
            blocked_beads.append(bead.rel_path)
            escape_text = " ".join([bead.closeout.get("blocked_escape", ""), bead.handback, bead.closeout.get("follow_up_bead_needed", "")]).lower()
            if not any(term in escape_text for term in ("unblocker", "escape", "manual", "wait", "blocked", "user", "external")):
                warnings.append(f"{bead.rel_path} is blocked without an escape path or unblocker signal")
        if not closeout_follow_up_destination(root, bead):
            follow_up_candidates.append(bead.rel_path)
            warnings.append(f"{bead.rel_path} has a follow-up candidate without a destination")
        if any(term in closeout_text for term in ("deferred", "defer", "superseded")):
            deferred_or_superseded.append(bead.rel_path)
            if not any(term in closeout_text for term in LONG_HORIZON_REVISIT_TERMS):
                warnings.append(f"{bead.rel_path} mentions deferred or superseded work without an owner or revisit trigger")

        for dependency in bead.depends_on:
            dependency_bead = bead_lookup.get(dependency)
            if dependency_bead is None:
                dependency_gaps.append(f"{bead.rel_path} depends on missing {dependency}")
                continue
            if dependency_bead.status != "done":
                dependency_gaps.append(f"{bead.rel_path} depends on non-done {dependency_bead.rel_path} ({dependency_bead.status})")

    for gap in proposed_readiness_gaps:
        warnings.append(gap)
    for gap in dependency_gaps:
        warnings.append(gap)

    details = {
        "current_bead": current_bead.rel_path if current_bead else todo.get("current_bead"),
        "approved_prds": [prd["path"] for prd in prds if prd["status"] == "approved"],
        "approved_prds_without_beads": approved_prds_without_beads,
        "prd_drafts": prd_drafts,
        "ready_beads": ready_beads,
        "blocked_beads": blocked_beads,
        "follow_up_candidates": follow_up_candidates,
        "deferred_or_superseded_signals": deferred_or_superseded,
        "dependency_gaps": dependency_gaps,
        "proposed_readiness_gaps": proposed_readiness_gaps,
        "active_memory": ACTIVE_MEMORY,
        "next_human_review_prompt": "Review approved, blocked, deferred, ready, and follow-up work without activating anything.",
        "generated_report_warning": "Generated long-horizon maps are evidence only; do not use them as active memory, priority ordering, or task selection.",
    }
    return {"status": "warning" if warnings else "pass", "warnings": warnings, "details": details}


def latest_event_time(events: list[dict[str, Any]], action: str, bead: str | None = None) -> datetime | None:
    latest = None
    for event in events:
        if event.get("action") != action:
            continue
        if bead and event.get("bead") != bead:
            continue
        timestamp = parse_iso_timestamp(event.get("timestamp"))
        if timestamp and (latest is None or timestamp > latest):
            latest = timestamp
    return latest


def latest_check_time_for_bead(check_results: list[dict[str, Any]], bead: BeadRecord | None) -> datetime | None:
    if not bead:
        return None
    latest = None
    for row in check_results:
        if row.get("bead") != bead.rel_path:
            continue
        timestamp = parse_iso_timestamp(row.get("timestamp"))
        if timestamp and (latest is None or timestamp > latest):
            latest = timestamp
    return latest


def completion_session_freshness(
    bead_status: str,
    latest_check: datetime | None,
    latest_close: datetime | None,
) -> str:
    if latest_check is None:
        return "no-recorded-checks"
    if latest_close is not None and latest_close >= latest_check:
        return "current"
    if bead_status == "in_progress":
        return "open"
    return "stale"


def completion_handoff_quality(
    root: Path,
    todo: dict[str, Any],
    bead: BeadRecord | None,
    beads: list[BeadRecord],
    check_results: list[dict[str, Any]],
    current_checks: dict[tuple[str, str], dict[str, Any]],
    events: list[dict[str, Any]],
    promotion_state: dict[str, Any],
) -> dict[str, Any]:
    warnings: list[str] = []
    if bead is None:
        return {
            "status": "warning",
            "warnings": ["current bead is missing"],
            "details": {"next_safe_action": "repair active bead pointer before handoff or closeout"},
        }

    bead_rows = [row for row in check_results if row.get("bead") == bead.rel_path]
    closeout = bead.closeout
    todo_sections = todo.get("sections") or {}
    bead_map = {item.rel_path: item for item in beads}

    if not bead_rows:
        warnings.append("closeout exists but no recorded checks exist for the active bead")
    if not manual_verification_structured(closeout.get("manual_verification", "")):
        warnings.append("manual verification is missing or vague")
    if not review_decision_valid(closeout.get("review_decision", "")):
        warnings.append("review decision is missing or invalid")

    next_value = normalize_optional(closeout.get("next_bead", ""))
    next_rel = parse_next_bead_reference(next_value, root) if next_value else None
    next_start = None
    if next_value and not is_missing_or_none(next_value) and next_value.lower() not in {"not evaluated"}:
        if not next_rel:
            warnings.append(f"next bead is named but not found: {next_value}")
        elif next_rel not in bead_map:
            warnings.append(f"next bead file is missing: {next_rel}")
        else:
            next_start = start_readiness(bead_map[next_rel], bead_map)
            if next_start.get("blockers"):
                warnings.append(f"next bead is named but not ready: {next_start['blockers'][:6]}")

    if not closeout_follow_up_destination(root, bead):
        warnings.append("follow-up work has no destination")

    handback_text = normalize_optional(bead.handback)
    if not handback_text or any(term in handback_text.lower() for term in ("tbd", "todo", "later", "as needed")):
        warnings.append("handback is vague or missing")

    latest_check = latest_check_time_for_bead(check_results, bead)
    latest_close = latest_event_time(events, "session-close", bead.rel_path)
    session_freshness = completion_session_freshness(bead.status, latest_check, latest_close)
    if session_freshness == "stale":
        warnings.append("active bead has recorded evidence newer than the latest session close")

    required_context = {
        "active bead": bead.rel_path,
        "state": bead.status,
        "done-when": todo_sections.get("Done When", ""),
        "primary authority": bead.primary_authority,
        "files in play": "\n".join(bead.files_in_play),
        "out of scope": todo_sections.get("Explicit Out-of-Scope", ""),
        "checks": "\n".join(bead.checks),
        "allowed actions": "\n".join((bead.run_contract or {}).get("allowed_paths") or []),
        "proof needed": "\n".join((bead.run_contract or {}).get("proof_needed") or []),
        "stop conditions": bead.sections.get("Stop If", ""),
        "open questions": todo_sections.get("Open Questions", ""),
        "latest evidence": bead_rows[-1].get("output") if bead_rows else "",
        "blockers": "; ".join(promotion_state.get("blockers", [])),
        "next safe action": "",
        "generated-report warning": "Generated reports are evidence only.",
    }
    if not (bead.run_contract or {}).get("present"):
        required_context["allowed actions"] = "not applicable; no run contract declared"
        required_context["proof needed"] = "not applicable; no run contract declared"

    close_state = close_readiness(bead, current_checks)
    if bead.status in {"needs_info", "manual_testing"}:
        next_safe_action = "record exact blocked escape path or create a narrow unblocker bead"
    elif close_state.get("eligible") and review_decision_accepted(closeout.get("review_decision", "")):
        next_safe_action = "review transition proposal; user approval is still required"
    elif bead_rows:
        next_safe_action = "complete manual verification and review decision before transition"
    else:
        next_safe_action = "run and record the active bead checks"
    required_context["next safe action"] = next_safe_action

    missing_context = [name for name, value in required_context.items() if not normalize_optional(str(value))]
    if missing_context:
        warnings.append(f"required handoff Context Pack fields are missing: {missing_context}")

    if promotion_state.get("eligible"):
        warnings.append("transition appears eligible; explicit user approval is still required")

    if bead.status in {"needs_info", "manual_testing"}:
        escape_text = " ".join([closeout.get("blocked_escape", ""), bead.handback, closeout.get("follow_up_bead_needed", "")]).lower()
        required_terms = ("owner", "input", "unblocker", "manual", "user", "wait", "external", "escape", "blocked")
        if not any(term in escape_text for term in required_terms):
            warnings.append("blocked or manual-testing bead lacks owner, exact missing input, escape path, or unblocker signal")

    details = {
        "current_bead": bead.rel_path,
        "closeout_status": "complete" if not close_state.get("blockers") else "incomplete",
        "closeout_blockers": close_state.get("blockers", []),
        "promotion_status": "eligible" if promotion_state.get("eligible") else "blocked",
        "promotion_blockers": promotion_state.get("blockers", []),
        "manual_verification": closeout.get("manual_verification", "not recorded"),
        "review_decision": closeout.get("review_decision", "not recorded"),
        "latest_check_timestamp": latest_check.isoformat() if latest_check else None,
        "latest_session_close_timestamp": latest_close.isoformat() if latest_close else None,
        "session_freshness": session_freshness,
        "next_bead": next_rel or next_value or "not recorded",
        "next_bead_start_readiness": next_start,
        "handoff_context_missing": missing_context,
        "next_safe_action": next_safe_action,
        "handoff_packet": required_context,
        "generated_report_warning": "Generated handoff packets are evidence only; do not use them as active memory, task selection, or transition approval.",
    }
    return {"status": "warning" if warnings else "pass", "warnings": warnings, "details": details}


def tool_execution_quality(
    root: Path,
    bead: BeadRecord | None,
    tool_rows: list[dict[str, Any]],
    check_results: list[dict[str, Any]],
    changed: list[str],
) -> dict[str, Any]:
    warnings: list[str] = []
    details: dict[str, Any] = {}
    current_rel = bead.rel_path if bead else ""
    active_tool_rows = [row for row in tool_rows if str(row.get("task") or "") == current_rel] if current_rel else []
    recent_rows = tool_rows[-10:]
    approval_gaps: list[str] = []
    destructive_rows: list[str] = []
    missing_failure_category: list[str] = []
    approval_command_terms = ("push", "merge", "deploy", "rollback", "migrate", "drop", "delete", "rm ", "reset", "force", "secret", "token", "credential")

    for row in tool_rows:
        tool_class = str(row.get("class") or "").strip()
        command = str(row.get("command") or "")
        status = str(row.get("status") or "").strip().lower()
        failure_category = str(row.get("failure_category") or "").strip()
        approval_note = str(row.get("approval_note") or "").strip()

        if tool_class and tool_class not in TOOL_CLASSES:
            warnings.append(f"tool run has unknown class `{tool_class}`: {command}")
        if tool_class in TOOL_APPROVAL_CLASSES and not approval_note:
            approval_gaps.append(command or str(row.get("tool") or "unknown tool"))
        if tool_class == "destructive":
            destructive_rows.append(command or str(row.get("tool") or "unknown tool"))
        if status in {"fail", "failed", "blocked"} and not failure_category:
            missing_failure_category.append(command or str(row.get("tool") or "unknown tool"))
        if failure_category and failure_category not in TOOL_FAILURE_CATEGORIES:
            warnings.append(f"tool run has unknown failure category `{failure_category}`: {command}")
        if any(term in command.lower() for term in approval_command_terms) and not approval_note:
            approval_gaps.append(command or str(row.get("tool") or "unknown tool"))

    if approval_gaps:
        warnings.append(f"approval-required tool runs lack approval notes: {approval_gaps[:6]}")
    if destructive_rows:
        warnings.append(f"destructive tool runs are present and require review: {destructive_rows[:6]}")
    if missing_failure_category:
        warnings.append(f"failed or blocked tool runs lack failure category: {missing_failure_category[:6]}")

    if bead:
        vague_checks = [
            check
            for check in bead.checks
            if any(term in check.lower() for term in ("etc", "as needed", "appropriate", "manual check", "verify it works"))
        ]
        if vague_checks:
            warnings.append(f"active bead has vague checks: {vague_checks[:6]}")

    generated_refresh_count = sum(1 for row in active_tool_rows if row.get("class") == "generated_refresh")
    active_check_rows = [row for row in check_results if current_rel and row.get("bead") == current_rel]
    if generated_refresh_count and not active_check_rows:
        warnings.append("generated reports were refreshed for active work but no verification evidence exists")

    changed_names = [changed_path_name(item) for item in changed]
    changed_names = [item for item in changed_names if item]
    if changed_names and active_check_rows:
        latest_check_ts = max(str(row.get("timestamp") or "") for row in active_check_rows)
        latest_tool_ts = max([str(row.get("timestamp") or "") for row in active_tool_rows] or [""])
        if latest_tool_ts and latest_check_ts < latest_tool_ts:
            warnings.append("command evidence may be stale relative to later logged tool activity")

    latest_failure = next(
        (
            {
                "tool": row.get("tool"),
                "command": row.get("command"),
                "failure_category": row.get("failure_category") or "missing",
                "timestamp": row.get("timestamp"),
            }
            for row in reversed(tool_rows)
            if str(row.get("status") or "").lower() in {"fail", "failed", "blocked"}
        ),
        None,
    )
    class_counts = Counter(str(row.get("class") or "unknown") for row in tool_rows)
    details = {
        "entries": len(tool_rows),
        "active_bead_entries": len(active_tool_rows),
        "recent_entries": recent_rows,
        "class_counts": dict(sorted(class_counts.items())),
        "latest_failure": latest_failure,
        "approval_gap_count": len(set(approval_gaps)),
        "destructive_count": len(destructive_rows),
        "missing_failure_category_count": len(missing_failure_category),
    }
    return {"status": "warning" if warnings else "pass", "warnings": warnings, "details": details}


def start_readiness(bead: BeadRecord, bead_map: dict[str, BeadRecord]) -> dict[str, Any]:
    blockers: list[str] = []
    if bead.status != "ready":
        blockers.append(f"status must be ready to start; found {bead.status or 'missing'}")
    if not bead.primary_authority:
        blockers.append("primary authority is missing")
    if not bead.files_in_play:
        blockers.append("files in play are missing")
    if not bead.checks:
        blockers.append("checks are missing")
    if len(bead.files_in_play) > 20:
        blockers.append("files in play exceed the 20-file operating limit")

    for dependency in bead.depends_on:
        dependency_match = None
        for candidate in bead_map.values():
            if candidate.bead_id == dependency or candidate.rel_path == dependency:
                dependency_match = candidate
                break
        if dependency_match is None:
            blockers.append(f"dependency is missing: {dependency}")
            continue
        if dependency_match.status != "done":
            blockers.append(f"dependency is not done: {dependency_match.rel_path} ({dependency_match.status})")

    if bead.bead_kind == "implementation":
        if not bead.parent_prd:
            blockers.append("parent PRD is missing")
        if not bead.requirement_ids:
            blockers.append("requirement IDs are missing")
        if bead.parent_prd.lower().startswith("tbd"):
            blockers.append("parent PRD is still TBD")
        if any("tbd" in requirement.lower() for requirement in bead.requirement_ids):
            blockers.append("requirement IDs still contain TBD placeholders")

    return {"eligible": not blockers, "blockers": blockers}


def close_readiness(bead: BeadRecord, latest_checks: dict[tuple[str, str], dict[str, Any]]) -> dict[str, Any]:
    blockers: list[str] = []
    if bead.status == "ready":
        blockers.append("bead has not started yet")

    check_rows = check_rows_for_bead(bead, latest_checks)
    if not check_rows:
        blockers.append("no checks are declared for this bead")
    else:
        missing = [row["source"] for row in check_rows if row["status"] == "missing"]
        failing = [row["source"] for row in check_rows if row["status"] == "fail" or row["exit_code"] not in {0, None}]
        if missing:
            blockers.append(f"missing recorded check evidence: {missing}")
        if failing:
            blockers.append(f"latest recorded checks are failing: {failing}")

    manual = bead.closeout.get("manual_verification", "")
    if not manual_verification_clear(manual):
        blockers.append("manual verification is missing or still pending")

    return {
        "eligible": not blockers,
        "blockers": blockers,
        "checks": check_rows,
        "manual_verification": manual or "not recorded",
        "review_decision": bead.closeout.get("review_decision", "not recorded"),
    }


def find_next_bead(bead: BeadRecord, root: Path) -> str | None:
    next_value = bead.closeout.get("next_bead", "")
    if next_value:
        next_bead = parse_next_bead_reference(next_value, root)
        if next_bead:
            return next_bead

    return parse_next_bead_reference(bead.handback, root)


def promotion_readiness(
    root: Path,
    bead: BeadRecord,
    bead_map: dict[str, BeadRecord],
    latest_checks: dict[tuple[str, str], dict[str, Any]],
) -> dict[str, Any]:
    blockers: list[str] = []
    close_state = close_readiness(bead, latest_checks)
    blockers.extend(close_state["blockers"])

    if bead.status not in {"review", "done"}:
        blockers.append(f"current bead status must be review or done before promotion; found {bead.status or 'missing'}")

    if not review_decision_accepted(close_state["review_decision"]):
        blockers.append("review decision is not accepted")

    next_rel = find_next_bead(bead, root)
    next_start: dict[str, Any] | None = None
    if not next_rel:
        blockers.append("next bead is not named in Closeout Evidence or Handback")
    elif next_rel not in bead_map:
        blockers.append(f"next bead file is missing: {next_rel}")
    else:
        next_start = start_readiness(bead_map[next_rel], bead_map)
        blockers.extend([f"next bead blocker: {item}" for item in next_start["blockers"]])

    return {
        "eligible": not blockers,
        "blockers": blockers,
        "next_bead": next_rel,
        "next_start_readiness": next_start,
        "close_readiness": close_state,
    }


def follow_up_suggestion(bead: BeadRecord, close_state: dict[str, Any]) -> str:
    explicit = normalize_optional(bead.closeout.get("follow_up_bead_needed", ""))
    if explicit:
        return explicit

    blocker_text = " ".join(close_state["blockers"]).lower()
    if bead.status in {"needs_info", "manual_testing"}:
        return "create a narrow unblocker bead or wait on the documented blocked escape path"
    if "manual verification" in blocker_text:
        return "create an unblocker bead for manual verification only if the missing input is a separate logical unit"
    if "failing" in blocker_text or "missing recorded check evidence" in blocker_text:
        return "create a follow-up bead only if verification remediation would widen the current bead"
    return "none"


def bead_depth_quality(bead: BeadRecord | None) -> dict[str, Any]:
    warnings: list[str] = []
    if not bead:
        return {
            "status": "warning",
            "warnings": ["current bead is missing"],
            "details": {
                "plain_english_summary": "I cannot judge planning depth because there is no active bead.",
                "user_decision": "repair state",
                "why_this_matters": "Precode needs one active bead before it can tell whether planning is too light or too heavy.",
                "stop_if": "Stop if the agent cannot name the active bead.",
                "approval_prompt": "Ask the agent to repair active state before continuing.",
                "advisory_only": True,
            },
        }

    stop_text = (bead.sections.get("Stop If", "") or "").strip()
    sensitive_text = " ".join(
        [
            bead.title,
            bead.bead_kind,
            bead.primary_authority,
            " ".join(bead.requirement_ids),
            " ".join(bead.files_in_play),
            bead.sections.get("Objective", ""),
            bead.sections.get("Done When", ""),
            stop_text,
        ]
    ).lower()
    sensitive_surface = any(term in sensitive_text for term in SENSITIVE_SURFACE_TERMS)
    file_count = len(bead.files_in_play)
    inferred_complexity = "standard"
    if file_count <= 2 and not sensitive_surface:
        inferred_complexity = "trivial"
    elif file_count <= 5 and not sensitive_surface:
        inferred_complexity = "narrow"
    elif sensitive_surface:
        inferred_complexity = "high-risk"
    if file_count > 20:
        inferred_complexity = "multi-system"

    inferred_depth = "brief"
    if inferred_complexity == "trivial":
        inferred_depth = "none"
    elif inferred_complexity == "standard":
        inferred_depth = "PRD"
    elif inferred_complexity == "high-risk":
        inferred_depth = "PRD+architecture"
    elif inferred_complexity == "multi-system":
        inferred_depth = "PRD+architecture+test-plan"

    inferred_autonomy = "supervised"
    if sensitive_surface or inferred_complexity in {"high-risk", "multi-system"}:
        inferred_autonomy = "human-only"

    complexity = bead.complexity or inferred_complexity
    required_depth = bead.required_planning_depth or inferred_depth
    autonomy = bead.autonomy_level or inferred_autonomy
    inferred_defaults = {
        "complexity": {"value": inferred_complexity, "used": not bool(bead.complexity)},
        "required_planning_depth": {"value": inferred_depth, "used": not bool(bead.required_planning_depth)},
        "autonomy_level": {"value": inferred_autonomy, "used": not bool(bead.autonomy_level)},
    }

    if bead.complexity and bead.complexity not in COMPLEXITY_LEVELS:
        warnings.append(f"unknown complexity `{bead.complexity}`")
    if bead.required_planning_depth and bead.required_planning_depth not in REQUIRED_PLANNING_DEPTHS:
        warnings.append(f"unknown required_planning_depth `{bead.required_planning_depth}`")
    if bead.autonomy_level and bead.autonomy_level not in AUTONOMY_LEVELS:
        warnings.append(f"unknown autonomy_level `{bead.autonomy_level}`")

    if bead.complexity == "trivial" and file_count > 5:
        warnings.append("trivial bead has more than 5 files in play; consider narrow or split scope")
    if complexity in {"high-risk", "multi-system"}:
        if required_depth in {"", "none", "brief"}:
            warnings.append("high-risk or multi-system bead should require PRD+architecture planning depth or stronger")
        if not any(tier in {"integration", "browser", "manual", "external"} for tier in bead.verification_type):
            warnings.append("high-risk or multi-system bead should include runtime, manual, or external verification")
        if not stop_text:
            warnings.append("high-risk or multi-system bead should name stop conditions")
    if sensitive_surface and required_depth in {"", "none", "brief"}:
        warnings.append("sensitive-surface bead should not use none/brief planning depth without explicit rationale")
    if autonomy == "bounded-afk":
        if not bead.checks:
            warnings.append("bounded-afk bead needs explicit checks")
        if not stop_text:
            warnings.append("bounded-afk bead needs explicit stop conditions")
        if file_count > 20:
            warnings.append("bounded-afk bead exceeds the 20-file operating limit")
    if autonomy == "human-only":
        gate_text = " ".join([stop_text, bead.handback, bead.closeout.get("blocked_escape", "")]).lower()
        if not any(term in gate_text for term in ("manual", "approval", "human", "user", "dashboard", "external")):
            warnings.append("human-only bead should name the manual gate, approval, or human-owned action")

    if warnings:
        user_decision = "approval needed" if sensitive_surface or autonomy == "human-only" else "ask for proof"
        summary = "This bead may need clearer planning, proof, or human approval before a beginner should trust it."
        stop_if = "Stop if the agent cannot explain the planning depth, checks, stop conditions, or approval gate in plain English."
        approval_prompt = "Ask the agent what planning or approval is missing before continuing."
    else:
        user_decision = "continue"
        summary = "The planning depth looks proportionate for this bead."
        stop_if = "Stop if the task grows beyond the named files, risk, or checks."
        approval_prompt = "No extra planning approval is suggested by adaptive depth."

    return {
        "status": "warning" if warnings else "pass",
        "warnings": warnings,
        "details": {
            "current_bead": bead.rel_path,
            "complexity": complexity,
            "required_planning_depth": required_depth,
            "autonomy_level": autonomy,
            "files_in_play_count": file_count,
            "checks_count": len(bead.checks),
            "verification_type": bead.verification_type,
            "sensitive_surface_detected": sensitive_surface,
            "inferred_defaults": inferred_defaults,
            "plain_english_summary": summary,
            "user_decision": user_decision,
            "why_this_matters": "Adaptive depth keeps tiny work light while asking for more planning and proof when risk rises.",
            "stop_if": stop_if,
            "approval_prompt": approval_prompt,
            "advisory_only": True,
        },
    }


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

    if any(term in lower for term in COMMAND_DESTRUCTIVE_TERMS):
        tool_class = "destructive"
        user_decision = "stop"
        summary = "This command looks destructive. Stop and get explicit approval before running it."
        approval_prompt = "Ask the user to approve the exact destructive command, expected effect, rollback or escape path, and evidence plan."
    elif any(term in lower for term in COMMAND_SENSITIVE_TERMS):
        tool_class = "secret_bearing" if any(term in lower for term in ("secret", "token", "credential", "password", ".env")) else "external_mutation"
        user_decision = "approval needed"
        summary = "This command touches a sensitive surface. Ask for approval before running it."
        approval_prompt = "Ask the user to approve the exact sensitive action, scope, risk, and rollback or blocked escape path."
    elif any(term in lower for term in COMMAND_EXTERNAL_MUTATION_TERMS):
        tool_class = "external_mutation"
        user_decision = "approval needed"
        summary = "This command may mutate an external service or shared branch. Ask for approval before running it."
        approval_prompt = "Ask the user to approve the exact external mutation and recovery plan."
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
            user_decision = "approval needed"
            summary = "This command may change local files on a sensitive bead. Ask for approval before running it."
            approval_prompt = "Ask the user to approve the sensitive local mutation, expected files, and rollback or escape path."
        else:
            user_decision = "continue"
            summary = "This command may change local project files. Continue only if the paths stay inside files_in_play."
            approval_prompt = "Ask for approval if this widens scope, installs dependencies, or touches sensitive files."
    else:
        tool_class = "read_only"
        user_decision = "continue"
        summary = "This command does not look destructive or sensitive from its summary."
        approval_prompt = "No special approval suggested."

    return {
        "command": command_text,
        "class": tool_class,
        "user_decision": user_decision,
        "plain_english_summary": summary,
        "why_this_matters": "Non-technical builders need command risk translated before a tool mutates files, services, secrets, or production state.",
        "stop_if": "Stop if the command deletes, force-resets, migrates, deploys, exposes secrets, or touches production without explicit approval.",
        "approval_prompt": approval_prompt,
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
        summary = "The agent appears to have changed files outside the approved task. Stop and ask whether this is generated evidence, current-bead work, or a separate bead."
        stop_if = "Stop if any changed path is outside files_in_play and is not generated Precode output."
        approval_prompt = "Ask the user whether to narrow the change, split a follow-up bead, or explicitly approve the scope change."
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


def gather_markdown_docs(root: Path) -> list[Path]:
    patterns = [
        "*.md",
        "docs/*.md",
        "adapters/*.md",
        "tasks/**/*.md",
        "modes/*.md",
        ".github/copilot-instructions.md",
        "logs/LOG-EVIDENCE-TAXONOMY.md",
        ".claude/commands/*.md",
        ".claude/rules/*.md",
    ]
    paths: set[Path] = set()
    for pattern in patterns:
        for path in root.glob(pattern):
            if path.is_file():
                paths.add(path)
    return sorted(paths)


def surface_group(rel: str) -> str:
    if rel in ACTIVE_MEMORY:
        return "active-memory"
    if rel in SHIM_DOCS:
        return "shim"
    if rel.startswith("adapters/"):
        return "adapter"
    if rel.startswith("docs/"):
        return "doc"
    if rel.startswith("tasks/beads/"):
        return "bead"
    if rel.startswith("tasks/prds/"):
        return "prd"
    if rel.startswith("tasks/reference/"):
        return "reference"
    if rel.startswith("tasks/templates/"):
        return "template"
    if rel.startswith("modes/"):
        return "mode"
    if rel.startswith("logs/"):
        return "log-reference"
    return "doc"


def compile_authority_map(root: Path) -> dict[str, Any]:
    docs: list[dict[str, Any]] = []
    for path in gather_markdown_docs(root):
        rel = rel_path(path, root)
        text = read_text(path)
        contract = extract_contract_values(text)
        if not contract:
            continue
        docs.append(
            {
                "path": rel,
                "title": heading_title(text),
                "anchor": extract_anchor(text),
                "class": contract.get("class"),
                "surface": surface_group(rel),
                "authority": contract.get("authority"),
                "not_authority": contract.get("not_authority"),
                "load_when": contract.get("load_when"),
            }
        )

    return {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "active_memory": ACTIVE_MEMORY,
        "docs": docs,
    }


def script_header(path: Path) -> dict[str, str | None]:
    text = read_text(path)
    version = re.search(r"^# Version:\s*(.+)$", text, re.MULTILINE)
    updated = re.search(r"^# Last updated:\s*(.+)$", text, re.MULTILINE)
    owner = re.search(r"^# Owner:\s*(.+)$", text, re.MULTILINE)
    return {
        "version": version.group(1).strip() if version else None,
        "last_updated": updated.group(1).strip() if updated else None,
        "owner": owner.group(1).strip() if owner else None,
    }


def document_version_metadata(text: str) -> dict[str, str | None]:
    creator = re.search(r"^Creator:\s*(.+)$", text, re.MULTILINE)
    version = re.search(r"^Document version:\s*(.+)$", text, re.MULTILINE)
    updated = re.search(r"^Last updated:\s*(.+)$", text, re.MULTILINE)
    return {
        "creator": creator.group(1).strip() if creator else None,
        "version": version.group(1).strip() if version else None,
        "last_updated": updated.group(1).strip() if updated else None,
    }


def maintained_markdown_docs(root: Path) -> list[Path]:
    return [
        path
        for path in gather_markdown_docs(root)
        if rel_path(path, root) not in {"OS-HEALTH.md", "PRECODE-HELP.md", "PROGRESS.md"}
        and (not rel_path(path, root).startswith("logs/") or rel_path(path, root) == "logs/LOG-EVIDENCE-TAXONOMY.md")
    ]


def workflow_paths(root: Path) -> list[Path]:
    base = root / ".github" / "workflows"
    if not base.is_dir():
        return []
    return sorted([*base.glob("*.yml"), *base.glob("*.yaml")])


def generated_output_paths(root: Path) -> list[Path]:
    paths: set[Path] = set()
    for pattern in ("OS-HEALTH.md", "PRECODE-HELP.md", "PROGRESS.md", "logs/*.md", "logs/*.json", "logs/*.jsonl"):
        for path in root.glob(pattern):
            if path.is_file() and rel_path(path, root) != "logs/LOG-EVIDENCE-TAXONOMY.md":
                paths.add(path)
    return sorted(paths)


def docs_html_paths(root: Path) -> list[Path]:
    base = root / "docs-html"
    if not base.is_dir():
        return []
    return sorted(base.glob("*.html"))


def file_size(path: Path) -> int:
    try:
        if path.is_file():
            return path.stat().st_size
        if path.is_dir():
            return sum(item.stat().st_size for item in path.rglob("*") if item.is_file())
    except OSError:
        return 0
    return 0


def git_command(root: Path, args: list[str]) -> subprocess.CompletedProcess[str] | None:
    try:
        return subprocess.run(
            ["git", *args],
            cwd=root,
            text=True,
            capture_output=True,
            check=False,
        )
    except OSError:
        return None


def git_available(root: Path) -> bool:
    result = git_command(root, ["rev-parse", "--is-inside-work-tree"])
    return bool(result and result.returncode == 0 and result.stdout.strip() == "true")


def git_ignored(root: Path, rel: str) -> bool:
    result = git_command(root, ["check-ignore", "--quiet", rel])
    return bool(result and result.returncode == 0)


def git_tracked(root: Path, rel: str) -> bool:
    result = git_command(root, ["ls-files", "--error-unmatch", rel])
    return bool(result and result.returncode == 0)


def protected_evidence_outputs(root: Path, beads: list[Bead], check_results: list[dict[str, Any]], current_bead: Bead | None) -> set[str]:
    protected_beads: set[str] = set()
    if current_bead:
        protected_beads.add(current_bead.rel_path)
    for bead in beads:
        review_decision = normalize_inline_status_value(bead.closeout.get("review_decision", ""))
        if bead.status != "done" or not any(marker in review_decision for marker in APPROVED_MARKERS):
            protected_beads.add(bead.rel_path)

    outputs: set[str] = set()
    for row in check_results:
        output = str(row.get("output") or "").strip()
        if output and row.get("bead") in protected_beads:
            outputs.add(output)
    return outputs


def local_hygiene_summary(
    root: Path,
    beads: list[Bead],
    check_results: list[dict[str, Any]],
    current_bead: Bead | None,
    *,
    now: datetime | None = None,
) -> dict[str, Any]:
    warnings: list[str] = []
    now = now or datetime.now(timezone.utc)
    cutoff = now.timestamp() - (LOCAL_HYGIENE_RETENTION_DAYS * 24 * 60 * 60)
    protected_outputs = protected_evidence_outputs(root, beads, check_results, current_bead)

    missing_referenced_outputs: list[str] = []
    for row in check_results:
        output = str(row.get("output") or "").strip()
        if output and not (root / output).is_file():
            missing_referenced_outputs.append(output)
    if missing_referenced_outputs:
        warnings.append(f"{len(set(missing_referenced_outputs))} referenced check-output file(s) are missing")

    bulky_outputs: list[dict[str, Any]] = []
    protected_bulky_outputs: list[dict[str, Any]] = []
    for directory in sorted(LOCAL_HYGIENE_BULKY_LOG_DIRS):
        base = root / directory
        if not base.is_dir():
            continue
        for path in sorted(item for item in base.rglob("*") if item.is_file()):
            rel = rel_path(path, root)
            mtime = file_mtime(path) or datetime.fromtimestamp(path.stat().st_mtime, timezone.utc)
            item = {
                "path": rel,
                "bytes": file_size(path),
                "mtime": mtime.isoformat(),
                "age_days": max(0, int((now - mtime).total_seconds() // 86400)),
                "rule": f"bulky generated output older than {LOCAL_HYGIENE_RETENTION_DAYS} days",
            }
            if rel in protected_outputs:
                protected_bulky_outputs.append({**item, "reason": "referenced by current or unaccepted bead evidence"})
                continue
            if path.stat().st_mtime < cutoff:
                bulky_outputs.append(item)

    if bulky_outputs:
        warnings.append(f"{len(bulky_outputs)} bulky log output file(s) exceed {LOCAL_HYGIENE_RETENTION_DAYS}-day retention")

    logs_dir = root / "logs"
    unexpected_logs: list[str] = []
    if logs_dir.is_dir():
        for path in sorted(item for item in logs_dir.rglob("*") if item.is_file()):
            rel = rel_path(path, root)
            top_family = "/".join(rel.split("/")[:2])
            if top_family in LOCAL_HYGIENE_BULKY_LOG_DIRS:
                continue
            if rel not in LOCAL_HYGIENE_EXPECTED_LOG_FILES:
                unexpected_logs.append(rel)
    if unexpected_logs:
        warnings.append(f"{len(unexpected_logs)} unexpected file(s) found under logs/")

    git_ok = git_available(root)
    cache_candidates: list[dict[str, Any]] = []
    cache_observed_not_candidate: list[dict[str, Any]] = []
    for path in sorted(root.rglob("*")):
        if not path.is_dir() or path.name not in LOCAL_HYGIENE_CACHE_NAMES:
            continue
        rel = rel_path(path, root)
        if rel.startswith(".git/") or rel == ".git":
            continue
        ignored = git_ignored(root, rel) if git_ok else False
        tracked = git_tracked(root, rel) if git_ok else False
        item = {
            "path": rel,
            "bytes": file_size(path),
            "rule": "known cache/build/dependency directory that is ignored or untracked",
            "git_ignored": ignored,
            "git_tracked": tracked,
            "git_available": git_ok,
        }
        if ignored or (git_ok and not tracked):
            cache_candidates.append(item)
        else:
            cache_observed_not_candidate.append({**item, "reason": "not proven ignored or untracked"})

    if cache_candidates:
        warnings.append(f"{len(cache_candidates)} ignored or untracked cache/build directorie(s) are cleanup candidates")

    details = {
        "retention_days": LOCAL_HYGIENE_RETENTION_DAYS,
        "advisory_only": True,
        "cleanup_modes_enabled": [],
        "next_safe_action": "review candidates; no files are moved, deleted, archived, or compacted by Local Hygiene v1",
        "bulky_log_candidates": bulky_outputs,
        "bulky_log_candidate_count": len(bulky_outputs),
        "bulky_log_candidate_bytes": sum(item["bytes"] for item in bulky_outputs),
        "cache_candidates": cache_candidates,
        "cache_candidate_count": len(cache_candidates),
        "cache_candidate_bytes": sum(item["bytes"] for item in cache_candidates),
        "protected_evidence_outputs": sorted(protected_outputs),
        "protected_bulky_outputs": protected_bulky_outputs,
        "unexpected_logs": unexpected_logs,
        "missing_referenced_outputs": sorted(set(missing_referenced_outputs)),
        "cache_observed_not_candidate": cache_observed_not_candidate,
        "generated_preview_files": ["logs/local-hygiene-preview.json", "logs/local-hygiene-preview.md"],
        "truth_is_not_cleanup": True,
    }
    return {"status": "warning" if warnings else "pass", "warnings": warnings, "details": details}


def local_hygiene_preview_from_summary(summary: dict[str, Any]) -> dict[str, Any]:
    details = summary.get("details") if isinstance(summary.get("details"), dict) else {}
    actions: list[dict[str, Any]] = []
    for item in details.get("bulky_log_candidates") or []:
        if not isinstance(item, dict):
            continue
        actions.append(
            {
                "action": "would_archive_log_output",
                "path": item.get("path"),
                "bytes": item.get("bytes", 0),
                "reason": item.get("rule"),
                "mutates_now": False,
            }
        )
    for item in details.get("cache_candidates") or []:
        if not isinstance(item, dict):
            continue
        actions.append(
            {
                "action": "would_delete_cache",
                "path": item.get("path"),
                "bytes": item.get("bytes", 0),
                "reason": item.get("rule"),
                "mutates_now": False,
            }
        )
    for path in details.get("protected_evidence_outputs") or []:
        actions.append(
            {
                "action": "protected",
                "path": path,
                "reason": "referenced by current or unaccepted bead evidence",
                "mutates_now": False,
            }
        )

    return {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "status": summary.get("status", "missing"),
        "advisory_only": True,
        "mutates_files": False,
        "warnings": summary.get("warnings") or [],
        "summary": {
            "would_archive_log_output": sum(1 for action in actions if action.get("action") == "would_archive_log_output"),
            "would_delete_cache": sum(1 for action in actions if action.get("action") == "would_delete_cache"),
            "protected": sum(1 for action in actions if action.get("action") == "protected"),
            "candidate_bytes": int(details.get("bulky_log_candidate_bytes") or 0) + int(details.get("cache_candidate_bytes") or 0),
        },
        "actions": actions,
        "source": "scripts/local-hygiene-dry-run.py",
        "next_safe_action": details.get("next_safe_action") or "review candidates only",
    }


def render_local_hygiene_preview_markdown(preview: dict[str, Any]) -> str:
    actions = preview.get("actions") if isinstance(preview.get("actions"), list) else []
    rows = []
    for action in actions:
        if not isinstance(action, dict):
            continue
        rows.append(
            "| "
            + " | ".join(
                [
                    str(action.get("action") or "missing"),
                    f"`{action.get('path') or 'missing'}`",
                    str(action.get("bytes", "")),
                    str(action.get("reason") or "").replace("|", "\\|"),
                ]
            )
            + " |"
        )
    table = "\n".join(
        [
            "| Action | Path | Bytes | Reason |",
            "| --- | --- | --- | --- |",
            *rows,
        ]
    ) if rows else "- No local hygiene actions would be taken."

    warnings = preview.get("warnings") if isinstance(preview.get("warnings"), list) else []
    summary = preview.get("summary") if isinstance(preview.get("summary"), dict) else {}
    return f"""# PrecodeOS -- Local Hygiene Dry-Run Preview
<!-- ANCHOR: local-hygiene-preview -->

> AUTHORITY: Generated preview of local hygiene archive/delete candidates.
> NOT_AUTHORITY: Active memory, task selection, product decisions, implementation plans, bead state, cleanup approval, archive approval, delete approval, or generated progress state.
> LOAD_WHEN: Reviewing local hygiene candidates; never as active session memory or cleanup permission.
> CLASS: generated
>
> Generated from `scripts/local-hygiene-dry-run.py`.
> Do not use this file as active memory.
> This dry-run does not move, delete, archive, compact, or rewrite candidate files.

Generated at: `{preview.get('generated_at')}`

## Summary

- Status: {preview.get('status', 'missing')}
- Advisory only: {preview.get('advisory_only', True)}
- Mutates files: {preview.get('mutates_files', False)}
- Would archive log outputs: {summary.get('would_archive_log_output', 0)}
- Would delete caches: {summary.get('would_delete_cache', 0)}
- Protected evidence entries: {summary.get('protected', 0)}
- Candidate bytes: {summary.get('candidate_bytes', 0)}
- Next safe action: {preview.get('next_safe_action', 'review candidates only')}

## Warnings

{chr(10).join(f"- {warning}" for warning in warnings) if warnings else "- No local hygiene warnings."}

## Planned Actions

{table}
"""


def inventory_family_for(rel: str) -> str:
    if rel in ACTIVE_MEMORY:
        return "active-memory"
    if rel in SHIM_DOCS or rel == ".github/copilot-instructions.md":
        return "shim"
    if rel.startswith("adapters/"):
        return "adapter"
    if rel.startswith("modes/"):
        return "mode"
    if rel.startswith("tasks/reference/"):
        return "reference-protocol"
    if rel.startswith("docs/"):
        return "reader-doc"
    if rel.startswith("tasks/templates/"):
        return "template"
    if rel.startswith("tasks/beads/"):
        return "bead-doc"
    if rel.startswith("tasks/prds/"):
        return "prd-doc"
    if rel.startswith("scripts/"):
        return "script"
    if rel.startswith("memory/"):
        return "reviewed-memory"
    if rel.startswith(".github/workflows/"):
        return "workflow"
    if rel.startswith("logs/"):
        return "generated-evidence"
    if rel in {"OS-HEALTH.md", "PRECODE-HELP.md", "PROGRESS.md"}:
        return "generated-report"
    return "root-doc"


def inventory_family_covered(rel: str, inventory_text: str) -> bool:
    if f"`{rel}`" in inventory_text or rel in inventory_text:
        return True
    family_tokens = [
        ("docs/", "`docs/*.md`"),
        ("docs-html/", "`docs-html/*.html`"),
        ("tasks/reference/", "`tasks/reference/*.md`"),
        ("tasks/templates/", "`tasks/templates/*.md`"),
        ("tasks/beads/", "`tasks/beads/*.md`"),
        ("tasks/prds/", "`tasks/prds/*.md`"),
        ("scripts/", "`scripts/*.py`"),
        ("scripts/", "`scripts/*.sh`"),
        ("adapters/", "`adapters/*.md`"),
        ("modes/", "`modes/*.md`"),
        ("memory/cards/", "`memory/cards/*.md`"),
        (".github/workflows/", "`.github/workflows/*.yml`"),
    ]
    return any(rel.startswith(prefix) and token in inventory_text for prefix, token in family_tokens)


def compile_file_inventory(root: Path) -> dict[str, Any]:
    warnings: list[str] = []
    package_inventory_rel = "docs/PRECODE-PACKAGE-FILE-INVENTORY.md"
    package_inventory_text = read_text(root / package_inventory_rel)

    docs: list[dict[str, Any]] = []
    for path in maintained_markdown_docs(root):
        rel = rel_path(path, root)
        text = read_text(path)
        contract = extract_contract_values(text)
        metadata = document_version_metadata(text)
        if not contract:
            warnings.append(f"{rel} is missing an authority contract")
        if not metadata.get("version") or not metadata.get("last_updated"):
            warnings.append(f"{rel} is missing version metadata")
        if package_inventory_text and not inventory_family_covered(rel, package_inventory_text):
            warnings.append(f"{rel} is not referenced in {package_inventory_rel}")
        docs.append(
            {
                "path": rel,
                "family": inventory_family_for(rel),
                "title": heading_title(text),
                "anchor": extract_anchor(text),
                "class": contract.get("class"),
                "authority": contract.get("authority"),
                "load_when": contract.get("load_when"),
                "version": metadata.get("version"),
                "last_updated": metadata.get("last_updated"),
            }
        )

    scripts: list[dict[str, Any]] = []
    for path in sorted((root / "scripts").glob("*.py")) + sorted((root / "scripts").glob("*.sh")):
        rel = rel_path(path, root)
        header = script_header(path)
        if not header.get("version") or not header.get("last_updated") or header.get("owner") != "PrecodeOS":
            warnings.append(f"{rel} is missing script version header metadata")
        if package_inventory_text and not inventory_family_covered(rel, package_inventory_text):
            warnings.append(f"{rel} is not referenced in {package_inventory_rel}")
        scripts.append({"path": rel, "family": "script", **header})

    workflows: list[dict[str, Any]] = []
    for path in workflow_paths(root):
        rel = rel_path(path, root)
        header = script_header(path)
        if not header.get("version") or not header.get("last_updated") or header.get("owner") != "PrecodeOS":
            warnings.append(f"{rel} is missing workflow version header metadata")
        if package_inventory_text and not inventory_family_covered(rel, package_inventory_text):
            warnings.append(f"{rel} is not referenced in {package_inventory_rel}")
        workflows.append({"path": rel, "family": "workflow", **header})

    docs_html: list[dict[str, Any]] = []
    for path in docs_html_paths(root):
        rel = rel_path(path, root)
        if package_inventory_text and not inventory_family_covered(rel, package_inventory_text):
            warnings.append(f"{rel} is not referenced in {package_inventory_rel}")
        docs_html.append({"path": rel, "family": "generated-docs-html", "bytes": file_size(path)})

    generated: list[dict[str, Any]] = []
    for path in generated_output_paths(root):
        rel = rel_path(path, root)
        text = read_text(path)
        is_markdown = path.suffix == ".md"
        demoted = True
        if is_markdown:
            demoted = "> CLASS: generated" in text and "Do not use this file" in text
            if not demoted:
                warnings.append(f"{rel} does not clearly demote itself as generated output")
        generated.append(
            {
                "path": rel,
                "family": inventory_family_for(rel),
                "documented_as_family": rel.startswith("logs/") and rel != "logs/LOG-EVIDENCE-TAXONOMY.md",
                "generated_demotion": demoted,
            }
        )

    family_counts = Counter(
        item.get("family", "unknown")
        for item in [*docs, *scripts, *workflows, *docs_html, *generated]
        if isinstance(item, dict)
    )

    return {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "status": "warning" if warnings else "pass",
        "warnings": warnings,
        "active_memory": ACTIVE_MEMORY,
        "package_inventory": package_inventory_rel,
        "canonical_inventory": package_inventory_rel,
        "generated_is_not_authority": True,
        "counts": {
            "docs": len(docs),
            "scripts": len(scripts),
            "workflows": len(workflows),
            "docs_html": len(docs_html),
            "generated_outputs": len(generated),
            "families": dict(sorted(family_counts.items())),
        },
        "docs": docs,
        "scripts": scripts,
        "workflows": workflows,
        "docs_html": docs_html,
        "generated_outputs": generated,
        "generated_families": sorted(GENERATED_JSON_FAMILIES),
    }


def shared_command_surface(root: Path) -> list[str]:
    adapter_index_doc = MarkdownDocument.load(root / "adapters" / "ADAPTER-INDEX.md")
    return [strip_inline_code(item) for item in bullet_items(adapter_index_doc.sections.get("Shared Command Surface", ""))]


def compile_adapter_index(root: Path) -> dict[str, Any]:
    commands = shared_command_surface(root)
    adapters: list[dict[str, Any]] = []
    for rel in ADAPTER_DOCS:
        path = root / rel
        if not path.is_file():
            continue
        text = read_text(path)
        contract = extract_contract_values(text)
        adapter_doc = MarkdownDocument.load(path)
        adapter_commands = [strip_inline_code(item) for item in bullet_items(adapter_doc.sections.get("Shared Command Surface", ""))]
        adapters.append(
            {
                "path": rel,
                "title": heading_title(text),
                "load_when": contract.get("load_when"),
                "shared_command_surface_present": bool(adapter_commands),
                "missing_commands": [command for command in commands if command not in adapter_commands],
            }
        )

    return {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "canonical_source": "AGENT.md",
        "shared_command_surface": commands,
        "adapters": adapters,
    }


def compile_shim_index(root: Path) -> dict[str, Any]:
    shims: list[dict[str, Any]] = []
    for rel in SHIM_DOCS:
        path = root / rel
        if not path.is_file():
            continue
        text = read_text(path)
        contract = extract_contract_values(text)
        shims.append(
            {
                "path": rel,
                "title": heading_title(text),
                "load_when": contract.get("load_when"),
                "canonical_target": "AGENT.md",
            }
        )

    return {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "canonical_source": "AGENT.md",
        "shims": shims,
    }


def compile_events(
    check_results: list[dict[str, Any]],
    loop_rows: list[dict[str, Any]],
    handoff_rows: list[dict[str, Any]],
    transition_rows: list[dict[str, Any]],
    spend_rows: list[dict[str, Any]],
    tool_rows: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    events: list[dict[str, Any]] = []

    for row in loop_rows:
        events.append(
            {
                "timestamp": row.get("timestamp"),
                "stream": "loop",
                "entity": "session",
                "action": row.get("event"),
                "bead": row.get("bead"),
                "branch": row.get("branch"),
                "status": row.get("status"),
            }
        )

    for row in handoff_rows:
        events.append(
            {
                "timestamp": row.get("timestamp"),
                "stream": "handoff",
                "entity": "handoff",
                "action": row.get("event") or "handoff",
                "bead": row.get("bead"),
                "branch": row.get("branch"),
                "status": row.get("status"),
                "tool": row.get("tool"),
                "target": row.get("target"),
            }
        )

    for row in transition_rows:
        events.append(
            {
                "timestamp": row.get("timestamp"),
                "stream": "transition",
                "entity": "bead",
                "action": row.get("event") or "bead-promoted",
                "from": row.get("from"),
                "to": row.get("to"),
            }
        )

    for row in check_results:
        events.append(
            {
                "timestamp": row.get("timestamp"),
                "stream": "checks",
                "entity": "check",
                "action": "recorded-check",
                "bead": row.get("bead"),
                "branch": row.get("branch"),
                "status": row.get("status"),
                "command": row.get("command"),
                "cwd": row.get("cwd"),
                "exit_code": row.get("exit_code"),
                "output": row.get("output"),
            }
        )

    for row in spend_rows:
        total_tokens = row.get("total_tokens", row.get("tokens"))
        events.append(
            {
                "timestamp": row.get("timestamp"),
                "stream": "spend",
                "entity": "spend",
                "action": "logged-spend",
                "tool": row.get("tool"),
                "task": row.get("task"),
                "input_tokens": row.get("input_tokens"),
                "output_tokens": row.get("output_tokens"),
                "total_tokens": total_tokens,
                "cost_usd": row.get("cost_usd"),
                "confidence": row.get("confidence"),
                "telemetry_source": row.get("telemetry_source"),
            }
        )

    for row in tool_rows:
        events.append(
            {
                "timestamp": row.get("timestamp"),
                "stream": "tools",
                "entity": "tool-run",
                "action": "logged-tool-run",
                "tool": row.get("tool"),
                "class": row.get("class"),
                "task": row.get("task"),
                "status": row.get("status"),
                "failure_category": row.get("failure_category"),
                "approval_note": row.get("approval_note"),
            }
        )

    return sorted(events, key=lambda item: str(item.get("timestamp") or ""))


def spend_summary(rows: list[dict[str, Any]]) -> dict[str, Any]:
    total_known = 0.0
    known_count = 0
    total_tokens = 0
    known_token_entries = 0
    unknown_cost_entries = 0
    unknown_token_entries = 0
    by_tool: dict[str, dict[str, Any]] = {}
    by_task: dict[str, dict[str, Any]] = {}
    latest_timestamp = None

    def bucket(target: dict[str, dict[str, Any]], key: str) -> dict[str, Any]:
        value = target.setdefault(
            key,
            {
                "entries": 0,
                "known_token_entries": 0,
                "total_tokens": 0,
                "known_cost_entries": 0,
                "known_cost_usd": 0.0,
                "unknown_token_entries": 0,
                "unknown_cost_entries": 0,
            },
        )
        return value

    for row in rows:
        latest_timestamp = max(latest_timestamp or "", str(row.get("timestamp") or "")) or latest_timestamp
        cost = number_or_none(row.get("cost_usd"))
        tokens = int_or_none(row.get("total_tokens", row.get("tokens")))
        tool = str(row.get("tool") or "unknown")
        task = str(row.get("task") or "unknown")
        buckets = [bucket(by_tool, tool), bucket(by_task, task)]

        for item in buckets:
            item["entries"] += 1

        if cost is not None:
            total_known += cost
            known_count += 1
            for item in buckets:
                item["known_cost_entries"] += 1
                item["known_cost_usd"] = round(float(item["known_cost_usd"]) + cost, 4)
        else:
            unknown_cost_entries += 1
            for item in buckets:
                item["unknown_cost_entries"] += 1

        if tokens is not None:
            total_tokens += tokens
            known_token_entries += 1
            for item in buckets:
                item["known_token_entries"] += 1
                item["total_tokens"] += tokens
        else:
            unknown_token_entries += 1
            for item in buckets:
                item["unknown_token_entries"] += 1

    for group in (by_tool, by_task):
        for item in group.values():
            item["known_cost_usd"] = round(float(item["known_cost_usd"]), 4)

    return {
        "entries": len(rows),
        "known_cost_entries": known_count,
        "known_cost_usd": round(total_known, 4),
        "known_token_entries": known_token_entries,
        "total_tokens": total_tokens,
        "unknown_cost_entries": unknown_cost_entries,
        "unknown_token_entries": unknown_token_entries,
        "latest_timestamp": latest_timestamp,
        "by_tool": dict(sorted(by_tool.items())),
        "by_task": dict(sorted(by_task.items())),
    }


def memory_card_paths(root: Path) -> list[Path]:
    base = root / "memory" / "cards"
    if not base.is_dir():
        return []
    return sorted(
        path
        for path in base.glob("*.md")
        if path.name != "MEMORY-CARD-FORMAT.md" and not path.name.lower().startswith("memory-card-template")
    )


def parse_memory_frontmatter(text: str) -> dict[str, Any]:
    match = re.search(r"(?ms)^---\n(.*?)\n---\s*$", text)
    if not match:
        match = re.search(r"(?ms)^---\n(.*?)\n---\s*\n", text)
    if not match:
        return {}

    values: dict[str, Any] = {}
    current_key: str | None = None
    for raw_line in match.group(1).splitlines():
        line = raw_line.rstrip()
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if line.startswith("  - ") and current_key:
            current = values.setdefault(current_key, [])
            if isinstance(current, list):
                current.append(line[4:].strip())
            continue
        if ":" not in line:
            continue
        key, raw_value = line.split(":", 1)
        key = key.strip()
        value = raw_value.strip()
        current_key = key
        if value:
            values[key] = value
        else:
            values[key] = []
    return values


def section_excerpt(text: str, heading: str) -> str:
    doc = MarkdownDocument.from_text(text) if hasattr(MarkdownDocument, "from_text") else None
    if doc:
        return doc.sections.get(heading, "").strip()
    pattern = re.compile(rf"(?ms)^## {re.escape(heading)}\s*\n(.*?)(?=^## |\Z)")
    match = pattern.search(text)
    return match.group(1).strip() if match else ""


def memory_summary(root: Path) -> dict[str, Any]:
    warnings: list[str] = []
    cards: list[dict[str, Any]] = []
    by_category: Counter[str] = Counter()
    by_freshness: Counter[str] = Counter()
    promotion_needed: list[str] = []
    stale_or_superseded: list[str] = []
    glossary_terms: list[dict[str, Any]] = []

    for path in memory_card_paths(root):
        rel = rel_path(path, root)
        text = read_text(path)
        meta = parse_memory_frontmatter(text)
        title = heading_title(text) or path.stem
        category = str(meta.get("category") or "").strip()
        confidence = str(meta.get("confidence") or "").strip()
        freshness = str(meta.get("freshness") or "").strip()
        status = str(meta.get("status") or "").strip()
        sources = normalize_list(meta.get("source_pointers") if isinstance(meta.get("source_pointers"), list) else [meta.get("source_pointers")])
        topics = normalize_list(meta.get("topics") if isinstance(meta.get("topics"), list) else [meta.get("topics")])
        summary_text = section_excerpt(text, "Summary")
        glossary_text = section_excerpt(text, "Project Glossary") or section_excerpt(text, "Glossary Terms") or section_excerpt(text, "Domain Terms")

        if category not in MEMORY_CATEGORIES:
            warnings.append(f"{rel} has missing or unsupported category")
        if confidence not in MEMORY_CONFIDENCE:
            warnings.append(f"{rel} has missing or unsupported confidence")
        if freshness not in MEMORY_FRESHNESS:
            warnings.append(f"{rel} has missing or unsupported freshness")
        if status not in MEMORY_STATUS:
            warnings.append(f"{rel} has missing or unsupported status")
        if not sources:
            warnings.append(f"{rel} has no source pointers")
        if not summary_text:
            warnings.append(f"{rel} has no Summary section")
        if category == "project_glossary":
            normalized_glossary = " ".join(glossary_text.lower().split())
            if not glossary_text or normalized_glossary in {"not applicable", "n/a", "none"}:
                warnings.append(f"{rel} is a project_glossary card with no glossary terms section")
            if not topics and not glossary_text:
                warnings.append(f"{rel} is a project_glossary card with no topics or glossary terms")

        lower_text = text.lower()
        if any(term in lower_text for term in MEMORY_SECRET_TERMS):
            warnings.append(f"{rel} may contain secret-bearing language; review before sharing or exporting")
        if any(term in lower_text for term in MEMORY_AUTHORITY_TERMS):
            warnings.append(f"{rel} may be acting like authority or active task instructions")
        if status == "needs_promotion":
            owner = str(meta.get("authority_owner_if_promoted") or "").strip()
            if not owner or owner.lower() in FRONTMATTER_EMPTY_MARKERS:
                warnings.append(f"{rel} needs promotion but has no authority owner")
            promotion_needed.append(rel)
        if freshness in {"stale", "superseded"} or status in {"superseded", "archived"}:
            stale_or_superseded.append(rel)
        if category == "project_glossary":
            glossary_terms.append(
                {
                    "path": rel,
                    "title": title,
                    "freshness": freshness or "missing",
                    "status": status or "missing",
                    "topics": topics,
                    "authority_owner_if_promoted": str(meta.get("authority_owner_if_promoted") or "none"),
                    "summary": " ".join(summary_text.split())[:240],
                    "glossary_excerpt": " ".join(glossary_text.split())[:360],
                }
            )

        if category:
            by_category[category] += 1
        if freshness:
            by_freshness[freshness] += 1

        cards.append(
            {
                "path": rel,
                "title": title,
                "category": category or "missing",
                "confidence": confidence or "missing",
                "freshness": freshness or "missing",
                "status": status or "missing",
                "related_bead": str(meta.get("related_bead") or "none"),
                "related_prd": str(meta.get("related_prd") or "none"),
                "authority_owner_if_promoted": str(meta.get("authority_owner_if_promoted") or "none"),
                "source_pointers": sources,
                "topics": topics,
                "summary": " ".join(summary_text.split())[:240],
            }
        )

    details = {
        "cards": cards,
        "card_count": len(cards),
        "by_category": dict(sorted(by_category.items())),
        "by_freshness": dict(sorted(by_freshness.items())),
        "glossary_terms": glossary_terms,
        "promotion_needed": promotion_needed,
        "stale_or_superseded": stale_or_superseded,
        "next_human_review_prompt": "Search reviewed memory for relevant lessons, then return to active memory and the active bead before acting.",
    }
    return {"status": "warning" if warnings else "pass", "warnings": warnings, "details": details}


def render_memory_index_markdown(memory: dict[str, Any]) -> str:
    details = memory.get("details") if isinstance(memory.get("details"), dict) else {}
    cards = details.get("cards") if isinstance(details.get("cards"), list) else []
    warnings = memory.get("warnings") if isinstance(memory.get("warnings"), list) else []
    rows: list[str] = []
    for card in cards:
        if not isinstance(card, dict):
            continue
        rows.append(
            "| "
            + " | ".join(
                [
                    f"`{card.get('path', 'missing')}`",
                    str(card.get("category") or "missing"),
                    str(card.get("freshness") or "missing"),
                    str(card.get("status") or "missing"),
                    str(card.get("summary") or "").replace("|", "\\|") or "missing",
                ]
            )
            + " |"
        )
    table = "\n".join(
        [
            "| Card | Category | Freshness | Status | Summary |",
            "| --- | --- | --- | --- | --- |",
            *rows,
        ]
    ) if rows else "- No reviewed memory cards found."

    return f"""# PrecodeOS -- Memory Index
<!-- ANCHOR: memory-index -->

> AUTHORITY: Generated index of reviewed Precode filesystem memory cards.
> NOT_AUTHORITY: Active memory, task selection, product decisions, feature requirements, implementation plans, route structure, schema definitions, bead state, or generated progress state.
> LOAD_WHEN: Searching or auditing reviewed memory; never as active session memory or a task plan.
> CLASS: generated
>
> Generated from reviewed memory cards and `scripts/update-memory-index.py` or `scripts/os-health.py`.
> Do not use this file as active memory.
> Working memory lives in `AGENT.md`, `DECISIONS.md`, and `tasks/todo.md`.

Generated at: `{datetime.now(timezone.utc).isoformat()}`

## Reading Rule

Use this index to find reviewed memory cards. Before acting, return to active memory, the active bead, and the primary authority file.

## Summary

- Status: {memory.get('status', 'missing')}
- Reviewed memory cards: {details.get('card_count', 0)}
- Project glossary cards: {len(details.get('glossary_terms') or [])}
- Promotion-needed cards: {len(details.get('promotion_needed') or [])}
- Stale or superseded cards: {len(details.get('stale_or_superseded') or [])}

## Cards

{table}

## Warnings

{chr(10).join(f"- {warning}" for warning in warnings) if warnings else "- No first-pass memory warnings."}
"""


def compile_state(root: Path, command: str = "", edit_lock: bool = False) -> dict[str, Any]:
    now = datetime.now(timezone.utc).isoformat()
    branch = run_git(["rev-parse", "--abbrev-ref", "HEAD"], root) or "unknown"
    changed = [line for line in run_git(["status", "--short"], root).splitlines() if line.strip()]

    todo = read_todo_state(root)
    beads = [read_bead(path, root) for path in bead_paths(root)]
    bead_map = {bead.rel_path: bead for bead in beads}
    bead_by_id = {bead.bead_id: bead.rel_path for bead in beads}

    check_results = load_jsonl(root / "logs" / "check-results.jsonl")
    loop_rows = load_jsonl(root / "logs" / "loop-runs.jsonl")
    handoff_rows = load_jsonl(root / "logs" / "handoffs.jsonl")
    transition_rows = load_jsonl(root / "logs" / "bead-transitions.jsonl")
    spend_rows = load_jsonl(root / "logs" / "agent-spend.jsonl")
    tool_rows = load_jsonl(root / "logs" / "tool-runs.jsonl")
    events = compile_events(check_results, loop_rows, handoff_rows, transition_rows, spend_rows, tool_rows)

    readiness_by_bead: dict[str, Any] = {}
    bead_status_counts = Counter(bead.status for bead in beads)

    latest_validate = next(
        (row for row in reversed(check_results) if str(row.get("command") or "") == "bash scripts/validate-memory.sh"),
        None,
    )

    current_rel = todo["current_bead"]
    current_bead = bead_map.get(current_rel or "")
    current_checks = latest_by_command(check_results, current_rel if current_bead else None)
    active_bead_checks: list[dict[str, Any]] = []

    for bead in beads:
        latest = latest_by_command(check_results, bead.rel_path)
        start_state = start_readiness(bead, bead_map)
        close_state = close_readiness(bead, latest)
        readiness_by_bead[bead.rel_path] = {
            "bead_id": bead.bead_id,
            "status": bead.status,
            "kind": bead.bead_kind,
            "start": start_state,
            "close": {
                "eligible": close_state["eligible"],
                "blockers": close_state["blockers"],
                "manual_verification": close_state["manual_verification"],
                "review_decision": close_state["review_decision"],
            },
            "follow_up_suggestion": follow_up_suggestion(bead, close_state),
        }
        if current_bead and bead.rel_path == current_bead.rel_path:
            active_bead_checks = close_state["checks"]

    if current_bead:
        verification_quality = evidence_quality(root, current_bead, check_results, changed)
        current_decomposition_quality = decomposition_quality(current_bead)
        promotion_state = promotion_readiness(root, current_bead, bead_map, current_checks)
        readiness_by_bead[current_bead.rel_path]["promote"] = promotion_state
        next_bead = promotion_state.get("next_bead") or find_next_bead(current_bead, root)
        learning = {
            "drift_observed": current_bead.closeout.get("drift_observed", "not recorded"),
            "lesson_to_promote": current_bead.closeout.get("lesson_to_promote", "not recorded"),
            "follow_up_bead_needed": follow_up_suggestion(current_bead, close_readiness(current_bead, current_checks)),
        }
        blocked = {
            "manual_verification": current_bead.closeout.get("manual_verification", "not recorded"),
            "next_bead": current_bead.closeout.get("next_bead", next_bead or "not recorded"),
            "blocked_escape": normalize_inline_status_value(current_bead.closeout.get("blocked_escape", "not recorded")),
        }
    else:
        verification_quality = evidence_quality(root, None, check_results, changed)
        current_decomposition_quality = decomposition_quality(None)
        promotion_state = {"eligible": False, "blockers": ["current bead is missing"], "next_bead": None}
        learning = {
            "drift_observed": "not recorded",
            "lesson_to_promote": "not recorded",
            "follow_up_bead_needed": "not recorded",
        }
        blocked = {
            "manual_verification": "not recorded",
            "next_bead": "not recorded",
            "blocked_escape": "not recorded",
        }

    current_intent_orchestration = intent_orchestration(root, todo, current_bead, beads, check_results, current_checks)
    current_tool_execution = tool_execution_quality(root, current_bead, tool_rows, check_results, changed)
    current_workflow_planning = workflow_planning(root, todo, current_bead, beads)
    current_long_horizon_planning = long_horizon_planning(root, todo, current_bead, beads)
    current_goal_frame = goal_frame_summary(root, current_bead)
    current_completion_handoff = completion_handoff_quality(
        root,
        todo,
        current_bead,
        beads,
        check_results,
        current_checks,
        events,
        promotion_state,
    )
    current_bead_depth = bead_depth_quality(current_bead)
    current_files_in_play_guardrail = files_in_play_guardrail(root, current_bead, command=command, edit_lock=edit_lock)
    current_run_contract = run_contract_quality(current_bead, check_results)
    current_next_step = next_step_guidance(
        root,
        todo,
        current_bead,
        promotion_state,
        current_completion_handoff,
        current_workflow_planning,
        current_bead_depth,
        current_files_in_play_guardrail,
        current_run_contract,
        current_goal_frame,
    )
    current_pattern_guidance = system_design_pattern_guidance(root, todo, current_bead, beads)
    current_memory = memory_summary(root)
    current_file_inventory = compile_file_inventory(root)
    current_local_hygiene = local_hygiene_summary(root, beads, check_results, current_bead)

    loop_metrics = {
        "events": len(events),
        "recorded_checks": sum(1 for event in events if event.get("stream") == "checks"),
        "passing_checks": sum(1 for row in check_results if row.get("status") == "pass"),
        "failing_checks": sum(1 for row in check_results if row.get("status") == "fail"),
        "tool_runs": len(tool_rows),
        "session_start": sum(1 for event in events if event.get("action") == "session-start"),
        "checkpoint": sum(1 for event in events if event.get("action") == "checkpoint"),
        "session_close": sum(1 for event in events if event.get("action") == "session-close"),
        "handoffs": sum(1 for event in events if event.get("stream") == "handoff"),
        "transitions": sum(1 for event in events if event.get("stream") == "transition"),
        "latest_validate_memory": latest_validate,
        "spend": spend_summary(spend_rows),
    }

    return {
        "generated_at": now,
        "app_dir": APP_DIR,
        "active_memory": ACTIVE_MEMORY,
        "branch": branch,
        "changed_path_count": len(changed),
        "changed_paths": changed,
        "todo": todo,
        "current_bead": current_rel,
        "current_bead_status": current_bead.status if current_bead else "missing",
        "bead_status_counts": dict(sorted(bead_status_counts.items())),
        "beads": [
            {
                "rel_path": bead.rel_path,
                "title": bead.title,
                "bead_id": bead.bead_id,
                "status": bead.status,
                "bead_kind": bead.bead_kind,
                "primary_authority": bead.primary_authority,
                "depends_on": bead.depends_on,
                "parent_prd": bead.parent_prd,
                "requirement_ids": bead.requirement_ids,
                "files_in_play": bead.files_in_play,
                "checks": bead.checks,
                "verification_type": bead.verification_type,
                "delegation_mode": bead.delegation_mode,
                "test_strategy": bead.test_strategy,
                "review_context": bead.review_context,
                "complexity": bead.complexity,
                "required_planning_depth": bead.required_planning_depth,
                "autonomy_level": bead.autonomy_level,
                "run_contract": bead.run_contract,
            }
            for bead in beads
        ],
        "bead_by_id": bead_by_id,
        "loop_metrics": loop_metrics,
        "active_bead_checks": active_bead_checks,
        "learning": learning,
        "blocked_escape": blocked,
        "verification_quality": verification_quality,
        "decomposition_quality": current_decomposition_quality,
        "state_integrity": state_integrity(root, todo, current_bead, beads, events),
        "intent_orchestration": current_intent_orchestration,
        "tool_execution": current_tool_execution,
        "workflow_planning": current_workflow_planning,
        "long_horizon_planning": current_long_horizon_planning,
        "goal_frame": current_goal_frame,
        "completion_handoff": current_completion_handoff,
        "next_step": current_next_step,
        "bead_depth": current_bead_depth,
        "files_in_play_guardrail": current_files_in_play_guardrail,
        "run_contract": current_run_contract,
        "pattern_guidance": current_pattern_guidance,
        "memory": current_memory,
        "file_inventory": current_file_inventory,
        "local_hygiene": current_local_hygiene,
        "readiness": {
            "generated_at": now,
            "current_bead": current_rel,
            "current_promotion": promotion_state,
            "beads": readiness_by_bead,
        },
        "authority_map": compile_authority_map(root),
        "adapter_index": compile_adapter_index(root),
        "shim_index": compile_shim_index(root),
        "events": events,
    }


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def render_simple_yaml(value: Any, indent: int = 0) -> str:
    pad = " " * indent
    if isinstance(value, dict):
        lines: list[str] = []
        for key, item in value.items():
            if isinstance(item, (dict, list)):
                lines.append(f"{pad}{key}:")
                lines.append(render_simple_yaml(item, indent + 2))
            else:
                lines.append(f"{pad}{key}: {json.dumps(item)}")
        return "\n".join(lines)
    if isinstance(value, list):
        if not value:
            return f"{pad}[]"
        lines = []
        for item in value:
            if isinstance(item, (dict, list)):
                lines.append(f"{pad}-")
                lines.append(render_simple_yaml(item, indent + 2))
            else:
                lines.append(f"{pad}- {json.dumps(item)}")
        return "\n".join(lines)
    return f"{pad}{json.dumps(value)}"


def write_yaml(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(render_simple_yaml(payload) + "\n", encoding="utf-8")


def write_events_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, separators=(",", ":")) + "\n")


def render_handoff_packet(payload: dict[str, Any]) -> str:
    completion = payload.get("completion_handoff") or {}
    details = completion.get("details") or {}
    packet = details.get("handoff_packet") or {}
    warnings = completion.get("warnings") or []

    def item(name: str) -> str:
        return str(packet.get(name) or "not recorded")

    return f"""# PrecodeOS -- Handoff Packet
<!-- ANCHOR: handoff-packet -->

> AUTHORITY: Generated handoff orientation snapshot for the current PrecodeOS session.
> NOT_AUTHORITY: Active memory, task selection, product decisions, review acceptance, transition approval, implementation plans, or external mutations.
> LOAD_WHEN: Preparing an agent handoff or reviewing completion state; never as active session memory.
> CLASS: generated
>
> Generated from `scripts/os_compiler.py`.
> Generated by PrecodeOS, created by Dan Sears / Recode.
> Do not use this file as active memory.
> Working memory lives in `AGENT.md`, `DECISIONS.md`, and `tasks/todo.md`.

Generated at: `{payload.get('generated_at')}`

## Context Pack

- Active bead: `{item('active bead')}`
- State: `{item('state')}`
- Primary authority: `{item('primary authority')}`
- Next safe action: {item('next safe action')}
- Generated-report warning: {item('generated-report warning')}

## Done When

{item('done-when')}

## Files In Play

{item('files in play')}

## Out Of Scope

{item('out of scope')}

## Checks

{item('checks')}

## Allowed Actions

{item('allowed actions')}

## Proof Needed

{item('proof needed')}

## Stop Conditions

{item('stop conditions')}

## Open Questions

{item('open questions')}

## Latest Evidence

{item('latest evidence')}

## Blockers

{item('blockers')}

## Completion Warnings

{chr(10).join(f"- {warning}" for warning in warnings) if warnings else "- No first-pass completion or handoff warnings."}
"""


def render_precode_help(payload: dict[str, Any]) -> str:
    next_step = payload.get("next_step") or {}
    next_details = next_step.get("details") or {}
    depth = payload.get("bead_depth") or {}
    depth_details = depth.get("details") or {}
    guardrail = payload.get("files_in_play_guardrail") or {}
    guardrail_details = guardrail.get("details") or {}
    run_contract = payload.get("run_contract") or {}
    run_details = run_contract.get("details") or {}
    goal_frame = payload.get("goal_frame") or {}
    goal_details = goal_frame.get("details") or {}
    current_goal = goal_details.get("current") or {}
    blockers = next_details.get("blockers") or []
    load_plan = next_details.get("load_plan") or {}
    context_footprint = next_details.get("context_footprint") or {}

    return f"""# Precode Help
<!-- ANCHOR: precode-help -->

> AUTHORITY: Generated next-step guidance for the current PrecodeOS workspace.
> NOT_AUTHORITY: Active memory, task selection authority, product decisions, implementation plans, review acceptance, bead transition approval, or command approval.
> LOAD_WHEN: A user wants a quick generated hint about what Precode expects next; never as active session memory.
> CLASS: generated
>
> Generated from `scripts/os_compiler.py`.
> Generated by PrecodeOS, created by Dan Sears / Recode.
> Do not use this file as active memory.
> Working memory lives in `AGENT.md`, `DECISIONS.md`, and `tasks/todo.md`.

Generated at: `{payload.get('generated_at')}`

## Next Step

- What to do now: {next_details.get('plain_english_summary', next_details.get('recommended_action', 'repair active state before continuing'))}
- User decision: `{next_details.get('user_decision', 'repair state')}`
- Active bead: `{next_details.get('current_bead', 'missing')}`
- State: `{next_details.get('current_bead_status', 'missing')}`
- Recommended action: {next_details.get('recommended_action', 'repair active state before continuing')}
- Action category: `{next_details.get('action_category', 'unknown')}`
- Single next protocol: `{next_details.get('single_next_protocol', 'not recorded')}`
- Why not more context: {next_details.get('why_not_more_context', 'Load only what the active bead proves is needed.')}
- Stop if: {next_details.get('stop_if', 'stop if workflow, scope, evidence, or approval is unclear')}
- Approval prompt: {next_details.get('approval_prompt', 'No approval prompt compiled.')}
- Needs review: {next_details.get('needs_review', False)}
- Needs transition approval: {next_details.get('needs_transition', False)}
- Next bead: `{next_details.get('next_bead', 'not recorded')}`

## Load Plan

- Router owner: `{load_plan.get('router_owner', 'scripts/next-step.py')}`
- Required first: `{', '.join(load_plan.get('required_first') or [])}`
- Then load: `{', '.join(load_plan.get('then_load') or [])}`
- Single next protocol: `{load_plan.get('single_next_protocol', 'not recorded')}`
- Why not more context: {load_plan.get('why_not_more_context', 'Load only what the active bead proves is needed.')}

## Context Footprint

- Active memory: `{', '.join(context_footprint.get('active_memory') or [])}`
- Active bead: `{context_footprint.get('active_bead', 'missing')}`
- Primary authority: `{context_footprint.get('primary_authority', 'missing')}`
- Required context: `{', '.join(context_footprint.get('required_context') or [])}`
- Conditional references: `{', '.join(context_footprint.get('conditional_references') or []) or 'none'}`
- Generated reports touched: `{', '.join(context_footprint.get('generated_reports_touched') or [])}`
- Approx document lines: `{context_footprint.get('approx_document_lines', 'unknown')}`
- Budget rule: {context_footprint.get('budget_rule', 'Prepare a checkpoint, compaction, restart, or handoff around 80% context usage.')}

## Goal Frame

- Status: {current_goal.get('status', 'none')}
- Owner file: `{current_goal.get('path', 'not recorded')}`
- Horizon: `{current_goal.get('horizon', 'not recorded')}`
- Workflow guidance: `{current_goal.get('workflow_guidance', 'not recorded')}`
- Goal: {current_goal.get('goal', 'not recorded')}
- Reaffirmation trigger: {current_goal.get('reaffirmation_trigger', 'not recorded')}
- Advisory warning: {next_details.get('goal_frame_advisory', 'Goal Frames are advisory only.')}

{chr(10).join(f"- Warning: {warning}" for warning in (goal_frame.get('warnings') or [])) if goal_frame.get('warnings') else "- No Goal Frame warnings."}

## Blockers

{chr(10).join(f"- {blocker}" for blocker in blockers) if blockers else "- No compiled next-step blockers."}

## Adaptive Depth

- Status: {depth.get('status', 'missing')}
- Complexity: `{depth_details.get('complexity', 'unspecified')}`
- Required planning depth: `{depth_details.get('required_planning_depth', 'unspecified')}`
- Autonomy level: `{depth_details.get('autonomy_level', 'unspecified')}`
- User decision: `{depth_details.get('user_decision', 'continue')}`
- Why this matters: {depth_details.get('why_this_matters', 'Adaptive depth keeps planning proportional to risk.')}
- Stop if: {depth_details.get('stop_if', 'Stop if risk and planning depth do not match.')}

{chr(10).join(f"- Warning: {warning}" for warning in (depth.get('warnings') or [])) if depth.get('warnings') else "- No adaptive-depth warnings."}

## Files In Play Guardrail

- Status: {guardrail.get('status', 'missing')}
- Git status available: {guardrail_details.get('git_status_available', False)}
- Changed paths: {len(guardrail_details.get('changed_paths') or [])}
- Out-of-scope paths: {len(guardrail_details.get('out_of_scope_paths') or [])}
- User decision: `{guardrail_details.get('user_decision', 'continue')}`
- Why this matters: {guardrail_details.get('why_this_matters', 'Files in play keep edits inside the approved bead.')}
- Stop if: {guardrail_details.get('stop_if', 'Stop if changed paths are outside files_in_play.')}

{chr(10).join(f"- Warning: {warning}" for warning in (guardrail.get('warnings') or [])) if guardrail.get('warnings') else "- No files-in-play guardrail warnings."}

## Run Contract

- Status: {run_contract.get('status', 'missing')}
- Present: {run_details.get('present', False)}
- Required: {run_details.get('required', False)}
- User decision: `{run_details.get('user_decision', 'continue')}`
- Why this matters: {run_details.get('why_this_matters', 'Run contracts clarify allowed actions and proof needed when risk rises.')}
- Stop if: {run_details.get('stop_if', 'Stop if allowed actions, proof needed, approval gates, or rollback path are unclear.')}

{chr(10).join(f"- Warning: {warning}" for warning in (run_contract.get('warnings') or [])) if run_contract.get('warnings') else "- No run-contract warnings."}
"""


def markdown_table(rows: list[list[str]]) -> str:
    if not rows:
        return ""
    escaped = [[str(cell).replace("|", "\\|") for cell in row] for row in rows]
    header = "| " + " | ".join(escaped[0]) + " |"
    divider = "| " + " | ".join("---" for _ in escaped[0]) + " |"
    body = ["| " + " | ".join(row) + " |" for row in escaped[1:]]
    return "\n".join([header, divider, *body])


def first_bullets(text: str, limit: int = 4) -> list[str]:
    items = bullet_items(text)
    return items[:limit]


def progress_payload(payload: dict[str, Any]) -> dict[str, Any]:
    todo = payload.get("todo") or {}
    todo_sections = todo.get("sections") or {}
    current_checks = payload.get("active_bead_checks") or []
    missing_checks = sum(1 for row in current_checks if row.get("status") == "missing")
    failing_checks = sum(1 for row in current_checks if row.get("status") == "fail")
    passing_checks = sum(1 for row in current_checks if row.get("status") == "pass")
    readiness = payload.get("readiness") or {}
    promotion = readiness.get("current_promotion") or {}
    next_step = payload.get("next_step") or {}
    next_details = next_step.get("details") or {}
    state = payload.get("state_integrity") or {}

    attention: list[str] = []
    if missing_checks:
        attention.append(f"{missing_checks} declared check(s) have no recorded evidence.")
    if failing_checks:
        attention.append(f"{failing_checks} declared check(s) are currently failing.")
    for blocker in (promotion.get("blockers") or [])[:4]:
        attention.append(str(blocker))
    for warning in (next_step.get("warnings") or []):
        text = str(warning)
        if "adaptive depth" in text:
            message = "Planning and proof depth need review before continuing."
        elif "run contract" in text:
            message = "Run contract details may be needed before this bead is accepted."
        else:
            message = text
        if message not in attention:
            attention.append(message)
        if len(attention) >= 7:
            break

    stale_reports = [
        str(warning).split(":", 1)[1].strip()
        for warning in (state.get("warnings") or [])
        if str(warning).startswith("generated report may be stale relative to latest evidence:")
        and "PROGRESS.md" not in str(warning)
    ]
    if stale_reports:
        attention.append("Some generated reports may be stale; refresh generated reports before reviewing them.")
    for warning in (state.get("warnings") or []):
        text = str(warning)
        if text.startswith("generated report may be stale relative to latest evidence:"):
            continue
        if text not in attention:
            attention.append(text)
        if len(attention) >= 8:
            break

    return {
        "generated_at": payload.get("generated_at"),
        "source": "scripts/progress.py or scripts/os-health.py via scripts/os_compiler.py",
        "current_work": {
            "current_bead": payload.get("current_bead") or "missing",
            "status": payload.get("current_bead_status") or "missing",
            "build_lane": todo.get("build_lane") or "not recorded",
            "active_feature_window": todo.get("active_feature_window") or "not recorded",
            "primary_authority": todo.get("primary_authority") or "not recorded",
            "done_when": first_bullets(str(todo_sections.get("Done When", ""))),
            "next_step": next_details.get("plain_english_summary", next_details.get("recommended_action", "repair active state before continuing")),
            "user_decision": next_details.get("user_decision", "repair state"),
            "stop_if": next_details.get("stop_if", "stop if workflow, scope, evidence, or approval is unclear"),
        },
        "completion": {
            "bead_status_counts": payload.get("bead_status_counts") or {},
            "beads": [
                {
                    "bead_id": bead.get("bead_id") or "",
                    "title": bead.get("title") or bead.get("rel_path") or "untitled",
                    "status": bead.get("status") or "missing",
                    "path": bead.get("rel_path") or "",
                }
                for bead in (payload.get("beads") or [])
            ],
        },
        "proof": {
            "declared_checks": len(current_checks),
            "passing_checks": passing_checks,
            "missing_checks": missing_checks,
            "failing_checks": failing_checks,
            "checks": current_checks,
        },
        "needs_attention": attention,
        "boundaries": [
            "Generated reports are evidence only.",
            "Repair owner files first, then regenerate this report.",
            "Active memory remains AGENT.md, DECISIONS.md, and tasks/todo.md.",
        ],
    }


def render_progress_markdown(payload: dict[str, Any]) -> str:
    progress = progress_payload(payload)
    current = progress["current_work"]
    completion = progress["completion"]
    proof = progress["proof"]
    counts = completion.get("bead_status_counts") or {}
    checks = proof.get("checks") or []

    status_rows = [["Status", "Count"]] + [[f"`{status}`", str(count)] for status, count in sorted(counts.items())]
    bead_rows = [["Bead", "Status", "Path"]] + [
        [
            str(bead.get("title") or bead.get("bead_id") or "untitled"),
            f"`{bead.get('status', 'missing')}`",
            f"`{bead.get('path', '')}`",
        ]
        for bead in completion.get("beads", [])
    ]
    check_rows = [["Command", "Status", "Evidence"]] + [
        [
            f"`{row.get('command', 'missing')}`",
            str(row.get("status", "missing")),
            f"`{row.get('output')}`" if row.get("output") else "missing",
        ]
        for row in checks
    ]
    done_when = current.get("done_when") or []
    attention = progress.get("needs_attention") or []

    return f"""# PrecodeOS -- Generated Progress
<!-- ANCHOR: progress -->

> AUTHORITY: Generated user-facing progress snapshot for the current PrecodeOS workspace.
> NOT_AUTHORITY: Active memory, task selection, product decisions, implementation plans, roadmap authority, review acceptance, bead transition approval, or proof by itself.
> LOAD_WHEN: A user wants a short generated answer to where the work is and what appears complete; never as active session memory.
> CLASS: generated
>
> Generated from `scripts/progress.py` or `scripts/os-health.py`.
> Generated by PrecodeOS, created by Dan Sears / Recode.
> Do not use this file as active memory.
> Working memory lives in `AGENT.md`, `DECISIONS.md`, and `tasks/todo.md`.

Generated at: `{progress.get('generated_at')}`

## Where You Are

- Current bead: `{current.get('current_bead')}`
- State: `{current.get('status')}`
- Build lane: {current.get('build_lane')}
- Active feature window: {current.get('active_feature_window')}
- Primary authority: `{current.get('primary_authority')}`
- What to do now: {current.get('next_step')}
- User decision: `{current.get('user_decision')}`
- Stop if: {current.get('stop_if')}

## Done When

{chr(10).join(f"- {item}" for item in done_when) if done_when else "- No current Done When bullets found."}

## Completion Picture

{markdown_table(status_rows) if len(status_rows) > 1 else "- No bead status counts found."}

{markdown_table(bead_rows) if len(bead_rows) > 1 else "- No beads found."}

## Proof Status

- Declared checks: {proof.get('declared_checks', 0)}
- Passing checks: {proof.get('passing_checks', 0)}
- Missing checks: {proof.get('missing_checks', 0)}
- Failing checks: {proof.get('failing_checks', 0)}

{markdown_table(check_rows) if len(check_rows) > 1 else "- No declared active-bead checks found."}

## Needs Attention

{chr(10).join(f"- {item}" for item in attention) if attention else "- No compiled progress blockers or warnings."}

## Boundaries

- Generated reports are evidence only.
- Repair owner files first, then regenerate this report.
- Active memory remains `AGENT.md`, `DECISIONS.md`, and `tasks/todo.md`.
"""


def write_compiled_sidecars(root: Path, payload: dict[str, Any]) -> None:
    write_json(root / "logs" / "authority-map.json", payload["authority_map"])
    write_json(root / "logs" / "adapter-index.json", payload["adapter_index"])
    write_json(root / "logs" / "shim-index.json", payload["shim_index"])
    write_json(root / "logs" / "readiness.json", payload["readiness"])
    write_json(root / "logs" / "orchestration-map.json", payload["intent_orchestration"])
    write_json(root / "logs" / "workflow-map.json", payload["workflow_planning"])
    write_json(root / "logs" / "long-horizon-map.json", payload["long_horizon_planning"])
    write_json(root / "logs" / "goal-frame.json", payload["goal_frame"])
    write_json(root / "logs" / "handoff-packet.json", payload["completion_handoff"])
    write_json(root / "logs" / "next-step.json", payload["next_step"])
    write_json(root / "logs" / "run-contract.json", payload["run_contract"])
    write_yaml(root / "logs" / "run-contract.yaml", payload["run_contract"])
    write_json(root / "logs" / "pattern-guidance.json", payload["pattern_guidance"])
    write_json(root / "logs" / "progress.json", progress_payload(payload))
    write_json(root / "logs" / "memory-index.json", payload["memory"])
    (root / "logs" / "memory-index.md").write_text(render_memory_index_markdown(payload["memory"]), encoding="utf-8")
    write_json(root / "logs" / "file-inventory.json", payload["file_inventory"])
    (root / "logs" / "handoff-packet.md").write_text(render_handoff_packet(payload), encoding="utf-8")
    (root / "PROGRESS.md").write_text(render_progress_markdown(payload), encoding="utf-8")
    (root / "PRECODE-HELP.md").write_text(render_precode_help(payload), encoding="utf-8")
    write_events_jsonl(root / "logs" / "os-events.jsonl", payload["events"])
