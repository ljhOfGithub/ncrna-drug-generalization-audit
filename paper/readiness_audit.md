# Benchmark paper readiness audit

## Verdict

**结果已冻结，双语事实稿、可编译投稿工程、双许可证和 clean-room 证据包已完成；尚不能直接投稿。** 条件性主线已经固定，不再以新增实验换取更强结论。英文摘要、Highlights、Cover Letter、10 篇直接相关引文审计和单栏 LaTeX 工程已完成。当前实质阻断项是作者对基金与利益冲突的确认；永久归档 DOI 尚未分配，但不得把 GitHub tag 冒充 DOI。

## Critical issues

1. **Versioned public evidence package prepared.** A 93-file SHA-256 portable evidence-package scope, data card, third-party boundary, maintenance plan, manuscript/submission source files, claim audit, core reproduction command, and manifest exist. The manifest-only v11 directory rebuilt the 13-row main table and main figure, passed 14 rebuild tests, 22 package tests, and all 93 hashes. Statistics/case tables that require excluded third-party material remain hash-verified unless an explicit flag is used. The public repository and `v0.1.1` target are fixed; final tag/release verification is recorded separately.
2. **英文稿已形成，但仍需作者终审。** `manuscript_en.md` 与 `submission-pattern-recognition/main.tex` 已保持冻结数字和条件性主张，主稿与 Cover Letter 均通过内置编译。作者身份、公开链接和许可证已记录；仍待基金、利益冲突、原创性和未一稿多投确认。当前 10 篇直接相关文献已核验，相关工作仍偏窄，但未核实到期刊官方存在“35--55 篇”数量要求。

## Major issues

1. **Baseline fairness sensitivity completed.** Dynamic-resampling LocalGL changes AP from `0.152560` to `0.153275` (`+0.000715`, 95% CI `[-0.001093,+0.002555]`), below the preregistered `0.005` materiality threshold; the main table now uses the dynamic result. The comparison remains implementation-specific rather than universal.
2. **Model coverage remains qualified.** `public_method_coverage.md` / `.csv` now enumerate each verified public family, evidence tier, exact strict-protocol adaptation, observed result, and reason for non-comparability. PLMF-MDA's independent strict adapter completed all `15/15` formal units and passed its direct-baseline gate. Coverage is still incomplete because the full sequence-aware sChemNET was not triggered by its preregistered rule, RAHGL-MDR lacks released training code, and MGCNA/GCFMCL have not been rerun on the common endpoint.
3. **Licensing boundary resolved for the public package.** The package excludes third-party raw material and upstream ncRD-LG code. Rights-clear independent code uses MIT; original manuscript, figures, and documentation use CC BY 4.0. This does not license upstream or third-party material.
4. **Historical method-selection bias cannot be removed by the current confidence intervals.** The manuscript must foreground this limitation and avoid interpreting Mi bootstrap intervals as untouched confirmation.

## Minor issues

1. 工作标题已改为与条件性主线一致的 *When Gains under Drug-Cold Evaluation Do Not Persist under Scaffold Separation*；尚未做冻结后标题碰撞终查，因此不能声称标题唯一。
2. `Pattern Recognition` 是当前工作目标；英文正文、方括号顺序编号、218 词摘要、6 个关键词和 5 条合规 Highlights 已落盘。当前 7 篇引用仍低于期刊建议覆盖。
3. `runtime_hardware.md` / `.csv` now record the exact machine class and complete LocalGL per-fold wall-clock values. RAHGL clean-run timing and an end-to-end reproduction time remain unmeasured.

## Checklist status

| Category | Complete | Partial | Missing |
|---|---|---|---|
| Introduction | evaluation gap, three RQs, contributions, concrete headline numbers, evaluation-ladder figure, five-full-text-work protocol comparison | design rationale, narrative sequence | full prose |
| Benchmark section | G1–G5, scope, taxonomy, metrics, deterministic pipeline, seven-row dataset/protocol statistics table, self-contained pipeline figure | quality control and some coverage details distributed across logs | data examples |
| Experiments | headline table, fine-grained split/overlap/source analyses, four Finding statements, uncertainty, three rule-selected split-sensitivity cases | public-model coverage, research-opportunity synthesis | finalized cross-model comparison |
| Structure/release | limitations, provenance sources, hashes, tests, reproducibility boundary, data card, third-party policy, maintenance plan, single-command artifact rebuild | related work, appendix plan, release scope | clean checkout/tag, license selection, hosting, venue format |

## Shortest credible path

1. 在不吸收三个既有 tracked 修改的前提下形成干净提交/归档，并从干净 checkout 重建主表与图。
2. 解决新增代码许可证、作者/单位/基金/利益冲突/CRediT、最终数据与代码 URL。
3. 补齐并核验相关工作、确认作者与声明字段，完成最终页数和投稿前评审。

## Completed supporting artifacts

- `dataset_protocol_stats.md` / `.csv`: seven aligned resources with entity, positive-pair, scaffold, provenance-field, and benchmark-role counts.
- `rahgl_split_case_studies.md` / `.csv`: three post hoc explanatory cases, selected deterministically as the largest protocol-induced delta-AP drop inside prespecified positive-count strata. These cases are descriptive, not inferential evidence.
- `../figures/evaluation-ladder.mmd` / `.md` / `.svg` / `.pdf` / `.png`: syntax-verified and visually reviewed protocol/evidence ladder with a separate Chinese caption.
- `verified_neighbor_comparison.md` / `.csv`: five full-text-verified near-neighbor protocols plus the bounded provisional gap; author-reported metrics are not pooled across incompatible candidate spaces.
- `public_method_coverage.md` / `.csv`: seven public method families separated into author-model adaptations, independent ablations, diagnostic baselines, and verified-but-unadapted coverage boundaries.
- `runtime_hardware.md` / `.csv`: privacy-safe hardware specification, observed test/smoke/failed-run wall-clock values, and explicit missing timing boundaries.
- `venue_eligibility.md`: 2026-10-20 official-directory attempt and per-journal `official_partition_unverified` boundary; no third-party partition is promoted to evidence.
- `candidate_failure_map.md` / `.csv`: complete 58/58 pilot-design index with typed run state and stop decision; a test rejects missing, duplicate, or extra mappings.
- `../release/`: portable evidence-package definition with SHA-256 manifest, data card, third-party boundary, maintenance plan, bilingual manuscript/submission sources, citation/claim audits, and a clean-room verified core rebuild command. This is not yet a committed public release.
