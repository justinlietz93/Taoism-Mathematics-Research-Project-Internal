# Phase 5 v5: Orthad Primitive-Origin Audit

## Claim

The overset Orthad point chart, dual cochain chart, cross-chart transfer, and quadratic self-twist are generated from the finite QBL orientation successor. They are not imported as modular objects.

## Source-fixed primitive core

The primitive operator core remains `U={Q,B,L}`. The orientation carrier in this pass is the retained finite cyclic orbit

```text
W_r = (BQ)^r,    r in Z/NZ
sigma_N(W_r)=W_(r+1 mod N)
```

No Fourier target is used to define this orbit.

## Derivation

1. The point chart `OmegaPlus` is the orbit basis `e_r` of the earned successor.
2. The dual chart `OmegaMinus` is the successor-stable cochain chart.
3. A cochain `chi_s` is legal iff `chi_s(sigma_N x)=lambda_s chi_s(x)`.
4. Finite closure `sigma_N^N=id` forces `lambda_s^N=1`.
5. Positive QBL orientation fixes `lambda_s=exp(-2pi i s/N)`.
6. Unitarity fixes normalization to `N^(-1/2)`.
7. Therefore `chi_s(e_r)=N^(-1/2) exp(-2pi i r s/N)`.
8. The cross-chart transfer is the evaluation table `K_N(r,s)=chi_s(e_r)`.
9. The reverse transfer gives pairing `B_+(r,s)=rs/N`.
10. For even N, the same-chart self-twist is the quadratic refinement `q(r)=r^2/(2N)` and `G_N(r)=exp(2pi i q(r))`.

## Choice points

The audit found choice points, not hidden imports:

- finite cyclic carrier closure is a canon dependency;
- basepoint is gauge;
- orientation sign selects forward vs reverse chart;
- normalization is forced by unitarity;
- even N is required for the quadratic self-twist.

## Verdict

The dual chart is not an external modular-form object. It is the cochain chart forced by the earned cyclic successor. The transfer matrix is the chart-change table between point orientation and successor eigen-cochains. The Gauss diagonal is the quadratic refinement of the reverse transfer pairing.

## Remaining Phase 5 burden

Run Phase 5 v6 regression against all failed v1 branches, then Phase 5 v7 Lean/SymPy/Jupyter closure attack.
