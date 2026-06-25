# Phase 5 v1 — Reweighted-Q Budget Repair Test

## One-sentence claim attacked

Reweighting `Q` by the existing B/Q refinement budget should make the self-channel quadratic and its polarization should generate the finite Fourier pair-channel.

## Verdict

```text
REJECTED_AT_COLLAPSE_CONSISTENCY_AND_BOUNDARY_DIFFERENT_GROWTH
```

The repair is not a valid extension of the current Orthad because it fails the mandatory collapse-consistency check at the second latch.

## Definitions used

The primitive stack remains unchanged.

```text
Q: theta -> theta + pi/2
B: (u,v) -> sort(v,u+v), germ width -> 1/(v(u+v))
L: host lift, q carried, theta -> theta + pi/2, rank grows by one
```

The accessible B/Q capacity note supplies the explicit candidate budget:

```text
floor_capacity(n) = 2^(2n) = 4^n
```

No new budget was introduced.

## Derived reweighted-Q action

Let the orientation vector have basis `e_r`.

```text
Q_budget e_r = exp(i*pi*b_r/2) e_{r+1}
b_r = 4^r
```

The self-channel is the running accumulation:

```text
Self_N(r) = exp(i*pi/2 * f(r))
f(r) = sum_{j=0}^{r-1} 4^j = (4^r - 1)/3
```

Modulo four:

```text
f(0) = 0
f(r) = 1 for every r >= 1
```

So the generated self-channel is:

```text
Self_N(0) = 1
Self_N(r) = i for r >= 1
```

This is not quadratic.

## Polarized pair-channel

The pair-channel is not inserted. It is computed from the sealed self exponent:

```text
Pair_N(r,s) = exp(i*pi/2 * (f((r+s) mod N) - f(r) - f(s)))
```

This produces a derived dense-ish phase table, but it is not the finite Fourier kernel and carries no earned `1/sqrt(N)` normalization.

## Sealed discipline

The native self and pair channel CSV files were written and hashed before the Weil comparison files were constructed. See:

```text
sealed/SEALED_BEFORE_WEIL_TARGETS.json
```

## Collapse consistency

The existing trace requires:

```text
Ω_after_L1 = diag(i/4895, 1)
Ω_after_L2 = diag(i/4895, -i/62423800998, 1)
```

The reweighted-Q repair gives:

```text
L1: +i/4895
L2: +i/62423800998
```

The corrected product is:

```text
196418 * 317811 = 62423800998
```

Therefore the repair passes the first latch and fails the second.

## Post-seal comparison

The comparison is recorded, but the repair is already rejected by collapse consistency.

```text
N=12: Weil_G residual = 1.9318516525782612
N=12: Weil_F residual = 1.2886751345948129
N=8:  Weil_G residual = 1.6629392246051327
N=8:  Weil_F residual = 1.3535533905932737
```

## Final result

```text
Boundary, different growth.
```

The B/Q budget available in the current materials is not linear in the orientation index. Its cumulative phase law is not quadratic. Under primitive phase periodicity it collapses to a constant `i` after the first occupied orientation, and it fails the existing second-latch trace.
