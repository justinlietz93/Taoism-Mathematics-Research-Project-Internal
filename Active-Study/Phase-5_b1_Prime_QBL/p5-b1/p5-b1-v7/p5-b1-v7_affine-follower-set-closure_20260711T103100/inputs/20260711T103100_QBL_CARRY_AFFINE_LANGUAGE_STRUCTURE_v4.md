# QBL Carry Affine Language Structure v4

**Step:** `p5-b1-v6`  
**Primary authority:** `QBL_PRIMITIVE_CUSTODY_AND_ORTHAD_LAW_v2.md`  
**Scope:** affine ceiling carry language, its exact interval coding, complexity, entropy, soficity, and mixing.  
**Excluded tracks:** global exact-Fibonacci threshold bridge; specific-orbit equidistribution; gauge/FQM interpretation of count parity or primality.

## 1. Disposition

### Proved abstractly

- The affine ceiling recurrence induces the three-symbol carry partition `7,8,9`.
- The one-step Lebesgue matrices `J` and `P` remain exact under `1/6<a<1/4`.
- `989` is forbidden; at the current constant `787` is also forbidden.
- The length-three language contains 15 words.
- For every `n>=1`, the affine carry language has

  \[
  p(n)=2^{n+1}-1.
  \]

- The affine coding entropy is

  \[
  h_{\mathrm{affine}}=\log 2.
  \]

- The affine carry language is **not sofic**. No finite labeled-graph presentation exists.
- The affine carry language is **topologically mixing**.
- Consequently, the language is not a finite-order Markov shift for any order.

### Certified finitely

- The imported trace has exactly one row for every `A=0..10000`, all carries lie in `{7,8,9}`, and there are exactly 9999 adjacent transitions.
- The derived transition counts match the included prior transition table exactly.
- Rational-affine cylinder endpoints `q*a+r`, compared over an outward-rounded enclosure of the current `a`, reproduce all cylinders through length 12.
- The direct cylinder counts agree with `2^(n+1)-1` through length 12.
- Orders `1..10` have explicit interval-certified finite memory counterexamples.
- Outward-rounded interval propagation certifies no affine-orbit boundary hit for `A=0..10000`.

### Observed

- The imported orbit is substantially closer to the Lebesgue one-step edge law `J` than to the Parry edge law `K` of the pairwise envelope.
- Its state and defect frequencies are close to the Lebesgue benchmarks on the tested range.

### Open

```text
SPECIFIC-ORBIT EQUIDISTRIBUTION: NOT PROVED
GLOBAL T_A=ceil(y_A) BRIDGE: NOT YET PROVED
GAUGE/FQM MAP FROM d_A=±1: NOT YET DERIVED
```

The interval coding itself is a complete presentation of the affine language. What this pass proves is that no **finite-state/sofic** presentation can be equivalent to it.

## 2. Affine ceiling bridge

Assume

\[
y_A=2y_{A-1}+\gamma,
\qquad
T_A=\lceil y_A\rceil.
\]

Define

\[
E_A=y_A-T_A,
\qquad
c_A=T_A-2T_{A-1}.
\]

For every `A>=1`,

\[
\begin{aligned}
T_A
&=\left\lceil 2y_{A-1}+\gamma\right\rceil\\
&=\left\lceil 2(T_{A-1}+E_{A-1})+\gamma\right\rceil\\
&=2T_{A-1}+\left\lceil2E_{A-1}+\gamma\right\rceil,
\end{aligned}
\]

because `2T_(A-1)` is an integer. Therefore

\[
\boxed{c_A=\left\lceil2E_{A-1}+\gamma\right\rceil}.
\]

Also,

\[
\begin{aligned}
E_A
&=y_A-T_A\\
&=2(T_{A-1}+E_{A-1})+\gamma-T_A\\
&=2E_{A-1}+\gamma-(T_A-2T_{A-1}),
\end{aligned}
\]

so

\[
\boxed{E_A=2E_{A-1}+\gamma-c_A}.
\]

These are exact identities of the affine ceiling model. Their transfer to the exact Fibonacci threshold for every `A` remains open.

## 3. Half-open partition and branch maps

Write

\[
\gamma=8+2a,
\qquad
\frac16<a<\frac14.
\]

Since `E=y-ceil(y)`,

\[
E\in(-1,0].
\]

The carry intervals are

\[
\begin{aligned}
I_7&=\left(-1,-\frac12-a\right],\\
I_8&=\left(-\frac12-a,-a\right],\\
I_9&=(-a,0].
\end{aligned}
\]

The downward boundary assignment follows from the ceiling convention:

\[
2\left(-\frac12-a\right)+\gamma=7,
\qquad
2(-a)+\gamma=8.
\]

The branch maps are

\[
F_c(x)=2x+\gamma-c,
\]

hence

\[
F_7(x)=2x+1+2a,
\quad
F_8(x)=2x+2a,
\quad
F_9(x)=2x-1+2a.
\]

## 4. One-step Lebesgue law

For states ordered `(7,8,9)`, define

\[
J_{ij}=\operatorname{Leb}\{x\in I_i:F_i(x)\in I_j\}.
\]

The exact joint mass matrix is

\[
\boxed{
J=
\begin{pmatrix}
0 & \dfrac{1-3a}{2} & \dfrac a2\\[2mm]
\dfrac{1-2a}{4} & \dfrac14 & \dfrac a2\\[2mm]
\dfrac{1-2a}{4} & \dfrac{3a}{2}-\dfrac14 & 0
\end{pmatrix}.}
\]

Under `1/6<a<1/4`, exactly seven entries are positive and

\[
J_{77}=J_{99}=0.
\]

The row and column marginals are both

\[
\pi_{\mathrm{Leb}}=
\left(\frac12-a,\frac12,a\right),
\]

and the total mass is one.

The conditional one-step table

\[
P_{ij}=\frac{J_{ij}}{\pi_{\mathrm{Leb},i}}
\]

is

\[
P=
\begin{pmatrix}
0 & \dfrac{1-3a}{1-2a} & \dfrac{a}{1-2a}\\[2mm]
\dfrac{1-2a}{2} & \dfrac12 & a\\[2mm]
\dfrac{1-2a}{4a} & \dfrac{6a-1}{4a} & 0
\end{pmatrix}.
\]

It is row stochastic and

\[
\pi_{\mathrm{Leb}}P=\pi_{\mathrm{Leb}}.
\]

`P` is a one-step conditional table. It is not a first-order Markov presentation of the full language.

## 5. Pairwise support is not the language

The pairwise support matrix is

\[
M=
\begin{pmatrix}
0&1&1\\
1&1&1\\
1&1&0
\end{pmatrix}.
\]

It records positive one-step edges only.

### 5.1 Forbidden `989`

For the prefix `9->8`, start with `x in I9` and require `F9(x) in I8`. The current-state cylinder after the first step is

\[
C_{98}=\left(-\frac12-a,-1+2a\right].
\]

Applying `F8`,

\[
F_8(C_{98})=(-1,-2+6a].
\]

Because `a<1/4`,

\[
-2+6a<-a,
\]

so this image misses `I9=(-a,0]`. Therefore

\[
\boxed{989\notin\mathcal L}.
\]

Both adjacent pairs `98` and `89` are allowed by `M`, so `M` is strictly an edge envelope.

### 5.2 Length-three count

At the current constant, `a>3/14`, which also removes `787`. Exactly 15 length-three words remain, while the edge envelope admits 17.

## 6. Circle conjugacy and the transformed partition

Set

\[
z=E+1\pmod1,
\qquad
y=z+2a\pmod1.
\]

Then

\[
z'=2z+2a\pmod1,
\qquad
y'=2y\pmod1.
\]

Thus the affine error map is conjugate to the doubling map

\[
D(y)=2y\pmod1
\]

on the circle `T=R/Z`.

Let

\[
p=2a.
\]

The transformed atoms are the three circular arcs

\[
\begin{aligned}
A_9&=(p/2,p],\\
A_7&=(p,(p+1)/2],\\
A_8&=((p+1)/2,p/2],
\end{aligned}
\]

where the last interval is read around the circle through `1=0`. Therefore

\[
\boxed{\partial\mathcal P=\{p\}\cup D^{-1}(p)}.
\]

The three boundary points are

\[
p/2,\quad p,\quad (p+1)/2.
\]

## 7. Irrationality and nonperiodicity of the cut

From the definitions,

\[
p=-\frac{13}{2}+
\frac{\log(4096/5)}{2\log\varphi}.
\]

If `p` were rational, then `log(4096/5)/log(phi)` would be a positive rational `m/n`, giving

\[
\left(\frac{4096}{5}\right)^n=\varphi^m.
\]

The left side is rational. For every positive integer `m`,

\[
\varphi^m=F_m\varphi+F_{m-1}
\]

is irrational. This is impossible. Hence

\[
\boxed{p\notin\mathbb Q}.
\]

A point under doubling is eventually periodic exactly when it is rational. Therefore the orbit

\[
p,Dp,D^2p,\ldots
\]

contains no repetitions.

## 8. Complete complexity proof

For length `n`, define the refinement

\[
\mathcal P^{(n)}=
\bigvee_{j=0}^{n-1}D^{-j}\mathcal P.
\]

### Lemma 8.1: exact refinement boundary

Since

\[
\partial\mathcal P=\{p\}\cup D^{-1}(p),
\]

we have

\[
\begin{aligned}
\partial\mathcal P^{(n)}
&=\bigcup_{j=0}^{n-1}D^{-j}(\partial\mathcal P)\\
&=\bigcup_{j=0}^{n-1}
\left(D^{-j}(p)\cup D^{-(j+1)}(p)\right)\\
&=\boxed{\bigcup_{k=0}^{n}D^{-k}(p)}.
\end{aligned}
\]

No point in this union is inactive. A point of least preimage level `k=0` is the boundary `p` itself. A point of least level `k>=1` maps after `k-1` iterates to one of the two points in `D^{-1}(p)`, which is a genuine boundary of the base partition.

### Lemma 8.2: all boundary points are distinct

Each set `D^(-k)(p)` contains exactly `2^k` points. If a point occurred at levels `m<n`, then applying `D^m` would give

\[
D^{n-m}(p)=p,
\]

which would make `p` periodic and rational. Therefore the levels are disjoint.

Hence

\[
\#\partial\mathcal P^{(n)}
=\sum_{k=0}^{n}2^k
=2^{n+1}-1.
\]

### Lemma 8.3: every complementary arc is one nonempty cylinder

On a connected component of

\[
\mathbb T\setminus\partial\mathcal P^{(n)},
\]

none of the first `n` iterates crosses a partition boundary. Every coordinate of the length-`n` itinerary is therefore locally constant, hence constant on the whole component. Each component is nonempty by definition, so it realizes one word.

Conversely, the interior of any length-`n` cylinder cannot cross a refinement boundary. It lies inside one complementary component. The half-open endpoint convention attaches boundary points to adjacent cylinders but creates no additional word.

### Lemma 8.4: adjacent arcs carry distinct words

Let two adjacent components be separated by a refinement boundary `b`, and let `k` be the least integer with

\[
D^k(b)=p.
\]

If `k=0`, the two sides already lie in different base atoms at time zero.

If `k>=1`, then

\[
D^{k-1}(b)\in D^{-1}(p),
\]

which is a base-partition boundary. The two sides therefore receive different symbols at itinerary coordinate `k-1`. Since `k<=n`, this coordinate occurs within the length-`n` word.

Thus every counted cut separates two different words.

### Theorem 8.5: word complexity

The complementary arcs and the length-`n` words are in bijection. Therefore, for every `n>=1`,

\[
\boxed{p(n)=2^{n+1}-1}.
\]

Consequently,

\[
\boxed{
 h_{\mathrm{affine}}
 =\lim_{n\to\infty}\frac1n\log p(n)
 =\log2.}
\]

This closes the proof gap identified in the v5 audit: the boundary count is now explicitly connected to nonempty, pairwise-distinct cylinders.

## 9. Pairwise-envelope entropy only

For the edge envelope,

\[
M^2=
\begin{pmatrix}
2&2&1\\
2&3&2\\
1&2&2
\end{pmatrix}>0.
\]

Its Perron root and a Perron vector are

\[
\rho=1+\sqrt2,
\qquad
r=(1,\sqrt2,1)^T.
\]

Thus the edge-envelope entropy is

\[
h_{\mathrm{edge}}=\log(1+\sqrt2).
\]

The normalized Parry joint edge measure of that envelope is

\[
K_{ij}=\frac{M_{ij}r_ir_j}{4(1+\sqrt2)}.
\]

Neither `h_edge` nor `K` is the entropy or maximal-entropy measure of the actual affine carry language.

## 10. Non-soficity

### 10.1 Cylinders form a separating basis

The refinement boundary at depth `m` contains `D^(-m)(p)`, whose `2^m` points are equally spaced. Therefore every complementary arc has length at most `2^(-m)`. The mesh tends to zero.

For an open arc `U`, define its continuation language

\[
\mathcal F(U)=\{v:\operatorname{int}C(v)\cap U\neq\varnothing\}.
\]

If two open arcs `U` and `V` differ, their symmetric difference contains a nonempty open interval. At sufficiently fine depth, a cylinder lies inside that interval. Its word belongs to exactly one of `F(U)` and `F(V)`. Hence

\[
\boxed{\mathcal F(U)=\mathcal F(V)\Longrightarrow U=V.}
\]

### 10.2 Boundary-adjacent follower arcs

For each `n`, let `C_n^-` and `C_n^+` be the two length-`n` cylinder interiors adjacent to the boundary point `p`.

Because `D^(-n)(p)` has mesh `2^(-n)` and `p` is not itself an `n`th preimage of `p`, both adjacent cylinders lie in a neighborhood on which `D^n` is injective. Set

\[
U_n^-=D^n(C_n^-),
\qquad
U_n^+=D^n(C_n^+).
\]

These are two open follower arcs lying on opposite sides of

\[
p_n=D^n(p),
\]

and

\[
\overline{U_n^-}\cap\overline{U_n^+}=\{p_n\}.
\]

The follower set of the word carried by `C_n^±` is exactly `F(U_n^±)`.

### 10.3 Finite follower sets would force periodicity

A finite labeled graph has only finitely many word follower sets: a word's followers are determined by the finite subset of graph vertices at which that word can terminate.

Assume the affine carry language were sofic. Then the ordered pairs

\[
\left(\mathcal F(U_n^-),\mathcal F(U_n^+)\right)
\]

could take only finitely many values. There would be `n<m` with the same pair.

The separating-basis lemma would imply

\[
U_n^-=U_m^-\quad\text{and}\quad U_n^+=U_m^+.
\]

Their unique common boundary would then satisfy

\[
D^n(p)=D^m(p).
\]

That makes `p` eventually periodic and therefore rational, contradicting Section 7.

Hence

\[
\boxed{\text{the affine carry language is non-sofic}.}
\]

Equivalently:

```text
FINITE-STATE/SOFIC STATUS: PROVED NON-SOFIC
FINITE-STATE/SOFIC PRESENTATION: DOES NOT EXIST
```

Since every finite-order Markov language is a shift of finite type and therefore sofic, no finite Markov order can present this language. The package also supplies explicit interval-certified counterexamples for orders `1..10`.

## 11. Topological mixing

Let `u` and `v` be arbitrary realizable words. Let `m=|u|` and let

\[
U=D^m(\operatorname{int}C(u)).
\]

`U` is a nonempty open arc because `D` is an open local covering map and every cylinder has nonempty interior.

The doubling map is topologically exact. If an open arc has length `ell>0`, then after any `r` with

\[
2^r\ell>1,
\]

its image under `D^r` is the entire circle. Once the image is the circle, every later image is also the circle.

Therefore there is `N(u)` such that for every `r>=N(u)`,

\[
D^r(U)=\mathbb T.
\]

In particular, `D^r(U)` intersects `int C(v)`. Choose a point realizing that intersection and pull it back through `D^m` to `C(u)`. Its itinerary has the form

\[
u\,w\,v
\]

with `|w|=r`.

Thus for every pair of words `u,v`, all sufficiently large bridge lengths occur:

\[
\boxed{\text{the affine carry language is topologically mixing}.}
\]

This proof belongs to the actual interval language. It does not transfer mixing from `M`.

## 12. Exact finite cylinder engine

Every cylinder endpoint is represented as

\[
q a+r,
\qquad q,r\in\mathbb Q.
\]

Endpoint comparisons are performed by rational arithmetic over an outward-rounded enclosure of the current value of `a`. A comparison is accepted only when the entire enclosure has one strict sign. This produces interval-certified cylinders through depth 12 and interval-certified finite Markov witnesses through order 10.

The direct counts are

\[
3,7,15,31,63,\ldots,2^{13}-1
\]

through word length 12, exactly matching the theorem.

## 13. Finite empirical edge comparison

Using the 9999 transitions for `A=2..10000`:

```text
empirical versus J:
    max error = 0.0068256825682568257
    L1        = 0.014047774522984873
    TV        = 0.007023887261492436

empirical versus edge-envelope K:
    max error = 0.049718901381709301
    L1        = 0.18401018949366276
    TV        = 0.092005094746831379
```

The finite orbit is closer to `J`. This is evidence only. It is not a proof that the specific orbit is Lebesgue-generic or equidistributed.

Defect aggregation

\[
d_A=c_A-c_{A-1}
\]

compresses the `3x3` edge table to five difference classes and therefore loses edge information.

## 14. Finite boundary certificate

The package propagates the imported affine orbit using `mpmath.iv` outward-rounded interval arithmetic at 3300 decimal digits.

It certifies no hit of `-1`, `-1/2-a`, `-a`, or `0` for `A=0..10000`. The minimum certified separation is approximately

\[
9.72886578265059\times10^{-5}
\]

at `A=1416` from the `7/8` boundary.

This is a finite certificate only. Global nonintegrality and global boundary avoidance remain unproved.

## 15. Global threshold route remains separate

A plausible future route is:

1. write the exact Fibonacci product threshold with Binet's formula;
2. bound the exponentially small conjugate-root correction;
3. lower-bound the distance of the affine main term from an integer using a linear-forms-in-logarithms theorem;
4. verify the finite initial range directly.

This is a proposed route, not a theorem in this package.

## 16. Orthad boundary

The current Orthad law states that ordered QBL history is retained state and operation counts are insufficient. It also keeps the following obligations open:

- all-depth primary pairing recurrence;
- explicit chart maps proving both lenses are restrictions;
- exact bidirectional transfer recurrences;
- full multi-axis FQM generation and classification.

Therefore no count property, including `d_A=±1`, oddness, or primality, licenses inference of:

- an Orthad chart matrix;
- a gauge value;
- holonomy;
- an FQM isometry class;
- a Weil projection.

```text
GAUGE/FQM MAP FROM d_A=±1: NOT YET DERIVED
```

## 17. Formalization status

The package contains Lean theorem surfaces for the `J` identities and for the complete `989` prefix theorem, including definitions of `I7`, `I8`, `I9`, `F7`, `F8`, `F9`, and the `98` prefix predicate.

```text
LEAN SOURCE PRESENT; COMPILATION NOT VERIFIED
```

Lean and a matching Mathlib environment were unavailable in the build container.

## 18. Final status

```text
AFFINE CEILING MAP: PROVED
HALF-OPEN PARTITION: PROVED
ONE-STEP J AND P: PROVED
FORBIDDEN 989: PROVED
LENGTH-THREE LANGUAGE COUNT 15: PROVED AT CURRENT a
AFFINE COMPLEXITY 2^(n+1)-1: PROVED
AFFINE ENTROPY log(2): PROVED
FINITE-STATE/SOFIC STATUS: PROVED NON-SOFIC
ACTUAL AFFINE LANGUAGE MIXING: PROVED
FINITE MARKOV ORDER: NONE
SPECIFIC-ORBIT EQUIDISTRIBUTION: NOT PROVED
GLOBAL T_A=ceil(y_A) BRIDGE: NOT YET PROVED
GAUGE/FQM MAP FROM d_A=±1: NOT YET DERIVED
```
