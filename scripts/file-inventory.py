#!/usr/bin/env python3
# Version: v0.1.1
# Last updated: 2026-05-06
# Owner: PrecodeOS
# Created by Dan Sears / Recode.
# SPDX-License-Identifier: Apache-2.0
from __future__ import annotations

import argparse
import json

from os_compiler import compile_file_inventory, repo_root, write_json


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="print advisory inventory warnings without writing generated output")
    args = parser.parse_args()

    root = repo_root()
    payload = compile_file_inventory(root)
    if args.check:
        print(json.dumps({"tool": "file-inventory", **payload}, indent=2, sort_keys=True))
        return 0

    write_json(root / "logs" / "file-inventory.json", payload)
    print("file-inventory: wrote logs/file-inventory.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
