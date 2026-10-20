import pandas as pd
import pytest

from rna_frequency_stratum_audit import align_predictions, frequency_stratum, stratum_metrics


def test_frequency_stratum_boundaries():
    assert [frequency_stratum(value) for value in (0, 1, 2, 3, 9, 10)] == [
        "zero",
        "low_1_2",
        "low_1_2",
        "mid_3_9",
        "mid_3_9",
        "high_ge_10",
    ]
    with pytest.raises(ValueError):
        frequency_stratum(-1)


def test_align_predictions_requires_exact_pair_alignment():
    rows = []
    for model in ("candidate", "baseline"):
        rows.append(
            {"fold": 0, "rna_id": 1, "drug_id": 2, "label": 1, "model": model, "probability": 0.7}
        )
    aligned = align_predictions(pd.DataFrame(rows), "candidate", "baseline")
    assert len(aligned) == 1
    with pytest.raises(ValueError):
        align_predictions(pd.DataFrame(rows[:-1]), "candidate", "baseline")


def test_stratum_metrics_detects_positive_residual_separation():
    frame = pd.DataFrame(
        {
            "label": [1, 1, 0, 0],
            "candidate_probability": [0.9, 0.8, 0.2, 0.1],
            "baseline_probability": [0.5, 0.5, 0.5, 0.5],
        }
    )
    metrics = stratum_metrics(frame)
    assert metrics["delta_balanced_ap"] > 0
    assert metrics["residual_separation"] == pytest.approx(0.7)
    assert metrics["positive_residual_gt_zero_fraction"] == 1.0
    assert metrics["unlabeled_residual_gt_zero_fraction"] == 0.0
