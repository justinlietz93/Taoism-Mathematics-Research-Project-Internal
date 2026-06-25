
# Shadow Residual Jacobi / Unary-Theta Proof Attempt v58

## Status

`STRONG ATTEMPT COMPLETE / NOT A SCALAR-CLOSURE PROOF`

This pass resolves the loose blocker into a precise theorem/obstruction.
The Shadow Residual cannot be honestly described as a direct scalar Jacobi-variable derivative of the even `χ12` eta theta without adding an orientation / half-lattice / vector-valued residue-class state.

## Definitions used in this pass

Let

```math
χ_{12}(n)=\begin{cases}
  +1,&n\equiv 1,11\pmod{12},\\
  -1,&n\equiv 5,7\pmod{12},\\
  0,&(n,6)>1.
\end{cases}
```

The eta theta identity is the bilateral even theta:

```math
η(τ)=\sum_{n\in\mathbb Z}χ_{12}(n)q^{n^2/24}.
```

The project Shadow Residual channel has been tracked as the positive/oriented series

```math
R(τ)=\sum_{n\ge 1}χ_{12}(n)nq^{n^2/24}.
```

## What closes

1. `R` is not `η`.
2. `R` is not `q∂_q η`; that derivative weights coefficients by `n^2/24`, not by `n`.
3. A Jacobi variable derivative naturally produces `n` weighting, but the direct bilateral derivative of the even `χ12` theta cancels:

```math
\left.\frac{1}{2π i}\partial_z \sum_{n\in\mathbb Z}χ_{12}(n)e^{2π i n z}q^{n^2/24}\right|_{z=0}
=\sum_{n\in\mathbb Z}χ_{12}(n)nq^{n^2/24}=0.
```

The zero is not a computational accident. It follows because `χ12(-n)=χ12(n)` while the extra factor `n` is odd.

## Main obstruction

A full bilateral scalar Jacobi derivative needs an odd coefficient rule `c(-r)=-c(r)` for residue classes. To match the positive Shadow coefficients, it would also need `c(r)=χ12(r)` for positive residues `r=1,5,7,11`.

This is impossible because:

```text
χ12(1)=χ12(11)=+1, but oddness requires c(11)=-c(1).
χ12(5)=χ12(7)=-1, but oddness requires c(7)=-c(5).
```

Therefore the positive Shadow Residual is not closed by a single scalar odd Dirichlet character derivative.

## Corrected bridge-level formulation

The honest closure target is:

```text
Shadow Residual
= oriented / positive-half / vector-valued unary theta derivative channel
not scalar eta and not q-derivative of eta.
```

At the Phase/Orthad bridge level this is useful, because it says the Shadow comparison requires an orientation/readout state. It is not loaded into the lifted object.

## Result

`Shadow Residual` remains external to Phase custody, but the reason is now sharper:

```text
Shadow uses a terminal oriented unary-theta readout channel.
It is compatible with Jacobi-variable derivative machinery only after retaining residue/orientation state.
A scalar readout without that retained state is not state-complete.
```
