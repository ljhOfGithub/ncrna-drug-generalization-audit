# Drug-Cold Gains Do Not Persist under Scaffold Separation in ncRNA–Drug Prediction

> Manuscript status: English submission draft derived from the frozen Chinese factual manuscript. Numerical results are frozen. Author identity, affiliation, licensing, ethics, CRediT, AI-use disclosure, ten directly relevant references, and the public versioned release are recorded. Funding and competing-interest confirmation remain submission blockers; an archive DOI is desirable but is not represented as already assigned.

**Author:** Jihao Li  
**Affiliation:** Independent Researcher, Shenzhen, Guangdong, China  
**Corresponding author:** Jihao Li, Shenzhen, Guangdong, China; jihao.li@polyu.edu.hk

## Abstract

Drug–non-coding RNA (ncRNA) association models are often evaluated using random pair splits or ordinary entity cold-start protocols. However, holding out drug identities does not establish extrapolation to unseen chemical scaffolds. We froze and compared two protocols: the public RAHGL-MDR ordinary drug-cold full-candidate ranking and a strict split with no Bemis–Murcko scaffold shared across training, validation, and test sets. On the fixed RAHGL-MDR folds, an entity-balanced prior-residual candidate achieved a drug-macro average precision (AP) of 0.184244 versus 0.170664 for a training-only RNA-frequency prior, a gain of 0.013580 (95% paired-bootstrap interval, 0.005139–0.024170; non-decreasing in 5/5 folds). Under the scaffold-disjoint protocol, candidate and prior AP were 0.175435 and 0.175139, respectively, yielding a gain of 0.000296 (scaffold-cluster 95% interval, −0.007782–0.008476; non-decreasing in 2/5 folds), with one of three training seeds producing a negative gain. On the Mi data, the candidate exceeded strict adaptations of LocalGL, a sequence-free sChemNET ablation, and PLMF-MDA, but improved over the RNA prior by only 0.004239, below the prespecified 0.01 materiality threshold. Cross-database de-overlap also changed the ncRNADrug gain from 0.007581 to −0.012729. The supported conclusion is conditional: the candidate improves new-drug ranking under the fixed ordinary drug-cold protocol, but the present scaffold-disjoint evaluation does not confirm robust gain for unseen chemical cores. New-drug studies should jointly report full-candidate ranking, strong frequency priors, scaffold separation, and source-overlap audits.

**Keywords:** ncRNA–drug association; drug cold start; scaffold-disjoint split; full-candidate ranking; frequency prior; evaluation protocol

## 1. Introduction

Drug–ncRNA association prediction seeks to recover or extend potentially relevant associations from previously reported relations. Recent work has used graph neural networks, local subgraphs, multi-view representations, and biological language models, while evaluation has expanded from random pair splits to drug-cold, RNA-cold, and double-cold protocols. These protocols answer different questions. A random pair split allows training and test sets to share entities. An ordinary drug-cold split withholds test-drug identities but does not require their chemical scaffolds to be absent from training. A scaffold-disjoint split imposes the stronger condition that the structural cores of test drugs are unseen. Without distinguishing these levels, evidence for “new-drug prediction” can be interpreted as the stronger and unsupported claim of extrapolation to new chemical scaffolds.

A second issue is the strength of simple priors. In full-candidate ranking, reporting frequencies differ markedly across RNAs. Ranking candidates only by RNA frequency in the training set can therefore provide a strong drug-independent baseline. A model may outperform more complex public neural systems while adding little over this prior. Likewise, database-level validation may reuse RNAs, drugs, and positive pairs. Calling a second database independent without auditing these overlaps can overstate the evidence.

This study does not propose a universally superior algorithm. Instead, it freezes a conditional question: can an entity-balanced prior-residual ranker reliably improve full-candidate ranking for unseen drug identities under an ordinary drug-cold protocol, and does that advantage persist under strict separation of chemical scaffolds? We additionally use Mi, ncRNADrug, NoncoRNA, a historical SM2miR snapshot, and labels supported by distinct PubMed identifiers to examine how strong priors, structural separation, entity overlap, and source independence affect the conclusion [8–10].

The contributions are as follows:

1. We report a frozen conditional result. On the fixed RAHGL-MDR drug-cold folds, the candidate improves AP over the RNA prior by 0.013580; under the present strict scaffold-disjoint protocol, the gain is only 0.000296 and its uncertainty interval crosses zero.
2. We define an evaluation ladder that distinguishes random-pair, entity-cold, scaffold-cold, temporal-new-drug, and independent-source targets, using full-candidate drug-macro AP as the common primary endpoint.
3. We evaluate strict adaptations of ncRD-LG LocalGL, a sequence-free sChemNET ablation, and PLMF-MDA on the same endpoint, while distinguishing original implementations, independent adaptations, and non-comparable reported results.
4. We quantify entity and positive-pair overlap between Mi and ncRNADrug and use de-overlap, temporal-new-drug, and distinct-PubMed analyses to expose dependence in apparent external evidence.
5. We provide a local evidence package that rebuilds the frozen main table and figures from summary/configuration files and records failed routes and prohibited claims.

## 2. Related work

ncRD-LG combines biological language models with local semantic subgraphs for drug–ncRNA association prediction. Its principal protocol is a random pair-level split, while leave-one-drug-out, leave-one-ncRNA-out, and scaffold-based splitting are identified as future evaluation directions [1]. RAHGL-MDR evaluates leakage-controlled edge, miRNA-cold, drug-cold, and double-cold settings and includes full-candidate ranking and degree/popularity baselines [2]. Cold-start evaluation and full-candidate ranking are therefore not new in this study.

HMVCC reports edge-level, cross-species, cross-database, and drug-cold settings for ncRNA–drug association prediction [3]. MGCNA learns multi-view graph-convolutional representations for miRNA–drug association prediction, whereas PLMF-MDA combines RNA-FM, ChemBERTa-2, intrinsic encoders, and cross-modal attention for miRNA–drug resistance and sensitivity associations [4,5]. sChemNET directly studies small molecules targeting microRNA function and evaluates chemically dissimilar test subsets using a molecular-fingerprint similarity threshold; this is not a Bemis–Murcko scaffold split [6]. The public GCFMCL implementation uses drug-as-user Bayesian personalized ranking during representation learning, so we do not claim to introduce pairwise ranking for this task [7].

As of the freeze date, our bounded full-text review found no single direct neighbor that jointly reports Bemis–Murcko scaffold separation, full-candidate drug-macro AP, a training-only RNA-frequency prior, cross-database entity de-overlap, temporal-new-drug evidence, and labels supported by distinct PubMed identifiers in one ncRNA–drug audit. This is a provisional gap under a bounded search, not a claim of priority or exhaustive absence.

## 3. Methods

### 3.1. Task and estimand

Given reported positive ncRNA–drug associations in a training set, the model scores the full set of candidate ncRNAs for each held-out drug. The primary metric is average precision for each drug, macro-averaged over test drugs. Database-unrecorded pairs are treated as unlabeled candidates, not as experimentally verified biological negatives.

We distinguish two main protocols:

- **Ordinary drug-cold:** drug identities are mutually exclusive across training, validation, and test sets, but scaffolds are not forced to be disjoint. We interpret this only as entity cold start on the fixed RAHGL-MDR folds, not as a universal deployment distribution.
- **Strict scaffold-disjoint:** Bemis–Murcko scaffolds define groups that do not overlap across training, validation, and test sets. Acyclic molecules are grouped by canonical SMILES. This protocol represents a stronger unseen-core requirement.

Ordinary drug-cold evaluation does not imply that every test drug shares a training scaffold, and it is not equivalent to strict scaffold extrapolation. We compare two frozen protocols and do not attribute their difference to a single leakage mechanism.

### 3.2. Data and candidate spaces

The RAHGL-MDR data contain 635 miRNAs, 216 drugs, and 5,379 unique positive pairs; 197 drugs with at least one positive association enter the drug-cold or scaffold-cold outer tests. The aligned Mi artifact contains 1,805 ncRNAs, 625 drugs, and 9,395 positive pairs, with 606 active drugs entering the principal scaffold-disjoint evaluation. ncRNADrug, NoncoRNA, a temporal subset from SM2miR, and a Mi subset supported by distinct PubMed identifiers are used for boundary analyses. Aligned resource counts and provenance-field availability are reported in the supplementary dataset/protocol statistics.

All primary evaluations enumerate every ncRNA candidate for each test drug. Overlap between Mi and ncRNADrug is computed using frozen normalization rules for RNA names, drug names, and positive pairs. The de-overlap confirmation removes entities that match Mi; it does not selectively remove pairs after observing model scores.

### 3.3. Candidate and strong baseline

The RNA prior is estimated only from RNA positive counts among inner-training drugs and uses Laplace smoothing. The candidate learns a pairwise residual over this prior from drug and RNA features. For the RAHGL-MDR main analysis, each training drug contributes equally to total pairwise loss, preventing drugs with more observed edges from dominating the objective. A residual scale is selected from a frozen grid using only the inner validation set; a scale of zero exactly recovers the RNA prior.

We do not claim that this objective is a novel ranking loss. GCFMCL already uses Bayesian personalized ranking for this task. Here the candidate tests whether entity-balanced training improves a specific drug-cold distribution rather than establishing universal algorithmic novelty.

### 3.4. Comparators and implementation boundaries

The strict Mi endpoint includes a dynamically resampled adaptation of ncRD-LG LocalGL, an sChemNET ablation without miRNA sequence information or external unlabeled-drug augmentation, and an independent three-seed strict adaptation of PLMF-MDA. The sChemNET and PLMF-MDA results are not reproductions of the original reported numbers. RAHGL-MDR does not release its training implementation and per-candidate predictions; we therefore reuse its public data and fixed folds for diagnostic baselines but do not make a paired head-to-head claim against the authors’ trained model.

### 3.5. Statistical analysis and freeze rules

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

The public evidence package contains frozen summaries/configurations, the main table and figures, rebuilding scripts, tests, a third-party boundary, and a SHA-256 manifest. Third-party raw data, repository code, model weights, and paper PDFs are not redistributed. Repository: https://github.com/ljhOfGithub/ncrna-drug-generalization-audit; versioned release: https://github.com/ljhOfGithub/ncrna-drug-generalization-audit/releases/tag/v0.1.0. A permanent archive DOI has not yet been assigned.

## Ethics statement

This computational study used public or lawfully accessed data and involved no new participant recruitment, intervention, animal experiment, or identifiable individual-level information. Ethical approval and informed consent were therefore not applicable.

## CRediT authorship contribution statement

Jihao Li: Conceptualization, Methodology, Software, Validation, Formal analysis, Investigation, Data curation, Writing–original draft, Writing–review and editing, Visualization, and Project administration.

## Declaration of competing interest

[STATEMENT CONFIRMED BY ALL AUTHORS REQUIRED.]

## Funding

[FUNDER, GRANT NUMBER, AND RECIPIENT OR CONFIRMED NO-SPECIFIC-FUNDING STATEMENT REQUIRED.]

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
