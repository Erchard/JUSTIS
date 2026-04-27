#!/usr/bin/env python3
"""Lightweight integrity checks for the JUSTIS corpus."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def parse_table_rows(path: Path) -> list[list[str]]:
    rows: list[list[str]] = []
    for line in read_text(path).splitlines():
        stripped = line.strip()
        if not stripped.startswith("|"):
            continue
        if set(stripped.replace("|", "").replace("-", "").replace(" ", "")) == set():
            continue
        cells = [cell.strip() for cell in stripped.strip("|").split("|")]
        rows.append(cells)
    return rows


def check_markdown_links(errors: list[str]) -> None:
    link_pattern = re.compile(r"`([^`]+?\.(?:md|yml|yaml|txt|cff|py))`")
    for path in ROOT.rglob("*.md"):
        if ".git" in path.parts or "archive" in path.parts:
            continue
        text = read_text(path)
        for match in link_pattern.finditer(text):
            target = match.group(1)
            if target.startswith(("http://", "https://")):
                continue
            target_path = (ROOT / target).resolve()
            try:
                target_path.relative_to(ROOT)
            except ValueError:
                continue
            if not target_path.exists():
                fail(errors, f"{path.relative_to(ROOT)} references missing file `{target}`")


def check_open_questions(errors: list[str]) -> None:
    path = ROOT / "OPEN_QUESTIONS.md"
    rows = parse_table_rows(path)
    data_rows = [row for row in rows if row and re.fullmatch(r"Q-\d{3}", row[0])]
    seen: set[str] = set()
    valid_statuses = {
        "not_started",
        "opened",
        "in_research",
        "in_session",
        "blocked_by_deeper_question",
        "protocol_done",
        "argument_tree_done",
        "codex_candidate",
        "codex_done",
        "aporia",
        "ratification_required",
    }
    for row in data_rows:
        if len(row) != 6:
            fail(errors, f"OPEN_QUESTIONS.md row {row[0]} has {len(row)} cells, expected 6")
            continue
        qid, priority, status = row[0], row[1], row[2]
        if qid in seen:
            fail(errors, f"OPEN_QUESTIONS.md duplicates {qid}")
        seen.add(qid)
        if priority not in {"P0", "P1", "P2", "P3"}:
            fail(errors, f"{qid} has invalid priority {priority}")
        if status not in valid_statuses:
            fail(errors, f"{qid} has invalid status {status}")


def check_decisions(errors: list[str]) -> None:
    path = ROOT / "DECISIONS.md"
    rows = parse_table_rows(path)
    data_rows = [row for row in rows if row and re.fullmatch(r"D-\d{3}", row[0])]
    seen: set[str] = set()
    valid_content = {
        "consensus_plenus",
        "consensus_limitatus",
        "consensus_practicus",
        "aporia",
        "revisendum",
    }
    for row in data_rows:
        if len(row) != 7:
            fail(errors, f"DECISIONS.md row {row[0]} has {len(row)} cells, expected 7")
            continue
        did, status = row[0], row[4]
        if did in seen:
            fail(errors, f"DECISIONS.md duplicates {did}")
        seen.add(did)
        if status not in valid_content:
            fail(errors, f"{did} has invalid content status {status}")


def check_cases(errors: list[str]) -> None:
    path = ROOT / "CASES.md"
    rows = parse_table_rows(path)
    data_rows = [row for row in rows if row and re.fullmatch(r"C-\d{3}", row[0])]
    seen: set[str] = set()
    valid_statuses = {
        "candidate",
        "selected",
        "in_analysis",
        "tested",
        "requires_codex_revision",
        "archived",
    }
    for row in data_rows:
        if len(row) != 7:
            fail(errors, f"CASES.md row {row[0]} has {len(row)} cells, expected 7")
            continue
        cid, priority, status = row[0], row[1], row[2]
        if cid in seen:
            fail(errors, f"CASES.md duplicates {cid}")
        seen.add(cid)
        if priority not in {"P0", "P1", "P2", "P3"}:
            fail(errors, f"{cid} has invalid priority {priority}")
        if status not in valid_statuses:
            fail(errors, f"{cid} has invalid status {status}")


def check_codex_traceability(errors: list[str]) -> None:
    codex = read_text(ROOT / "codex" / "UNIVERSAL_JUSTICE_CODE.md")
    justification_index = read_text(ROOT / "support" / "codex" / "JUSTIFICATION_INDEX.md")
    status_index = read_text(ROOT / "support" / "codex" / "STATUS_INDEX.md")
    law_numbers = re.findall(r"### Lex ([IVXLCDM]+)\.", codex)
    for number in law_numbers:
        if f"Lex {number}" not in status_index:
            fail(errors, f"Codex Lex {number} missing status index entry")
        section_pattern = re.compile(rf"## Lex {re.escape(number)}\..*?(?=## Lex [IVXLCDM]+\.|\Z)", re.S)
        match = section_pattern.search(justification_index)
        if not match:
            fail(errors, f"Codex Lex {number} missing justification index entry")
            continue
        section = match.group(0)
        for required in ("protocols/", "arguments/", "research/"):
            if required not in section:
                fail(errors, f"Codex Lex {number} missing `{required}` traceability in justification index")


def check_codex_translations(errors: list[str]) -> None:
    translations_dir = ROOT / "codex" / "translations"
    expected = {
        "UNIVERSAL_JUSTICE_CODE.uk.md",
        "UNIVERSAL_JUSTICE_CODE.en.md",
        "UNIVERSAL_JUSTICE_CODE.zh-Hans.md",
        "UNIVERSAL_JUSTICE_CODE.hi.md",
        "UNIVERSAL_JUSTICE_CODE.es.md",
        "UNIVERSAL_JUSTICE_CODE.ar.md",
        "UNIVERSAL_JUSTICE_CODE.he.md",
    }
    actual = {
        path.name
        for path in translations_dir.glob("UNIVERSAL_JUSTICE_CODE.*.md")
        if path.is_file()
    }
    missing = expected - actual
    extra = actual - expected
    for filename in sorted(missing):
        fail(errors, f"Missing official codex translation {filename}")
    for filename in sorted(extra):
        fail(errors, f"Unexpected official codex translation {filename}")


def main() -> int:
    errors: list[str] = []
    check_markdown_links(errors)
    check_open_questions(errors)
    check_decisions(errors)
    check_cases(errors)
    check_codex_traceability(errors)
    check_codex_translations(errors)
    if errors:
        print("JUSTIS validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("JUSTIS validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
