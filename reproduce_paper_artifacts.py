from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent

REQUIRED_INPUTS = (
    "results/chemberta-pairwise-residual-pilot-20261019/mi_full_candidate_summary.csv",
    "results/chemberta-pairwise-residual-pilot-20261019/mi_config.json",
    "results/chemberta-pairwise-residual-confirmation-seed-20261020/mi_full_candidate_summary.csv",
    "results/chemberta-pairwise-residual-confirmation-seed-20261020/mi_config.json",
    "results/ncrdlg-localgl-scaffold-resampling-sensitivity-20261020/aggregate/mi_summary.csv",
    "results/ncrdlg-localgl-scaffold-resampling-sensitivity-20261020/aggregate/mi_config.json",
    "results/schemnet-strict-scaffold-baseline-20261020/summary.json",
    "results/plmf-mda-strict-scaffold-baseline-20261020/summary.json",
    "results/hmvcc-drug-cold-confirmation-20261019/ncRNADrug_full_candidate_summary.csv",
    "results/hmvcc-drug-cold-confirmation-20261019/combined_config.json",
    "results/hmvcc-drug-cold-confirmation-20261019/NoncoRNA_full_candidate_summary.csv",
    "results/hmvcc-mi-deoverlap-confirmation-20261019/ncRNADrug_mi_deoverlap_full_candidate_summary.csv",
    "results/hmvcc-mi-deoverlap-confirmation-20261019/combined_config.json",
    "results/sm2mir-virgin-drug-temporal-20261019/summary.csv",
    "results/sm2mir-virgin-drug-temporal-20261019/config.json",
    "results/rahgl-objective-alignment-confirmation-20261020/summary.json",
    "results/rahgl-scaffold-cold-confirmation-20261020/summary.json",
    "results/independent-source-replication-pilot-20261020/summary.json",
)

BUILD_STEPS = (
    "paper_evidence_matrix.py",
    "figures/gen_fig_conclusion_reversals.py",
)

THIRD_PARTY_BUILD_STEPS = ("build_paper_diagnostics.py",)

EXPECTED_OUTPUTS = (
    "paper/main_results.csv",
    "paper/main_results.md",
    "paper/dataset_protocol_stats.csv",
    "paper/dataset_protocol_stats.md",
    "paper/rahgl_split_case_studies.csv",
    "paper/rahgl_split_case_studies.md",
    "figures/fig_conclusion_reversals.pdf",
    "figures/fig_conclusion_reversals.png",
)

ARTIFACT_TESTS = (
    "tests/test_paper_evidence_matrix.py",
    "tests/test_conclusion_reversal_figure.py",
    "tests/test_evaluation_ladder_figure.py",
    "tests/test_verified_neighbor_comparison.py",
)

THIRD_PARTY_TESTS = ("tests/test_paper_diagnostics.py",)


def _missing(paths: tuple[str, ...]) -> list[str]:
    return [path for path in paths if not (ROOT / path).is_file()]


def validate_inputs() -> None:
    missing = _missing(REQUIRED_INPUTS)
    if missing:
        raise FileNotFoundError("缺少论文构建输入：\n" + "\n".join(missing))


def validate_outputs() -> None:
    missing = _missing(EXPECTED_OUTPUTS)
    if missing:
        raise FileNotFoundError("缺少论文构建输出：\n" + "\n".join(missing))


def run_command(command: list[str]) -> None:
    subprocess.run(command, cwd=ROOT, check=True)


def main() -> None:
    parser = argparse.ArgumentParser(description="重建并校验论文主表、诊断表和结论反转图。")
    parser.add_argument("--check-only", action="store_true", help="只检查冻结输入和现有输出是否齐全。")
    parser.add_argument("--skip-tests", action="store_true", help="重建后跳过论文工件专项测试。")
    parser.add_argument(
        "--with-third-party-diagnostics",
        action="store_true",
        help="在已合法取得 Dataset 和 RAHGL 缓存时，额外重建资源统计与案例表。",
    )
    args = parser.parse_args()

    validate_inputs()
    if not args.check_only:
        for script in BUILD_STEPS:
            run_command([sys.executable, script])
        if args.with_third_party_diagnostics:
            for script in THIRD_PARTY_BUILD_STEPS:
                run_command([sys.executable, script])
        if not args.skip_tests:
            tests = list(ARTIFACT_TESTS)
            if args.with_third_party_diagnostics:
                tests.extend(THIRD_PARTY_TESTS)
            run_command([sys.executable, "-m", "pytest", "-q", *tests])
    validate_outputs()
    print(
        f"论文工件检查通过：{len(REQUIRED_INPUTS)} 个冻结输入，"
        f"{len(EXPECTED_OUTPUTS)} 个声明输出；默认重建主表与主图，"
        "第三方依赖诊断表按显式开关重建。"
    )


if __name__ == "__main__":
    main()
