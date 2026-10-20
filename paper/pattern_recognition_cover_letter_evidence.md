# Pattern Recognition Cover Letter 证据清单

状态：投稿前素材，不是已提交 cover letter。  
依据：2026-10-20 官方 Guide for Authors 要求说明 SOTA 比较、公共数据集和验证指标。

## 1. 是否与 SOTA 比较

回答：**是，但比较分为同协议重实现、严格适配和协议级对照，不能把跨协议论文数字直接写成胜负。**

可列出的五篇代表性近邻：

1. **ncRD-LG (Pattern Recognition, 2026)**：本研究起点；严格 scaffold-cold 下运行其 LocalGL 组件动态重采样适配。动态相对固定 AP 仅 `+0.000715`、95% CI 跨 0，且绝对差低于预注册 `0.005`；主表使用动态版并保留实现限定。
2. **RAHGL-MDR (IJMS, 2026)**：全文与公开固定数据已核；其完整候选 degree/popularity 基线说明强频率先验不可省略。本研究比较固定 drug-cold 与 scaffold-disjoint 结论翻转，不冒充作者模型复现。
3. **HMVCC (Expert Systems with Applications, 2027；online 2026)**：出版商完整 HTML 已读至参考文献；论文任务为 ncRNA–drug 而非仅 miRNA–drug。本研究运行公开代码的严格 drug-cold 适配，并审计 Mi–ncRNADrug 实体/正 pair 重叠及去重后的结论翻转。
4. **sChemNET (Nature Communications, 2024)**：官方 PDF 全文已核；本研究实现无 miRNA 序列、无外部未标注扩增的 MACCS 严格 scaffold-cold 消融。结果不能外推为完整 sChemNET 胜负。
5. **PLMF-MDA (PLOS Computational Biology, 2026)**：出版商开放全文已核；其语言模型、多尺度序列/分子编码与实体 cold-start 属于直接近邻，但未报告本研究联合采用的 scaffold、频率先验、跨库去重、时间和独立来源审计。独立严格三种子适配完成后 AP 为 `0.135050`；同协议候选高 `0.026698`，95% CI `[0.021679,0.031884]`。必须称独立适配，不称作者结果复现。

Cover letter 应强调：主贡献不是在不兼容协议上宣称 SOTA，而是证明严格评测、强先验和证据独立性会改变“模型是否进步”的结论，并给出可复核的同协议适配。

## 2. 使用了哪些公共数据集

主文/主表使用：

- ncRD-LG 的 Mi 数据：主要 scaffold-disjoint 开发与严格公开基线适配；
- HMVCC 的 ncRNADrug 与 NoncoRNA：drug-cold 外部边界与实体去重审计；
- RAHGL-MDR：固定 drug-cold 与 scaffold-disjoint 对照；
- SM2miR 历史快照：非 Mi CID 的时间 mini-holdout；
- ncRNADrug 来源字段：不同 PMID 再支持代理目标。

补充诊断使用 ChEMBL、miRTarBase、STRING、Reactome、CTD、PRISM 与 LINCS/GEO 元数据。它们的获取、版本、哈希、许可证/通知义务和未进入发布包的边界分别记录在实验日志、复现说明和 `release/THIRD_PARTY.md`。不得在 cover letter 中写成“所有原始数据均随包发布”。

## 3. 使用了哪些验证指标

- **主指标**：held-out drug 对全部 ncRNA 候选的 average precision，再对药物宏平均（drug-macro AP）。
- **不确定性**：按药物或 Bemis–Murcko scaffold 聚类的 paired bootstrap 95% 区间；同时报告五折方向一致性。
- **诊断指标**：balanced sampled-unlabeled pooled AUPR；只用于与旧协议衔接，不替代 full-candidate 主终点。
- **稳健性维度**：第二 scaffold split seed、三训练种子、实体去重、时间 holdout、独立 PMID 目标、公开模型适配差异和预注册效果门。

Cover letter 不应把数据库未记录 pair 称为实验确认阴性，也不应把 bootstrap 区间解释为已经校正历史方法选择偏差。
