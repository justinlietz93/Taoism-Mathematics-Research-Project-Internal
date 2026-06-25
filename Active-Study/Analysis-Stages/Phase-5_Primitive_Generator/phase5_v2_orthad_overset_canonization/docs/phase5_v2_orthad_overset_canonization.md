# Phase 5 v2: Orthad Overset Canonization

## Claim

The Orthad is canonically an overset dual-lens readout:

```text
same-chart self-read preserves the old diagonal retained trace;
cross-chart transfer generates the finite Fourier pairing;
same-chart quadratic self-twist generates the Gauss diagonal.
```

## Canonical definition

Let the finite orientation carrier at a readout boundary be

```text
A_N = Z/NZ
```

and let the QBL orientation histories be indexed by

```text
W_r = (BQ)^r
```

with native cyclic successor

```text
sigma_N(e_r) = e_{r+1 mod N}.
```

The Orthad readout now has two complementary charts:

```text
OmegaPlus  = point-orientation chart, basis e_r
OmegaMinus = dual eigen-cochain chart, basis chi_s
```

The dual chart is not a candidate bank. It is forced by the native successor relation:

```text
chi_s(sigma_N e_r) = lambda_s chi_s(e_r), lambda_s^N = 1.
```

Choosing the positive QBL successor orientation gives

```text
lambda_s = exp(-2 pi i s/N).
```

Thus the cross-chart transfer coefficient is

```text
K_N(r,s) = chi_s(e_r) = N^(-1/2) exp(-2 pi i r s/N).
```

The reverse transfer has phase

```text
exp(+2 pi i r s/N).
```

Its same-chart quadratic refinement is

```text
q(r) = r^2/(2N)
G_N(r) = exp(2 pi i q(r)) = exp(pi i r^2/N).
```

## Canonical correction to the old Orthad

The old diagonal lens is not removed. It is reclassified as the same-chart self-read/collapse.

```text
old lens = OrthadSameRead
new cross terms = OrthadCrossTransfer
new quadratic diagonal = OrthadQuadraticSelfTwist
```

The off-diagonal entries do not belong inside the one old diagonal lens. They belong to the transfer map between two complementary lenses.

## Regression gates

The package verifies N=8 and N=12:

- cross-transfer unitarity,
- square equals orientation reversal,
- fourth power identity,
- quadratic refinement polarizes to the reverse transfer phase,
- post-seal equality to Weil_F_N and Weil_G_N,
- old trace collapse consistency.

## Collapse consistency

The same-chart read preserves:

```text
L1 = i/4895
L2 = -i/(196418 * 317811)
196418 * 317811 = 62423800998
```

## Scope

This package canonizes the Orthad overset behavior for finite cyclic orientation carriers and verifies the two Phase 5 carrier levels used so far, N=8 and N=12. Phase 5 v3 is the N-general stability sweep.
