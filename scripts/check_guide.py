#!/usr/bin/env python3
"""Validate the guide: internal links resolve, chapters are complete, CSV is well formed.

Run from the repository root:  python3 scripts/check_guide.py
Exits non-zero on any error, so it can run in CI on every push.
"""

from __future__ import annotations

import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
HEADING_RE = re.compile(r"^#{1,6}\s+(.*?)\s*$", re.MULTILINE)

USE_CASE_DIR = ROOT / "02-use-cases"
REQUIRED_USE_CASE_HEADINGS = [
    "What it actually does",
    "What it needs from you",
    "Where it goes wrong",
    "How to judge a pilot",
    "Questions worth asking a vendor",
]
TOP_LEVEL_CHAPTERS = [
    "01-what-ai-in-construction-means.md",
    "03-your-data-decides.md",
    "04-risks-and-controls.md",
    "05-a-90-day-plan.md",
    "06-how-to-buy-and-pilot.md",
    "07-faq.md",
]
TEMPLATES = [
    "templates/ai-use-case-scorecard.csv",
    "templates/pilot-scorecard.md",
    "templates/ai-acceptable-use-policy.md",
    "templates/vendor-questions.md",
]

errors: list[str] = []
notes: list[str] = []


def slug(text: str) -> str:
    text = re.sub(r"`", "", text.strip().lower())
    text = re.sub(r"[^\w\s-]", "", text)
    return re.sub(r"\s+", "-", text).strip("-")


def markdown_files() -> list[Path]:
    return sorted(p for p in ROOT.rglob("*.md") if ".git" not in p.parts)


def anchors_of(path: Path) -> set[str]:
    return {slug(h) for h in HEADING_RE.findall(path.read_text(encoding="utf-8"))}


def check_links() -> None:
    for path in markdown_files():
        text = path.read_text(encoding="utf-8")
        for raw in LINK_RE.findall(text):
            target = raw.strip()
            if target.startswith(("http://", "https://", "mailto:")):
                continue
            if target.startswith("#"):
                anchor, target_file = target[1:], path
            elif "#" in target:
                target_file_part, anchor = target.split("#", 1)
                target_file = (path.parent / target_file_part).resolve()
            else:
                anchor, target_file = "", (path.parent / target).resolve()

            rel = path.relative_to(ROOT)
            if target_file != path and not target_file.exists():
                errors.append(f"{rel}: link target does not exist -> {target}")
                continue
            if anchor and anchor not in anchors_of(target_file):
                errors.append(f"{rel}: anchor not found -> {target}")


def check_structure() -> None:
    if not (ROOT / "README.md").exists():
        errors.append("README.md is missing")

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    use_cases = sorted(USE_CASE_DIR.glob("*.md"))
    if len(use_cases) < 7:
        errors.append(f"expected at least 7 use-case chapters, found {len(use_cases)}")

    for path in use_cases:
        rel = path.relative_to(ROOT).as_posix()
        if rel not in readme:
            errors.append(f"README does not link to {rel}")
        body = path.read_text(encoding="utf-8")
        for heading in REQUIRED_USE_CASE_HEADINGS:
            if f"## {heading}" not in body:
                errors.append(f"{rel}: missing section '## {heading}'")
        for field in ("**Answers the question:**", "**Maturity:**", "**Data it needs:**"):
            if field not in body:
                errors.append(f"{rel}: missing summary field {field}")

    for rel in TOP_LEVEL_CHAPTERS + TEMPLATES:
        if not (ROOT / rel).exists():
            errors.append(f"missing file: {rel}")
        elif rel not in readme:
            errors.append(f"README does not link to {rel}")

    for rel in TEMPLATES:
        if rel in readme and rel not in {
            p.relative_to(ROOT).as_posix() for p in ROOT.rglob("*") if p.is_file()
        }:
            notes.append(f"template listed but not present: {rel}")


def check_csv() -> None:
    for rel in TEMPLATES:
        if not rel.endswith(".csv"):
            continue
        path = ROOT / rel
        if not path.exists():
            continue
        with path.open(encoding="utf-8", newline="") as handle:
            rows = list(csv.reader(handle))
        if not rows:
            errors.append(f"{rel}: empty")
            continue
        width = len(rows[0])
        if width < 5:
            errors.append(f"{rel}: header row looks wrong ({width} columns)")
        for index, row in enumerate(rows, start=1):
            if row and len(row) != width:
                errors.append(f"{rel}: row {index} has {len(row)} columns, expected {width}")


def check_word_counts() -> None:
    for path in markdown_files():
        rel = path.relative_to(ROOT).as_posix()
        if not rel.startswith("02-use-cases/"):
            continue
        words = len(path.read_text(encoding="utf-8").split())
        if words < 500:
            errors.append(f"{rel}: looks thin ({words} words)")


def main() -> int:
    check_links()
    check_structure()
    check_csv()
    check_word_counts()

    files = len(markdown_files())
    for note in notes:
        print(f"note: {note}")
    if errors:
        print(f"\nFAIL: {len(errors)} problem(s) across {files} markdown files\n")
        for error in errors:
            print(f"  - {error}")
        return 1

    use_cases = len(list(USE_CASE_DIR.glob("*.md")))
    print(f"OK: {files} markdown files, {use_cases} use-case chapters, all internal links resolve")
    return 0


if __name__ == "__main__":
    sys.exit(main())
