# QBL Carry J Derivation and Symbolic Boundary v3

**Status:** corrected theorem-and-boundary document  
**Step:** `p5-b1-v5`  
**Primary Orthad authority:** `inputs/20260711T074914_QBL_PRIMITIVE_CUSTODY_AND_ORTHAD_LAW_v2.md`  
**Older Phase 5 ledger:** provenance only  
**Affine parameter:**

\[
\gamma=8.4702446042907841279349898711327462608\ldots,
\qquad
a=\frac{\gamma-8}{2}=0.2351223021453920639674949355663731304\ldots
\]

with

\[
\frac16<a<\frac14,
\qquad
a>\frac3{14}.
\]

## 1. Disposition

### Proved abstractly

- The affine ceiling recurrence induces the exact error-coordinate map.
- The half-open carry partition is exact.
- The one-step Lebesgue joint law \(J\), conditional table \(P\), stationarity, and five defect masses are exact under \(1/6<a<1/4\).
- The pairwise support matrix \(M\) is not the full language: `989` is forbidden despite both of its adjacent pairs being allowed.
- At the current constant, exactly fifteen length-three words are realizable; the pairwise envelope admits seventeen.
- The affine carry coding has exact word complexity \(p(n)=2^{n+1}-1\) and therefore entropy \(\log 2\).
- \(\log(1+\sqrt2)\) is the entropy only of the pairwise edge-shift envelope.

### Certified finitely

- The imported trace has exactly one row for every \(A=0,\ldots,10000\), every carry lies in \(\{7,8,9\}\), and it contains exactly 9999 transitions.
- Its transition counts exactly match the included prior transition table.
- Direct interval enumeration agrees with \(2^{n+1}-1\) through length 12; exact boundary-preimage counting supplies lengths 13 through 20.
- Outward-rounded interval arithmetic certifies no affine-orbit boundary hit for \(A=0,\ldots,10000\).
- Exact cylinder calculations rule out every fixed Markov order \(k\le10\).

### Observed

- The finite orbit is substantially closer to the Lebesgue edge law \(J\) than to the Parry edge law \(K\) of the pairwise envelope.
- State and defect frequencies are close to the Lebesgue benchmarks on the finite range.

### Open

```text
ACTUAL CARRY LANGUAGE PRESENTATION: NOT YET DERIVED
SPECIFIC-ORBIT EQUIDISTRIBUTION: NOT PROVED
GLOBAL T_A=ceil(y_A) BRIDGE: NOT YET PROVED
GAUGE/FQM MAP FROM d_A=±1: NOT YET DERIVED
ACTUAL CARRY LANGUAGE MIXING: NOT YET DERIVED
```

The exact complexity and entropy theorem applies to the **affine ceiling coding**. Transfer of that theorem to the exact Fibonacci-threshold process for every \(A\) still requires the global threshold bridge.

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

For every \(A\ge1\),

\[
\begin{aligned}
T_A
&=\left\lceil2y_{A-1}+\gamma\right\rceil\\
&=\left\lceil2(T_{A-1}+E_{A-1})+\gamma\right\rceil\\
&=\left\lceil2T_{A-1}+2E_{A-1}+\gamma\right\rceil\\
&=2T_{A-1}+\left\lceil2E_{A-1}+\gamma\right\rceil,
\end{aligned}
\]

because \(2T_{A-1}\in\mathbb Z\). Hence

\[
\boxed{c_A=\left\lceil2E_{A-1}+\gamma\right\rceil},
\qquad A\ge1.
\]

Likewise,

\[
\begin{aligned}
E_A
&=y_A-T_A\\
&=2y_{A-1}+\gamma-T_A\\
&=2(T_{A-1}+E_{A-1})+\gamma-T_A\\
&=2E_{A-1}+\gamma-(T_A-2T_{A-1}),
\end{aligned}
\]

so

\[
\boxed{E_A=2E_{A-1}+\gamma-c_A},
\qquad A\ge1.
\]

This is an exact theorem of the affine ceiling model. The identification of the exact Fibonacci threshold with \(\lceil y_A\rceil\) is imported only on \(A=0,\ldots,10000\) and remains globally open.

## 3. Endpoint law and carry partition

For the ceiling convention,

\[
E_A=y_A-\lceil y_A\rceil\in(-1,0].
\]

The interval is left-open and right-closed:

- if \(y_A\notin\mathbb Z\), then \(-1<E_A<0\);
- if \(y_A\in\mathbb Z\), then \(E_A=0\).

Since \(\gamma=8+2a\), the carry partition is

\[
\begin{aligned}
I_7&=\left(-1,-\frac12-a\right],\\
I_8&=\left(-\frac12-a,-a\right],\\
I_9&=(-a,0].
\end{aligned}
\]

At the two internal boundaries the ceiling assigns downward:

\[
2\left(-\frac12-a\right)+\gamma=7,
\qquad
2(-a)+\gamma=8.
\]

Thus \(-\frac12-a\in I_7\) and \(-a\in I_8\). The point \(0\) belongs to \(I_9\).

The branch maps are

\[
F_c(x)=2x+\gamma-c,
\]

or explicitly

\[
F_7(x)=2x+1+2a,
\quad
F_8(x)=2x+2a,
\quad
F_9(x)=2x-1+2a.
\]

## 4. One-step Lebesgue law \(J\)

For states ordered as \((7,8,9)\), define

\[
J_{ij}=\operatorname{Leb}\{x\in I_i:F_i(x)\in I_j\}.
\]

The exact matrix is

\[
\boxed{
J=
\begin{pmatrix}
0 & \dfrac{1-3a}{2} & \dfrac a2\\[2mm]
\dfrac{1-2a}{4} & \dfrac14 & \dfrac a2\\[2mm]
\dfrac{1-2a}{4} & \dfrac{3a}{2}-\dfrac14 & 0
\end{pmatrix}.}
\]

For \(1/6<a<1/4\), seven entries are positive and exactly two are zero:

\[
J_{77}=J_{99}=0.
\]

The row and column marginals are both

\[
\pi_{\mathrm{Leb}}=\left(\frac12-a,\frac12,a\right),
\]

and the total mass is one.

At the current parameter,

\[
J\approx
\begin{pmatrix}
0 & 0.147316546781912 & 0.117561151072696\\
0.132438848927304 & 0.25 & 0.117561151072696\\
0.132438848927304 & 0.102683453218088 & 0
\end{pmatrix}.
\]

## 5. Conditional one-step table \(P\)

Define

\[
P_{ij}=\frac{J_{ij}}{\pi_{\mathrm{Leb},i}}.
\]

Then

\[
P=
\begin{pmatrix}
0 & \dfrac{1-3a}{1-2a} & \dfrac{a}{1-2a}\\[2mm]
\dfrac{1-2a}{2} & \dfrac12 & a\\[2mm]
\dfrac{1-2a}{4a} & \dfrac{6a-1}{4a} & 0
\end{pmatrix}.
\]

Every row sums to one and \(\pi_{\mathrm{Leb}}P=\pi_{\mathrm{Leb}}\).

This makes \(P\) the exact **one-step conditional table** under Lebesgue measure. It does not make the complete symbolic process first-order Markov.

## 6. The pairwise graph is incomplete

The pairwise-support matrix is

\[
M=\begin{pmatrix}0&1&1\\1&1&1\\1&1&0\end{pmatrix}.
\]

It records the seven positive entries of \(J\). It does not encode all higher-order interval constraints.

### 6.1 Full proof that `989` is forbidden

The prefix `9→8` begins in \(I_9=(-a,0]\). Its image under \(F_9\) is

\[
F_9(I_9)=(-1,-1+2a].
\]

Intersecting with \(I_8=(-\frac12-a,-a]\) gives

\[
C_{98}=\left(-\frac12-a,-1+2a\right].
\]

Applying \(F_8(x)=2x+2a\),

\[
F_8(C_{98})=(-1,-2+6a].
\]

Because \(a<1/4\), \(-2+6a<-1/2<-a\). Therefore

\[
F_8(C_{98})\cap I_9=\varnothing.
\]

Hence \(989\) is impossible even though \(M_{98}=M_{89}=1\).

### 6.2 The second missing pairwise word

For `7→8`,

\[
C_{78}=(-1+2a,-a],
\qquad
F_8(C_{78})=(-2+6a,0].
\]

This intersects \(I_7=(-1,-\frac12-a]\) only when \(a<3/14\). The current constant satisfies \(a>3/14\), certified by the included outward interval enclosure. Therefore `787` is also absent at the current parameter.

## 7. Complete length-three language

The table uses initial-error cylinders \(C(w)\subset(-1,0]\). All nonempty intervals are left-open and right-closed.

| Word | Pairwise envelope | Realizable | Initial cylinder | Reason |
|---|---:|---:|---|---|
| `777` | NO | NO | `empty` | empty because 7->7 has zero one-step mass |
| `778` | NO | NO | `empty` | empty because 7->7 has zero one-step mass |
| `779` | NO | NO | `empty` | empty because 7->7 has zero one-step mass |
| `787` | YES | NO | `empty` | empty at the current constant: after 7->8, F8 image starts at -2+6a; a>3/14 makes it miss I7 |
| `788` | YES | YES | `(-1, -7/4*a -1/2]` | nonempty exact affine cylinder at the current parameter enclosure |
| `789` | YES | YES | `(-7/4*a -1/2, -3/2*a -1/2]` | nonempty exact affine cylinder at the current parameter enclosure |
| `797` | YES | YES | `(-3/2*a -1/2, -7/4*a -3/8]` | nonempty exact affine cylinder at the current parameter enclosure |
| `798` | YES | YES | `(-7/4*a -3/8, -a -1/2]` | nonempty exact affine cylinder at the current parameter enclosure |
| `799` | NO | NO | `empty` | empty because 9->9 has zero one-step mass |
| `877` | NO | NO | `empty` | empty because 7->7 has zero one-step mass |
| `878` | YES | YES | `(-a -1/2, -7/4*a -1/4]` | nonempty exact affine cylinder at the current parameter enclosure |
| `879` | YES | YES | `(-7/4*a -1/4, -3/2*a -1/4]` | nonempty exact affine cylinder at the current parameter enclosure |
| `887` | YES | YES | `(-3/2*a -1/4, -7/4*a -1/8]` | nonempty exact affine cylinder at the current parameter enclosure |
| `888` | YES | YES | `(-7/4*a -1/8, -7/4*a]` | nonempty exact affine cylinder at the current parameter enclosure |
| `889` | YES | YES | `(-7/4*a, -3/2*a]` | nonempty exact affine cylinder at the current parameter enclosure |
| `897` | YES | YES | `(-3/2*a, -7/4*a + 1/8]` | nonempty exact affine cylinder at the current parameter enclosure |
| `898` | YES | YES | `(-7/4*a + 1/8, -a]` | nonempty exact affine cylinder at the current parameter enclosure |
| `899` | NO | NO | `empty` | empty because 9->9 has zero one-step mass |
| `977` | NO | NO | `empty` | empty because 7->7 has zero one-step mass |
| `978` | YES | YES | `(-a, -7/4*a + 1/4]` | nonempty exact affine cylinder at the current parameter enclosure |
| `979` | YES | YES | `(-7/4*a + 1/4, -3/2*a + 1/4]` | nonempty exact affine cylinder at the current parameter enclosure |
| `987` | YES | YES | `(-3/2*a + 1/4, -7/4*a + 3/8]` | nonempty exact affine cylinder at the current parameter enclosure |
| `988` | YES | YES | `(-7/4*a + 3/8, 0]` | nonempty exact affine cylinder at the current parameter enclosure |
| `989` | YES | NO | `empty` | empty: after 9->8, F8 image is (-1,-2+6a], which lies left of I9 for a<1/4 |
| `997` | NO | NO | `empty` | empty because 9->9 has zero one-step mass |
| `998` | NO | NO | `empty` | empty because 9->9 has zero one-step mass |
| `999` | NO | NO | `empty` | empty because 9->9 has zero one-step mass |

Thus \(\#\mathcal L_3=15\) while \(\#\mathcal E_3=17\).

## 8. Exact word complexity and entropy

Set \(z=E+1\pmod1\). The affine error map becomes

\[
z'=2z+2a\pmod1.
\]

Translate by \(y=z+2a\pmod1\). Then \(y'=2y\pmod1\), so the affine carry map is conjugate to the ordinary doubling map \(D(y)=2y\pmod1\).

Let \(p=2a\). The two internal carry boundaries become \(a\) and \(a+1/2\), exactly the two preimages of \(p\).

### 8.1 Irrationality of the cut point

From the definitions,

\[
p=-\frac{13}{2}+\frac{\log(4096/5)}{2\log\varphi}.
\]

If \(p\in\mathbb Q\), then \(\log(4096/5)/\log\varphi\in\mathbb Q\). Writing that positive rational as \(m/n\) yields

\[
\left(\frac{4096}{5}\right)^n=\varphi^m.
\]

The left side is rational, whereas \(\varphi^m=F_m\varphi+F_{m-1}\) is irrational for every positive integer \(m\). Contradiction. Therefore \(p=2a\) is irrational.

### 8.2 Boundary-preimage count

The length-\(n\) refinement boundaries are

\[
\{p\}\cup\bigcup_{m=1}^n D^{-m}(p).
\]

Each \(D^{-m}(p)\) has \(2^m\) points. Different levels are disjoint: an overlap between levels \(m<n\) would imply \(D^{n-m}(p)=p\), making \(p\) periodic and rational.

Therefore

\[
\boxed{p(n)=1+\sum_{m=1}^n2^m=2^{n+1}-1}
\]

and

\[
\boxed{h_{\mathrm{actual,affine}}=\log2}.
\]

This proves equality with the degree-two upper bound for the affine coding. It does not prove the global exact-Fibonacci threshold bridge.

### 8.3 Complexity through length 20

| Length | Actual affine cylinders | Direct interval enumeration | Edge-envelope paths | Envelope excess |
|---:|---:|---:|---:|---:|
| 1 | 3 | 3 | 3 | 0 |
| 2 | 7 | 7 | 7 | 0 |
| 3 | 15 | 15 | 17 | 2 |
| 4 | 31 | 31 | 41 | 10 |
| 5 | 63 | 63 | 99 | 36 |
| 6 | 127 | 127 | 239 | 112 |
| 7 | 255 | 255 | 577 | 322 |
| 8 | 511 | 511 | 1393 | 882 |
| 9 | 1023 | 1023 | 3363 | 2340 |
| 10 | 2047 | 2047 | 8119 | 6072 |
| 11 | 4095 | 4095 | 19601 | 15506 |
| 12 | 8191 | 8191 | 47321 | 39130 |
| 13 | 16383 | not enumerated | 114243 | 97860 |
| 14 | 32767 | not enumerated | 275807 | 243040 |
| 15 | 65535 | not enumerated | 665857 | 600322 |
| 16 | 131071 | not enumerated | 1607521 | 1476450 |
| 17 | 262143 | not enumerated | 3880899 | 3618756 |
| 18 | 524287 | not enumerated | 9369319 | 8845032 |
| 19 | 1048575 | not enumerated | 22619537 | 21570962 |
| 20 | 2097151 | not enumerated | 54608393 | 52511242 |

Direct interval enumeration was performed through length 12. Lengths 13 through 20 use the exact boundary-preimage theorem.

## 9. Finite-state, Markov, and mixing boundary

A finite-state presentation that generates exactly the full affine carry language was not established.

```text
ACTUAL CARRY LANGUAGE PRESENTATION: NOT YET DERIVED
```

Exact cylinder witnesses disprove fixed Markov orders 1 through 10:

| Tested order | Shared suffix | First follower set | Second follower set |
|---:|---|---|---|
| 1 | `8` | `78` → `89` | `88` → `789` |
| 2 | `88` | `788` → `89` | `888` → `789` |
| 3 | `888` | `7888` → `789` | `9888` → `7` |
| 4 | `8887` | `78887` → `89` | `98887` → `8` |
| 5 | `88878` | `788878` → `89` | `988878` → `8` |
| 6 | `888788` | `7888788` → `89` | `9888788` → `8` |
| 7 | `8887888` | `78887888` → `9` | `88887888` → `789` |
| 8 | `88878889` | `788878889` → `8` | `888878889` → `78` |
| 9 | `888788898` | `7888788898` → `78` | `9888788898` → `7` |
| 10 | `8887888987` | `78887888987` → `89` | `98887888987` → `8` |

These do not prove that no finite sofic presentation exists.

The matrix \(M\) has \(M^2>0\), so the **pairwise edge-shift envelope** is mixing. No mixing claim is transferred to the full language.

```text
ACTUAL CARRY LANGUAGE MIXING: NOT YET DERIVED
```

## 10. Corrected edge-envelope Perron and Parry data

For the pairwise envelope,

\[
\rho=1+\sqrt2,
\qquad
r=(1,\sqrt2,1)^T,
\qquad
h_{\mathrm{edge\ envelope}}=\log(1+\sqrt2).
\]

The Parry state distribution of the envelope is \((1/4,1/2,1/4)\). Its joint edge measure is

\[
K_{ij}=\frac{M_{ij}r_ir_j}{4(1+\sqrt2)}
\]

and has row and column marginals \((1/4,1/2,1/4)\) and total mass one. It is an optional over-approximating baseline, not the maximal-entropy measure of the actual coding.

## 11. Direct finite edge comparison

The empirical joint matrix for transitions \(A=2,\ldots,10000\) is

\[
\widehat J=\begin{pmatrix}
0 & 1475/9999 & 1162/9999\\
1316/9999 & 2568/9999 & 1158/9999\\
1321/9999 & 999/9999 & 0
\end{pmatrix}.
\]

| Comparison | Maximum absolute error | \(L^1\) error | Total variation |
|---|---:|---:|---:|
| Empirical vs. \(J\) | 0.0068256825682568256825682568256825682568256825682568256825682568256825682568256826 | 0.014047774522984872770571615379987478043369022030181406333002463062002686548350906 | 0.007023887261492436385285807689993739021684511015090703166501231531001343274175453 |
| Empirical vs. envelope \(K\) | 0.049718901381709301281723894720833528971989744879782789094228387830316329025772163 | 0.18401018949366275733052021901598593545082271998788322076803369834443433561216997 | 0.092005094746831378665260109507992967725411359993941610384016849172217167806084987 |

These are finite comparisons, not an equidistribution proof.

## 12. State and defect frequencies

### 12.1 Carry states

| Carry | Count | Empirical | Lebesgue | Parry envelope |
|---:|---:|---:|---:|---:|
| 7 | 2637 | 0.2637000000 | 0.2648776979 | 0.2500000000 |
| 8 | 5042 | 0.5042000000 | 0.5000000000 | 0.5000000000 |
| 9 | 2321 | 0.2321000000 | 0.2351223021 | 0.2500000000 |

### 12.2 Defects

The exact Lebesgue defect masses are

\[
\Pr(-2)=\frac{1-2a}{4},\quad
\Pr(-1)=a,\quad
\Pr(0)=\frac14,\quad
\Pr(1)=\frac12-a,\quad
\Pr(2)=\frac a2.
\]

| Defect | Count | Empirical | Lebesgue benchmark | Deviation |
|---:|---:|---:|---:|---:|
| -2 | 1321 | 0.1321132113 | 0.1324388489 | -0.0003256376 |
| -1 | 2315 | 0.2315231523 | 0.2351223021 | -0.0035991498 |
| 0 | 2568 | 0.2568256826 | 0.2500000000 | +0.0068256826 |
| 1 | 2633 | 0.2633263326 | 0.2648776979 | -0.0015513652 |
| 2 | 1162 | 0.1162116212 | 0.1175611511 | -0.0013495299 |

Defect aggregation loses edge information. For example, \(d=-1\) combines `8→7` and `9→8`; their sum cannot detect `989`.

## 13. Finite endpoint certificate

This package uses outward-rounded interval arithmetic through `mpmath.iv==1.3.0` at 3300 decimal digits. The imported carry word was propagated by interval recurrence. At every one of 10000 steps, the complete source interval lies inside its assigned half-open carry piece and the complete ceiling argument lies inside \((c_A-1,c_A]\).

```text
all imported carries certified: true
all E_A intervals disjoint from every boundary for A=0..10000: true
minimum certified boundary separation:
  A = 1416
  boundary = b7
  lower bound = 0.0000972886578265059463613837509126160593972980625695725222419052083488155622623262037317601713999371329179548992365886789964
maximum propagated orbit interval width:
  5.64373810178526734283704027260205632687047918756941594617872441211609614703745251588738458567147023114749159028711825257e-289
```

This is finite certification only. Global nonintegrality remains open.

## 14. Threshold and equidistribution boundary

The exact Fibonacci-threshold agreement through \(A=10000\) is an **imported prior finite certificate**. This package validates the rows, carries, and transition counts but does not rerun the original threshold verifier.

```text
GLOBAL T_A=ceil(y_A) BRIDGE: NOT YET PROVED
SPECIFIC-ORBIT EQUIDISTRIBUTION: NOT PROVED
```

A proposed later route is Binet correction control against a lower bound for a nonzero linear form in logarithms, followed by finite verification. It is not a result of this pass.

## 15. Orthad and FQM boundary

The current Orthad law states that ordered QBL history is retained state and operation counts are insufficient. It also leaves open the all-prefix primary-pairing recurrence, explicit chart maps, bidirectional transfer recurrences, and full multi-axis FQM construction.

Count primality and \(d_A=\pm1\) therefore cannot determine a chart matrix, gauge value, holonomy, FQM class, or Weil projection.

```text
GAUGE/FQM MAP FROM d_A=±1: NOT YET DERIVED
```

The proved statement is only arithmetic: \(B_A=2B_{A-1}+d_A\), so \(d_A=\pm1\) is the oddness gate for a possible prime \(B_A\).

## 16. Final corrected boundary

```text
AFFINE CEILING MAP: PROVED
HALF-OPEN PARTITION: PROVED
ONE-STEP LEBESGUE LAW J: PROVED
ONE-STEP CONDITIONAL TABLE P: PROVED
PAIRWISE EDGE-SHIFT ENVELOPE M/K: PROVED AND RELABELED
PAIRWISE ENVELOPE AS FULL LANGUAGE: FALSE
AFFINE WORD COMPLEXITY p(n)=2^(n+1)-1: PROVED
AFFINE CODING ENTROPY log(2): PROVED
FINITE BOUNDARY NONHIT A=0..10000: OUTWARD-INTERVAL CERTIFIED
ACTUAL CARRY LANGUAGE PRESENTATION: NOT YET DERIVED
ACTUAL CARRY LANGUAGE MIXING: NOT YET DERIVED
SPECIFIC-ORBIT EQUIDISTRIBUTION: NOT PROVED
GLOBAL T_A=ceil(y_A) BRIDGE: NOT YET PROVED
GAUGE/FQM MAP FROM d_A=±1: NOT YET DERIVED
LEAN SOURCE PRESENT; COMPILATION NOT VERIFIED
```
