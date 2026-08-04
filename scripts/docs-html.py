#!/usr/bin/env python3
# Version: v0.1.10
# Last updated: 2026-08-04
# Owner: PrecodeOS
# Created by Dan Sears / Recode.
# SPDX-License-Identifier: Apache-2.0
from __future__ import annotations

import argparse
from dataclasses import dataclass
from html import escape
from pathlib import Path
import re
import shutil
import sys
import tempfile
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
OUTPUT = ROOT / "docs-html"
REFERENCE = ROOT / "tasks" / "reference"

ROOT_DOCS = [
    "CANDIDATE-QUEUE.md",
]

DOC_ORDER = [
    "PRECODE-DAILY-COCKPIT.md",
    "CANDIDATE-QUEUE.md",
    "PRECODE-OS-README.md",
    "PRECODE-USER-GUIDE.md",
    "CLAUDE-CODE-FIELD-GUIDE.md",
    "PRECODE-GUIDED-SETUP.md",
    "HOW-TO-BUILD-SOFTWARE-WITH-PRECODE.md",
    "PRECODE-TROUBLESHOOTING.md",
    "PRECODE-SUPPORT-RUNBOOK.md",
    "PRECODE-ARCHITECTURE-OVERVIEW.md",
    "PRECODE-PACKAGE-FILE-INVENTORY.md",
    "PRECODE-MANIFESTO.md",
]

COMPASS = [
    {
        "label": "Setup And Daily Work",
        "summary": "Start here for orientation, daily operation, builder guidance, setup, and the plain-English software-building path.",
        "home": True,
        "docs": [
            "PRECODE-DAILY-COCKPIT.md",
            "CANDIDATE-QUEUE.md",
            "PRECODE-OS-README.md",
            "PRECODE-USER-GUIDE.md",
            "CLAUDE-CODE-FIELD-GUIDE.md",
            "PRECODE-GUIDED-SETUP.md",
            "HOW-TO-BUILD-SOFTWARE-WITH-PRECODE.md",
        ],
    },
    {
        "label": "Advanced Topics",
        "summary": "Use these when something breaks, someone else needs support, or you need architecture, package inventory, or philosophy context.",
        "docs": [
            "PRECODE-TROUBLESHOOTING.md",
            "PRECODE-SUPPORT-RUNBOOK.md",
            "PRECODE-ARCHITECTURE-OVERVIEW.md",
            "PRECODE-PACKAGE-FILE-INVENTORY.md",
            "PRECODE-MANIFESTO.md",
        ],
    },
]


@dataclass(frozen=True)
class TocItem:
    level: int
    text: str
    anchor: str


@dataclass(frozen=True)
class Doc:
    path: Path
    filename: str
    html_name: str
    title: str
    anchor: str
    authority: str
    not_authority: str
    load_when: str
    doc_class: str
    version: str
    last_updated: str
    summary: str
    content_html: str
    toc: list[TocItem]


@dataclass(frozen=True)
class PromptCard:
    category: str
    title: str
    description: str
    when: str
    prompt: str
    source: str


@dataclass(frozen=True)
class ProtocolCard:
    category: str
    title: str
    filename: str
    authority: str
    load_when: str
    version: str
    last_updated: str
    launch: str


PROMPT_STRUCTURAL_HEADINGS = {
    "purpose",
    "daily prompt aliases",
    "core default loop",
    "advanced / conditional surfaces",
    "safe prompt pack",
    "no-engineer fallback prompt pack",
}

PROMPT_CATEGORY_HINTS = {
    "Discovery": {
        "artifact chooser",
        "question-to-artifact filing",
        "local source intake",
        "source-to-promotion hygiene review",
        "owner-file promotion before prd shaping",
        "client engagement intake",
        "product constitution review",
        "founder-friendly product brief",
        "alignment / product brief",
        "ubiquitous language review",
        "glossary card proposal",
        "domain naming review",
        "idea to evidence trace",
        "precode idea coach",
        "first prd walkthrough",
        "precode conviction handoff",
        "hypothesis review / learning loop",
        "accessibility advisor fit interview",
        "product discovery interview skill",
    },
    "Planning": {
        "prd shaping",
        "destination prd review",
        "prd handoff readiness packet",
        "requirements gap and conflict review",
        "bead decomposition",
        "vertical-slice decomposition",
        "architecture shaping",
        "system design shape",
        "pattern fit",
        "workflow selection",
        "workflow selection skill",
        "plan loop",
        "plan mode candidate craft loop",
        "routing check",
        "context budget check",
        "compact or handoff context pack",
        "goal frame proposal",
        "workbook candidate goal frame",
        "goal frame reaffirmation",
        "goal frame fit check",
        "goal frame boundaries",
        "long-horizon review",
        "candidate queue review",
        "add candidate queue entry",
        "candidate queue shaping proposal",
        "candidate queue import preview",
        "afk-candidate review",
        "ready to become a bead",
    },
    "Build": {
        "session start",
        "task confirmation",
        "engineering quality floor",
        "vibe-to-agentic boundary",
        "engineer initiation",
        "backend-only with existing frontend",
        "active bead before editing",
        "git hygiene before new work",
        "repository topology migration",
        "source and target confirmation",
        "one question at a time",
        "build-react-learn exploratory prototype bead",
        "team assignment packet prompts v2",
        "teammate startup in a team lane",
        "small team collaboration lane",
        "small team collaboration preview",
        "team merge and re-entry review pack",
        "bounded-afk re-entry",
        "delegation re-entry evidence pack",
        "classify tool call",
        "record tool run",
        "command safety",
        "local hygiene check",
        "local hygiene dry run",
        "implementation",
        "failing-first implementation",
        "checkpoint",
        "approved-bead handoff",
        "build attribution review",
    },
    "Review": {
        "acceptance",
        "review / acceptance skill",
        "requirement-to-proof review",
        "review lanes",
        "multi-lane review invocation",
        "review",
        "review lane",
        "dependency graph review lane",
        "prd quality review lane",
        "engineering quality review lane",
        "polish / product-taste review lane",
        "cross-reference / staleness review lane",
        "make acceptance criteria testable",
        "review acceptance criteria for vague behavior",
        "release candidate evidence profile",
        "verification and release evidence review",
        "release candidate review",
        "fresh-context comprehension review",
        "fresh-context review",
        "stale artifact handling",
        "manual verification",
        "completion check",
        "reviewed memory",
        "learning diary review",
    },
    "Recovery": {
        "close the session",
        "handoff",
        "handoff packet",
        "transition readiness",
        "intent changed",
        "implemented bead reversal",
        "state repair",
        "stuck recovery",
        "agent is lost",
        "checks failed",
        "app will not start",
        "approved too much",
        "copied wrong files",
        "decide whether to stop",
        "bootstrap recovery guidance",
        "existing repo intake",
        "supervised setup plan",
        "supervised setup apply",
        "existing project adaptation plan",
        "existing precode refresh",
        "package upgrade preview",
        "package upgrade apply",
        "stop before precode control-layer edits",
        "maintainer package review skill",
        "skill / extension review skill",
        "precode skill playbook",
        "evidence is not authority",
        "triage github feedback or package bug",
        "session friction review",
    },
}

PROTOCOL_CATEGORY_HINTS = [
    (
        "Discovery",
        {
            "LOCAL-SOURCE-INTAKE-PROTOCOL.md",
            "PRODUCT-DISCOVERY-VALIDATION-PROTOCOL.md",
            "CLIENT-ENGAGEMENT-INTAKE-PROTOCOL.md",
            "HYPOTHESIS-REVIEW-PROTOCOL.md",
            "UBIQUITOUS-LANGUAGE-PROTOCOL.md",
            "MEMORY-PROTOCOL.md",
            "LEARNING-DIARY-PROTOCOL.md",
        },
    ),
    (
        "Planning",
        {
            "PRD-PROTOCOL.md",
            "DECOMPOSITION-PROTOCOL.md",
            "CANDIDATE-QUEUE-PROTOCOL.md",
            "WORKFLOW-SELECTION-PROTOCOL.md",
            "PLANNING-PROTOCOL.md",
            "GOAL-FRAME-PROTOCOL.md",
            "LONG-HORIZON-PLANNING-PROTOCOL.md",
            "ARCHITECTURE-SHAPING-PROTOCOL.md",
            "SYSTEM-DESIGN-PATTERN-PROTOCOL.md",
            "INTENT-ORCHESTRATION-PROTOCOL.md",
            "SEMANTIC-CHANGE-PROPOSAL-PROTOCOL.md",
        },
    ),
    (
        "Build",
        {
            "CONTEXT-ENGINEERING-PROTOCOL.md",
            "AGENT-ROUTING-PROTOCOL.md",
            "TOOL-EXECUTION-PROTOCOL.md",
            "TEAM-COLLABORATION-PROTOCOL.md",
            "BEAD-BUILD-JOURNAL-PROTOCOL.md",
            "RALPH-LOOP-PROTOCOL.md",
            "LOCAL-HYGIENE-PROTOCOL.md",
            "GITHUB-INTEGRATION-PROTOCOL.md",
            "EXTERNAL-STATUS-INTEGRATION-PROTOCOL.md",
            "EXTENSION-PROTOCOL.md",
            "SKILL-PLAYBOOK-PROTOCOL.md",
            "VERSIONING-PROTOCOL.md",
        },
    ),
    (
        "Review",
        {
            "VERIFICATION-GUARDRAIL-PROTOCOL.md",
            "REVIEW-LANES-PROTOCOL.md",
            "ENGINEERING-QUALITY-STANDARDS-PROTOCOL.md",
            "RELEASE-READINESS-PROTOCOL.md",
            "SESSION-COMPLETION-HANDOFF-PROTOCOL.md",
        },
    ),
    (
        "Recovery",
        {
            "RECOVERY-PROTOCOL.md",
            "STATE-MANAGEMENT-PROTOCOL.md",
            "OS-INTEGRITY-PROTOCOL.md",
            "SCHEDULED-AUDIT-PROTOCOL.md",
            "BOOTSTRAP-CONFIDENCE-PROTOCOL.md",
            "INSTALL-UPDATE-MANIFEST-PROTOCOL.md",
            "SUPERVISED-SETUP-PLAN-PROTOCOL.md",
            "SUPERVISED-SETUP-APPLY-PROTOCOL.md",
            "BOOTSTRAP-CLOSEOUT-PROTOCOL.md",
            "EXISTING-REPO-INTAKE-PROTOCOL.md",
        },
    ),
]


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    normalized = "\n".join(line.rstrip() for line in text.splitlines()) + "\n"
    path.write_text(normalized, encoding="utf-8")


def h(value: Any) -> str:
    return escape(str(value), quote=True)


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return slug or "section"


def unique_slug(base: str, used: dict[str, int]) -> str:
    count = used.get(base, 0)
    used[base] = count + 1
    if count == 0:
        return base
    return f"{base}-{count + 1}"


def extract_title(text: str) -> str:
    match = re.search(r"^#\s+(.+)$", text, re.MULTILINE)
    return match.group(1).strip() if match else "Untitled"


def extract_anchor(text: str) -> str:
    match = re.search(r"<!--\s*ANCHOR:\s*([a-z0-9_-]+)\s*-->", text, re.IGNORECASE)
    return match.group(1).strip() if match else slugify(extract_title(text))


def extract_contract(text: str, key: str) -> str:
    match = re.search(rf"^\s*>\s*{re.escape(key)}:\s*(.+)$", text, re.MULTILINE)
    return match.group(1).strip() if match else ""


def extract_metadata(text: str, label: str) -> str:
    match = re.search(rf"^{re.escape(label)}:\s*(.+)$", text, re.MULTILINE)
    return match.group(1).strip() if match else ""


def strip_metadata(text: str) -> str:
    lines = text.splitlines()
    kept: list[str] = []
    skip_contract = False
    for line in lines:
        if line.startswith("> AUTHORITY:"):
            skip_contract = True
            continue
        if skip_contract:
            if line.startswith("> ") or not line.strip():
                continue
            skip_contract = False
        if re.match(r"^(Creator|License|Copyright|Document version|Last updated|Companion to):\s+", line):
            continue
        kept.append(line)
    return "\n".join(kept).strip() + "\n"


def plain_text(markdown: str) -> str:
    text = re.sub(r"```.*?```", " ", markdown, flags=re.DOTALL)
    text = re.sub(r"<!--.*?-->", " ", text, flags=re.DOTALL)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"[*_`>#|\-]+", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def first_paragraph(markdown: str) -> str:
    body = strip_metadata(markdown)
    body = re.sub(r"^# .+\n", "", body, count=1).strip()
    parts = re.split(r"\n\s*\n", body)
    for part in parts:
        candidate = part.strip()
        if not candidate:
            continue
        if re.match(r"^#{1,6}\s+", candidate):
            continue
        if re.fullmatch(r"<!--\s*ANCHOR:\s*[a-z0-9_-]+\s*-->", candidate, re.IGNORECASE):
            continue
        if candidate in {"---", "***", "___"}:
            continue
        clean = plain_text(part)
        if clean:
            return clean[:230].rstrip()
    return ""


def first_sentence(markdown: str, fallback: str = "") -> str:
    clean = plain_text(markdown)
    if not clean:
        return fallback
    match = re.search(r"(.+?[.!?])(?:\s|$)", clean)
    if match:
        return match.group(1).strip()
    return clean[:180].rstrip()


def filename_to_html(filename: str) -> str:
    return Path(filename).with_suffix(".html").name


def link_target(url: str) -> str:
    if re.match(r"^[a-z][a-z0-9+.-]*:", url) or url.startswith("#"):
        return url
    clean = url
    anchor = ""
    if "#" in clean:
        clean, anchor = clean.split("#", 1)
        anchor = f"#{anchor}"
    if clean.startswith("../"):
        clean = clean[3:]
    if clean.startswith("docs/") and clean.endswith(".md"):
        return f"{filename_to_html(Path(clean).name)}{anchor}"
    if clean in ROOT_DOCS:
        return f"{filename_to_html(clean)}{anchor}"
    if clean.startswith("../") and clean[3:] in ROOT_DOCS:
        return f"{filename_to_html(clean[3:])}{anchor}"
    if clean.endswith(".md") and "/" not in clean:
        if (DOCS / clean).is_file() or (ROOT / clean).is_file():
            return f"{filename_to_html(clean)}{anchor}"
    return url


def inline(markdown: str) -> str:
    placeholders: list[str] = []

    def stash_code(match: re.Match[str]) -> str:
        placeholders.append(f"<code>{h(match.group(1))}</code>")
        return f"\u0000{len(placeholders) - 1}\u0000"

    text = re.sub(r"`([^`]+)`", stash_code, h(markdown))
    text = re.sub(
        r"\[([^\]]+)\]\(([^)]+)\)",
        lambda match: f'<a href="{h(link_target(match.group(2)))}">{match.group(1)}</a>',
        text,
    )
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"\*([^*]+)\*", r"<em>\1</em>", text)
    for index, value in enumerate(placeholders):
        text = text.replace(f"\u0000{index}\u0000", value)
    return text


def is_table_start(lines: list[str], index: int) -> bool:
    if index + 1 >= len(lines):
        return False
    return lines[index].strip().startswith("|") and re.match(r"^\s*\|?\s*:?-{3,}:?\s*(\|\s*:?-{3,}:?\s*)+\|?\s*$", lines[index + 1]) is not None


def table_cells(row: str) -> list[str]:
    return [cell.strip() for cell in row.strip().strip("|").split("|")]


def render_table(lines: list[str]) -> str:
    headers = table_cells(lines[0])
    rows = [table_cells(line) for line in lines[2:]]
    head = "".join(f"<th>{inline(cell)}</th>" for cell in headers)
    body_rows = []
    for row in rows:
        body_rows.append("<tr>" + "".join(f"<td>{inline(cell)}</td>" for cell in row) + "</tr>")
    class_name = " table-action-map" if headers and headers[0].lower().startswith("i need to") else ""
    return f'<div class="table-wrap{class_name}"><table><thead><tr>{head}</tr></thead><tbody>{"".join(body_rows)}</tbody></table></div>'


def render_list(items: list[str], ordered: bool) -> str:
    tag = "ol" if ordered else "ul"
    rows = "".join(f"<li>{inline(item)}</li>" for item in items)
    return f"<{tag}>{rows}</{tag}>"


def render_blockquote(lines: list[str]) -> str:
    content = "\n".join(line.strip()[1:].strip() for line in lines)
    return f"<blockquote>{render_markdown(content, include_title=True)[0]}</blockquote>"


def section_ranges(markdown: str) -> list[tuple[int, str, int, int]]:
    headings = list(re.finditer(r"^(#{1,6})\s+(.+)$", markdown, re.MULTILINE))
    ranges: list[tuple[int, str, int, int]] = []
    for index, match in enumerate(headings):
        level = len(match.group(1))
        title = match.group(2).strip()
        end = len(markdown)
        for next_match in headings[index + 1 :]:
            if len(next_match.group(1)) <= level:
                end = next_match.start()
                break
        ranges.append((level, title, match.end(), end))
    return ranges


def prompt_category(title: str, parent: str | None) -> str:
    key = title.lower()
    for category, titles in PROMPT_CATEGORY_HINTS.items():
        if key in titles:
            return category
    if parent and parent.lower() == "safe prompt pack":
        return "Recovery" if any(word in key for word in ("recovery", "stuck", "failed", "repair")) else "Build"
    return "Review" if "review" in key or "proof" in key or "acceptance" in key else "Planning"


def extract_prompt_cards() -> list[PromptCard]:
    path = REFERENCE / "PROMPT-PATTERNS.md"
    markdown = read_text(path)
    ranges = section_ranges(markdown)
    cards: list[PromptCard] = []
    seen_titles: set[str] = set()
    current_h2: str | None = None
    for level, title, start, end in ranges:
        if level == 2:
            current_h2 = title
        key = title.lower()
        if level not in {2, 3} or key in PROMPT_STRUCTURAL_HEADINGS:
            continue
        if key in seen_titles:
            continue
        section = markdown[start:end]
        code_match = re.search(r"```(?:text|bash)?\n(.*?)\n```", section, re.DOTALL)
        if not code_match:
            continue
        before_code = section[: code_match.start()]
        description = first_sentence(before_code, fallback=f"Copyable Precode prompt for {title}.")
        when_match = re.search(r"Use (?:this prompt )?when ([^.]+(?:\.[^\n]*)?)", before_code, re.IGNORECASE)
        when = first_sentence(when_match.group(1), fallback="Use when this workflow moment applies.") if when_match else "Use when this workflow moment applies."
        cards.append(
            PromptCard(
                category=prompt_category(title, current_h2),
                title=title,
                description=description,
                when=when,
                prompt=code_match.group(1).strip(),
                source="../tasks/reference/PROMPT-PATTERNS.md",
            )
        )
        seen_titles.add(key)
    return cards


def protocol_category(filename: str) -> str:
    for category, filenames in PROTOCOL_CATEGORY_HINTS:
        if filename in filenames:
            return category
    return "Planning"


def extract_protocol_cards() -> list[ProtocolCard]:
    cards: list[ProtocolCard] = []
    for path in sorted(REFERENCE.glob("*PROTOCOL.md")):
        markdown = read_text(path)
        title = extract_title(markdown)
        load_when = extract_contract(markdown, "LOAD_WHEN")
        authority = extract_contract(markdown, "AUTHORITY")
        launch = (
            f"Use the {title}.\n\n"
            f"Load when: {load_when or 'the protocol trigger applies.'}\n\n"
            "Preserve its authority boundaries. Do not treat this invocation as task selection, PRD approval, "
            "bead activation, implementation acceptance, generated evidence authority, command approval, external mutation, "
            "or permission to bypass human approval gates."
        )
        cards.append(
            ProtocolCard(
                category=protocol_category(path.name),
                title=title,
                filename=path.name,
                authority=authority,
                load_when=load_when,
                version=extract_metadata(markdown, "Document version"),
                last_updated=extract_metadata(markdown, "Last updated"),
                launch=launch,
            )
        )
    return cards


def render_markdown(markdown: str, include_title: bool = False) -> tuple[str, list[TocItem]]:
    lines = strip_metadata(markdown).splitlines()
    html: list[str] = []
    toc: list[TocItem] = []
    used: dict[str, int] = {}
    paragraph: list[str] = []
    index = 0

    def flush_paragraph() -> None:
        if paragraph:
            html.append(f"<p>{inline(' '.join(part.strip() for part in paragraph))}</p>")
            paragraph.clear()

    while index < len(lines):
        raw = lines[index]
        line = raw.rstrip()
        stripped = line.strip()

        if not stripped:
            flush_paragraph()
            index += 1
            continue

        if stripped.startswith("```"):
            flush_paragraph()
            language = stripped[3:].strip()
            code: list[str] = []
            index += 1
            while index < len(lines) and not lines[index].strip().startswith("```"):
                code.append(lines[index])
                index += 1
            if index < len(lines):
                index += 1
            class_name = f' class="language-{h(language)}"' if language else ""
            html.append(f"<pre><code{class_name}>{h(chr(10).join(code))}</code></pre>")
            continue

        heading = re.match(r"^(#{1,6})\s+(.+)$", stripped)
        if heading:
            flush_paragraph()
            level = len(heading.group(1))
            text = heading.group(2).strip()
            if level == 1 and not include_title:
                index += 1
                if index < len(lines) and re.match(r"<!--\s*ANCHOR:", lines[index].strip(), re.IGNORECASE):
                    index += 1
                continue
            anchor = ""
            if index + 1 < len(lines):
                anchor_match = re.match(r"<!--\s*ANCHOR:\s*([a-z0-9_-]+)\s*-->", lines[index + 1].strip(), re.IGNORECASE)
                if anchor_match:
                    anchor = anchor_match.group(1).strip()
                    index += 1
            anchor = unique_slug(anchor or slugify(plain_text(text)), used)
            heading_label = h(plain_text(text))
            html.append(
                f'<h{level} id="{h(anchor)}"><a class="heading-anchor" href="#{h(anchor)}" '
                f'aria-label="Link to {heading_label}">#</a>{inline(text)}</h{level}>'
            )
            if level <= 3:
                toc.append(TocItem(level=level, text=plain_text(text), anchor=anchor))
            index += 1
            continue

        if re.match(r"<!--\s*ANCHOR:", stripped, re.IGNORECASE):
            index += 1
            continue

        if stripped in {"---", "***", "___"}:
            flush_paragraph()
            html.append("<hr>")
            index += 1
            continue

        if is_table_start(lines, index):
            flush_paragraph()
            table_lines = [lines[index], lines[index + 1]]
            index += 2
            while index < len(lines) and lines[index].strip().startswith("|"):
                table_lines.append(lines[index])
                index += 1
            html.append(render_table(table_lines))
            continue

        unordered = re.match(r"^\s*[-*]\s+(.+)$", line)
        ordered = re.match(r"^\s*\d+\.\s+(.+)$", line)
        if unordered or ordered:
            flush_paragraph()
            ordered_list = ordered is not None
            items: list[str] = []
            while index < len(lines):
                item_match = re.match(r"^\s*\d+\.\s+(.+)$" if ordered_list else r"^\s*[-*]\s+(.+)$", lines[index])
                if not item_match:
                    break
                items.append(item_match.group(1).strip())
                index += 1
            html.append(render_list(items, ordered_list))
            continue

        if stripped.startswith(">"):
            flush_paragraph()
            quote_lines: list[str] = []
            while index < len(lines) and lines[index].strip().startswith(">"):
                quote_lines.append(lines[index])
                index += 1
            html.append(render_blockquote(quote_lines))
            continue

        paragraph.append(line)
        index += 1

    flush_paragraph()
    return "\n".join(html), toc


def load_docs() -> list[Doc]:
    paths = [ROOT / filename for filename in ROOT_DOCS if (ROOT / filename).is_file()]
    paths.extend(sorted(DOCS.glob("*.md")))
    order = {name: index for index, name in enumerate(DOC_ORDER)}
    paths.sort(key=lambda path: (order.get(path.name, len(DOC_ORDER)), path.name))
    docs: list[Doc] = []
    for path in paths:
        text = read_text(path)
        content_html, toc = render_markdown(text)
        docs.append(
            Doc(
                path=path,
                filename=path.name,
                html_name=filename_to_html(path.name),
                title=extract_title(text),
                anchor=extract_anchor(text),
                authority=extract_contract(text, "AUTHORITY"),
                not_authority=extract_contract(text, "NOT_AUTHORITY"),
                load_when=extract_contract(text, "LOAD_WHEN"),
                doc_class=extract_contract(text, "CLASS"),
                version=extract_metadata(text, "Document version"),
                last_updated=extract_metadata(text, "Last updated"),
                summary=first_paragraph(text),
                content_html=content_html,
                toc=toc,
            )
        )
    return docs


def css() -> str:
    return """
:root {
  color-scheme: light;
  --ink: #1c2520;
  --muted: #637067;
  --line: #d8dfda;
  --paper: #fffdf8;
  --wash: #f7f1e8;
  --wash-2: #edf5f2;
  --accent: #176c63;
  --accent-2: #b65332;
  --accent-3: #284f8f;
  --shadow: 0 18px 50px rgba(54, 43, 28, .10);
  --measure: 78ch;
}
* { box-sizing: border-box; }
html { scroll-behavior: smooth; }
body {
  margin: 0;
  color: var(--ink);
  background:
    linear-gradient(180deg, rgba(255,253,248,.94), rgba(247,241,232,.98)),
    var(--wash);
  font: 16px/1.6 -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
}
a { color: var(--accent); text-underline-offset: 3px; }
.reading-progress {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: 20;
  height: 4px;
  background: rgba(216, 223, 218, .7);
}
.reading-progress span {
  display: block;
  width: 100%;
  height: 100%;
  background: linear-gradient(90deg, var(--accent), var(--accent-2));
  transform: scaleX(0);
  transform-origin: left center;
}
.shell { min-height: 100vh; display: grid; grid-template-columns: 300px minmax(0, 1fr); }
.sidebar {
  position: sticky;
  top: 0;
  height: 100vh;
  overflow: auto;
  padding: 24px 20px;
  border-right: 1px solid var(--line);
  background: rgba(255, 253, 248, .88);
}
.brand { display: grid; gap: 4px; margin-bottom: 22px; }
.brand strong { font-size: 18px; }
.brand span, .notice, .meta, .toc a, .doc-card p, .lane p { color: var(--muted); }
.notice {
  border: 1px solid var(--line);
  border-left: 4px solid var(--accent-2);
  background: #fffaf1;
  padding: 12px;
  border-radius: 8px;
  font-size: 13px;
}
.nav-group { margin-top: 22px; }
.nav-label {
  margin: 0 0 8px;
  color: var(--muted);
  font-size: 12px;
  font-weight: 800;
  letter-spacing: .08em;
  text-transform: uppercase;
}
.nav-link {
  display: block;
  padding: 8px 10px;
  border-radius: 8px;
  color: var(--ink);
  text-decoration: none;
  font-size: 14px;
}
.nav-link:hover, .nav-link.active { background: var(--wash-2); color: var(--accent); }
.nav-divider { height: 1px; margin: 16px 0 14px; border: 0; background: var(--line); }
main { min-width: 0; }
.hero, .content { max-width: 1040px; margin: 0 auto; padding: 42px 32px; }
.hero { display: grid; gap: 18px; padding-top: 58px; }
.eyebrow {
  margin: 0;
  color: var(--accent-2);
  font-size: 12px;
  font-weight: 850;
  letter-spacing: .1em;
  text-transform: uppercase;
}
h1, h2, h3, h4 { line-height: 1.15; letter-spacing: 0; }
h1 { max-width: 850px; margin: 0; font-size: 48px; }
h2 { margin-top: 42px; font-size: 28px; }
h3 { margin-top: 30px; font-size: 21px; }
h4 { margin-top: 24px; font-size: 17px; }
h2, h3, h4, h5, h6 { scroll-margin-top: 22px; }
.heading-anchor {
  float: left;
  width: 22px;
  margin-left: -28px;
  color: var(--muted);
  text-decoration: none;
  opacity: 0;
}
h2:hover .heading-anchor,
h3:hover .heading-anchor,
h4:hover .heading-anchor,
h5:hover .heading-anchor,
h6:hover .heading-anchor,
.heading-anchor:focus { opacity: 1; }
.lede { max-width: 760px; margin: 0; color: #37443c; font-size: 20px; }
.compass-grid, .reference-card-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 14px; margin-top: 18px; }
.cockpit-hero {
  padding-bottom: 26px;
}
.cockpit-strip {
  display: grid;
  gap: 16px;
  max-width: 930px;
}
.cockpit-ritual-grid {
  display: grid;
  grid-template-columns: repeat(4, minmax(0, 1fr));
  gap: 12px;
}
.cockpit-tile {
  display: grid;
  gap: 7px;
  border: 1px solid var(--line);
  border-radius: 8px;
  background: var(--paper);
  box-shadow: 0 12px 34px rgba(54, 43, 28, .07);
  padding: 16px;
  color: var(--ink);
  text-decoration: none;
}
.cockpit-tile strong { font-size: 19px; }
.cockpit-tile span { color: var(--muted); font-size: 14px; }
.cockpit-tile:hover { border-color: var(--accent); }
.cockpit-catalog-row {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  align-items: center;
}
.cockpit-catalog-row span {
  color: var(--muted);
  font-size: 13px;
  font-weight: 800;
  letter-spacing: .08em;
  text-transform: uppercase;
}
.cockpit-catalog-row a {
  border: 1px solid var(--line);
  border-radius: 8px;
  background: var(--wash-2);
  padding: 7px 10px;
  color: var(--ink);
  text-decoration: none;
  font-size: 13px;
}
.cockpit-catalog-row a:hover { border-color: var(--accent); color: var(--accent); }
.lane, .doc-card, .page-nav a {
  border: 1px solid var(--line);
  border-radius: 8px;
  background: var(--paper);
  box-shadow: var(--shadow);
}
.lane { padding: 18px; }
.lane h2 { margin: 0 0 8px; font-size: 22px; }
.lane ul, .toc ul { margin: 12px 0 0; padding-left: 20px; }
.doc-list { display: grid; gap: 12px; margin-top: 18px; }
.doc-card { display: grid; gap: 6px; padding: 16px; text-decoration: none; color: var(--ink); }
.doc-card:hover { border-color: var(--accent); }
.doc-card strong { font-size: 18px; }
.meta { display: flex; flex-wrap: wrap; gap: 10px; font-size: 13px; }
.reference-surface {
  margin: 40px 0;
  border: 1px solid var(--line);
  border-radius: 8px;
  background: linear-gradient(180deg, rgba(237,245,242,.72), rgba(255,253,248,.96));
  padding: 24px;
}
.reference-surface > :first-child { margin-top: 0; }
.reference-surface .lede { font-size: 17px; }
.jump-chips { display: flex; flex-wrap: wrap; gap: 8px; margin: 18px 0 26px; }
.jump-chip {
  display: inline-flex;
  align-items: center;
  border: 1px solid var(--line);
  border-radius: 8px;
  background: var(--paper);
  padding: 7px 10px;
  color: var(--ink);
  text-decoration: none;
  font-size: 13px;
}
.jump-chip:hover { border-color: var(--accent); color: var(--accent); }
.reference-group { margin-top: 28px; }
.reference-group h3 {
  display: flex;
  align-items: center;
  gap: 10px;
  margin-bottom: 12px;
  color: var(--accent);
  font-size: 20px;
}
.reference-group h3::before {
  content: "";
  width: 9px;
  height: 9px;
  border-radius: 999px;
  background: var(--accent-2);
  flex: none;
}
.reference-card {
  display: grid;
  gap: 12px;
  border: 1px solid var(--line);
  border-radius: 8px;
  background: var(--paper);
  box-shadow: 0 12px 34px rgba(54, 43, 28, .07);
  padding: 18px;
}
.reference-card h4 { margin: 0; font-size: 18px; }
.reference-card p { margin: 0; }
.reference-card .label-row {
  display: grid;
  gap: 4px;
  border-top: 1px solid var(--line);
  padding-top: 10px;
}
.reference-card .label-row strong {
  color: var(--accent-2);
  font-size: 12px;
  letter-spacing: .08em;
  text-transform: uppercase;
}
.copy-block {
  display: grid;
  gap: 10px;
  border: 1px solid #283630;
  border-radius: 8px;
  background: #1d2521;
  padding: 12px;
}
.copy-block-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 10px;
}
.copy-block-header span {
  color: #d2ddd7;
  font-size: 12px;
  font-weight: 800;
  letter-spacing: .08em;
  text-transform: uppercase;
}
.copy-button {
  border: 1px solid rgba(248, 251, 247, .32);
  border-radius: 8px;
  background: transparent;
  color: #f8fbf7;
  padding: 5px 8px;
  font: inherit;
  font-size: 12px;
  cursor: pointer;
}
.copy-button:hover { border-color: #f8fbf7; }
.copy-block pre {
  margin: 0;
  border: 0;
  border-radius: 0;
  padding: 0;
  background: transparent;
  color: #f8fbf7;
  box-shadow: none;
}
.layout { display: grid; grid-template-columns: minmax(0, 1fr) 260px; gap: 34px; align-items: start; }
.reader-aside { display: grid; gap: 14px; position: sticky; top: 24px; }
.article {
  min-width: 0;
  border: 1px solid var(--line);
  border-radius: 8px;
  background: var(--paper);
  box-shadow: var(--shadow);
  padding: 34px;
}
.article > :first-child { margin-top: 0; }
.article p, .article li { max-width: var(--measure); }
h2:target, h3:target, h4:target {
  outline: 2px solid rgba(23, 108, 99, .25);
  outline-offset: 4px;
}
.toc, .page-tools {
  border: 1px solid var(--line);
  border-radius: 8px;
  background: rgba(255, 253, 248, .88);
  padding: 16px;
}
.toc a { display: block; padding: 4px 0; text-decoration: none; font-size: 13px; }
.toc .level-3 { padding-left: 12px; }
.page-tools { display: grid; gap: 8px; }
.page-tools .meta { display: block; margin: 2px 0 0; font-size: 12px; }
.tool-link {
  display: block;
  border: 1px solid var(--line);
  border-radius: 8px;
  padding: 8px 10px;
  color: var(--ink);
  text-decoration: none;
  font-size: 13px;
}
.tool-link:hover { border-color: var(--accent); color: var(--accent); }
code {
  border: 1px solid var(--line);
  border-radius: 5px;
  padding: 1px 5px;
  background: #f3f0e8;
  font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
  font-size: .92em;
}
pre {
  overflow: auto;
  max-width: 100%;
  border: 1px solid var(--line);
  border-radius: 8px;
  padding: 16px;
  background: #1d2521;
  color: #f8fbf7;
}
pre code { border: 0; padding: 0; background: transparent; color: inherit; }
blockquote {
  margin: 20px 0;
  border-left: 4px solid var(--accent);
  padding: 10px 18px;
  background: var(--wash-2);
  color: #314139;
}
.table-wrap {
  overflow-x: auto;
  max-width: 100%;
  margin: 20px 0;
  border: 1px solid var(--line);
  border-radius: 8px;
}
.table-action-map {
  border-color: rgba(23, 108, 99, .34);
  box-shadow: 0 12px 34px rgba(23, 108, 99, .08);
}
.table-action-map table { min-width: 760px; }
.table-action-map th { background: var(--wash-2); color: var(--accent); }
table { width: 100%; border-collapse: collapse; min-width: 620px; background: #fffefa; }
th, td { padding: 10px 12px; border-bottom: 1px solid var(--line); text-align: left; vertical-align: top; }
th { color: var(--muted); font-size: 12px; letter-spacing: .06em; text-transform: uppercase; background: #f5f1e9; }
.page-nav { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin-top: 24px; }
.page-nav a { padding: 14px; color: var(--ink); text-decoration: none; }
.page-nav span { display: block; color: var(--muted); font-size: 12px; font-weight: 800; letter-spacing: .08em; text-transform: uppercase; }
footer { max-width: 1040px; margin: 0 auto; padding: 16px 32px 42px; color: var(--muted); font-size: 13px; }
@media (max-width: 920px) {
  .shell { display: block; }
  .sidebar { position: relative; height: auto; border-right: 0; border-bottom: 1px solid var(--line); }
  .layout { display: block; }
  .reader-aside { position: relative; top: auto; margin-top: 18px; }
  h1 { font-size: 36px; }
  .heading-anchor { opacity: 1; margin-left: 0; width: auto; padding-right: 8px; float: none; }
}
@media (max-width: 620px) {
  .sidebar { padding: 16px 18px; }
  .sidebar .notice, .sidebar .nav-group { display: none; }
  .brand { margin-bottom: 0; }
  .hero, .content { padding: 30px 18px; }
  .article { padding: 22px; }
  .reference-surface { padding: 16px; }
  .cockpit-ritual-grid { grid-template-columns: repeat(4, minmax(0, 1fr)); }
  .cockpit-tile { min-height: 54px; padding: 12px; align-content: center; }
  .cockpit-tile strong { font-size: 16px; }
  .cockpit-tile span { display: none; }
  .cockpit-catalog-row { gap: 6px; }
  .cockpit-catalog-row a { padding: 6px 8px; font-size: 12px; }
  .page-nav { grid-template-columns: 1fr; }
}
"""


def sidebar(docs: list[Doc], active: str | None = None) -> str:
    lookup = {doc.filename: doc for doc in docs}
    groups: list[str] = []
    for index, lane in enumerate(COMPASS):
        links = []
        if lane.get("home"):
            active_class = " active" if active is None else ""
            links.append(f'<a class="nav-link{active_class}" href="index.html">Docs Home</a>')
        for filename in lane["docs"]:
            doc = lookup.get(filename)
            if not doc:
                continue
            active_class = " active" if active == doc.html_name else ""
            links.append(f'<a class="nav-link{active_class}" href="{h(doc.html_name)}">{h(doc.title)}</a>')
        divider = '<hr class="nav-divider">' if index > 0 else ""
        groups.append(f'{divider}<p class="nav-label">{h(lane["label"])}</p>{"".join(links)}')
    return f"""
<aside class="sidebar">
  <div class="brand">
    <strong>PrecodeOS Docs</strong>
    <span>Generated public reading surface</span>
  </div>
  <div class="notice">Generated from canonical Markdown in <code>docs/*.md</code> and selected root docs. Use the Markdown source for authority.</div>
  <nav class="nav-group" aria-label="Docs">
    {"".join(groups)}
  </nav>
</aside>
"""


def site_stamp(docs: list[Doc]) -> str:
    dates = [doc.last_updated for doc in docs if doc.last_updated]
    return max(dates) if dates else "unknown"


def page_shell(title: str, body: str, docs: list[Doc], active: str | None = None) -> str:
    generated_at = site_stamp(docs)
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="generator" content="PrecodeOS docs-html.py">
  <meta name="generated-at" content="{h(generated_at)}">
  <title>{h(title)} · PrecodeOS Docs</title>
  <style>{css()}</style>
</head>
<body>
  <div class="reading-progress" aria-hidden="true"><span id="reading-progress-bar"></span></div>
  <div class="shell">
    {sidebar(docs, active)}
    <main>
      {body}
      <footer>Generated from PrecodeOS Markdown docs. Markdown remains canonical.</footer>
    </main>
  </div>
  <script>
    (() => {{
      const bar = document.getElementById("reading-progress-bar");
      if (!bar) return;
      const update = () => {{
        const scrollable = document.documentElement.scrollHeight - window.innerHeight;
        const progress = scrollable > 0 ? Math.min(1, Math.max(0, window.scrollY / scrollable)) : 0;
        bar.style.transform = `scaleX(${{progress}})`;
      }};
      update();
      window.addEventListener("scroll", update, {{ passive: true }});
      window.addEventListener("resize", update);
    }})();
    (() => {{
      if (!navigator.clipboard) return;
      document.querySelectorAll("[data-copy-target]").forEach((button) => {{
        button.addEventListener("click", async () => {{
          const target = document.getElementById(button.getAttribute("data-copy-target"));
          if (!target) return;
          const original = button.textContent;
          try {{
            await navigator.clipboard.writeText(target.textContent || "");
            button.textContent = "Copied";
            window.setTimeout(() => {{ button.textContent = original; }}, 1400);
          }} catch (error) {{
            button.textContent = "Select text";
            window.setTimeout(() => {{ button.textContent = original; }}, 1800);
          }}
        }});
      }});
    }})();
  </script>
</body>
</html>
"""


def render_index(docs: list[Doc]) -> str:
    lookup = {doc.filename: doc for doc in docs}
    lanes = []
    for lane in COMPASS:
        links = []
        if lane.get("home"):
            links.append('<li><a href="index.html">Docs Home</a></li>')
        for filename in lane["docs"]:
            doc = lookup.get(filename)
            if doc:
                links.append(f'<li><a href="{h(doc.html_name)}">{h(doc.title)}</a></li>')
        lanes.append(
            f"""
<section class="lane">
  <p class="eyebrow">Learning Path</p>
  <h2>{h(lane["label"])}</h2>
  <p>{h(lane["summary"])}</p>
  <ul>{"".join(links)}</ul>
</section>
"""
        )
    cards = []
    for doc in docs:
        cards.append(
            f"""
<a class="doc-card" href="{h(doc.html_name)}">
  <strong>{h(doc.title)}</strong>
  <p>{h(doc.summary)}</p>
  <span class="meta"><span>{h(doc.filename)}</span><span>{h(doc.doc_class or "reference")}</span></span>
</a>
"""
        )
    body = f"""
<section class="hero">
  <p class="eyebrow">PrecodeOS Documentation</p>
  <h1>A guided reading surface for the Markdown that owns the truth.</h1>
  <p class="lede">Use these pages to find your way through setup, daily work, support, troubleshooting, and architecture. The original Markdown files remain the canonical docs.</p>
</section>
<section class="content">
  <div class="compass-grid">{"".join(lanes)}</div>
  <h2>All Docs</h2>
  <div class="doc-list">{"".join(cards)}</div>
</section>
"""
    return page_shell("Home", body, docs)


def render_toc(doc: Doc) -> str:
    if not doc.toc:
        return ""
    items = "".join(
        f'<a class="level-{item.level}" href="#{h(item.anchor)}">{h(item.text)}</a>' for item in doc.toc
    )
    return f'<aside class="toc"><p class="nav-label">On This Page</p>{items}</aside>'


def render_page_tools(doc: Doc, source_href: str) -> str:
    return f"""<aside class="page-tools" aria-label="Reading tools">
  <p class="nav-label">Reading Tools</p>
  <a class="tool-link" href="{h(source_href)}">Source Markdown</a>
  <a class="tool-link" href="#top">Back to top</a>
  <p class="meta">Progress and section links are reading aids only. Markdown remains canonical.</p>
</aside>"""


def grouped_prompt_cards(cards: list[PromptCard]) -> dict[str, list[PromptCard]]:
    grouped: dict[str, list[PromptCard]] = {}
    for card in cards:
        grouped.setdefault(card.category, []).append(card)
    return grouped


def grouped_protocol_cards(cards: list[ProtocolCard]) -> dict[str, list[ProtocolCard]]:
    grouped: dict[str, list[ProtocolCard]] = {}
    for card in cards:
        grouped.setdefault(card.category, []).append(card)
    return grouped


def render_copy_block(label: str, text: str, copy_id: str) -> str:
    return f"""
<div class="copy-block">
  <div class="copy-block-header">
    <span>{h(label)}</span>
    <button class="copy-button" type="button" data-copy-target="{h(copy_id)}">Copy</button>
  </div>
  <pre id="{h(copy_id)}"><code>{h(text)}</code></pre>
</div>
"""


def render_prompt_card(card: PromptCard, index: int) -> str:
    copy_id = f"prompt-copy-{index}"
    return f"""
<article class="reference-card">
  <h4>{h(card.title)}</h4>
  <p>{h(card.description)}</p>
  <div class="label-row"><strong>When to use</strong><span>{h(card.when)}</span></div>
  {render_copy_block("Copy this prompt", card.prompt, copy_id)}
  <p class="meta"><a href="{h(card.source)}">Source: PROMPT-PATTERNS.md</a></p>
</article>
"""


def render_protocol_card(card: ProtocolCard, index: int) -> str:
    copy_id = f"protocol-copy-{index}"
    return f"""
<article class="reference-card">
  <h4>{h(card.title)}</h4>
  <p>{h(card.authority)}</p>
  <div class="label-row"><strong>Load when</strong><span>{h(card.load_when)}</span></div>
  {render_copy_block("Say this to load it", card.launch, copy_id)}
  <p class="meta"><a href="../tasks/reference/{h(card.filename)}">{h(card.filename)}</a><span>{h(card.version)}</span><span>Updated {h(card.last_updated)}</span></p>
</article>
"""


def render_reference_surface() -> str:
    prompt_cards = extract_prompt_cards()
    protocol_cards = extract_protocol_cards()
    prompt_groups = grouped_prompt_cards(prompt_cards)
    protocol_groups = grouped_protocol_cards(protocol_cards)
    categories = ["Discovery", "Planning", "Build", "Review", "Recovery"]
    chips = []
    for prefix, grouped in (("Prompts", prompt_groups), ("Protocols", protocol_groups)):
        for category in categories:
            if category in grouped:
                anchor = slugify(f"{prefix} {category}")
                chips.append(f'<a class="jump-chip" href="#{h(anchor)}">{h(prefix)} · {h(category)}</a>')
    prompt_sections = []
    prompt_index = 0
    for category in categories:
        cards = prompt_groups.get(category, [])
        if not cards:
            continue
        rendered_cards = []
        for card in cards:
            prompt_index += 1
            rendered_cards.append(render_prompt_card(card, prompt_index))
        prompt_sections.append(
            f"""
<section class="reference-group" id="{h(slugify(f'Prompts {category}'))}">
  <h3>{h(category)}</h3>
  <div class="reference-card-grid">{"".join(rendered_cards)}</div>
</section>
"""
        )
    protocol_sections = []
    protocol_index = 0
    for category in categories:
        cards = protocol_groups.get(category, [])
        if not cards:
            continue
        rendered_cards = []
        for card in cards:
            protocol_index += 1
            rendered_cards.append(render_protocol_card(card, protocol_index))
        protocol_sections.append(
            f"""
<section class="reference-group" id="{h(slugify(f'Protocols {category}'))}">
  <h3>{h(category)}</h3>
  <div class="reference-card-grid">{"".join(rendered_cards)}</div>
</section>
"""
        )
    return f"""
<section class="reference-surface" aria-labelledby="precode-prompts-protocols">
  <p class="eyebrow">Generated Reference Aid</p>
  <h2 id="precode-prompts-protocols">PrecodeOS Prompts And Protocols</h2>
  <p class="lede">These cards make the existing prompt and protocol surfaces easier to browse and copy from the Daily Cockpit. They are generated from canonical Markdown; source files remain authoritative.</p>
  <div class="jump-chips">{"".join(chips)}</div>
  <h2>PrecodeOS Prompts</h2>
  <p>Copyable prompt cards from <code>tasks/reference/PROMPT-PATTERNS.md</code>. They do not approve work, choose tasks, activate beads, accept review, or replace active memory and owner files.</p>
  {"".join(prompt_sections)}
  <h2>PrecodeOS Protocols</h2>
  <p>Protocol cards for every <code>tasks/reference/*PROTOCOL.md</code> file. Use them only when their load trigger applies; do not load every protocol by default.</p>
  {"".join(protocol_sections)}
</section>
"""


def render_cockpit_strip() -> str:
    return """
  <div class="cockpit-strip" aria-label="Daily Cockpit ritual">
    <div class="cockpit-ritual-grid">
      <a class="cockpit-tile" href="#daily-loop">
        <strong>Daily Loop</strong>
        <span>Run the build loop: Active, Changed, Proven, Parked, Approval, Next.</span>
      </a>
      <a class="cockpit-tile" href="#next">
        <strong>Next</strong>
        <span>Choose the next safe move, approval, recovery path, or transition candidate.</span>
      </a>
      <a class="cockpit-tile" href="#health">
        <strong>Health</strong>
        <span>Check state, warnings, proof freshness, and whether the system is safe to use.</span>
      </a>
      <a class="cockpit-tile" href="#diary">
        <strong>Diary</strong>
        <span>Capture what transpired, changed, was learned, parked, or needs promotion.</span>
      </a>
    </div>
    <div class="cockpit-catalog-row" aria-label="Daily Cockpit catalogs">
      <span>Reference shelves</span>
      <a href="#full-prompt-patterns-catalog">Prompt Patterns Catalog</a>
      <a href="#full-protocol-catalog">Protocol Catalog</a>
      <a href="#precode-prompts-protocols">Copyable HTML Cards</a>
    </div>
  </div>
"""


def render_host_agent_return_surface() -> str:
    cards = [
        (
            "Prepare",
            "Name the active bead, primary authority, files in play, proof needed, and stop condition.",
            "Prepare host-agent work: show active bead, primary authority, files in play, proof needed, approval still required, and stop condition before any host agent edits.",
        ),
        (
            "Bound",
            "Set access level, allowed actions, approval gates, forbidden actions, and Run Contract needs.",
            "Bound this agent: name the current access level, allowed actions, approval required before risky actions, forbidden actions, proof needed, Run Contract needs, and stop conditions.",
        ),
        (
            "Send",
            "Give one scoped approved-bead or bounded prompt to the host agent.",
            "Use Approved-Bead Handoff for the current approved bead. Restate active bead, authority, files in play, allowed actions, proof, checks, stop conditions, blocked escape, review-return shape, approval gates, and generated-report warning before editing.",
        ),
        (
            "Return",
            "Require changed files, checks, manual verification, risks, approvals, and forbidden actions not taken.",
            "Review returned agent work before I accept it. Show scope returned, changed files, checks and results, manual verification, proof still missing, unresolved risks, approval still required, parked follow-ups, forbidden actions not taken, and next safe prompt.",
        ),
        (
            "Prove",
            "Separate recorded checks and manual verification from generated evidence and agent confidence.",
            "Prove: show recorded checks, manual verification, what each proof source does and does not prove, what generated evidence does not decide, and what I should verify manually before acceptance.",
        ),
        (
            "Review",
            "Recommend continue, review, split, block, or handoff without accepting work.",
            "Review: recommend only continue, review, split, block, or handoff. Do not accept implementation, approve review, approve transition, activate another bead, mutate external systems, or treat generated reports, generated HTML, PR status, screenshots, or chat summaries as proof by themselves.",
        ),
        (
            "Close/Next",
            "Record digest, parked follow-ups, approval state, and next safe prompt without activation.",
            "Close: run session close, summarize the work digest, suggested commit message, checks, blockers, approvals, learning context, parked follow-ups, next safe prompt, and end with Close State.",
        ),
    ]
    rendered_cards = []
    for index, (title, summary, prompt) in enumerate(cards):
        rendered_cards.append(
            f"""
    <article class="reference-card">
      <h4>{h(title)}</h4>
      <p>{h(summary)}</p>
      {render_copy_block("Copy this cockpit prompt", prompt, f"host-agent-return-{index}")}
    </article>
"""
        )
    return f"""
<section class="reference-surface" id="host-agent-return-loop" aria-label="Host-Agent Return Loop">
  <p class="eyebrow">Agent Work Cockpit V2</p>
  <h2>Host-Agent Return Loop</h2>
  <p class="lede"><code>Prepare -&gt; Bound -&gt; Send -&gt; Return -&gt; Prove -&gt; Review -&gt; Close/Next</code></p>
  <p class="lede">Use these copy cards when coordinating Codex, Claude Code, Cursor, Copilot, Gemini, or another host agent. They are generated from the package contract for easier browsing; canonical Markdown and protocols remain authoritative.</p>
  <div class="cockpit-catalog-row" aria-label="Host-Agent Return Loop sources">
    <span>Source authority</span>
    <a href="../docs/PRECODE-DAILY-COCKPIT.md">Daily Cockpit Markdown</a>
    <a href="../tasks/reference/PROMPT-PATTERNS.md">Prompt Patterns</a>
    <a href="../tasks/reference/SESSION-COMPLETION-HANDOFF-PROTOCOL.md">Session Completion/Handoff</a>
  </div>
  <div class="reference-card-grid">{"".join(rendered_cards)}</div>
</section>
"""


def render_doc_page(doc: Doc, docs: list[Doc], previous_doc: Doc | None, next_doc: Doc | None) -> str:
    previous_link = (
        f'<a href="{h(previous_doc.html_name)}"><span>Previous</span>{h(previous_doc.title)}</a>'
        if previous_doc
        else "<span></span>"
    )
    next_link = (
        f'<a href="{h(next_doc.html_name)}"><span>Next</span>{h(next_doc.title)}</a>' if next_doc else "<span></span>"
    )
    source_href = f"../docs/{doc.filename}" if doc.path.parent == DOCS else f"../{doc.filename}"
    reader_aside_items = [render_page_tools(doc, source_href)]
    toc = render_toc(doc)
    if toc:
        reader_aside_items.append(toc)
    reader_aside = "\n    ".join(reader_aside_items)
    is_cockpit = doc.filename == "PRECODE-DAILY-COCKPIT.md"
    hero_class = "hero cockpit-hero" if is_cockpit else "hero"
    cockpit_strip = render_cockpit_strip() if is_cockpit else ""
    hero_summary = (
        "Daily operating surface: run the Daily Loop, choose Next, check Health, capture Diary. "
        "Prompt and protocol catalogs stay below as reference shelves."
        if is_cockpit
        else doc.summary
    )
    body = f"""
<section class="{hero_class}" id="top">
  <p class="eyebrow">PrecodeOS Doc</p>
  <h1>{h(doc.title)}</h1>
  <p class="lede">{h(hero_summary)}</p>
  <p class="meta"><a href="{h(source_href)}">Source Markdown</a><span>{h(doc.version)}</span><span>Updated {h(doc.last_updated)}</span></p>
  {cockpit_strip}
</section>
<section class="content layout">
  <article class="article">
    {doc.content_html}
    {render_host_agent_return_surface() if is_cockpit else ""}
    {render_reference_surface() if is_cockpit else ""}
    <nav class="page-nav" aria-label="Previous and next docs">{previous_link}{next_link}</nav>
  </article>
  <div class="reader-aside">
    {reader_aside}
  </div>
</section>
"""
    return page_shell(doc.title, body, docs, active=doc.html_name)


def render_site(output_dir: Path) -> None:
    docs = load_docs()
    write_text(output_dir / "index.html", render_index(docs))
    for index, doc in enumerate(docs):
        previous_doc = docs[index - 1] if index > 0 else None
        next_doc = docs[index + 1] if index + 1 < len(docs) else None
        write_text(output_dir / doc.html_name, render_doc_page(doc, docs, previous_doc, next_doc))


def compare_dirs(expected: Path, actual: Path) -> list[str]:
    diffs: list[str] = []
    expected_files = sorted(path.relative_to(expected).as_posix() for path in expected.rglob("*") if path.is_file())
    actual_files = sorted(path.relative_to(actual).as_posix() for path in actual.rglob("*") if path.is_file()) if actual.is_dir() else []
    for filename in sorted(set(expected_files) | set(actual_files)):
        expected_path = expected / filename
        actual_path = actual / filename
        if not actual_path.is_file():
            diffs.append(f"missing {filename}")
            continue
        if not expected_path.is_file():
            diffs.append(f"extra {filename}")
            continue
        if expected_path.read_text(encoding="utf-8") != actual_path.read_text(encoding="utf-8"):
            diffs.append(f"stale {filename}")
    return diffs


def generate() -> int:
    if OUTPUT.exists():
        shutil.rmtree(OUTPUT)
    render_site(OUTPUT)
    print(f"Generated {OUTPUT.relative_to(ROOT).as_posix()}")
    return 0


def check() -> int:
    with tempfile.TemporaryDirectory(prefix="precode-docs-html-") as tmp:
        expected = Path(tmp) / "docs-html"
        render_site(expected)
        diffs = compare_dirs(expected, OUTPUT)
    if diffs:
        print("docs-html is stale:")
        for diff in diffs:
            print(f"- {diff}")
        return 1
    print("docs-html is up to date")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Generate the public PrecodeOS HTML docs site from docs/*.md and selected root docs."
    )
    parser.add_argument("--check", action="store_true", help="fail if docs-html/ does not match the generated output")
    args = parser.parse_args(argv)
    return check() if args.check else generate()


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
