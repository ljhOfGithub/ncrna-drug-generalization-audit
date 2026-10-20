from pathlib import Path

import pandas as pd
import pytest

from paper_evidence_matrix import (
    ROOT,
    _model_mean,
    collect_main_results,
    validate_main_results,
)


def test_model_mean_requires_exactly_one_row(tmp_path: Path) -> None:
    path = tmp_path / "summary.csv"
    pd.DataFrame({"model": ["a", "b"], "mean": [0.2, 0.3]}).to_csv(path, index=False)
    assert _model_mean(tmp_path, "summary.csv", "a") == pytest.approx(0.2)
    with pytest.raises(ValueError, match="不是唯一一行"):
        _model_mean(tmp_path, "summary.csv", "missing")


def test_validation_rejects_inconsistent_delta() -> None:
    frame = pd.DataFrame(
        {
            "comparison_id": ["x"],
            "candidate_ap": [0.2],
            "baseline_ap": [0.1],
            "delta": [0.2],
            "ci_low": [0.0],
            "ci_high": [0.3],
        }
    )
    with pytest.raises(ValueError, match="无法复算 delta"):
        validate_main_results(frame)


def test_collects_only_the_frozen_claim_changing_comparisons() -> None:
    frame = collect_main_results(ROOT)
    assert len(frame) == 13
    assert frame["comparison_id"].is_unique
    assert set(frame["dataset"]) >= {"Mi", "ncRNADrug", "NoncoRNA", "RAHGL-MDR"}
    local = frame.set_index("comparison_id").loc["mi_scaffold_candidate_vs_localgl"]
    assert local["delta"] == pytest.approx(0.008472680224997678)
    schemnet = frame.set_index("comparison_id").loc[
        "mi_scaffold_candidate_vs_schemnet_no_seq"
    ]
    assert schemnet["delta"] == pytest.approx(0.007247545610775424)
    assert schemnet["ci_low"] > 0
    plmf = frame.set_index("comparison_id").loc[
        "mi_scaffold_candidate_vs_plmf_mda"
    ]
    assert plmf["delta"] == pytest.approx(0.026698046123734415)
    assert plmf["ci_low"] > 0
    deoverlap = frame.set_index("comparison_id").loc["ncrnadrug_entity_deoverlap_vs_prior"]
    assert deoverlap["delta"] < 0
