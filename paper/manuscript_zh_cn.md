# 普通 drug-cold 增益未在本次新骨架评估中保持：ncRNA–药物关联预测的条件性研究

> 稿件状态：简体中文事实稿，结果已冻结；尚不是可直接上传期刊系统的英文终稿。  
> 工作英文标题：*Drug-Cold Gains Do Not Persist under Scaffold Separation in ncRNA–Drug Prediction*
> 作者：Jihao Li；单位：Independent Researcher, Shenzhen, Guangdong, China；通讯邮箱：jihao.li@polyu.edu.hk

## 摘要

药物–非编码 RNA（ncRNA）关联预测常以随机配对或普通实体冷启动评估模型，但“测试药物未在训练中出现”并不等同于“模型能够外推到未见化学骨架”。本研究冻结并比较两个评估协议：RAHGL-MDR 固定普通 drug-cold 完整候选排序，以及训练、验证、测试之间 Bemis–Murcko scaffold 完全隔离的严格排序。我们在 RAHGL-MDR 公开数据和固定 drug-cold 折上评估按药物均衡的 prior-residual 候选，并以仅由训练集估计的 RNA 频率先验为强基线。三个训练种子的逐药物汇总显示，普通 drug-cold 下候选的 drug-macro average precision（AP）为 `0.184244`，高于先验的 `0.170664`，差值为 `+0.013580`，95% bootstrap 区间为 `[+0.005139,+0.024170]`，五折均不下降。改用五折 scaffold-disjoint 协议后，候选和先验的 AP 分别为 `0.175435` 和 `0.175139`，差值仅 `+0.000296`，scaffold-cluster 95% 区间为 `[-0.007782,+0.008476]`，仅 `2/5` 折不下降，且一个训练种子出现负增益。Mi 数据上的严格 scaffold-cold 评估进一步表明，候选虽然优于 LocalGL、sChemNET 无序列消融和 PLMF-MDA 独立适配，但相对 RNA 先验只提高 `0.004239`，未达到 `+0.01` 实际意义门。跨库审计还发现，ncRNADrug 原始快照上的正增益在去除与 Mi 同名实体后由 `+0.007581` 变为 `-0.012729`。这些结果支持一个条件性结论：该候选可以改善 RAHGL-MDR 固定普通 drug-cold 协议下的新药排序，但本次严格 scaffold-disjoint 评估没有确认稳健增益；普通 drug-cold 的性能主张不能直接推广到未见化学骨架。评估新药预测时，应同时报告完整候选、强频率先验、scaffold 隔离和数据来源边界。

**关键词：** ncRNA–药物关联；新药冷启动；scaffold-disjoint；完整候选排序；频率先验；评估协议

## 1 引言

药物–ncRNA 关联预测试图从已报道关系中恢复或扩展潜在关联。它同时具有交互预测和检索属性：模型需要针对每个药物，在正例稀少、未报道 pair 仍为 unlabeled 的大候选集中排序。相关 RNA–小分子研究覆盖特征编码、亲和力回归、结构虚拟筛选和序列交互评分[11–15]；这些任务的输入、端点、负例构造和候选空间不同，不能脱离共同协议直接比较数值。

现有 ncRNA–药物研究已经使用图神经网络、局部子图、多视图表示和生物语言模型，并逐步从随机配对划分扩展到 drug-cold、RNA-cold 和 double-cold 评估。随机配对允许共享实体；普通 drug-cold 阻断测试药物身份，却可能保留相近化学核心；scaffold-disjoint 进一步要求结构核心未见。这与 DTI 文献的 S1–S4 协议区分一致[24]。若不区分这些层级，“预测新药”容易被误读为实验并未支持的“外推到新化学骨架”。

另一个容易被忽略的因素是强先验。在完整候选排序中，不同 RNA 被报道的频率高度不均。仅按训练集中 RNA 的出现频率排序，往往已经形成很强的 drug-independent 基线。一个模型可以显著优于较复杂的公开模型，却只比这一先验高出很小幅度。类似地，跨数据库结果可能共享 RNA、药物和正 pair；在未审计这些交集时，把第二个数据库称为独立外部验证会夸大证据强度。

本研究不再提出普适新算法，而是冻结一个条件性问题：按药物均衡的 prior-residual 排序器能否在普通 drug-cold 新药扩展中稳定改善完整候选排序，以及该优势能否保持到严格新 scaffold 条件。围绕这一问题，我们还使用 Mi、ncRNADrug、NoncoRNA、SM2miR 和不同 PMID 再支持标签，检验强先验、结构隔离、实体重叠和来源独立性如何改变结论。

本文贡献如下：

1. 给出一个冻结的条件性结果：RAHGL-MDR 固定普通 drug-cold 下候选相对 RNA 先验提高 `0.013580` AP；本次严格 scaffold-disjoint 下只提高 `0.000296`，且不确定性区间跨 0。
2. 建立区分随机配对、实体冷启动、scaffold 冷启动、时间新药和独立来源目标的评估阶梯，并统一使用完整候选 drug-macro AP。
3. 在共同严格终点下评估 ncRD-LG LocalGL、sChemNET 无序列消融和 PLMF-MDA 独立适配，明确作者实现、独立重实现和不可比结果的边界。
4. 定量审计 Mi 与 ncRNADrug 的实体和正 pair 重叠，并通过去重、时间新药和不同 PMID 标签展示外部证据依赖性。
5. 提供由冻结 summary/config 重建主表和图的本地证据包，同时保留失败路线和禁止主张。

## 2 相关工作

### 2.1 RNA–小分子与 ncRNA–药物预测

RNAincoder 学习 RNA 和化合物多描述符表示[11]；RNAmigos 从 RNA 口袋图预测配体指纹并在 decoy 中排序[12]，RNAmigos2 进一步加入大规模 docking 监督和结合位点结构簇隔离[13]。RSAPred 评估 RNA–小分子亲和力回归[14]；RNAsmol 报告 RNA-cold、小分子-cold、double-cold 和 decoy 排名[15]。这些工作构成重要先例，但其端点不等同于关联数据库上的完整候选 drug-macro AP。

ncRD-LG 使用局部语义子图和生物语言模型进行 ncRNA–药物关联预测，其主协议为随机配对划分，并把 leave-drug、leave-ncRNA 和 scaffold 划分列为未来工作[1]。RAHGL-MDR 已覆盖 leakage-safe edge、miRNA-cold、drug-cold、double-cold 和完整候选排序，并报告 degree/popularity 强基线[2]。因此，cold-start 和完整候选排序本身不是本文的新颖点。

HMVCC 报告 edge split、跨物种、跨数据库和 drug cold-start 等多种设置[3]；MGCNA 采用多视图图卷积与注意力融合进行 miRNA–药物关联预测[4]；PLMF-MDA 使用 RNA-FM、ChemBERTa-2、内在编码器和跨模态注意力预测 miRNA–药物耐药/敏感性关联[5]。sChemNET 直接研究小分子靶向 miRNA 功能，并用分子指纹相似度阈值评估化学不相似测试子集；该协议不是 Bemis–Murcko scaffold 划分[6]。GCFMCL 的公开实现已在表征学习阶段采用 drug-as-user 的 BPR，因此本文不把 pairwise ranking 声称为首次[7]。

### 2.2 预训练表示与冷启动迁移

RNA-FM、RNAErnie 和 BiRNA-BERT 从大规模 RNA 序列学习可迁移表示[16–18]，ChemBERTa 在 SMILES 上预训练并包含 scaffold-split 分子属性任务[19]。DTI 文献中，TransDTI 与 GraphDTA 使用语言或图表示[20,22]，C2P2 将辅助交互知识迁移到未见药物或靶点[21]，DrugBAN 比较随机、未见实体、cold-pair 和聚类跨域协议[23]。DrugBAN 还明确指出：当高度相似药物跨越划分时，按身份留出的 unseen-drug 仍可能过易。因此，预训练和身份新颖性本身不能建立化学核心新颖性。

### 2.3 局部子图、排序目标与评估设计

SEAL 把局部 enclosing subgraph 建立为一般链接预测策略[25]；BPR 则针对 implicit feedback 形式化 pairwise 排序，并不把所有缺失项当成已验证阴性[26]。Pahikkala 等区分 pair-wise、unseen-drug、unseen-target 和 double-unseen 协议[24]；MoleculeNet 说明化学数据的随机划分可能不适当，并用 scaffold grouping 形成更强结构测试[27]。对不平衡候选空间，PR 分析能直接显示假阳性负担，而且优化 ROC 面积不保证优化 PR 面积[28,29]。

### 2.4 标识符与证据来源

miRBase 与 Rfam 分别提供 microRNA 命名和 RNA 家族注释资源[30,35]；PubChem 区分提交者 Substance 记录和标准化 Compound 结构[31]。RNAInter 混合实验与计算预测交互[32]，lncRNAdb 侧重人工整理的功能证据[33]，DrugBank 同时包含人工整理与预测字段[34]。因此必须保留标识符、证据类型与来源边界；数据库缺失不是已确认生物阴性。

截至冻结日期，有界全文核验未发现单篇直接近邻在同一 ncRNA–drug 审计中联合使用 Bemis–Murcko scaffold 隔离、完整候选 drug-macro AP、RNA 频率强先验、跨库实体去重、时间新药和不同 PMID 再支持。该差异只是暂定空缺，不构成穷尽性“首次”主张。

## 3 方法

### 3.1 任务与估计对象

给定训练集中已报道的 ncRNA–药物正关联，对每个测试药物为全部候选 ncRNA 产生分数。主指标是每个药物上的 average precision，再对测试药物作宏平均。未被数据库记录的 pair 只作为 unlabeled 候选，不解释为真实生物学阴性。

本文区分两个主协议：

- **普通 drug-cold：** 训练、验证和测试药物身份互斥，但不强制 scaffold 互斥；本文只把它解释为 RAHGL-MDR 固定划分上的实体冷启动，不假定它代表所有部署分布。
- **严格 scaffold-disjoint：** 以 Bemis–Murcko scaffold 为分组单位，使训练、验证和测试 scaffold 完全不重叠，代表更强的新骨架外推要求。无环分子按 canonical SMILES 形成独立组。

普通 drug-cold 不等同于“所有测试药物共享训练 scaffold”，也不等同于严格新骨架评估。本文只比较两种已冻结协议，不把它们的差异归因为单一 scaffold 泄漏机制。

### 3.2 协议层级与划分构造

随机 pair、drug-cold、double-cold、scaffold-disjoint 和时间新药估计的是不同部署问题，而不是同一难度标尺。按身份互斥的药物仍可能与训练药物共享近邻或相同二维核心。普通协议沿用 RAHGL-MDR 固定折；严格协议为每个标准化分子计算 Bemis–Murcko framework，并把完整 framework group 置于同一外层分区，无环分子按 canonical SMILES 分组。这一设计遵循 MoleculeNet 对 scaffold split 的化学学习动机[27]。所有分组在拟合前确定，验证集只用于已冻结的候选选择。

### 3.3 数据与候选空间

RAHGL-MDR 数据包含 635 个 miRNA、216 个药物和 5,379 个唯一正 pair；197 个有正例药物进入 drug-cold 或 scaffold-cold 外层测试。Mi 对齐工件包含 1,805 个 ncRNA、625 个药物和 9,395 个正 pair，606 个活跃药物进入主要 scaffold-disjoint 评估。ncRNADrug、NoncoRNA、SM2miR 时间子集和 Mi 的不同 PMID 再支持子集用于外部边界审计。各资源的对齐统计和来源字段见 `dataset_protocol_stats.md`。

所有主评估均枚举测试药物与完整 ncRNA 候选集。Mi 与 ncRNADrug 的同名 RNA、药物和正 pair 采用固定规范化规则计算交集；去重确认删除与 Mi 同名的实体，而不是在看到结果后选择性删除 pair。

RNA 名称按 miRBase 与 Rfam 所描述的资源职责核对[30,35]，化合物规范化保留 PubChem 对提交记录和标准化结构的区分[31]。RNAInter、lncRNAdb 和 DrugBank 的证据类型与整理范围不同[32–34]，因此来源字段不被抹平。规范化只能减少表面命名差异，不能统一实验条件或把缺失 pair 变成阴性。

### 3.4 候选与强基线

RNA prior 只使用内层训练药物中的 RNA 正例频率并进行 Laplace 平滑。候选模型在 prior 基础上学习药物和 RNA 特征的 pairwise 残差；RAHGL-MDR 主候选进一步使每个训练药物对总 pairwise loss 的贡献相等，避免高频药物以边数主导目标。残差 scale 只在内层验证集从冻结网格选择，scale 为 0 时精确回退到 RNA prior。

本文不把这一目标称为新 ranking loss。GCFMCL 已在同任务使用 BPR；候选在本文中的作用是检验“药物均衡训练是否能改善特定 drug-cold 分布”，而不是建立普适算法新颖性。

残差依据已观察与未观察候选之间的排序训练。按照 BPR 对 implicit feedback 的基本区分[26]，未观察 pair 始终保持 unlabeled，不解释为实验阴性。

### 3.5 对照与实现边界

Mi 严格终点包括：动态重采样的 ncRD-LG LocalGL 适配、sChemNET 无 miRNA 序列/无外部药物扩增的 MACCS 消融，以及 PLMF-MDA 的独立三种子严格适配。sChemNET 和 PLMF-MDA 结果不是作者原论文数值复现。RAHGL-MDR 缺少作者训练源码和逐候选预测，因此本文只复用其公开数据和固定折运行诊断基线，不与作者模型作配对胜负结论。

### 3.6 统计分析与冻结规则

average precision 先在每个测试药物的完整候选列表上计算，再对药物宏平均，使每个测试药物权重相同。由于正例稀少且假阳性会直接降低 precision，PR 指标比单独 AUROC 更贴近本任务[28,29]。本文不把受限或平衡负例集上的 AP 与完整候选 AP 视为可直接比较。

RAHGL-MDR 的普通 drug-cold 对逐药物差值进行 paired bootstrap；严格 scaffold-cold 按 scaffold group 成簇 bootstrap。两项 RAHGL-MDR 主协议均报告 95% 区间、五折不下降数和三个训练种子。严格 scaffold 确认门要求候选相对 RNA prior 至少 `+0.01` AP、区间下界大于 0、至少 `4/5` 折不下降、三个种子差值均为正且至少两个种子达到 `+0.01`；普通 drug-cold 的早期门另要求候选超过论文所报 popularity MAP。区间条件于固定外层划分和已经运行的训练种子：先对同一 fold/drug 的种子特异 AP 求均值，再对药物或 scaffold group 重采样；它不覆盖重新抽取训练种子或外层划分的不确定性。Mi、外部数据库和来源标签等辅助分析采用各自冻结配置中的种子与判定门，不把主协议的门泛化为统一标准。

2026-10-20 起停止全部新增探索、训练、数据下载和调参。冻结后只允许重建已有表图、校验哈希和测试、整理引用以及制作投稿材料。历史方法选择偏差不能由 bootstrap 区间消除，Mi 结果因此明确标为开发性证据。

## 4 结果

### 4.1 普通 drug-cold 增益未在本次严格 scaffold 评估中保持

RAHGL-MDR 作者固定 drug-cold 折上，三个训练种子的 entity-balanced prior-residual 汇总 AP 为 `0.184244`，RNA prior 为 `0.170664`，差值 `+0.013580`，95% 区间 `[+0.005139,+0.024170]`，五折均不下降。候选通过冻结的 drug-cold 门。

使用同一数据、候选空间、模型家族和训练种子，但重新构造五折 scaffold-disjoint 协议后，候选 AP 为 `0.175435`，RNA prior 为 `0.175139`，差值降至 `+0.000296`，scaffold-cluster 95% 区间 `[-0.007782,+0.008476]`，只有 `2/5` 折不下降。三个训练种子的差值分别为 `+0.005339`、`+0.008217` 和 `-0.012667`。候选相对同预算普通 pairwise 的差值也只有 `+0.000857`，区间跨 0。

两种协议同时改变了训练、验证和测试药物的组成，因此现有证据不能把结果差异归因为 scaffold 隔离的单独因果效应。可支持的结论是：固定普通 drug-cold 中的正结果，在本次严格 scaffold-disjoint 评估中没有获得稳健确认。

### 4.2 Mi 严格评估中，公开模型胜负不等于超过强先验

Mi 的主要五折 scaffold-disjoint 结果中，候选 AP 为 `0.161748`，RNA prior 为 `0.157509`，差值 `+0.004239`，95% 区间 `[+0.002812,+0.005899]`，五折均不下降，但没有达到 `+0.01` 门。第二个 scaffold split 的差值为 `+0.002881`，区间 `[+0.001047,+0.004782]`，`4/5` 折不下降，同样失败。

同一候选空间和 scaffold 终点下，动态 LocalGL、sChemNET 无序列消融和 PLMF-MDA 独立严格适配的 AP 分别为 `0.153275`、`0.154500` 和 `0.135050`。候选分别高 `0.008473`、`0.007248` 和 `0.026698`。各公开模型汇总使用其对应的匹配 prior；它们的 prior 约为 `0.157507`，与主候选表的 `0.157509` 相差约 `1.8×10^-6`，不改变结论，但不写成完全相同的数值对照。候选相对其主表 prior 的实际增量仍不足 `+0.01`。这说明“优于复杂公开模型”和“对强先验有实质增益”是两个不同命题。

### 4.3 跨数据库重叠改变外部验证结论

Mi 与 ncRNADrug 对齐快照存在 RNA、药物和正 pair 重叠。原始 ncRNADrug drug-cold 中，候选相对 prior 为 `+0.007581`，95% 区间 `[+0.001838,+0.013747]`，五折均不下降。删除与 Mi 同名的实体后，候选 AP 为 `0.063689`，prior AP 为 `0.076418`，差值变为 `-0.012729`，区间跨 0，确认门失败。NoncoRNA 上的差值为 `+0.003579`，区间同样跨 0，仅 `2/5` 折不下降。

去重结果不能证明原始增益完全由泄漏引起，因为去重也改变了样本组成和支持度；它能证明的是，未审计实体和 pair 交集的第二数据库不能自动视为独立确认。

### 4.4 时间新药和不同来源标签暴露额外边界

在 18 个非 Mi CID 的 SM2miR 时间 mini-holdout 上，候选相对 prior 为 `-0.019876`，不支持当前方法迁移到真正未参与开发的新药标签。该子集很小，只能否定正向确认，不能估计普适外部效应。

对于至少两个不同 PMID 支持的 Mi pair，直接以重复文献支持标签训练的 ECFP residual 相对该标签的频率 prior 提高 `+0.010933`；但它比使用全部已报道 pair 估计的 RNA prior 低 `0.035344`。本次 `interaction_hurdle` 在五折中均选择权重 0，因而精确回退到第一阶段；`conditional_prior_hurdle` 仅第 2 折选择非零权重。该结果只说明本次模型尚未显示对重复文献支持标签的额外预测价值；不同 PMID 不自动等同于独立实验复现，也不能据此识别报道过程的因果机制。

## 5 讨论

### 5.1 条件性贡献

本文最强、也最窄的结论不是“提出了可泛化到新 scaffold 的算法”，而是“在 RAHGL-MDR 固定普通 drug-cold 划分中，该候选能稳定改善完整候选排序；本次严格 scaffold-disjoint 评估未确认同等稳健增益”。普通 drug-cold 结果可作为该固定协议下的有限证据；若目标是发现新骨架，现有证据不足，不能沿用同一性能主张。

### 5.2 为什么必须保留强先验

RNA 频率先验反映训练数据中的报道结构，而不是生物学机制。但正因为数据库高度不均衡，它是评估模型是否增加药物特异信息的必要对照。Mi 中候选显著高于多个神经模型适配，却只比 prior 高不到 `0.005` AP，展示了复杂基线之间的胜负可能掩盖最关键的实际比较。

### 5.3 不能从结果推出的机制

普通 drug-cold 与 scaffold-disjoint 的差异不能简单归因为同 scaffold 泄漏。严格 scaffold 重划分同时改变了结构支持、训练组成和外层测试分布，本文没有设计能识别这些因素的单独因果贡献，也不根据事后分层重新选择模型。

### 5.4 对报告规范的建议

面向新药的 ncRNA–药物关联研究至少应报告：完整候选 drug-macro AP；仅由训练集估计的频率先验；普通 drug-cold 和 scaffold-disjoint 两种结果；训练与测试的实体、scaffold 和正 pair 重叠；多个 split/training seeds；按药物或 scaffold 聚类的不确定性；作者模型复现与独立适配的明确区分；以及未知 pair 为 unlabeled 的边界。

### 5.5 局限性

第一，多个候选曾在 Mi 上开发，现有区间不能消除历史方法选择偏差。第二，RAHGL-MDR 未发布作者训练代码和逐候选预测，本文不能与作者模型进行同实现配对复现。第三，普通 drug-cold 与 scaffold-disjoint 使用不同的外层分配；二者反映不同协议条件下的表现差异，不是单药物反事实。第四，ncRNADrug triples 缺少 pair-level PMID，来源独立性无法完整核验。第五，SM2miR 时间子集样本小。第六，所有标签来自已报道关联，缺少前瞻性实验或湿实验验证。第七，上游部分仓库未见许可证，当前发布包只含本地摘要、配置、表图和重建逻辑，不能替代完整训练数据发布。

## 6 结论

在 RAHGL-MDR 的固定普通 drug-cold 划分中，按药物均衡的 prior-residual 候选对完整 ncRNA 候选排序取得稳定、超过幅度门的增益；当评估改为本次严格 scaffold-disjoint 划分后，增益接近零、区间跨零且跨种子不稳定。结合 Mi 强先验、跨库去重和重复文献支持标签审计，本文把可支持的科学主张限定为：**固定普通 drug-cold 协议下存在增益，但该性能主张不能直接推广到未见化学骨架。**这一边界比追求普适算法更接近当前证据，也为后续研究提供了可复核的评估要求。

## 数据与代码可用性

公开证据包提供冻结 summary/config、主表、图、重建脚本、测试、第三方边界和 SHA-256 清单。第三方原始数据、仓库代码、模型权重和论文 PDF 不随包重新分发。公开仓库为 `https://github.com/ljhOfGithub/ncrna-drug-generalization-audit`，冻结版本为 `v0.1.3`。尚未分配永久归档 DOI，不把 GitHub 标签冒充 DOI。

## 伦理声明

本研究使用公开或依法访问的计算数据，不涉及新的人体招募、干预、动物实验或可识别个体信息，因此伦理审批与知情同意不适用。

## 作者贡献（CRediT）

Jihao Li：Conceptualization、Methodology、Software、Validation、Formal analysis、Investigation、Data curation、Writing–original draft、Writing–review and editing、Visualization、Project administration。

## 利益冲突

作者声明不存在利益冲突。

## 基金

本研究未获得公共、商业或非营利资助机构的专项基金资助。

## 生成式 AI 使用说明

稿件准备期间，作者使用 OpenAI Codex 辅助文献发现、代码起草与检查、执行支持、统计结果核对、稿件草拟、语言编辑、引用核验和一致性检查。作者审阅并编辑了全部输出，对照来源材料和已保存的机器可读结果核验引用与报告数值，并对论文内容承担全部责任。生成式 AI 未被列为作者，也未用于创建或修改原始研究数据。

## 参考文献标识（已核实，待期刊格式终排）

1. ncRD-LG. *Pattern Recognition* (2026). DOI: `10.1016/j.patcog.2026.113556`.
2. RAHGL-MDR. *International Journal of Molecular Sciences* 27(20):9013 (2026). DOI: `10.3390/ijms27209013`.
3. Zhihao Ma, Yu Chen, Hailing Wang, Xidong Xi, Guitao Cao, Lei Deng, Min Wu. Hypergraph multi-view learning for ncRNA–drug association prediction with cluster anchors and contrastive alignment. *Expert Systems with Applications* 334, Part D:134658 (2027；online 2026). DOI: `10.1016/j.eswa.2026.134658`.
4. Nan Sheng, Yunzhi Liu, Ling Gao, Lei Wang, Lan Huang, Yan Wang. Multi-view fusion based on graph convolutional network with attention mechanism for predicting miRNA related to drugs. *PLOS Computational Biology* 21(11):e1013703 (2025). DOI: `10.1371/journal.pcbi.1013703`.
5. Nan Sheng, Yunzhi Liu, Ling Gao, Wenju Hou, Lan Huang, Yan Wang. A pre-trained language model-based cross-modal fusion framework for predicting miRNA-drug resistance and sensitivity associations. *PLOS Computational Biology* 22(2):e1013968 (2026). DOI: `10.1371/journal.pcbi.1013968`.
6. Diego Galeano, Imrat, Jeffrey Haltom, Chaylen Andolino, Aliza Yousey, Victoria Zaksas, Saswati Das, Stephen B. Baylin, Douglas C. Wallace, Frank J. Slack, Francisco J. Enguita, Eve Syrkin Wurtele, Dorothy Teegarden, Robert Meller, Daniel Cifuentes, Afshin Beheshti. sChemNET: a deep learning framework for predicting small molecules targeting microRNA function. *Nature Communications* 15:9149 (2024). DOI: `10.1038/s41467-024-49813-w`.
7. Jinhang Wei, Linlin Zhuo, Zhecheng Zhou, Xinze Lian, Xiangzheng Fu, Xiaojun Yao. GCFMCL: predicting miRNA-drug sensitivity using graph collaborative filtering and multi-view contrastive learning. *Briefings in Bioinformatics* 24(4):bbad247 (2023). DOI: `10.1093/bib/bbad247`.
8. Xinyu Cao 等. ncRNADrug: a database for validated and predicted ncRNAs associated with drug resistance and targeted by drugs. *Nucleic Acids Research* 52(D1):D1393–D1399 (2024). DOI: `10.1093/nar/gkad1042`.
9. Lulu Li 等. NoncoRNA: a database of experimentally supported non-coding RNAs and drug targets in cancer. *Journal of Hematology & Oncology* 13:15 (2020). DOI: `10.1186/s13045-020-00849-7`.
10. Xinyi Liu 等. SM2miR: a database of the experimentally validated small molecules' effects on microRNA expression. *Bioinformatics* 29(3):409–411 (2013). DOI: `10.1093/bioinformatics/bts698`.

11. RNAincoder. *Nucleic Acids Research* 51(W1):W509–W519 (2023). DOI: `10.1093/nar/gkad404`。
12. RNAmigos. *Nucleic Acids Research* 48(14):7690–7699 (2020). DOI: `10.1093/nar/gkaa583`。
13. RNAmigos2. *Nature Communications* 16:2799 (2025). DOI: `10.1038/s41467-025-57852-0`。
14. RSAPred. *Briefings in Bioinformatics* 25(2):bbae002 (2024). DOI: `10.1093/bib/bbae002`。
15. RNAsmol. *Nature Computational Science* 5(8):648–660 (2025). DOI: `10.1038/s43588-025-00820-x`。
16. RNA-FM. arXiv:2204.00300 (2022). DOI: `10.48550/arXiv.2204.00300`。
17. RNAErnie. *Nature Machine Intelligence* 6(5):548–557 (2024). DOI: `10.1038/s42256-024-00836-4`。
18. BiRNA-BERT. *Communications Biology* 8:1621 (2025). DOI: `10.1038/s42003-025-08982-0`。
19. ChemBERTa. arXiv:2010.09885 (2020). DOI: `10.48550/arXiv.2010.09885`。
20. TransDTI. *ACS Omega* 7(3):2706–2717 (2022). DOI: `10.1021/acsomega.1c05203`。
21. C2P2 cold-start DTA. *Briefings in Bioinformatics* 23(4):bbac269 (2022). DOI: `10.1093/bib/bbac269`。
22. GraphDTA. *Bioinformatics* 37(8):1140–1147 (2021). DOI: `10.1093/bioinformatics/btaa921`。
23. DrugBAN. *Nature Machine Intelligence* 5(2):126–136 (2023). DOI: `10.1038/s42256-022-00605-1`。
24. Toward more realistic drug-target interaction predictions. *Briefings in Bioinformatics* 16(2):325–337 (2015). DOI: `10.1093/bib/bbu010`。
25. SEAL. *NeurIPS 2018*:5165–5175。
26. BPR. *UAI 2009*:452–461。
27. MoleculeNet. *Chemical Science* 9(2):513–530 (2018). DOI: `10.1039/C7SC02664A`。
28. Davis–Goadrich PR/ROC. *ICML 2006*:233–240. DOI: `10.1145/1143844.1143874`。
29. Saito–Rehmsmeier PRC. *PLOS ONE* 10(3):e0118432 (2015). DOI: `10.1371/journal.pone.0118432`。
30. miRBase. *Nucleic Acids Research* 42(D1):D68–D73 (2014). DOI: `10.1093/nar/gkt1181`。
31. PubChem 2023. *Nucleic Acids Research* 51(D1):D1373–D1380 (2023). DOI: `10.1093/nar/gkac956`。
32. RNAInter v4.0. *Nucleic Acids Research* 50(D1):D326–D332 (2022). DOI: `10.1093/nar/gkab997`。
33. lncRNAdb v2.0. *Nucleic Acids Research* 43(D1):D168–D173 (2015). DOI: `10.1093/nar/gku988`。
34. DrugBank 5.0. *Nucleic Acids Research* 46(D1):D1074–D1082 (2018). DOI: `10.1093/nar/gkx1037`。
35. Rfam 14. *Nucleic Acids Research* 49(D1):D192–D200 (2021). DOI: `10.1093/nar/gkaa1047`。

> 35 篇条目的存在性、元数据与正文语境均已审计；32 篇有全文或权威完整来源核验，其余访问边界见 `CITATION_AUDIT.md`。期刊作者指南请求 35–55 篇，本稿达到下限，不再为数量继续扩引。
