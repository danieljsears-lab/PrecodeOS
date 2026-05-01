#!/usr/bin/env python3
# Version: v0.1.0
# Last updated: 2026-04-26
# Owner: Precode OS
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
from typing import Any, Iterable

from os_compiler import load_jsonl, read_todo_state, repo_root


LEDGER = "logs/agent-spend.jsonl"
CONFIDENCE_VALUES = {"exact", "estimated", "unknown"}


def as_int(value: Any) -> int | None:
    if value is None or value == "":
        return None
    try:
        return int(value)
    except (TypeError, ValueError):
        return None


def as_float(value: Any) -> float | None:
    if value is None or value == "":
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def first(*values: Any) -> Any:
    for value in values:
        if value not in (None, ""):
            return value
    return None


def nested(row: dict[str, Any], *keys: str) -> Any:
    value: Any = row
    for key in keys:
        if not isinstance(value, dict):
            return None
        value = value.get(key)
    return value


def read_source(path: Path) -> list[dict[str, Any]]:
    text = path.read_text(encoding="utf-8")
    if not text.strip():
        return []

    if path.suffix.lower() == ".jsonl":
        rows: list[dict[str, Any]] = []
        for line in text.splitlines():
            if not line.strip():
                continue
            value = json.loads(line)
            if isinstance(value, dict):
                rows.append(value)
        return rows

    value = json.loads(text)
    if isinstance(value, list):
        return [item for item in value if isinstance(item, dict)]
    if isinstance(value, dict):
        for key in ("entries", "records", "sessions", "usage"):
            items = value.get(key)
            if isinstance(items, list):
                return [item for item in items if isinstance(item, dict)]
        return [value]
    return []


def import_id(entry: dict[str, Any]) -> str:
    payload = json.dumps(
        {
            "timestamp": entry.get("timestamp"),
            "tool": entry.get("tool"),
            "task": entry.get("task"),
            "input_tokens": entry.get("input_tokens"),
            "output_tokens": entry.get("output_tokens"),
            "total_tokens": entry.get("total_tokens"),
            "cost_usd": entry.get("cost_usd"),
            "model": entry.get("model"),
            "session_id": entry.get("session_id"),
            "telemetry_source": entry.get("telemetry_source"),
        },
        sort_keys=True,
        separators=(",", ":"),
    )
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()[:16]


def normalize_row(row: dict[str, Any], *, default_tool: str | None, source_label: str, default_task: str) -> dict[str, Any] | None:
    usage = row.get("usage") if isinstance(row.get("usage"), dict) else {}
    cost = row.get("cost") if isinstance(row.get("cost"), dict) else {}

    tool = first(row.get("tool"), row.get("agent"), row.get("provider"), default_tool)
    task = first(row.get("task"), row.get("bead"), row.get("current_bead"), row.get("task_id"), default_task)
    input_tokens = as_int(first(row.get("input_tokens"), row.get("prompt_tokens"), usage.get("input_tokens"), usage.get("prompt_tokens"), nested(row, "message", "usage", "input_tokens")))
    output_tokens = as_int(first(row.get("output_tokens"), row.get("completion_tokens"), usage.get("output_tokens"), usage.get("completion_tokens"), nested(row, "message", "usage", "output_tokens")))
    total_tokens = as_int(first(row.get("total_tokens"), row.get("tokens"), usage.get("total_tokens"), usage.get("tokens")))
    if total_tokens is None and input_tokens is not None and output_tokens is not None:
        total_tokens = input_tokens + output_tokens
    flat_cost = row.get("cost") if not isinstance(row.get("cost"), dict) else None
    cost_usd = as_float(first(row.get("cost_usd"), row.get("usd"), cost.get("usd"), cost.get("cost_usd"), flat_cost))

    if not tool or not task:
        return None
    if input_tokens is None and output_tokens is None and total_tokens is None and cost_usd is None:
        return None

    confidence = str(first(row.get("confidence"), row.get("import_confidence"), "exact" if source_label != "manual" else "unknown"))
    if confidence not in CONFIDENCE_VALUES:
        confidence = "unknown"

    entry = {
        "timestamp": str(first(row.get("timestamp"), row.get("created_at"), row.get("time"), datetime.now(timezone.utc).isoformat())),
        "tool": str(tool),
        "task": str(task),
        "branch": row.get("branch"),
        "input_tokens": input_tokens,
        "output_tokens": output_tokens,
        "total_tokens": total_tokens,
        "tokens": total_tokens,
        "cost_usd": cost_usd,
        "model": first(row.get("model"), row.get("model_name")),
        "session_id": first(row.get("session_id"), row.get("run_id"), row.get("request_id"), row.get("id")),
        "telemetry_source": str(first(row.get("telemetry_source"), row.get("source"), source_label)),
        "confidence": confidence,
        "notes": row.get("notes"),
    }
    entry["import_id"] = import_id(entry)
    return entry


def append_entries(path: Path, entries: Iterable[dict[str, Any]]) -> int:
    path.parent.mkdir(parents=True, exist_ok=True)
    existing_ids = {str(row.get("import_id")) for row in load_jsonl(path) if row.get("import_id")}
    written = 0
    with path.open("a", encoding="utf-8") as handle:
        for entry in entries:
            if entry.get("import_id") in existing_ids:
                continue
            handle.write(json.dumps(entry, separators=(",", ":")) + "\n")
            written += 1
    return written


def main() -> int:
    parser = argparse.ArgumentParser(description="Import agent token/cost telemetry into logs/agent-spend.jsonl.")
    parser.add_argument("--tool", help="default agent/tool name when source rows omit one")
    parser.add_argument("--source", action="append", help="JSON or JSONL telemetry file to import")
    parser.add_argument("--dry-run", action="store_true", help="parse and report importable rows without writing")
    args = parser.parse_args()

    root = repo_root()
    todo = read_todo_state(root)
    default_task = str(todo.get("current_bead") or "unknown")
    sources = [Path(value).expanduser() for value in args.source or []]

    if not sources:
        print("import-agent-spend: no importable telemetry found")
        return 0

    normalized: list[dict[str, Any]] = []
    for source in sources:
        path = source if source.is_absolute() else root / source
        if not path.is_file():
            print(f"import-agent-spend: source not found: {source}")
            continue
        for row in read_source(path):
            entry = normalize_row(row, default_tool=args.tool, source_label=source.as_posix(), default_task=default_task)
            if entry is not None:
                normalized.append(entry)

    if not normalized:
        print("import-agent-spend: no importable telemetry found")
        return 0

    if args.dry_run:
        print(json.dumps({"importable": len(normalized), "entries": normalized}, indent=2, sort_keys=True))
        return 0

    count = append_entries(root / LEDGER, normalized)
    print(f"import-agent-spend: imported {count} new spend entr{'y' if count == 1 else 'ies'} to {LEDGER}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
