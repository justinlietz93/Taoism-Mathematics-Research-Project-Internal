# Protocol Definitions

## Objects

```text
C(h): pairwise bilinear coupling projection
J(h): antisymmetric holonomy limb induced by C
M(h): symmetric gluing-cost Laplacian induced by |C|
Z(h): pair-local contact/latch coordinate
K(h): contact-extended retained object (M,J,Z,N)
```

## Finite contact law

For latch event `e` on pair `(i,j)`:

```text
p_e = pair-local latch count after admitting e
dc_e = latch coupling increment
dz_e = p_e * dc_e
alpha_e = dz_e - p_e * dc_e
```

Gate:

```text
alpha_e = 0 for every admitted latch event
```

## Legal rewrite law

Disjoint pair events commute. Same-pair latch events do not commute unless their latch impulses are equal or an explicit equivalence rule proves equality of contact signature.

## Contact necessity law

If two histories have the same `C` but different `Z`, raw `C` and finite `H=M+iJ` are not full retained boundary state.
