# Phase 5 v8m: The 229 Data-Gated Decomposition

Ledger authority applied before generation. v8m has one mathematical target: the 229 ground-truth rows.

## Result

- 229/229 rows emit explicit integer basis matrices.
- 229/229 rows pass the local Section-V certificate verifier.
- 26 rows do not admit the package's radical-direct-summand split search; each is emitted with a failure vector and exhausted target record.
- F1/F2/F3 patches are emitted.
- `global_pass` is `false` because declared gates are ANDed and the radical-direct-summand split gate remains open.

## Key files

- `outputs/phase5_v8m_groundtruth_229_decomposition_certificates.csv`
- `outputs/phase5_v8m_sectionV_verifier_results.csv`
- `outputs/phase5_v8m_radical_split_failure_rows.csv`
- `outputs/phase5_v8m_f1_archival_edge_diag_provenance_diff.csv`
- `outputs/phase5_v8m_f2_stable_class_keys_true_diag_rank4.csv`
- `outputs/phase5_v8m_f2_class_id_reconciliation.csv`
- `outputs/phase5_v8m_f3_global_pass_patch.csv`
