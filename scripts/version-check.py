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
import re
import subprocess
import tempfile
from typing import Any

from os_compiler import repo_root


MARKDOWN_EXCLUDES = {
    "OS-HEALTH.md",
    "PRECODE-HELP.md",
    "PROGRESS.md",
    "logs/bead-build-journal.md",
    "logs/handoff-packet.md",
    "logs/learning-diary.md",
    "logs/scheduled-audit.md",
}
SCRIPT_VERSION_RE = re.compile(r"^# Version: v\d+\.\d+\.\d+$", re.MULTILINE)
SCRIPT_UPDATED_RE = re.compile(r"^# Last updated: \d{4}-\d{2}-\d{2}$", re.MULTILINE)
SCRIPT_OWNER_RE = re.compile(r"^# Owner: PrecodeOS$", re.MULTILINE)
DOC_VERSION_RE = re.compile(r"^Document version: v\d+\.\d+\.\d+$", re.MULTILINE)
DOC_UPDATED_RE = re.compile(r"^Last updated: \d{4}-\d{2}-\d{2}$", re.MULTILINE)
DOC_CREATOR_RE = re.compile(r"^Creator: Dan Sears / Recode$", re.MULTILINE)


def rel(path: Path, root: Path) -> str:
    return path.relative_to(root).as_posix()


def add(issues: list[dict[str, Any]], path: str, message: str) -> None:
    issues.append({"path": path, "severity": "warning", "message": message})


def public_git_candidates(root: Path) -> list[Path] | None:
    try:
        result = subprocess.run(
            ["git", "ls-files", "--cached", "--others", "--exclude-standard", "-z"],
            cwd=root,
            text=True,
            capture_output=True,
            check=False,
        )
    except OSError:
        return None
    if result.returncode != 0:
        return None
    return sorted(root / name for name in result.stdout.split("\0") if name and (root / name).is_file())


def markdown_files(root: Path) -> list[Path]:
    git_candidates = public_git_candidates(root)
    if git_candidates is not None:
        candidates = [path for path in git_candidates if path.suffix == ".md"]
    else:
        candidates = list(root.rglob("*.md"))

    included: list[Path] = []
    for path in candidates:
        name = rel(path, root)
        if ".git/" in name or name in MARKDOWN_EXCLUDES:
            continue
        if name.startswith(".agents/skills/"):
            continue
        if name.startswith("logs/") and name != "logs/LOG-EVIDENCE-TAXONOMY.md":
            continue
        included.append(path)
    return sorted(included)


def script_files(root: Path) -> list[Path]:
    git_candidates = public_git_candidates(root)
    if git_candidates is not None:
        return sorted(
            path
            for path in git_candidates
            if rel(path, root).startswith("scripts/") and path.suffix in {".py", ".sh"}
        )
    return sorted((root / "scripts").glob("*.py")) + sorted((root / "scripts").glob("*.sh"))


def workflow_files(root: Path) -> list[Path]:
    git_candidates = public_git_candidates(root)
    if git_candidates is not None:
        return sorted(
            path
            for path in git_candidates
            if rel(path, root).startswith(".github/workflows/") and path.suffix in {".yml", ".yaml"}
        )
    base = root / ".github" / "workflows"
    if not base.is_dir():
        return []
    return sorted([*base.glob("*.yml"), *base.glob("*.yaml")])


def check_doc(path: Path, root: Path, issues: list[dict[str, Any]]) -> None:
    text = path.read_text(encoding="utf-8")
    name = rel(path, root)
    if not DOC_CREATOR_RE.search(text):
        add(issues, name, "missing Creator metadata")
    if not DOC_VERSION_RE.search(text):
        add(issues, name, "missing or malformed Document version metadata")
    if not DOC_UPDATED_RE.search(text):
        add(issues, name, "missing or malformed Last updated metadata")


def check_script(path: Path, root: Path, issues: list[dict[str, Any]]) -> None:
    text = path.read_text(encoding="utf-8")
    name = rel(path, root)
    if not SCRIPT_VERSION_RE.search(text):
        add(issues, name, "missing or malformed script Version header")
    if not SCRIPT_UPDATED_RE.search(text):
        add(issues, name, "missing or malformed script Last updated header")
    if not SCRIPT_OWNER_RE.search(text):
        add(issues, name, "missing script Owner header")


def build_payload(root: Path) -> dict[str, Any]:
    issues: list[dict[str, Any]] = []
    markdown = markdown_files(root)
    scripts = script_files(root)
    workflows = workflow_files(root)

    for path in markdown:
        check_doc(path, root, issues)
    for path in scripts:
        check_script(path, root, issues)
    for path in workflows:
        check_script(path, root, issues)

    return {
        "tool": "version-check",
        "status": "pass" if not issues else "fail",
        "checked": {
            "markdown": len(markdown),
            "scripts": len(scripts),
            "workflows": len(workflows),
        },
        "issues": issues,
    }


def exit_code(payload: dict[str, Any]) -> int:
    return 0 if payload.get("status") == "pass" else 1


def self_test() -> int:
    failures: list[dict[str, str]] = []
    with tempfile.TemporaryDirectory(prefix="precode-version-check-") as tmp:
        root = Path(tmp)
        good_doc = root / "GOOD.md"
        bad_doc = root / "BAD.md"
        good_script = root / "scripts" / "good.py"
        bad_script = root / "scripts" / "bad.py"
        good_doc.write_text(
            "# Good\n\n"
            "Creator: Dan Sears / Recode\n"
            "Document version: v0.1.0\n"
            "Last updated: 2026-07-26\n",
            encoding="utf-8",
        )
        bad_doc.write_text("# Bad\n", encoding="utf-8")
        good_script.parent.mkdir(parents=True, exist_ok=True)
        good_script.write_text(
            "#!/usr/bin/env python3\n"
            "# Version: v0.1.0\n"
            "# Last updated: 2026-07-26\n"
            "# Owner: PrecodeOS\n",
            encoding="utf-8",
        )
        bad_script.write_text("#!/usr/bin/env python3\n", encoding="utf-8")

        pass_issues: list[dict[str, Any]] = []
        check_doc(good_doc, root, pass_issues)
        check_script(good_script, root, pass_issues)
        pass_payload = {"status": "pass" if not pass_issues else "fail", "issues": pass_issues}
        if exit_code(pass_payload) != 0:
            failures.append({"scenario": "clean fixture exit", "expected": "0", "actual": str(exit_code(pass_payload))})

        fail_issues: list[dict[str, Any]] = []
        check_doc(bad_doc, root, fail_issues)
        check_script(bad_script, root, fail_issues)
        fail_payload = {"status": "pass" if not fail_issues else "fail", "issues": fail_issues}
        if exit_code(fail_payload) == 0:
            failures.append({"scenario": "drift fixture exit", "expected": "nonzero", "actual": "0"})
        if len(fail_issues) < 5:
            failures.append({"scenario": "drift fixture issues", "expected": "metadata issues", "actual": str(fail_issues)})

    payload = {
        "tool": "version-check",
        "mode": "self-test",
        "status": "pass" if not failures else "fail",
        "scenario_count": 2,
        "failures": failures,
    }
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0 if not failures else 1


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--self-test", action="store_true", help="run deterministic version-check enforcement fixtures")
    args = parser.parse_args()
    if args.self_test:
        return self_test()
    payload = build_payload(repo_root())
    print(json.dumps(payload, indent=2, sort_keys=True))
    return exit_code(payload)


if __name__ == "__main__":
    raise SystemExit(main())
