# v62 — General Shadow Correspondence Push

## Closed starting point

The χ12 Shadow Residual instance is closed:

\[
R_{12}(\tau)=\sum_{n\ge 1}\chi_{12}(n)nq^{n^2/24}.
\]

It is the positive-orientation readout of the retained level-12 state. Its scalar bilateral projection is zero. Its coefficient-stripped shadow is

\[
G_{12}(\tau)=\sum_{n\ge 1}\chi_{12}(n)q^{n^2/24}=\eta(\tau).
\]

The level-12 S/T surface is derived from the retained residue/orientation carrier.

## Load-bearing structure

For a unary theta carrier with \(m\ge 1\), set

\[
A_m=\mathbb Z/(2m)\mathbb Z,\qquad q_r(\tau)=q^{r^2/(4m)}.
\]

The retained residue vector has components

\[
\Theta^{(0)}_{m,r}(\tau)=\sum_{n\equiv r\!\!\!\pmod{2m}}q^{n^2/(4m)}
\]

and derivative/orientation components

\[
\Theta^{(1)}_{m,r}(\tau)=\sum_{n\equiv r\!\!\!\pmod{2m}}nq^{n^2/(4m)}.
\]

The primitive multiplier surface is

\[
T_r=\exp\left(\frac{\pi i r^2}{2m}\right),
\]

\[
S_{r,s}=\frac{1}{\sqrt{2m}}\exp\left(-\frac{\pi i rs}{m}\right).
\]

The \(n\)-weight contributes the weight lift from \(1/2\) to \(3/2\).

## General versus χ12-specific

| Feature | Status |
|---|---|
| two orientations \(+n,-n\) | general |
| even coefficient rule \(a(-r)=a(r)\) | general condition for n-weighted scalar cancellation |
| coefficient-stripped \(n^0\) theta channel | general lower-weight shadow carrier |
| \(n\)-weight derivative channel | general weight-raising retained-orientation channel |
| finite residue carrier \(A_m\) | general unary theta carrier |
| \(T_r=\exp(\pi i r^2/(2m))\) | general |
| \(S_{r,s}=(2m)^{-1/2}\exp(-\pi irs/m)\) | general |
| \(\chi_{12}\) support \(\{1,5,7,11\}\) | χ12-specific |
| \(\chi_{12}\) gives \(\eta\) coefficient-for-coefficient | χ12-specific |
| \(\chi_{12}\) scalar channel is T-eigenclosed | χ12-specific stronger closure |

## Second worked case: level 8 / χ8

Define

\[
\chi_8(n)=
\begin{cases}
1,&n\equiv 1,7\pmod 8,\\
-1,&n\equiv 3,5\pmod 8,\\
0,&n\equiv 0,2,4,6\pmod 8.
\end{cases}
\]

The second retained positive-orientation readout is

\[
R_8(\tau)=\sum_{n\ge 1}\chi_8(n)nq^{n^2/16}.
\]

The coefficient-stripped shadow channel is

\[
G_8(\tau)=\sum_{n\ge 1}\chi_8(n)q^{n^2/16}.
\]

The bilateral derivative channel cancels:

\[
\sum_{n\in\mathbb Z}\chi_8(n)nq^{n^2/16}=0.
\]

The retained positive half does not cancel:

\[
R_8(\tau)=q^{1/16}-3q^{9/16}-5q^{25/16}+7q^{49/16}+9q^{81/16}-\cdots.
\]

The retained carrier is \(A_4=\mathbb Z/8\mathbb Z\). Its primitive multiplier values are

\[
T_r=\exp(\pi i r^2/8),
\]

\[
S_{r,s}=8^{-1/2}\exp(-2\pi irs/8).
\]

## Decisive boundary discovered

The χ8 scalar compression is not T-stable.

Let

\[
\chi_8=[0,1,0,-1,0,-1,0,1]
\]

and let

\[
\psi_{\mathrm{odd}}=[0,1,0,1,0,1,0,1].
\]

Then

\[
S\chi_8=\chi_8,
\]

but

\[
T\chi_8=e^{\pi i/8}\psi_{\mathrm{odd}},
\]

and

\[
T\psi_{\mathrm{odd}}=e^{\pi i/8}\chi_8.
\]

So the case closes on the retained residue carrier, not on a one-dimensional scalar character quotient.

This is the general lesson: the correspondence is vector-valued at the retained-state level. The χ12 case has an additional scalar-eigenchannel simplification because all supported residues satisfy \(r^2\equiv 1\pmod{24}\).

## General conjecture

For unary false-theta/mock-shadow channels carried by a finite quadratic module \(A_m=\mathbb Z/(2m)\mathbb Z\) with even orientation coefficient vector \(a(-r)=a(r)\), the shadow map is the Phase Calculus projection-loss gate in the modular setting.

The retained positive-orientation channel gives the false/mock object. The symmetric scalar projection forgets the orientation channel. The coefficient-stripped lower-weight theta is the modular shadow that survives the projection.

## Falsifier

A counterexample is any unary false-theta/mock-shadow pair with:

1. an even orientation coefficient vector,
2. a declared finite quadratic module,
3. known S/T multiplier,
4. known lower-weight shadow,

for which the multiplier cannot be recovered from

\[
T_r=\exp(\pi i r^2/(2m))
\]

and

\[
S_{r,s}=(2m)^{-1/2}\exp(-\pi irs/m),
\]

or for which the known shadow is not the coefficient-stripped symmetric projection of the same retained state.

## Result

The second case works. The scalar-compressed quotient breaks exactly where the retained-state theory predicts it should: T needs the full residue carrier. That is not a failure of the mechanism. It identifies the correct general class as vector-valued retained residue/orientation channels.
