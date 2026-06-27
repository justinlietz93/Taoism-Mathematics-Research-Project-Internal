# Phase 5 v7c: Doubled-Carrier Reverification of Generated Orthad Operators

## Claim

All Phase 5 generated cyclic Orthad operators survive when the carrier is corrected from a folded single orientation carrier to the doubled orientation carrier.

```text
D_N = Z/(2N)Z
```

## Corrected law

```text
K_D(a,b) = D^(-1/2) exp(-2πi ab/D)
G_D(a)   = exp(πi a²/D)
```

where `D = 2N`.

## Result

```text
STATUS: ALL_PRIOR_GENERATED_CYCLIC_RESULTS_REVERIFIED_ON_DOUBLED_ORIENTATION_CARRIER
GLOBAL_PASS: true
```

## Sweeps

Base moduli swept: 69

Range: 1 through 240

## Gates

1. `K_D K_D* = I`
2. `K_D² = reversal`
3. `K_D⁴ = I`
4. `G_D(a+b)/(G_D(a)G_D(b)) = exp(2πiab/D)`
5. representative invariance of `G_D` under `a -> a + D`
6. post-seal comparison residuals zero

## Hard residuals

```text
max_property_residual: 1.152670228422045e-12
max_post_seal_residual: 0.0
```

## Character/shadow re-entry

The cases `χ12`, `χ8`, Legendre-5, and Legendre-13 were rerun on their doubled orientation carrier sizes: `D=12`, `8`, `10`, and `26`.

`χ12` and `χ8` remain exact scalar quotient closures. Legendre-5 and Legendre-13 remain full-vector carrier cases.

## Important restriction

This pass re-verifies the **single-axis cyclic doubled carrier** result. It does not close the multi-axis finite quadratic module frontier.

The next target is Phase 5 v7d: Multi-Axis Finite Quadratic Module Test.
