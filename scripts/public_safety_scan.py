#!/usr/bin/env python3
"""Conservative public-safety scan for obvious documentation leaks."""

from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKIP_DIRS = {".git"}
SAFE_ENV_EXAMPLE_RE = re.compile(r"(^|/).*\.env\.example$|(^|/)\.env\.example$")
PIHOLE_EXAMPLE = Path("examples/pihole/local-dns-records.example.csv")
SECRET_SCAN_WORKFLOW = Path(".github/workflows/secret-scan.yml")


@dataclass(frozen=True)
class Rule:
    name: str
    pattern: re.Pattern[str]
    skip_paths: tuple[Path, ...] = ()
    skip_env_examples: bool = False


RULES = (
    Rule("private key header", re.compile("PRIVATE" r"\s+KEY")),
    Rule("password assignment", re.compile("password" r"\s*=", re.IGNORECASE), skip_env_examples=True),
    Rule("api key assignment", re.compile("api_" r"key\s*=", re.IGNORECASE), skip_env_examples=True),
    Rule("secret assignment", re.compile("secret" r"\s*=", re.IGNORECASE), skip_env_examples=True),
    Rule("token assignment", re.compile("token" r"\s*=", re.IGNORECASE), skip_env_examples=True),
    Rule("tunnel secret", re.compile("Tunnel" r"Secret"), skip_env_examples=True),
    Rule("RSA private key marker", re.compile("BEGIN" r"\s+RSA")),
    Rule("OpenSSH private key marker", re.compile("BEGIN" r"\s+OPENSSH")),
    Rule(
        "private domain",
        re.compile(r"\b(?:kitpro" r"\.us|home\.kitpro" r"\.us|keepittechie" r"\.com)\b", re.IGNORECASE),
    ),
    Rule(
        "personal email or path",
        re.compile(r"(keepittechie" r"@gmail\.com|josh" r"@|/home/" r"josh|Documents/" r"GitHub)"),
    ),
    Rule(
        "private owner language",
        re.compile(
            r"\b(?:Josh" r"\s+should|my" r"\s+homelab|my" r"\s+channel|I" r"\s+need\s+to|for" r"\s+me)\b",
            re.IGNORECASE,
        ),
    ),
    Rule(
        "exact private host IP",
        re.compile(r"\b10\.10\.0\.(?:[1-9]|[1-9]\d|1\d{2}|2[0-4]\d|25[0-4])\b"),
        skip_paths=(PIHOLE_EXAMPLE,),
    ),
)


def rel_path(path: Path) -> Path:
    return path.relative_to(ROOT)


def is_binary(path: Path) -> bool:
    try:
        chunk = path.read_bytes()[:2048]
    except OSError:
        return True
    return b"\0" in chunk


def should_skip_file(path: Path) -> bool:
    relative = rel_path(path)
    if any(part in SKIP_DIRS for part in relative.parts):
        return True
    if relative == SECRET_SCAN_WORKFLOW:
        return True
    return is_binary(path)


def should_skip_rule(rule: Rule, path: Path) -> bool:
    relative = rel_path(path)
    if relative in rule.skip_paths:
        return True
    if rule.skip_env_examples and SAFE_ENV_EXAMPLE_RE.match(relative.as_posix()):
        return True
    return False


def iter_files() -> list[Path]:
    return sorted(path for path in ROOT.rglob("*") if path.is_file() and not should_skip_file(path))


def scan_file(path: Path) -> list[str]:
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except UnicodeDecodeError:
        return []

    findings: list[str] = []
    relative = rel_path(path)
    for line_no, line in enumerate(lines, 1):
        for rule in RULES:
            if should_skip_rule(rule, path):
                continue
            if rule.pattern.search(line):
                findings.append(f"{relative}:{line_no}: {rule.name}")
    return findings


def main() -> int:
    findings: list[str] = []
    files = iter_files()
    for path in files:
        findings.extend(scan_file(path))

    if findings:
        print("Public-safety scan found possible issues:")
        for finding in findings:
            print(f"- {finding}")
        print("\nReview the matches. If this is a sanitized example, narrow the allowlist intentionally.")
        return 1

    print(f"Public-safety scan passed for {len(files)} files.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
