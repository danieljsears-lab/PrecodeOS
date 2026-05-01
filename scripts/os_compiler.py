#!/usr/bin/env python3
# Version: v0.1.2
# Last updated: 2026-04-27
# Owner: Precode OS
from __future__ import annotations

from collections import Counter
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
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


APP_DIR = "app"
ACTIVE_MEMORY = ["AGENT.md", "DECISIONS.md", "tasks/todo.md"]
SHIM_DOCS = ["AGENTS.md", "GEMINI.md", ".github/copilot-instructions.md", "CLAUDE.md"]
ADAPTER_DOCS = [
    "adapters/README.md",
    "adapters/CLAUDE.md",
    "adapters/CODEX.md",
    "adapters/GEMINI.md",
    "adapters/ANTIGRAVITY.md",
    "adapters/CURSOR.md",
]
FRONTMATTER_EMPTY_MARKERS = {"", "none", "n/a", "na", "null", "not applicable"}
PENDING_MARKERS = {"pending", "blocked", "not recorded", "unavailable", "missing", "fail", "failed", "needs_info", "manual_testing"}
APPROVED_MARKERS = ("accepted", "approve", "approved")
VERIFICATION_TIERS = {"static", "unit", "integration", "browser", "manual", "external"}
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
GENERATED_REPORTS = ["PROGRESS.md", "OS-HEALTH.md", "logs/learning-diary.md", "logs/memory-index.md", "logs/scheduled-audit.md"]
LOOP_FRESHNESS_REPORTS = {"OS-HEALTH.md", "logs/learning-diary.md", "logs/memory-index.md", "logs/scheduled-audit.md"}
GENERATED_JSON_FAMILIES = {
    "logs/*.json",
    "logs/*.jsonl",
    "logs/check-output/*",
    "logs/scheduled-audit-output/*",
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
    return sorted(path for path in (root / "tasks" / "beads").glob("*.md") if path.name != "README.md")


def parse_closeout_values(section: str) -> dict[str, str]:
    return colon_bullets(section)


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
        if path not in files_in_play
        and not path.startswith("logs/")
        and path not in {"OS-HEALTH.md", "PROGRESS.md"}
    ]
    code_changing = any(looks_code_path(path) for path in changed_names + bead.files_in_play)
    bead_rows = [row for row in check_results if row.get("bead") == bead.rel_path]
    passing_commands = [str(row.get("command") or "") for row in bead_rows if row.get("status") == "pass"]
    tier_set = set(tier.lower() for tier in bead.verification_type)
    inferred_tiers = check_tiers(passing_commands)
    known_tiers = sorted((tier_set & VERIFICATION_TIERS) | inferred_tiers)

    if code_changing and passing_commands and set(passing_commands) <= {"bash scripts/validate-memory.sh"}:
        warnings.append("only memory validation is recorded for a code-changing bead")
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
        "known_tiers": known_tiers,
        "code_changing": code_changing,
        "recorded_pass_commands": passing_commands,
        "changed_outside_files_in_play": outside_files,
        "sensitive_surface_detected": sensitive,
    }
    return {"status": "warning" if warnings else "pass", "warnings": warnings, "details": details}


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

    details = {
        "bead": bead.rel_path,
        "bead_kind": bead.bead_kind,
        "primary_authority": bead.primary_authority,
        "files_in_play_count": len(files),
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
        if path.name == "README.md":
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
    if latest_check and (latest_close is None or latest_close < latest_check):
        warnings.append("active bead has recorded evidence newer than the latest session close")

    required_context = {
        "active bead": bead.rel_path,
        "state": bead.status,
        "done-when": todo_sections.get("Done When", ""),
        "primary authority": bead.primary_authority,
        "files in play": "\n".join(bead.files_in_play),
        "out of scope": todo_sections.get("Explicit Out-of-Scope", ""),
        "checks": "\n".join(bead.checks),
        "stop conditions": bead.sections.get("Stop If", ""),
        "open questions": todo_sections.get("Open Questions", ""),
        "latest evidence": bead_rows[-1].get("output") if bead_rows else "",
        "blockers": "; ".join(promotion_state.get("blockers", [])),
        "next safe action": "",
        "generated-report warning": "Generated reports are evidence only.",
    }

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


def gather_markdown_docs(root: Path) -> list[Path]:
    patterns = [
        "*.md",
        "adapters/*.md",
        "tasks/**/*.md",
        "modes/*.md",
        ".github/copilot-instructions.md",
        "logs/README.md",
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
    if rel.startswith("tasks/beads/"):
        return "bead"
    if rel.startswith("tasks/prds/"):
        return "prd"
    if rel.startswith("tasks/reference/"):
        return "reference"
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
        if rel_path(path, root) not in {"OS-HEALTH.md", "PROGRESS.md"}
        and (not rel_path(path, root).startswith("logs/") or rel_path(path, root) == "logs/README.md")
    ]


def workflow_paths(root: Path) -> list[Path]:
    base = root / ".github" / "workflows"
    if not base.is_dir():
        return []
    return sorted([*base.glob("*.yml"), *base.glob("*.yaml")])


def generated_output_paths(root: Path) -> list[Path]:
    paths: set[Path] = set()
    for pattern in ("OS-HEALTH.md", "PROGRESS.md", "logs/*.md", "logs/*.json", "logs/*.jsonl"):
        for path in root.glob(pattern):
            if path.is_file() and rel_path(path, root) != "logs/README.md":
                paths.add(path)
    return sorted(paths)


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
    if rel in {"OS-HEALTH.md", "PROGRESS.md"}:
        return "generated-report"
    return "root-doc"


def inventory_family_covered(rel: str, inventory_text: str) -> bool:
    if f"`{rel}`" in inventory_text or rel in inventory_text:
        return True
    family_tokens = [
        ("tasks/reference/", "`tasks/reference/*.md`"),
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
    inventory_path = root / "PRECODE-FILE-INVENTORY.md"
    inventory_text = read_text(inventory_path)

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
        if inventory_text and not inventory_family_covered(rel, inventory_text):
            warnings.append(f"{rel} is not referenced in PRECODE-FILE-INVENTORY.md")
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
        if not header.get("version") or not header.get("last_updated") or header.get("owner") != "Precode OS":
            warnings.append(f"{rel} is missing script version header metadata")
        if inventory_text and not inventory_family_covered(rel, inventory_text):
            warnings.append(f"{rel} is not referenced in PRECODE-FILE-INVENTORY.md")
        scripts.append({"path": rel, "family": "script", **header})

    workflows: list[dict[str, Any]] = []
    for path in workflow_paths(root):
        rel = rel_path(path, root)
        header = script_header(path)
        if not header.get("version") or not header.get("last_updated") or header.get("owner") != "Precode OS":
            warnings.append(f"{rel} is missing workflow version header metadata")
        if inventory_text and not inventory_family_covered(rel, inventory_text):
            warnings.append(f"{rel} is not referenced in PRECODE-FILE-INVENTORY.md")
        workflows.append({"path": rel, "family": "workflow", **header})

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
                "documented_as_family": rel.startswith("logs/") and rel != "logs/README.md",
                "generated_demotion": demoted,
            }
        )

    family_counts = Counter(
        item.get("family", "unknown")
        for item in [*docs, *scripts, *workflows, *generated]
        if isinstance(item, dict)
    )

    return {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "status": "warning" if warnings else "pass",
        "warnings": warnings,
        "active_memory": ACTIVE_MEMORY,
        "canonical_inventory": "PRECODE-FILE-INVENTORY.md",
        "generated_is_not_authority": True,
        "counts": {
            "docs": len(docs),
            "scripts": len(scripts),
            "workflows": len(workflows),
            "generated_outputs": len(generated),
            "families": dict(sorted(family_counts.items())),
        },
        "docs": docs,
        "scripts": scripts,
        "workflows": workflows,
        "generated_outputs": generated,
        "generated_families": sorted(GENERATED_JSON_FAMILIES),
    }


def shared_command_surface(root: Path) -> list[str]:
    adapter_index_doc = MarkdownDocument.load(root / "adapters" / "README.md")
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
        if path.name != "README.md" and not path.name.lower().startswith("memory-card-template")
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

    return f"""# Precode OS -- Memory Index
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
- Promotion-needed cards: {len(details.get('promotion_needed') or [])}
- Stale or superseded cards: {len(details.get('stale_or_superseded') or [])}

## Cards

{table}

## Warnings

{chr(10).join(f"- {warning}" for warning in warnings) if warnings else "- No first-pass memory warnings."}
"""


def compile_state(root: Path) -> dict[str, Any]:
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
    current_pattern_guidance = system_design_pattern_guidance(root, todo, current_bead, beads)
    current_memory = memory_summary(root)
    current_file_inventory = compile_file_inventory(root)

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
        "completion_handoff": current_completion_handoff,
        "pattern_guidance": current_pattern_guidance,
        "memory": current_memory,
        "file_inventory": current_file_inventory,
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

    return f"""# Precode OS -- Handoff Packet
<!-- ANCHOR: handoff-packet -->

> AUTHORITY: Generated handoff orientation snapshot for the current Precode OS session.
> NOT_AUTHORITY: Active memory, task selection, product decisions, review acceptance, transition approval, implementation plans, or external mutations.
> LOAD_WHEN: Preparing an agent handoff or reviewing completion state; never as active session memory.
> CLASS: generated
>
> Generated from `scripts/os_compiler.py`.
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


def write_compiled_sidecars(root: Path, payload: dict[str, Any]) -> None:
    write_json(root / "logs" / "authority-map.json", payload["authority_map"])
    write_json(root / "logs" / "adapter-index.json", payload["adapter_index"])
    write_json(root / "logs" / "shim-index.json", payload["shim_index"])
    write_json(root / "logs" / "readiness.json", payload["readiness"])
    write_json(root / "logs" / "orchestration-map.json", payload["intent_orchestration"])
    write_json(root / "logs" / "workflow-map.json", payload["workflow_planning"])
    write_json(root / "logs" / "long-horizon-map.json", payload["long_horizon_planning"])
    write_json(root / "logs" / "handoff-packet.json", payload["completion_handoff"])
    write_json(root / "logs" / "pattern-guidance.json", payload["pattern_guidance"])
    write_json(root / "logs" / "memory-index.json", payload["memory"])
    (root / "logs" / "memory-index.md").write_text(render_memory_index_markdown(payload["memory"]), encoding="utf-8")
    write_json(root / "logs" / "file-inventory.json", payload["file_inventory"])
    (root / "logs" / "handoff-packet.md").write_text(render_handoff_packet(payload), encoding="utf-8")
    write_events_jsonl(root / "logs" / "os-events.jsonl", payload["events"])
