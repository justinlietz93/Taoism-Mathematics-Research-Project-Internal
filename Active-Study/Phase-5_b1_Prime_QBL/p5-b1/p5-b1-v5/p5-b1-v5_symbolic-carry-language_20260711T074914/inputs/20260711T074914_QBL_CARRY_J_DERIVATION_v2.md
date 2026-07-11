# QBL Carry Geometry: Ceiling Bridge, Lebesgue Transition Law, and Research Boundary

**Status:** `J_TRACK_CLOSED_ON_AFFINE_CEILING_MODEL`  
**Finite correspondence:** the exact Fibonacci threshold agrees with the affine ceiling model only on the previously certified range `A=0..10000`  
**Specific-orbit equidistribution:** evidence only, not proved  
**Current Orthad authority:** `QBL_PRIMITIVE_CUSTODY_AND_ORTHAD_LAW_v2.md`  
**Older Phase 5 ledgers:** provenance only

The constants are

\[
\gamma=8.4702446042907841279349898711327462608\ldots,
\qquad
a=\frac{\gamma-8}{2}
=0.2351223021453920639674949355663731304\ldots
\]

and therefore

\[
\gamma=8+2a,
\qquad
\frac16<a<\frac14.
\]

## 1. Strategic ordering

The short `J` track should be closed before the global threshold theorem.

That ordering is stronger because the following steps depend only on the affine ceiling recurrence:

1. the exact error-coordinate map;
2. the half-open carry partition;
3. the joint Lebesgue transition matrix `J`;
4. the conditional matrix `P` and its stationary measure;
5. the topological adjacency matrix `M` and the Parry measure;
6. direct finite comparison against the existing `A=2..10000` transition trace.

The global theorem connecting the exact Fibonacci threshold to the affine ceiling model for every `A` is a separate analytic burden. It is not needed to derive `J` as a theorem of the affine model.

The corrected dependency order is

```text
affine ceiling recurrence
    -> exact error map and endpoint law
    -> interval coding
    -> J and P
    -> topological/Parry comparison
    -> finite empirical edge comparison

separate later track:
exact Fibonacci threshold
    -> Binet correction bound
    -> lower bound for the relevant logarithmic linear form
    -> finite remainder check
    -> possible global T_A = ceil(y_A) theorem
```

No part of the present pass infers Orthad, gauge, FQM, or Weil data from count primality.

---

## 2. Ceiling recurrence to the interval map

Assume the affine model

\[
y_A=2y_{A-1}+\gamma,
\qquad
T_A=\lceil y_A\rceil
\]

for `A>=1`, with `T_0=ceil(y_0)`.

Define

\[
E_A=y_A-T_A
\]

for `A>=0`, and

\[
c_A=T_A-2T_{A-1}
\]

for `A>=1`.

Because

\[
y_{A-1}=T_{A-1}+E_{A-1},
\]

we have

\[
\begin{aligned}
T_A
&=\left\lceil y_A\right\rceil\\
&=\left\lceil2y_{A-1}+\gamma\right\rceil\\
&=\left\lceil2(T_{A-1}+E_{A-1})+\gamma\right\rceil\\
&=\left\lceil2T_{A-1}+2E_{A-1}+\gamma\right\rceil.
\end{aligned}
\]

Since `2T_(A-1)` is an integer,

\[
\lceil n+x\rceil=n+\lceil x\rceil
\qquad(n\in\mathbb Z),
\]

so

\[
T_A
=2T_{A-1}+\left\lceil2E_{A-1}+\gamma\right\rceil.
\]

Subtracting `2T_(A-1)` gives

\[
\boxed{
c_A=\left\lceil2E_{A-1}+\gamma\right\rceil,
\qquad A\ge1.
}
\]

The error recurrence follows directly:

\[
\begin{aligned}
E_A
&=y_A-T_A\\
&=(2y_{A-1}+\gamma)-T_A\\
&=2(T_{A-1}+E_{A-1})+\gamma-T_A\\
&=2E_{A-1}+\gamma-(T_A-2T_{A-1})\\
&=2E_{A-1}+\gamma-c_A.
\end{aligned}
\]

Therefore

\[
\boxed{
E_A=2E_{A-1}+\gamma-c_A,
\qquad A\ge1.
}
\]

### Index and scope boundary

- `y_A`, `T_A`, and `E_A` are defined from `A=0` onward.
- `c_A` and the map from `E_(A-1)` to `E_A` begin at `A=1`.
- Carry-to-carry transitions `c_(A-1) -> c_A` begin at `A=2`.
- The empirical joint matrix in this document uses exactly `A=2..10000`, which gives `9999` transitions.
- The identification of this affine `T_A` with the exact Fibonacci threshold is certified only for `A=0..10000`.

---

## 3. Exact endpoint convention

For every real `y`,

\[
y-\lceil y\rceil\in(-1,0].
\]

Thus the exact state interval is

\[
\boxed{E_A\in(-1,0].}
\]

The endpoint `E_A=0` occurs exactly when `y_A` is an integer. Global nonintegrality of this specific orbit is not proved here.

Because `gamma=8+2a`, the carry thresholds are

\[
\frac{7-\gamma}{2}=-\frac12-a,
\qquad
\frac{8-\gamma}{2}=-a.
\]

The exact half-open partition induced by the ceiling function is

\[
\boxed{
\begin{aligned}
I_7&=\left(-1,-\frac12-a\right],\\
I_8&=\left(-\frac12-a,-a\right],\\
I_9&=(-a,0].
\end{aligned}}
\]

The boundary assignments are forced:

- at `x=-1/2-a`, `2x+gamma=7`, so `ceil(2x+gamma)=7`;
- at `x=-a`, `2x+gamma=8`, so `ceil(2x+gamma)=8`;
- at `x=0`, `2x+gamma=gamma in (8,9)`, so the carry is `9`;
- `x=-1` is excluded by the exact error interval.

For Lebesgue measure, changing finitely many endpoint assignments does not change any transition mass. For the exact individual orbit, the above half-open law is the required convention.

### Finite boundary check through `A=10000`

No boundary hit was found through `A=10000`. The calculation was repeated at `3500` and `4500` decimal digits and was stable to at least `70` displayed digits.

| Boundary | Closest domain | Minimum computed distance |
|---|---:|---:|
| `-1` | 1868 | `0.000347820781084709852124717722753387320148510640974287423008...` |
| `-1/2-a` | 1416 | `0.000097288657826505946361383750912616059397298062569572522242...` |
| `-a` | 2845 | `0.000162039752325495239177790016762946438168634913236091222511...` |
| `0` | 1417 | `0.000194577315653011892722767501825232118794596125139145044484...` |

The smallest finite distance is

\[
\boxed{
9.72886578265059463613837509126\times10^{-5}
}
\]

at `A=1416`, relative to the boundary `-1/2-a`.

This is a finite high-precision certificate. It is not a proof that no boundary is ever hit.

---

## 4. Interval maps

On the piece with carry `c`,

\[
F_c(x)=2x+\gamma-c.
\]

Using `gamma=8+2a`,

\[
F_7(x)=2x+1+2a,
\qquad
F_8(x)=2x+2a,
\qquad
F_9(x)=2x-1+2a.
\]

With the exact half-open intervals,

\[
F_7(I_7)=(-1+2a,0],
\]

\[
F_8(I_8)=(-1,0],
\]

\[
F_9(I_9)=(-1,-1+2a].
\]

Every branch has slope `2`. Therefore a target overlap of length `L` has source preimage length `L/2`.

The source interval lengths are

\[
\mu(I_7)=\frac12-a,
\qquad
\mu(I_8)=\frac12,
\qquad
\mu(I_9)=a.
\]

---

## 5. Derivation of the joint transition matrix `J`

Define

\[
J_{ij}=\mu\left(I_i\cap F_i^{-1}(I_j)\right),
\qquad i,j\in\{7,8,9\}.
\]

Since the full interval has length `1`, the entries are already normalized joint masses.

### 5.1 Row 7

The image `F_7(I_7)=(-1+2a,0]` starts inside `I_8`, covers the remainder of `I_8`, and covers all of `I_9`.

The inequality

\[
(-1+2a)-\left(-\frac12-a\right)=3a-\frac12>0
\]

uses `a>1/6` and proves that the image starts strictly to the right of `I_7`. Hence

\[
J_{77}=0.
\]

The image overlap with `I_8` has length

\[
-a-(-1+2a)=1-3a,
\]

so

\[
J_{78}=\frac{1-3a}{2}.
\]

The overlap with `I_9` has length `a`, so

\[
J_{79}=\frac a2.
\]

### 5.2 Row 8

The branch `F_8` maps `I_8` onto the full interval `(-1,0]`. Each target receives half its own length:

\[
J_{87}=\frac{1-2a}{4},
\qquad
J_{88}=\frac14,
\qquad
J_{89}=\frac a2.
\]

### 5.3 Row 9

The image `F_9(I_9)=(-1,-1+2a]` covers all of `I_7`, then an initial portion of `I_8`.

The inequality

\[
(-1+2a)-(-a)=-1+3a<0
\]

uses `a<1/3`, which follows from `a<1/4`, and proves that the image ends strictly to the left of `I_9`. Hence

\[
J_{99}=0.
\]

The full `I_7` overlap gives

\[
J_{97}=\frac{1-2a}{4}.
\]

The image overlap with `I_8` has length

\[
(-1+2a)-\left(-\frac12-a\right)=3a-\frac12,
\]

so

\[
J_{98}=\frac12\left(3a-\frac12\right)
=\frac{3a}{2}-\frac14.
\]

### 5.4 Symbolic and numerical matrix

With rows and columns ordered as `(7,8,9)`,

\[
\boxed{
J=
\begin{pmatrix}
0 & \dfrac{1-3a}{2} & \dfrac a2\\[2mm]
\dfrac{1-2a}{4} & \dfrac14 & \dfrac a2\\[2mm]
\dfrac{1-2a}{4} & \dfrac{3a}{2}-\dfrac14 & 0
\end{pmatrix}.}
\]

Numerically,

\[
J\approx
\begin{pmatrix}
0 & 0.147316546781912 & 0.117561151072696\\
0.132438848927304 & 0.250000000000000 & 0.117561151072696\\
0.132438848927304 & 0.102683453218088 & 0
\end{pmatrix}.
\]

Under `1/6<a<1/4`, exactly seven entries are positive:

\[
J_{78},J_{79},J_{87},J_{88},J_{89},J_{97},J_{98}>0,
\]

and exactly two entries are zero:

\[
J_{77}=J_{99}=0.
\]

The positivity of `J_98` is exactly where the lower assumption `a>1/6` is used. The negative control `a=1/10` gives `J_98=-1/10`, so the seven-positive-edge support law is not valid outside the stated interval.

---

## 6. Marginals, conditional matrix, and stationarity

The row sums are

\[
\left(\frac12-a,\frac12,a\right),
\]

and the column sums are the same. The total mass is `1`.

Define

\[
\boxed{
\pi_{\mathrm{Leb}}
=\left(\frac12-a,\frac12,a\right).
}
\]

The conditional transition matrix is

\[
P_{ij}=\frac{J_{ij}}{\pi_{\mathrm{Leb},i}}.
\]

Therefore

\[
\boxed{
P=
\begin{pmatrix}
0 & \dfrac{1-3a}{1-2a} & \dfrac{a}{1-2a}\\[3mm]
\dfrac{1-2a}{2} & \dfrac12 & a\\[3mm]
\dfrac{1-2a}{4a} & \dfrac{6a-1}{4a} & 0
\end{pmatrix}.}
\]

Numerically,

\[
P\approx
\begin{pmatrix}
0 & 0.556168178654189 & 0.443831821345811\\
0.264877697854608 & 0.500000000000000 & 0.235122302145392\\
0.563276421329900 & 0.436723578670100 & 0
\end{pmatrix}.
\]

Every row sums to `1`, so `P` is row stochastic. Also,

\[
\pi_{\mathrm{Leb}}P
=\pi_{\mathrm{Leb}},
\]

because the column sums of `J` equal `pi_Leb`.

Thus `J` is the stationary joint edge measure and `P` is its conditional transition law.

---

## 7. Topological system and Parry measure

The allowed transition graph has adjacency matrix

\[
\boxed{
M=
\begin{pmatrix}
0&1&1\\
1&1&1\\
1&1&0
\end{pmatrix}.}
\]

Its square is

\[
\boxed{
M^2=
\begin{pmatrix}
2&2&1\\
2&3&2\\
1&2&2
\end{pmatrix},}
\]

which is entrywise positive. Therefore `M` is primitive, with primitivity exponent at most `2` and in fact equal to `2` because `M` itself has zeros.

The eigenvalues are

\[
1+\sqrt2,
\qquad
-1,
\qquad
1-\sqrt2.
\]

The Perron root is

\[
\boxed{\rho=1+\sqrt2,}
\]

with Perron vector

\[
\boxed{r=(1,\sqrt2,1)^T.}
\]

The topological entropy is

\[
\boxed{h_{\mathrm{top}}=\log(1+\sqrt2).}
\]

Because `M` is symmetric, the left and right Perron vectors agree. Their squared normalization is

\[
1^2+(\sqrt2)^2+1^2=4.
\]

Hence the Parry state distribution is

\[
\boxed{
\pi_{\mathrm{Parry}}=\left(\frac14,\frac12,\frac14\right).
}
\]

The Parry joint edge measure is

\[
K_{ij}=\frac{M_{ij}r_ir_j}{4(1+\sqrt2)}.
\]

Thus

\[
\boxed{
K=\frac1{4(1+\sqrt2)}
\begin{pmatrix}
0&\sqrt2&1\\
\sqrt2&2&\sqrt2\\
1&\sqrt2&0
\end{pmatrix}.}
\]

Numerically,

\[
K\approx
\begin{pmatrix}
0&0.146446609406726&0.103553390593274\\
0.146446609406726&0.207106781186548&0.146446609406726\\
0.103553390593274&0.146446609406726&0
\end{pmatrix}.
\]

Its row sums and column sums are both `pi_Parry`, and its total mass is `1`.

The topological and geometric systems therefore share the same support but not the same invariant measure.

---

## 8. Direct finite edge comparison

The certified finite trace contains `9999` carry transitions for `A=2..10000`:

\[
C=
\begin{pmatrix}
0&1475&1162\\
1316&2568&1158\\
1321&999&0
\end{pmatrix}.
\]

Dividing by `9999` gives the empirical joint matrix

\[
\widehat J=
\begin{pmatrix}
0&0.147514751475148&0.116211621162116\\
0.131613161316132&0.256825682568257&0.115811581158116\\
0.132113211321132&0.099909990999100&0
\end{pmatrix}.
\]

### 8.1 Empirical versus Lebesgue `J`

\[
\max_{ij}|\widehat J_{ij}-J_{ij}|
=0.006825682568256826,
\]

\[
\|\widehat J-J\|_1
=0.014047774522984873,
\]

\[
\operatorname{TV}(\widehat J,J)
=\frac12\|\widehat J-J\|_1
=0.007023887261492436.
\]

### 8.2 Empirical versus Parry `K`

\[
\max_{ij}|\widehat J_{ij}-K_{ij}|
=0.049718901381709301,
\]

\[
\|\widehat J-K\|_1
=0.184010189493662757,
\]

\[
\operatorname{TV}(\widehat J,K)
=0.092005094746831379.
\]

The finite orbit is substantially closer to the Lebesgue joint law than to the Parry joint law on this range. This is finite evidence. It is not a proof that the specific orbit is equidistributed.

---

## 9. State-frequency comparison

The carry counts for `A=1..10000` are

\[
(2637,5042,2321)
\]

for states `(7,8,9)`.

| Measure | State 7 | State 8 | State 9 |
|---|---:|---:|---:|
| Parry | `0.250000000000000` | `0.500000000000000` | `0.250000000000000` |
| Lebesgue | `0.264877697854608` | `0.500000000000000` | `0.235122302145392` |
| Empirical, `A=1..10000` | `0.263700000000000` | `0.504200000000000` | `0.232100000000000` |

Empirical deviations from the Lebesgue state frequencies are

\[
(-0.001177697854608,
\ 0.004200000000000,
\ -0.003022302145392).
\]

Empirical deviations from the Parry state frequencies are

\[
(0.0137,
\ 0.0042,
\ -0.0179).
\]

Again, the finite state marginals are closer to the Lebesgue partition lengths, but no asymptotic conclusion is claimed.

---

## 10. Defect frequencies

For an edge `i -> j`, the defect is

\[
d=j-i.
\]

Aggregating `J` by defect gives

\[
\boxed{
\begin{aligned}
\Pr(d=-2)&=J_{97}=\frac{1-2a}{4},\\
\Pr(d=-1)&=J_{87}+J_{98}=a,\\
\Pr(d=0)&=J_{77}+J_{88}+J_{99}=\frac14,\\
\Pr(d=+1)&=J_{78}+J_{89}=\frac12-a,\\
\Pr(d=+2)&=J_{79}=\frac a2.
\end{aligned}}
\]

The finite counts over `A=2..10000` are:

| Defect | Count | Empirical frequency | Lebesgue benchmark | Empirical minus benchmark |
|---:|---:|---:|---:|---:|
| `-2` | 1321 | `0.132113211321132` | `0.132438848927304` | `-0.000325637606172` |
| `-1` | 2315 | `0.231523152315232` | `0.235122302145392` | `-0.003599149830161` |
| `0` | 2568 | `0.256825682568257` | `0.250000000000000` | `+0.006825682568257` |
| `+1` | 2633 | `0.263326332633263` | `0.264877697854608` | `-0.001551365221345` |
| `+2` | 1162 | `0.116211621162116` | `0.117561151072696` | `-0.001349529910580` |

### Defect aggregation loses edge information

The defect word is a quotient of the edge word:

- `d=-1` combines `8->7` and `9->8`;
- `d=+1` combines `7->8` and `8->9`;
- `d=0` records only equal-symbol edges and does not by itself identify which state supplied them;
- only `d=-2` and `d=+2` identify a unique edge.

Therefore the five defect frequencies cannot replace the full `3x3` joint transition matrix.

---

## 11. Evidence boundary for equidistribution

The following statements are supported:

1. `M` is primitive, so the allowed symbolic shift is topologically mixing.
2. `J` is the exact Lebesgue joint edge law for the interval coding.
3. The finite `A=2..10000` edge data are much closer to `J` than to the Parry edge measure `K`.
4. The finite state and defect marginals are close to the corresponding Lebesgue benchmarks.

The following statement is not proved:

```text
THE SPECIFIC ORBIT GENERATED BY THE QBL CONSTANTS IS EQUIDISTRIBUTED.
```

Primitivity proves a property of the allowed language. Ergodicity of the doubling map proves equidistribution for almost every starting point. Neither result proves that this specific logarithmic starting point is generic.

The correct wording is:

> The certified finite orbit provides evidence consistent with the Lebesgue invariant measure.

---

## 12. Current Orthad boundary

The current authority states that exact ordered QBL history is part of the retained state and that operation counts are insufficient. It also states that raw coordinate matrices are not retained invariants.

The following construction steps remain open obligations in the current Orthad law:

- the explicit all-depth recurrence for the primary pairing under the clean primitive state;
- explicit chart maps proving both lenses are restrictions at every prefix;
- exact bidirectional transfer recurrences at every prefix;
- full multi-axis FQM generation and classification.

Consequently, count primality or the arithmetic condition `d_A=+/-1` does not determine:

- a chart matrix;
- a gauge value;
- holonomy;
- an FQM class;
- a Weil projection.

The required locks are

```text
GAUGE/FQM MAP FROM d_A=±1: NOT YET DERIVED
GLOBAL T_A=ceil(y_A) BRIDGE: NOT YET PROVED
```

The arithmetic statement retained here is only

\[
B_A=2B_{A-1}+d_A,
\]

so `d_A=+/-1` is the oddness gate required for a nontrivial prime `B_A`. No topological interpretation is attached.

---

## 13. Proposed route for the global threshold theorem

The exact Fibonacci threshold contains a Binet correction to the affine logarithmic approximation. A plausible later proof route is:

1. write the exact threshold inequality using Binet's formula;
2. bound the decaying conjugate-root correction explicitly;
3. express the distance of the affine quantity from the nearest integer as a nonzero linear form in logarithms;
4. apply a suitable lower bound for that linear form;
5. prove that the lower bound eventually dominates the Binet correction;
6. check the remaining finite initial range directly.

This is only a proposed route. No explicit linear-form constants, crossover index, or global proof are supplied in this pass.

---

## 14. Final status split

### Proved abstractly

- The ceiling-map identities
  \[
  c_A=\lceil2E_{A-1}+\gamma\rceil,
  \qquad
  E_A=2E_{A-1}+\gamma-c_A
  \]
  for the affine model and `A>=1`.
- The exact half-open partition of `(-1,0]`.
- Every entry of `J` under `1/6<a<1/4`.
- Seven positive entries and the two geometric zeros `J_77=J_99=0`.
- Row sums, column sums, and total mass.
- The conditional matrix `P` and stationarity of `pi_Leb`.
- `M^2>0`, Perron root `1+sqrt(2)`, Perron vector `(1,sqrt(2),1)`, and Parry state measure `(1/4,1/2,1/4)`.
- The Parry joint edge measure `K` and its normalization.
- The five defect-mass identities.

### Certified finitely

- Prior exact Fibonacci threshold agreement with the affine ceiling model for `A=0..10000`.
- No computed partition-boundary hit through `A=10000`, with the minimum-distance calculation stable between `3500` and `4500` decimal digits.
- The `9999` carry transitions for `A=2..10000` and all direct edge metrics reported above.

### Observed

- The finite joint edge distribution is closer to `J` than to `K`.
- The finite state and defect frequencies are close to the Lebesgue benchmarks.
- The observed agreement is consistent with, but does not prove, specific-orbit equidistribution.

### Open

- Specific-orbit equidistribution or binary normality.
- Global exact equality between the Fibonacci threshold and `ceil(y_A)`.
- Any gauge/FQM meaning attached specifically to `d_A=+/-1` or to prime count events.
