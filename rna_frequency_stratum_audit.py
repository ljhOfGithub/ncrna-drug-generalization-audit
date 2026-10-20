"""审计冻结 OOF 预测在训练期 RNA 频率层级上的信息增量。"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.metrics import average_precision_score

KEYS = ["fold", "rna_id", "drug_id", "label"]


def frequency_stratum(degree: int) -> str:
    if degree < 0:
        raise ValueError("RNA degree 不能为负")
    if degree == 0:
        return "zero"
    if degree <= 2:
        return "low_1_2"
    if degree <= 9:
        return "mid_3_9"
    return "high_ge_10"


def align_predictions(
    frame: pd.DataFrame,
    candidate_model: str,
    baseline_model: str,
) -> pd.DataFrame:
    required = set(KEYS + ["model", "probability"])
    missing = required.difference(frame.columns)
    if missing:
        raise ValueError(f"预测文件缺列: {sorted(missing)}")
    if frame.duplicated(KEYS + ["model"]).any():
        raise ValueError("同一 pair/model 出现重复行")
    selected = frame[frame["model"].isin([candidate_model, baseline_model])]
    wide = selected.pivot(index=KEYS, columns="model", values="probability").reset_index()
    if len(wide) * 2 != len(selected):
        raise ValueError("候选与基线 pair 未严格一一对齐")
    if wide[[candidate_model, baseline_model]].isna().any().any():
        raise ValueError("候选与基线存在缺失预测")
    return wide.rename(
        columns={candidate_model: "candidate_probability", baseline_model: "baseline_probability"}
    )


def stratum_metrics(frame: pd.DataFrame) -> dict[str, float | int | str]:
    labels = frame["label"].to_numpy(dtype=np.int64)
    if set(np.unique(labels)) != {0, 1}:
        raise ValueError("每个层级必须同时含正例与 sampled-unlabeled")
    candidate = frame["candidate_probability"].to_numpy(dtype=np.float64)
    baseline = frame["baseline_probability"].to_numpy(dtype=np.float64)
    residual = candidate - baseline
    positive = labels == 1
    unknown = ~positive
    candidate_ap = average_precision_score(labels, candidate)
    baseline_ap = average_precision_score(labels, baseline)
    return {
        "positive_count": int(positive.sum()),
        "sampled_unlabeled_count": int(unknown.sum()),
        "candidate_balanced_ap": float(candidate_ap),
        "baseline_balanced_ap": float(baseline_ap),
        "delta_balanced_ap": float(candidate_ap - baseline_ap),
        "mean_positive_residual": float(residual[positive].mean()),
        "mean_unlabeled_residual": float(residual[unknown].mean()),
        "residual_separation": float(residual[positive].mean() - residual[unknown].mean()),
        "positive_residual_gt_zero_fraction": float((residual[positive] > 0).mean()),
        "unlabeled_residual_gt_zero_fraction": float((residual[unknown] > 0).mean()),
    }


def audit(
    predictions: pd.DataFrame,
    dataset_dir: Path,
    split_seed: int,
    folds: int,
    candidate_model: str,
    baseline_model: str,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    # The clean public evidence package exercises the pure alignment/metric helpers
    # without redistributing the upstream-data loader. Load it only for the optional
    # third-party diagnostic path that actually needs the original dataset.
    from generalization_audit import load_bundle, load_drug_scaffolds, scaffold_cv_split

    bundle = load_bundle(dataset_dir, "Mi")
    scaffolds = load_drug_scaffolds(dataset_dir, "Mi")
    aligned = align_predictions(predictions, candidate_model, baseline_model)
    enriched = []
    for fold in range(folds):
        split = scaffold_cv_split(bundle, scaffolds, fold=fold, n_folds=folds, seed=split_seed)
        degrees = split.train_positive_matrix.sum(axis=1).astype(np.int64)
        part = aligned[aligned["fold"] == fold].copy()
        if part.empty:
            raise ValueError(f"预测文件缺少 fold {fold}")
        part["train_rna_degree"] = degrees[part["rna_id"].to_numpy(dtype=np.int64)]
        part["stratum"] = [frequency_stratum(int(value)) for value in part["train_rna_degree"]]
        enriched.append(part)
    scored = pd.concat(enriched, ignore_index=True)

    fold_rows = []
    for (fold, stratum), group in scored.groupby(["fold", "stratum"], sort=True):
        row = {"fold": int(fold), "stratum": stratum}
        row.update(stratum_metrics(group))
        fold_rows.append(row)
    fold_metrics = pd.DataFrame(fold_rows)

    summary_rows = []
    total_positives = int((scored["label"] == 1).sum())
    for stratum, group in scored.groupby("stratum", sort=True):
        row = {"stratum": stratum}
        row.update(stratum_metrics(group))
        positive_count = int((group["label"] == 1).sum())
        deltas = fold_metrics.loc[fold_metrics["stratum"] == stratum, "delta_balanced_ap"]
        row["positive_share"] = positive_count / total_positives
        row["fold_non_decrease_count"] = int((deltas >= 0).sum())
        row["fold_count"] = int(len(deltas))
        summary_rows.append(row)
    return pd.DataFrame(summary_rows), fold_metrics


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset-dir", type=Path, default=Path("Dataset"))
    parser.add_argument(
        "--predictions",
        type=Path,
        default=Path("results/chemberta-pairwise-residual-pilot-20261019/mi_oof_predictions.csv"),
    )
    parser.add_argument("--split-seed", type=int, default=20261019)
    parser.add_argument("--folds", type=int, default=5)
    parser.add_argument("--candidate-model", default="prior_preserving_pairwise_residual")
    parser.add_argument("--baseline-model", default="rna_prior_only")
    parser.add_argument(
        "--output-dir", type=Path, default=Path("results/rna-frequency-stratum-audit-20261020")
    )
    args = parser.parse_args()
    predictions = pd.read_csv(args.predictions)
    summary, fold_metrics = audit(
        predictions,
        args.dataset_dir,
        args.split_seed,
        args.folds,
        args.candidate_model,
        args.baseline_model,
    )
    args.output_dir.mkdir(parents=True, exist_ok=True)
    summary.to_csv(args.output_dir / "summary.csv", index=False)
    fold_metrics.to_csv(args.output_dir / "fold_metrics.csv", index=False)
    config = {
        "dataset_dir": str(args.dataset_dir),
        "predictions": str(args.predictions),
        "split_seed": args.split_seed,
        "folds": args.folds,
        "candidate_model": args.candidate_model,
        "baseline_model": args.baseline_model,
        "strata": {"zero": [0, 0], "low_1_2": [1, 2], "mid_3_9": [3, 9], "high_ge_10": [10, None]},
        "estimand": "balanced sampled-unlabeled OOF diagnostic; not full-candidate AP",
    }
    (args.output_dir / "config.json").write_text(
        json.dumps(config, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(summary.to_string(index=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
