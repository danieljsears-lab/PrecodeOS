from __future__ import annotations

import json
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TODO = ROOT / "tasks" / "todo.md"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write(path: Path, content: str) -> None:
    path.write_text(content, encoding="utf-8")


def frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---"):
        return {}
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}
    data: dict[str, str] = {}
    for raw_line in parts[1].splitlines():
        line = raw_line.strip()
        if not line or ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip('"')
    return data


def todo_data() -> dict[str, str]:
    return frontmatter(read(TODO))


def current_bead_path() -> Path:
    bead = todo_data().get("current_bead")
    if not bead:
        raise SystemExit("tasks/todo.md does not declare current_bead.")
    return ROOT / bead


def current_bead_text() -> str:
    return read(current_bead_path())


def current_bead_data() -> dict[str, str]:
    return frontmatter(current_bead_text())


def section(text: str, heading: str) -> list[str]:
    pattern = re.compile(rf"^## {re.escape(heading)}\n(?P<body>.*?)(?=^## |\Z)", re.M | re.S)
    match = pattern.search(text)
    if not match:
        return []
    return [line[2:].strip() for line in match.group("body").splitlines() if line.startswith("- ")]


def write_json(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


def git_status_paths() -> list[str]:
    try:
        root_result = subprocess.run(
            ["git", "rev-parse", "--show-toplevel"],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )
        if root_result.returncode != 0:
            return []
        if Path(root_result.stdout.strip()).resolve() != ROOT.resolve():
            return []
        result = subprocess.run(
            ["git", "status", "--porcelain"],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )
    except FileNotFoundError:
        return []
    if result.returncode != 0:
        return []
    return [line[3:] for line in result.stdout.splitlines() if len(line) > 3]


def replace_status(path: Path, status: str, class_name: str | None = None) -> None:
    text = read(path)
    text = re.sub(r"status: .+", f"status: {status}", text, count=1)
    if class_name:
        text = re.sub(r"> CLASS: [^\n]+", f"> CLASS: {class_name}", text, count=1)
    write(path, text)


def set_active_bead(bead_path: str) -> None:
    text = read(TODO)
    text = re.sub(r"current_bead: .+", f"current_bead: {bead_path}", text, count=1)
    text = re.sub(r"current_state: .+", "current_state: in_progress", text, count=1)
    text = re.sub(
        r"- `tasks/beads/[^`]+`\n- State: `[^`]+`",
        f"- `{bead_path}`\n- State: `in_progress`",
        text,
        count=1,
    )
    write(TODO, text)
