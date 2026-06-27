#!/usr/bin/env python3
# Version: v0.1.0
# Last updated: 2026-06-27
# Owner: PrecodeOS
# Created by Dan Sears / Recode.
# SPDX-License-Identifier: Apache-2.0
"""Suggest the next monotonic PRD or bead ID without mutating source files."""

from __future__ import annotations

import argparse
import json
import re
import tempfile
from collections import defaultdict
from pathlib import Path
from typing import Any


CONFIG = {
    "prd": {
        "directory": Path("tasks/prds"),
        "pattern": "*.md",
        "skip_names": {"PRD-000-template.md", "PRD-SHARD-SCHEMA.md"},
        "field": "prd_id",
        "prefix": "PRD",
        "filename_pattern": re.compile(r"^(PRD-\d{3})-.+\.md$"),
    },
    "bead": {
        "directory": Path("tasks/beads"),
        "pattern": "*.md",
        "skip_names": {"BEAD-SCHEMA.md"},
        "field": "bead_id",
        "prefix": "B",
        "filename_pattern": re.compile(r"^(B\d{3})-.+\.md$"),
    },
}


def frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---", 4)
    if end == -1:
        return {}
    values: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if ":" in line and not line.startswith(" "):
            key, value = line.split(":", 1)
            values[key.strip()] = value.strip().strip("'\"")
    return values


def scan_ids(root: Path, kind: str) -> dict[str, Any]:
    config = CONFIG[kind]
    directory = root / config["directory"]
    field = str(config["field"])
    prefix = str(config["prefix"])
    id_pattern = re.compile(rf"^{re.escape(prefix)}-(\d{{3}})$" if prefix == "PRD" else r"^B(\d{3})$")

    entries: list[dict[str, str]] = []
    ids_by_value: dict[str, list[str]] = defaultdict(list)
    warnings: list[str] = []
    mismatches: list[dict[str, str]] = []
    numeric_ids: list[int] = []

    for item_path in sorted(directory.glob(str(config["pattern"]))):
        if item_path.name in config["skip_names"] or not item_path.is_file():
            continue
        rel_path = item_path.relative_to(root).as_posix()
        item_id = frontmatter(item_path.read_text(encoding="utf-8")).get(field, "").strip()
        if not item_id:
            warnings.append(f"{rel_path}: missing {field}")
            continue
        entries.append({"id": item_id, "path": rel_path})
        ids_by_value[item_id].append(rel_path)
        match = id_pattern.match(item_id)
        if match:
            numeric_ids.append(int(match.group(1)))
        else:
            warnings.append(f"{rel_path}: {field} has unexpected format {item_id}")
        filename_match = config["filename_pattern"].match(item_path.name)
        if filename_match and item_id != filename_match.group(1):
            mismatches.append(
                {
                    "path": rel_path,
                    "filename_id": filename_match.group(1),
                    "frontmatter_id": item_id,
                }
            )

    duplicates = {item_id: paths for item_id, paths in sorted(ids_by_value.items()) if len(paths) > 1}
    for item_id, paths in duplicates.items():
        warnings.append(f"duplicate {field} {item_id}: {', '.join(paths)}")
    for mismatch in mismatches:
        warnings.append(
            f"{mismatch['path']}: {field} {mismatch['frontmatter_id']} does not match filename ID {mismatch['filename_id']}"
        )

    max_number = max(numeric_ids, default=0)
    next_number = max_number + 1
    if prefix == "PRD":
        next_id = f"PRD-{next_number:03d}"
        max_existing_id = f"PRD-{max_number:03d}" if numeric_ids else None
    else:
        next_id = f"B{next_number:03d}"
        max_existing_id = f"B{max_number:03d}" if numeric_ids else None

    return {
        "kind": kind,
        "field": field,
        "prefix": prefix,
        "next_id": next_id,
        "max_existing_id": max_existing_id,
        "entries": entries,
        "duplicates": duplicates,
        "mismatches": mismatches,
        "warnings": warnings,
        "mutates": False,
        "reserves_id": False,
    }


def run_self_test() -> int:
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        (root / "tasks/prds").mkdir(parents=True)
        (root / "tasks/beads").mkdir(parents=True)
        (root / "tasks/prds/PRD-001-one.md").write_text("---\nprd_id: PRD-001\n---\n", encoding="utf-8")
        (root / "tasks/prds/PRD-003-three.md").write_text("---\nprd_id: PRD-003\n---\n", encoding="utf-8")
        (root / "tasks/prds/PRD-004-dup-a.md").write_text("---\nprd_id: PRD-004\n---\n", encoding="utf-8")
        (root / "tasks/prds/PRD-005-dup-b.md").write_text("---\nprd_id: PRD-004\n---\n", encoding="utf-8")
        (root / "tasks/prds/PRD-000-template.md").write_text("---\nprd_id: PRD-000\n---\n", encoding="utf-8")
        (root / "tasks/beads/B000-start.md").write_text("---\nbead_id: B000\n---\n", encoding="utf-8")
        (root / "tasks/beads/B002-two.md").write_text("---\nbead_id: B002\n---\n", encoding="utf-8")
        prd_result = scan_ids(root, "prd")
        bead_result = scan_ids(root, "bead")
    checks = [
        prd_result["next_id"] == "PRD-005",
        "PRD-004" in prd_result["duplicates"],
        bool(prd_result["warnings"]),
        bead_result["next_id"] == "B003",
        not bead_result["duplicates"],
        prd_result["mutates"] is False and bead_result["reserves_id"] is False,
    ]
    if all(checks):
        print("next-id self-test passed")
        return 0
    print("next-id self-test failed")
    print(json.dumps({"prd": prd_result, "bead": bead_result}, indent=2))
    return 1


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("kind", nargs="?", choices=sorted(CONFIG), help="ID family to inspect")
    parser.add_argument("--json", action="store_true", help="emit machine-readable JSON")
    parser.add_argument("--self-test", action="store_true", help="run built-in fixture tests")
    args = parser.parse_args()

    if args.self_test:
        return run_self_test()
    if not args.kind:
        parser.error("kind is required unless --self-test is used")
    result = scan_ids(Path.cwd(), args.kind)
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print(f"Next free {result['prefix']} ID: {result['next_id']}")
        if result["max_existing_id"]:
            print(f"Highest existing {result['prefix']} ID: {result['max_existing_id']}")
        if result["warnings"]:
            print("\nWarnings:")
            for warning in result["warnings"]:
                print(f"- {warning}")
        print("\nNo files were changed. This command suggests an ID only; it does not reserve or apply it.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
