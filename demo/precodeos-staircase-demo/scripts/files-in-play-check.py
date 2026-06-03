#!/usr/bin/env python3
import sys
from fnmatch import fnmatch
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from scripts.precode_demo import current_bead_text, git_status_paths, section

patterns = section(current_bead_text(), "Files In Play")
changed = git_status_paths()

if not changed:
    print("Files In Play Check: Clear")
    print("No changed files detected by git.")
    raise SystemExit(0)

outside = []
for path in changed:
    if not any(fnmatch(path, pattern) or fnmatch(path, pattern.rstrip("/**")) for pattern in patterns):
        outside.append(path)

if outside:
    print("Files In Play Check: Drift Risk")
    print("Changed paths outside the active bead files in play:")
    for path in outside:
        print(f"- {path}")
    raise SystemExit(1)

print("Files In Play Check: Clear")
print("Changed paths are inside the active bead files in play:")
for path in changed:
    print(f"- {path}")
