# QBL Carry Geometry: Derivation of the Lebesgue Transition Matrix

**Status:** closed derivation on the affine dyadic ceiling model; finite QBL correspondence certified through `A = 10000`; global QBL correspondence not claimed  
**Constants:**

\[
\gamma=8.470244604290784127934989871\ldots,
\qquad
a=\frac{\gamma-8}{2}=0.235122302145392063967494936\ldots
\]

**Authority boundary:** this note uses the clean count laws and the experiment assumption lock. It does not infer an Orthad matrix, gauge value, FQM presentation, or topological transition from operation-count primality.

---

## 1. Strategic decision

Derive the interval transition matrix `J` first and keep the global Fibonacci-threshold bridge as a separate hard track.

This is the stronger ordering because:

1. `J` has a short, exact derivation from the already identified interval coding.
2. It separates topological admissibility from metric frequency immediately.
3. It explains the benchmark defect frequencies without overstating equidistribution.
4. It creates a closed theorem surface that does not depend on finishing the all-`A` Binet threshold proof.
5. It keeps the Orthad/FQM boundary clean instead of filling an open chart-map recurrence from count data.

Recommended order:

```text
interval coding
    -> exact joint transition matrix J
    -> defect-frequency benchmark
    -> topological vs metric comparison
    -> freeze equidistribution at evidence-only status
    -> later: global threshold bridge
    -> only after the all-depth Orthad recurrence exists: FQM prime map
```

---

## 2. Carry partition and map

Let the error coordinate lie in

\[
E\in(-1,0).
\]

The carry is determined by

\[
c=\lceil 2E+\gamma\rceil\in\{7,8,9\}.
\]

Since \(\gamma=8+2a\), the partition points are

\[
\frac{7-\gamma}{2}=-\frac12-a,
\qquad
\frac{8-\gamma}{2}=-a.
\]

Define

\[
I_7=\left(-1,-\frac12-a\right),
\]

\[
I_8=\left[-\frac12-a,-a\right),
\]

\[
I_9=[-a,0).
\]

Endpoint conventions do not affect any Lebesgue measure below.

Their lengths are

\[
\mu(I_7)=\frac12-a,
\qquad
\mu(I_8)=\frac12,
\qquad
\mu(I_9)=a.
\]

On the piece carrying symbol \(c\), the error evolves by

\[
F_c(x)=2x+\gamma-c.
\]

For the present constant,

\[
\frac16<a<\frac14.
\]

The three branch images are therefore

\[
F_7(I_7)=(-1+2a,0),
\]

\[
F_8(I_8)=(-1,0),
\]

\[
F_9(I_9)=(-1,-1+2a).
\]

Because every branch has slope `2`, a target-overlap interval of length `L` has a source preimage of length `L/2`.

---

## 3. Definition and derivation of `J`

Define the joint one-step Lebesgue transition mass

\[
J_{ij}=\mu\bigl(I_i\cap F_i^{-1}(I_j)\bigr),
\qquad i,j\in\{7,8,9\}.
\]

The total interval has length `1`, so these source lengths are already normalized joint masses. `J` is not a row-stochastic conditional matrix. Dividing a row by \(\mu(I_i)\) would produce the corresponding conditional probabilities.

### 3.1 Transitions from `7`

The image \((-1+2a,0)\) begins inside `I8`, crosses all of `I9`, and does not meet `I7`.

The overlap with `I8` has length

\[
-a-(-1+2a)=1-3a.
\]

Therefore

\[
J_{78}=\frac{1-3a}{2}.
\]

The overlap with `I9` has length `a`, so

\[
J_{79}=\frac a2.
\]

Also,

\[
J_{77}=0.
\]

### 3.2 Transitions from `8`

The branch `8` maps its entire source interval onto `(-1,0)`. Each target interval therefore receives half of its own length:

\[
J_{87}=\frac12\left(\frac12-a\right)=\frac{1-2a}{4},
\]

\[
J_{88}=\frac12\left(\frac12\right)=\frac14,
\]

\[
J_{89}=\frac12(a)=\frac a2.
\]

### 3.3 Transitions from `9`

The image \((-1,-1+2a)\) covers all of `I7`, then an initial portion of `I8`, and does not meet `I9`.

Thus

\[
J_{97}=\frac12\left(\frac12-a\right)=\frac{1-2a}{4}.
\]

The overlap with `I8` has length

\[
(-1+2a)-\left(-\frac12-a\right)=3a-\frac12,
\]

so

\[
J_{98}=\frac12\left(3a-\frac12\right)
      =\frac{3a}{2}-\frac14.
\]

Also,

\[
J_{99}=0.
\]

### 3.4 Closed matrix

With rows and columns ordered as `(7,8,9)`,

\[
\boxed{
J=
\begin{pmatrix}
0 & \dfrac{1-3a}{2} & \dfrac a2 \\
\dfrac{1-2a}{4} & \dfrac14 & \dfrac a2 \\
\dfrac{1-2a}{4} & \dfrac{3a}{2}-\dfrac14 & 0
\end{pmatrix}.}
\]

The requested count of six nonzero entries is off by one. There are **six nonzero off-diagonal entries plus the central entry**

\[
J_{88}=\frac14,
\]

so `J` has **seven** nonzero entries in total.

Numerically:

\[
J\approx
\begin{pmatrix}
0 & 0.1473165468 & 0.1175611511\\
0.1324388489 & 0.2500000000 & 0.1175611511\\
0.1324388489 & 0.1026834532 & 0
\end{pmatrix}.
\]

---

## 4. Invariance and the two forbidden transitions

The row sums are

\[
\left(\frac12-a,\frac12,a\right).
\]

The column sums are the same:

\[
\left(\frac12-a,\frac12,a\right).
\]

Therefore the partition-mass vector

\[
\boxed{
\pi_{\mathrm{Leb}}=
\left(\frac12-a,\frac12,a\right)
}
\]

is invariant under the joint transition geometry.

### Why `7 -> 7` has zero measure

The left endpoint of `F7(I7)` is `-1 + 2a`. The right endpoint of `I7` is `-1/2 - a`. Since

\[
(-1+2a)-\left(-\frac12-a\right)=3a-\frac12>0,
\]

`F7(I7)` lies strictly to the right of `I7`. Hence

\[
J_{77}=0.
\]

### Why `9 -> 9` has zero measure

The right endpoint of `F9(I9)` is `-1+2a`. The left endpoint of `I9` is `-a`. Since

\[
(-1+2a)-(-a)=-1+3a<0,
\]

`F9(I9)` lies strictly to the left of `I9`. Hence

\[
J_{99}=0.
\]

These are geometric exclusions, not merely transitions that happened to be absent in the finite trace.

---

## 5. Defect frequencies reproduced by `J`

For a transition from previous carry `i` to current carry `j`,

\[
d=j-i.
\]

Collecting the entries of `J` by adjacent difference gives:

\[
\boxed{
\begin{aligned}
\Pr(d=-2)&=J_{97}=\frac{1-2a}{4},\\
\Pr(d=-1)&=J_{87}+J_{98}=a,\\
\Pr(d=0)&=J_{88}=\frac14,\\
\Pr(d=+1)&=J_{78}+J_{89}=\frac12-a,\\
\Pr(d=+2)&=J_{79}=\frac a2.
\end{aligned}}
\]

Numerically:

| Defect | Closed form | Lebesgue benchmark |
|---:|---:|---:|
| `-2` | `(1-2a)/4` | `0.132438848927304` |
| `-1` | `a` | `0.235122302145392` |
| `0` | `1/4` | `0.250000000000000` |
| `+1` | `1/2-a` | `0.264877697854608` |
| `+2` | `a/2` | `0.117561151072696` |

This exactly reproduces the benchmark vector recorded in the experiment package.

---

## 6. Topological system versus geometric system

The allowed-transition adjacency matrix is

\[
M=
\begin{pmatrix}
0&1&1\\
1&1&1\\
1&1&0
\end{pmatrix}.
\]

Its square is strictly positive:

\[
M^2=
\begin{pmatrix}
2&2&1\\
2&3&2\\
1&2&2
\end{pmatrix},
\]

so `M` is irreducible and primitive with exponent `2`.

Its Perron root is

\[
\rho(M)=1+\sqrt2,
\]

and its topological entropy is

\[
h_{\mathrm{top}}=\log(1+\sqrt2).
\]

A Perron eigenvector is

\[
(1,\sqrt2,1).
\]

Because `M` is symmetric, the Parry state distribution is proportional to the componentwise square of this vector:

\[
\boxed{
\pi_{\mathrm{Parry}}=
\left(\frac14,\frac12,\frac14\right).
}
\]

The Parry measure is the maximal-entropy measure on the allowed symbolic language. It is not the same as the Lebesgue measure pushed through the actual interval coding.

### Carry-state frequency comparison

The empirical row below uses carries at `A = 2..10000`, with counts

```text
7: 2637
8: 5042
9: 2320
```

| Measure / sample | `7` | `8` | `9` |
|---|---:|---:|---:|
| Parry | `0.250000000000000` | `0.500000000000000` | `0.250000000000000` |
| Lebesgue coding | `0.264877697854608` | `0.500000000000000` | `0.235122302145392` |
| Empirical `A=2..10000` | `0.263726372637264` | `0.504250425042504` | `0.232023202320232` |

The empirical orbit is substantially closer to the Lebesgue coding than to the Parry measure:

```text
maximum state-frequency deviation from Parry:     0.0179767977
maximum state-frequency deviation from Lebesgue:  0.0042504250
```

Therefore the observed orbit follows the geometric benchmark much more closely than the maximal-entropy symbolic benchmark.

This distinguishes the two pictures:

```text
M:
    which carry words are topologically admissible

J:
    how Lebesgue interval mass is transported by the actual affine branches
```

---

## 7. Equidistribution boundary

The following statement is supported:

> The finite orbit through `A = 10000` agrees closely with the Lebesgue benchmark generated by `J`.

The following stronger statements are **not** supported:

```text
the specific logarithmic dyadic orbit is proved equidistributed
the carry word is proved generic for Lebesgue measure
primitivity of M proves this orbit is equidistributed
J proves the empirical frequencies for every A
```

Primitivity proves topological mixing of the allowed shift. Ergodicity of the doubling map proves Lebesgue-generic behavior for almost every starting point. Neither statement proves that this particular constant is a generic point.

Correct status:

```text
EQUILIBRIUM FREQUENCY LAW FOR LEBESGUE CODING: DERIVED
SPECIFIC ORBIT AGREEMENT THROUGH A=10000: OBSERVED
SPECIFIC ORBIT EQUIDISTRIBUTION: NOT PROVED
```

---

## 8. FQM and Orthad boundary

The experiment assumption lock explicitly forbids inferring any Orthad matrix claim from count primality.

The Orthad law also leaves the following as open obligations:

- the explicit all-depth recurrence for the primary pairing;
- explicit chart maps proving both lenses are restrictions at every prefix;
- exact bidirectional transfer recurrences at every prefix;
- full multi-axis FQM generation and classification.

Therefore no chart matrix, gauge transformation, holonomy value, or FQM isometry class may be assigned from `d_A`, `B_A`, or primality alone.

The current exact result is only

\[
B_A=2B_{A-1}+d_A,
\]

so

\[
B_A\text{ is odd}\iff d_A\in\{-1,+1\}.
\]

Thus `d = +/-1` is an arithmetic parity gate and a necessary B-prime candidate gate.

### NOT YET DERIVED 1

```text
A gauge/FQM transformation attached specifically to d_A = +/-1
is NOT YET DERIVED.
```

The FQM prime map becomes licensed only after the exact QBL-prefix-to-pairing-to-charts-to-transfers-to-FQM recurrence exists.

---

## 9. Global threshold bridge boundary

The experiment has certified

\[
T_A=\lceil y_A\rceil
\]

for `A = 0..10000`, but not for every `A`.

The next hard-track route is:

1. write the exact Fibonacci product using Binet's formula;
2. isolate the affine leading threshold coordinate `y_A`;
3. give a uniform upper bound on the decaying Binet correction;
4. give a nonzero lower bound for the distance of `y_A` from the nearest integer using a linear form in logarithms;
5. prove that the lower bound eventually dominates the Binet correction;
6. verify the remaining finite initial range directly.

This work is intentionally outside the present `J` derivation.

### NOT YET PROVED 2

```text
The global all-A identity T_A = ceil(y_A)
is NOT YET PROVED.
```

Consequently, `J` is a closed theorem for the affine dyadic ceiling model and is bound to the exact QBL threshold sequence on the currently certified finite range. Its all-`A` identification with exact Fibonacci threshold counts remains conditional on the global bridge.

---

## 10. Final disposition

```text
J DERIVATION: CLOSED
SEVEN NONZERO TRANSITION MASSES: CLOSED
7->7 AND 9->9 ZERO-MEASURE EXCLUSION: CLOSED
LEBESGUE DEFECT BENCHMARK: CLOSED
PERRON ROOT / ENTROPY / PARRY MEASURE: CLOSED
PARRY VS LEBESGUE DISTINCTION: CLOSED
FINITE ORBIT AGREEMENT THROUGH A=10000: EVIDENCE
SPECIFIC ORBIT EQUIDISTRIBUTION: NOT PROVED
FQM PRIME MAP: NOT YET DERIVED
GLOBAL THRESHOLD BRIDGE: NOT YET PROVED
```
