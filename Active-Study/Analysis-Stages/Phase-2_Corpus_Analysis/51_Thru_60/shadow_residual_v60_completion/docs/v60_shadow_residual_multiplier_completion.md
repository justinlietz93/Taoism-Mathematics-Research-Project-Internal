# v60 Shadow Residual Multiplier Completion

## Result

`CLOSED_MULTIPLIER_SURFACE / RETAINED_ORIENTATION_CHANNEL`

The v58 scalar obstruction stays correct. The stale verdict is removed.

The Shadow Residual does not close as a single scalar bilateral Jacobi derivative. It closes as the positive-orientation readout of an orientation-by-residue unary-theta derivative channel. The scalar bilateral projection is the zero projection. That is the state-completeness gate firing.

## Objects

Let

\[
\chi_{12}(n)=
\begin{cases}
+1,&n\equiv 1,11\pmod{12},\\
-1,&n\equiv 5,7\pmod{12},\\
0,&(n,6)>1.
\end{cases}
\]

Let \(q=e^{2\pi i\tau}\). The project Shadow Residual is

\[
R(\tau)=\sum_{n\ge 1}\chi_{12}(n)nq^{n^2/24}.
\]

The eta shadow candidate is

\[
\eta(\tau)=\sum_{n\ge 1}\chi_{12}(n)q^{n^2/24}.
\]

The two orientations are

\[
R_+(\tau)=\sum_{n\ge 1}\chi_{12}(n)nq^{n^2/24},
\qquad
R_-(\tau)=\sum_{n\ge 1}\chi_{12}(n)(-n)q^{n^2/24}.
\]

Therefore

\[
R_+(\tau)=R(\tau),\qquad R_-(\tau)=-R(\tau),\qquad R_+(\tau)+R_-(\tau)=0.
\]

The scalar projection is zero. The retained orientation projection is nonzero.

## Residue-vector parent

The closed finite multiplier object is the residue-vector unary-theta derivative parent. For residues \(r\in\mathbb Z/12\mathbb Z\), define

\[
\Theta_r(\tau)=\sum_{n\equiv r\;(12)}q^{n^2/24}
\]

and

\[
D_r(\tau)=\sum_{n\equiv r\;(12)}nq^{n^2/24}.
\]

The Shadow Residual is the positive-orientation half of the \(\chi_{12}\)-supported derivative channel:

\[
R(\tau)=\sum_{r\in\{1,5,7,11\}} \sum_{k\ge0}\chi_{12}(r)(12k+r)q^{(12k+r)^2/24}.
\]

The eta shadow is the corresponding coefficient-stripped half:

\[
\eta(\tau)=\sum_{r\in\{1,5,7,11\}} \sum_{k\ge0}\chi_{12}(r)q^{(12k+r)^2/24}.
\]

Equivalently, using the bilateral residue parent,

\[
\eta(\tau)=\frac12\sum_{r\in\mathbb Z/12\mathbb Z}\chi_{12}(r)\Theta_r(\tau).
\]

## T transformation

For both \(\Theta_r\) and \(D_r\),

\[
\Theta_r(\tau+1)=e^{\pi i r^2/12}\Theta_r(\tau),
\]

\[
D_r(\tau+1)=e^{\pi i r^2/12}D_r(\tau).
\]

On the support \(r\in\{1,5,7,11\}\), \(r^2\equiv1\pmod{24}\). Therefore the eta support vector has the eta T multiplier

\[
e^{\pi i/12}.
\]

## S transformation

Poisson/Jacobi transformation gives the residue-vector multiplier matrices:

\[
\Theta_r(-1/\tau)=\frac{(-i\tau)^{1/2}}{\sqrt{12}}
\sum_{s\bmod 12}e^{-\pi i rs/6}\Theta_s(\tau),
\]

\[
D_r(-1/\tau)=\frac{i(-i\tau)^{3/2}}{\sqrt{12}}
\sum_{s\bmod 12}e^{-\pi i rs/6}D_s(\tau).
\]

Thus the derivative residue vector has weight \(3/2\) and multiplier

\[
S^{(3/2)}_{r,s}=\frac{i}{\sqrt{12}}e^{-\pi i rs/6},
\qquad
T^{(3/2)}_{r,r}=e^{\pi i r^2/12}.
\]

The coefficient-stripped residue vector has weight \(1/2\) and multiplier

\[
S^{(1/2)}_{r,s}=\frac{1}{\sqrt{12}}e^{-\pi i rs/6},
\qquad
T^{(1/2)}_{r,r}=e^{\pi i r^2/12}.
\]

The \(\chi_{12}\) support vector

\[
\chi=(0,1,0,0,0,-1,0,-1,0,0,0,1)^T
\]

is an eigenvector of \(S^{(1/2)}\) with eigenvalue \(1\), and an eigenvector of \(T^{(1/2)}\) on support with eigenvalue \(e^{\pi i/12}\). This is exactly the eta multiplier surface:

\[
\eta(-1/\tau)=(-i\tau)^{1/2}\eta(\tau),
\qquad
\eta(\tau+1)=e^{\pi i/12}\eta(\tau).
\]

## Completion statement

The completed v60 statement is:

```text
Shadow Residual = retained positive-orientation component of the weight-3/2 unary-theta derivative channel.
Scalar bilateral projection = zero.
Eta = coefficient-stripped weight-1/2 shadow on the same support/sign channel.
The exact finite multiplier system is the residue-vector S/T system above.
```

## Verification gates

The package verifies:

1. `R_plus + R_minus = 0` through the tested support range.
2. `R_plus` is nonzero.
3. Removing the factor `n` from `R_plus` gives eta coefficient-for-coefficient through `q^(650+1/24)`.
4. The \(\chi_{12}\) eta vector has the eta S/T multipliers.
5. The residue-vector \(\Theta_r\) transformation satisfies the weight-1/2 S/T formulas numerically below `1e-45`.
6. The residue-vector derivative \(D_r\) transformation satisfies the weight-3/2 S/T formulas numerically below `1e-45`.

All gates pass in `outputs/v60_verification_summary.json`.
