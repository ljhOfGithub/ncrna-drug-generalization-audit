from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MMD = ROOT / "figures" / "evaluation-ladder.mmd"
WRAPPER = ROOT / "figures" / "evaluation-ladder.md"


def test_markdown_embeds_exact_mermaid_source():
    source = MMD.read_text(encoding="utf-8").strip()
    wrapper = WRAPPER.read_text(encoding="utf-8")
    embedded = wrapper.split("```mermaid\n", 1)[1].split("\n```", 1)[0].strip()
    assert embedded == source


def test_required_gates_and_controls_are_present():
    source = MMD.read_text(encoding="utf-8")
    for label in (
        "随机配对",
        "药物冷启动",
        "骨架隔离",
        "实体去重",
        "时间外推",
        "来源复现",
        "RNA 频率强先验",
        "full-candidate drug-macro AP",
    ):
        assert label in source


def test_evidence_gates_are_parallel_not_sequential():
    source = MMD.read_text(encoding="utf-8")
    assert "overlap --> temporal" in source
    assert "overlap --> source" in source
    assert "temporal --> source" not in source
    assert "source --> temporal" not in source
