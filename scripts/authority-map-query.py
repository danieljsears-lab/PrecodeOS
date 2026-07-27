#!/usr/bin/env python3
# Version: v0.1.0
# Last updated: 2026-07-27
# Owner: PrecodeOS
# Created by Dan Sears / Recode.
# SPDX-License-Identifier: Apache-2.0
from __future__ import annotations

import argparse
import json
from pathlib import Path
import tempfile
from typing import Any

from os_compiler import compile_authority_map, repo_root


TOOL = "authority-map-query"
BOUNDARY_WARNING = (
    "Authority Map Query output is read-only navigation evidence. It does not approve edits, "
    "select tasks, approve commands, replace owner files, approve PRDs, activate beads, enforce runtime behavior, "
    "expose private maintainer inventory, or create registry, optional-pack, install/update, release-channel, "
    "or package-manager behavior."
)
FORBIDDEN_USES = [
    "task selection",
    "command approval",
    "owner-file replacement",
    "PRD approval",
    "bead activation",
    "transition approval",
    "implementation acceptance",
    "runtime enforcement",
    "private maintainer inventory",
    "generated-output authority",
    "registry behavior",
    "optional-pack behavior",
    "install/update behavior",
    "release-channel behavior",
    "package-manager behavior",
]
SEARCH_FIELDS = ("path", "title", "surface", "surface_class", "class", "authority", "not_authority", "load_when")


def normalize(value: str) -> str:
    return " ".join(value.lower().split())


def doc_matches(doc: dict[str, Any], terms: list[str]) -> bool:
    haystack = normalize(" ".join(str(doc.get(field) or "") for field in SEARCH_FIELDS))
    return all(term in haystack for term in terms)


def query_docs(
    authority_map: dict[str, Any],
    *,
    query: str = "",
    path: str = "",
    surface_class: str = "",
    limit: int = 10,
) -> list[dict[str, Any]]:
    docs = [doc for doc in authority_map.get("docs", []) if isinstance(doc, dict)]
    if path:
        docs = [doc for doc in docs if str(doc.get("path") or "") == path]
    if surface_class:
        docs = [doc for doc in docs if str(doc.get("surface_class") or "") == surface_class]
    terms = [normalize(part) for part in query.split() if normalize(part)]
    if terms:
        docs = [doc for doc in docs if doc_matches(doc, terms)]
    return docs[:limit]


def build_payload(
    root: Path,
    *,
    query: str = "",
    path: str = "",
    surface_class: str = "",
    list_surface_classes: bool = False,
    limit: int = 10,
) -> dict[str, Any]:
    authority_map = compile_authority_map(root)
    matches = query_docs(authority_map, query=query, path=path, surface_class=surface_class, limit=limit)
    surface_classes = authority_map.get("surface_classes") if list_surface_classes else None
    payload: dict[str, Any] = {
        "tool": TOOL,
        "query": query,
        "path": path,
        "surface_class": surface_class,
        "match_count": len(matches),
        "matches": matches,
        "boundary_warning": BOUNDARY_WARNING,
        "forbidden_uses": FORBIDDEN_USES,
    }
    if surface_classes is not None:
        payload["surface_classes"] = surface_classes
    return payload


def render_text(payload: dict[str, Any]) -> str:
    lines = [BOUNDARY_WARNING]
    surface_classes = payload.get("surface_classes")
    if isinstance(surface_classes, dict):
        lines.append("")
        lines.append("Surface classes:")
        for name, metadata in sorted(surface_classes.items()):
            if not isinstance(metadata, dict):
                continue
            count = metadata.get("parsed_authority_contract_count", 0)
            label = metadata.get("label") or name
            lines.append(f"- {name}: {label} ({count} parsed authority contracts)")
            lines.append(f"  Authority: {metadata.get('authority') or 'not recorded'}")
            lines.append(f"  Not authority: {metadata.get('not_authority') or 'not recorded'}")

    matches = payload.get("matches") if isinstance(payload.get("matches"), list) else []
    lines.append("")
    lines.append(f"Matches: {payload.get('match_count', 0)}")
    for index, match in enumerate(matches, 1):
        if not isinstance(match, dict):
            continue
        lines.append("")
        lines.append(f"{index}. {match.get('path') or 'unknown path'}")
        lines.append(f"   Title: {match.get('title') or 'not recorded'}")
        lines.append(f"   Surface class: {match.get('surface_class') or 'not recorded'}")
        lines.append(f"   Authority: {match.get('authority') or 'not recorded'}")
        lines.append(f"   Not authority: {match.get('not_authority') or 'not recorded'}")
        lines.append(f"   Load when: {match.get('load_when') or 'not recorded'}")
    return "\n".join(lines)


def write_fixture(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def self_test() -> int:
    failures: list[dict[str, str]] = []
    with tempfile.TemporaryDirectory(prefix="precode-authority-map-query-") as tmp:
        root = Path(tmp)
        write_fixture(
            root / "AGENT.md",
            "# Agent\n"
            "<!-- ANCHOR: agent -->\n\n"
            "> AUTHORITY: Active memory fixture.\n"
            "> NOT_AUTHORITY: Task selection or PRD approval.\n"
            "> LOAD_WHEN: Start of every fixture session.\n"
            "> CLASS: active-memory\n",
        )
        write_fixture(
            root / "tasks" / "prds" / "PRD-999-fixture.md",
            "# PRD-999 -- Fixture\n"
            "<!-- ANCHOR: prd-999-fixture -->\n\n"
            "> AUTHORITY: Fixture PRD approval requirements.\n"
            "> NOT_AUTHORITY: Command approval or runtime enforcement.\n"
            "> LOAD_WHEN: Testing PRD lookup.\n"
            "> CLASS: reference\n",
        )
        write_fixture(
            root / "_maintainer" / "PRIVATE.md",
            "# Private\n"
            "<!-- ANCHOR: private -->\n\n"
            "> AUTHORITY: Private maintainer fixture.\n"
            "> NOT_AUTHORITY: Public package authority.\n"
            "> LOAD_WHEN: Never in public package tooling.\n"
            "> CLASS: private-reference\n",
        )
        query_payload = build_payload(root, query="Fixture requirements")
        if query_payload["match_count"] != 1:
            failures.append({"scenario": "query match count", "expected": "1", "actual": str(query_payload["match_count"])})
        match_paths = [match.get("path") for match in query_payload["matches"]]
        if "tasks/prds/PRD-999-fixture.md" not in match_paths:
            failures.append({"scenario": "query path", "expected": "tasks/prds/PRD-999-fixture.md", "actual": str(match_paths)})
        path_payload = build_payload(root, path="AGENT.md")
        if path_payload["match_count"] != 1:
            failures.append({"scenario": "path lookup", "expected": "1", "actual": str(path_payload["match_count"])})
        surface_payload = build_payload(root, surface_class="active-memory")
        if surface_payload["match_count"] != 1:
            failures.append({"scenario": "surface lookup", "expected": "1", "actual": str(surface_payload["match_count"])})
        classes_payload = build_payload(root, list_surface_classes=True)
        if "surface_classes" not in classes_payload:
            failures.append({"scenario": "surface classes", "expected": "surface_classes", "actual": "missing"})
        private_payload = build_payload(root, query="Private maintainer")
        if private_payload["match_count"] != 0:
            failures.append({"scenario": "private exclusion", "expected": "0", "actual": str(private_payload["match_count"])})
        if not any("command approval" in item for item in query_payload.get("forbidden_uses", [])):
            failures.append({"scenario": "forbidden uses", "expected": "command approval", "actual": str(query_payload.get("forbidden_uses"))})

    payload = {
        "tool": TOOL,
        "mode": "self-test",
        "status": "pass" if not failures else "fail",
        "scenario_count": 6,
        "failures": failures,
        "boundary_warning": BOUNDARY_WARNING,
        "forbidden_uses": FORBIDDEN_USES,
    }
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0 if not failures else 1


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Query PrecodeOS authority-map contracts for navigation only; output is not approval or authority.",
    )
    parser.add_argument("terms", nargs="*", help="query terms")
    parser.add_argument("--query", help="query text")
    parser.add_argument("--path", default="", help="exact public package path to look up")
    parser.add_argument("--surface-class", default="", help="filter by authority-map surface class")
    parser.add_argument("--list-surface-classes", action="store_true", help="include authority-map surface-class summaries")
    parser.add_argument("--limit", type=int, default=10, help="maximum matches to return")
    parser.add_argument("--json", action="store_true", help="print JSON output")
    parser.add_argument("--self-test", action="store_true", help="run deterministic authority-map query fixture checks")
    args = parser.parse_args(argv)
    if args.limit < 1:
        parser.error("--limit must be at least 1")
    if args.query and args.terms:
        parser.error("use either positional query terms or --query, not both")
    return args


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    if args.self_test:
        return self_test()
    query = args.query if args.query is not None else " ".join(args.terms)
    payload = build_payload(
        repo_root(),
        query=query,
        path=args.path,
        surface_class=args.surface_class,
        list_surface_classes=args.list_surface_classes,
        limit=args.limit,
    )
    if args.json:
        print(json.dumps(payload, indent=2, sort_keys=True))
    else:
        print(render_text(payload))
    if payload.get("match_count", 0) == 0 and not args.list_surface_classes:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
