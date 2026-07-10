#!/usr/bin/env python3
# Version: v0.1.0
# Last updated: 2026-07-10
# Owner: PrecodeOS
# Created by Dan Sears / Recode.
# SPDX-License-Identifier: Apache-2.0
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from dataclasses import dataclass
import json
from pathlib import Path, PurePosixPath
import re
import tempfile
from typing import Any

from os_compiler import repo_root
from precode_outputs import write_json


TOOL = "package-knowledge-lint"
GENERATED_WARNING = (
    "Package Knowledge Lint output is advisory generated evidence only. It does not approve edits, "
    "select tasks, promote sources, rewrite docs, declare stale claims authoritative, create proof, "
    "accept implementation, create a checker gate, or create registry, optional-pack, install/update, "
    "release-channel, or package-manager behavior."
)
PUBLIC_FINDING_TERMS = (
    "broken internal links or anchors; duplicate heading labels; orphan public references; "
    "stale generated sidecar cues; duplicate authority claims; public/private boundary risk"
)
FORBIDDEN_USES = [
    "edit approval",
    "task selection",
    "source promotion approval",
    "automatic doc rewrite",
    "stale-claim authority",
    "generated proof",
    "implementation acceptance",
    "checker gate",
    "registry behavior",
    "optional-pack behavior",
    "install/update behavior",
    "package-manager behavior",
]
SOURCE_GLOBS = [
    "README.md",
    "llms.txt",
    "docs/*.md",
    "tasks/reference/*.md",
    "adapters/*.md",
    "AGENTS.md",
    "CLAUDE.md",
    "GEMINI.md",
    ".github/copilot-instructions.md",
    "scripts/*.py",
    "scripts/*.sh",
    "logs/authority-map.json",
    "logs/file-inventory.json",
]
ORPHAN_PREFIXES = ("docs/", "tasks/reference/", "adapters/")
LINK_PATTERN = re.compile(r"(?<!!)\[[^\]]+\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
HEADING_PATTERN = re.compile(r"^(#{1,6})\s+(.+?)\s*#*\s*$", re.MULTILINE)
HTML_ANCHOR_PATTERN = re.compile(r"<a\s+[^>]*id=[\"']([^\"']+)[\"']", re.IGNORECASE)
COMMENT_ANCHOR_PATTERN = re.compile(r"<!--\s*ANCHOR:\s*([a-zA-Z0-9_.:-]+)\s*-->")
CONTRACT_PATTERN = re.compile(r"^>\s*AUTHORITY:\s*(.+)$", re.MULTILINE)


@dataclass(frozen=True)
class SourceFile:
    rel_path: str
    path: Path
    text: str


def rel(path: Path, root: Path) -> str:
    return path.relative_to(root).as_posix()


def is_public_source(rel_path: str) -> bool:
    return not rel_path.startswith("_maintainer/")


def is_doc_like(rel_path: str) -> bool:
    return rel_path.endswith(".md") or rel_path == "llms.txt"


def is_public_doc_or_sidecar(rel_path: str) -> bool:
    return is_doc_like(rel_path) or rel_path in {"logs/authority-map.json", "logs/file-inventory.json"}


def source_files(root: Path) -> list[SourceFile]:
    seen: set[str] = set()
    files: list[SourceFile] = []
    for pattern in SOURCE_GLOBS:
        for path in sorted(root.glob(pattern)):
            if not path.is_file():
                continue
            name = rel(path, root)
            if name in seen or not is_public_source(name):
                continue
            try:
                text = path.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                continue
            seen.add(name)
            files.append(SourceFile(name, path, text))
    return files


def normalize_label(value: str) -> str:
    value = re.sub(r"`([^`]+)`", r"\1", value)
    value = re.sub(r"<[^>]+>", "", value)
    value = value.lower()
    value = re.sub(r"[^a-z0-9]+", " ", value)
    return " ".join(value.split())


def slugify(value: str) -> str:
    value = re.sub(r"`([^`]+)`", r"\1", value)
    value = re.sub(r"<[^>]+>", "", value).strip().lower()
    value = re.sub(r"[^a-z0-9 _-]+", "", value)
    value = re.sub(r"\s+", "-", value)
    return value.strip("-")


def anchors_for(text: str) -> set[str]:
    anchors = set(HTML_ANCHOR_PATTERN.findall(text))
    anchors.update(COMMENT_ANCHOR_PATTERN.findall(text))
    slug_counts: Counter[str] = Counter()
    for _, heading in HEADING_PATTERN.findall(text):
        slug = slugify(heading)
        if not slug:
            continue
        slug_counts[slug] += 1
        anchors.add(slug if slug_counts[slug] == 1 else f"{slug}-{slug_counts[slug] - 1}")
    return anchors


def split_link(raw_target: str) -> tuple[str, str]:
    target = raw_target.strip()
    if target.startswith("<") and target.endswith(">"):
        target = target[1:-1]
    if "#" not in target:
        return target, ""
    path, anchor = target.split("#", 1)
    return path, anchor


def normalize_target(source_rel: str, target: str) -> str:
    source_dir = PurePosixPath(source_rel).parent
    if target.startswith("/"):
        target_path = PurePosixPath(target.lstrip("/"))
    else:
        target_path = source_dir / target
    parts: list[str] = []
    for part in target_path.parts:
        if part in {"", "."}:
            continue
        if part == "..":
            if parts:
                parts.pop()
            continue
        parts.append(part)
    return PurePosixPath(*parts).as_posix() if parts else ""


def is_external_target(target: str) -> bool:
    lowered = target.lower()
    return (
        not target
        or lowered.startswith(("http://", "https://", "mailto:", "tel:"))
        or lowered.startswith("app://")
    )


def add_finding(
    findings: list[dict[str, Any]],
    *,
    category: str,
    severity: str,
    source_refs: list[str],
    message: str,
    recommended_destination: str,
    promotion_path: str,
) -> None:
    findings.append(
        {
            "id": f"PKL-{len(findings) + 1:03d}",
            "category": category,
            "severity": severity,
            "source_refs": source_refs,
            "message": message,
            "recommended_destination": recommended_destination,
            "promotion_path": promotion_path,
            "forbidden_uses": FORBIDDEN_USES,
        }
    )


def link_findings(root: Path, sources: list[SourceFile], findings: list[dict[str, Any]]) -> dict[str, set[str]]:
    anchors_by_path = {source.rel_path: anchors_for(source.text) for source in sources}
    inbound: dict[str, set[str]] = defaultdict(set)
    existing_source_paths = {source.rel_path for source in sources}
    for source in sources:
        if not is_doc_like(source.rel_path):
            continue
        for raw_target in LINK_PATTERN.findall(source.text):
            target, anchor = split_link(raw_target)
            if is_external_target(target):
                continue
            target_rel = source.rel_path if target == "" else normalize_target(source.rel_path, target)
            if target_rel:
                inbound[target_rel].add(source.rel_path)
            if target_rel.startswith("_maintainer/"):
                add_finding(
                    findings,
                    category="public_private_boundary_risk",
                    severity="warning",
                    source_refs=[source.rel_path],
                    message=f"Public source links to maintainer-local material: {raw_target}",
                    recommended_destination="docs/PRECODE-PACKAGE-FILE-INVENTORY.md or tasks/reference/EXTENSION-PROTOCOL.md",
                    promotion_path="Review whether the public source should name a public owner file instead of maintainer-local context.",
                )
                continue
            if target_rel and not (root / target_rel).exists():
                add_finding(
                    findings,
                    category="broken_internal_link",
                    severity="warning",
                    source_refs=[source.rel_path],
                    message=f"Internal link target is missing: {raw_target}",
                    recommended_destination=source.rel_path,
                    promotion_path="Repair the source Markdown link or route the stale reference through Cross-Reference / Staleness Review.",
                )
            elif anchor:
                target_anchors = anchors_by_path.get(target_rel)
                if target_rel not in existing_source_paths and (root / target_rel).is_file():
                    try:
                        target_anchors = anchors_for((root / target_rel).read_text(encoding="utf-8"))
                    except UnicodeDecodeError:
                        target_anchors = set()
                if target_anchors is not None and anchor not in target_anchors:
                    add_finding(
                        findings,
                        category="broken_internal_anchor",
                        severity="warning",
                        source_refs=[source.rel_path, target_rel],
                        message=f"Internal link anchor is missing: {raw_target}",
                        recommended_destination=source.rel_path,
                        promotion_path="Repair the anchor or source link after checking the canonical Markdown target.",
                    )
    return inbound


def heading_findings(sources: list[SourceFile], findings: list[dict[str, Any]]) -> None:
    headings: dict[str, list[str]] = defaultdict(list)
    for source in sources:
        if not is_doc_like(source.rel_path):
            continue
        for _, heading in HEADING_PATTERN.findall(source.text):
            normalized = normalize_label(heading)
            if normalized:
                headings[normalized].append(source.rel_path)
    for normalized, paths in sorted(headings.items()):
        unique_paths = sorted(set(paths))
        if len(unique_paths) < 2:
            continue
        if normalized in {"purpose", "stop conditions", "promotion path", "document metadata"}:
            continue
        add_finding(
            findings,
            category="duplicate_heading_label",
            severity="info",
            source_refs=unique_paths[:8],
            message=f"Repeated heading label may represent duplicate concept surface: {normalized}",
            recommended_destination="tasks/reference/REVIEW-LANES-PROTOCOL.md",
            promotion_path="Use Cross-Reference / Staleness Review before deciding whether any owner file needs consolidation.",
        )


def orphan_findings(sources: list[SourceFile], inbound: dict[str, set[str]], findings: list[dict[str, Any]]) -> None:
    for source in sources:
        if not is_doc_like(source.rel_path) or not source.rel_path.startswith(ORPHAN_PREFIXES):
            continue
        if source.rel_path in {"docs/PRECODE-PACKAGE-FILE-INVENTORY.md", "tasks/reference/PROMPT-PATTERNS.md"}:
            continue
        incoming = inbound.get(source.rel_path, set()) - {source.rel_path}
        if not incoming:
            add_finding(
                findings,
                category="orphan_public_reference",
                severity="info",
                source_refs=[source.rel_path],
                message="Public reference surface has no inbound Markdown links from the checked public core source set.",
                recommended_destination="docs/PRECODE-PACKAGE-FILE-INVENTORY.md or llms.txt",
                promotion_path="Review whether the surface needs navigation, inventory coverage, or should remain intentionally discoverable only by direct protocol trigger.",
            )


def authority_findings(sources: list[SourceFile], findings: list[dict[str, Any]]) -> None:
    claims: dict[str, list[str]] = defaultdict(list)
    for source in sources:
        if not is_doc_like(source.rel_path):
            continue
        match = CONTRACT_PATTERN.search(source.text)
        if match:
            normalized = normalize_label(match.group(1))
            if normalized:
                claims[normalized].append(source.rel_path)
    for claim, paths in sorted(claims.items()):
        unique_paths = sorted(set(paths))
        if len(unique_paths) > 1:
            add_finding(
                findings,
                category="duplicate_authority_claim",
                severity="warning",
                source_refs=unique_paths,
                message=f"Multiple files share the same normalized AUTHORITY claim: {claim}",
                recommended_destination="docs/PRECODE-PACKAGE-FILE-INVENTORY.md",
                promotion_path="Review authority ownership before treating either surface as canonical for the same domain.",
            )


def sidecar_findings(root: Path, sources: list[SourceFile], findings: list[dict[str, Any]]) -> None:
    source_paths = [source.path for source in sources if not source.rel_path.startswith("logs/")]
    for rel_sidecar in ("logs/authority-map.json", "logs/file-inventory.json"):
        sidecar = root / rel_sidecar
        if not sidecar.is_file():
            add_finding(
                findings,
                category="missing_generated_sidecar",
                severity="warning",
                source_refs=[rel_sidecar],
                message=f"Expected generated sidecar is missing: {rel_sidecar}",
                recommended_destination=rel_sidecar,
                promotion_path="Regenerate the owning generated evidence command before relying on sidecar freshness.",
            )
            continue
        try:
            json.loads(sidecar.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            add_finding(
                findings,
                category="malformed_generated_sidecar",
                severity="warning",
                source_refs=[rel_sidecar],
                message=f"Generated sidecar is not valid JSON: {exc}",
                recommended_destination=rel_sidecar,
                promotion_path="Regenerate the owning generated evidence command; do not hand-edit generated JSON as authority.",
            )
        sidecar_mtime = sidecar.stat().st_mtime
        newer = [rel(path, root) for path in source_paths if path.stat().st_mtime > sidecar_mtime]
        if newer:
            add_finding(
                findings,
                category="possibly_stale_generated_sidecar",
                severity="info",
                source_refs=[rel_sidecar, *newer[:8]],
                message=f"{rel_sidecar} is older than {len(newer)} checked public source files.",
                recommended_destination=rel_sidecar,
                promotion_path="Run the owning generated-surface command and verify source Markdown remains authoritative.",
            )


def private_boundary_findings(sources: list[SourceFile], findings: list[dict[str, Any]]) -> None:
    for source in sources:
        if not is_public_doc_or_sidecar(source.rel_path):
            continue
        if "_maintainer/" not in source.text:
            continue
        add_finding(
            findings,
            category="public_private_boundary_risk",
            severity="info",
            source_refs=[source.rel_path],
            message="Public checked source mentions maintainer-local material; confirm the mention is boundary guidance, not a dependency.",
            recommended_destination="docs/PRECODE-PACKAGE-FILE-INVENTORY.md or tasks/reference/EXTENSION-PROTOCOL.md",
            promotion_path="If the public package depends on maintainer-local context, move the needed rule into a public owner file or remove the dependency.",
        )


def build_payload(root: Path) -> dict[str, Any]:
    sources = source_files(root)
    findings: list[dict[str, Any]] = []
    inbound = link_findings(root, sources, findings)
    heading_findings(sources, findings)
    orphan_findings(sources, inbound, findings)
    authority_findings(sources, findings)
    sidecar_findings(root, sources, findings)
    private_boundary_findings(sources, findings)
    category_counts = Counter(finding["category"] for finding in findings)
    severity_counts = Counter(finding["severity"] for finding in findings)
    return {
        "tool": TOOL,
        "status": "pass" if not findings else "warning",
        "generated_warning": GENERATED_WARNING,
        "source_scope": {
            "included": SOURCE_GLOBS,
            "excluded": ["_maintainer/", "private maintainer material", "untracked external systems"],
            "mode": "public_core",
        },
        "checked_files": [source.rel_path for source in sources],
        "summary": {
            "checked_file_count": len(sources),
            "finding_count": len(findings),
            "categories": dict(sorted(category_counts.items())),
            "severities": dict(sorted(severity_counts.items())),
        },
        "findings": findings,
    }


def write_fixture(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def self_test() -> dict[str, Any]:
    failures: list[dict[str, str]] = []
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        write_fixture(root / "README.md", "# Fixture\n\n[Broken](docs/MISSING.md)\n\n[Bad Anchor](docs/A.md#missing)\n")
        write_fixture(root / "llms.txt", "- `docs/A.md`: fixture\n")
        write_fixture(root / "docs" / "A.md", "# Shared Name\n\n> AUTHORITY: Duplicate fixture authority.\n> NOT_AUTHORITY: fixture\n> LOAD_WHEN: fixture\n> CLASS: reference\n\nSee [_maintainer](_maintainer/PRIVATE.md).\n")
        write_fixture(root / "docs" / "B.md", "# Shared Name\n\n> AUTHORITY: Duplicate fixture authority.\n> NOT_AUTHORITY: fixture\n> LOAD_WHEN: fixture\n> CLASS: reference\n")
        write_fixture(root / "tasks" / "reference" / "C.md", "# C\n")
        write_fixture(root / "adapters" / "ADAPTER-INDEX.md", "# Adapter Index\n")
        write_fixture(root / "AGENTS.md", "# Shim\n")
        write_fixture(root / "CLAUDE.md", "# Shim\n")
        write_fixture(root / "GEMINI.md", "# Shim\n")
        write_fixture(root / ".github" / "copilot-instructions.md", "# Copilot\n")
        write_fixture(root / "scripts" / "example.py", "#!/usr/bin/env python3\n")
        write_fixture(root / "scripts" / "example.sh", "#!/usr/bin/env bash\n")
        write_fixture(root / "logs" / "authority-map.json", "{}\n")
        write_fixture(root / "logs" / "file-inventory.json", "{}\n")
        payload = build_payload(root)

    categories = {finding["category"] for finding in payload["findings"]}
    expected_categories = {
        "broken_internal_link",
        "broken_internal_anchor",
        "duplicate_heading_label",
        "orphan_public_reference",
        "duplicate_authority_claim",
        "public_private_boundary_risk",
    }
    for category in expected_categories:
        if category not in categories:
            failures.append({"scenario": "fixture category coverage", "expected": category, "actual": str(sorted(categories))})
    if payload["status"] != "warning":
        failures.append({"scenario": "advisory finding status", "expected": "warning", "actual": str(payload["status"])})
    warning = payload.get("generated_warning") or ""
    for term in ["advisory generated evidence only", "does not approve edits", "select tasks", "rewrite docs", "package-manager behavior"]:
        if term not in warning:
            failures.append({"scenario": "generated warning wording", "expected": term, "actual": warning})
    for finding in payload["findings"]:
        for field in ["id", "category", "severity", "source_refs", "message", "recommended_destination", "promotion_path", "forbidden_uses"]:
            if field not in finding:
                failures.append({"scenario": f"finding field: {finding.get('category')}", "expected": field, "actual": "missing"})
        forbidden = " ".join(finding.get("forbidden_uses") or [])
        for term in ["task selection", "source promotion approval", "automatic doc rewrite", "checker gate"]:
            if term not in forbidden:
                failures.append({"scenario": f"forbidden use: {finding.get('category')}", "expected": term, "actual": forbidden})
    return {
        "tool": TOOL,
        "status": "pass" if not failures else "fail",
        "failures": failures,
        "fixture_findings": payload["summary"],
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="print advisory package-knowledge findings without writing generated output")
    parser.add_argument("--self-test", action="store_true", help="run package-knowledge lint fixture checks")
    args = parser.parse_args()

    if args.self_test:
        payload = self_test()
        print(json.dumps(payload, indent=2, sort_keys=True))
        return 0 if payload["status"] == "pass" else 1

    root = repo_root()
    payload = build_payload(root)
    if args.check:
        print(json.dumps(payload, indent=2, sort_keys=True))
        return 0

    write_json(root / "logs" / "package-knowledge-lint.json", payload)
    print("package-knowledge-lint: wrote logs/package-knowledge-lint.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
