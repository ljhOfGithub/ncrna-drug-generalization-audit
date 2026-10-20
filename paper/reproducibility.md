# Reproducibility status

## Frozen local state

- Working branch: `feat/generalization-audit`.
- Git base commit at audit time: `f1358d53299bb33ccb3b23bb5d7f9e61195f2caa`.
- Status: **not release-ready**. Most audit scripts, tests, results, and paper artifacts are untracked; `main.py`, `train_eval.py`, and `util_functions.py` also contain pre-existing tracked modifications. No commit, push, or merge has been performed in this work session.
- Python environment: shared `/Users/jackie/Documents/Git/.venv`; Python 3.11.15.
- Verified package versions: NumPy 2.4.6, Pandas 2.3.3, scikit-learn 1.8.0, PyTorch 2.12.0, RDKit 2026.9.1, SciPy 1.17.1, Matplotlib 3.11.2.
- Local evidence-package manifest: `release/manifest.json`; SHA-256 covers the frozen inputs, generated tables/figures, build sources, environment list, data card, third-party boundary, and maintenance plan.

## Fixed external identities

| Asset | Verified identity |
|---|---|
| RAHGL-MDR public repository | commit `95ce15ee958038c9a4ac9844f67f571cd8173feb` |
| RAHGL-MDR official paper PDF | SHA-256 `98a75e1cbad699e65f1b379c4c6e9710c49a9cac307acbaf318ff86c01e8c8f0` |
| sChemNET public repository (evidence only; not run or released) | commit `66c0c880c3477270a77dad412a05a8415a89d3a7` |
| sChemNET official paper PDF | SHA-256 `0e0ec0fbbcded84eaf9d519afc14350988251f4ac4befe44f3e22f9cf589455d` |
| SM2miR 2015 XLS | SHA-256 `2f8a993055552ba4e0ad5f080f8789145d9237c7357e0e94c1b6731dc5a0ee1e` |
| Mapped PMID/source table | SHA-256 `22f2657460577b584f748536eea0592a9ae6d63bcabfc402b7d34c61ed1c4710` |
| Mi–ncRNADrug overlapping-pair set | SHA-256 `9c0b4b69a338e74a748162442abf3212e748c33f521b352e5e98f1d9ca939e74` |
| CTD chemical–gene source snapshot | SHA-256 `84ed0fc7104fb886296157ea2da1690e9519ad8c8ba5450988936302c43fc82a` |

## Reproduction entry points

The following commands are verified local entry points. The portable artifact command rebuilds 13 main comparisons and the conclusion-reversal figure, runs portable artifact tests, and checks the presence of seven frozen dataset/protocol rows and three frozen cases. The latter tables require excluded third-party data for recomputation and are protected by the package manifest rather than silently rebuilt from unavailable inputs.

```bash
/Users/jackie/Documents/Git/.venv/bin/python -m pytest -q
/Users/jackie/Documents/Git/.venv/bin/python reproduce_paper_artifacts.py
/Users/jackie/Documents/Git/.venv/bin/python release_manifest.py
```

After legally obtaining the third-party inputs described in `release/THIRD_PARTY.md`, run
`reproduce_paper_artifacts.py --with-third-party-diagnostics` to additionally recompute the
dataset/protocol and case-study tables. Neither command retrains the paper models.

Primary frozen results referenced by the paper are listed row-by-row in `paper/main_results.csv`. The `sources` column is the machine-readable provenance pointer, and `paper_evidence_matrix.py` rejects any row whose reported delta cannot be reconstructed from the candidate and baseline means. The 18 required build inputs include the sChemNET no-sequence and PLMF-MDA strict-adaptation summaries; raw databases, model caches, checkpoints, third-party repository clones, and paper PDFs are excluded.

## Remaining release blockers

- Create a clean release commit without absorbing unrelated tracked modifications; this requires reviewing the existing dirty files first.
- Obtain permission or isolate the new implementation from the unlicensed upstream repository. The conservative release policy now excludes every third-party raw dataset, repository clone, model weight, cache, and paper PDF; this avoids unauthorized redistribution but does not grant a license to derivative code.
- Add a single environment lockfile derived from the working shared environment; `requirements-audit.txt` is not yet demonstrated to recreate all experiments from scratch.
- Re-run the main-table build and figure generation from a clean checkout before release.
- `runtime_hardware.md` / `.csv` record the current hardware and complete LocalGL per-fold wall-clock values. A clean rerun time for the three-seed RAHGL confirmation remains missing.
- Archive exact stdout/stderr or run manifests for confirmatory executions; summary files alone do not prove clean end-to-end reruns.

## Manifest-only clean-package verification

On 2026-10-20, the 92 files declared by `release/manifest.json` were copied into a new directory:

`/Users/jackie/Documents/research/ncrd-lg-generalization-audit-clean-repro-20261020-v9`

From that directory, the default artifact command rebuilt all 13 main comparisons and the conclusion-reversal figure, passed its 14 portable tests, and passed SHA-256 verification for all 92 declared files. The copied `submission-pattern-recognition/main.tex` also compiled successfully with the built-in LaTeX compiler.

This demonstrates that the declared evidence package is self-contained for its stated default scope. It is not a committed clean checkout, does not retrain models, and does not resolve licensing or third-party input availability.

## Integrity boundary

Passing unit tests, generating a table, or possessing hashes is not publication proof. A release becomes reproducible only after a clean checkout can recover permitted data, recreate the declared environment, execute the documented commands, and reproduce the main numbers within stated tolerances.
