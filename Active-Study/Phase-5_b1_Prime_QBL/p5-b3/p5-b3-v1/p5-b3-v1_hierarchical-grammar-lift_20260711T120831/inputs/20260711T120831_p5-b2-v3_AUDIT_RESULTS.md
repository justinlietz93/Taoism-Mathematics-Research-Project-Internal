# p5-b2-v3 Audit Results

## Verdict

```text
ADOPT

GLOBAL T_A=ceil(y_A) BRIDGE: PROVED
EXACT BINET / INTEGER-GAP ROUTE: PROVED
DETERMINISTIC RETURNED ARCHIVE: VERIFIED
LEAN SOURCE PRESENT; COMPILATION NOT VERIFIED
p5-b2 BRANCH STATUS: CLOSED
NEXT INTERACTION: p5-b3-v1
```

## Integrity checks

The exact uploaded archive was checked.

```text
Reported and actual ZIP SHA-256:
4c76d4aaa8c20eb36bb3d7cb8ad2a0d95705c1307ddea1bef02a69bbcc02a7f8

Reported and actual document SHA-256:
04eb66a2fe85b1b5cbdd3bfe8cd6cf426123124d51582b6f17bfb93f8b2603b9

Manifest entries:                  44
Manifest coverage:                 PASS
Manifest sizes and hashes:         PASS
Notebook code cells:               12
Notebook cells with PASS:          12/12
Extracted figures:                 12
Stable ZIP ordering:               PASS
Fixed ZIP timestamps:              PASS
Clean one-command rebuild:         PASS
Clean rebuild vs returned archive: BYTE-IDENTICAL
```

The builder regenerated the package tree, manifest, executed notebook, figures, deterministic ZIP, and external SHA-256 file. The resulting ZIP was byte-identical to the uploaded archive.

## Mathematical audit

### 1. Exact Binet identity

For

\[
P_n=F_{n+1}F_{n+2},
\qquad
L_n=\frac{\varphi^{2n+3}}5,
\]

the package derives

\[
P_n=L_n+\rho_n,
\qquad
\rho_n=\frac{(-1)^n-\varphi^{-(2n+3)}}5.
\]

The cross-term reduction is correct because

\[
\varphi-\varphi^{-1}=1.
\]

### 2. Uniform correction bound

For even `n`,

\[
0<\rho_n<\frac15.
\]

For odd `n>=1`,

\[
|\rho_n|\le\frac{1+\varphi^{-5}}5<\frac14.
\]

The exact positive margin is

\[
\frac14-\frac{1+\varphi^{-5}}5
=\frac{23}{20}-\frac{\sqrt5}{2}>0.
\]

Therefore

\[
|\rho_n|<\frac14
\]

for every `n>=0`.

### 3. Power-of-two obstruction

If

\[
F_{n+1}F_{n+2}=2^m,
\]

then the coprime consecutive Fibonacci factors are both powers of two. Their gcd is one, so one factor must be one. The only possible indexed products are

\[
P_0=1,
\qquad
P_1=2.
\]

Every QBL threshold satisfies

\[
X_A=2^{12(2^{A+1}-1)}\ge2^{12}.
\]

Hence

\[
P_n\ne X_A
\]

for every `A,n>=0`.

### 4. Integer-gap transfer

Since `P_n` and `X_A` are distinct integers,

\[
|P_n-X_A|\ge1.
\]

Together with `P_n=L_n+rho_n` and `|rho_n|<1/4`, this gives

\[
P_n>X_A\iff L_n>X_A
\]

and

\[
|L_n-X_A|>\frac34.
\]

This step is valid on both sides of the threshold.

### 5. Nonintegrality and ceiling reduction

The leading equality `L_n=X_A` is equivalent to `n=y_A`. If `y_A` were integral, the exact decomposition would make the nonzero integer `P_n-X_A` have absolute value below `1/4`, which is impossible. Thus `y_A` is never integral.

The logarithmic inequality then gives

\[
L_n>X_A\iff n>y_A\iff n\ge\lceil y_A\rceil.
\]

Therefore

\[
\boxed{T_A=\lceil y_A\rceil}
\]

for every `A>=0`.

No Baker–Matveev cutoff is needed.

## Proof-companion boundary

The Lean file now states the complete requested theorem surface, but seven theorem bodies remain `sorry` and Lean was unavailable. The package reports that boundary correctly.

The derivation script checks exact symbolic sub-identities, dependency names, document markers, and finite regressions. It does **not** formally verify the full document proof or compare Lean theorem statements semantically. Its `PROVED` output is therefore a package consistency status inherited from the accepted written proof, not an independent machine proof.

This is non-blocking because:

1. the written theorem is independently valid;
2. the package does not claim successful Lean compilation;
3. deterministic delivery and the required theorem surface are both present.

A minor formatting defect remains in `docs/20260711T113107_RESULTS.md`: `\rceil` was emitted as a carriage-return sequence. It does not affect the theorem document or package evidence.

## Research boundary

```text
SPECIFIC-ORBIT EQUIDISTRIBUTION: NOT PROVED
GAUGE/FQM MAP FROM d_A=±1: NOT YET DERIVED
QBL-TO-AFFINE INTERNAL FACTOR MAP: NOT YET DERIVED
HIGHER-ORDER L / GRAMMAR SELF-RECURRENCE: NOT YET DERIVED
```

The global count bridge materially strengthens the self-recurrence observation: the affine carry grammar is now tied to the exact QBL/Fibonacci threshold sequence for every domain. It does not yet prove that the affine grammar is an internal factor of the complete lifted state or that its emergence is literally an `L` operation at a higher descriptive layer.
