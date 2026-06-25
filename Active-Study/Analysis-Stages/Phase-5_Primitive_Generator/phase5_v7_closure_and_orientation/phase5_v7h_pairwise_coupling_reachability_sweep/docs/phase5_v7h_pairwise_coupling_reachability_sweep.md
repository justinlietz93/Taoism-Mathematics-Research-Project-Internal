# Phase 5 v7h: Pairwise Coupling Reachability Sweep

## Objective

After v7g, the finite quadratic module layer supports multi-axis product carriers through symmetric pairwise bilinear coupling tensors. v7h asks whether the native QBL history families can reach all admissible nondegenerate pairwise coupling classes, not just selected examples.

## Carrier

```text
A = Z/D_iZ × Z/D_jZ
L = lcm(D_i,D_j)
```

## Coupling term

```text
B_c(x,y) = x_i y_i/D_i + x_j y_j/D_j + c(x_i y_j+x_j y_i)/L
```

## Admissibility

Representative invariance requires:

```text
L | c D_i
L | c D_j
```

Equivalently, `c` is a multiple of `L/gcd(D_i,D_j)`.

## Native reachability families

```text
independent axes: 0
single shared latch: ±ab
double same-sign latch: ab+a'b'
double opposed latch: ab-a'b'
branch commutator: ab'-a'b
unit-latch program: repeated ±1 latch
```

## Summary

```json
{
  "phase": "5_v7h",
  "title": "Pairwise Coupling Reachability Sweep",
  "status": "PAIRWISE_COUPLING_REACHABILITY_SUPPORTED_FOR_BOUNDED_NATIVE_HISTORY_FAMILIES",
  "global_pass": true,
  "phase5_closed": false,
  "D_pair_count": 167,
  "registry_rows": 1166,
  "coverage_rows": 167,
  "full_valid_coverage_pairs": 167,
  "mean_valid_reachability_fraction": 1.0,
  "unreachable_valid_pair_count": 0,
  "max_shared_latch_count_bound": 1,
  "property_gate_rows": 884,
  "numeric_full_matrix_samples": 115,
  "negative_controls": 211,
  "negative_controls_passed": 211,
  "max_numeric_positive_residual": 4.063423753964662e-14,
  "sealed_before_comparison": true,
  "hand_supplied_cij_used_as_generation_evidence": false,
  "frontier": "bounded native families reach all admissible nondegenerate pairwise classes in swept pairs; full arbitrary QBL history classification remains open"
}
```

## Interpretation

Every admissible nondegenerate pairwise `c_ij` class in the swept pairs received a native bounded-history witness before product-module comparison. The full arbitrary-history theorem remains open.
