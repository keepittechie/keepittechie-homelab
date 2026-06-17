#!/usr/bin/env python3
"""Check public-safe Mermaid diagram page structure."""

from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DIAGRAM_DIR = ROOT / "diagrams"
REQUIRED_SECTIONS = ("# ", "## Diagram", "## How to Read This", "## Public-Safe Notes")
INDEX_FILES = {DIAGRAM_DIR / "README.md"}


def check_diagram(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    rel_path = path.relative_to(ROOT)
    errors: list[str] = []

    if "```mermaid" not in text:
        errors.append(f"{rel_path}: missing Mermaid code fence")

    lines = text.splitlines()
    if not any(line.startswith("# ") for line in lines):
        errors.append(f"{rel_path}: missing top-level heading")

    for section in REQUIRED_SECTIONS[1:]:
        if section not in text:
            errors.append(f"{rel_path}: missing section {section!r}")

    return errors


def main() -> int:
    diagram_files = sorted(DIAGRAM_DIR.glob("*.md"))
    checked = [path for path in diagram_files if path not in INDEX_FILES]
    errors: list[str] = []

    for path in checked:
        errors.extend(check_diagram(path))

    if errors:
        print("Diagram structure issues found:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Diagram check passed for {len(checked)} diagram files.")
    if INDEX_FILES:
        skipped = ", ".join(path.relative_to(ROOT).as_posix() for path in sorted(INDEX_FILES))
        print(f"Skipped diagram index files: {skipped}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
