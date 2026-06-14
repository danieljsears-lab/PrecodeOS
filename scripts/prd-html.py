#!/usr/bin/env python3
# Version: v0.2.0
# Last updated: 2026-06-14
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
PRDS = ROOT / "tasks" / "prds"
OUTPUT = ROOT / "tasks" / "prds-html"
SKIP_PRDS = {"PRD-000-template.md", "PRD-SHARD-SCHEMA.md"}

sys.path.insert(0, str(ROOT / "scripts"))

from os_parser import extract_contract_values, parse_sections, split_frontmatter


@dataclass(frozen=True)
class TocItem:
    level: int
    text: str
    anchor: str


@dataclass(frozen=True)
class Prd:
    path: Path
    filename: str
    html_name: str
    title: str
    anchor: str
    frontmatter: dict[str, Any]
    authority: str
    not_authority: str
    load_when: str
    doc_class: str
    version: str
    last_updated: str
    sections: dict[str, str]
    content_html: str
    toc: list[TocItem]


@dataclass(frozen=True)
class MarkdownTable:
    headers: list[str]
    rows: list[list[str]]


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


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
    return match.group(1).strip() if match else "Untitled PRD"


def extract_anchor(text: str) -> str:
    match = re.search(r"<!--\s*ANCHOR:\s*([a-z0-9_-]+)\s*-->", text, re.IGNORECASE)
    return match.group(1).strip() if match else slugify(extract_title(text))


def extract_metadata(text: str, label: str) -> str:
    match = re.search(rf"^{re.escape(label)}:\s*(.+)$", text, re.MULTILINE)
    return match.group(1).strip() if match else ""


def strip_metadata(text: str) -> str:
    _, body = split_frontmatter(text)
    lines = body.splitlines()
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


def source_href(prd: Prd, anchor: str | None = None) -> str:
    suffix = f"#{anchor}" if anchor else ""
    return f"../prds/{prd.filename}{suffix}"


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
    if clean.startswith("tasks/prds/") and clean.endswith(".md"):
        return f"../prds/{Path(clean).name}{anchor}"
    if clean.startswith("_maintainer/"):
        return f"../../{clean}{anchor}"
    if clean.startswith("docs/"):
        return f"../../{clean}{anchor}"
    if clean.startswith("tasks/reference/"):
        return f"../reference/{Path(clean).name}{anchor}"
    if clean.endswith(".md") and "/" not in clean:
        candidate = PRDS / clean
        if candidate.is_file():
            return f"../prds/{clean}{anchor}"
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
    return lines[index].strip().startswith("|") and re.match(
        r"^\s*\|?\s*:?-{3,}:?\s*(\|\s*:?-{3,}:?\s*)+\|?\s*$",
        lines[index + 1],
    ) is not None


def table_cells(row: str) -> list[str]:
    return [cell.strip() for cell in row.strip().strip("|").split("|")]


def first_markdown_table(markdown: str) -> MarkdownTable | None:
    lines = [line for line in markdown.splitlines() if line.strip()]
    for index in range(len(lines)):
        if is_table_start(lines, index):
            headers = table_cells(lines[index])
            rows: list[list[str]] = []
            cursor = index + 2
            while cursor < len(lines) and lines[cursor].strip().startswith("|"):
                row = table_cells(lines[cursor])
                if len(row) < len(headers):
                    row.extend([""] * (len(headers) - len(row)))
                rows.append(row[: len(headers)])
                cursor += 1
            return MarkdownTable(headers=headers, rows=rows)
    return None


def render_table(lines: list[str]) -> str:
    headers = table_cells(lines[0])
    rows = [table_cells(line) for line in lines[2:]]
    head = "".join(f"<th>{inline(cell)}</th>" for cell in headers)
    body_rows = []
    for row in rows:
        body_rows.append("<tr>" + "".join(f"<td>{inline(cell)}</td>" for cell in row) + "</tr>")
    return f'<div class="table-wrap"><table><thead><tr>{head}</tr></thead><tbody>{"".join(body_rows)}</tbody></table></div>'


def render_list(items: list[str], ordered: bool) -> str:
    tag = "ol" if ordered else "ul"
    rows = "".join(f"<li>{inline(item)}</li>" for item in items)
    return f"<{tag}>{rows}</{tag}>"


def render_markdown(markdown: str) -> tuple[str, list[TocItem]]:
    lines = strip_metadata(markdown).splitlines()
    html: list[str] = []
    toc: list[TocItem] = []
    paragraph: list[str] = []
    used_slugs: dict[str, int] = {}
    index = 0

    def flush_paragraph() -> None:
        if paragraph:
            html.append(f"<p>{inline(' '.join(paragraph))}</p>")
            paragraph.clear()

    while index < len(lines):
        line = lines[index]
        stripped = line.strip()

        if not stripped:
            flush_paragraph()
            index += 1
            continue

        if stripped.startswith("<!--"):
            index += 1
            continue

        if stripped.startswith("```"):
            flush_paragraph()
            lang = stripped.strip("`").strip()
            code: list[str] = []
            index += 1
            while index < len(lines) and not lines[index].strip().startswith("```"):
                code.append(lines[index])
                index += 1
            index += 1
            class_attr = f' class="language-{h(lang)}"' if lang else ""
            html.append(f"<pre><code{class_attr}>{h(chr(10).join(code))}</code></pre>")
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

        heading = re.match(r"^(#{1,4})\s+(.+)$", stripped)
        if heading:
            flush_paragraph()
            level = len(heading.group(1))
            text = heading.group(2).strip()
            anchor = unique_slug(slugify(text), used_slugs)
            if level <= 3:
                toc.append(TocItem(level=level, text=text, anchor=anchor))
            html.append(f'<h{level} id="{h(anchor)}">{inline(text)}</h{level}>')
            index += 1
            continue

        unordered: list[str] = []
        while index < len(lines) and lines[index].strip().startswith("- "):
            unordered.append(lines[index].strip()[2:].strip())
            index += 1
        if unordered:
            flush_paragraph()
            html.append(render_list(unordered, ordered=False))
            continue

        ordered: list[str] = []
        while index < len(lines) and re.match(r"^\d+\.\s+", lines[index].strip()):
            ordered.append(re.sub(r"^\d+\.\s+", "", lines[index].strip()))
            index += 1
        if ordered:
            flush_paragraph()
            html.append(render_list(ordered, ordered=True))
            continue

        paragraph.append(stripped)
        index += 1

    flush_paragraph()
    return "\n".join(html), toc


def prd_files() -> list[Path]:
    return sorted(
        path
        for path in PRDS.glob("PRD-*.md")
        if path.name not in SKIP_PRDS and path.is_file()
    )


def load_prds() -> list[Prd]:
    prds: list[Prd] = []
    for path in prd_files():
        text = read_text(path)
        frontmatter, _ = split_frontmatter(text)
        contract = extract_contract_values(text)
        content_html, toc = render_markdown(text)
        prds.append(
            Prd(
                path=path,
                filename=path.name,
                html_name=path.with_suffix(".html").name,
                title=extract_title(text),
                anchor=extract_anchor(text),
                frontmatter=frontmatter,
                authority=contract.get("authority", ""),
                not_authority=contract.get("not_authority", ""),
                load_when=contract.get("load_when", ""),
                doc_class=contract.get("class", ""),
                version=extract_metadata(text, "Document version"),
                last_updated=extract_metadata(text, "Last updated"),
                sections=parse_sections(text),
                content_html=content_html,
                toc=toc,
            )
        )
    return prds


def section(prd: Prd, name: str) -> str:
    return prd.sections.get(name, "")


def section_anchor(prd: Prd, heading: str) -> str:
    return slugify(heading)


def status_class(status: str) -> str:
    return slugify(status or "unknown")


def display_value(value: Any, fallback: str = "unknown") -> str:
    if isinstance(value, list):
        return ", ".join(str(item) for item in value) if value else "none"
    if value is None or value == "":
        return fallback
    return str(value)


def table_preview(markdown: str, *, max_rows: int = 6) -> str:
    lines = [line for line in markdown.splitlines() if line.strip()]
    for index in range(len(lines)):
        if is_table_start(lines, index):
            table_lines = [lines[index], lines[index + 1]]
            row_count = 0
            cursor = index + 2
            while cursor < len(lines) and lines[cursor].strip().startswith("|") and row_count < max_rows:
                table_lines.append(lines[cursor])
                row_count += 1
                cursor += 1
            return render_table(table_lines)
    return '<p class="empty">None recorded.</p>'


def markdown_table_cell(value: str) -> str:
    return (
        value.replace("\r\n", "\n")
        .replace("\r", "\n")
        .replace("\n", "<br>")
        .replace("|", "&#124;")
        .strip()
    )


def markdown_table(table: MarkdownTable) -> str:
    separator = ["---"] * len(table.headers)
    lines = [
        "| " + " | ".join(markdown_table_cell(cell) for cell in table.headers) + " |",
        "| " + " | ".join(separator) + " |",
    ]
    for row in table.rows:
        lines.append("| " + " | ".join(markdown_table_cell(cell) for cell in row) + " |")
    return "\n".join(lines)


def acceptance_cockpit(prd: Prd) -> str:
    acceptance = section(prd, "Acceptance Oracle Matrix")
    table = first_markdown_table(acceptance)
    if table is None:
        return '<p class="empty">No Acceptance Oracle Matrix table found for export.</p>'

    header_html = "".join(f"<th>{h(header)}</th>" for header in table.headers)
    rows_html = []
    for row in table.rows:
        cells = []
        for cell in row:
            cells.append(f'<td><textarea data-cockpit-cell>{h(cell)}</textarea></td>')
        rows_html.append("<tr>" + "".join(cells) + "</tr>")

    fallback_block = "## Acceptance Oracle Matrix\n\n" + markdown_table(table)
    return f"""
    <section class="cockpit" data-acceptance-cockpit data-source="{h(prd.filename)}">
      <div class="cockpit-header">
        <div>
          <h3>Acceptance Oracle Export Cockpit</h3>
          <p class="muted">Edit cells locally, then export a proposed Markdown replacement block. Apply it manually to <code>{h(prd.filename)}</code>; this page cannot write source files or approve PRD changes.</p>
        </div>
        <button type="button" data-export-markdown>Export Markdown</button>
      </div>
      <div class="table-wrap cockpit-table">
        <table>
          <thead><tr>{header_html}</tr></thead>
          <tbody>{"".join(rows_html)}</tbody>
        </table>
      </div>
      <label class="cockpit-export-label" for="acceptance-export-{h(prd.anchor)}">Proposed Markdown replacement block</label>
      <textarea id="acceptance-export-{h(prd.anchor)}" class="cockpit-export" data-export-output readonly>{h(fallback_block)}</textarea>
      <p class="muted">Proposal only: manually review and paste into the canonical Markdown PRD, then regenerate and check <code>tasks/prds-html/</code>. No approval, write-back, task selection, bead activation, or implementation acceptance happens here.</p>
    </section>
    """


def has_blocking_open_question(prd: Prd) -> bool:
    open_questions = section(prd, "Open Questions").lower()
    return "| yes |" in open_questions or open_questions.count("blocking") > 1


def approval_summary(prd: Prd) -> str:
    approval = section(prd, "Approval")
    if not approval:
        return "No approval section found."
    approved_by = re.search(r"^- Approved by:\s*(.+)$", approval, re.MULTILINE)
    approved_on = re.search(r"^- Approved on:\s*(.+)$", approval, re.MULTILINE)
    if approved_by or approved_on:
        return f"{approved_by.group(1).strip() if approved_by else 'unknown'} on {approved_on.group(1).strip() if approved_on else 'unknown'}"
    return "Approval section present; details not parsed."


def next_safe_decision(prd: Prd) -> str:
    status = str(prd.frontmatter.get("status", "")).lower()
    if has_blocking_open_question(prd):
        return "Resolve blocking open questions in the Markdown PRD before approval, decomposition, or implementation."
    if status == "approved":
        return "Use the Markdown PRD for decomposition or review; do not treat this HTML page as approval, bead activation, or implementation permission."
    if status in {"draft", "needs_info"}:
        return "Continue shaping the Markdown PRD and resolve missing information before approval or bead creation."
    if status == "superseded":
        return "Find the replacement PRD or decision record before using this shard for new work."
    return "Check the Markdown PRD state before deciding the next action."


def guardrail_text() -> str:
    return (
        "This HTML is a generated review convenience. It cannot approve PRDs, activate beads, "
        "choose tasks, accept implementation, write source Markdown, promote generated text, or replace `tasks/prds/*.md`."
    )


def style() -> str:
    return """
    :root {
      color-scheme: light;
      --bg: #f7f8fa;
      --panel: #ffffff;
      --ink: #1f2933;
      --muted: #5f6f82;
      --line: #d8dee8;
      --accent: #0f766e;
      --accent-2: #3949ab;
      --warn: #9a3412;
      --code: #eef2f7;
    }
    * { box-sizing: border-box; }
    body {
      margin: 0;
      background: var(--bg);
      color: var(--ink);
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      line-height: 1.5;
    }
    a { color: var(--accent-2); text-decoration-thickness: 1px; }
    header {
      background: var(--panel);
      border-bottom: 1px solid var(--line);
      padding: 28px max(24px, calc((100vw - 1120px) / 2));
    }
    main { max-width: 1120px; margin: 0 auto; padding: 24px; }
    .eyebrow { color: var(--accent); font-size: 0.78rem; font-weight: 700; letter-spacing: 0.08em; text-transform: uppercase; }
    h1 { margin: 6px 0 10px; font-size: 2rem; line-height: 1.15; letter-spacing: 0; }
    h2 { margin-top: 34px; padding-top: 10px; border-top: 1px solid var(--line); font-size: 1.35rem; letter-spacing: 0; }
    h3 { margin-top: 24px; font-size: 1.1rem; letter-spacing: 0; }
    h4 { margin-top: 20px; font-size: 1rem; letter-spacing: 0; }
    .summary, .notice, .card, .toc {
      background: var(--panel);
      border: 1px solid var(--line);
      border-radius: 8px;
      padding: 16px;
    }
    .notice { border-left: 4px solid var(--warn); }
    .summary-grid, .card-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
      gap: 12px;
      margin: 18px 0;
    }
    .metric { background: #f9fafb; border: 1px solid var(--line); border-radius: 6px; padding: 12px; }
    .metric span { display: block; color: var(--muted); font-size: 0.8rem; }
    .metric strong { display: block; margin-top: 4px; overflow-wrap: anywhere; }
    .status { display: inline-flex; align-items: center; border-radius: 999px; padding: 3px 10px; font-size: 0.78rem; font-weight: 700; background: #e5e7eb; }
    .status.approved { background: #d1fae5; color: #065f46; }
    .status.draft, .status.needs-info { background: #ffedd5; color: #9a3412; }
    .status.superseded { background: #e5e7eb; color: #4b5563; }
    .table-wrap { overflow-x: auto; margin: 14px 0; border: 1px solid var(--line); border-radius: 8px; background: var(--panel); }
    table { width: 100%; border-collapse: collapse; min-width: 620px; }
    th, td { border-bottom: 1px solid var(--line); padding: 10px 12px; text-align: left; vertical-align: top; }
    th { background: #eef2f7; font-size: 0.82rem; }
    tr:last-child td { border-bottom: 0; }
    code { background: var(--code); border-radius: 4px; padding: 1px 4px; }
    pre { overflow-x: auto; background: #111827; color: #f9fafb; border-radius: 8px; padding: 14px; }
    pre code { background: transparent; padding: 0; }
    .layout { display: grid; grid-template-columns: minmax(0, 1fr) 260px; gap: 20px; align-items: start; }
    .toc { position: sticky; top: 16px; }
    .toc a { display: block; margin: 6px 0; font-size: 0.9rem; }
    .toc .level-3 { margin-left: 12px; color: var(--muted); }
    .empty, .muted { color: var(--muted); }
    .source-links { display: flex; flex-wrap: wrap; gap: 10px; margin-top: 12px; }
    .source-links a { font-weight: 600; }
    button {
      appearance: none;
      border: 1px solid var(--accent);
      border-radius: 6px;
      background: var(--accent);
      color: #ffffff;
      cursor: pointer;
      font: inherit;
      font-weight: 700;
      padding: 8px 12px;
    }
    button:focus-visible, textarea:focus-visible { outline: 3px solid #99f6e4; outline-offset: 2px; }
    .cockpit { margin: 18px 0; background: #f8fafc; border: 1px solid var(--line); border-radius: 8px; padding: 16px; }
    .cockpit-header { display: flex; gap: 16px; justify-content: space-between; align-items: flex-start; }
    .cockpit-header h3 { margin: 0 0 6px; }
    .cockpit-header p { margin: 0; }
    .cockpit-table textarea {
      width: 100%;
      min-width: 160px;
      min-height: 72px;
      resize: vertical;
      border: 1px solid var(--line);
      border-radius: 6px;
      padding: 8px;
      color: var(--ink);
      font: inherit;
      line-height: 1.35;
      background: #ffffff;
    }
    .cockpit-export-label { display: block; margin: 14px 0 6px; font-weight: 700; }
    .cockpit-export {
      width: 100%;
      min-height: 180px;
      resize: vertical;
      border: 1px solid var(--line);
      border-radius: 6px;
      padding: 10px;
      font: 0.9rem ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
      background: #ffffff;
      color: var(--ink);
    }
    @media (max-width: 860px) {
      header { padding: 24px 18px; }
      main { padding: 18px; }
      .layout { display: block; }
      .toc { position: static; margin-bottom: 18px; }
      .cockpit-header { display: block; }
      .cockpit-header button { margin-top: 12px; }
    }
    """


def script() -> str:
    return """
<script>
(() => {
  const normalizeCell = (value) => value
    .replace(/\\r\\n/g, "\\n")
    .replace(/\\r/g, "\\n")
    .replace(/\\n/g, "<br>")
    .replace(/\\|/g, "&#124;")
    .trim();

  const tableToMarkdown = (cockpit) => {
    const headers = Array.from(cockpit.querySelectorAll("thead th")).map((cell) => normalizeCell(cell.textContent || ""));
    const rows = Array.from(cockpit.querySelectorAll("tbody tr")).map((row) =>
      Array.from(row.querySelectorAll("[data-cockpit-cell]")).map((cell) => normalizeCell(cell.value || ""))
    );
    const separator = headers.map(() => "---");
    const line = (cells) => `| ${cells.join(" | ")} |`;
    return [
      "## Acceptance Oracle Matrix",
      "",
      line(headers),
      line(separator),
      ...rows.map(line),
    ].join("\\n");
  };

  document.querySelectorAll("[data-acceptance-cockpit]").forEach((cockpit) => {
    const output = cockpit.querySelector("[data-export-output]");
    const button = cockpit.querySelector("[data-export-markdown]");
    const exportMarkdown = () => {
      output.value = tableToMarkdown(cockpit);
      output.focus();
      output.select();
    };
    cockpit.addEventListener("input", exportMarkdown);
    button.addEventListener("click", exportMarkdown);
  });
})();
</script>
"""


def page_shell(title: str, body: str) -> str:
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{h(title)}</title>
  <style>{style()}</style>
</head>
<body>
{body}
{script()}
</body>
</html>
"""


def render_index(prds: list[Prd]) -> str:
    rows = []
    for prd in prds:
        status = display_value(prd.frontmatter.get("status"))
        rows.append(
            "<tr>"
            f'<td><a href="{h(prd.html_name)}">{h(prd.title)}</a></td>'
            f'<td><span class="status {h(status_class(status))}">{h(status)}</span></td>'
            f"<td>{h(display_value(prd.frontmatter.get('risk_level')))}</td>"
            f"<td>{h(display_value(prd.frontmatter.get('feature_link')))}</td>"
            f'<td><a href="{h(source_href(prd, prd.anchor))}">{h(prd.filename)}</a></td>'
            f"<td>{h(next_safe_decision(prd))}</td>"
            "</tr>"
        )
    table = (
        '<div class="table-wrap"><table><thead><tr>'
        "<th>PRD</th><th>Status</th><th>Risk</th><th>Feature</th><th>Markdown source</th><th>Next safe review decision</th>"
        "</tr></thead><tbody>"
        + "".join(rows)
        + "</tbody></table></div>"
    )
    body = f"""
<header>
  <p class="eyebrow">Generated PRD review surface</p>
  <h1>Precode PRD Review Index</h1>
  <p class="muted">Static HTML generated from canonical Markdown PRD shards in <code>tasks/prds/</code>.</p>
  <div class="source-links">
    <a href="../prds/">Markdown PRD folder</a>
  </div>
</header>
<main>
  <section class="notice">
    <strong>Not authority:</strong> {inline(guardrail_text())}
  </section>
  <section class="summary-grid">
    <div class="metric"><span>Rendered PRDs</span><strong>{len(prds)}</strong></div>
    <div class="metric"><span>Source</span><strong>tasks/prds/*.md</strong></div>
    <div class="metric"><span>Generated output</span><strong>tasks/prds-html/*.html</strong></div>
  </section>
  {table}
</main>
"""
    return page_shell("Precode PRD Review Index", body)


def render_prd_page(prd: Prd) -> str:
    status = display_value(prd.frontmatter.get("status"))
    metrics = [
        ("Status", f'<span class="status {h(status_class(status))}">{h(status)}</span>'),
        ("Risk", h(display_value(prd.frontmatter.get("risk_level")))),
        ("Feature", h(display_value(prd.frontmatter.get("feature_link")))),
        ("Features status", h(display_value(prd.frontmatter.get("features_status")))),
        ("Approval", h(approval_summary(prd))),
        ("Last updated", h(prd.last_updated or "unknown")),
    ]
    metric_html = "".join(f'<div class="metric"><span>{label}</span><strong>{value}</strong></div>' for label, value in metrics)
    toc = "".join(f'<a class="level-{item.level}" href="#{h(item.anchor)}">{h(item.text)}</a>' for item in prd.toc if item.level >= 2)
    if not toc:
        toc = '<p class="empty">No headings parsed.</p>'
    body = f"""
<header>
  <p class="eyebrow">Generated PRD review surface</p>
  <h1>{h(prd.title)}</h1>
  <p class="muted">Static HTML generated from <code>{h(prd.filename)}</code>. Markdown remains canonical.</p>
  <div class="source-links">
    <a href="index.html">PRD index</a>
    <a href="{h(source_href(prd, prd.anchor))}">Canonical Markdown source</a>
  </div>
</header>
<main>
  <section class="notice">
    <strong>Not authority:</strong> {inline(guardrail_text())}
  </section>
  <section class="summary-grid">{metric_html}</section>
  <section class="summary">
    <h2 id="review-cues">Review Cues</h2>
    <p><strong>Next safe review decision:</strong> {h(next_safe_decision(prd))}</p>
    <p><strong>Authority:</strong> {h(prd.authority or "See Markdown source.")}</p>
    <p><strong>Not authority:</strong> {h(prd.not_authority or "Generated HTML is not authority.")}</p>
    <h3>Unresolved blockers and questions</h3>
    {table_preview(section(prd, "Open Questions"), max_rows=8)}
    <h3>Requirements</h3>
    {table_preview(section(prd, "Requirements"), max_rows=12)}
    <h3>Acceptance oracle export</h3>
    {acceptance_cockpit(prd)}
    <h3>Risk and permission model</h3>
    {render_markdown(section(prd, "Risk And Permission Model"))[0] if section(prd, "Risk And Permission Model") else '<p class="empty">None recorded.</p>'}
    <h3>Agent context</h3>
    {render_markdown(section(prd, "Agent Context Contract"))[0] if section(prd, "Agent Context Contract") else '<p class="empty">None recorded.</p>'}
    <h3>Bead proposals</h3>
    {table_preview(section(prd, "Bead Proposals"), max_rows=6)}
  </section>
  <div class="layout">
    <article>
      {prd.content_html}
    </article>
    <nav class="toc" aria-label="Page contents">
      <strong>Contents</strong>
      {toc}
    </nav>
  </div>
</main>
"""
    return page_shell(prd.title, body)


def render_all(output: Path) -> list[Path]:
    prds = load_prds()
    output.mkdir(parents=True, exist_ok=True)
    for old_html in output.glob("*.html"):
        old_html.unlink()

    written: list[Path] = []
    index_path = output / "index.html"
    write_text(index_path, render_index(prds))
    written.append(index_path)
    for prd in prds:
        path = output / prd.html_name
        write_text(path, render_prd_page(prd))
        written.append(path)
    return written


def compare_dirs(expected: Path, actual: Path) -> list[str]:
    failures: list[str] = []
    expected_files = sorted(path.relative_to(expected) for path in expected.glob("*.html"))
    actual_files = sorted(path.relative_to(actual) for path in actual.glob("*.html"))
    if expected_files != actual_files:
        failures.append(
            "file set mismatch: expected "
            + ", ".join(str(path) for path in expected_files)
            + "; found "
            + ", ".join(str(path) for path in actual_files)
        )
        return failures
    for relative in expected_files:
        expected_text = read_text(expected / relative)
        actual_text = read_text(actual / relative)
        if expected_text != actual_text:
            failures.append(f"stale generated HTML: {relative}")
    return failures


def check_output() -> int:
    with tempfile.TemporaryDirectory(prefix="precode-prd-html-") as tmp:
        tmp_output = Path(tmp) / "prds-html"
        render_all(tmp_output)
        if not OUTPUT.is_dir():
            print(f"prd-html: missing output directory {OUTPUT.relative_to(ROOT)}")
            return 1
        failures = compare_dirs(tmp_output, OUTPUT)
    if failures:
        print("prd-html: check failed")
        for failure in failures:
            print(f"- {failure}")
        return 1
    print("prd-html: check passed")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate the static PRD HTML review surface.")
    parser.add_argument("--check", action="store_true", help="check committed PRD HTML output without writing it")
    parser.add_argument("--output", default=str(OUTPUT), help="output HTML directory")
    args = parser.parse_args()

    output = Path(args.output)
    if not output.is_absolute():
        output = ROOT / output

    if args.check:
        if output != OUTPUT:
            with tempfile.TemporaryDirectory(prefix="precode-prd-html-check-") as tmp:
                expected = Path(tmp) / "expected"
                render_all(expected)
                failures = compare_dirs(expected, output)
            if failures:
                print("prd-html: check failed")
                for failure in failures:
                    print(f"- {failure}")
                return 1
            print("prd-html: check passed")
            return 0
        return check_output()

    written = render_all(output)
    relative = output.relative_to(ROOT) if output.is_relative_to(ROOT) else output
    print(f"prd-html: wrote {len(written)} files to {relative}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
