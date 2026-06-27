# Phase 5 v7o: Contact/Latch Boundary Extension

## Objective

Determine whether the finite Orthad QGT object `H = M + iJ` is state-complete for boundary latch histories.

## Result

It is not. A finite contact-like coordinate is required for tested histories where the same bilinear coupling projection is reached by different latch paths.

## Definitions

For each pair `(i,j)`, let `c_ij` be the product-module coupling projection.

For each latch event on pair `(i,j)`:

```text
dc_ij = native latch impulse
p_ij  = pair-local latch clock
dz_ij = p_ij * dc_ij
alpha = dz_ij - p_ij dc_ij
```

The contact-extended retained boundary object is:

```text
K(h) = (M(h), J(h), Z(h), N_latch(h))
```

where `Z` stores the contact/latch coordinate.

## Necessity witness

There exist histories with identical `C` and therefore identical projected `J/M` coupling, but different `Z`.

```text
same_C_path_A:
  impulses [1, 5]
  C = 6
  Z = 1*1 + 2*5 = 11

same_C_path_B:
  impulses [5, 1]
  C = 6
  Z = 1*5 + 2*1 = 7
```

The same raw coupling tensor cannot distinguish these retained boundary paths.

## Interpretation

The contact coordinate is not decorative. It records boundary latch path data erased by bilinear projection.

## Boundary

This is a finite contact analogue. It supports a contact/latch extension as necessary for tested retained histories. It does not prove the full continuum CF02 contact branch.
