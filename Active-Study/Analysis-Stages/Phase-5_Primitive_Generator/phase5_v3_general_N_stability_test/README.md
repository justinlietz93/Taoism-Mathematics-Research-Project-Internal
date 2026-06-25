# Phase 5 v3: General N Stability Test

## Status

`EVEN_CYCLIC_CARRIER_STABILITY_SUPPORTED`

The overset Orthad transfer/self-twist construction was swept across 20 even finite cyclic carriers.

## Main result

For even `N`, with carrier `A_N = Z/NZ`:

```text
K_N(r,s) = N^(-1/2) exp(-2πi r s/N)
G_N(r)   = exp(πi r²/N)
```

passed:

```text
K_N K_N* = I
K_N² = orientation reversal
K_N⁴ = I
G(r+s)/(G(r)G(s)) = exp(2πi r s/N)
```

## Boundary

Odd `N` is not admitted as a quadratic self-twist carrier for `q(r)=r²/(2N)` because the self-twist is not well-defined on `Z/NZ`. The correct canonical carrier is the even residue-orientation carrier `A_m = Z/(2m)Z`.

## Max residuals

```text
max_property_residual: 9.614661196166605e-14
max_post_seal_residual: 0.0
```
