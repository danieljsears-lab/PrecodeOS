#!/usr/bin/env python3
# Version: v0.1.0
# Last updated: 2026-04-26
# Owner: Precode OS
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import json
from pathlib import Path
import re
import subprocess
from typing import Any

from os_compiler import repo_root


JSONL = "logs/github-source-intake.jsonl"
MARKDOWN = "logs/github-source-intake.md"


def run(args: list[str], root: Path) -> tuple[int, str]:
    try:
        result = subprocess.run(args, cwd=root, check=False, capture_output=True, text=True, timeout=25)
    except (OSError, subprocess.TimeoutExpired) as exc:
        return 1, str(exc)
    return result.returncode, (result.stdout or result.stderr).strip()


def load_source(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(value, dict):
        return value
    raise ValueError("source JSON must be an object")


def fetch(kind: str, number: str, root: Path) -> tuple[int, dict[str, Any] | None, str]:
    if kind == "issue":
        fields = "number,title,url,state,author,labels,body,comments,createdAt,updatedAt,closedAt"
        code, text = run(["gh", "issue", "view", number, "--json", fields], root)
    else:
        fields = "number,title,url,state,author,labels,body,comments,createdAt,updatedAt,closedAt,reviewDecision,mergeStateStatus,statusCheckRollup"
        code, text = run(["gh", "pr", "view", number, "--json", fields], root)
    if code != 0:
        return code, None, text
    try:
        data = json.loads(text)
    except json.JSONDecodeError as exc:
        return 1, None, f"invalid JSON from gh: {exc}"
    data["_source_kind"] = kind
    return 0, data, ""


def text_excerpt(value: str | None, limit: int = 700) -> str:
    text = re.sub(r"\s+", " ", value or "").strip()
    if len(text) <= limit:
        return text
    return text[: limit - 3].rstrip() + "..."


def label_names(labels: Any) -> list[str]:
    if not isinstance(labels, list):
        return []
    names: list[str] = []
    for label in labels:
        if isinstance(label, dict) and label.get("name"):
            names.append(str(label["name"]))
        elif isinstance(label, str):
            names.append(label)
    return names


def author_name(author: Any) -> str | None:
    if isinstance(author, dict):
        return str(author.get("login") or author.get("name") or "") or None
    if author:
        return str(author)
    return None


def comments_summary(comments: Any) -> list[str]:
    if not isinstance(comments, list):
        return []
    summaries: list[str] = []
    for comment in comments[:5]:
        if not isinstance(comment, dict):
            continue
        body = text_excerpt(comment.get("body"), 220)
        if body:
            summaries.append(body)
    return summaries


def extract_lines(body: str, patterns: list[str]) -> list[str]:
    lines: list[str] = []
    for raw in (body or "").splitlines():
        line = raw.strip(" -*\t")
        if not line:
            continue
        lower = line.lower()
        if any(pattern in lower for pattern in patterns):
            lines.append(line)
    return lines[:8]


def normalize(data: dict[str, Any], source_hint: str) -> dict[str, Any]:
    kind = data.get("_source_kind") or data.get("source_type") or ("pull_request" if data.get("reviewDecision") is not None else "issue")
    body = str(data.get("body") or "")
    comments = comments_summary(data.get("comments"))
    acceptance = extract_lines(body, ["accept", "done when", "success", "verify", "check"])
    questions = extract_lines(body + "\n" + "\n".join(comments), ["?", "question", "unclear", "decide", "blocked"])
    candidates = extract_lines(body, ["must", "should", "need", "allow", "support", "prevent"])

    return {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "source_type": f"github_{kind}",
        "source_reference": data.get("url") or source_hint,
        "number": data.get("number"),
        "title": data.get("title"),
        "state": data.get("state"),
        "author": author_name(data.get("author")),
        "labels": label_names(data.get("labels")),
        "created_at": data.get("createdAt"),
        "updated_at": data.get("updatedAt"),
        "body_summary": text_excerpt(body),
        "comments_summary": comments,
        "acceptance_hints": acceptance,
        "open_questions": questions,
        "candidate_requirements": candidates,
        "candidate_bead_notes": candidates[:3],
        "likely_authority_files": ["tasks/prds/*.md", "FEATURES.md", "DECISIONS.md", "tasks/beads/*.md"],
        "promotion_rule": "Generated GitHub source intake is evidence only. Promote reviewed conclusions through the Local Source Intake Protocol.",
    }


def render_markdown(entries: list[dict[str, Any]]) -> str:
    blocks = [
        "# Precode OS -- GitHub Source Intake",
        "<!-- ANCHOR: github-source-intake -->",
        "",
        "> AUTHORITY: Generated GitHub issue and pull request source-intake summaries.",
        "> NOT_AUTHORITY: Active memory, task selection, product decisions, approved requirements, implementation plans, bead state, or generated progress state.",
        "> LOAD_WHEN: Reviewing GitHub-derived source evidence before promotion into Precode-owned artifacts.",
        "> CLASS: generated",
        ">",
        "> Do not use this file as active memory or as a task plan.",
        "",
        f"Generated at: `{datetime.now(timezone.utc).isoformat()}`",
        "",
        "## Reading Rule",
        "",
        "These summaries are evidence only. A user must promote stable conclusions into a PRD, decision, authority file, or approved bead.",
        "",
    ]
    for entry in entries:
        blocks.extend(
            [
                f"## {entry.get('source_type')} #{entry.get('number')}: {entry.get('title')}",
                "",
                f"- Reference: {entry.get('source_reference')}",
                f"- State: {entry.get('state')}",
                f"- Labels: {', '.join(entry.get('labels') or []) or 'none'}",
                f"- Body summary: {entry.get('body_summary') or 'none'}",
                f"- Acceptance hints: {', '.join(entry.get('acceptance_hints') or []) or 'none found'}",
                f"- Open questions: {', '.join(entry.get('open_questions') or []) or 'none found'}",
                f"- Candidate requirements: {', '.join(entry.get('candidate_requirements') or []) or 'none found'}",
                "",
            ]
        )
    return "\n".join(blocks).rstrip() + "\n"


def append_jsonl(path: Path, entries: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        for entry in entries:
            handle.write(json.dumps(entry, separators=(",", ":")) + "\n")


def main() -> int:
    parser = argparse.ArgumentParser(description="Import GitHub issues or pull requests as generated source-intake evidence.")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--issue", help="GitHub issue number to read with gh")
    group.add_argument("--pr", help="GitHub pull request number to read with gh")
    group.add_argument("--source", help="Local JSON export from gh issue/pr view")
    parser.add_argument("--dry-run", action="store_true", help="print normalized intake without writing logs")
    args = parser.parse_args()

    root = repo_root()
    if args.source:
        path = Path(args.source).expanduser()
        source_path = path if path.is_absolute() else root / path
        if not source_path.is_file():
            print(f"import-github-sources: no importable GitHub source found: source not found: {source_path}")
            return 0
        try:
            data = load_source(source_path)
        except (OSError, ValueError, json.JSONDecodeError) as exc:
            print(f"import-github-sources: no importable GitHub source found: {exc}")
            return 0
        entries = [normalize(data, source_path.as_posix())]
    else:
        kind = "issue" if args.issue else "pr"
        number = args.issue or args.pr or ""
        code, data, error = fetch(kind, number, root)
        if code != 0 or data is None:
            print(f"import-github-sources: no importable GitHub source found: {error}")
            return 0
        entries = [normalize(data, f"github:{kind}:{number}")]

    if args.dry_run:
        print(json.dumps({"entries": entries, "dry_run": True}, indent=2, sort_keys=True))
        return 0

    append_jsonl(root / JSONL, entries)
    (root / MARKDOWN).write_text(render_markdown(entries), encoding="utf-8")
    print(f"import-github-sources: wrote {JSONL} and {MARKDOWN}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
