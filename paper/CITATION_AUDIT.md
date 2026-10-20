# 核心引用审计

核验日期：2026-10-20  
范围：英文稿当前实际引用的 35 篇论文
审计独立性：`same-family`  
接受状态：`provisional`

## 总结

- 35/35 个正式身份存在；31 篇有 DOI，SEAL 与 BPR 以正式会议论文集核验，RNA-FM 与 ChemBERTa 以明确标注的 arXiv 预印本身份引用。
- 3 条可原样保留：ncRD-LG、RAHGL-MDR、GCFMCL（GCFMCL 需限定为源码中的表征学习阶段 BPR）。
- 3 条需修正语境或年份：HMVCC、MGCNA、sChemNET。
- 1 条原复合记录必须移除后以真实论文整体替换：PLMF-MDA。原记录把真实 DOI 与错误作者、错误题名、错误方法拼接在一起。
- 所有确定性修正已写入 `manuscript_en.md`、`manuscript_zh_cn.md` 和 `references_verified.bib`。
- *Pattern Recognition* Guide for Authors 已核实：普通论文建议 20--35 页，并请求 35--55 篇近期、相关且来源多样的参考文献。当前稿件恰有 35 篇，全部在正文实际使用；数量达标不替代语境核验。

## 逐条结论

| 编号 | 工作 | 原审计判定 | 修正后状态 | 关键边界 |
|---|---|---|---|---|
| 1 | ncRD-LG | KEEP | 可保留 | 主协议为 60/20/20 pair split；leave-drug、leave-ncRNA、scaffold-based splitting 是未来工作 |
| 2 | RAHGL-MDR | KEEP | 可保留 | full-candidate 覆盖 cold-start；“未见实体”仍可使用实体特征和辅助生物关系；未独立审计作者代码 |
| 3 | HMVCC | FIX | 已修正 | 任务是 ncRNA–drug，不应缩窄为 miRNA–drug；正式卷期年份为 2027，online 2026 |
| 4 | MGCNA | FIX | 已修正 | DOI 对应 Nan Sheng 等的 multi-view GCN 论文，不是 Jia Zhang 等的 miRNA-disease/collective-neighborhood 条目 |
| 5 | PLMF-MDA | REMOVE 原复合条目 | 已整体替换 | DOI 对应 Nan Sheng 等的 PLM + CNN/GCN + cross-modal attention 论文，不是 Diler 的 miRNA-disease/LMF 方法 |
| 6 | sChemNET | FIX | 已修正 | 作者评估 Tanimoto `<0.6` 的化学不相似子集；不能写成 Bemis–Murcko scaffold split |
| 7 | GCFMCL | KEEP（限定语境） | 可保留 | 固定提交源码在表征学习阶段采用 drug-as-user BPR，最终分类阶段使用 MLP + BCE；未取得 OUP 全文 |
| 8 | ncRNADrug | KEEP | 可保留 | 官方 PMC 全文核对；只支撑数据库来源、收录范围与重叠审计语境 |
| 9 | NoncoRNA | KEEP | 可保留 | 官方 PMC 全文核对；只支撑数据库来源与人工整理范围 |
| 10 | SM2miR | KEEP（来源限定） | 可保留 | PubMed 正式记录、摘要及 ncRNADrug 全文中的回溯描述已核；OUP 全文受 Cloudflare 阻断，不声称全文精读 |

## 新增 25 篇逐条用途与边界

| 工作 | 正式身份/全文证据 | 正文用途 | 不支持的更强主张 |
|---|---|---|---|
| RNAincoder | NAR 2023；PMC 全文与 PDF | RNA/化合物多描述符编码先例 | 不支持 scaffold-cold 或完整候选排名 |
| RNAmigos | NAR 2020；PMC 全文 | 结构口袋图与 decoy 排名先例 | 不是 ncRNA–drug 关联数据库评估 |
| RNAmigos2 | Nature Communications 2025；PMC 全文 | 结构簇隔离与大规模虚拟筛选 | 结构口袋 split 不等于药物 Bemis--Murcko split |
| RSAPred | Briefings in Bioinformatics 2024；PMC 全文 | RNA–小分子亲和力回归与外部集 | 端点不是完整候选 AP |
| RNAsmol | Nature Computational Science 2025；最终 DOI 元数据＋作者公开全文预印本 | RNA/小分子/双方 cold 定义与 decoy 评估 | 冷小分子身份不自动等于新 scaffold |
| RNAErnie | Nature Machine Intelligence 2024；正式全文 | motif-aware RNA 预训练先例 | 不支持药物关联外推 |
| BiRNA-BERT | Communications Biology 2025；PMC 全文 | 自适应 tokenization 与多 RNA 下游任务 | 不支持化学 scaffold 结论 |
| RNA-FM | arXiv:2204.00300；官方预印本全文 | 大规模 ncRNA 自监督表示 | 预训练表示不等于下游 scaffold 泛化 |
| ChemBERTa | arXiv:2010.09885；官方预印本全文 | SMILES 预训练与 MoleculeNet scaffold 任务 | 文中结果并非 ncRNA–drug 关联结果 |
| TransDTI | ACS Omega 2022；PMC 全文 | 语言模型用于 DTI | 外部集不自动证明实体或 scaffold 独立 |
| C2P2 cold-start DTA | Briefings in Bioinformatics 2022；PMC 全文 | 未见药物/靶点与辅助知识迁移 | 未报告 Bemis--Murcko scaffold 隔离 |
| GraphDTA | Bioinformatics 2021；作者公开 PDF | 分子图＋蛋白序列 DTA | 主实验为 pair split，不是 strict cold |
| DrugBAN | Nature Machine Intelligence 2023；arXiv 全文 | unseen entity 与聚类跨域评估；指出相似药物可使 naive unseen-drug 过易 | 不能把其 unseen-drug 结果称作 scaffold 泛化 |
| Pahikkala et al. | Briefings in Bioinformatics 2015；PMC 全文 | S1--S4 协议和 nested-CV 边界 | 不直接提供本文数据上的性能结论 |
| SEAL | NeurIPS 2018；正式论文全文 | 局部 enclosing subgraph 链接预测先例 | 不支持本文具体 biological endpoint |
| BPR | UAI 2009；正式论文全文 | implicit-feedback pairwise ranking 先例 | 不把 unobserved pair 变成实验阴性 |
| MoleculeNet | Chemical Science 2018；PMC 全文 | 随机 split 与 scaffold split 的化学学习区别 | benchmark 定义不证明本文模型稳健 |
| Davis--Goadrich | ICML 2006；正式论文全文 | ROC/PR 关系及不等价优化目标 | 不单独决定本文统计设计 |
| Saito--Rehmsmeier | PLOS ONE 2015；PMC 全文 | 类别不平衡时 PR 的解释优势 | 不说明任一具体模型优劣 |
| miRBase | NAR 2014；PMC 全文 | miRNA 命名与注释置信边界 | 收录不等于统一实验质量 |
| PubChem 2023 | NAR 2023；PMC 全文 | Substance/Compound 与结构标准化语境 | 聚合记录不等于相同生物端点 |
| RNAInter v4.0 | NAR 2022；PMC 全文 | 混合证据类型与置信分数 | 预测条目或缺失条目不是真阴性 |
| lncRNAdb v2.0 | NAR 2015；PMC 全文 | 人工整理的功能性 lncRNA 证据范围 | 小型已表征集合不代表完整 lncRNA 空间 |
| DrugBank 5.0 | NAR 2018；PMC 全文 | 药物标识、人工整理与预测字段并存 | 不把全部字段当成同一证据等级 |
| Rfam 14 | NAR 2021；PMC 全文 | RNA 家族、比对与 covariance model 资源边界 | 不是药物响应标签库 |

## 规范书目信息

1. Yuran Xie, Wei Wang, Jia Xu, Linyang Li, Shuai Wu, Hang Wei. “ncRD-LG: A unified framework integrating molecular language models and subgraph learning for drug–ncRNA target prediction.” *Pattern Recognition* 179, Part A (2026): 113556. DOI `10.1016/j.patcog.2026.113556`.
2. Murtada K. Elbashir. “Relation-Aware Heterogeneous Graph Learning for miRNA–Drug Response Association Prediction Under Cold-Start Generalization.” *International Journal of Molecular Sciences* 27(20) (2026): 9013. DOI `10.3390/ijms27209013`.
3. Zhihao Ma, Yu Chen, Hailing Wang, Xidong Xi, Guitao Cao, Lei Deng, Min Wu. “Hypergraph multi-view learning for ncRNA–drug association prediction with cluster anchors and contrastive alignment.” *Expert Systems with Applications* 334, Part D (2027): 134658. DOI `10.1016/j.eswa.2026.134658`; online 2026.
4. Nan Sheng, Yunzhi Liu, Ling Gao, Lei Wang, Lan Huang, Yan Wang. “Multi-view fusion based on graph convolutional network with attention mechanism for predicting miRNA related to drugs.” *PLOS Computational Biology* 21(11) (2025): e1013703. DOI `10.1371/journal.pcbi.1013703`.
5. Nan Sheng, Yunzhi Liu, Ling Gao, Wenju Hou, Lan Huang, Yan Wang. “A pre-trained language model-based cross-modal fusion framework for predicting miRNA-drug resistance and sensitivity associations.” *PLOS Computational Biology* 22(2) (2026): e1013968. DOI `10.1371/journal.pcbi.1013968`.
6. Diego Galeano et al. “sChemNET: a deep learning framework for predicting small molecules targeting microRNA function.” *Nature Communications* 15 (2024): 9149. DOI `10.1038/s41467-024-49813-w`.
7. Jinhang Wei, Linlin Zhuo, Zhecheng Zhou, Xinze Lian, Xiangzheng Fu, Xiaojun Yao. “GCFMCL: predicting miRNA-drug sensitivity using graph collaborative filtering and multi-view contrastive learning.” *Briefings in Bioinformatics* 24(4) (2023): bbad247. DOI `10.1093/bib/bbad247`.
8. Xinyu Cao et al. “ncRNADrug: a database for validated and predicted ncRNAs associated with drug resistance and targeted by drugs.” *Nucleic Acids Research* 52(D1) (2024): D1393--D1399. DOI `10.1093/nar/gkad1042`.
9. Lulu Li et al. “NoncoRNA: a database of experimentally supported non-coding RNAs and drug targets in cancer.” *Journal of Hematology & Oncology* 13 (2020): 15. DOI `10.1186/s13045-020-00849-7`.
10. Xinyi Liu et al. “SM2miR: a database of the experimentally validated small molecules' effects on microRNA expression.” *Bioinformatics* 29(3) (2013): 409--411. DOI `10.1093/bioinformatics/bts698`.

## 来源与访问边界

- ncRD-LG、HMVCC：系统 Chrome 默认用户目录普通标签页，在显示 PolyU 机构访问的 ScienceDirect 正式全文核验。
- RAHGL-MDR：MDPI 正式全文。
- MGCNA、PLMF-MDA：PLOS 正式全文；均读至结论/参考文献边界。
- sChemNET：Nature 正式 HTML、官方 PDF和官方补充材料；补充材料未纳入发布包。
- GCFMCL：PubMed 正式身份记录与官方 GitHub 固定提交源码。OUP 页面停在 Cloudflare 验证，未绕过，故不声称完成全文精读。
- ncRNADrug、NoncoRNA：系统 Chrome 读取官方 PMC 全文至参考文献/数据可用性边界。
- SM2miR：PubMed 正式身份、全体作者、摘要、卷页和 DOI 已核；OUP HTML/PDF 均停在 Cloudflare 验证。其作为历史快照来源的语境还由 ncRNADrug 官方 PMC 全文交叉核对，但不写成已完成原文全文精读。
- 新增 25 篇：通过系统 Chrome 默认用户目录从 Google 精确题名回到 PubMed/PMC、Nature、arXiv、NeurIPS/UAI 或作者公开版本；可下载文件先用 `file`/`pdfinfo` 核身份，再逐节读取到结论、数据可用性或附录边界。ACS 的 Bemis--Murcko 原文触发 Cloudflare 后未绕过，故未纳入引用；scaffold split 的定义改由已全文核实的 MoleculeNet 支撑。
- 全程未使用内置浏览器、Edge、调试端口或新 profile，未绕过 CAPTCHA/Cloudflare，未提交表单或凭据。

## 投稿前仍需处理

1. GCFMCL 若在相关工作中承担超出 BPR 源码先例的实质论述，必须先取得并精读合法全文。
2. 当前 35 篇均已完成存在性与语境复核；仍维持 `same-family/provisional`，除非取得真正独立 reviewer。
3. 投稿前只允许修正元数据或语境，不以增加数量为目的继续扩展引用。
