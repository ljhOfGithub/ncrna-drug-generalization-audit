# 核心引用审计

核验日期：2026-10-20  
范围：英文稿当前引用的 7 篇核心方法工作和 3 篇数据资源论文  
审计独立性：`same-family`  
接受状态：`provisional`

## 总结

- 10/10 个 DOI/正式身份存在。
- 3 条可原样保留：ncRD-LG、RAHGL-MDR、GCFMCL（GCFMCL 需限定为源码中的表征学习阶段 BPR）。
- 3 条需修正语境或年份：HMVCC、MGCNA、sChemNET。
- 1 条原复合记录必须移除后以真实论文整体替换：PLMF-MDA。原记录把真实 DOI 与错误作者、错误题名、错误方法拼接在一起。
- 所有确定性修正已写入 `manuscript_en.md`、`manuscript_zh_cn.md` 和 `references_verified.bib`。
- 当前为 7 篇核心方法引用和 3 篇直接使用的数据资源引用。未核实到 *Pattern Recognition* 官方作者指南存在“35--55 篇”硬性或建议范围；此前该数字只能视为内部覆盖目标，不能作为投稿门槛。相关工作覆盖仍偏窄，但不得为凑数加入未读或不支撑正文的文献。

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
- 全程未使用内置浏览器、Edge、调试端口或新 profile，未绕过 CAPTCHA/Cloudflare，未提交表单或凭据。

## 投稿前仍需处理

1. 扩充并逐条核验完整相关工作集；不得为达到数量而填充未读文献。
2. GCFMCL 若在相关工作中承担超出 BPR 源码先例的实质论述，必须先取得并精读合法全文。
3. 参考文献增补后重新运行逐条存在性和语境审计，并维持 `same-family/provisional` 限定，除非取得真正独立 reviewer。
