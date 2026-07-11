# QBL Global Exact-Threshold Bridge

**Branch:** `p5-b2-v2`  
**Status:** theorem-bearing research document  
**Current Orthad authority:** `QBL_PRIMITIVE_CUSTODY_AND_ORTHAD_LAW_v2.md`  
**Older canonical ledgers:** provenance only

## 1. Result

The exact Fibonacci threshold count agrees with the affine ceiling law for every domain index \(A\ge 0\):

\[
\boxed{T_A=\lceil y_A\rceil}.
\]

The proof does not require a Baker–Matveev cutoff. Binet's formula leaves a bounded additive correction of absolute size strictly below \(1/4\), while the exact Fibonacci product and the QBL threshold are distinct integers. Their nonzero integer gap is at least \(1\). Therefore the affine leading term and the exact product lie on the same side of the threshold, uniformly for every \(A\) and every candidate depth \(n\).

```text
GLOBAL T_A=ceil(y_A) BRIDGE: PROVED
GAUGE/FQM MAP FROM d_A=±1: NOT YET DERIVED
```

## 2. Exact threshold definition

Use the Fibonacci convention

\[
F_0=0,\qquad F_1=1,\qquad F_{k+2}=F_{k+1}+F_k.
\]

After \(n\) balanced refinements, the carried pair is

\[
(F_{n+1},F_{n+2}),
\]

so the exact product is

\[
P_n:=F_{n+1}F_{n+2}.
\]

For domain \(A\), the final global phase-position index is

\[
j_{\mathrm{final}}(A)=6(2^{A+1}-1),
\]

and the final capacity is

\[
X_A:=2^{2j_{\mathrm{final}}(A)}
    =2^{m_A},
\qquad
m_A:=12(2^{A+1}-1).
\]

The exact cumulative threshold count is

\[
T_A:=\min\{n\in\mathbb N_0:P_n\ge X_A\}.
\]

Define

\[
\varphi:=\frac{1+\sqrt5}2
\]

and the affine main term

\[
y_A:=\frac{m_A\log2+\log5}{2\log\varphi}-\frac32.
\]

Equivalently, with

\[
\alpha:=\frac{6\log2}{\log\varphi},
\qquad
\gamma:=\alpha+\frac32-\frac{\log5}{2\log\varphi},
\]

we have

\[
y_A=\alpha 2^{A+1}-\gamma,
\qquad
y_A=2y_{A-1}+\gamma\quad(A\ge1).
\]

Numerically,

\[
\alpha=8.64252054247533887410530899753,\qquad
\gamma=8.47024460429078412793498987113.
\]

The target identity is exactly

\[
\min\{n:F_{n+1}F_{n+2}\ge2^{12(2^{A+1}-1)}\}
=
\left\lceil
\frac{12(2^{A+1}-1)\log2+\log5}{2\log\varphi}-\frac32
\right\rceil.
\]

## 3. Exact Binet reduction

Let

\[
\psi:=\frac{1-\sqrt5}2=-\varphi^{-1}.
\]

Binet's formula gives

\[
F_k=\frac{\varphi^k-\psi^k}{\sqrt5}.
\]

Therefore

\[
\begin{aligned}
P_n
&=\frac15
(\varphi^{n+1}-\psi^{n+1})
(\varphi^{n+2}-\psi^{n+2})\\
&=\frac15\left(
\varphi^{2n+3}
-\varphi^{n+1}\psi^{n+2}
-\psi^{n+1}\varphi^{n+2}
+\psi^{2n+3}
\right).
\end{aligned}
\]

Since \(\psi=-\varphi^{-1}\),

\[
-\varphi^{n+1}\psi^{n+2}
-\psi^{n+1}\varphi^{n+2}
=(-1)^n(\varphi-\varphi^{-1})=(-1)^n,
\]

using \(\varphi-\varphi^{-1}=1\), and

\[
\psi^{2n+3}=-\varphi^{-(2n+3)}.
\]

Hence the exact closed form is

\[
\boxed{
P_n=L_n+\rho_n
}
\]

with

\[
L_n:=\frac{\varphi^{2n+3}}5,
\qquad
\rho_n:=\frac{(-1)^n-\varphi^{-(2n+3)}}5.
\]

This is the exact additive split. The correction is a bounded signed parity term with an exponentially decaying tail. Relative to the leading term it decays exponentially. Equivalently, with \(s=2n+3\),

\[
P_n=\frac{\varphi^s}{5}\left(1+(-1)^n\varphi^{-s}-\varphi^{-2s}\right),
\]

so the logarithmic correction

\[
\eta_n:=\log\left(1+(-1)^n\varphi^{-s}-\varphi^{-2s}\right)
\]

is exponentially decaying and

\[
\log P_n=s\log\varphi-\log5+\eta_n.
\]

The global proof below uses the sharper additive correction and integer separation.

## 4. Uniform correction bound

For even \(n\),

\[
0<\rho_n<\frac15.
\]

For odd \(n\ge1\),

\[
|\rho_n|
=\frac{1+\varphi^{-(2n+3)}}5
\le\frac{1+\varphi^{-5}}5
<\frac14,
\]

because \(\varphi^5>4\). Thus, uniformly for every \(n\ge0\),

\[
\boxed{|\rho_n|<\frac14}.
\]

The sign is also exact:

\[
\rho_n>0\text{ for even }n,
\qquad
\rho_n<0\text{ for odd }n.
\]

## 5. Exact equality is impossible

For consecutive Fibonacci numbers,

\[
\gcd(F_{n+1},F_{n+2})=1.
\]

Suppose

\[
P_n=F_{n+1}F_{n+2}=2^m.
\]

Both factors must then be powers of \(2\). Since they are coprime, one factor must equal \(1\). The only Fibonacci indices with value \(1\) are \(1\) and \(2\). Hence the only consecutive products that are powers of two are

\[
P_0=F_1F_2=1,
\qquad
P_1=F_2F_3=2.
\]

But for every \(A\ge0\),

\[
m_A\ge12,
\qquad
X_A\ge2^{12}=4096.
\]

Therefore

\[
\boxed{P_n\ne X_A\quad\text{for all }A,n\ge0}.
\]

This nonzero condition is the load-bearing replacement for an external lower-bound theorem.

## 6. Integer-gap sign-transfer lemma

Fix \(A,n\ge0\). Since \(P_n-X_A\) is a nonzero integer,

\[
|P_n-X_A|\ge1.
\]

Because \(P_n=L_n+\rho_n\),

\[
L_n-X_A=(P_n-X_A)-\rho_n.
\]

If \(P_n>X_A\), then \(P_n-X_A\ge1\), so

\[
L_n-X_A>1-\frac14=\frac34>0.
\]

If \(P_n<X_A\), then \(P_n-X_A\le-1\), so

\[
L_n-X_A<-1+\frac14=-\frac34<0.
\]

Consequently,

\[
\boxed{
P_n>X_A\iff L_n>X_A
}
\]

and the leading-term separation is uniformly bounded by

\[
\boxed{|L_n-X_A|>\frac34}.
\]

This is stronger than a merely asymptotic Binet estimate: the exact integer lattice prevents the exponentially small correction from ever changing the threshold side.

## 7. Ceiling reduction and global theorem

By definition of \(y_A\),

\[
L_n>X_A
\iff
\frac{\varphi^{2n+3}}5>2^{m_A}
\iff
n>y_A.
\]

The value \(y_A\) cannot be an integer. If \(y_A=n\in\mathbb Z\), then \(L_n=X_A\). But

\[
P_n-X_A=\rho_n
\]

would be an integer of absolute value below \(1/4\), forcing \(\rho_n=0\), which is impossible from its exact formula.

Thus

\[
n>y_A\iff n\ge\lceil y_A\rceil.
\]

Combining this with the sign-transfer lemma,

\[
\begin{aligned}
T_A
&=\min\{n:P_n\ge X_A\}\\
&=\min\{n:P_n>X_A\}\\
&=\min\{n:L_n>X_A\}\\
&=\min\{n:n>y_A\}\\
&=\lceil y_A\rceil.
\end{aligned}
\]

Therefore:

\[
\boxed{T_A=\lceil y_A\rceil\quad\text{for every }A\ge0}.
\]

## 8. Distance-to-integers and logarithmic linear form

The relevant logarithmic linear form is

\[
\Lambda_{A,n}
:=(2n+3)\log\varphi-\log5-m_A\log2
=2\log\varphi\,(n-y_A).
\]

It is nonzero for every \(A,n\ge0\), by the preceding argument.

Since

\[
\frac{L_n}{X_A}=e^{\Lambda_{A,n}}
\]

and \(|L_n-X_A|>3/4\),

\[
|e^{\Lambda_{A,n}}-1|
>\frac{3}{4X_A}.
\]

Set

\[
c_A^*:=\frac{3}{4X_A}.
\]

For \(\Lambda\ge0\), the preceding inequality implies

\[
\Lambda>\log(1+c_A^*).
\]

For \(\Lambda<0\), it implies

\[
-\Lambda>-\log(1-c_A^*)>\log(1+c_A^*).
\]

Hence

\[
\boxed{
|\Lambda_{A,n}|>
\log\left(1+\frac{3}{4X_A}\right)
}
\]

and therefore

\[
\boxed{
\operatorname{dist}(y_A,\mathbb Z)
>
\frac{1}{2\log\varphi}
\log\left(1+\frac{3}{4X_A}\right)
}.
\]

This is an explicit global distance-to-integers lower bound.

### Relation to Baker–Matveev theory

The form \(\Lambda_{A,n}\) is a linear form in logarithms of the positive algebraic numbers

\[
\varphi,\quad 2,\quad 5
\]

inside \(K=\mathbb Q(\sqrt5)\), of degree \(D=2\), with integer coefficients

\[
b_1=2n+3,
\qquad
b_2=-m_A,
\qquad
b_3=-1.
\]

Their absolute logarithmic heights are

\[
h(\varphi)=\frac12\log\varphi,
\qquad
h(2)=\log2,
\qquad
h(5)=\log5.
\]

Thus an explicit Matveev theorem is applicable once nonvanishing is known. It is not load-bearing here. The exact integer-gap lemma gives a stronger problem-specific bound immediately and removes the need for a huge asymptotic cutoff.

## 9. Bound comparison and finite remainder

The correction satisfies

\[
|\rho_n|<\frac14,
\]

whereas the nonzero threshold separation satisfies

\[
|L_n-X_A|>\frac34.
\]

Therefore the required dominance inequality holds for all \(A,n\ge0\):

\[
|L_n-X_A|>\frac34>\frac14>|\rho_n|.
\]

The global cutoff is consequently

\[
\boxed{A_0=0}.
\]

There is no finite remainder range below \(A_0\). The finite-remainder certificate is vacuous. The package nevertheless performs independent exact-integer spot checks for \(A=0,\ldots,12\).

The first threshold is

\[
A=0,
\qquad
X_0=2^{12}=4096,
\]

with

\[
P_8=F_9F_{10}=34\cdot55=1870<4096,
\]

and

\[
P_9=F_{10}F_{11}=55\cdot89=4895>4096.
\]

Thus \(T_0=9=\lceil y_0\rceil\).

## 10. Consequences for the carry model

Because the bridge is global, the affine threshold sequence is no longer merely a finite-range proxy for the exact QBL Fibonacci threshold sequence. Every theorem that depends only on the identity \(T_A=\lceil y_A\rceil\) now transfers to all depths, subject to its own stated hypotheses.

This closes only the threshold bridge. It does not infer any Orthad chart matrix, transition pairing, gauge class, holonomy, finite quadratic module, or Weil projection from operation counts. The current Orthad law explicitly separates primitive custody from the attached dual-chart reader and leaves the all-depth chart and transfer recurrences as independent obligations.

```text
GAUGE/FQM MAP FROM d_A=±1: NOT YET DERIVED
```

Specific-orbit equidistribution remains a separate question. The global ceiling identity does not prove that the particular affine orbit is generic for Lebesgue measure.

```text
SPECIFIC-ORBIT EQUIDISTRIBUTION: NOT PROVED
```

## 11. Status partition

### Proved abstractly

- The exact Binet product identity.
- The signed correction bound \(|\rho_n|<1/4\).
- The power-of-two equality obstruction.
- Uniform sign transfer between \(P_n-X_A\) and \(L_n-X_A\).
- The explicit logarithmic and distance-to-integers lower bounds.
- The global identity \(T_A=\lceil y_A\rceil\) for every \(A\ge0\).

### Certified finitely

- Exact integer threshold checks for \(A=0,\ldots,12\).
- Hash-addressed large-integer witnesses for the bracketing products.
- Reproducible notebook, scripts, traces, and manifest.

### Observed

- No observational claim is needed for the global theorem.
- Previously observed finite orbit statistics remain evidence for, not proof of, specific-orbit equidistribution.

### Open

```text
SPECIFIC-ORBIT EQUIDISTRIBUTION: NOT PROVED
GAUGE/FQM MAP FROM d_A=±1: NOT YET DERIVED
```

## 12. Final status

```text
GLOBAL T_A=ceil(y_A) BRIDGE: PROVED
GAUGE/FQM MAP FROM d_A=±1: NOT YET DERIVED
```
