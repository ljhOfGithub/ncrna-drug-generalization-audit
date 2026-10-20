"""生成冷启动审计的结论翻转森林图。"""

from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "paper" / "main_results.csv"
OUTPUT_PDF = Path(__file__).resolve().parent / "fig_conclusion_reversals.pdf"
OUTPUT_PNG = Path(__file__).resolve().parent / "fig_conclusion_reversals.png"

SELECTION = [
    ("Public-model and prior baselines", "mi_scaffold_seed_20261019_vs_prior", "Mi scaffold-cold: residual vs RNA prior"),
    ("Public-model and prior baselines", "mi_scaffold_candidate_vs_localgl", "Mi scaffold-cold: residual vs LocalGL"),
    ("Split and overlap audits", "ncrnadrug_drug_cold_vs_prior", "ncRNADrug drug-cold: raw snapshot"),
    ("Split and overlap audits", "ncrnadrug_entity_deoverlap_vs_prior", "ncRNADrug drug-cold: de-overlapped"),
    ("Split and overlap audits", "rahgl_fixed_drug_cold_vs_prior", "RAHGL-MDR: fixed drug-cold"),
    ("Split and overlap audits", "rahgl_scaffold_cold_vs_prior", "RAHGL-MDR: scaffold-disjoint"),
    ("Source-target audit", "pmid_replication_vs_replicated_rna_prior", "Replication target: vs replication prior"),
    ("Source-target audit", "pmid_replication_vs_reported_rna_prior", "Replication target: vs reported prior"),
]

COLORS = {
    "positive": "#0072B2",
    "uncertain": "#7F7F7F",
    "negative": "#D55E00",
}

PDF_METADATA = {
    "Creator": "ncRD-LG generalization audit",
    "Producer": "Matplotlib",
    "CreationDate": datetime(2026, 10, 20, tzinfo=timezone.utc),
    "ModDate": datetime(2026, 10, 20, tzinfo=timezone.utc),
}


def interval_class(ci_low: float, ci_high: float) -> str:
    if ci_low > 0:
        return "positive"
    if ci_high < 0:
        return "negative"
    return "uncertain"


def selected_results(frame: pd.DataFrame) -> pd.DataFrame:
    indexed = frame.set_index("comparison_id", verify_integrity=True)
    missing = [comparison_id for _, comparison_id, _ in SELECTION if comparison_id not in indexed.index]
    if missing:
        raise ValueError(f"主结果表缺少绘图比较: {missing}")
    rows = []
    for group, comparison_id, label in SELECTION:
        row = indexed.loc[comparison_id].to_dict()
        row.update(
            {
                "comparison_id": comparison_id,
                "group": group,
                "label": label,
                "interval_class": interval_class(row["ci_low"], row["ci_high"]),
            }
        )
        rows.append(row)
    return pd.DataFrame(rows)


def build_figure(frame: pd.DataFrame) -> plt.Figure:
    plot = selected_results(frame)
    plt.rcParams.update(
        {
            "font.family": "serif",
            "font.serif": ["Times New Roman", "DejaVu Serif"],
            "font.size": 9,
            "axes.labelsize": 9.5,
            "legend.fontsize": 8,
            "legend.frameon": False,
            "figure.dpi": 300,
            "savefig.dpi": 300,
            "savefig.bbox": "tight",
            "axes.spines.top": False,
            "axes.spines.right": False,
        }
    )
    fig, ax = plt.subplots(figsize=(6.75, 4.45))
    y_positions = list(range(len(plot) - 1, -1, -1))
    for y, row in zip(y_positions, plot.itertuples(index=False), strict=True):
        color = COLORS[row.interval_class]
        ax.errorbar(
            row.delta,
            y,
            xerr=[[row.delta - row.ci_low], [row.ci_high - row.delta]],
            fmt="o",
            color=color,
            ecolor=color,
            elinewidth=1.8,
            capsize=3,
            markersize=5.5,
            markeredgecolor="white",
            markeredgewidth=0.6,
            zorder=3,
        )
        ax.text(
            row.ci_high + 0.0016,
            y,
            f"{row.delta:+.3f}",
            va="center",
            fontsize=7.7,
            color="#333333",
        )

    ax.axvline(0, color="#333333", linewidth=1.0, linestyle="--", zorder=1)
    ax.set_yticks(y_positions)
    ax.set_yticklabels(plot["label"].tolist())
    ax.set_xlabel(r"$\Delta$ full-candidate drug-macro AP (candidate $-$ baseline)")
    ax.set_xlim(-0.060, 0.031)
    ax.grid(axis="x", color="#D0D0D0", linewidth=0.6, alpha=0.55)
    ax.grid(axis="y", visible=False)
    ax.tick_params(axis="y", length=0)

    group_bounds: dict[str, list[int]] = {}
    for y, group in zip(y_positions, plot["group"], strict=True):
        group_bounds.setdefault(group, []).append(y)
    for index, (group, positions) in enumerate(group_bounds.items()):
        top, bottom = max(positions), min(positions)
        ax.axhspan(bottom - 0.48, top + 0.48, color="#F5F5F2" if index % 2 == 0 else "#FFFFFF", zorder=0)
        ax.text(
            -0.059,
            top + 0.62,
            group,
            ha="left",
            va="bottom",
            fontsize=8.2,
            fontweight="bold",
            color="#3B3B3B",
        )

    legend = [
        Line2D([0], [0], marker="o", color="none", markerfacecolor=COLORS["positive"], markeredgecolor="white", markersize=6, label="95% CI > 0"),
        Line2D([0], [0], marker="o", color="none", markerfacecolor=COLORS["uncertain"], markeredgecolor="white", markersize=6, label="95% CI includes 0"),
        Line2D([0], [0], marker="o", color="none", markerfacecolor=COLORS["negative"], markeredgecolor="white", markersize=6, label="95% CI < 0"),
    ]
    ax.legend(handles=legend, loc="lower right", ncol=3, bbox_to_anchor=(1.0, -0.25))
    fig.subplots_adjust(left=0.43, right=0.98, top=0.95, bottom=0.18)
    return fig


def save_figure(fig: plt.Figure, pdf_path: Path, png_path: Path) -> None:
    """以固定 PDF 元数据保存，避免重建时间改变证据包哈希。"""
    fig.savefig(pdf_path, metadata=PDF_METADATA)
    fig.savefig(png_path, dpi=300)


def main() -> None:
    frame = pd.read_csv(INPUT)
    fig = build_figure(frame)
    save_figure(fig, OUTPUT_PDF, OUTPUT_PNG)
    plt.close(fig)
    print(f"wrote {OUTPUT_PDF}")
    print(f"wrote {OUTPUT_PNG}")


if __name__ == "__main__":
    main()
