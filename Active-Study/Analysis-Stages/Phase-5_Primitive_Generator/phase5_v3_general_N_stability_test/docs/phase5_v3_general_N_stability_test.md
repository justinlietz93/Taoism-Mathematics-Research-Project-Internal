# Phase 5 v3: General N Stability Test

## Claim

For even finite cyclic residue-orientation carriers `A_m = Z/(2m)Z`, the canonical overset Orthad dual-lens readout is stable in `N`: cross-chart transfer gives the finite Fourier generator and reverse-transfer quadratic self-twist gives the Gauss diagonal.

## Definitions

Let `N = 2m` and `A_N = Z/NZ`.

Point chart:

```text
OmegaPlus basis: e_r, r in A_N
```

Dual cochain chart:

```text
OmegaMinus basis: chi_s(e_r) = N^(-1/2) exp(-2πi r s/N)
```

Cross-chart transfer:

```text
K_N(r,s) = N^(-1/2) exp(-2πi r s/N)
```

Reverse transfer pairing:

```text
B_+(r,s) = r s / N
```

Quadratic self-twist:

```text
q(r) = r²/(2N)
G_N(r) = exp(2πi q(r)) = exp(πi r²/N)
```

## Sealed discipline

The native `K_N`, `K_N^{-1}`, and `G_N` entries were written to `sealed/` and hashed before the post-seal comparison table was produced.

## Positive sweep

Positive even `N` values:

```text
2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 24, 26, 28, 30, 32, 36, 40, 48, 52, 60
```

All passed the finite-carrier property gates.

## Odd boundary

Odd cyclic carriers fail the quadratic self-twist well-definedness gate:

```text
G(r+N) != G(r)
```

for `G(r)=exp(πi r²/N)`. This refines the canon: the Fourier transfer exists for cyclic carriers, but the Phase 5 Gauss self-twist canon is naturally an even residue-orientation carrier law.

## Negative controls

The following controls failed as required:

```text
1. no dual chart,
2. unnormalized transfer,
3. wrong transfer sign,
4. wrong self-twist denominator.
```

## Verdict

The Phase 5 v2 overset Orthad canon is stable across the even finite cyclic carrier sweep. Phase 5 remains open for character/shadow re-entry and primitive-origin audit.
