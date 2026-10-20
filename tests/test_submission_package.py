from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_english_abstract_and_keywords_meet_pattern_recognition_limits() -> None:
    text = (ROOT / "paper/manuscript_en.md").read_text(encoding="utf-8")
    abstract = text.split("## Abstract\n", 1)[1].split("**Keywords:**", 1)[0]
    words = re.findall(r"\b[\w–-]+\b", abstract)
    assert 150 <= len(words) <= 250

    keyword_line = text.split("**Keywords:**", 1)[1].splitlines()[0]
    keywords = [item.strip() for item in keyword_line.split(";") if item.strip()]
    assert 1 <= len(keywords) <= 7


def test_highlights_meet_count_and_character_limits() -> None:
    lines = [
        line.strip()
        for line in (ROOT / "paper/highlights_en.txt").read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    assert 3 <= len(lines) <= 5
    assert all(len(line) <= 85 for line in lines)


def test_core_citation_audit_is_complete_and_unique() -> None:
    audit = json.loads((ROOT / "paper/CITATION_AUDIT.json").read_text(encoding="utf-8"))
    entries = audit["entries"]
    extended_keys = audit["extended_reference_keys"]
    assert len(entries) == 10
    assert len(extended_keys) == 25
    assert audit["summary"]["references"] == len(entries) + len(extended_keys) == 35
    assert audit["summary"]["existence_verified"] == audit["summary"]["references"]
    assert audit["summary"]["post_fix_unresolved_core_entries"] == 0
    dois = [entry["doi"].lower() for entry in entries]
    assert len(dois) == len(set(dois))
    core_keys = {entry["key"] for entry in entries}
    assert len(extended_keys) == len(set(extended_keys))
    assert core_keys.isdisjoint(extended_keys)


def test_cover_letter_answers_journal_specific_questions() -> None:
    text = (ROOT / "paper/cover_letter_en.md").read_text(encoding="utf-8")
    assert "Comparison with the state of the art" in text
    assert "Public datasets" in text
    assert "Validation metrics" in text


def test_submission_copy_matches_authoritative_highlights() -> None:
    assert (ROOT / "submission-pattern-recognition/highlights.txt").read_bytes() == (
        ROOT / "paper/highlights_en.txt"
    ).read_bytes()
