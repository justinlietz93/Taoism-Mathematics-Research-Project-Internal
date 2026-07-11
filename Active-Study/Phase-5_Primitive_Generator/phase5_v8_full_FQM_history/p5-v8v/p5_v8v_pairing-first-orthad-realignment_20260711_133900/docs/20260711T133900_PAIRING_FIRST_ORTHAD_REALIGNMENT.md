# p5_v8v Pairing-First Orthad Realignment

## Result

The pairing-first dependency order is recovered, but the exact primary pairing is not yet derivable from the supplied authority and historical corpus.

```text
FIRST TRUE GAP:
    PRIMARY PAIRING TYPE, SEED, AND PER-LETTER MUTATION

NATIVE SUCCESSOR ON Z/12Z:
    DOWNSTREAM COORDINATE QUESTION

ORTHAD EXISTS FROM FIRST PRIMITIVE TICK:
    ARCHITECTURAL LAW

PRIMITIVE CUSTODY STATE:
    Xi_t

FULLY RETAINED LIFTED STATE:
    Xi_hat_t

ORTHAD:
    ⌞Xi_hat_t⌝

EXACT PRIMARY PAIRING TYPE:
    NOT_YET_DERIVED

EXACT PRIMARY PAIRING SEED:
    NOT_YET_DERIVED

EXACT PRIMARY PAIRING RECURRENCE:
    NOT_YET_DERIVED

EXACT CHART MAPS:
    NOT_YET_DERIVED

EXACT DIRECTED TRANSFERS:
    NOT_YET_DERIVED

QBL_TO_AFFINE FACTOR MAP:
    NOT_YET_DERIVED

MHD_ORTHAD_READINESS:
    NOT_READY
```

## Strategic choice

The successor-first branch is retired as the generative path. A cyclic shift on a chosen finite surface can be a valid downstream coordinate operator, but it does not create the primary pairing, chart restrictions, or directed transfers. The strongest dependency order supported by the current authority is:

```text
primitive custody Xi_t
-> pairing type datum
-> pairing seed P_0
-> B/Q/L pairing mutations
-> chart embeddings
-> chart restrictions and directed transfers
-> fully retained lifted state Xi_hat_t
-> Orthad wrapper ⌞Xi_hat_t⌝
-> terminal projection after halt
```

The exact pairing type datum is the first missing object. It must identify at least:

```text
D_P = (K, H_0, duality-or-involution, argument variance, symmetry law)
```

Without `D_P`, the notation `P_t`, `iota^* P_t iota`, `orthogonal`, `rank(P_t)`, and the block adjoint `C_t*` do not have one exact algebraic meaning.

## What the sources force about P_t

The authority forces these structural facts:

1. `P_t` is primary. It is not assembled from independently seeded chart matrices.
2. `P_t` is retained and mutates at every primitive tick.
3. The two chart restrictions and the two directed transfers must all be induced from `P_t` and chart maps.
4. `B` and `Q` preserve the architectural pairing rank.
5. `L` retains the old block, latches the completed active axis, appends one new orthogonal active axis, and raises the architectural rank by one.
6. `P_t` is not the Bloch sphere, `Z/12Z`, one chart matrix, a terminal character, an imported Weil operator, or a finished FQM form.

These constraints define an interface, not an exact type.

## Why the type is still open

The local descendant

```text
a_t = exp(i theta_t)/(u_t v_t)
```

is not sufficient to distinguish the following realizations:

```text
complex bilinear form
complex sesquilinear form without a fixed Hermitian law
operator-valued pairing with the same scalar component
general morphism H_t -> D(H_t) in a category with duality
quadratic object whose polarization supplies a later pairing
```

The historical finite tensor `H=M+iJ` is a Hermitian overlap reconstruction built from sealed overlap/coupling histories. It is a useful downstream clue, but it is not a clean `P_0` seed and does not provide the per-tick `B/Q/L` recurrence. The historical scalar cochain `T_ab=lens(b)/lens(a)` is also only a constrained transition descendant. It is not the mixed block induced from one primary pairing. The finished FQM quadratic form is downstream of gauge and overlap construction, so it cannot be imported as `P_0`.

## Abstract seed underdetermination

Fix a one-dimensional rational module. Two bilinear forms are

```text
P_1(x,y) = x y
P_2(x,y) = 2 x y.
```

They are distinct because `P_1(1,1)=1` and `P_2(1,1)=2`. The custody tuple

```text
Xi_0 = (0,(1,1),0,0,1,empty)
```

contains no equation selecting either form. Therefore custody alone cannot determine the pairing seed. A seed map is required:

```text
eta_P : (Xi_0, W_0, D_P) -> P_0.
```

This is an abstract nonuniqueness proof under the current custody-only axioms. It is not a claim that no future source can supply `eta_P`.

## B mutation

The clean custody mutation is exact:

```text
(u,v) -> (v,u+v)
```

with phase, domain, and position indices unchanged. The licensed local shorthand changes from

```text
exp(i theta)/(u v)
```

to

```text
exp(i theta)/(v(u+v)).
```

This does not determine the full pairing mutation. The missing map is:

```text
B_pairing : (P_t, Xi_t, Xi_{t+1}, W_{t+1}) -> P_{t+1}.
```

## Q mutation

The clean custody mutation is exact:

```text
theta -> theta + pi/2
k -> k+1
j -> j+1.
```

The licensed local shorthand multiplies by `i`, while its denominator is retained. This does not determine the full pairing mutation. The missing map is:

```text
Q_pairing : (P_t, Xi_t, Xi_{t+1}, W_{t+1}) -> P_{t+1}.
```

## L extension

The custody action is completely certified:

```text
A -> A+1
q carried
phase carried
k -> 0
j -> j_start(A+1).
```

The architectural pairing obligation is:

```text
retain old block
latch completed active axis
append one new orthogonal active axis
architectural rank 1 -> 2 at the first L.
```

The schematic block is

```text
P_{t+1} = [ P_t   C_t   ]
          [ C_t*  p_new ].
```

If a future exact pairing type interprets orthogonality as vanishing mixed pairing, then a compatible basis will have `C_t=0` at the instant of birth. This is a conditional formal consequence, not an emitted matrix and not yet a derived theorem. The new-axis datum `p_new` is still not forced. The missing map is:

```text
L_pairing : (P_t, Xi_t, Xi_{t+1}, W_{t+1}) -> P_{t+1}.
```

## Charts and transfers

The intended equations are retained only as typing obligations:

```text
Omega_plus  = iota_plus*  P_t iota_plus
Omega_minus = iota_minus* P_t iota_minus
T_plus_to_minus = iota_minus* P_t iota_plus
T_minus_to_plus = iota_plus*  P_t iota_minus.
```

No chart module, embedding, overlap domain, restriction matrix, or mixed transfer matrix is emitted because `P_t` and the chart maps are not derived.

## Canonical custody trace

The state self-selects:

```text
BQQBBBQBQBBQBBL
```

and certifies:

```text
floor pair:             (55,89)
floor product:          4895
Q steps:                5
phase at boundary:      5*pi/2
phase modulo 2*pi:      pi/2
complex phase witness:  i
immediately after L:    A=1, pair=(55,89), phase_quarters=5, k=0, j=7
first next-domain B:    (55,89) -> (89,144)
```

The Domain-0 local active-axis shorthand is `i/4895`. It is not promoted to a primary-pairing or chart entry.

## Z/12Z disposition

`Z/12Z` is supported as a finite doubled phase/orientation carrier and as the finite shadow skeleton used by the downstream `chi_12` result. It retains six local positions and two orientation hands. It discards the exact pair, unbounded word, full phase-quarter count, primary pairing, chart maps, and transfer data.

Because `{B,Q,L}*` is infinite and `Z/12Z` is finite, no map into `Z/12Z` can retain every exact word injectively. It is not the fully retained lifted state.

## Affine boundary

```text
AFFINE_GLOBAL_THRESHOLD_BRIDGE: PROVED
QBL_TO_AFFINE_FACTOR_MAP: NOT_YET_DERIVED
INTERNAL_ORTHAD_SEED_FROM_AFFINE_MAP: NOT_LICENSED
```

The possible future source object for an affine factor remains open:

```text
Xi_hat_A -> (E_A,c_A)
```

or

```text
⌞Xi_hat_A⌝ -> (E_A,c_A).
```

## MHD boundary

The external data intake is not an Orthad implementation. MHD use remains blocked by the missing pairing recurrence, chart maps, directed transfers, overlap domain, route-consistency law, vector and tensor transformation laws, units/grid verification, and field-valued channels.

## Claim boundary

No pairing matrix, chart matrix, transfer matrix, overlap residual, cocycle residual, terminal projection, gauge quotient, FQM object, Weil operator, Bloch state, character transport, or MHD field result is emitted in this package.
