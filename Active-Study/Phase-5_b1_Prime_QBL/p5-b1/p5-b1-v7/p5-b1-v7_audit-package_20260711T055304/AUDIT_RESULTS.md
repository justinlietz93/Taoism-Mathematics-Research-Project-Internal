# p5-b1-v7 Audit Results

## Verdict

```text
ADOPT

STANDARD HALF-OPEN FOLLOWER BRIDGE: PROVED
FINITE-STATE/SOFIC STATUS: PROVED NON-SOFIC
FINITE MARKOV ORDER: NONE
ACTUAL AFFINE LANGUAGE MIXING: PROVED
p5-b1 BRANCH STATUS: CLOSED
```

## Integrity and reproducibility

The uploaded archive passed every mechanical check:

```text
Package SHA-256:
0181c907c0fbe0e3e502fb72ad06ac13c2f9ab91146f2589a5c670094c7fc94c

Document SHA-256:
46996ac568f205d6a7cbb200a2c4108e77cec2b3e3b8e13a8aa5ffb854cba8ed

Manifest entries:               62
Manifest path coverage:         PASS
Manifest hashes and byte counts: PASS
Notebook code cells:            16
Notebook cells passing:         16/16
Figures emitted:                16
Clean rebuild:                  PASS
Byte-identical archive rebuild: PASS
```

The byte-identical rebuild requires preserving the package root basename because the deterministic archive includes that root directory in every archive path. Rebuilding under the original basename reproduces the uploaded archive exactly.

## Load-bearing proof audit

### 1. Exact standard follower identity

For a word `w` of length `n`, the package defines the actual half-open cylinder `C(w)` and follower region

\[
H_w=D^n(C(w)).
\]

The identity

\[
C(wv)=C(w)\cap D^{-n}(C(v))
\]

is exact. Therefore

\[
v\in\operatorname{Fol}(w)
\iff
H_w\cap C(v)\ne\varnothing.
\]

This is a set-theoretic equivalence. It preserves included and excluded endpoints and no longer substitutes open interiors for the actual cylinders.

### 2. Separation by standard follower sets

For the proper half-open arcs used in the construction, equality of the intersection languages

\[
\Phi(H)=\{v:H\cap C(v)\ne\varnothing\}
\]

forces equality of interiors. If the interiors differ, the difference contains an open subarc. The refinement cylinders have mesh tending to zero because each refinement contains the full grid `D^{-n}(p)`. A sufficiently deep cylinder lies inside that subarc and separates the two languages.

This implication is exactly strong enough. The proof does not claim that finite follower data must recover isolated endpoint membership.

### 3. Boundary-adjacent follower regions

The two length-`n` cylinders adjacent to `p` lie inside one `D^{-n}(p)` fundamental gap. Their lengths are strictly below `2^{-n}`, so `D^n` is injective on their union. Their exact images are

\[
H_n^-=(\alpha_n,q_n],
\qquad
H_n^+=(q_n,\beta_n],
\qquad
q_n=D^n(p).
\]

The ordered pair has a unique oriented minus-to-plus handoff at `q_n`. When the image arcs are complementary, their closures may share a second point, but the orientation at that point is plus-to-minus. The ordered handoff still identifies `q_n` uniquely.

### 4. Non-soficity

Equality of two ordered standard follower-set pairs implies equality of their ordered interior pairs. The oriented handoff then gives

\[
D^n(p)=D^m(p).
\]

For `n\ne m`, this would make `p` eventually periodic under doubling and therefore rational. The package proves `p` irrational. Hence the ordered follower-set pairs are all distinct.

A finite labeled graph permits only finitely many word follower sets, hence only finitely many ordered pairs. The actual affine carry language is therefore non-sofic.

### 5. No finite Markov order

A finite-memory language is a shift of finite type. Every shift of finite type is sofic. Non-soficity therefore rules out every finite Markov order. The order `1..10` witnesses remain valid finite certificates but are not used as the global proof.

### 6. Mixing

For realizable words `u` and `v`, the open set

\[
U=D^{|u|}(\operatorname{int}C(u))
\]

is nonempty. Doubling is topologically exact, so `D^r(U)` is the whole circle for all sufficiently large `r`. It then meets `int C(v)`, producing a realization of `u w v` for every sufficiently large bridge length `|w|=r`.

This proves topological mixing for the actual affine language independently of the pairwise edge envelope and independently of the non-soficity proof.

## Previously accepted results retained

```text
AFFINE COMPLEXITY: p(n)=2^(n+1)-1
AFFINE ENTROPY: log(2)
PAIRWISE M/K SYSTEM: EDGE-SHIFT ENVELOPE ONLY
FINITE ORBIT BOUNDARY A=0..10000: INTERVAL-CERTIFIED
```

## Formalization boundary

The Lean files are theorem surfaces. Lean was unavailable, and the package correctly states:

```text
LEAN SOURCE PRESENT; COMPILATION NOT VERIFIED
```

This does not block the on-page mathematical proof, but it is not a machine-checked theorem certificate.

## Standing research holds

```text
SPECIFIC-ORBIT EQUIDISTRIBUTION: NOT PROVED
GLOBAL T_A=ceil(y_A) BRIDGE: NOT YET PROVED
GAUGE/FQM MAP FROM d_A=±1: NOT YET DERIVED
```

## Branch disposition

Branch 1 has reached the bottom of the affine carry-language question. The exact interval presentation is derived, its complexity and entropy are proved, its higher-order language is proved non-sofic, no finite Markov order exists, and mixing is proved.

```text
p5-b1 BRANCH STATUS: CLOSED
```
