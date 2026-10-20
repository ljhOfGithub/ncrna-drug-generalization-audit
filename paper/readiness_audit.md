# Benchmark paper readiness audit

## Verdict

**结果已冻结，双语事实稿、可编译投稿工程、作者声明、双许可证和 clean-room 证据包均已完成，已具备技术上传条件。** 条件性主线已经固定，不再以新增实验换取更强结论。英文摘要、Highlights、Cover Letter、35 篇引文审计和单栏 LaTeX 工程已完成。作者已确认无专项基金、无利益冲突、稿件原创、未一稿多投并同意投稿。上传前仍需按期刊单盲流程保留实名稿并通读最终 PDF；永久归档 DOI 尚未分配，但不是本轮技术打包阻断项，也不得把 GitHub tag 冒充 DOI。

## Critical issues

1. **Versioned public evidence package prepared.** A SHA-256 portable evidence-package scope, data card, third-party boundary, maintenance plan, manuscript/submission source files, claim audit, core reproduction command, and manifest exist. The clean package rebuilds the 13-row main table and main figure, passes the portable and package tests, and verifies every declared hash. Statistics/case tables that require excluded third-party material remain hash-verified unless an explicit flag is used. The public repository and `v0.1.3` release identify the frozen package; the GitHub tag is not represented as an archival DOI.
2. **英文稿已形成，声明占位符已清除。** `manuscript_en.md` 与 `submission-pattern-recognition/main.tex` 保持冻结数字和条件性主张，主稿与 Cover Letter 均通过内置编译。作者身份、公开链接、许可证、基金、利益冲突、原创性和未一稿多投声明均已记录。当前 35 篇文献均已核对元数据、使用位置和主张边界；其中 32 篇完成全文或权威完整来源核验，3 篇按合格的部分来源边界记录。期刊作者指南请求 35--55 篇，本稿达到下限；Overleaf 云端终稿为 25 页，位于 20--35 页范围内。

## Major issues

1. **Baseline fairness sensitivity completed.** Dynamic-resampling LocalGL changes AP from `0.152560` to `0.153275` (`+0.000715`, 95% CI `[-0.001093,+0.002555]`), below the preregistered `0.005` materiality threshold; the main table now uses the dynamic result. The comparison remains implementation-specific rather than universal.
2. **Model coverage remains qualified.** `public_method_coverage.md` / `.csv` now enumerate each verified public family, evidence tier, exact strict-protocol adaptation, observed result, and reason for non-comparability. PLMF-MDA's independent strict adapter completed all `15/15` formal units and passed its direct-baseline gate. Coverage is still incomplete because the full sequence-aware sChemNET was not triggered by its preregistered rule, RAHGL-MDR lacks released training code, and MGCNA/GCFMCL have not been rerun on the common endpoint.
3. **Licensing boundary resolved for the public package.** The package excludes third-party raw material and upstream ncRD-LG code. Rights-clear independent code uses MIT; original manuscript, figures, and documentation use CC BY 4.0. This does not license upstream or third-party material.
4. **Historical method-selection bias cannot be removed by the current confidence intervals.** The manuscript must foreground this limitation and avoid interpreting Mi bootstrap intervals as untouched confirmation.

## Minor issues

1. 工作标题已改为与条件性主线一致的 *Drug-Cold Gains Do Not Persist under Scaffold Separation in ncRNA--Drug Prediction*；尚未做冻结后标题碰撞终查，因此不能声称标题唯一。
2. `Pattern Recognition` 是当前工作目标；英文正文、方括号顺序编号、218 词摘要、6 个关键词和 5 条合规 Highlights 已落盘。当前 35 篇引用覆盖直接近邻、RNA/小分子表示、冷启动、局部子图、排序评估和数据溯源；正文仍明确区分直接近邻与方法学背景。
3. `runtime_hardware.md` / `.csv` now record the exact machine class and complete LocalGL per-fold wall-clock values. RAHGL clean-run timing and an end-to-end reproduction time remain unmeasured.

## Checklist status

| Category | Complete | Partial | Missing |
|---|---|---|---|
| Introduction | evaluation gap, contributions, concrete headline numbers, evaluation-ladder figure, protocol comparison | broader related-work coverage | none within the frozen claim |
| Benchmark section | scope, taxonomy, metrics, deterministic pipeline, seven-row dataset/protocol statistics table, self-contained pipeline figure | some coverage details remain in supplements | none within the portable scope |
| Experiments | headline table, fine-grained split/overlap/source analyses, uncertainty, rule-selected split-sensitivity cases | public-model coverage remains qualified | no prospective biological validation |
| Structure/release | limitations, provenance, hashes, tests, reproducibility boundary, data card, third-party policy, maintenance plan, licenses, public repository and versioned release | final submission-system fields and optional archival DOI | none for technical upload |

## 投稿前剩余动作

1. 作者通读 Overleaf 生成的最终 PDF，确认标题、作者信息、声明和分页。
2. 按期刊当前单盲流程使用实名稿，并在投稿系统填写作者与声明字段。
3. 若后续取得永久归档 DOI，再替换“尚未分配”的诚实边界；在此之前保留 GitHub `v0.1.3` 链接。

## Completed supporting artifacts

- `dataset_protocol_stats.md` / `.csv`: seven aligned resources with entity, positive-pair, scaffold, provenance-field, and benchmark-role counts.
- `rahgl_split_case_studies.md` / `.csv`: three post hoc explanatory cases, selected deterministically as the largest protocol-induced delta-AP drop inside prespecified positive-count strata. These cases are descriptive, not inferential evidence.
- `../figures/evaluation-ladder.mmd` / `.md` / `.svg` / `.pdf` / `.png`: syntax-verified and visually reviewed protocol/evidence ladder with a separate Chinese caption.
- `verified_neighbor_comparison.md` / `.csv`: five full-text-verified near-neighbor protocols plus the bounded provisional gap; author-reported metrics are not pooled across incompatible candidate spaces.
- `public_method_coverage.md` / `.csv`: seven public method families separated into author-model adaptations, independent ablations, diagnostic baselines, and verified-but-unadapted coverage boundaries.
- `runtime_hardware.md` / `.csv`: privacy-safe hardware specification, observed test/smoke/failed-run wall-clock values, and explicit missing timing boundaries.
- `venue_eligibility.md`: 2026-10-20 official-directory attempt and per-journal `official_partition_unverified` boundary; no third-party partition is promoted to evidence.
- `candidate_failure_map.md` / `.csv`: complete 58/58 pilot-design index with typed run state and stop decision; a test rejects missing, duplicate, or extra mappings.
- `../release/`: portable evidence-package definition with SHA-256 manifest, data card, third-party boundary, maintenance plan, bilingual manuscript/submission sources, citation/claim audits, and a clean-room verified core rebuild command, published as `v0.1.3` without redistributing excluded third-party material.
