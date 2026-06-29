#!/usr/bin/env python3
# Version: v0.1.1
# Last updated: 2026-06-19
# Owner: PrecodeOS
# Created by Dan Sears / Recode.
# SPDX-License-Identifier: Apache-2.0
from __future__ import annotations

import argparse
import os
from pathlib import Path
import shlex
import subprocess
import sys


REQUIRED_ROOT_PATHS = ("AGENT.md", "DECISIONS.md", "tasks/todo.md", "scripts/next-step.py")
BOUNDARY_NOTE = (
    "precode is a local wrapper over existing PrecodeOS scripts. Markdown owner files and "
    "underlying scripts remain authoritative; generated output is evidence only."
)
def find_repo_root(start: Path | None = None) -> Path | None:
    current = (start or Path.cwd()).resolve()
    for candidate in (current, *current.parents):
        if all((candidate / path).exists() for path in REQUIRED_ROOT_PATHS):
            return candidate
    return None


def command_text(command: list[str]) -> str:
    return " ".join(shlex.quote(part) for part in command)


def run_commands(commands: list[list[str]], *, root: Path, dry_run: bool = False) -> int:
    print(BOUNDARY_NOTE, flush=True)
    for command in commands:
        print(f"Underlying command: {command_text(command)}", flush=True)
    if dry_run:
        return 0
    for command in commands:
        completed = subprocess.run(command, cwd=root, env=os.environ.copy(), check=False)
        if completed.returncode != 0:
            return completed.returncode
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="precode",
        description="Optional local shortcut over trusted PrecodeOS repo commands; start normal work in the Daily Cockpit.",
        epilog=(
            "This wrapper does not approve tasks, transitions, releases, setup mutation, "
            "external mutation, package updates, or generated evidence as authority."
        ),
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="print the underlying command without running it",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    def add_dry_run(subparser: argparse.ArgumentParser) -> argparse.ArgumentParser:
        subparser.add_argument(
            "--dry-run",
            action="store_true",
            default=argparse.SUPPRESS,
            help="print the underlying command without running it",
        )
        return subparser

    add_dry_run(subparsers.add_parser("start", help="run the Daily Cockpit session-start command"))
    add_dry_run(subparsers.add_parser("next", help="show advisory next-step guidance; does not choose work"))
    add_dry_run(subparsers.add_parser("health", help="show generated OS Health evidence; not authority"))
    add_dry_run(subparsers.add_parser("validate", help="validate active memory and package state"))
    add_dry_run(subparsers.add_parser("check", help="run the local package validation summary"))

    bootstrap = add_dry_run(subparsers.add_parser(
        "bootstrap-check",
        help="run scripts/bootstrap-check.py with curated setup-inspection flags",
    ))
    bootstrap.add_argument("--source", required=True, help="PrecodeOS package source path")
    bootstrap.add_argument("--target", required=True, help="target project path")
    bootstrap.add_argument("--json", action="store_true", help="print JSON output")
    bootstrap.add_argument("--preview-manifest", action="store_true", help="include manifest dry-run preview")
    bootstrap.add_argument("--supervised-setup-plan", action="store_true", help="include supervised setup plan")
    bootstrap.add_argument(
        "--apply-supervised-setup",
        action="store_true",
        help="apply only explicitly approved supervised setup copy actions",
    )
    bootstrap.add_argument(
        "--approve-action",
        action="append",
        default=[],
        help="approved supervised setup action ID; required for apply mode",
    )
    return parser


def build_commands(args: argparse.Namespace, parser: argparse.ArgumentParser) -> list[list[str]]:
    if args.command == "start":
        return [["bash", "scripts/session-start.sh"]]
    if args.command == "next":
        return [["python3", "scripts/next-step.py"]]
    if args.command == "health":
        return [["python3", "scripts/os-health.py"]]
    if args.command == "validate":
        return [["bash", "scripts/validate-memory.sh"]]
    if args.command == "check":
        return [
            ["bash", "scripts/validate-memory.sh"],
            ["python3", "scripts/version-check.py"],
            ["python3", "scripts/file-inventory.py", "--check"],
            ["python3", "scripts/public-repo-check.py"],
        ]
    if args.command == "bootstrap-check":
        if args.apply_supervised_setup and not args.supervised_setup_plan:
            parser.error("bootstrap-check --apply-supervised-setup requires --supervised-setup-plan")
        if args.apply_supervised_setup and not args.approve_action:
            parser.error("bootstrap-check --apply-supervised-setup requires at least one --approve-action <SP-ID>")
        command = [
            "python3",
            "scripts/bootstrap-check.py",
            "--source",
            args.source,
            "--target",
            args.target,
        ]
        if args.preview_manifest:
            command.append("--preview-manifest")
        if args.supervised_setup_plan:
            command.append("--supervised-setup-plan")
        if args.apply_supervised_setup:
            command.append("--apply-supervised-setup")
        for action_id in args.approve_action:
            command.extend(["--approve-action", action_id])
        if args.json:
            command.append("--json")
        return [command]
    parser.error(f"unknown command: {args.command}")
    raise AssertionError("unreachable")


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    root = find_repo_root()
    if root is None:
        print(
            "precode: not inside a PrecodeOS repo. Run from a repository containing "
            "AGENT.md, DECISIONS.md, tasks/todo.md, and scripts/next-step.py.",
            file=sys.stderr,
        )
        return 2
    commands = build_commands(args, parser)
    return run_commands(commands, root=root, dry_run=args.dry_run)


if __name__ == "__main__":
    raise SystemExit(main())
