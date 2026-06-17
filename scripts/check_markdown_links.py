#!/usr/bin/env python3
"""Check local Markdown links without external dependencies."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
LINK_RE = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
FENCE_RE = re.compile(r"^\s*```")
EXTERNAL_PREFIXES = ("http://", "https://", "mailto:", "tel:")


def iter_markdown_files() -> list[Path]:
    return sorted(
        path
        for path in ROOT.rglob("*.md")
        if ".git" not in path.relative_to(ROOT).parts
    )


def strip_title(raw_target: str) -> str:
    target = raw_target.strip()
    if target.startswith("<") and ">" in target:
        return target[1 : target.index(">")].strip()
    if " " in target:
        first, rest = target.split(" ", 1)
        if rest.lstrip().startswith(("\"", "'")):
            return first.strip()
    return target


def clean_target(raw_target: str) -> str | None:
    target = strip_title(raw_target)
    if not target or target.startswith("#"):
        return None
    if target.startswith(EXTERNAL_PREFIXES):
        return None
    if target.startswith(("app://", "ssh://")):
        return None
    return unquote(target.split("#", 1)[0].split("?", 1)[0])


def check_file(path: Path) -> list[str]:
    errors: list[str] = []
    in_fence = False

    for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if FENCE_RE.match(line):
            in_fence = not in_fence
            continue
        if in_fence:
            continue

        for match in LINK_RE.finditer(line):
            target = clean_target(match.group(1))
            if target is None:
                continue

            if target.startswith("/"):
                candidate = ROOT / target.lstrip("/")
            else:
                candidate = path.parent / target

            if not candidate.exists():
                rel_path = path.relative_to(ROOT)
                errors.append(f"{rel_path}:{line_no}: broken local link: {match.group(1)}")

    return errors


def main() -> int:
    errors: list[str] = []
    files = iter_markdown_files()
    for path in files:
        errors.extend(check_file(path))

    if errors:
        print("Broken local Markdown links found:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Markdown link check passed for {len(files)} files.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
