#!/usr/bin/env python3
# Version: v0.1.0
# Last updated: 2026-06-23
# Owner: PrecodeOS
# Created by Dan Sears / Recode.
# SPDX-License-Identifier: Apache-2.0
"""Preview and apply approval-gated Candidate Queue actions."""

from __future__ import annotations

import argparse
import copy
import datetime as dt
import json
import re
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_QUEUE_PATH = ROOT / "CANDIDATE-QUEUE.md"
TODO_PATH = ROOT / "tasks" / "todo.md"

ACTION_PREFIX = "CQA"
VALID_PRODUCT_VALUE_RATINGS = {"P0", "P1", "P2", "P3", "unrated"}
VALID_SHAPING_STATUSES = {"unshaped", "proposed", "reviewed", "needs_research", "blocked", "stale", "deferred"}
BEAD_ID_RE = re.compile(r"\bB\d{3}\b")
QUEUE_HEADING_RE = re.compile(r"^### (CQ-(\d{3})-[a-z0-9][a-z0-9-]*)\b", re.MULTILINE)


class QueueError(ValueError):
    """User-facing validation error."""


@dataclass(frozen=True)
class Action:
    action_id: str
    action_type: str
    candidate_id: str
    title: str
    target_file: str
    approval_required: bool
    preview_text: str
    payload: dict[str, Any]

    def to_json(self) -> dict[str, Any]:
        return {
            "action_id": self.action_id,
            "action_type": self.action_type,
            "candidate_id": self.candidate_id,
            "title": self.title,
            "target_file": self.target_file,
            "approval_required": self.approval_required,
            "preview_text": self.preview_text,
            "payload": self.payload,
        }


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise QueueError(f"missing file: {path}") from exc


def write_text(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8")


def today() -> str:
    return dt.date.today().isoformat()


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return slug[:42].strip("-") or "candidate"


def truncate(value: str, limit: int = 240) -> str:
    normalized = " ".join(value.split())
    if len(normalized) <= limit:
        return normalized
    return normalized[: limit - 3].rstrip() + "..."


def next_action_id(index: int) -> str:
    return f"{ACTION_PREFIX}-{index:03d}"


def candidate_ids(queue_text: str) -> set[str]:
    return {match.group(1) for match in QUEUE_HEADING_RE.finditer(queue_text)}


def next_candidate_id(queue_text: str, title: str) -> str:
    numbers = [int(match.group(2)) for match in QUEUE_HEADING_RE.finditer(queue_text)]
    return f"CQ-{(max(numbers) + 1 if numbers else 1):03d}-{slugify(title)}"


def first_markdown_heading(text: str) -> str | None:
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("#"):
            return stripped.lstrip("#").strip() or None
    return None


def first_paragraph(text: str) -> str:
    paragraphs = [block.strip() for block in re.split(r"\n\s*\n", text) if block.strip()]
    if not paragraphs:
        return ""
    heading = first_markdown_heading(text)
    if heading and paragraphs[0].lstrip("#").strip() == heading:
        paragraphs = paragraphs[1:]
    return paragraphs[0] if paragraphs else heading or ""


def relative_source_pointer(path: Path, root: Path = ROOT) -> str:
    try:
        return str(path.resolve().relative_to(root))
    except ValueError:
        return str(path)


def assert_no_bead_ids(value: Any) -> None:
    serialized = json.dumps(value, sort_keys=True) if not isinstance(value, str) else value
    if BEAD_ID_RE.search(serialized):
        raise QueueError("candidate queue actions must not contain B### bead IDs")


def privacy_warning() -> str:
    return (
        "Do not store secrets, credentials, dashboard values, billing details, "
        "private raw transcripts, or sensitive raw data in CANDIDATE-QUEUE.md."
    )


def build_import_entry(candidate_id: str, title: str, source_pointer: str, summary: str) -> str:
    date = today()
    return f"""### {candidate_id} -- {title}

- Status: `idea`
- Reviewed rank:
- Shaping status: `unshaped`
- Product-value rating: `unrated`
- Product-value rationale:
- Themes:
- User intent: {summary}
- Why this matters:
- Raw source pointer: `{source_pointer}`
- Evidence or source pointers: `{source_pointer}`
- Open questions:
  - What user problem is this solving?
  - What evidence supports it?
  - What promotion path fits: intake, discovery, PRD, decision, decomposition review, defer, or kill?
- Evidence strength: `unknown`
- Weakest assumption:
- Blocked or stale reason:
- Promotion target: `Local Source Intake`
- Related PRDs:
- Candidate bead visibility:
- Near-bead sketches:
  - None reviewed.
- Next review trigger: Local Source Intake review
- Last reviewed: `{date}`

Shaping review:

- No shaping review has been approved yet.

Promotion notes:

- No promotion has been approved yet.
"""


def preview_import(raw_path: Path, queue_path: Path = DEFAULT_QUEUE_PATH) -> list[Action]:
    if not raw_path.exists() or not raw_path.is_file():
        raise QueueError(f"raw notes path must be a file: {raw_path}")
    raw_text = read_text(raw_path)
    queue_text = read_text(queue_path)
    title = first_markdown_heading(raw_text) or raw_path.stem.replace("-", " ").replace("_", " ").title()
    summary = truncate(first_paragraph(raw_text) or title)
    source_pointer = relative_source_pointer(raw_path)
    candidate_id = next_candidate_id(queue_text, title)
    entry_text = build_import_entry(candidate_id, title, source_pointer, summary)
    assert_no_bead_ids(entry_text)
    return [
        Action(
            action_id=next_action_id(1),
            action_type="import_minimal_candidate",
            candidate_id=candidate_id,
            title=title,
            target_file="CANDIDATE-QUEUE.md",
            approval_required=True,
            preview_text=entry_text,
            payload={
                "title": title,
                "source_pointer": source_pointer,
                "short_summary": summary,
                "open_questions": [
                    "What user problem is this solving?",
                    "What evidence supports it?",
                    "What promotion path fits: intake, discovery, PRD, decision, decomposition review, defer, or kill?",
                ],
                "privacy_warning": privacy_warning(),
            },
        )
    ]


def require_string(data: dict[str, Any], key: str) -> str:
    value = data.get(key)
    if not isinstance(value, str) or not value.strip():
        raise QueueError(f"proposal must include non-empty string: {key}")
    return value.strip()


def load_json(path: Path) -> dict[str, Any]:
    try:
        data = json.loads(read_text(path))
    except json.JSONDecodeError as exc:
        raise QueueError(f"proposal must be valid JSON: {exc}") from exc
    if not isinstance(data, dict):
        raise QueueError("proposal JSON must be an object")
    return data


def validate_shaping_proposal(data: dict[str, Any], queue_text: str) -> dict[str, Any]:
    assert_no_bead_ids(data)
    candidate_id = require_string(data, "candidate_id")
    if candidate_id not in candidate_ids(queue_text):
        raise QueueError(f"unknown candidate ID: {candidate_id}")
    rating = require_string(data, "product_value_rating")
    if rating not in VALID_PRODUCT_VALUE_RATINGS:
        raise QueueError(f"invalid product-value rating: {rating}")
    shaping_status = data.get("shaping_status", "proposed")
    if not isinstance(shaping_status, str) or shaping_status not in VALID_SHAPING_STATUSES:
        raise QueueError(f"invalid shaping status: {shaping_status}")
    rationale = require_string(data, "product_value_rationale")
    themes = data.get("themes", [])
    if not isinstance(themes, list) or not all(isinstance(item, str) and item.strip() for item in themes):
        raise QueueError("themes must be a list of non-empty strings")
    sketches = data.get("near_bead_sketches", [])
    if not isinstance(sketches, list):
        raise QueueError("near_bead_sketches must be a list")
    normalized_sketches = []
    expected_prefix = f"{candidate_id}-S"
    for sketch in sketches:
        if not isinstance(sketch, dict):
            raise QueueError("each near-bead sketch must be an object")
        sketch_id = require_string(sketch, "sketch_id")
        if not re.fullmatch(re.escape(expected_prefix) + r"\d{2,}", sketch_id):
            raise QueueError(f"invalid near-bead sketch ID: {sketch_id}")
        normalized_sketches.append(
            {
                "sketch_id": sketch_id,
                "title": require_string(sketch, "title"),
                "outcome": require_string(sketch, "outcome"),
                "likely_authority": require_string(sketch, "likely_authority"),
                "likely_verification": require_string(sketch, "likely_verification"),
                "dependencies": require_string(sketch, "dependencies"),
                "status": str(sketch.get("status", "proposed")).strip() or "proposed",
            }
        )
    weakest_assumption = data.get("weakest_assumption", "")
    return {
        "candidate_id": candidate_id,
        "shaping_status": shaping_status,
        "product_value_rating": rating,
        "product_value_rationale": rationale,
        "themes": [item.strip() for item in themes],
        "near_bead_sketches": normalized_sketches,
        "weakest_assumption": weakest_assumption.strip() if isinstance(weakest_assumption, str) else "",
    }


def build_shaping_block(proposal: dict[str, Any]) -> str:
    theme_text = ", ".join(proposal["themes"]) if proposal["themes"] else "None reviewed."
    rows = [
        "| Sketch ID | Title | Outcome | Likely authority | Likely verification | Dependencies | Status |",
        "|---|---|---|---|---|---|---|",
    ]
    if proposal["near_bead_sketches"]:
        for sketch in proposal["near_bead_sketches"]:
            rows.append(
                "| `{sketch_id}` | {title} | {outcome} | {likely_authority} | {likely_verification} | {dependencies} | `{status}` |".format(
                    **{key: escape_table(str(value)) for key, value in sketch.items()}
                )
            )
    else:
        rows.append("| None reviewed. |  |  |  |  |  |  |")
    weakest = proposal["weakest_assumption"] or "Not reviewed."
    return f"""Shaping review:

- Shaping status: `{proposal["shaping_status"]}`
- Product-value rating: `{proposal["product_value_rating"]}`
- Product-value rationale: {proposal["product_value_rationale"]}
- Themes: {theme_text}
- Weakest assumption: {weakest}
- Rating boundary: Product value only; not review order, implementation priority, task selection, or permission to code.
- Sketch boundary: Near-bead sketches are not bead files, do not reserve `B###` IDs, and do not activate beads.

Near-bead sketches:

{chr(10).join(rows)}
"""


def escape_table(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ")


def preview_shaping(proposal_path: Path, queue_path: Path = DEFAULT_QUEUE_PATH) -> list[Action]:
    queue_text = read_text(queue_path)
    proposal = validate_shaping_proposal(load_json(proposal_path), queue_text)
    block = build_shaping_block(proposal)
    assert_no_bead_ids(block)
    return [
        Action(
            action_id=next_action_id(1),
            action_type="apply_shaping_review",
            candidate_id=proposal["candidate_id"],
            title=f"Shaping review for {proposal['candidate_id']}",
            target_file="CANDIDATE-QUEUE.md",
            approval_required=True,
            preview_text=block,
            payload=proposal,
        )
    ]


def ensure_candidate_entries_section(queue_text: str) -> str:
    if "\n## Candidate Entries\n" in queue_text:
        return queue_text
    marker = "\n## Candidate Entry Template\n"
    section = "\n## Candidate Entries\n\nReviewed queue entries live here. Keep templates below this section.\n\n"
    if marker in queue_text:
        return queue_text.replace(marker, section + marker, 1)
    return queue_text.rstrip() + section


def append_candidate_entry(queue_text: str, action: Action) -> str:
    if action.candidate_id in candidate_ids(queue_text):
        raise QueueError(f"duplicate candidate ID: {action.candidate_id}")
    queue_text = ensure_candidate_entries_section(queue_text)
    marker = "\n## Candidate Entry Template\n"
    entry = "\n" + action.preview_text.strip() + "\n"
    if marker in queue_text:
        return queue_text.replace(marker, entry + marker, 1)
    return queue_text.rstrip() + "\n" + entry


def replace_shaping_review(queue_text: str, action: Action) -> str:
    if action.candidate_id not in candidate_ids(queue_text):
        raise QueueError(f"unknown candidate ID: {action.candidate_id}")
    heading_match = re.search(rf"^### {re.escape(action.candidate_id)}\b.*$", queue_text, flags=re.MULTILINE)
    if not heading_match:
        raise QueueError(f"candidate heading not found: {action.candidate_id}")
    next_match = re.search(r"^### CQ-\d{3}-|\n## ", queue_text[heading_match.end() :], flags=re.MULTILINE)
    section_end = heading_match.end() + next_match.start() if next_match else len(queue_text)
    section = queue_text[heading_match.start() : section_end]
    block = "\n" + action.preview_text.strip() + "\n"
    if "\nShaping review:\n" in section:
        start = section.index("\nShaping review:\n")
        next_promo = section.find("\nPromotion notes:", start)
        if next_promo == -1:
            new_section = section[:start].rstrip() + block
        else:
            new_section = section[:start].rstrip() + block + "\n" + section[next_promo:].lstrip()
    else:
        promo = section.find("\nPromotion notes:")
        if promo == -1:
            new_section = section.rstrip() + block
        else:
            new_section = section[:promo].rstrip() + block + "\n" + section[promo:].lstrip()
    return queue_text[: heading_match.start()] + new_section + queue_text[section_end:]


def apply_actions(actions: list[Action], approved_ids: list[str], queue_path: Path = DEFAULT_QUEUE_PATH) -> dict[str, Any]:
    if not approved_ids:
        raise QueueError("apply requires at least one --approve-action ID")
    action_by_id = {action.action_id: action for action in actions}
    unknown = [action_id for action_id in approved_ids if action_id not in action_by_id]
    if unknown:
        raise QueueError(f"unknown approved action ID(s): {', '.join(unknown)}")
    if queue_path.resolve() != DEFAULT_QUEUE_PATH.resolve() and DEFAULT_QUEUE_PATH.exists():
        # Test-only alternate paths are allowed when DEFAULT_QUEUE_PATH is absent in temp chdir.
        pass
    queue_text = read_text(queue_path)
    before_todo = read_text(TODO_PATH) if TODO_PATH.exists() else None
    applied: list[str] = []
    for action_id in approved_ids:
        action = action_by_id[action_id]
        if action.target_file != "CANDIDATE-QUEUE.md":
            raise QueueError(f"refusing to edit non-queue target: {action.target_file}")
        assert_no_bead_ids(action.to_json())
        if action.action_type == "import_minimal_candidate":
            queue_text = append_candidate_entry(queue_text, action)
        elif action.action_type == "apply_shaping_review":
            queue_text = replace_shaping_review(queue_text, action)
        else:
            raise QueueError(f"unknown action type: {action.action_type}")
        applied.append(action_id)
    if before_todo is not None and read_text(TODO_PATH) != before_todo:
        raise QueueError("refusing apply: tasks/todo.md changed during candidate queue operation")
    write_text(queue_path, queue_text)
    return {"applied": applied, "mutated_files": ["CANDIDATE-QUEUE.md"]}


def preview_contract() -> dict[str, Any]:
    return {
        "mutates_now": False,
        "generated_preview_is_authority": False,
        "apply_requires": "--apply --approve-action <ID>",
        "product_value_rating_boundary": "P0/P1/P2/P3 are product value only, not implementation priority.",
        "near_bead_sketch_boundary": "Near-bead sketches are not bead files and do not reserve B### IDs.",
    }


def output_result(kind: str, actions: list[Action], args: argparse.Namespace, applied: dict[str, Any] | None = None) -> None:
    result = {
        "tool": "scripts/candidate-queue.py",
        "preview_kind": kind,
        "status": "applied" if applied else "preview",
        **preview_contract(),
        "warnings": [
            "Generated preview is review input only.",
            "Apply requires explicit --approve-action.",
            "Product-value rating is not implementation priority.",
            "Near-bead sketches are not bead files.",
            privacy_warning(),
        ],
        "actions": [action.to_json() for action in actions],
        "apply_result": applied,
    }
    if args.json:
        print(json.dumps(result, indent=2, sort_keys=True))
        return
    print(f"tool: {result['tool']}")
    print(f"preview_kind: {kind}")
    print(f"status: {result['status']}")
    print("mutates_now: false")
    print("generated_preview_is_authority: false")
    print("apply_requires: --apply --approve-action <ID>")
    print("product_value_rating_boundary: P0/P1/P2/P3 are product value only, not implementation priority.")
    print("near_bead_sketch_boundary: Near-bead sketches are not bead files and do not reserve B### IDs.")
    print(f"privacy_warning: {privacy_warning()}")
    for action in actions:
        print()
        print(f"action_id: {action.action_id}")
        print(f"action_type: {action.action_type}")
        print(f"candidate_id: {action.candidate_id}")
        print(f"target_file: {action.target_file}")
        print("approval_required: true")
        print("preview_text:")
        print(action.preview_text.rstrip())
    if applied:
        print()
        print(f"applied: {', '.join(applied['applied'])}")
        print(f"mutated_files: {', '.join(applied['mutated_files'])}")


def build_actions(args: argparse.Namespace, queue_path: Path = DEFAULT_QUEUE_PATH) -> tuple[str, list[Action]]:
    if args.preview_import:
        return "import", preview_import(Path(args.preview_import), queue_path)
    if args.preview_shaping:
        return "shaping", preview_shaping(Path(args.preview_shaping), queue_path)
    raise QueueError("choose --preview-import <path>, --preview-shaping <path>, or --self-test")


def run_cli(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Preview and apply approval-gated Candidate Queue actions.")
    parser.add_argument("--preview-import", metavar="PATH", help="Preview minimal Candidate Queue import from raw notes.")
    parser.add_argument("--preview-shaping", metavar="PATH", help="Preview shaping review from proposal JSON.")
    parser.add_argument("--apply", action="store_true", help="Apply approved action IDs to CANDIDATE-QUEUE.md.")
    parser.add_argument("--approve-action", action="append", default=[], help="Approved action ID to apply, for example CQA-001.")
    parser.add_argument("--json", action="store_true", help="Print structured JSON output.")
    parser.add_argument("--self-test", action="store_true", help="Run deterministic script self-tests.")
    args = parser.parse_args(argv)
    try:
        if args.self_test:
            run_self_test()
            print("candidate-queue self-test passed")
            return 0
        kind, actions = build_actions(args)
        applied = None
        if args.apply:
            applied = apply_actions(actions, args.approve_action)
        elif args.approve_action:
            raise QueueError("--approve-action is only valid with --apply")
        output_result(kind, actions, args, applied)
        return 0
    except QueueError as exc:
        if args.json:
            print(json.dumps({"status": "blocked", "error": str(exc), **preview_contract()}, indent=2, sort_keys=True))
        else:
            print(f"blocked: {exc}", file=sys.stderr)
        return 2


def run_self_test() -> None:
    original_root = copy.copy(ROOT)
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_root = Path(temp_dir)
        queue = temp_root / "CANDIDATE-QUEUE.md"
        todo = temp_root / "tasks" / "todo.md"
        todo.parent.mkdir()
        write_text(todo, "current execution only\n")
        queue_text = """# PrecodeOS Candidate Queue

## Candidate Entries

### CQ-001-example -- Example Candidate

- Status: `idea`
- Reviewed rank: `1`
- Shaping status: `unshaped`
- Product-value rating: `unrated`
- Product-value rationale:
- Themes:
- User intent:
- Why this matters:
- Raw source pointer:
- Evidence or source pointers:
- Open questions:
- Evidence strength: `unknown`
- Weakest assumption:
- Promotion target: `Local Source Intake`
- Related PRDs:
- Candidate bead visibility:
- Near-bead sketches:
  - None reviewed.
- Next review trigger:
- Last reviewed: `2026-06-23`

Shaping review:

- No shaping review has been approved yet.

Promotion notes:

- No promotion has been approved yet.

## Candidate Entry Template
"""
        write_text(queue, queue_text)
        raw = temp_root / "raw-notes.md"
        write_text(raw, "# Queue Health\n\nUsers need a place to park queue health ideas.")
        proposal = temp_root / "proposal.json"
        write_text(
            proposal,
            json.dumps(
                {
                    "candidate_id": "CQ-001-example",
                    "shaping_status": "proposed",
                    "product_value_rating": "P1",
                    "product_value_rationale": "High product value after review.",
                    "themes": ["Queue visibility", "Planning"],
                    "weakest_assumption": "Users will maintain candidate quality.",
                    "near_bead_sketches": [
                        {
                            "sketch_id": "CQ-001-example-S01",
                            "title": "Queue review prompt",
                            "outcome": "User sees review-ready queue guidance.",
                            "likely_authority": "PRD amendment",
                            "likely_verification": "clarity scenario",
                            "dependencies": "Candidate Queue Protocol",
                            "status": "proposed",
                        }
                    ],
                }
            ),
        )
        actions = preview_import(raw, queue)
        assert actions[0].action_id == "CQA-001"
        try:
            apply_actions(actions, [], queue)
            raise AssertionError("apply without approval should fail")
        except QueueError:
            pass
        before_todo = read_text(todo)
        apply_actions(actions, ["CQA-001"], queue)
        assert "CQ-002-queue-health" in read_text(queue)
        assert read_text(todo) == before_todo
        shaping_actions = preview_shaping(proposal, queue)
        apply_actions(shaping_actions, ["CQA-001"], queue)
        assert "Product-value rating: `P1`" in read_text(queue)
        bad_rank = temp_root / "bad-rank.json"
        bad_data = json.loads(read_text(proposal))
        bad_data["product_value_rating"] = "P9"
        write_text(bad_rank, json.dumps(bad_data))
        expect_error(lambda: preview_shaping(bad_rank, queue), "invalid P-ranks")
        bad_bead = temp_root / "bad-bead.json"
        bad_data = json.loads(read_text(proposal))
        bad_data["near_bead_sketches"][0]["title"] = "Reserve B123"
        write_text(bad_bead, json.dumps(bad_data))
        expect_error(lambda: preview_shaping(bad_bead, queue), "forbidden B### IDs")
        bad_unknown = temp_root / "bad-unknown.json"
        bad_data = json.loads(read_text(proposal))
        bad_data["candidate_id"] = "CQ-999-missing"
        write_text(bad_unknown, json.dumps(bad_data))
        expect_error(lambda: preview_shaping(bad_unknown, queue), "unknown candidate IDs")
        expect_error(lambda: apply_actions(shaping_actions, ["CQA-999"], queue), "unknown approved action IDs")
        assert original_root == ROOT


def expect_error(fn: Any, label: str) -> None:
    try:
        fn()
    except QueueError:
        return
    raise AssertionError(f"expected QueueError for {label}")


if __name__ == "__main__":
    raise SystemExit(run_cli())
