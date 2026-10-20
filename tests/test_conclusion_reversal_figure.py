import hashlib

import matplotlib.pyplot as plt
import pandas as pd
import pytest

from figures.gen_fig_conclusion_reversals import (
    INPUT,
    SELECTION,
    build_figure,
    interval_class,
    save_figure,
    selected_results,
)


def test_interval_classification() -> None:
    assert interval_class(0.01, 0.02) == "positive"
    assert interval_class(-0.01, 0.02) == "uncertain"
    assert interval_class(-0.03, -0.01) == "negative"


def test_selected_results_are_complete_and_ordered() -> None:
    selected = selected_results(pd.read_csv(INPUT))
    assert selected["comparison_id"].tolist() == [row[1] for row in SELECTION]
    assert set(selected["interval_class"]) == {"positive", "uncertain", "negative"}


def test_selected_results_reject_missing_comparison() -> None:
    with pytest.raises(ValueError, match="缺少绘图比较"):
        selected_results(pd.DataFrame({"comparison_id": ["other"]}))


def test_pdf_is_byte_deterministic(tmp_path) -> None:
    frame = pd.read_csv(INPUT)
    hashes = []
    for index in range(2):
        fig = build_figure(frame)
        pdf = tmp_path / f"figure-{index}.pdf"
        png = tmp_path / f"figure-{index}.png"
        save_figure(fig, pdf, png)
        plt.close(fig)
        hashes.append(hashlib.sha256(pdf.read_bytes()).hexdigest())
    assert hashes[0] == hashes[1]
