#!/usr/bin/env python3
# Version: v0.1.1
# Last updated: 2026-05-06
# Owner: Precode OS
# Created by Dan Sears / Recode.
# SPDX-License-Identifier: Apache-2.0
from __future__ import annotations

from dataclasses import dataclass
import re
from pathlib import Path
from typing import Any


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8") if path.is_file() else ""


def strip_inline_code(value: str) -> str:
    return value.strip().strip("`").strip()


def normalize_key(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", value.strip().lower()).strip("_")


def split_frontmatter(text: str) -> tuple[dict[str, Any], str]:
    lines = text.splitlines()
    if not lines:
        return {}, text

    first_non_empty = next((index for index, line in enumerate(lines) if line.strip()), None)
    if first_non_empty is None or lines[first_non_empty].strip() != "---":
        return {}, text

    closing_index: int | None = None
    for index in range(first_non_empty + 1, len(lines)):
        if lines[index].strip() == "---":
            closing_index = index
            break

    if closing_index is None:
        return {}, text

    raw_frontmatter = lines[first_non_empty + 1 : closing_index]
    body = "\n".join(lines[closing_index + 1 :]).lstrip("\n")
    return parse_frontmatter(raw_frontmatter), body


def parse_frontmatter(lines: list[str]) -> dict[str, Any]:
    data: dict[str, Any] = {}
    current_list_key: str | None = None

    for raw_line in lines:
        if not raw_line.strip() or raw_line.lstrip().startswith("#"):
            continue

        if raw_line.startswith("  - ") or raw_line.startswith("- "):
            if current_list_key is None:
                continue
            items = data.setdefault(current_list_key, [])
            if isinstance(items, list):
                items.append(parse_scalar(raw_line.split("- ", 1)[1].strip()))
            continue

        current_list_key = None
        if ":" not in raw_line:
            continue

        key, raw_value = raw_line.split(":", 1)
        key = key.strip()
        raw_value = raw_value.strip()
        if raw_value == "":
            data[key] = []
            current_list_key = key
            continue
        if raw_value == "[]":
            data[key] = []
            continue
        data[key] = parse_scalar(raw_value)

    return data


def parse_scalar(raw_value: str) -> Any:
    value = raw_value.strip()
    if value.startswith(("'", '"')) and value.endswith(("'", '"')) and len(value) >= 2:
        value = value[1:-1]

    lowered = value.lower()
    if lowered == "true":
        return True
    if lowered == "false":
        return False
    if lowered in {"null", "none"}:
        return None
    return strip_inline_code(value)


def format_frontmatter_value(value: Any) -> str:
    if value is None:
        return "null"
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)


def dump_frontmatter(data: dict[str, Any], key_order: list[str] | None = None) -> str:
    ordered_keys: list[str] = []
    if key_order:
        ordered_keys.extend(key for key in key_order if key in data)
    ordered_keys.extend(key for key in data.keys() if key not in ordered_keys)

    lines = ["---"]
    for key in ordered_keys:
        value = data.get(key)
        if isinstance(value, list):
            if not value:
                lines.append(f"{key}: []")
                continue
            lines.append(f"{key}:")
            for item in value:
                lines.append(f"  - {format_frontmatter_value(item)}")
            continue
        lines.append(f"{key}: {format_frontmatter_value(value)}")
    lines.append("---")
    return "\n".join(lines)


def replace_frontmatter(text: str, data: dict[str, Any], key_order: list[str] | None = None) -> str:
    _, body = split_frontmatter(text)
    rendered = dump_frontmatter(data, key_order=key_order)
    if body:
        return rendered + "\n" + body.lstrip("\n")
    return rendered + "\n"


def parse_sections(text: str) -> dict[str, str]:
    _, body = split_frontmatter(text)
    sections: dict[str, str] = {}
    current: str | None = None
    lines: list[str] = []

    for line in body.splitlines():
        match = re.match(r"^## (.+)$", line)
        if match:
            if current is not None:
                sections[current] = "\n".join(lines).strip()
            current = match.group(1).strip()
            lines = []
            continue
        if current is not None:
            lines.append(line)

    if current is not None:
        sections[current] = "\n".join(lines).strip()
    return sections


def bullet_items(section: str) -> list[str]:
    return [
        line.strip()[2:].strip()
        for line in section.splitlines()
        if line.strip().startswith("- ")
    ]


def first_bullet(section: str) -> str | None:
    for item in bullet_items(section):
        value = strip_inline_code(item)
        if value:
            return value
    return None


def colon_bullets(section: str) -> dict[str, str]:
    values: dict[str, str] = {}
    for item in bullet_items(section):
        if ":" not in item:
            continue
        label, value = item.split(":", 1)
        values[normalize_key(label)] = strip_inline_code(value)
    return values


def labeled_bullets(section: str) -> dict[str, str]:
    values: dict[str, str] = {}
    for item in bullet_items(section):
        if ":" not in item:
            continue
        label, value = item.split(":", 1)
        values[strip_inline_code(label)] = value.strip()
    return values


def replace_labeled_bullets(text: str, heading: str, ordered_items: list[tuple[str, str]]) -> str:
    section_body = "\n".join([f"- {label}: {value}" for label, value in ordered_items]).rstrip()
    replacement = f"## {heading}\n\n{section_body}\n"
    return replace_section(text, heading, replacement)


def replace_section(text: str, heading: str, replacement: str) -> str:
    pattern = re.compile(rf"^## {re.escape(heading)}\n.*?(?=^## |\Z)", re.MULTILINE | re.DOTALL)
    if not pattern.search(text):
        raise ValueError(f"{heading} section not found")
    return pattern.sub(replacement + "\n", text, count=1)


def extract_contract_values(text: str) -> dict[str, str]:
    _, body = split_frontmatter(text)
    top_lines = body.splitlines()[:25]
    values: dict[str, str] = {}
    for key in ("AUTHORITY", "NOT_AUTHORITY", "LOAD_WHEN", "CLASS"):
        pattern = re.compile(rf"^\s*>\s*{key}:\s*(.+)$", re.MULTILINE)
        match = pattern.search("\n".join(top_lines))
        if match:
            values[key.lower()] = match.group(1).strip()
    return values


def extract_anchor(text: str) -> str | None:
    _, body = split_frontmatter(text)
    match = re.search(r"<!--\s*ANCHOR:\s*([a-z0-9_-]+)\s*-->", body, re.IGNORECASE)
    return match.group(1) if match else None


@dataclass
class MarkdownDocument:
    path: Path
    frontmatter: dict[str, Any]
    body: str
    sections: dict[str, str]

    @classmethod
    def load(cls, path: Path) -> "MarkdownDocument":
        text = read_text(path)
        frontmatter, body = split_frontmatter(text)
        return cls(path=path, frontmatter=frontmatter, body=body, sections=parse_sections(text))
