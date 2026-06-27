# Phase 5 v7f: Coupling Registry Sweep

## Objective

Map which bounded QBL shared-boundary latch patterns generate which inter-axis coupling classes.

## Classifier

For axes `Z/D_iZ × Z/D_jZ`, define:

```text
L = lcm(D_i,D_j)
g = gcd(D_i,D_j)
admissible_step = L/g
```

A cross coefficient is representative-invariant only when:

```text
L | c D_i
L | c D_j
```

Equivalently:

```text
c is a multiple of L/g.
```

The bilinear form is:

```text
B_c(x,y)
=
x_i y_i / D_i
+
x_j y_j / D_j
+
c (x_i y_j + x_j y_i) / L
```

The transfer and twist are:

```text
K_A(x,y) = |A|^(-1/2) exp(-2πi B_c(x,y))
G_A(x) = exp(πi B_c(x,x))
```

## Native extraction

The native extractor used for shared latch histories is:

```text
c_native = Σ sign_b · (q_i(b)+1) · (q_j(b)+1) mod L
```

The extracted registry is sealed before any transfer/Weil comparison.

## Summary

```json
{
  "phase": "5_v7f",
  "title": "Coupling Registry Sweep",
  "status": "COUPLING_REGISTRY_SWEEP_SUPPORTED_FOR_BOUNDED_SHARED_LATCH_HISTORIES_FRONTIER_REFINED",
  "global_pass": true,
  "phase5_closed": false,
  "D_pair_count": 15,
  "registry_rows": 918,
  "unique_generated_c_total": 918,
  "property_gate_cases": 29,
  "property_gate_cases_passed": 29,
  "negative_controls": 23,
  "negative_controls_passed": 23,
  "max_positive_residual": 1.0226784664791497e-12,
  "full_valid_coverage_pairs": 15,
  "mean_valid_closure_coverage_fraction": 1.0,
  "mean_admissible_coverage_fraction": 1.0,
  "sealed_before_comparison": true,
  "hand_supplied_cij_used_as_generation_evidence": false,
  "frontier": "bounded shared-latch histories generate many admissible nonzero couplings; complete arbitrary-history registry remains open"
}
```

## Interpretation

The sweep supports the claim that shared-boundary QBL histories generate a nontrivial coupling registry. It also shows that not every generated residue is admissible: some candidates are rejected by representative invariance, and some admissible candidates are rejected by degeneracy.

The next frontier is not whether coupling can appear. It can. The frontier is the full arbitrary-history theorem: a complete map from QBL branch/latch/commutator patterns to all admissible nondegenerate product-module coupling classes.
