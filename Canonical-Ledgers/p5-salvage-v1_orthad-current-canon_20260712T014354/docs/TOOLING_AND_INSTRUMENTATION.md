# Tooling and Instrumentation Salvage

The `tooling/` directory contains selected original packages or scripts whose mathematical role can be kept external to the current Orthad ontology.

## Algebra

- `v7r_fqm_classifier`: finite quadratic-module isometry classifier.
- `v7s_2primary_policy`: 2-primary normalization and Jordan policy.
- `v8m_229_decomposition`: certified decomposition and non-summand calibration corpus.
- `v8m_external_audit`: independent certificate, purity, and provenance checks.

## Conditional compilers

- `v7t_t_to_fqm`: transition-record to FQM extraction.
- `v7u_lens_compiler`: legacy lens-to-transition-to-FQM compiler.
- `v8a_confluence`: rewrite, confluence, and cocycle test machinery.

These compilers are retained as test harnesses. Their legacy input semantics are not current canon.

## Custody and finite targets

- `v7y_b_ladder`: exact B-ladder arithmetic and inverse checks.
- `v7z_chi12`: finite FQM/character skeleton.
- `v8q_primitive_engine`: clean current-canon primitive baseline.

## Audit controls

The later audits introduced reusable controls:

- certificate-is-data;
- ambient radical testing;
- SNF span and kernel checks;
- purity witnesses for non-summand radicals;
- stable invariant class keys;
- source-file hash and excerpt binding;
- provenance diffs instead of retyping;
- semantic corruption tests that run the actual verifier.
