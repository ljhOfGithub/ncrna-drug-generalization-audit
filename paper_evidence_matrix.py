"""从冻结实验结果生成论文主结果证据表。"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parent


def _json(root: Path, relative: str) -> dict:
    return json.loads((root / relative).read_text(encoding="utf-8"))


def _model_mean(root: Path, relative: str, model: str) -> float:
    frame = pd.read_csv(root / relative)
    rows = frame.loc[frame["model"].eq(model), "mean"]
    if len(rows) != 1:
        raise ValueError(f"{relative} 中模型 {model!r} 不是唯一一行")
    return float(rows.iloc[0])


def _dataset_result(config: dict, dataset: str) -> dict:
    matches = [row for row in config["dataset_results"] if row["dataset"] == dataset]
    if len(matches) != 1:
        raise ValueError(f"数据集 {dataset!r} 的配置结果不是唯一一项")
    return matches[0]


def _row(
    *,
    comparison_id: str,
    dataset: str,
    protocol: str,
    candidate: str,
    baseline: str,
    candidate_ap: float,
    baseline_ap: float,
    delta: float,
    ci: tuple[float, float],
    non_decrease: str,
    gate_status: str,
    evidence_role: str,
    sources: list[str],
) -> dict:
    return {
        "comparison_id": comparison_id,
        "dataset": dataset,
        "protocol": protocol,
        "candidate": candidate,
        "baseline": baseline,
        "candidate_ap": candidate_ap,
        "baseline_ap": baseline_ap,
        "delta": delta,
        "ci_low": ci[0],
        "ci_high": ci[1],
        "non_decrease": non_decrease,
        "gate_status": gate_status,
        "evidence_role": evidence_role,
        "sources": ";".join(sources),
    }


def collect_main_results(root: Path = ROOT) -> pd.DataFrame:
    rows: list[dict] = []

    chem_summary = "results/chemberta-pairwise-residual-pilot-20261019/mi_full_candidate_summary.csv"
    chem_config_path = "results/chemberta-pairwise-residual-pilot-20261019/mi_config.json"
    chem_config = _json(root, chem_config_path)
    chem_ap = _model_mean(root, chem_summary, "prior_preserving_pairwise_residual")
    chem_prior = _model_mean(root, chem_summary, "rna_prior_only")
    chem_ci = chem_config["full_candidate_bootstrap_95"]
    rows.append(
        _row(
            comparison_id="mi_scaffold_seed_20261019_vs_prior",
            dataset="Mi",
            protocol="5-fold scaffold-disjoint full-candidate",
            candidate="ChemBERTa pairwise prior-residual",
            baseline="RNA prior",
            candidate_ap=chem_ap,
            baseline_ap=chem_prior,
            delta=chem_config["full_candidate_macro_ap_delta"],
            ci=(chem_ci["low"], chem_ci["high"]),
            non_decrease=f'{chem_config["full_candidate_fold_non_decrease_count"]}/5 folds',
            gate_status="FAIL (+0.01 gate)",
            evidence_role="development result",
            sources=[chem_summary, chem_config_path],
        )
    )

    confirm_summary = "results/chemberta-pairwise-residual-confirmation-seed-20261020/mi_full_candidate_summary.csv"
    confirm_config_path = "results/chemberta-pairwise-residual-confirmation-seed-20261020/mi_config.json"
    confirm_config = _json(root, confirm_config_path)
    confirm_ci = confirm_config["full_candidate_bootstrap_95"]
    rows.append(
        _row(
            comparison_id="mi_scaffold_seed_20261020_vs_prior",
            dataset="Mi",
            protocol="second 5-fold scaffold-disjoint full-candidate",
            candidate="ChemBERTa pairwise prior-residual",
            baseline="RNA prior",
            candidate_ap=_model_mean(root, confirm_summary, "prior_preserving_pairwise_residual"),
            baseline_ap=_model_mean(root, confirm_summary, "rna_prior_only"),
            delta=confirm_config["full_candidate_macro_ap_delta"],
            ci=(confirm_ci["low"], confirm_ci["high"]),
            non_decrease=f'{confirm_config["full_candidate_fold_non_decrease_count"]}/5 folds',
            gate_status="FAIL (+0.01 gate)",
            evidence_role="split sensitivity",
            sources=[confirm_summary, confirm_config_path],
        )
    )

    local_summary = (
        "results/ncrdlg-localgl-scaffold-resampling-sensitivity-20261020/"
        "aggregate/mi_summary.csv"
    )
    local_config_path = (
        "results/ncrdlg-localgl-scaffold-resampling-sensitivity-20261020/"
        "aggregate/mi_config.json"
    )
    local_config = _json(root, local_config_path)
    local_ci = local_config["candidate_minus_localgl_bootstrap_95"]
    rows.append(
        _row(
            comparison_id="mi_scaffold_candidate_vs_localgl",
            dataset="Mi",
            protocol="same 5-fold scaffold-disjoint full-candidate",
            candidate="ChemBERTa pairwise prior-residual",
            baseline="ncRD-LG LocalGL dynamic-resampling adaptation",
            candidate_ap=chem_ap,
            baseline_ap=_model_mean(root, local_summary, "ncrdlg_localgl"),
            delta=local_config["candidate_minus_localgl"],
            ci=(local_ci["low"], local_ci["high"]),
            non_decrease=f'{local_config["candidate_vs_localgl_fold_non_decrease"]}/5 folds',
            gate_status="PASS public-baseline gate",
            evidence_role="main protocol comparison",
            sources=[chem_summary, local_summary, local_config_path],
        )
    )

    schemnet_path = "results/schemnet-strict-scaffold-baseline-20261020/summary.json"
    schemnet = _json(root, schemnet_path)
    schemnet_cmp = schemnet["strong_candidate_vs_schemnet"]
    rows.append(
        _row(
            comparison_id="mi_scaffold_candidate_vs_schemnet_no_seq",
            dataset="Mi",
            protocol="same 5-fold scaffold-disjoint full-candidate; 3 training seeds",
            candidate="ChemBERTa pairwise prior-residual",
            baseline="sChemNET no-sequence MACCS adaptation",
            candidate_ap=schemnet["macro_ap"]["prior_preserving_pairwise_residual"],
            baseline_ap=schemnet["macro_ap"]["schemnet_no_seq_maccs"],
            delta=schemnet_cmp["delta"],
            ci=(
                schemnet_cmp["scaffold_bootstrap_95"][0],
                schemnet_cmp["scaffold_bootstrap_95"][2],
            ),
            non_decrease=f'{schemnet_cmp["fold_non_decrease_count"]}/5 folds',
            gate_status="PASS direct-baseline gate",
            evidence_role="direct structural-baseline comparison",
            sources=[schemnet_path],
        )
    )

    plmf_path = "results/plmf-mda-strict-scaffold-baseline-20261020/summary.json"
    plmf = _json(root, plmf_path)
    plmf_cmp = plmf["strong_candidate_vs_plmf"]
    rows.append(
        _row(
            comparison_id="mi_scaffold_candidate_vs_plmf_mda",
            dataset="Mi",
            protocol="same 5-fold scaffold-disjoint full-candidate; 3 training seeds",
            candidate="ChemBERTa pairwise prior-residual",
            baseline="PLMF-MDA independent strict adaptation",
            candidate_ap=plmf["macro_ap"]["prior_preserving_pairwise_residual"],
            baseline_ap=plmf["macro_ap"]["plmf_mda_strict_adapter"],
            delta=plmf_cmp["delta"],
            ci=(
                plmf_cmp["scaffold_bootstrap_95"][0],
                plmf_cmp["scaffold_bootstrap_95"][2],
            ),
            non_decrease=f'{plmf_cmp["fold_non_decrease_count"]}/5 folds',
            gate_status="PASS direct-baseline gate",
            evidence_role="direct language-model baseline comparison",
            sources=[plmf_path],
        )
    )

    hmvcc_config_path = "results/hmvcc-drug-cold-confirmation-20261019/combined_config.json"
    hmvcc_config = _json(root, hmvcc_config_path)
    for dataset, summary, role in (
        (
            "ncRNADrug",
            "results/hmvcc-drug-cold-confirmation-20261019/ncRNADrug_full_candidate_summary.csv",
            "overlap-sensitive external result",
        ),
        (
            "NoncoRNA",
            "results/hmvcc-drug-cold-confirmation-20261019/NoncoRNA_full_candidate_summary.csv",
            "external boundary",
        ),
    ):
        result = _dataset_result(hmvcc_config, dataset)
        ci = result["full_candidate_bootstrap_95"]
        rows.append(
            _row(
                comparison_id=f"{dataset.lower()}_drug_cold_vs_prior",
                dataset=dataset,
                protocol=result["split_protocol"] + " full-candidate",
                candidate="RNA-FM + ECFP pairwise prior-residual",
                baseline="RNA prior",
                candidate_ap=_model_mean(root, summary, "prior_preserving_pairwise_residual"),
                baseline_ap=_model_mean(root, summary, "rna_prior_only"),
                delta=result["full_candidate_macro_ap_delta"],
                ci=(ci["low"], ci["high"]),
                non_decrease=f'{result["full_candidate_fold_non_decrease_count"]}/5 folds',
                gate_status="PASS" if result["dataset_gate_passed"] else "FAIL",
                evidence_role=role,
                sources=[summary, hmvcc_config_path],
            )
        )

    deoverlap_summary = "results/hmvcc-mi-deoverlap-confirmation-20261019/ncRNADrug_mi_deoverlap_full_candidate_summary.csv"
    deoverlap_config_path = "results/hmvcc-mi-deoverlap-confirmation-20261019/combined_config.json"
    deoverlap = _dataset_result(_json(root, deoverlap_config_path), "ncRNADrug_mi_deoverlap")
    deoverlap_ci = deoverlap["full_candidate_bootstrap_95"]
    rows.append(
        _row(
            comparison_id="ncrnadrug_entity_deoverlap_vs_prior",
            dataset="ncRNADrug minus Mi-name-overlap entities",
            protocol=deoverlap["split_protocol"] + " full-candidate",
            candidate="RNA-FM + ECFP pairwise prior-residual",
            baseline="RNA prior",
            candidate_ap=_model_mean(root, deoverlap_summary, "prior_preserving_pairwise_residual"),
            baseline_ap=_model_mean(root, deoverlap_summary, "rna_prior_only"),
            delta=deoverlap["full_candidate_macro_ap_delta"],
            ci=(deoverlap_ci["low"], deoverlap_ci["high"]),
            non_decrease=f'{deoverlap["full_candidate_fold_non_decrease_count"]}/5 folds',
            gate_status="FAIL",
            evidence_role="main overlap audit",
            sources=[deoverlap_summary, deoverlap_config_path],
        )
    )

    sm_summary = "results/sm2mir-virgin-drug-temporal-20261019/summary.csv"
    sm_config_path = "results/sm2mir-virgin-drug-temporal-20261019/config.json"
    sm_config = _json(root, sm_config_path)
    sm_ci = sm_config["full_candidate_bootstrap_95"]
    rows.append(
        _row(
            comparison_id="sm2mir_virgin_drug_temporal_vs_prior",
            dataset="SM2miR non-Mi CIDs",
            protocol="2011-2014 first-seen drug temporal mini-holdout",
            candidate="ECFP pairwise prior-residual",
            baseline="RNA prior",
            candidate_ap=_model_mean(root, sm_summary, "prior_preserving_pairwise_residual"),
            baseline_ap=_model_mean(root, sm_summary, "rna_prior_only"),
            delta=sm_config["full_candidate_macro_ap_delta"],
            ci=(sm_ci["low"], sm_ci["high"]),
            non_decrease=f'{sm_config["test_drug_non_decrease_count"]}/{sm_config["test_drug_count"]} drugs',
            gate_status="FAIL",
            evidence_role="independent-label boundary",
            sources=[sm_summary, sm_config_path],
        )
    )

    rahgl_drug_path = "results/rahgl-objective-alignment-confirmation-20261020/summary.json"
    rahgl_drug = _json(root, rahgl_drug_path)
    rahgl_drug_cmp = rahgl_drug["entity_balanced_vs_rna_prior"]
    rows.append(
        _row(
            comparison_id="rahgl_fixed_drug_cold_vs_prior",
            dataset="RAHGL-MDR",
            protocol="author fixed drug-cold folds; 3 training seeds",
            candidate="entity-balanced pairwise prior-residual",
            baseline="RNA prior",
            candidate_ap=rahgl_drug["macro_ap"]["entity_balanced_pairwise_residual"],
            baseline_ap=rahgl_drug["macro_ap"]["rna_prior_only"],
            delta=rahgl_drug_cmp["delta"],
            ci=(rahgl_drug_cmp["bootstrap_95_low"], rahgl_drug_cmp["bootstrap_95_high"]),
            non_decrease=f'{rahgl_drug_cmp["fold_non_decrease_count"]}/5 folds',
            gate_status="PASS drug-cold gate",
            evidence_role="split-limited positive result",
            sources=[rahgl_drug_path],
        )
    )

    rahgl_scaffold_path = "results/rahgl-scaffold-cold-confirmation-20261020/summary.json"
    rahgl_scaffold = _json(root, rahgl_scaffold_path)
    rahgl_scaffold_cmp = rahgl_scaffold["entity_vs_prior"]
    rows.append(
        _row(
            comparison_id="rahgl_scaffold_cold_vs_prior",
            dataset="RAHGL-MDR",
            protocol="5-fold scaffold-disjoint; 3 training seeds",
            candidate="entity-balanced pairwise prior-residual",
            baseline="RNA prior",
            candidate_ap=rahgl_scaffold["macro_ap"]["entity_balanced_pairwise_residual"],
            baseline_ap=rahgl_scaffold["macro_ap"]["rna_prior_only"],
            delta=rahgl_scaffold_cmp["delta"],
            ci=(rahgl_scaffold_cmp["scaffold_bootstrap_95"][0], rahgl_scaffold_cmp["scaffold_bootstrap_95"][2]),
            non_decrease=f'{rahgl_scaffold_cmp["fold_non_decrease_count"]}/5 folds',
            gate_status="FAIL",
            evidence_role="main split-dependence audit",
            sources=[rahgl_scaffold_path],
        )
    )

    replication_path = "results/independent-source-replication-pilot-20261020/summary.json"
    replication = _json(root, replication_path)
    for baseline_key, baseline_name, role in (
        ("replicated_rna_prior", "replicated-pair frequency prior", "within-target positive control"),
        ("reported_rna_prior", "all-reported RNA prior", "main selection-process audit"),
    ):
        comparison = replication["comparisons"][baseline_key]
        rows.append(
            _row(
                comparison_id=f"pmid_replication_vs_{baseline_key}",
                dataset="Mi pairs with distinct-PMID support",
                protocol="5-fold scaffold-disjoint replication target",
                candidate="replication-label ECFP pairwise residual",
                baseline=baseline_name,
                candidate_ap=replication["macro_ap"]["replication_pairwise_residual"],
                baseline_ap=replication["macro_ap"][baseline_key],
                delta=comparison["delta"],
                ci=(comparison["scaffold_bootstrap_95"][0], comparison["scaffold_bootstrap_95"][2]),
                non_decrease=f'{comparison["fold_non_decrease_count"]}/5 folds',
                gate_status="SUBTARGET PASS" if baseline_key == "replicated_rna_prior" else "OVERALL FAIL",
                evidence_role=role,
                sources=[replication_path],
            )
        )

    frame = pd.DataFrame(rows)
    validate_main_results(frame)
    return frame


def validate_main_results(frame: pd.DataFrame) -> None:
    if frame["comparison_id"].duplicated().any():
        raise ValueError("comparison_id 必须唯一")
    calculated = frame["candidate_ap"] - frame["baseline_ap"]
    if not ((calculated - frame["delta"]).abs() < 1e-9).all():
        bad = frame.loc[(calculated - frame["delta"]).abs() >= 1e-9, "comparison_id"].tolist()
        raise ValueError(f"候选与基线均值无法复算 delta: {bad}")
    if not (frame["ci_low"] <= frame["ci_high"]).all():
        raise ValueError("置信区间上下界顺序错误")


def to_markdown(frame: pd.DataFrame) -> str:
    lines = [
        "# 投稿主结果证据表",
        "",
        "> 本表由 `paper_evidence_matrix.py` 从冻结结果自动生成；AP 为 full-candidate drug-macro average precision。PASS 只指对应预注册局部门，不等于论文或算法整体通过。",
        "",
        "| ID | 数据与协议 | 候选 vs 基线 | AP | ΔAP（95% CI） | 方向 | 门 | 论文角色 |",
        "|---|---|---|---:|---:|---:|---|---|",
    ]
    for row in frame.itertuples(index=False):
        lines.append(
            f"| `{row.comparison_id}` | {row.dataset}; {row.protocol} | {row.candidate} vs {row.baseline} | "
            f"{row.candidate_ap:.6f} vs {row.baseline_ap:.6f} | {row.delta:+.6f} "
            f"[{row.ci_low:+.6f}, {row.ci_high:+.6f}] | {row.non_decrease} | "
            f"{row.gate_status} | {row.evidence_role} |"
        )
    lines.extend(
        [
            "",
            "## 读取边界",
            "",
            "- `PASS public-baseline gate`：只支持候选优于本研究严格适配的 LocalGL；不支持优于 RNA prior 或算法新颖性。",
            "- `PASS direct-baseline gate`：只支持候选优于本研究独立重实现的 sChemNET 无序列消融；不支持优于完整 sChemNET、RNA prior 或 SOTA。",
            "- `PASS drug-cold gate`：在作者固定 drug-cold 折成立；同一候选在 scaffold-disjoint 中失败，不能外推为结构泛化。",
            "- `SUBTARGET PASS`：只说明稀疏复现标签内部存在结构信号；相对全部报道 prior 的整体门失败。",
            "- 所有来源文件逐行保存在 CSV 的 `sources` 列，便于复算和审稿核验。",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--output-dir", type=Path, default=ROOT / "paper")
    args = parser.parse_args()
    frame = collect_main_results(args.root)
    args.output_dir.mkdir(parents=True, exist_ok=True)
    frame.to_csv(args.output_dir / "main_results.csv", index=False)
    (args.output_dir / "main_results.md").write_text(to_markdown(frame), encoding="utf-8")
    print(f"wrote {len(frame)} comparisons to {args.output_dir}")


if __name__ == "__main__":
    main()
