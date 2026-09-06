#!/usr/bin/env python3
# Version: v0.1.0
# Last updated: 2026-09-06
# Owner: PrecodeOS
# Created by Dan Sears / Recode.
# SPDX-License-Identifier: Apache-2.0
"""Verify the bounded v1 instruction and setup contract for certified adapters."""

from __future__ import annotations

import argparse
import json
import tempfile
from pathlib import Path
from typing import Any

from os_compiler import repo_root


CORE_FILES = ["AGENT.md", "DECISIONS.md", "tasks/todo.md"]
ADAPTERS = {
    "Codex": {"shim": "AGENTS.md", "adapter": "adapters/CODEX.md", "external_evidence": "pending"},
    "Claude Code": {"shim": "CLAUDE.md", "adapter": "adapters/CLAUDE.md", "external_evidence": "pending"},
    "Cursor": {"shim": "AGENTS.md", "adapter": "adapters/CURSOR.md", "external_evidence": "not_in_six_session_plan"},
    "Gemini": {"shim": "GEMINI.md", "adapter": "adapters/GEMINI.md", "external_evidence": "not_in_six_session_plan"},
}
SETUP_CONTRACT = "V1 Agent-Operated Setup Contract"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8") if path.is_file() else ""


def build_payload(root: Path) -> dict[str, Any]:
    failures: list[dict[str, str]] = []
    results: list[dict[str, Any]] = []
    index = read(root / "adapters/ADAPTER-INDEX.md")

    for name, contract in ADAPTERS.items():
        shim_path = root / contract["shim"]
        adapter_path = root / contract["adapter"]
        shim = read(shim_path)
        adapter = read(adapter_path)
        adapter_failures: list[str] = []
        if not shim:
            adapter_failures.append(f"missing shim {contract['shim']}")
        if not adapter:
            adapter_failures.append(f"missing adapter {contract['adapter']}")
        for core in CORE_FILES:
            if core not in shim:
                adapter_failures.append(f"shim does not route to {core}")
        if "NOT_AUTHORITY:" not in adapter or "CLASS: reference" not in adapter:
            adapter_failures.append("adapter authority boundary is incomplete")
        if SETUP_CONTRACT not in adapter:
            adapter_failures.append("adapter does not route to the shared v1 setup contract")
        if name not in index or "certified-for-launch" not in index:
            adapter_failures.append("adapter is absent from the launch certification matrix")
        for message in adapter_failures:
            failures.append({"adapter": name, "message": message})
        results.append(
            {
                "adapter": name,
                "status": "pass" if not adapter_failures else "fail",
                "shim": contract["shim"],
                "adapter_file": contract["adapter"],
                "external_usability_evidence": contract["external_evidence"],
            }
        )

    required_index_terms = [
        "npx @precodeos/precodeos fast-setup-preview --target <target-project-root>",
        "package version",
        "support status",
        "prerequisites",
        "approval IDs",
        "recovery route",
        "next safe action",
        "stop reason",
        "stop before product work",
        "external usability evidence remains pending",
    ]
    for term in required_index_terms:
        if term not in index:
            failures.append({"adapter": "shared_contract", "message": f"missing contract term: {term}"})
    if ".cursor/rules/precode-os.mdc" in read(root / "adapters/CURSOR.md"):
        failures.append({"adapter": "Cursor", "message": "stale unshipped .cursor rule shim claim"})

    return {
        "tool": "adapter-conformance-check",
        "status": "pass" if not failures else "fail",
        "certified_platform": "macOS",
        "claim_boundary": "bounded setup, validation, orientation, and next-safe-action identification",
        "adapters": results,
        "failures": failures,
        "generated_evidence_only": True,
        "approves_release": False,
    }


def self_test() -> dict[str, Any]:
    with tempfile.TemporaryDirectory(prefix="precode-adapter-conformance-") as tmp:
        root = Path(tmp)
        (root / "adapters").mkdir()
        for contract in ADAPTERS.values():
            shim = root / contract["shim"]
            shim.write_text("\n".join(CORE_FILES), encoding="utf-8")
            adapter = root / contract["adapter"]
            adapter.write_text(f"NOT_AUTHORITY: fixture\nCLASS: reference\n{SETUP_CONTRACT}\n", encoding="utf-8")
        (root / "adapters/ADAPTER-INDEX.md").write_text(
            "\n".join(
                [
                    *ADAPTERS.keys(),
                    "certified-for-launch",
                    "npx @precodeos/precodeos fast-setup-preview --target <target-project-root>",
                    "package version support status prerequisites approval IDs recovery route next safe action stop reason",
                    "stop before product work",
                    "external usability evidence remains pending",
                ]
            ),
            encoding="utf-8",
        )
        passing = build_payload(root)
        (root / "adapters/CURSOR.md").write_text("NOT_AUTHORITY: fixture\nCLASS: reference\n", encoding="utf-8")
        failing = build_payload(root)
    failures = []
    if passing["status"] != "pass":
        failures.append({"scenario": "complete fixture", "actual": passing["failures"]})
    if failing["status"] != "fail":
        failures.append({"scenario": "drift fixture", "actual": failing["status"]})
    return {"tool": "adapter-conformance-check", "mode": "self-test", "status": "pass" if not failures else "fail", "failures": failures}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    payload = self_test() if args.self_test else build_payload(repo_root())
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0 if payload["status"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
