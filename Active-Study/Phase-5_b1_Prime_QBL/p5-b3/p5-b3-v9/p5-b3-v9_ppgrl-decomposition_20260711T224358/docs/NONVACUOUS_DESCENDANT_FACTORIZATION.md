# Non-Vacuous Descendant Factorization

## Weakest typed interface

For each retained prefix `t`, use only:

- an ambient argument object `H_t`;
- chart argument objects `C_{+,t}` and `C_{-,t}`;
- state-fixed placements
  \[
  \iota_{+,t}:C_{+,t}\to H_t,
  \qquad
  \iota_{-,t}:C_{-,t}\to H_t;
  \]
- a codomain object `K_t`;
- a primary two-slot evaluator
  \[
  P_t:H_t\times H_t\to K_t.
  \]

No addition, scalar multiplication, adjoint, duality, symmetry, or matrix representation is assumed.

For `a,b in {+,-}`, define the descendant by the pointwise restriction identity

\[
D_{ab,t}(x,y)
=
P_t\bigl(\iota_{a,t}(x),\iota_{b,t}(y)\bigr).
\]

Equivalently,

\[
D_{ab,t}=\rho_t(P_t,\iota_{a,t},\iota_{b,t}),
\]

where the realization-fixed constructor `rho_t` is uniquely characterized by the displayed pointwise identity.

## Non-smuggling requirements

A restriction constructor is non-vacuous only when all of the following hold.

1. **Typed placement:** its inputs are the primary object and the two structural placements.
2. **No target input:** it receives no independently selected descendant value.
3. **Realization fixedness:** its rule is fixed by the realization, not regenerated from a desired target at each state.
4. **Pointwise fidelity:** every descendant evaluation equals the primary evaluation on placed arguments.
5. **Extensionality:** identical `P`, codomain transport, and placement data produce identical descendants.
6. **Placed sensitivity:** when two primary objects differ on the images of the same placements, their descendants differ there.

Pointwise fidelity implies extensionality and placed sensitivity.

## Why this is weaker than an adjoint formula

The formula requires only precomposition in two ordered slots. It does not type the repeated star in `iota_a^* P iota_b`. A represented realization may later express the same restriction using a dual, transpose, conjugate transpose, or another contravariant mechanism. Those are representations of this dependency only after their carrier and action laws are derived.

## QBL status

```text
NON-VACUOUS RESTRICTION FACTORIZATION INTERFACE: PROVED
EXACT QBL ARGUMENT OBJECTS: NOT YET DERIVED
EXACT QBL PLACEMENT MAPS: NOT YET DERIVED
EXACT QBL RESTRICTION CONSTRUCTOR REALIZATION: NOT YET DERIVED
```
