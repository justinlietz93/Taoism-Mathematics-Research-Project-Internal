# Phase 3 v1 — General Shadow Correspondence Sweep

## Result card

Status: `CONDITIONAL_CLASS_CLAIM_SUPPORTED_BY_SWEEP`

Global pass: `TRUE`

The χ₁₂ Shadow Residual instance remains closed. Phase 3 v1 tests whether the same mechanism holds across a broader unary finite-module class.

## Claim

For unary false-theta/mock-shadow channels carried by a finite quadratic module

```text
A_m = Z/(2m)Z
```

with an even orientation vector

```text
a(-r)=a(r),
```

the shadow map is the Phase Calculus projection-loss gate in the modular setting.

The retained positive-orientation channel gives the false/mock object:

```text
R_a(τ) = Σ_{n≥1} a(n) n q^(n²/(4m)).
```

The coefficient-stripped channel gives the weight-1/2 shadow candidate:

```text
G_a(τ) = Σ_{n≥1} a(n) q^(n²/(4m)).
```

The scalar bilateral n-weighted projection cancels:

```text
Σ_{n∈Z} a(n) n q^(n²/(4m)) = 0.
```

That zero is the projection-loss gate.

## Primitive carrier derivation

The retained residue carrier has dimension `2m`.

### T phase from Q square seating

```text
T_r = exp(π i r²/(2m)).
```

This follows because `τ -> τ + 1` multiplies the residue component with exponent `n²/(4m)` by

```text
exp(2πi n²/(4m)) = exp(πi r²/(2m)).
```

The value depends only on retained residue `r mod 2m`.

### S Gauss kernel from B/L dual seating

```text
S_{r,s} = (2m)^(-1/2) exp(-π i r s / m).
```

This is the finite Fourier/Gauss pairing on the retained residue carrier. It is not a scalar comparison. It is the re-chart matrix for the full residue state.

### Weight lift

The coefficient-stripped theta channel transforms with weight `1/2`.

The n-weighted derivative channel transforms with weight `3/2` and the same retained S/T carrier, with the derivative factor carried separately:

```text
D_r(-1/τ) =
  i(-iτ)^(3/2) Σ_s S_{r,s} D_s(τ).
```

## Cases tested

| Case | m | carrier | result |
|---|---:|---:|---|
| `chi12_eta_shadow_residual_closed_phase2` | 6 | Z/12Z | PASS |
| `chi8_level8_second_case` | 4 | Z/8Z | PASS |
| `legendre5_level10` | 5 | Z/10Z | PASS |
| `legendre13_level26` | 13 | Z/26Z | PASS |
| `delta_pair_m7` | 7 | Z/14Z | PASS |
| `three_pair_m9` | 9 | Z/18Z | PASS |

## Key finding

The sweep separates scalar quotient closure from retained vector closure.

`χ₁₂` has a scalar simplification. Several other cases require the full retained vector carrier. That is the expected general behavior and strengthens the Phase Calculus interpretation: the carried object is the retained residue/orientation vector, not a one-dimensional scalar character quotient.

## Pass gates

A case passes when:

```text
1. a(-r)=a(r)
2. bilateral n-weighted scalar projection cancels exactly
3. positive orientation readout is nonzero
4. S matrix is unitary
5. S² is orientation reversal r -> -r
6. theta S transform matches numerically
7. derivative S transform matches numerically
```

## Sweep result

All tested cases passed the retained-carrier gates.

## General versus χ₁₂-specific

See:

```text
outputs/phase3_v1_general_vs_specific.csv
```

The core distinction is:

```text
general:
  retained finite residue carrier
  even orientation vector
  scalar projection loss
  positive false-theta readout
  coefficient-stripped shadow channel
  S/T finite Gauss carrier

χ₁₂-specific:
  eta identity
  level-12 support gcd(n,6)=1
  one-dimensional scalar quotient simplification
```

## Conjecture produced by Phase 3 v1

For the unary finite-module class, the mock/false-theta shadow correspondence is the Phase Calculus projection-loss gate in the modular setting.

## Falsifier

A counterexample is any finite-module unary false-theta/mock-shadow pair with:

```text
1. even orientation vector a(-r)=a(r),
2. known finite quadratic module A_m,
3. known S/T multiplier,
4. known lower-weight shadow,
```

where either:

```text
T_r != exp(π i r²/(2m))
S_rs != (2m)^(-1/2) exp(-π i r s/m)
```

or the known lower-weight shadow is not the coefficient-stripped projection of the same retained carrier.

## Next target

Phase 3 v2: Modular-B Operator Family.
