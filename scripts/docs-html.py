#!/usr/bin/env python3
# Version: v0.1.4
# Last updated: 2026-06-23
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
        "summary": "Start here for orientation, daily operation, student guidance, setup, and the plain-English software-building path.",
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
        clean = plain_text(part)
        if clean:
            return clean[:230].rstrip()
    return ""


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
    return f'<div class="table-wrap"><table><thead><tr>{head}</tr></thead><tbody>{"".join(body_rows)}</tbody></table></div>'


def render_list(items: list[str], ordered: bool) -> str:
    tag = "ol" if ordered else "ul"
    rows = "".join(f"<li>{inline(item)}</li>" for item in items)
    return f"<{tag}>{rows}</{tag}>"


def render_blockquote(lines: list[str]) -> str:
    content = "\n".join(line.strip()[1:].strip() for line in lines)
    return f"<blockquote>{render_markdown(content, include_title=True)[0]}</blockquote>"


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
.compass-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 14px; margin-top: 18px; }
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
  .hero, .content { padding: 30px 18px; }
  .article { padding: 22px; }
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
    body = f"""
<section class="hero" id="top">
  <p class="eyebrow">PrecodeOS Doc</p>
  <h1>{h(doc.title)}</h1>
  <p class="lede">{h(doc.summary)}</p>
  <p class="meta"><a href="{h(source_href)}">Source Markdown</a><span>{h(doc.version)}</span><span>Updated {h(doc.last_updated)}</span></p>
</section>
<section class="content layout">
  <article class="article">
    {doc.content_html}
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
