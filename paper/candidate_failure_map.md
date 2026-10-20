# 候选方法与停止决策地图

本索引覆盖 `docs/` 下全部 `*-pilot-design.md`。它的用途是公开方法搜索范围和停止规则，避免只展示最终保留的基线。具体数值、门槛和竞争解释仍以 `EXPERIMENT_LOG.md` 及冻结结果文件为准。

## 状态定义

- `failed_gate`：已运行，但没有同时满足其预注册的实际意义、区间、折方向或安全门；不得继续同族追参。
- `retained_diagnostic_baseline`：没有成为论文级新算法，但因可解释性或强度保留为协议诊断基线。
- `stage_pass_later_failed`：早期数据/协议阶段通过，随后更严格 scaffold 确认失败。
- `mixed_overall_failed`：局部 estimand 有正信号，但预注册整体主张失败。
- `data_gate_failed`：在读取模型终点前因覆盖或身份门停止；`not_run` 不等于模型运行失败。
- `user_frozen_before_model`：数据门或设计已经存在，但用户在模型实现/训练前冻结论文；不得把未运行写成失败，也不得纳入论文结果。

## 方法族结论

| 方法族 | 覆盖的核心想法 | 当前结论 |
|---|---|---|
| 化学表征与邻域 | ECFP、ChemBERTa、MoLFormer、BPE motif、Tanimoto、原型、子结构富集 | 多个候选稳定高于 RNA prior，但最佳主增量约 `+0.0042`，未过 `+0.01`；简单拼接、邻域和更大预训练模型没有突破 |
| 训练目标与负例 | pairwise、listwise、BCE、实体等权、hard negative、nnPU | drug-cold 中可出现正信号，但 scaffold 确认或主幅度门失败；BPR 本身已有直接近邻 |
| 协同与潜变量 | AIMF、ALMF、低秩谱、非线性谱、两阶段协同蒸馏 | warm RNA 协同结构不能稳定映射到未见 scaffold；蒸馏候选相对锁定强基线显著退步 |
| 路由、门控与融合 | coverage router、concentration router、三专家、同号共识、reliability gate、rank stacker | validation 中的专家互补不能迁移到 test scaffold；test-label oracle 只作停止搜索上限 |
| 外部生物证据 | gene/PPI/Reactome/疾病桥、RNA-FM、PRISM 功能表型 | 覆盖通常不是唯一瓶颈；信号弱于 prior/结构强基线或不能超过 permutation |
| 跨域与层级 | 多物种序列、跨 ncRNA 多任务、seed-family 层级 | 严格同实体/序列排除后没有可归因增益；层级化学效应不优于组成基线 |
| 来源与时间 | PMID 来源平衡、独立复现、两阶段 hurdle、首次发现时间切分 | 证明评测目标会改变结论，但当前 side information 不能稳定识别独立复现或新药标签 |
| 公开模型适配 | LocalGL、sChemNET、HMVCC、RAHGL 数据协议 | 支持 benchmark/protocol 主张；不能升级为 universal model failure 或新算法 SOTA |

## 完整性边界

- CSV 中每个设计文件恰好一行；`tests/test_candidate_failure_map.py` 与文件系统集合做精确比较。
- 本表不把 post hoc oracle、smoke、数据门或未落盘运行混入正式结果。
- 当前停止规则是：所有新增算法探索均已暂停。只有用户重新明确授权，才允许另立路线；新的 estimand、机制或数据本身不再自动触发实验。

机器可读索引：`candidate_failure_map.csv`。
