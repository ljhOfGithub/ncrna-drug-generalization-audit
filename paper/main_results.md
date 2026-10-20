# 投稿主结果证据表

> 本表由 `paper_evidence_matrix.py` 从冻结结果自动生成；AP 为 full-candidate drug-macro average precision。PASS 只指对应预注册局部门，不等于论文或算法整体通过。

| ID | 数据与协议 | 候选 vs 基线 | AP | ΔAP（95% CI） | 方向 | 门 | 论文角色 |
|---|---|---|---:|---:|---:|---|---|
| `mi_scaffold_seed_20261019_vs_prior` | Mi; 5-fold scaffold-disjoint full-candidate | ChemBERTa pairwise prior-residual vs RNA prior | 0.161748 vs 0.157509 | +0.004239 [+0.002812, +0.005899] | 5/5 folds | FAIL (+0.01 gate) | development result |
| `mi_scaffold_seed_20261020_vs_prior` | Mi; second 5-fold scaffold-disjoint full-candidate | ChemBERTa pairwise prior-residual vs RNA prior | 0.159039 vs 0.156158 | +0.002881 [+0.001047, +0.004782] | 4/5 folds | FAIL (+0.01 gate) | split sensitivity |
| `mi_scaffold_candidate_vs_localgl` | Mi; same 5-fold scaffold-disjoint full-candidate | ChemBERTa pairwise prior-residual vs ncRD-LG LocalGL dynamic-resampling adaptation | 0.161748 vs 0.153275 | +0.008473 [+0.005320, +0.011759] | 5/5 folds | PASS public-baseline gate | main protocol comparison |
| `mi_scaffold_candidate_vs_schemnet_no_seq` | Mi; same 5-fold scaffold-disjoint full-candidate; 3 training seeds | ChemBERTa pairwise prior-residual vs sChemNET no-sequence MACCS adaptation | 0.161748 vs 0.154500 | +0.007248 [+0.004751, +0.009681] | 5/5 folds | PASS direct-baseline gate | direct structural-baseline comparison |
| `mi_scaffold_candidate_vs_plmf_mda` | Mi; same 5-fold scaffold-disjoint full-candidate; 3 training seeds | ChemBERTa pairwise prior-residual vs PLMF-MDA independent strict adaptation | 0.161748 vs 0.135050 | +0.026698 [+0.021679, +0.031884] | 5/5 folds | PASS direct-baseline gate | direct language-model baseline comparison |
| `ncrnadrug_drug_cold_vs_prior` | ncRNADrug; degree-balanced five-fold drug-cold full-candidate | RNA-FM + ECFP pairwise prior-residual vs RNA prior | 0.114019 vs 0.106438 | +0.007581 [+0.001838, +0.013747] | 5/5 folds | PASS | overlap-sensitive external result |
| `noncorna_drug_cold_vs_prior` | NoncoRNA; degree-balanced five-fold drug-cold full-candidate | RNA-FM + ECFP pairwise prior-residual vs RNA prior | 0.109175 vs 0.105596 | +0.003579 [-0.003311, +0.011684] | 2/5 folds | FAIL | external boundary |
| `ncrnadrug_entity_deoverlap_vs_prior` | ncRNADrug minus Mi-name-overlap entities; degree-balanced five-fold drug-cold full-candidate | RNA-FM + ECFP pairwise prior-residual vs RNA prior | 0.063689 vs 0.076418 | -0.012729 [-0.046089, +0.017057] | 3/5 folds | FAIL | main overlap audit |
| `sm2mir_virgin_drug_temporal_vs_prior` | SM2miR non-Mi CIDs; 2011-2014 first-seen drug temporal mini-holdout | ECFP pairwise prior-residual vs RNA prior | 0.068890 vs 0.088766 | -0.019876 [-0.046937, +0.002955] | 12/18 drugs | FAIL | independent-label boundary |
| `rahgl_fixed_drug_cold_vs_prior` | RAHGL-MDR; author fixed drug-cold folds; 3 training seeds | entity-balanced pairwise prior-residual vs RNA prior | 0.184244 vs 0.170664 | +0.013580 [+0.005139, +0.024170] | 5/5 folds | PASS drug-cold gate | split-limited positive result |
| `rahgl_scaffold_cold_vs_prior` | RAHGL-MDR; 5-fold scaffold-disjoint; 3 training seeds | entity-balanced pairwise prior-residual vs RNA prior | 0.175435 vs 0.175139 | +0.000296 [-0.007782, +0.008476] | 2/5 folds | FAIL | main split-dependence audit |
| `pmid_replication_vs_replicated_rna_prior` | Mi pairs with distinct-PMID support; 5-fold scaffold-disjoint replication target | replication-label ECFP pairwise residual vs replicated-pair frequency prior | 0.157118 vs 0.146185 | +0.010933 [+0.007037, +0.016041] | 5/5 folds | SUBTARGET PASS | within-target positive control |
| `pmid_replication_vs_reported_rna_prior` | Mi pairs with distinct-PMID support; 5-fold scaffold-disjoint replication target | replication-label ECFP pairwise residual vs all-reported RNA prior | 0.157118 vs 0.192462 | -0.035344 [-0.053405, -0.019741] | 0/5 folds | OVERALL FAIL | main selection-process audit |

## 读取边界

- `PASS public-baseline gate`：只支持候选优于本研究严格适配的 LocalGL；不支持优于 RNA prior 或算法新颖性。
- `PASS direct-baseline gate`：只支持候选优于本研究独立重实现的 sChemNET 无序列消融；不支持优于完整 sChemNET、RNA prior 或 SOTA。
- `PASS drug-cold gate`：在作者固定 drug-cold 折成立；同一候选在 scaffold-disjoint 中失败，不能外推为结构泛化。
- `SUBTARGET PASS`：只说明稀疏复现标签内部存在结构信号；相对全部报道 prior 的整体门失败。
- 所有来源文件逐行保存在 CSV 的 `sources` 列，便于复算和审稿核验。
