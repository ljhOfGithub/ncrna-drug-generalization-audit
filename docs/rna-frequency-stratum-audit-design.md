# RNA 频率层级信息量审计

## 问题

Mi 严格 scaffold-cold 的 ChemBERTa pairwise residual 在完整候选 drug-macro AP 上只比训练图 RNA 频率先验高约 `0.0042`。本审计检查这点增益是否来自训练低频 RNA 的稳定跨层重排，以判断层次先验是否仍有值得独立确认的窄假设。

## 冻结输入与分层

- 输入固定为 `results/chemberta-pairwise-residual-pilot-20261019/mi_oof_predictions.csv`；不重新训练、不改预测、不选择参数。
- 用 `MiPair.npy`、原 Bemis–Murcko scaffold 和 split seed `20261019` 重建每折训练正例矩阵。
- 每个 RNA 按该折训练药物中的正例次数固定分为：`0`、`1–2`、`3–9`、`≥10`。阈值不根据审计结果调整。
- 候选与 `rna_prior_only` 必须在 fold、RNA、drug、label 上严格一一对齐。

## 输出与边界

每层报告测试正例占比、候选与先验的 balanced sampled-unlabeled AP、逐折方向，以及候选减先验 residual 在正例和 sampled-unlabeled 上的均值差。OOF 文件包含全部测试正例和等量 sampled-unlabeled，但不是完整 1,805-RNA 候选分数，因此本审计只作信息量诊断，不能替代主文 full-candidate AP。

若低频层没有正向 residual separation，或 balanced AP 增量不能在至少 `4/5` 折同向，则关闭“仅靠当前 ChemBERTa residual 加层次频率收缩”的后续算法路线。即使诊断为正，也只能提出新的预注册确认，不能把本审计当独立验证。
