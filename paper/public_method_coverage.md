# 公开方法覆盖与严格协议适配表

本表回答一个限定问题：哪些公开方法已经被放到共同的药物冷启动或骨架隔离、完整候选终点中，哪些只完成了全文或源码核验，以及为什么不能把缺失项伪装成“本方法胜出”。绝对指标只在同一数据、同一划分和同一候选空间内比较。

| 方法 | 证据与公开工件 | 本项目适配状态 | 可报告结果或边界 | 尚不能声称什么 |
|---|---|---|---|---|
| ncRD-LG LocalGL | 出版商完整 HTML；官方代码/数据固定提交 `f1358d5…` | 作者公开模型已完成 Mi 五折 scaffold-disjoint、full-candidate 动态重采样适配 | 动态 LocalGL AP `0.153275`，低于 RNA prior `0.157507`；候选高 `0.008473`，95% CI `[0.005320,0.011759]`，`5/5` 折同向 | 动态−固定仅 `+0.000715`、CI 跨 0 且绝对差 `<0.005`；结论仍只限公开 LocalGL 实现 |
| sChemNET | 出版商 HTML、官方 PDF 至 EOF；官方仓库固定提交 `66c0c88…`，未见许可证 | 独立重实现无序列 MACCS 消融，完成三种子 scaffold-disjoint、full-candidate 适配 | 无序列 AP `0.154500`，低于 prior；候选高 `0.007248`，95% CI `[0.004751,0.009681]`，`5/5` 折同向 | 不是作者代码复现；未运行 miRNA 序列相似度和外部未标注药物扩增，不能称击败完整 sChemNET |
| HMVCC | 出版商完整 HTML；作者代码/数据固定提交 `be4dd3a…`，未见许可证 | 不复制作者源码，直接导入 loader/model；完成 ncRNADrug 严格 drug-cold、full-candidate 适配 | 作者模型 AP `0.064681`；候选相对作者模型 `+0.049337`，95% CI `[0.035925,0.063837]`，`5/5` 折同向 | 发布药物表没有逐行 SMILES，不能做可审计 scaffold split；Mi 实体/正边重叠显著，去重后候选正结果消失 |
| RAHGL-MDR | 官方 30 页 PDF 至 EOF；官方仓库固定提交 `95ce15e…` | 作者训练源码及逐候选分数缺失；只对其公开数据运行目标对齐诊断基线 | 固定 drug-cold 候选相对 prior `+0.013580`，但 scaffold-cold 仅 `+0.000296`，CI 跨 0，`2/5` 折同向 | 不是作者模型复现；不能把固定 drug-cold 的作者数值与新 scaffold 协议直接判胜负 |
| MGCNA | PLOS 正式全文与 supporting text 至 EOF；公开仓库 `sheng-n/MGCNA` | 已核实 edge、miRNA/drug/double-cold 协议；未做共同 scaffold/full-candidate 重跑 | 作为多视图 GCN 与实体冷启动的已知近邻 | 案例研究全候选排序不是 benchmark 主协议；released split 确定性与共同协议适配尚未核验 |
| PLMF-MDA | PLOS Version 2 正式全文至结论；公开仓库 `sheng-n/PLMF-MDA` | 独立严格三种子 scaffold/full-candidate 适配完成，`15/15` 单元与协议门通过 | PLMF AP `0.135050`，低于 prior `0.157507`；候选高 `0.026698`，95% CI `[0.021679,0.031884]`，`5/5` 折同向 | 不是作者原数值复现；冷实体、候选空间、划分与作者论文不同，结论只限本严格适配 |
| GCFMCL | 正式元数据与官方公开源码；出版商全文受访问验证阻断 | 源码已确认 drug-as-user BPR；未做论文级复现或共同协议适配 | 足以否定“首次把 drug-wise pairwise ranking 用于该任务” | 不能从源码反推全部论文协议或结果；全文未核实，不能作实质性横向性能结论 |

## 覆盖结论

- 共同严格终点下已有四个可审计对照：ncRD-LG LocalGL、sChemNET 无序列消融、HMVCC 作者模型与 PLMF-MDA 独立适配；其中 LocalGL、sChemNET 与 PLMF-MDA 使用 Mi scaffold-disjoint 终点。
- RAHGL-MDR 的公开数据足以检验“drug-cold 正结果是否经得起 scaffold 隔离”，但不足以复现作者模型。
- MGCNA 与 GCFMCL 仍是方法覆盖边界，不是缺席的“败者”；主文不能把未适配方法写成数值排名中的失败者。
- 当前表解决了公开方法是否被逐项枚举的问题，没有解决完整模型覆盖，也没有把 benchmark/protocol 结果升级为新算法 SOTA。

CSV 同源表：`public_method_coverage.csv`。
