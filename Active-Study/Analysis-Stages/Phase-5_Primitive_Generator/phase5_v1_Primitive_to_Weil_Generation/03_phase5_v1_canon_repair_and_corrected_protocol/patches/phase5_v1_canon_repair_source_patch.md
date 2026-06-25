# Canon Patch Instructions

## Replace degenerate macro wording

Replace:

```text
{R,S,T}, R = Q∘B = B∘Q, S = Q, T = L
```

with:

```text
Deprecated executable selector shorthands:
PC_REF  := Q∘B = B∘Q
PC_HOLD := Q
PC_LFT  := L

These are branch shorthands in the old balanced-window executable selector context, not the earned macro grammar.

Earned macro grammar:
Macro_QBL := iterative QBL words read through Orthad.
Status: UNDEFINED_PENDING_DERIVATION.
```

## Replace shadow carry law

Replace broad prohibition:

```text
No Shadow Residual / shadow object enters the lift.
```

with:

```text
No scalar mock-theta coefficient, entropy ratio, compression score, or terminal q-series coefficient is carried in the lift.
Retained orientation-residue vectors and retained cross-orientation pairings are native carried structure and may be present in the lifted state when earned by QBL custody.
```

## Replace lens restriction

Replace:

```text
The lens is diagonal one entry per axis.
```

with:

```text
The axis-inheritance part of the lens is diagonal. The orientation-index part is a retained block and may contain cross-orientation pairings. A diagonal orientation block is a degenerate subcase, not a law.
```
