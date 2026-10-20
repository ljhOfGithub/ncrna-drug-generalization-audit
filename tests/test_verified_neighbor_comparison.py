import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CSV_PATH = ROOT / "paper" / "verified_neighbor_comparison.csv"
MD_PATH = ROOT / "paper" / "verified_neighbor_comparison.md"
VENUE_PATH = ROOT / "paper" / "venue_eligibility.md"


def _rows():
    with CSV_PATH.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def _neighbors():
    return [row for row in _rows() if not row["work"].endswith("(this study)")]


def test_five_fulltext_neighbors_are_present():
    neighbors = _neighbors()
    assert {row["work"] for row in neighbors} == {
        "ncRD-LG",
        "RAHGL-MDR",
        "HMVCC",
        "MGCNA",
        "PLMF-MDA",
    }
    assert all("full HTML" in row["evidence_tier"] or "PDF to EOF" in row["evidence_tier"] for row in neighbors)


def test_neighbors_do_not_claim_scaffold_or_source_independence():
    neighbors = _neighbors()
    assert all(row["scaffold_disjoint"] == "no" for row in neighbors)
    assert all(row["independent_source"] == "no" for row in neighbors)


def test_markdown_preserves_provisional_novelty_boundary():
    text = MD_PATH.read_text(encoding="utf-8")
    assert "provisional gap" in text
    assert "不能写成“首次”" in text
    assert "案例研究中的全候选排序不算作" in text


def test_venue_eligibility_records_official_verification_boundary():
    text = VENUE_PATH.read_text(encoding="utf-8")
    assert "查询日期：2026-10-20" in text
    assert text.count("official_partition_unverified") >= 6
    assert "不得用 JCR Q1 替代中科院一区" in text
