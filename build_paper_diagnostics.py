"""生成 benchmark 统计表与规则化解释性案例。"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
import pandas as pd

from generalization_audit import load_bundle, load_drug_scaffolds


ROOT = Path(__file__).resolve().parent


def _json(root: Path, relative: str) -> dict:
    return json.loads((root / relative).read_text(encoding="utf-8"))


def _dataset_result(config: dict, dataset: str) -> dict:
    rows = [row for row in config["dataset_results"] if row["dataset"] == dataset]
    if len(rows) != 1:
        raise ValueError(f"数据集 {dataset!r} 的配置结果不是唯一一项")
    return rows[0]


def collect_dataset_stats(root: Path = ROOT) -> pd.DataFrame:
    mi_bundle = load_bundle(root / "Dataset", "Mi")
    mi_scaffolds = load_drug_scaffolds(root / "Dataset", "Mi")
    mi_active = np.flatnonzero(mi_bundle.pair.sum(axis=0) > 0)

    hmvcc = _json(root, "results/hmvcc-drug-cold-confirmation-20261019/combined_config.json")
    ncrna = _dataset_result(hmvcc, "ncRNADrug")
    nonco = _dataset_result(hmvcc, "NoncoRNA")
    deoverlap = _dataset_result(
        _json(root, "results/hmvcc-mi-deoverlap-confirmation-20261019/combined_config.json"),
        "ncRNADrug_mi_deoverlap",
    )
    rahgl = _json(root, "results/rahgl-scaffold-cold-confirmation-20261020/summary.json")
    sm = _json(root, "results/sm2mir-virgin-drug-temporal-20261019/config.json")
    sm_metrics = pd.read_csv(root / "results/sm2mir-virgin-drug-temporal-20261019/drug_metrics.csv")
    sm_test_positives = int(
        sm_metrics.loc[sm_metrics.model.eq("rna_prior_only"), "positive_count"].sum()
    )
    replication = _json(root, "results/independent-source-replication-pilot-20261020/summary.json")

    rows = [
        {
            "resource": "Mi",
            "rna_count": mi_bundle.pair.shape[0],
            "drug_count": mi_bundle.pair.shape[1],
            "active_or_test_drugs": len(mi_active),
            "positive_pairs": int(mi_bundle.pair.sum()),
            "scaffold_groups": len(set(mi_scaffolds[mi_active])),
            "source_fields": "mapped PMID/year table available",
            "benchmark_role": "primary scaffold-disjoint development",
        },
        {
            "resource": "ncRNADrug aligned",
            "rna_count": ncrna["aligned_rna_count"],
            "drug_count": ncrna["aligned_drug_count"],
            "active_or_test_drugs": ncrna["aligned_drug_count"],
            "positive_pairs": ncrna["mapped_positive_count"],
            "scaffold_groups": pd.NA,
            "source_fields": "no PMID/source column in triples.csv",
            "benchmark_role": "raw external-snapshot audit",
        },
        {
            "resource": "ncRNADrug entity-deoverlap",
            "rna_count": deoverlap["aligned_rna_count"],
            "drug_count": deoverlap["aligned_drug_count"],
            "active_or_test_drugs": deoverlap["aligned_drug_count"],
            "positive_pairs": deoverlap["mapped_positive_count"],
            "scaffold_groups": pd.NA,
            "source_fields": "no PMID/source column in triples.csv",
            "benchmark_role": "entity-independence sensitivity",
        },
        {
            "resource": "NoncoRNA aligned",
            "rna_count": nonco["aligned_rna_count"],
            "drug_count": nonco["aligned_drug_count"],
            "active_or_test_drugs": nonco["aligned_drug_count"],
            "positive_pairs": nonco["mapped_positive_count"],
            "scaffold_groups": pd.NA,
            "source_fields": "no source-level audit in current artifact",
            "benchmark_role": "external boundary",
        },
        {
            "resource": "RAHGL-MDR",
            "rna_count": rahgl["pair_shape"][0],
            "drug_count": rahgl["pair_shape"][1],
            "active_or_test_drugs": rahgl["active_drug_count"],
            "positive_pairs": rahgl["positive_pair_count"],
            "scaffold_groups": rahgl["active_scaffold_group_count"],
            "source_fields": "no pair-level PMID used here",
            "benchmark_role": "drug-cold versus scaffold-cold",
        },
        {
            "resource": "SM2miR non-Mi temporal subset",
            "rna_count": sm["rna_count"],
            "drug_count": sm["train_drug_count"] + sm["validation_drug_count"] + sm["test_drug_count"],
            "active_or_test_drugs": sm["test_drug_count"],
            "positive_pairs": sm_test_positives,
            "scaffold_groups": pd.NA,
            "source_fields": "miRBase ID, CID, PMID, year",
            "benchmark_role": "2011-2014 non-Mi test drugs; positives shown are test-only",
        },
        {
            "resource": "Mi distinct-PMID replication target",
            "rna_count": mi_bundle.pair.shape[0],
            "drug_count": mi_bundle.pair.shape[1],
            "active_or_test_drugs": replication["evaluable_test_drugs"],
            "positive_pairs": replication["mapping"]["replicated_pairs"],
            "scaffold_groups": pd.NA,
            "source_fields": "distinct PMID and publication year",
            "benchmark_role": "independent re-support target",
        },
    ]
    frame = pd.DataFrame(rows)
    if frame["resource"].duplicated().any():
        raise ValueError("resource 必须唯一")
    return frame


def collect_rahgl_case_studies(root: Path = ROOT) -> pd.DataFrame:
    run_dirs = [
        "results/rahgl-objective-alignment-pilot-20261020",
        "results/rahgl-objective-alignment-pilot-20261020-seed20261021",
        "results/rahgl-objective-alignment-pilot-20261020-seed20261022",
    ]
    drug_cold = pd.concat(
        [pd.read_csv(root / run / "per_drug_metrics.csv") for run in run_dirs],
        ignore_index=True,
    )
    drug_ap = drug_cold.groupby(["drug_id", "model"])["average_precision"].mean().unstack()
    drug_pos = drug_cold.groupby("drug_id")["positive_count"].nunique()
    if not drug_pos.eq(1).all():
        raise ValueError("drug-cold 三个种子的 positive_count 不一致")
    positive_count = drug_cold.groupby("drug_id")["positive_count"].first()

    scaffold = pd.read_csv(
        root / "results/rahgl-scaffold-cold-confirmation-20261020/aggregate_per_drug_metrics.csv"
    )
    scaffold_ap = scaffold.pivot(index="drug_id", columns="model", values="average_precision")
    scaffold_positive = scaffold.groupby("drug_id")["positive_count"].first()
    common = positive_count.index.intersection(scaffold_positive.index)
    if not positive_count.loc[common].equals(scaffold_positive.loc[common]):
        raise ValueError("drug-cold 与 scaffold-cold 的 positive_count 不一致")

    cases = pd.DataFrame(index=common)
    cases["positive_count"] = positive_count.loc[common]
    cases["drug_cold_candidate_ap"] = drug_ap.loc[common, "entity_balanced_pairwise_residual"]
    cases["drug_cold_prior_ap"] = drug_ap.loc[common, "rna_prior_only"]
    cases["drug_cold_delta"] = cases["drug_cold_candidate_ap"] - cases["drug_cold_prior_ap"]
    cases["scaffold_candidate_ap"] = scaffold_ap.loc[common, "entity_balanced_pairwise_residual"]
    cases["scaffold_prior_ap"] = scaffold_ap.loc[common, "rna_prior_only"]
    cases["scaffold_delta"] = cases["scaffold_candidate_ap"] - cases["scaffold_prior_ap"]
    cases["delta_drop"] = cases["drug_cold_delta"] - cases["scaffold_delta"]

    names = (
        pd.read_csv(
            root / ".cache/rahgl-mdr/repo/Dataset/midrug_master_final.csv",
            encoding="utf-8-sig",
        )[["Drug_ID", "Drug_Name", "DrugBank_ID", "CID"]]
        .drop_duplicates("Drug_ID")
        .set_index("Drug_ID")
    )
    cases = cases.join(names)
    strata = [
        ("5-9 positives", cases.positive_count.between(5, 9)),
        ("10-49 positives", cases.positive_count.between(10, 49)),
        ("50+ positives", cases.positive_count.ge(50)),
    ]
    selected = []
    for stratum, mask in strata:
        eligible = cases.loc[mask]
        if eligible.empty:
            raise ValueError(f"案例层级无候选: {stratum}")
        chosen = eligible.sort_values(["delta_drop", "positive_count"], ascending=[False, False]).iloc[0]
        row = chosen.to_dict()
        row.update({"drug_id": int(chosen.name), "selection_stratum": stratum})
        selected.append(row)
    frame = pd.DataFrame(selected)
    ordered = [
        "selection_stratum",
        "drug_id",
        "Drug_Name",
        "DrugBank_ID",
        "CID",
        "positive_count",
        "drug_cold_candidate_ap",
        "drug_cold_prior_ap",
        "drug_cold_delta",
        "scaffold_candidate_ap",
        "scaffold_prior_ap",
        "scaffold_delta",
        "delta_drop",
    ]
    return frame[ordered]


def stats_markdown(frame: pd.DataFrame) -> str:
    shown = frame.fillna("not centralized")
    lines = [
        "# Dataset and protocol statistics",
        "",
        "> Generated by `build_paper_diagnostics.py`. Counts describe the aligned artifact used by the stated benchmark role; they are not interchangeable with publisher-reported raw database totals.",
        "",
        "| Resource | ncRNAs | Drugs | Active/test drugs | Positive pairs | Scaffold groups | Source fields | Role |",
        "|---|---:|---:|---:|---:|---:|---|---|",
    ]
    for row in shown.itertuples(index=False):
        lines.append(
            f"| {row.resource} | {row.rna_count} | {row.drug_count} | {row.active_or_test_drugs} | "
            f"{row.positive_pairs} | {row.scaffold_groups} | {row.source_fields} | {row.benchmark_role} |"
        )
    lines.append("")
    return "\n".join(lines)


def cases_markdown(frame: pd.DataFrame) -> str:
    lines = [
        "# RAHGL split-sensitivity case studies",
        "",
        "> Post hoc explanatory cases, not inferential evidence. Within each prespecified positive-count stratum, the shown drug has the largest decrease in candidate-minus-prior AP from fixed drug-cold to scaffold-disjoint evaluation. Drug-cold and scaffold AP values are three-seed means.",
        "",
        "| Stratum | Drug | Positives | Drug-cold ΔAP | Scaffold ΔAP | Drop |",
        "|---|---|---:|---:|---:|---:|",
    ]
    for row in frame.itertuples(index=False):
        identifier = row.DrugBank_ID if pd.notna(row.DrugBank_ID) else f"CID {int(row.CID)}"
        lines.append(
            f"| {row.selection_stratum} | {row.Drug_Name.title()} ({identifier}) | {int(row.positive_count)} | "
            f"{row.drug_cold_delta:+.4f} | {row.scaffold_delta:+.4f} | {row.delta_drop:+.4f} |"
        )
    lines.extend(
        [
            "",
            "These examples show that split sensitivity is not confined to single-positive drugs. They do not identify a biological mechanism: the split changes the training set, validation choice, and available structural neighborhood simultaneously.",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--output-dir", type=Path, default=ROOT / "paper")
    args = parser.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    stats = collect_dataset_stats(args.root)
    cases = collect_rahgl_case_studies(args.root)
    stats.to_csv(args.output_dir / "dataset_protocol_stats.csv", index=False)
    (args.output_dir / "dataset_protocol_stats.md").write_text(stats_markdown(stats), encoding="utf-8")
    cases.to_csv(args.output_dir / "rahgl_split_case_studies.csv", index=False)
    (args.output_dir / "rahgl_split_case_studies.md").write_text(cases_markdown(cases), encoding="utf-8")
    print(f"wrote {len(stats)} resource rows and {len(cases)} case studies")


if __name__ == "__main__":
    main()
