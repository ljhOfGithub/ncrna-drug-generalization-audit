# 论文主张—冻结证据审计

- 审计日期：2026-10-20
- 审计对象：`paper/manuscript_zh_cn.md`
- 独立性：`same-family`（全新零上下文审计代理）
- 接受状态：`provisional`
- 判定：**PASS**
- 投稿就绪：**否**

该 PASS 只表示当前简体中文稿件的定量主张、统计口径和冻结证据一致；不证明新颖性、许可完备、公开发布完成、干净 checkout 全流程复现或投稿就绪。

## 问题计数

- Critical：0
- Major：0
- Minor：0

前两轮审计发现的 ChemBERTa–ECFP 无证据精确比较、未打包的精确跨库交集数、折级“提高/不下降”口径、两阶段 hurdle 范围和 RAHGL 确认门描述均已在当前稿件中修正。

## 核心核验结果

1. 主表 13 项比较的 AP、差值、区间和折数均对应冻结证据；`candidate_ap - baseline_ap - delta` 最大绝对误差为 `8.33e-17`。
2. RAHGL-MDR 固定普通 drug-cold：候选 `0.1842441003`、prior `0.1706644173`、差值 `+0.0135796830`、95% 区间 `[0.0051391472,0.0241701763]`、`5/5` 折不下降，三种子逐药物重算吻合。
3. RAHGL-MDR scaffold-disjoint：候选 `0.1754354585`、prior `0.1751391034`、差值 `+0.0002963550`、95% 区间 `[-0.0077824377,0.0084759677]`、`2/5` 折不下降；三个种子差值 `+0.0053386422`、`+0.0082173365`、`-0.0126669135`，聚类 bootstrap 重算吻合。
4. Mi 两个严格划分、LocalGL、sChemNET、PLMF-MDA、ncRNADrug 去重前后、NoncoRNA、SM2miR 时间子集、PMID 再支持和两阶段权重选择均与冻结文件吻合。
5. 当前主张限定在固定普通 drug-cold 协议；稿件没有把协议差异、实体去重差异或 PMID 支持解释为已识别的因果机制，也没有把结果推广为普适新骨架性能。

## 输入哈希

| 文件 | SHA-256 |
|---|---|
| `paper/manuscript_zh_cn.md` | `8997bd206bd1e438c73d8c7a7781b645bf2da916c9970d550b4f6f64d8d78f48` |
| `paper/main_results.csv` | `dcb475f272d3d51300520d56f863609eb0aa41a2f7ad2e9fbc1679ed44282986` |
| `results/rahgl-objective-alignment-confirmation-20261020/summary.json` | `1400f867ef8229134b349c4ab5bfddf94aa2a5a0d676bfb49730bf57f85a82e5` |
| `results/rahgl-scaffold-cold-confirmation-20261020/summary.json` | `badf96d75fa7d243f15720a89dec60ada4448c051252af67bf56bad8bc18627f` |
| `results/chemberta-pairwise-residual-pilot-20261019/mi_config.json` | `0019099adeb1d1f8697d45ac2bb994e0e9f25aa9e9307664451b6e5e8a603653` |
| `results/chemberta-pairwise-residual-confirmation-seed-20261020/mi_config.json` | `ae914074af237db5496446750266c30c90001f7dcb9937c0622957a4177e7cc6` |
| `results/ncrdlg-localgl-scaffold-resampling-sensitivity-20261020/aggregate/mi_config.json` | `841c748fd2d0107fbe935d7e063b594909df80942d14b870b5da53086bd097d0` |
| `results/schemnet-strict-scaffold-baseline-20261020/summary.json` | `16e4ffb7a6fcdf4db0341d006fbbb1453eeb080896454e3ec2480c6504aec35b` |
| `results/plmf-mda-strict-scaffold-baseline-20261020/summary.json` | `bdaed9e8184bfd053d240fcf9ba10837b46b321b768e7978a3eeac25227adc37` |
| `results/hmvcc-drug-cold-confirmation-20261019/combined_config.json` | `11790a58d1be1e05da9f6e8470aa3a964f39a6287bff0766f6651250d1e8f330` |
| `results/hmvcc-mi-deoverlap-confirmation-20261019/combined_config.json` | `9029b198108b38bf5d1a1ac6d9a2760f3a318bdd173ac22b8d7c33c87a9eb861` |
| `results/hmvcc-drug-cold-confirmation-20261019/NoncoRNA_full_candidate_summary.csv` | `09396d23709fd0b6b13996faccfee8984e18c32c98e8a9694aaef72885d181f0` |
| `results/sm2mir-virgin-drug-temporal-20261019/config.json` | `c204a63078fa137c20fcf073ca8f14380efd21aa3c65b5492c970148292de9ef` |
| `results/independent-source-replication-pilot-20261020/summary.json` | `2d99b2d03de351fff3cc8b344f26fc621c007d299fcd0b77b450212d2f16037c` |
| `results/two-stage-replication-hurdle-pilot-20261020/validation_selection.csv` | `382009456f8d5001a965f2f8a0a8565aa6d80c76ce7a2cebb2a4baea072fbee3` |

## 未由本审计验证

- 近邻论文全文与检索覆盖的完整性；
- 正式文献标识和新颖性成立；
- 第三方许可状态；
- 公开仓库或公开 release 已完成；
- 干净 checkout 的完整训练复现；
- 投稿系统所需作者、单位、伦理、基金和利益冲突信息。

