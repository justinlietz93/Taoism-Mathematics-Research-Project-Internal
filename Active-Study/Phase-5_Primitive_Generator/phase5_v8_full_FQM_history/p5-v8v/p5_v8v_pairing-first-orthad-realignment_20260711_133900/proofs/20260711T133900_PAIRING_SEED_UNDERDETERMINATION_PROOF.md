# Pairing Seed Underdetermination Proof

## Theorem

The primitive custody tuple and transition law do not determine a unique primary pairing seed unless an additional seed map is supplied.

## Proof

Let `H=Q` and consider bilinear forms

```text
P_1(x,y)=xy
P_2(x,y)=2xy.
```

They are distinct because

```text
P_1(1,1)=1
P_2(1,1)=2.
```

Let

```text
Xi_0=(0,(1,1),0,0,1,empty).
```

The custody laws for `B`, `Q`, and `L` mention only `A,q,theta,k,j,W`. They impose no equation on a pairing value. Therefore both `(Xi_0,P_1)` and `(Xi_0,P_2)` have the same custody projection and satisfy the same custody-only seed constraints.

Hence the custody tuple does not select a unique pairing seed. A map

```text
eta_P:(Xi_0,W_0,D_P)->P_0
```

or an equivalent axiom is necessary. QED.

## Boundary

This theorem is relative to the stated custody-only axioms. It does not prove that no omitted or future source can define `eta_P`.
