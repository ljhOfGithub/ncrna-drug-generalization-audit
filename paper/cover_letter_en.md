# Cover Letter — Pattern Recognition

> Submission source synchronized with the author's confirmation of originality, submission status, competing interests, and funding.

[Date]

Dear Editor,

We submit the Original Article entitled “Drug-Cold Gains Do Not Persist under Scaffold Separation in ncRNA–Drug Prediction” for consideration in *Pattern Recognition*.

This study examines two evaluation conditions that are often conflated in ncRNA–drug association prediction: ranking previously unseen drug identities under a fixed drug-cold split, and extrapolating to drugs whose Bemis–Murcko scaffolds are absent from training and validation. On the public RAHGL-MDR fixed drug-cold folds, an entity-balanced prior-residual ranker improved drug-macro average precision over a training-only RNA-frequency prior by 0.013580 across three training seeds (95% CI, 0.005139–0.024170; non-decreasing in 5/5 folds). Under a strict five-fold scaffold-disjoint protocol, the gain fell to 0.000296 (scaffold-cluster 95% CI, −0.007782–0.008476; non-decreasing in 2/5 folds).

The contribution is a conditional result and an evaluation boundary, not a claim of a universally superior algorithm or cross-protocol state of the art. The fixed drug-cold result supports expansion to unseen drug identities within the evaluated chemical space, whereas the scaffold-disjoint result does not confirm robust transfer to unseen cores. We further compare strict adaptations of LocalGL, a sequence-free sChemNET ablation, and PLMF-MDA on the Mi endpoint, and audit cross-database entity/pair overlap, a small temporal-drug holdout, and labels supported by distinct PubMed identifiers. These analyses show that full-candidate ranking, a strong frequency prior, scaffold separation, and source independence materially affect the claim that can be supported.

The work fits *Pattern Recognition* because it studies the generalization boundary of representation and ranking systems under distribution shift, uses a common full-candidate endpoint and clustered uncertainty estimates, and supplies an auditable evidence package. Unknown associations are treated as unlabeled candidates rather than experimentally confirmed negatives. Independent adaptations are not presented as reproductions of the original authors’ systems.

In response to the journal’s requested cover-letter information:

1. **Comparison with the state of the art.** We use protocol-matched adaptations and protocol-level comparisons rather than pooling incompatible reported scores. Five representative works are ncRD-LG (*Pattern Recognition*, 2026), RAHGL-MDR (*International Journal of Molecular Sciences*, 2026), HMVCC (*Expert Systems with Applications*, 2027), sChemNET (*Nature Communications*, 2024), and PLMF-MDA (*PLOS Computational Biology*, 2026). The manuscript states which components were rerun, independently adapted, or used only as protocol evidence.
2. **Public datasets.** The main analyses use the Mi resource distributed with ncRD-LG and the public data/folds associated with RAHGL-MDR. Boundary analyses use ncRNADrug, NoncoRNA, and a historical SM2miR snapshot. Supplemental diagnostics use metadata or resources from ChEMBL, miRTarBase, STRING, Reactome, CTD, PRISM, and LINCS/GEO subject to their individual access and licensing terms. Third-party raw files are not redistributed.
3. **Validation metrics.** The primary endpoint is average precision over the full ncRNA candidate set for each held-out drug, macro-averaged across drugs. We report paired bootstrap intervals clustered by drug or Bemis–Murcko scaffold, fold-level direction consistency, multiple training seeds, and a second scaffold split where available. Sampled-unlabeled pooled AUPR is diagnostic only and does not replace the primary endpoint.

I confirm that this manuscript is original, is not under consideration elsewhere, and has been approved for submission by the author. The author declares no competing interests. This research received no specific grant from any funding agency in the public, commercial, or not-for-profit sectors.

The review package contains an anonymized or identified manuscript as required by the submission system, editable figures/tables, highlights, supplementary material, and a versioned evidence archive. The public repository is https://github.com/ljhOfGithub/ncrna-drug-generalization-audit and the frozen release is https://github.com/ljhOfGithub/ncrna-drug-generalization-audit/releases/tag/v0.1.2. A permanent archive DOI has not yet been assigned.

Thank you for your consideration.

Sincerely,

Jihao Li\
Independent Researcher, Shenzhen, Guangdong, China\
Shenzhen, Guangdong, China\
jihao.li@polyu.edu.hk
