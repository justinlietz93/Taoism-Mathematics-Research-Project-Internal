# QBL Global Exact-Threshold Bridge

**Branch:** `p5-b2-v3`  
**Status:** accepted global theorem with corrected proof-companion and deterministic-delivery layer  
**Current Orthad authority:** `QBL_PRIMITIVE_CUSTODY_AND_ORTHAD_LAW_v2.md`  
**Older canonical ledgers:** provenance only

## 1. Theorem

Let

\[
F_0=0,\qquad F_1=1,\qquad F_{k+2}=F_{k+1}+F_k,
\]

\[
P_n:=F_{n+1}F_{n+2},
\qquad
m_A:=12(2^{A+1}-1),
\qquad
X_A:=2^{m_A},
\]

and

\[
T_A:=\min\{n\in\mathbb N_0:P_n\ge X_A\}.
\]

Define

\[
\varphi:=\frac{1+\sqrt5}{2},
\qquad
y_A:=\frac{m_A\log2+\log5}{2\log\varphi}-\frac32.
\]

Then, for every integer \(A\ge0\),

\[
\boxed{T_A=\lceil y_A\rceil}.
\]

The proof is global. It uses an exact Binet decomposition, a uniform additive correction below \(1/4\), an exact obstruction to equality with the power-of-two threshold, and the resulting nonzero integer gap. No finite cutoff and no external linear-forms theorem are load-bearing.

```text
GLOBAL T_A=ceil(y_A) BRIDGE: PROVED
SPECIFIC-ORBIT EQUIDISTRIBUTION: NOT PROVED
GAUGE/FQM MAP FROM d_A=±1: NOT YET DERIVED
```

## 2. Exact Binet product identity

Set

\[
\psi:=\frac{1-\sqrt5}{2}=-\varphi^{-1}.
\]

Binet's formula is

\[
F_k=\frac{\varphi^k-\psi^k}{\sqrt5}.
\]

Therefore

\[
\begin{aligned}
P_n
&=\frac15(\varphi^{n+1}-\psi^{n+1})(\varphi^{n+2}-\psi^{n+2})\\
&=\frac15\left(
\varphi^{2n+3}
-\varphi^{n+1}\psi^{n+2}
-\psi^{n+1}\varphi^{n+2}
+\psi^{2n+3}
\right).
\end{aligned}
\]

Because \(\psi=-\varphi^{-1}\),

\[
-\varphi^{n+1}\psi^{n+2}
-\psi^{n+1}\varphi^{n+2}
=(-1)^n(\varphi-\varphi^{-1})=(-1)^n,
\]

using \(\varphi-\varphi^{-1}=1\), and

\[
\psi^{2n+3}=-\varphi^{-(2n+3)}.
\]

Hence

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

This identity is exact for every \(n\ge0\).

## 3. Signed correction and the uniform bound

For even \(n\),

\[
0<\rho_n=\frac{1-\varphi^{-(2n+3)}}5<\frac15<\frac14.
\]

For odd \(n\ge1\), \(2n+3\ge5\), so

\[
|\rho_n|
=\frac{1+\varphi^{-(2n+3)}}5
\le \frac{1+\varphi^{-5}}5.
\]

Since

\[
\varphi^5=5\varphi+3>4,
\]

we have \(\varphi^{-5}<1/4\), and therefore

\[
\frac{1+\varphi^{-5}}5<\frac{1+1/4}{5}=\frac14.
\]

Thus, for every \(n\ge0\),

\[
\boxed{|\rho_n|<\frac14}.
\]

The sign is exact:

\[
\rho_n>0\text{ for even }n,
\qquad
\rho_n<0\text{ for odd }n.
\]

## 4. Exact power-of-two equality obstruction

Consecutive Fibonacci numbers are coprime:

\[
\gcd(F_{n+1},F_{n+2})=1.
\]

Suppose

\[
P_n=F_{n+1}F_{n+2}=2^m.
\]

Both factors must be powers of two. Since they are coprime, one factor must be \(1\). The only Fibonacci indices with value \(1\) are \(1\) and \(2\). Therefore the only indexed products \(P_n\) that are powers of two are

\[
P_0=F_1F_2=1,
\qquad
P_1=F_2F_3=2.
\]

For every \(A\ge0\),

\[
m_A\ge12,
\qquad
X_A\ge4096.
\]

Consequently,

\[
\boxed{P_n\ne X_A\quad(A,n\ge0)}.
\]

This is the required nonzero condition.

## 5. Integer-gap sign transfer

Fix \(A,n\ge0\). Both \(P_n\) and \(X_A\) are integers, and they are unequal. Hence

\[
|P_n-X_A|\ge1.
\]

Since \(P_n=L_n+\rho_n\),

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

Therefore

\[
\boxed{P_n>X_A\iff L_n>X_A}
\]

and

\[
\boxed{|L_n-X_A|>\frac34}.
\]

The direct integer-gap bound is problem-specific, direct, and sufficient. It removes the need to derive a Baker--Matveev cutoff for this theorem.

## 6. Nonintegrality of the affine threshold

By definition,

\[
L_n=X_A
\iff
\frac{\varphi^{2n+3}}5=2^{m_A}
\iff
n=y_A.
\]

Suppose \(y_A=n\in\mathbb Z\). Then \(L_n=X_A\), and therefore

\[
P_n-X_A=\rho_n.
\]

The left side is an integer, while \(|\rho_n|<1/4\). Thus the left side would have to be zero, contradicting \(P_n\ne X_A\). Hence

\[
\boxed{y_A\notin\mathbb Z\quad(A\ge0)}.
\]

## 7. Global ceiling reduction

The leading inequality is exactly

\[
\begin{aligned}
L_n>X_A
&\iff \frac{\varphi^{2n+3}}5>2^{m_A}\\
&\iff (2n+3)\log\varphi-\log5>m_A\log2\\
&\iff n>y_A.
\end{aligned}
\]

Since \(y_A\notin\mathbb Z\),

\[
n>y_A\iff n\ge\lceil y_A\rceil.
\]

The equality obstruction also gives \(P_n\ge X_A\iff P_n>X_A\). Combining all steps,

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

Thus

\[
\boxed{T_A=\lceil y_A\rceil\quad\text{for every }A\ge0}.
\]

The global cutoff is \(A_0=0\); there is no finite remainder below it.

## 8. Direct logarithmic distance bound

Define

\[
\Lambda_{A,n}:=(2n+3)\log\varphi-\log5-m_A\log2
=2\log\varphi\,(n-y_A).
\]

The nonintegrality result implies \(\Lambda_{A,n}\ne0\). Since

\[
\frac{L_n}{X_A}=e^{\Lambda_{A,n}}
\]

and \(|L_n-X_A|>3/4\),

\[
|e^{\Lambda_{A,n}}-1|>\frac{3}{4X_A}.
\]

Writing \(c_A^*:=3/(4X_A)\), both signs yield the direct and sufficient bound

\[
\boxed{
|\Lambda_{A,n}|>
\log\left(1+\frac{3}{4X_A}\right)
}.
\]

Therefore

\[
\boxed{
\operatorname{dist}(y_A,\mathbb Z)
>
\frac{1}{2\log\varphi}
\log\left(1+\frac{3}{4X_A}\right)
}.
\]

A general explicit theorem on linear forms in logarithms is applicable after nonvanishing is known, but it is not needed for the global bridge.

## 9. Proof-companion boundary

The computational companions are divided by logical strength.

### Universal proof obligations

The document proves:

1. the exact Binet identity;
2. the uniform signed correction bound;
3. the power-of-two equality obstruction;
4. the nonzero integer-gap lemma;
5. sign transfer and the \(3/4\) separation;
6. nonintegrality of \(y_A\);
7. the global ceiling theorem.

The derivation script encodes this dependency graph, checks the exact symbolic algebra and inequality margins, verifies that all theorem dependencies are present in both this document and the Lean theorem surface, and refuses to emit `PROVED` if a dependency is absent or inconsistent.

### Finite regression checks

The finite checks at \(A=0,\ldots,12\) and sampled Binet/correction checks test the implementation. They are not presented as proofs of universal statements.

### Lean status

The Lean source states the full theorem surface, including the Binet identity, correction, power-of-two obstruction, nonintegrality, and final bridge. Compilation is claimed only when a matching Lean/Mathlib environment actually succeeds.

```text
LEAN SOURCE PRESENT; COMPILATION NOT VERIFIED
```

## 10. Consequences and boundary

The global theorem transfers every result that depends only on the identity \(T_A=\lceil y_A\rceil\) from the affine model to the exact Fibonacci threshold sequence.

It does not infer an Orthad chart matrix, pairing recurrence, transfer recurrence, gauge value, holonomy, FQM class, or Weil projection from operation counts. The current Orthad law keeps those obligations separate.

```text
SPECIFIC-ORBIT EQUIDISTRIBUTION: NOT PROVED
GAUGE/FQM MAP FROM d_A=±1: NOT YET DERIVED
```

## 11. Status partition

### Proved abstractly

- Exact Binet product identity.
- Signed uniform correction bound \(|\rho_n|<1/4\).
- Exact power-of-two equality obstruction.
- Nonzero integer-gap sign transfer and \(3/4\) separation.
- Nonintegrality of \(y_A\).
- Direct logarithmic distance-to-integers bound.
- Global identity \(T_A=\lceil y_A\rceil\) for every \(A\ge0\).

### Certified finitely

- Exact integer threshold regressions for \(A=0,\ldots,12\).
- Deterministic package manifest and archive construction.
- Byte-identical archive rebuilding from two clean copies.

### Observed

- No observational claim is needed for the theorem.
- Existing finite orbit statistics remain evidence for, not proof of, specific-orbit equidistribution.

### Open

```text
SPECIFIC-ORBIT EQUIDISTRIBUTION: NOT PROVED
GAUGE/FQM MAP FROM d_A=±1: NOT YET DERIVED
```

## 12. Final status

```text
GLOBAL T_A=ceil(y_A) BRIDGE: PROVED
SPECIFIC-ORBIT EQUIDISTRIBUTION: NOT PROVED
GAUGE/FQM MAP FROM d_A=±1: NOT YET DERIVED
p5-b2 BRANCH STATUS: CLOSED
```
