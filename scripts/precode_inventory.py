#!/usr/bin/env python3
# Version: v0.1.1
# Last updated: 2026-07-26
# Owner: PrecodeOS
# Created by Dan Sears / Recode.
# SPDX-License-Identifier: Apache-2.0
from __future__ import annotations

from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
import re
from typing import Any

from os_parser import (
    MarkdownDocument,
    bullet_items,
    extract_anchor,
    extract_contract_values,
    read_text,
    strip_inline_code,
)
from precode_state import heading_title, rel_path

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
AUTHORITY_SURFACE_CLASSES: dict[str, dict[str, Any]] = {
    "active-memory": {
        "label": "Active memory",
        "patterns": ACTIVE_MEMORY,
        "authority": "Always-loaded operating state for a Precode session.",
        "not_authority": "Does not replace owner files, PRDs, beads, generated evidence review, or human approval.",
        "generated": False,
        "public_package": True,
    },
    "owner-reference-doc": {
        "label": "Owner and reference docs",
        "patterns": ["*.md", "docs/*.md"],
        "authority": "Durable package, product, architecture, policy, and user-facing reference meaning.",
        "not_authority": "Does not activate work, approve transitions, or make generated evidence true.",
        "generated": False,
        "public_package": True,
    },
    "protocol": {
        "label": "Protocols",
        "patterns": ["tasks/reference/*.md"],
        "authority": "Repeatable workflow rules and extension boundaries outside active memory.",
        "not_authority": "Does not select tasks, approve PRDs, activate beads, or override owner files.",
        "generated": False,
        "public_package": True,
    },
    "prd": {
        "label": "PRDs",
        "patterns": ["tasks/prds/*.md"],
        "authority": "Approved destination shards and requirement-level intent.",
        "not_authority": "Does not activate implementation by itself or prove completion.",
        "generated": False,
        "public_package": True,
    },
    "bead": {
        "label": "Beads",
        "patterns": ["tasks/beads/*.md"],
        "authority": "Executable journey units when approved and pointed to by active task state.",
        "not_authority": "Does not supersede PRDs, owner files, active memory, or human acceptance.",
        "generated": False,
        "public_package": True,
    },
    "template": {
        "label": "Templates",
        "patterns": ["tasks/templates/*.md"],
        "authority": "Copyable artifact shapes for source evidence, proposals, and completion evidence.",
        "not_authority": "Does not approve product decisions, bead activation, acceptance, or implementation.",
        "generated": False,
        "public_package": True,
    },
    "adapter": {
        "label": "Adapters",
        "patterns": ["adapters/*.md"],
        "authority": "Tool-specific compatibility guidance pointing back to the shared operating model.",
        "not_authority": "Does not become an alternate Precode system or expand active memory.",
        "generated": False,
        "public_package": True,
    },
    "shim": {
        "label": "Shims",
        "patterns": SHIM_DOCS,
        "authority": "Compatibility pointers for tools that auto-load a conventional instruction file.",
        "not_authority": "Does not replace AGENT.md, active memory, PRDs, owner files, or implementation status.",
        "generated": False,
        "public_package": True,
    },
    "mode": {
        "label": "Mode contracts",
        "patterns": ["modes/*.md"],
        "authority": "Compact role contracts for bounded agent behavior.",
        "not_authority": "Does not choose tasks, approve transitions, or override active memory.",
        "generated": False,
        "public_package": True,
    },
    "log-reference": {
        "label": "Log reference docs",
        "patterns": ["logs/LOG-EVIDENCE-TAXONOMY.md"],
        "authority": "Public reference guidance for generated evidence families.",
        "not_authority": "Does not make generated logs authoritative or sufficient proof by itself.",
        "generated": False,
        "public_package": True,
    },
    "generated-public-html": {
        "label": "Generated public HTML",
        "patterns": ["docs-html/*.html", "tasks/prds-html/*.html"],
        "authority": "Committed reading and review surfaces generated from canonical Markdown.",
        "not_authority": "Does not replace source Markdown, approve PRDs, activate beads, or persist exported edits.",
        "generated": True,
        "public_package": True,
    },
    "generated-report": {
        "label": "Generated reports and sidecars",
        "patterns": ["OS-HEALTH.md", "PRECODE-HELP.md", "PROGRESS.md", "logs/*.json", "logs/*.jsonl", "logs/*.md", "logs/*.yaml"],
        "authority": "Evidence and inspection output compiled from source files and recorded activity.",
        "not_authority": "Does not select tasks, approve work, rewrite owner files, or become proof without review.",
        "generated": True,
        "public_package": True,
    },
    "script": {
        "label": "Scripts",
        "patterns": ["scripts/*.py", "scripts/*.sh"],
        "authority": "Repo-local validation, compilation, routing, audit, and evidence generation behavior.",
        "not_authority": "Does not approve user decisions, hide mutation, or become package-manager behavior.",
        "generated": False,
        "public_package": True,
    },
    "workflow": {
        "label": "Workflows",
        "patterns": [".github/workflows/*.yml", ".github/PULL_REQUEST_TEMPLATE.md"],
        "authority": "Repository validation automation and pull-request evidence prompts.",
        "not_authority": "Does not merge, release, approve roadmap direction, or replace maintainer review.",
        "generated": False,
        "public_package": True,
    },
    "maintainer-private": {
        "label": "Maintainer-private surfaces",
        "patterns": ["_maintainer/**"],
        "authority": "Private local maintainer planning, roadmap, history, and review material.",
        "not_authority": "Not public package authority, active memory, generated proof, task selection, or user workflow guidance.",
        "generated": False,
        "public_package": False,
    },
}
GENERATED_JSON_FAMILIES = {
    "logs/*.json",
    "logs/*.jsonl",
    "logs/check-output/*",
    "logs/scheduled-audit-output/*",
    "logs/os-checkpoints/*",
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


def authority_surface_class(rel: str) -> str:
    if rel in ACTIVE_MEMORY:
        return "active-memory"
    if rel in SHIM_DOCS:
        return "shim"
    if rel.startswith("adapters/"):
        return "adapter"
    if rel.startswith("tasks/reference/"):
        return "protocol"
    if rel.startswith("tasks/prds/"):
        return "prd"
    if rel.startswith("tasks/beads/"):
        return "bead"
    if rel.startswith("tasks/templates/"):
        return "template"
    if rel.startswith("modes/"):
        return "mode"
    if rel == "logs/LOG-EVIDENCE-TAXONOMY.md":
        return "log-reference"
    return "owner-reference-doc"


def authority_surface_class_summary(docs: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    grouped_paths: dict[str, list[str]] = {name: [] for name in AUTHORITY_SURFACE_CLASSES}
    for item in docs:
        surface_class = str(item.get("surface_class", "owner-reference-doc"))
        grouped_paths.setdefault(surface_class, []).append(str(item.get("path", "")))

    summary: dict[str, dict[str, Any]] = {}
    for name, metadata in AUTHORITY_SURFACE_CLASSES.items():
        paths = sorted(path for path in grouped_paths.get(name, []) if path)
        summary[name] = {
            **metadata,
            "parsed_authority_contract_count": len(paths),
            "paths": paths,
        }
    return summary


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
                "surface_class": authority_surface_class(rel),
                "authority": contract.get("authority"),
                "not_authority": contract.get("not_authority"),
                "load_when": contract.get("load_when"),
            }
        )

    return {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "active_memory": ACTIVE_MEMORY,
        "generated_is_not_authority": True,
        "private_maintainer_surfaces_excluded": True,
        "surface_classes": authority_surface_class_summary(docs),
        "docs_by_surface": {
            surface_class: [item for item in docs if item.get("surface_class") == surface_class]
            for surface_class in sorted({str(item.get("surface_class", "owner-reference-doc")) for item in docs})
        },
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


def prd_html_paths(root: Path) -> list[Path]:
    base = root / "tasks" / "prds-html"
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
        ("tasks/prds-html/", "`tasks/prds-html/*.html`"),
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

    prd_html: list[dict[str, Any]] = []
    for path in prd_html_paths(root):
        rel = rel_path(path, root)
        if package_inventory_text and not inventory_family_covered(rel, package_inventory_text):
            warnings.append(f"{rel} is not referenced in {package_inventory_rel}")
        prd_html.append({"path": rel, "family": "generated-prd-html", "bytes": file_size(path)})

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
        for item in [*docs, *scripts, *workflows, *docs_html, *prd_html, *generated]
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
            "prd_html": len(prd_html),
            "generated_outputs": len(generated),
            "families": dict(sorted(family_counts.items())),
        },
        "docs": docs,
        "scripts": scripts,
        "workflows": workflows,
        "docs_html": docs_html,
        "prd_html": prd_html,
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

