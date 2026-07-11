# Phase 5 v7u: Full Orthad Lens Compiler Binding

Status: `FULL_ORTHAD_LENS_COMPILER_BOUND_TO_T_TO_FQM_EXTRACTION_WITH_NONBRUTEFORCE_CLASSIFIER_KEYS`

This package binds the native Orthad lens compiler directly to the transition-assignment and finite-quadratic-module extraction path.

Pipeline:

```text
Q/B/L/O/R retained history
  -> full Orthad lens compiler
  -> transition records T
  -> T-derived FQM presentations
  -> p-primary / 2-primary policy tags
  -> nonbruteforce mixed-prime classifier keys
  -> gauge / cocycle / rewrite gates
```

Phase 5 is not closed. This pass removes the fixture gap between v7q and v7t and records the remaining final closures.

Key outputs:

- `outputs/phase5_v7u_verification_summary.json`
- `outputs/phase5_v7u_transition_records.csv`
- `outputs/phase5_v7u_fqm_presentations.csv`
- `outputs/phase5_v7u_nonbruteforce_classifier_keys.csv`
- `outputs/phase5_v7u_cocycle_compatibility_checks.csv`
- `outputs/phase5_v7u_trace_rewrite_confluence_checks.csv`
- `outputs/phase5_v7u_negative_controls.csv`

Run:

```bash
python scripts/phase5_v7u_full_orthad_lens_compiler_binding.py
```
