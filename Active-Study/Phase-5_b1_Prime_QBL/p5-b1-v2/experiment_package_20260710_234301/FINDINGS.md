# FINDINGS

## Status

```text
DYADIC_CARRY_EXPLANATION_FOUND
FINITE_EXACT_THRESHOLD_BRIDGE_CERTIFIED_A0_A10000
GLOBAL_ALL_A_THRESHOLD_BRIDGE_NOT_CLAIMED
```

## Main result

The observed bound

\[
d_A=B_A-2B_{A-1}\in\{-2,-1,0,1,2\}
\]

is explained by a three-symbol integer carry process, not by an accidental prime coincidence.

Define

\[
\lambda=\frac{6\log 2}{\log\varphi},\qquad
\gamma=\lambda+\frac32-\frac{\log 5}{2\log\varphi},
\]

and the affine Binet threshold coordinate

\[
y_A=\lambda 2^{A+1}-\gamma.
\]

On the certified scan, the exact Fibonacci threshold is

\[
T_A=\lceil y_A\rceil.
\]

Because `y_A = 2y_(A-1)+gamma`, define, for `A >= 1`,

\[
c_A=T_A-2T_{A-1}.
\]

The carry is always one of

\[
\boxed{c_A\in\{7,8,9\}}.
\]

For `A >= 2`, the B-count defect is exactly

\[
\boxed{d_A=c_A-c_{A-1}},
\]

which forces

\[
\boxed{d_A\in\{-2,-1,0,1,2\}}.
\]

The initial value `d_1=0` is a boundary value arising from `T_(-1)=0`; it is not part of the carry-transition orbit and is excluded from transition-frequency statistics.

## Why this is interesting

The B-count sequence is a symbolic coding of a translated dyadic doubling orbit. The carry word is ternary (`7/8/9`), while its adjacent difference is the five-symbol defect word.

The exact transition graph after the initial boundary is:

```text
7 -> 8 or 9
8 -> 7, 8, or 9
9 -> 7 or 8
```

Thus `7->7` and `9->9` cannot occur.

## Prime gate

Since

\[
B_A=2B_{A-1}+d_A,
\]

`B_A` is odd exactly when `d_A` is odd. Under the five-symbol alphabet, this is equivalent to

\[
\boxed{d_A=\pm1}.
\]

Every B-prime through `A=1000` lies on this nearest-neighbor carry gate. The prime domains are:

```text
4, 17, 56, 72, 147, 177, 200, 294, 367, 878
```

The only simultaneous Q/B prime through `A=1000` remains `A=17`.

## Finite certificate

The exact Fibonacci threshold and affine-ceiling counts agree for every `A=0..10000`. The narrowest certified log margins are:

```text
terminal:    0.000146406957399902925263816
preterminal: 0.000227804795451679577591226
```

Both remain strictly positive after subtracting the Binet correction bounds.

## Benchmark frequencies

The translated doubling map has a Lebesgue invariant-measure benchmark. For

\[
a=\frac{\gamma-8}2=0.235122302145392064,
\]

the benchmark defect frequencies are:

```text
-2: 0.132438848927304
-1: 0.2351223021453921
 0: 0.25
+1: 0.2648776978546079
+2: 0.117561151072696
```

The maximum empirical deviation over `A=2..10000` is `0.006825682568256826`. This agreement is evidence, not a proof that the specific logarithmic dyadic orbit is equidistributed.

## Negative control

Changing dimensional growth from doubling to tripling destroys the bound when the same near-doubling residual `B_A-2B_(A-1)` is measured. The five-symbol alphabet is therefore tied to dyadic dimensional expansion.

The bounded-alphabet phenomenon is not unique to Fibonacci refinement by itself. It belongs to a dyadic affine-ceiling universality class. Fibonacci refinement fixes the specific constants, partition boundaries, carry word, and prime events realized by QBL.

## Scope

Proved abstractly:

- the three-symbol carry theorem for an affine dyadic ceiling law;
- the adjacent-carry identity for `d_A` for `A>=2`;
- the five-symbol defect bound;
- the parity/prime-candidate gate;
- the carry transition graph.

Certified finitely:

- the exact Fibonacci threshold equals the affine ceiling through `A=10000`;
- prime results through `A=1000`.

Open:

- the all-`A` exact threshold/ceiling theorem;
- equidistribution or normality of the specific dyadic orbit;
- any relationship between prime events and full Orthad gauge/FQM invariants.
