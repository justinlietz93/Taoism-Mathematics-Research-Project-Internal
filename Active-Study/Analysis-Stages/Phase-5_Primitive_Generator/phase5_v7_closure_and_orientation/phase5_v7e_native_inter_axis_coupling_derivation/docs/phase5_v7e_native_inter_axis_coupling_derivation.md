# Phase 5 v7e: Native Inter-Axis Coupling Derivation

## Status

```text
STATUS: NATIVE_SHARED_BOUNDARY_COUPLING_GENERATED_FOR_TESTED_PRODUCT_MODULES_FRONTIER_REFINED
GLOBAL_PASS: True
PHASE5_CLOSED: false
```

## Objective

v7d showed that product finite quadratic modules close when a cross-axis coupling `c_ij` is retained as module data. v7e tests whether `c_ij` can be extracted natively from QBL histories that share a retained boundary.

## Sealed extraction rule

Before product-module comparison, v7e extracts:

```text
c_native = sum sign * (q_i_before_latch + 1) * (q_j_before_latch + 1)
```

over shared `L`-boundary latch events. The value is reduced modulo `lcm(D_i,D_j)`.

This extractor uses only retained Q-depths and shared boundary incidence. It does not inspect a target coupling matrix.

## Product-module test

For carrier:

```text
A = Z/D_iZ × Z/D_jZ
```

v7e builds:

```text
B_c(x,y) = x_i y_i / D_i + x_j y_j / D_j + c_native (x_i y_j + x_j y_i) / lcm(D_i,D_j)
```

Then it tests:

```text
K_A K_A* = I
K_A² = orientation reversal
K_A⁴ = I
G_A(x+y)/(G_A(x)G_A(y)) = exp(2πi B_c(x,y))
```

## Positive cases

```text
positive_cases: 6
positive_cases_passed: 6
max_positive_residual: 3.17539875105184e-13
```

Shared-boundary cases generated nonzero native couplings and passed the product-module gates.

## Negative controls

```text
negative_controls: 5
negative_controls_passed: 5
```

Controls verified that independent axes, prefix-only sharing, invalid representative-invariance couplings, degenerate couplings, and hand-supplied couplings do not count as native generation evidence.

## Verdict

```text
Native inter-axis coupling is generated for the tested shared-boundary QBL histories.

The current frontier is no longer whether a product module can close with retained coupling.
The frontier is deriving the full coupling registry from arbitrary QBL branching histories.
```
