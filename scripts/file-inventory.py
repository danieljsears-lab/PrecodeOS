#!/usr/bin/env python3
# Version: v0.2.0
# Last updated: 2026-07-26
# Owner: PrecodeOS
# Created by Dan Sears / Recode.
# SPDX-License-Identifier: Apache-2.0
from __future__ import annotations

import argparse
import json
from pathlib import Path
import tempfile

from os_compiler import compile_file_inventory, repo_root, write_json


def check_payload(payload: dict) -> dict:
    warnings = payload.get("warnings") if isinstance(payload.get("warnings"), list) else []
    return {
        "tool": "file-inventory",
        **payload,
        "status": "pass" if not warnings else "fail",
        "enforced": True,
    }


def exit_code(payload: dict) -> int:
    return 0 if payload.get("status") == "pass" else 1


def write_fixture(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def write_inventory_fixture(root: Path) -> None:
    write_fixture(
        root / "docs" / "PRECODE-PACKAGE-FILE-INVENTORY.md",
        "# Inventory\n"
        "<!-- ANCHOR: package-file-inventory -->\n\n"
        "> AUTHORITY: Fixture inventory.\n"
        "> NOT_AUTHORITY: Fixture only.\n"
        "> LOAD_WHEN: Testing inventory enforcement.\n"
        "> CLASS: reference\n\n"
        "Creator: Dan Sears / Recode\n"
        "Document version: v0.1.0\n"
        "Last updated: 2026-07-26\n\n"
        "`docs/PRECODE-PACKAGE-FILE-INVENTORY.md`\n"
        "`scripts/*.py`\n"
        "`docs-html/*.html`\n"
        "`tasks/prds-html/*.html`\n",
    )


def self_test() -> int:
    failures: list[dict[str, str]] = []
    with tempfile.TemporaryDirectory(prefix="precode-file-inventory-") as tmp:
        clean = Path(tmp) / "clean"
        write_inventory_fixture(clean)
        write_fixture(
            clean / "scripts" / "good.py",
            "#!/usr/bin/env python3\n"
            "# Version: v0.1.0\n"
            "# Last updated: 2026-07-26\n"
            "# Owner: PrecodeOS\n",
        )
        write_fixture(clean / "docs-html" / "index.html", "<html></html>\n")
        write_fixture(clean / "tasks" / "prds-html" / "PRD-999.html", "<html></html>\n")
        clean_payload = check_payload(compile_file_inventory(clean))
        if exit_code(clean_payload) != 0:
            failures.append({"scenario": "clean fixture exit", "expected": "0", "actual": str(clean_payload.get("warnings"))})

        drift = Path(tmp) / "drift"
        write_inventory_fixture(drift)
        write_fixture(drift / "docs" / "UNVERSIONED.md", "# Missing Contract\n")
        drift_payload = check_payload(compile_file_inventory(drift))
        if exit_code(drift_payload) == 0:
            failures.append({"scenario": "drift fixture exit", "expected": "nonzero", "actual": "0"})
        if not drift_payload.get("warnings"):
            failures.append({"scenario": "drift fixture warnings", "expected": "inventory warnings", "actual": "none"})

    payload = {
        "tool": "file-inventory",
        "mode": "self-test",
        "status": "pass" if not failures else "fail",
        "scenario_count": 2,
        "failures": failures,
    }
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0 if not failures else 1


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="enforce public package inventory warnings without writing generated output")
    parser.add_argument("--self-test", action="store_true", help="run deterministic file-inventory enforcement fixtures")
    args = parser.parse_args()
    if args.self_test:
        return self_test()

    root = repo_root()
    payload = compile_file_inventory(root)
    if args.check:
        checked = check_payload(payload)
        print(json.dumps(checked, indent=2, sort_keys=True))
        return exit_code(checked)

    write_json(root / "logs" / "file-inventory.json", payload)
    print("file-inventory: wrote logs/file-inventory.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
