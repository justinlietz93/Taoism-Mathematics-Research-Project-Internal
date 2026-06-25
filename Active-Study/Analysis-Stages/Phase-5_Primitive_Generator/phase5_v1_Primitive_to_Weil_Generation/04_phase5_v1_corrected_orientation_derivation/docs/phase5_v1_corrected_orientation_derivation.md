# Phase 5 v1 — Corrected Orientation Derivation

## Claim first

The exact Q/B/L primitives, read by the current Orthad after the canon repair, produce a collapse-consistent diagonal orientation read only; they do not generate the Weil Fourier or quadratic Gauss generators.

## Status

```text
STATUS: DIAGONAL_ONLY_BOUNDARY
OLD_VERDICT: DEMOTED_TO_BANNED_METHOD_CONTROL
HAND_ADMITTED_DENSE_BLOCK: FORBIDDEN
SEALED_BEFORE_COMPARISON: TRUE
COLLAPSE_CONSISTENCY: PASS_STRUCTURAL_WITH_SOURCE_DECIMAL_CORRECTION
```

## Canon repairs retained

1. Degenerate macro grammar suspended.
2. S/T symbol collision killed.
3. Shadow law split: scalar readout external, orientation-residue vector carriable.
4. Standing rule locked.
5. New correction: a dense orientation block cannot be admitted by permission.

## First-principles full-orientation derivation

Let the orientation carrier be `C_N = Z/NZ` with basis vectors `e_r`.
The full orientation vector is

```math
a = \sum_{r\in C_N} a_r e_r.
```

From the exact primitive definitions:

```math
Q(A,q,	heta,\kappa,c)=(A,q,	heta+\pi/2,\lfloor(	heta+\pi/2)/2\pifloor,c+\pi/2)
```

so the induced full-orientation action is

```math
Q_N e_r = i e_{r+1}.
```

`Q_N` is a monomial shift with phase. It does not sum over orientation indices.

```math
B(A,(u,v),	heta,\kappa,c)=(A,\operatorname{sort}(v,u+v),	heta,\kappa,C(	heta,1/[v(u+v)]))
```

so `B` changes the real germ width and leaves the orientation index untouched:

```math
B_N e_r = eta(q) e_r, \qquad eta(q)>0.
```

`B_N` is same-orientation reanchoring. It does not create cross-orientation terms.

```math
L(A,q,	heta,\kappa,c)=(N(A),q,	heta+\pi/2,\lfloor(	heta+\pi/2)/2\pifloor,c+\pi/2)
```

so `L` freezes the current axis and appends a new active axis. It carries `q` and advances phase, but it introduces no orientation-index bilinear pairing.

Therefore every Q/B/L word is built from monomial/diagonal/inherit-and-extend actions. The current Orthad read, without a hand-admitted dense block, has the form

```math
K_N(r,s)=\delta_{r,s}\lambda_r.
```

For the pure orientation-cycle read sealed in this package:

```math
K_N(r,s)=\delta_{r,s}i^r.
```

All off-diagonal entries are exactly zero.

## Sealed-envelope discipline

The files

```text
outputs/phase5_v1_sealed_native_orientation_read_chi12_level12.csv
outputs/phase5_v1_sealed_native_orientation_read_chi8_level8.csv
```

were written and SHA-256 hashed before target construction. Their hashes are in

```text
outputs/phase5_v1_sealed_native_read_hashes.json
```

## Collapse-consistency

The derived read collapses to the existing diagonal Orthad lens:

```math
\Omega_{L1}=\operatorname{diag}(i/4895,1).
```

For the second latch the source pair form is recovered:

```math
\Omega_{L2}=\operatorname{diag}(i/4895,-i/(196418\cdot317811),1).
```

The package records a source decimal correction: `196418*317811 = 62423800998`, not `62403619338`.

## Post-seal comparison

After sealing, the comparison targets are:

```math
Weil\_F_N(r,s)=N^{-1/2}e^{-2\pi i rs/N}
```

and

```math
Weil\_G_N(r,s)=\delta_{r,s}e^{\pi i r^2/N}.
```

Results:

| Case | Target | Max residual | Verdict |
|---|---:|---:|---|
| χ12 N=12 | Weil_F | 1.2886751345948129 | not generated |
| χ12 N=12 | Weil_G | 1.8477590650225735 | not generated |
| χ8 N=8 | Weil_F | 1.2747548783981961 | not generated |
| χ8 N=8 | Weil_G | 1.6629392246050905 | not generated |

## Verdict

```text
DIAGONAL_ONLY_BOUNDARY
```

The corrected Orthad read, derived without a free dense block, produces no off-diagonal orientation coupling. The missing object is a derived bilinear orientation-pairing rule. If that rule exists, it is not yet present in the exact Q/B/L primitive definitions or the current Orthad read law.
