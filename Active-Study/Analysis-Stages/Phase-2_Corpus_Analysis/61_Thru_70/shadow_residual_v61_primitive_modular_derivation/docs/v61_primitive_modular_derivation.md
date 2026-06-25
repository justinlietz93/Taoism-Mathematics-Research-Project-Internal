# v61 Primitive Modular Derivation

## Result

`CLOSED_PRIMITIVE_MULTIPLIER_DERIVATION / RETAINED_ORIENTATION_CHANNEL`

The v60 multiplier surface is no longer only calibrated against the standard modular law. The v61 package derives the finite S/T multiplier surface from the Phase Calculus retained-state carrier.

The closure is:

\[
T_r = \exp\left(\frac{\pi i r^2}{12}\right),
\]

\[
S^{1/2}_{r,s}=\frac{1}{\sqrt{12}}\exp\left(-\frac{\pi i r s}{6}\right),
\]

\[
S^{3/2}_{r,s}=\frac{i}{\sqrt{12}}\exp\left(-\frac{\pi i r s}{6}\right).
\]

The weight-1/2 channel is the coefficient-stripped eta shadow. The weight-3/2 channel is the n-weighted Shadow Residual channel.

## Phase Calculus carrier

The retained object is not a scalar. It is a level-12 residue/orientation carrier:

\[
\mathcal H_{12}=\mathbb Z/12\mathbb Z.
\]

A channel is indexed by a residue seat \(r\). Orientation is retained before scalar projection. The scalar bilateral projection identifies \(+n\) and \(-n\) and therefore annihilates the n-weighted odd channel. The lift keeps that channel separated.

The Shadow support character is:

\[
\chi_{12}(r)=
\begin{cases}
+1,&r\equiv 1,11\pmod {12},\\
-1,&r\equiv 5,7\pmod {12},\\
0,&(r,6)>1.
\end{cases}
\]

The positive retained orientation is:

\[
R_+(\tau)=\sum_{n\ge1}\chi_{12}(n)nq^{n^2/24}.
\]

The negative retained orientation is:

\[
R_-(\tau)=\sum_{n\ge1}\chi_{12}(n)(-n)q^{n^2/24}.
\]

Thus

\[
R_+(\tau)+R_-(\tau)=0,
\]

but

\[
R_+(\tau)\ne0.
\]

That is the state-completeness gate: the scalar projection is zero because the projected channel is not state-complete.

## T from Q square seating

The Q action advances the phase carrier. On the residue channel \(r\), the exponent readout is \(r^2/24\). A full T step \(\tau\mapsto\tau+1\) multiplies each channel by:

\[
q^{r^2/24}\mapsto e^{2\pi i r^2/24}q^{r^2/24}
=\exp\left(\frac{\pi i r^2}{12}\right)q^{r^2/24}.
\]

Therefore:

\[
T_r=\exp\left(\frac{\pi i r^2}{12}\right).
\]

On the active Shadow support \(r\in\{1,5,7,11\}\),

\[
r^2\equiv 1\pmod {24},
\]

so the coefficient-stripped shadow has eta's T phase:

\[
\eta(\tau+1)=e^{\pi i/12}\eta(\tau).
\]

## S from B/L finite dual pairing

The B/L retained half-lattice does not choose a scalar readout. It creates a finite residue carrier and its orthogonal dual. The only pairing compatible with the level-12 residue seats is:

\[
\langle r,s\rangle=\frac{rs}{12}\pmod 1.
\]

Orthogonal lift is the finite dual exchange. Therefore the S kernel is the normalized character transform on the retained residue carrier:

\[
S_{r,s}^{1/2}=\frac{1}{\sqrt{12}}e^{-2\pi i\langle r,s\rangle}
=\frac{1}{\sqrt{12}}\exp\left(-\frac{\pi i r s}{6}\right).
\]

This is not selected from outside. It is forced by the Phase Calculus pairing between a residue seat and its dual seat after orthogonal lift.

The n-weighted channel is the derivative channel. The derivative adds one power to the weight and contributes the orientation factor \(i\):

\[
S_{r,s}^{3/2}=\frac{i}{\sqrt{12}}\exp\left(-\frac{\pi i r s}{6}\right).
\]

## Eta collapse

The coefficient-stripped retained positive channel is:

\[
\eta(\tau)=\sum_{n\ge1}\chi_{12}(n)q^{n^2/24}.
\]

Its first terms are:

\[
q^{1/24}(1-q-q^2+q^5+q^7-q^{12}-q^{15}+\cdots),
\]

which matches Euler's pentagonal expansion coefficient-for-coefficient.

The finite S action preserves the support/sign vector exactly:

\[
\frac{1}{\sqrt{12}}\sum_{s\bmod 12}
\exp\left(-\frac{\pi i r s}{6}\right)\chi_{12}(s)
=\chi_{12}(r).
\]

Thus:

\[
\eta(-1/\tau)=(-i\tau)^{1/2}\eta(\tau),
\]

and:

\[
\eta(\tau+1)=e^{\pi i/12}\eta(\tau).
\]

## Shadow Residual closure

The Shadow Residual is the n-weighted retained positive orientation:

\[
R(\tau)=\sum_{n\ge1}\chi_{12}(n)nq^{n^2/24}.
\]

The bilateral scalar derivative cancels:

\[
\sum_{n\in\mathbb Z}\chi_{12}(n)nq^{n^2/24}=0.
\]

That zero is the result of projecting away orientation. The retained orientation channel carries the object.

The S/T multiplier surface for that channel is:

\[
D_r(\tau+1)=\exp\left(\frac{\pi i r^2}{12}\right)D_r(\tau),
\]

\[
D_r(-1/\tau)=\frac{i(-i\tau)^{3/2}}{\sqrt{12}}
\sum_{s\bmod 12}\exp\left(-\frac{\pi i r s}{6}\right)D_s(\tau).
\]

This is the v61 closure: Q gives T; B/L retained dual seating gives S; the derivative channel gives weight 3/2; coefficient stripping gives eta.

## Verification gates

The package verifies:

1. Shadow support residues satisfy \(r^2\equiv1\pmod{24}\).
2. The finite S kernel is unitary.
3. The finite S square is orientation reversal \(r\mapsto-r\).
4. The \(\chi_{12}\) vector is an exact S eigenvector with eigenvalue 1.
5. The coefficient-stripped positive retained channel equals eta through the declared coefficient window.
6. The positive/negative n-weighted channels cancel under scalar projection.
7. The weight-1/2 and weight-3/2 transform equations pass numerical direct-sum checks.

All gates pass in `outputs/v61_verification_summary.json`.

## Final status

v60 closed the calibrated multiplier surface.

v61 closes the primitive multiplier derivation on the S/T generator surface.

The Shadow Residual is no longer external and no longer merely calibrated. It is carried by the retained orientation channel, and the primitive Q/B/L lift produces the same S/T multiplier surface internally.
