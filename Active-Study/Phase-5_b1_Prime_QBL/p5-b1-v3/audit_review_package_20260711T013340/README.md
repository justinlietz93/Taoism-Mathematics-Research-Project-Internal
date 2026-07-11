# Minimal Audit Review Package

This package reproduces the audit of:

- `QBL_CARRY_J_DERIVATION_AND_RESEARCH_BOUNDARY_v1.md`;
- `experiment_package_20260710_234301.zip`;
- `qbl_prime_pattern_watch_v1.zip`.

It also includes the current audit protocol and current primitive-custody/Orthad law used to judge package scope and authority.

## Verdict

```text
REVISE
ADOPT_J_MATHEMATICAL_CORE
WITHHOLD_CLOSED_DELIVERABLE_STATUS
```

## Run

From the package root:

```bash
python scripts/run_audit.py
python scripts/write_manifest.py .
```

The audit uses only the Python standard library.

## Outputs

- `AUDIT_RESULTS.md`: human-readable audit.
- `outputs/j_derivation_audit.json`: matrix, symbolic checks, empirical edge matrices, and comparison metrics.
- `outputs/package_integrity_audit.json`: zip integrity and reproducibility checks.
- `outputs/combined_audit.json`: combined machine-readable result.
- `MANIFEST.json`: SHA-256 and byte count for every package file except the manifest itself.

## Boundary

This package verifies the supplied derivation and package surfaces. It does not prove the open global Fibonacci-threshold theorem, specific-orbit equidistribution, or any gauge/FQM map from `d_A = +/-1`.
