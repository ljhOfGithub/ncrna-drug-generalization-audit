# 五篇全文近邻的评估协议比较

本表只比较已在正式全文中核实的评估设计，不横向比较来自不同数据集、负例池和候选空间的绝对 AUC/AUPR。`未报告`表示所读正文与补充材料中没有该协议，不等同于证明作者从未做过。案例研究中的全候选排序不算作预先定义的 benchmark 评测。

| 工作 | 随机边/配对 | 实体冷启动 | 双冷 | 骨架隔离 | 完整候选 benchmark | 频率强先验 | 跨库实体去重 | 时间外推 | 独立来源复现 |
|---|---|---|---|---|---|---|---|---|---|
| ncRD-LG (2026) | 是 | 未报告 | 未报告 | 未报告 | 未报告 | 未报告 | 未报告 | 未报告 | 未报告 |
| RAHGL-MDR (2026) | 是 | miRNA / drug | 是 | 未报告 | 是 | degree/popularity | 未报告 | 未报告 | 未报告 |
| HMVCC (2027；online 2026) | 是 | drug | 未报告 | 未报告 | 未报告 | 未报告 | 未报告 | 未报告 | 未报告 |
| MGCNA (2025) | 是 | miRNA / drug | 是 | 未报告 | 未报告 | 未报告 | 未报告 | 未报告 | 未报告 |
| PLMF-MDA (2026) | 是 | miRNA / drug | 未报告 | 未报告 | 未报告 | 未报告 | 未报告 | 未报告 | 未报告 |
| 本研究（进行中） | 是 | drug / scaffold | 未纳入 | 是 | 是 | RNA 频率 | 是 | 是 | 不同 PMID |

## 逐篇核验边界

- **ncRD-LG：**出版商完整 HTML 读至结论；主协议为随机配对划分并为每个正例抽取一个负例，作者把 leave-drug、leave-ncRNA 与 scaffold split 列为未来工作。
- **RAHGL-MDR：**官方 30 页 PDF 读至 EOF，并核对固定提交的公开数据；覆盖 leakage-safe edge、miRNA-cold、drug-cold、double-cold、sampled-unlabeled 和 full-candidate ranking，且提供 degree/popularity 强基线。
- **HMVCC：**ScienceDirect 完整 HTML 读至参考文献边界；覆盖 edge split、跨物种、跨数据集无微调迁移、drug cold-start、四类负采样与消融，但未报告 scaffold 或强频率先验审计。
- **MGCNA：**PLOS 完整 HTML 与补充材料读至 EOF；覆盖平衡负采样的随机边五折，以及 miRNA-cold、drug-cold、double-cold。针对单个药物的案例研究对全部 miRNA 排序，但这不是 benchmark 主协议。
- **PLMF-MDA：**PLOS Version 2 完整 HTML 读至结论；分别建模 resistance 与 sensitivity，覆盖平衡负采样五折和 drug/miRNA cold。冷启动测试实体从中等频率区间选取，未覆盖骨架隔离。

## 可以支持的差异化表述

现有全文证据支持一个窄而可检验的差异：五篇近邻均未把 Bemis–Murcko scaffold 隔离、完整候选 drug-macro AP、RNA 频率强先验、跨库实体去重、时间外推和不同 PMID 再支持放进同一套 ncRNA–drug 审计。该表述仍是**有界检索下的 provisional gap**，不能写成“首次”或“所有既有方法都没有”。

## 不能支持的表述

- 不能声称 cold-start、完整候选排序、语言模型或多视图融合本身新颖。
- 不能把不同候选空间上的作者 AUC/AUPR 与本研究 AP 直接排序。
- 不能把案例研究的文献命中当作独立来源确认，除非候选和核验来源在训练前已隔离。
- 不能把当前小规模时间/PMID 测试写成前瞻性生物验证。
