# Drug-Cold Gains Do Not Persist under Scaffold Separation in ncRNA–Drug Prediction

> Manuscript status: English submission draft derived from the frozen Chinese factual manuscript. Numerical results are frozen. Author identity, affiliation, licensing, ethics, CRediT, AI-use disclosure, funding, competing interests, originality and submission status, 35 audited references, and the public versioned release are recorded. A permanent archive DOI has not been assigned and is not represented as already assigned.

**Author:** Jihao Li  
**Affiliation:** Independent Researcher, Shenzhen, Guangdong, China  
**Corresponding author:** Jihao Li, Shenzhen, Guangdong, China; jihao.li@polyu.edu.hk

## Abstract

Drug–non-coding RNA (ncRNA) association models are often evaluated using random pair splits or ordinary entity cold-start protocols. However, holding out drug identities does not establish extrapolation to unseen chemical scaffolds. We froze and compared two protocols: the public RAHGL-MDR ordinary drug-cold full-candidate ranking and a strict split with no Bemis–Murcko scaffold shared across training, validation, and test sets. On the fixed RAHGL-MDR folds, an entity-balanced prior-residual candidate achieved a drug-macro average precision (AP) of 0.184244 versus 0.170664 for a training-only RNA-frequency prior, a gain of 0.013580 (95% paired-bootstrap interval, 0.005139–0.024170; non-decreasing in 5/5 folds). Under the scaffold-disjoint protocol, candidate and prior AP were 0.175435 and 0.175139, respectively, yielding a gain of 0.000296 (scaffold-cluster 95% interval, −0.007782–0.008476; non-decreasing in 2/5 folds), with one of three training seeds producing a negative gain. On the Mi data, the candidate exceeded strict adaptations of LocalGL, a sequence-free sChemNET ablation, and PLMF-MDA, but improved over the RNA prior by only 0.004239, below the prespecified 0.01 materiality threshold. Cross-database de-overlap also changed the ncRNADrug gain from 0.007581 to −0.012729. The supported conclusion is conditional: the candidate improves new-drug ranking under the fixed ordinary drug-cold protocol, but the present scaffold-disjoint evaluation does not confirm robust gain for unseen chemical cores. New-drug studies should jointly report full-candidate ranking, strong frequency priors, scaffold separation, and source-overlap audits.

**Keywords:** ncRNA–drug association; drug cold start; scaffold-disjoint split; full-candidate ranking; frequency prior; evaluation protocol

## 1. Introduction

Drug–ncRNA association prediction seeks to recover or extend potentially relevant associations from previously reported relations. The task lies between interaction prediction and retrieval: for each drug, a model ranks a large candidate set in which reported positives are sparse and unreported pairs remain unlabeled. Related RNA–small-molecule systems span feature encoders, affinity regressors, structure-based virtual screening, and sequence-based interaction scoring [11–15]. Their inputs, endpoints, negative constructions, and candidate spaces differ, so their reported numbers are not directly interchangeable.

Recent ncRNA–drug work has used graph neural networks, local subgraphs, multi-view representations, and biological language models, while evaluation has expanded from random pair splits to drug-cold, RNA-cold, and double-cold protocols. A random pair split allows shared entities; ordinary drug-cold withholds test-drug identities but may retain related chemical cores; scaffold-disjoint further requires unseen structural cores. This parallels the S1–S4 distinction in drug–target prediction [24]. Without this separation, “new-drug prediction” can be misread as the unsupported stronger claim of extrapolation to new chemical scaffolds.

A second issue is the strength of simple priors. In full-candidate ranking, reporting frequencies differ markedly across RNAs. Ranking candidates only by RNA frequency in the training set can therefore provide a strong drug-independent baseline. A model may outperform more complex public neural systems while adding little over this prior. Likewise, database-level validation may reuse RNAs, drugs, and positive pairs. Calling a second database independent without auditing these overlaps can overstate the evidence.

This study does not propose a universally superior algorithm. Instead, it freezes a conditional question: can an entity-balanced prior-residual ranker reliably improve full-candidate ranking for unseen drug identities under an ordinary drug-cold protocol, and does that advantage persist under strict separation of chemical scaffolds? We additionally use Mi, ncRNADrug, NoncoRNA, a historical SM2miR snapshot, and labels supported by distinct PubMed identifiers to examine how strong priors, structural separation, entity overlap, and source independence affect the conclusion [8–10].

The contributions are as follows:

1. We report a frozen conditional result. On the fixed RAHGL-MDR drug-cold folds, the candidate improves AP over the RNA prior by 0.013580; under the present strict scaffold-disjoint protocol, the gain is only 0.000296 and its uncertainty interval crosses zero.
2. We define an evaluation ladder that distinguishes random-pair, entity-cold, scaffold-cold, temporal-new-drug, and independent-source targets, using full-candidate drug-macro AP as the common primary endpoint.
3. We evaluate strict adaptations of ncRD-LG LocalGL, a sequence-free sChemNET ablation, and PLMF-MDA on the same endpoint, while distinguishing original implementations, independent adaptations, and non-comparable reported results.
4. We quantify entity and positive-pair overlap between Mi and ncRNADrug and use de-overlap, temporal-new-drug, and distinct-PubMed analyses to expose dependence in apparent external evidence.
5. We provide a local evidence package that rebuilds the frozen main table and figures from summary/configuration files and records failed routes and prohibited claims.

## 2. Related work

### 2.1. RNA–small-molecule and ncRNA–drug prediction

RNAincoder learns representations from RNA and compound descriptors [11]. RNAmigos predicts ligand fingerprints from RNA-pocket graphs and ranks native ligands among decoys [12], while RNAmigos2 adds large-scale docking supervision and binding-site cluster separation [13]. RSAPred evaluates RNA–small-molecule affinity regression [14]. RNAsmol reports RNA-cold, small-molecule-cold, double-cold, and decoy-ranking evaluations [15]. These studies establish relevant modeling precedents, but their endpoints are not equivalent to full-candidate drug-macro AP on association databases.

ncRD-LG combines biological language models with local semantic subgraphs for drug–ncRNA association prediction. Its principal protocol is a random pair-level split, while leave-one-drug-out, leave-one-ncRNA-out, and scaffold-based splitting are identified as future evaluation directions [1]. RAHGL-MDR evaluates leakage-controlled edge, miRNA-cold, drug-cold, and double-cold settings and includes full-candidate ranking and degree/popularity baselines [2]. Cold-start evaluation and full-candidate ranking are therefore not new in this study.

HMVCC reports edge-level, cross-species, cross-database, and drug-cold settings for ncRNA–drug association prediction [3]. MGCNA learns multi-view graph-convolutional representations for miRNA–drug association prediction, whereas PLMF-MDA combines RNA-FM, ChemBERTa-2, intrinsic encoders, and cross-modal attention for miRNA–drug resistance and sensitivity associations [4,5]. sChemNET directly studies small molecules targeting microRNA function and evaluates chemically dissimilar test subsets using a molecular-fingerprint similarity threshold; this is not a Bemis–Murcko scaffold split [6]. The public GCFMCL implementation uses drug-as-user Bayesian personalized ranking during representation learning, so we do not claim to introduce pairwise ranking for this task [7].

### 2.2. Pretrained representations and cold-start transfer

RNA-FM, RNAErnie, and BiRNA-BERT learn transferable RNA representations from large sequence corpora [16–18], whereas ChemBERTa pretrains on SMILES and evaluates molecular-property tasks including scaffold splits [19]. In drug–target prediction, TransDTI and GraphDTA use language or graph representations [20,22], C2P2 transfers auxiliary interaction knowledge to unseen drugs or targets [21], and DrugBAN compares random, unseen-entity, cold-pair, and clustering-based cross-domain protocols [23]. DrugBAN specifically notes that identity-level unseen-drug evaluation can remain easy when highly similar molecules cross the partition. Pretraining and identity novelty therefore do not by themselves establish chemical-core novelty.

### 2.3. Local subgraphs, ranking, and evaluation design

SEAL establishes local enclosing subgraphs as a general link-prediction strategy [25], while BPR formalizes pairwise learning from implicit feedback without treating every missing entry as a verified negative [26]. Pahikkala et al. separate pair-wise, unseen-drug, unseen-target, and double-unseen settings [24]. MoleculeNet likewise warns that random splitting is often inappropriate for chemical data and uses scaffold grouping as a stronger structural test [27]. Precision–recall analysis is especially informative for imbalanced candidate spaces, and optimizing ROC area does not guarantee optimizing PR area [28,29].

### 2.4. Identifier and evidence provenance

miRBase and Rfam provide complementary sequence naming and family-annotation resources [30,35]. PubChem distinguishes depositor-provided substances from standardized compound structures [31]. RNAInter mixes experimental and computational interactions [32], lncRNAdb focuses on manually curated functional evidence [33], and DrugBank includes both curated and predicted fields under source-specific terms [34]. These differences motivate explicit normalization and provenance audits; absence from a database is not a confirmed biological negative.

As of the freeze date, our bounded full-text review found no single direct neighbor that jointly reports Bemis–Murcko scaffold separation, full-candidate drug-macro AP, a training-only RNA-frequency prior, cross-database entity de-overlap, temporal-new-drug evidence, and labels supported by distinct PubMed identifiers in one ncRNA–drug audit. This is a provisional gap under a bounded search, not a claim of priority or exhaustive absence.

## 3. Methods

### 3.1. Task and estimand

Given reported positive ncRNA–drug associations in a training set, the model scores the full set of candidate ncRNAs for each held-out drug. The primary metric is average precision for each drug, macro-averaged over test drugs. Database-unrecorded pairs are treated as unlabeled candidates, not as experimentally verified biological negatives.

We distinguish two main protocols:

- **Ordinary drug-cold:** drug identities are mutually exclusive across training, validation, and test sets, but scaffolds are not forced to be disjoint. We interpret this only as entity cold start on the fixed RAHGL-MDR folds, not as a universal deployment distribution.
- **Strict scaffold-disjoint:** Bemis–Murcko scaffolds define groups that do not overlap across training, validation, and test sets. Acyclic molecules are grouped by canonical SMILES. This protocol represents a stronger unseen-core requirement.

Ordinary drug-cold evaluation does not imply that every test drug shares a training scaffold, and it is not equivalent to strict scaffold extrapolation. We compare two frozen protocols and do not attribute their difference to a single leakage mechanism.

### 3.2. Protocol hierarchy and split construction

Random-pair, drug-cold, double-cold, scaffold-disjoint, and temporal-new-drug protocols estimate different deployment questions rather than one monotone difficulty scale. Identity-disjoint drugs may still share close analogues or the same two-dimensional core with training drugs. The ordinary protocol uses the fixed RAHGL-MDR folds. The strict protocol computes a Bemis–Murcko framework per standardized molecule and keeps each framework group in one outer partition; acyclic molecules are grouped by canonical SMILES. This follows the chemical-learning rationale of scaffold splitting [27]. Group labels are computed before fitting, and validation data are used only for frozen candidate choices.

### 3.3. Data and candidate spaces

The RAHGL-MDR data contain 635 miRNAs, 216 drugs, and 5,379 unique positive pairs; 197 drugs with at least one positive association enter the drug-cold or scaffold-cold outer tests. The aligned Mi artifact contains 1,805 ncRNAs, 625 drugs, and 9,395 positive pairs, with 606 active drugs entering the principal scaffold-disjoint evaluation. ncRNADrug, NoncoRNA, a temporal subset from SM2miR, and a Mi subset supported by distinct PubMed identifiers are used for boundary analyses. Aligned resource counts and provenance-field availability are reported in the supplementary dataset/protocol statistics.

All primary evaluations enumerate every ncRNA candidate for each test drug. Overlap between Mi and ncRNADrug is computed using frozen normalization rules for RNA names, drug names, and positive pairs. The de-overlap confirmation removes entities that match Mi; it does not selectively remove pairs after observing model scores.

RNA names are checked against the roles documented by miRBase and Rfam [30,35], while compound normalization follows the PubChem distinction between depositor records and standardized structures [31]. Evidence provenance is retained because RNAInter, lncRNAdb, and DrugBank differ in evidence type and curation scope [32–34]. Normalization reduces superficial mismatches; it does not harmonize assays or turn missing pairs into negatives.

### 3.4. Candidate and strong baseline

The RNA prior is estimated only from RNA positive counts among inner-training drugs and uses Laplace smoothing. The candidate learns a pairwise residual over this prior from drug and RNA features. For the RAHGL-MDR main analysis, each training drug contributes equally to total pairwise loss, preventing drugs with more observed edges from dominating the objective. A residual scale is selected from a frozen grid using only the inner validation set; a scale of zero exactly recovers the RNA prior.

We do not claim that this objective is a novel ranking loss. GCFMCL already uses Bayesian personalized ranking for this task. Here the candidate tests whether entity-balanced training improves a specific drug-cold distribution rather than establishing universal algorithmic novelty.

The residual is trained from observed-versus-unobserved candidate orderings. Following the implicit-feedback distinction in BPR [26], unobserved pairs remain unlabeled rather than experimentally verified negatives.

### 3.5. Comparators and implementation boundaries

The strict Mi endpoint includes a dynamically resampled adaptation of ncRD-LG LocalGL, an sChemNET ablation without miRNA sequence information or external unlabeled-drug augmentation, and an independent three-seed strict adaptation of PLMF-MDA. The sChemNET and PLMF-MDA results are not reproductions of the original reported numbers. RAHGL-MDR does not release its training implementation and per-candidate predictions; we therefore reuse its public data and fixed folds for diagnostic baselines but do not make a paired head-to-head claim against the authors’ trained model.

### 3.6. Statistical analysis and freeze rules

Average precision is computed per held-out drug over its complete candidate list and then macro-averaged. PR-based summaries are appropriate because positives are sparse and false positives directly reduce precision [28,29]. AUROC is not the primary endpoint, and AP from balanced or restricted negative sets is not treated as comparable to full-candidate AP.

For ordinary RAHGL-MDR drug-cold evaluation, paired bootstrap resampling operates over drug-level differences. For strict scaffold-cold evaluation, bootstrap resampling is clustered by scaffold group. Both main RAHGL-MDR protocols report 95% intervals, the number of non-decreasing folds, and three training seeds. The frozen strict-scaffold confirmation gate requires an AP gain of at least 0.01 over the RNA prior, a confidence-interval lower bound above zero, non-decrease in at least four of five folds, positive gains for all three seeds, and gains of at least 0.01 for at least two seeds. An earlier ordinary drug-cold gate additionally required exceeding the popularity MAP reported in RAHGL-MDR.

The intervals are conditional on the fixed outer partition and the executed training seeds. Seed-specific AP is first averaged for the same fold and drug; drugs or scaffold groups are then resampled. The intervals do not integrate uncertainty from drawing new training seeds or new outer partitions. Auxiliary analyses on Mi, external databases, and source-derived labels use their own frozen configurations and decision gates.

All new exploration, training, data download, and hyperparameter tuning stopped on 20 October 2026. Post-freeze work is limited to rebuilding existing tables and figures, verifying hashes and tests, checking citations, and preparing submission material. Bootstrap intervals do not remove historical method-selection bias; Mi results are therefore labelled developmental evidence.

## 4. Results

### 4.1. Ordinary drug-cold gain did not persist under the strict scaffold evaluation

Across three training seeds on the fixed RAHGL-MDR drug-cold folds, the entity-balanced prior-residual candidate achieved an AP of 0.184244 versus 0.170664 for the RNA prior. The difference was 0.013580, with a 95% interval of 0.005139–0.024170 and non-decrease in all five folds. The candidate passed the frozen ordinary drug-cold gate.

With the same data source, candidate space, model family, and training seeds but a newly constructed five-fold scaffold-disjoint protocol, candidate AP was 0.175435 and prior AP was 0.175139. The gain fell to 0.000296, with a scaffold-cluster 95% interval of −0.007782–0.008476 and non-decrease in only two of five folds. Seed-specific gains were 0.005339, 0.008217, and −0.012667. Relative to the same-budget ordinary pairwise variant, the entity-balanced candidate gained only 0.000857 and the interval crossed zero.

The two protocols also change the composition of training, validation, and test drugs. These observations do not identify scaffold separation as the sole causal mechanism. They support the narrower conclusion that the positive result under the fixed ordinary drug-cold protocol was not robustly confirmed in the present strict scaffold-disjoint evaluation.

### 4.2. Beating public neural adaptations did not imply a material gain over the strong prior

On the main five-fold Mi scaffold-disjoint evaluation, candidate AP was 0.161748 and RNA-prior AP was 0.157509. The gain was 0.004239 (95% interval, 0.002812–0.005899), with non-decrease in all five folds, but it did not reach the 0.01 materiality gate. A second scaffold split produced a gain of 0.002881 (95% interval, 0.001047–0.004782) and non-decrease in four of five folds, also failing the gate.

On the same candidate space and scaffold endpoint, AP values for dynamic LocalGL, the sequence-free sChemNET ablation, and the independent strict PLMF-MDA adaptation were 0.153275, 0.154500, and 0.135050. The candidate was higher by 0.008473, 0.007248, and 0.026698, respectively. Each public-method summary used its matched prior, approximately 0.157507; this differs from the main-table prior of 0.157509 by about 1.8 × 10−6 and does not change the conclusion. The candidate’s practically relevant increment over the strong prior remained below 0.01. Thus, outperforming complex neural adaptations and adding material drug-specific information over a frequency prior are distinct claims.

### 4.3. Cross-database overlap changed the external-validation conclusion

The aligned Mi and ncRNADrug snapshots share RNAs, drugs, and positive pairs. Under the original ncRNADrug drug-cold evaluation, the candidate gained 0.007581 over the prior (95% interval, 0.001838–0.013747) and was non-decreasing in all five folds. After removing entities matched to Mi, candidate AP was 0.063689 and prior AP was 0.076418, producing a gain of −0.012729 with an interval crossing zero. The confirmation gate failed. On NoncoRNA, the gain was 0.003579, its interval also crossed zero, and only two of five folds were non-decreasing.

De-overlap does not prove that the original positive result was caused entirely by leakage because it also changes sample composition and support. It does show that a second database with unaudited entity and pair overlap cannot automatically be treated as independent confirmation.

### 4.4. Temporal drugs and source-derived labels exposed additional boundaries

On a temporal mini-holdout of 18 SM2miR compounds whose CIDs did not occur in Mi, the candidate underperformed the prior by 0.019876. The small subset rules out positive confirmation for this test but cannot estimate a universal external effect.

For Mi pairs supported by at least two distinct PubMed identifiers, an ECFP residual trained directly on the replicated-literature label gained 0.010933 over the frequency prior estimated for that label, but underperformed the RNA prior estimated from all reported pairs by 0.035344. The interaction-hurdle model selected zero weight in all five folds and therefore exactly recovered its first stage; the conditional-prior hurdle selected non-zero weight only in fold 2. These results do not show additional predictive value for a repeated-literature-support label. Distinct PubMed identifiers are not equivalent to independent experimental replication and do not identify a causal reporting mechanism.

## 5. Discussion

### 5.1. Conditional contribution

The strongest supported claim is deliberately narrow. Under the fixed RAHGL-MDR ordinary drug-cold partition, the candidate reliably improves full-candidate ranking. The present strict scaffold-disjoint evaluation does not confirm a comparably robust advantage. The ordinary drug-cold result is evidence for the evaluated entity-cold protocol. It is insufficient for a claim about unseen chemical cores.

### 5.2. Why the strong prior must be retained

The RNA-frequency prior reflects reporting structure rather than a biological mechanism. Precisely because association databases are highly imbalanced, it is a necessary control for whether a model adds drug-specific information. On Mi, the candidate significantly exceeded several neural adaptations yet improved AP over the prior by less than 0.005. Comparisons only among complex methods can therefore obscure the practically central baseline.

### 5.3. Mechanisms not identified by the results

The difference between ordinary drug-cold and scaffold-disjoint results cannot be attributed simply to same-scaffold leakage. Repartitioning by scaffold changes structural support, training composition, and the outer test distribution simultaneously. The study was not designed to identify separate causal effects for those factors and does not select models after inspecting post hoc strata.

### 5.4. Reporting recommendations

Studies that target new-drug ncRNA–drug prediction should report full-candidate drug-macro AP; a frequency prior estimated from training data only; both ordinary drug-cold and scaffold-disjoint results; train–test overlap in entities, scaffolds, and positive pairs; multiple split and training seeds; uncertainty clustered by drug or scaffold; a clear separation between original-model reproduction and independent adaptation; and the fact that unknown pairs are unlabeled.

### 5.5. Limitations

First, multiple candidates were developed on Mi, and the reported intervals do not remove historical method-selection bias. Second, RAHGL-MDR does not release its training code and per-candidate predictions, preventing a paired same-implementation reproduction of the authors’ model. Third, the ordinary drug-cold and scaffold-disjoint protocols use different outer assignments and therefore represent performance under different conditions rather than a single-drug counterfactual. Fourth, ncRNADrug triples lack pair-level PubMed identifiers, limiting source-independence checks. Fifth, the temporal SM2miR subset is small. Sixth, all labels are drawn from reported associations; no prospective or wet-laboratory validation was conducted. Seventh, several upstream repositories lack an explicit license. The current evidence package includes only local summaries, configurations, tables, figures, and rebuilding logic and is not a complete training-data release.

## 6. Conclusion

On the fixed RAHGL-MDR ordinary drug-cold folds, an entity-balanced prior-residual candidate produced a stable gain above the frozen materiality threshold for full-candidate ncRNA ranking. Under the present strict scaffold-disjoint split, the gain was near zero, its interval crossed zero, and its sign was unstable across seeds. Together with strong-prior comparisons on Mi, cross-database de-overlap, and source-derived-label audits, the evidence supports one conditional claim: **a gain exists under the fixed ordinary drug-cold protocol, but that performance claim cannot be directly extended to unseen chemical scaffolds.** This boundary is more faithful to the current evidence than a universal algorithmic claim and provides concrete requirements for future evaluation.

## Data and code availability

The public evidence package contains frozen summaries/configurations, the main table and figures, rebuilding scripts, tests, a third-party boundary, and a SHA-256 manifest. Third-party raw data, repository code, model weights, and paper PDFs are not redistributed. Repository: https://github.com/ljhOfGithub/ncrna-drug-generalization-audit; versioned release: https://github.com/ljhOfGithub/ncrna-drug-generalization-audit/releases/tag/v0.1.3. A permanent archive DOI has not yet been assigned.

## Ethics statement

This computational study used public or lawfully accessed data and involved no new participant recruitment, intervention, animal experiment, or identifiable individual-level information. Ethical approval and informed consent were therefore not applicable.

## CRediT authorship contribution statement

Jihao Li: Conceptualization, Methodology, Software, Validation, Formal analysis, Investigation, Data curation, Writing–original draft, Writing–review and editing, Visualization, and Project administration.

## Declaration of competing interest

The author declares no competing interests.

## Funding

This research received no specific grant from any funding agency in the public, commercial, or not-for-profit sectors.

## Declaration of generative AI and AI-assisted technologies

During manuscript preparation, the author used OpenAI Codex to assist literature discovery, code drafting and inspection, execution support, statistical-result checking, manuscript drafting, language editing, citation checking, and consistency checks. The author reviewed and edited all outputs, verified citations and reported numerical results against source materials and saved machine-readable results, and takes full responsibility for the content of the publication. Generative AI was not listed as an author and was not used to create or alter primary research data.

## References

[1] Y. Xie, W. Wang, J. Xu, L. Li, S. Wu, H. Wei, ncRD-LG: A unified framework integrating molecular language models and subgraph learning for drug–ncRNA target prediction, Pattern Recognition 179, Part A (2026) 113556. https://doi.org/10.1016/j.patcog.2026.113556.

[2] M.K. Elbashir, Relation-aware heterogeneous graph learning for miRNA–drug response association prediction under cold-start generalization, International Journal of Molecular Sciences 27 (20) (2026) 9013. https://doi.org/10.3390/ijms27209013.

[3] Z. Ma, Y. Chen, H. Wang, X. Xi, G. Cao, L. Deng, M. Wu, Hypergraph multi-view learning for ncRNA–drug association prediction with cluster anchors and contrastive alignment, Expert Systems with Applications 334, Part D (2027) 134658. https://doi.org/10.1016/j.eswa.2026.134658.

[4] N. Sheng, Y. Liu, L. Gao, L. Wang, L. Huang, Y. Wang, Multi-view fusion based on graph convolutional network with attention mechanism for predicting miRNA related to drugs, PLOS Computational Biology 21 (11) (2025) e1013703. https://doi.org/10.1371/journal.pcbi.1013703.

[5] N. Sheng, Y. Liu, L. Gao, W. Hou, L. Huang, Y. Wang, A pre-trained language model-based cross-modal fusion framework for predicting miRNA-drug resistance and sensitivity associations, PLOS Computational Biology 22 (2) (2026) e1013968. https://doi.org/10.1371/journal.pcbi.1013968.

[6] D. Galeano, Imrat, J. Haltom, C. Andolino, A. Yousey, V. Zaksas, S. Das, S.B. Baylin, D.C. Wallace, F.J. Slack, F.J. Enguita, E.S. Wurtele, D. Teegarden, R. Meller, D. Cifuentes, A. Beheshti, sChemNET: a deep learning framework for predicting small molecules targeting microRNA function, Nature Communications 15 (2024) 9149. https://doi.org/10.1038/s41467-024-49813-w.

[7] J. Wei, L. Zhuo, Z. Zhou, X. Lian, X. Fu, X. Yao, GCFMCL: predicting miRNA-drug sensitivity using graph collaborative filtering and multi-view contrastive learning, Briefings in Bioinformatics 24 (4) (2023) bbad247. https://doi.org/10.1093/bib/bbad247.

[8] X. Cao, X. Zhou, F. Hou, Y. Huang, M. Yuan, M. Long, S. Chen, W. Lei, J. Zhu, J. Chen, T. Zhang, A.-Y. Guo, W. Jiang, ncRNADrug: a database for validated and predicted ncRNAs associated with drug resistance and targeted by drugs, Nucleic Acids Research 52 (D1) (2024) D1393–D1399. https://doi.org/10.1093/nar/gkad1042.

[9] L. Li, P. Wu, Z. Wang, X. Meng, C. Zha, Z. Li, T. Qi, Y. Zhang, B. Han, S. Li, C. Jiang, Z. Zhao, J. Cai, NoncoRNA: a database of experimentally supported non-coding RNAs and drug targets in cancer, Journal of Hematology & Oncology 13 (2020) 15. https://doi.org/10.1186/s13045-020-00849-7.

[10] X. Liu, S. Wang, F. Meng, J. Wang, Y. Zhang, E. Dai, X. Yu, X. Li, W. Jiang, SM2miR: a database of the experimentally validated small molecules' effects on microRNA expression, Bioinformatics 29 (3) (2013) 409–411. https://doi.org/10.1093/bioinformatics/bts698.

[11] Y. Wang et al., RNAincoder: a deep learning-based encoder for RNA and RNA-associated interaction, Nucleic Acids Research 51 (W1) (2023) W509–W519. https://doi.org/10.1093/nar/gkad404.

[12] C. Oliver et al., Augmented base pairing networks encode RNA-small molecule binding preferences, Nucleic Acids Research 48 (14) (2020) 7690–7699. https://doi.org/10.1093/nar/gkaa583.

[13] J.G. Carvajal-Patiño et al., RNAmigos2: accelerated structure-based RNA virtual screening with deep graph learning, Nature Communications 16 (2025) 2799. https://doi.org/10.1038/s41467-025-57852-0.

[14] S.R. Krishnan, A. Roy, M.M. Gromiha, Reliable method for predicting the binding affinity of RNA-small molecule interactions using machine learning, Briefings in Bioinformatics 25 (2) (2024) bbae002. https://doi.org/10.1093/bib/bbae002.

[15] H. Ma et al., RNA–ligand interaction scoring via data perturbation and augmentation modeling, Nature Computational Science 5 (8) (2025) 648–660. https://doi.org/10.1038/s43588-025-00820-x.

[16] J. Chen et al., Interpretable RNA Foundation Model from Unannotated Data for Highly Accurate RNA Structure and Function Predictions, arXiv:2204.00300 (2022). https://doi.org/10.48550/arXiv.2204.00300.

[17] N. Wang et al., Multi-purpose RNA language modelling with motif-aware pretraining and type-guided fine-tuning, Nature Machine Intelligence 6 (5) (2024) 548–557. https://doi.org/10.1038/s42256-024-00836-4.

[18] M.T. Tahmid et al., BiRNA-BERT allows efficient RNA language modeling with adaptive tokenization, Communications Biology 8 (2025) 1621. https://doi.org/10.1038/s42003-025-08982-0.

[19] S. Chithrananda, G. Grand, B. Ramsundar, ChemBERTa: Large-Scale Self-Supervised Pretraining for Molecular Property Prediction, arXiv:2010.09885 (2020). https://doi.org/10.48550/arXiv.2010.09885.

[20] Y. Kalakoti, S. Yadav, D. Sundar, TransDTI: Transformer-Based Language Models for Estimating DTIs and Building a Drug Recommendation Workflow, ACS Omega 7 (3) (2022) 2706–2717. https://doi.org/10.1021/acsomega.1c05203.

[21] T.M. Nguyen, T. Nguyen, T. Tran, Mitigating cold-start problems in drug-target affinity prediction with interaction knowledge transferring, Briefings in Bioinformatics 23 (4) (2022) bbac269. https://doi.org/10.1093/bib/bbac269.

[22] T. Nguyen et al., GraphDTA: predicting drug–target binding affinity with graph neural networks, Bioinformatics 37 (8) (2021) 1140–1147. https://doi.org/10.1093/bioinformatics/btaa921.

[23] P. Bai et al., Interpretable bilinear attention network with domain adaptation improves drug–target prediction, Nature Machine Intelligence 5 (2) (2023) 126–136. https://doi.org/10.1038/s42256-022-00605-1.

[24] T. Pahikkala et al., Toward more realistic drug–target interaction predictions, Briefings in Bioinformatics 16 (2) (2015) 325–337. https://doi.org/10.1093/bib/bbu010.

[25] M. Zhang, Y. Chen, Link Prediction Based on Graph Neural Networks, Advances in Neural Information Processing Systems 31 (2018) 5165–5175.

[26] S. Rendle, C. Freudenthaler, Z. Gantner, L. Schmidt-Thieme, BPR: Bayesian Personalized Ranking from Implicit Feedback, UAI (2009) 452–461.

[27] Z. Wu et al., MoleculeNet: a benchmark for molecular machine learning, Chemical Science 9 (2) (2018) 513–530. https://doi.org/10.1039/C7SC02664A.

[28] J. Davis, M. Goadrich, The Relationship Between Precision-Recall and ROC Curves, ICML (2006) 233–240. https://doi.org/10.1145/1143844.1143874.

[29] T. Saito, M. Rehmsmeier, The Precision-Recall Plot Is More Informative than the ROC Plot When Evaluating Binary Classifiers on Imbalanced Datasets, PLOS ONE 10 (3) (2015) e0118432. https://doi.org/10.1371/journal.pone.0118432.

[30] A. Kozomara, S. Griffiths-Jones, miRBase: annotating high confidence microRNAs using deep sequencing data, Nucleic Acids Research 42 (D1) (2014) D68–D73. https://doi.org/10.1093/nar/gkt1181.

[31] S. Kim et al., PubChem 2023 update, Nucleic Acids Research 51 (D1) (2023) D1373–D1380. https://doi.org/10.1093/nar/gkac956.

[32] J. Kang et al., RNAInter v4.0: RNA interactome repository with redefined confidence scoring system and improved accessibility, Nucleic Acids Research 50 (D1) (2022) D326–D332. https://doi.org/10.1093/nar/gkab997.

[33] X.C. Quek et al., lncRNAdb v2.0: expanding the reference database for functional long noncoding RNAs, Nucleic Acids Research 43 (D1) (2015) D168–D173. https://doi.org/10.1093/nar/gku988.

[34] D.S. Wishart et al., DrugBank 5.0: a major update to the DrugBank database for 2018, Nucleic Acids Research 46 (D1) (2018) D1074–D1082. https://doi.org/10.1093/nar/gkx1037.

[35] I. Kalvari et al., Rfam 14: expanded coverage of metagenomic, viral and microRNA families, Nucleic Acids Research 49 (D1) (2021) D192–D200. https://doi.org/10.1093/nar/gkaa1047.
