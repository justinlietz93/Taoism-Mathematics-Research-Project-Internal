# Phase 5 v7: Lean/SymPy/Jupyter Closure Attack

## Claim

The canonized Orthad overset dual-lens construction survives independent closure attack:

```text
K_N(r,s) = N^(-1/2) exp(-2πi r s/N)
G_N(r)   = exp(πi r²/N)
```

for even finite cyclic residue-orientation carriers.

## Executed attacks

1. Numeric sweep over even `N` from `2` to `360`.
2. SymPy exact-expression attack for small `N`.
3. Negative controls: remove dual chart, remove self-twist, wrong normalization, wrong denominator, one-chart overlap.
4. Odd `N` boundary controls.
5. No-IO Jupyter notebook, one claim per cell.
6. Lake-ready Lean theorem surface.

## Result

```text
STATUS: NUMERIC_SYMPY_CLOSURE_ATTACK_PASSED_LEAN_LOCAL_PENDING
GLOBAL_PASS: true
```

## Hard residuals

```text
max_property_residual = 8.74312312065413e-13
max_post_seal_residual = 0.0
```

## Lean status

Lean/Lake were not available in this execution environment. The Lake workspace is included for local execution.
