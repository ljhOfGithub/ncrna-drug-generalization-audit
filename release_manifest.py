from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

from reproduce_paper_artifacts import ARTIFACT_TESTS, EXPECTED_OUTPUTS, REQUIRED_INPUTS


ROOT = Path(__file__).resolve().parent
DEFAULT_OUTPUT = ROOT / "release" / "manifest.json"

RELEASE_FILES = tuple(
    dict.fromkeys(
        (
            "requirements-audit.txt",
            "reproduce_paper_artifacts.py",
            "release_manifest.py",
            "paper_evidence_matrix.py",
            "build_paper_diagnostics.py",
            "rna_frequency_stratum_audit.py",
            "tests/test_rna_frequency_stratum_audit.py",
            "docs/rna-frequency-stratum-audit-design.md",
            "results/rna-frequency-stratum-audit-20261020/config.json",
            "results/rna-frequency-stratum-audit-20261020/fold_metrics.csv",
            "results/rna-frequency-stratum-audit-20261020/summary.csv",
            "figures/gen_fig_conclusion_reversals.py",
            "figures/fig_conclusion_reversals_caption.md",
            "figures/evaluation-ladder.mmd",
            "figures/evaluation-ladder.md",
            "figures/evaluation-ladder-caption.md",
            "figures/evaluation-ladder.pdf",
            "figures/evaluation-ladder.svg",
            "figures/evaluation-ladder.png",
            "paper/reproducibility.md",
            "paper/result_freeze_record.md",
            "paper/manuscript_zh_cn.md",
            "paper/manuscript_en.md",
            "paper/highlights_zh_cn.md",
            "paper/highlights_en.txt",
            "paper/cover_letter_zh_cn.md",
            "paper/cover_letter_en.md",
            "paper/author_metadata.md",
            "paper/references_verified.bib",
            "paper/CITATION_AUDIT.md",
            "paper/CITATION_AUDIT.json",
            "paper/release_license_decision.md",
            "paper/venue_fit_pattern_recognition.md",
            "paper/paper_configuration_record.md",
            "paper/readiness_audit.md",
            "paper/related_work_matrix.md",
            "paper/pattern_recognition_cover_letter_evidence.md",
            "paper/submission_checklist.md",
            "paper/PAPER_CLAIM_AUDIT.md",
            "paper/PAPER_CLAIM_AUDIT.json",
            "paper/verified_neighbor_comparison.csv",
            "paper/verified_neighbor_comparison.md",
            "paper/public_method_coverage.csv",
            "paper/public_method_coverage.md",
            "paper/runtime_hardware.csv",
            "paper/runtime_hardware.md",
            "paper/candidate_failure_map.csv",
            "paper/candidate_failure_map.md",
            "tests/test_submission_package.py",
            "paper/venue_eligibility.md",
            "release/README.md",
            "release/DATA_CARD.md",
            "release/LICENSE-CODE",
            "release/LICENSE-DOCUMENTATION",
            "release/THIRD_PARTY.md",
            "release/MAINTENANCE.md",
            "submission-pattern-recognition/main.tex",
            "submission-pattern-recognition/references.bib",
            "submission-pattern-recognition/highlights.txt",
            "submission-pattern-recognition/cover_letter.tex",
            "submission-pattern-recognition/README.md",
            "submission-pattern-recognition/figures/evaluation-ladder.pdf",
            "submission-pattern-recognition/figures/fig_conclusion_reversals.pdf",
            *ARTIFACT_TESTS,
            *REQUIRED_INPUTS,
            *EXPECTED_OUTPUTS,
        )
    )
)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def build_manifest() -> dict[str, object]:
    missing = [name for name in RELEASE_FILES if not (ROOT / name).is_file()]
    if missing:
        raise FileNotFoundError("缺少 release 文件：\n" + "\n".join(missing))
    files = []
    for name in RELEASE_FILES:
        path = ROOT / name
        files.append({"path": name, "bytes": path.stat().st_size, "sha256": sha256(path)})
    return {
        "schema_version": 1,
        "scope": "paper-evidence-artifacts-not-full-training-release",
        "file_count": len(files),
        "files": files,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="生成或核验论文证据包的 SHA-256 清单。")
    parser.add_argument("--write", action="store_true", help="将当前清单写入 release/manifest.json。")
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()

    manifest = build_manifest()
    rendered = json.dumps(manifest, ensure_ascii=False, indent=2) + "\n"
    output = args.output if args.output.is_absolute() else ROOT / args.output
    if args.write:
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(rendered, encoding="utf-8")
        print(f"已写入 {output.relative_to(ROOT)}：{manifest['file_count']} 个文件")
        return
    if not output.is_file():
        raise FileNotFoundError(f"清单不存在：{output}")
    if output.read_text(encoding="utf-8") != rendered:
        raise RuntimeError("release/manifest.json 与当前文件不一致；请审查后使用 --write 更新。")
    print(f"清单核验通过：{manifest['file_count']} 个文件")


if __name__ == "__main__":
    main()
