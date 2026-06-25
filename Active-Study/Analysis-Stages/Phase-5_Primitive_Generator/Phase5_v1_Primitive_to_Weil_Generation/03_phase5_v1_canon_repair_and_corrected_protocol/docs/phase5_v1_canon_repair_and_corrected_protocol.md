# Phase 5 v1 Canon Repair: Contamination Site, Corrected Law, Corrected Test

## Claim first

Phase 5 v1 is open because the reference macro grammar and shadow-carry law were contaminated: the old macro grammar relabeled primitives as macros, collided with Weil generator names, and the old shadow law banned the orientation pairing required to test the Fourier generator.

## Source defect 1: degenerate macro grammar

The inherited reference definition

```text
{R,S,T}, R = Q∘B = B∘Q, S = Q, T = L
```

is suspended as macro grammar.

It may survive only as deprecated executable selector shorthand inside its original balanced-window branch context:

```text
PC_REF  := Q∘B = B∘Q
PC_HOLD := Q
PC_LFT  := L
```

These are not earned macros. Two of three are bare primitives. The true macro layer is:

```text
Macro_QBL := earned iterative QBL words read through Orthad
```

Status:

```text
Macro_QBL = UNDEFINED_PENDING_DERIVATION
```

## Source defect 2: symbol collision

The names `S` and `T` collided with classical Weil generator names. That collision is permanently banned.

From now on:

```text
Weil_F_N := finite Fourier generator
Weil_G_N := quadratic Gauss diagonal generator
```

No PC operator may be compared to a Weil generator because a letter matches. The join must be structural.

## Source defect 3: over-broad Shadow law

The old no-shadow-in-lift law is split:

```text
scalar mock-theta coefficient/readout: external terminal projection
orientation-residue vector: retained state, carriable
cross-orientation coupling: retained state, carriable
```

This repairs the contradiction where the law correctly excluded scalar coefficients but incorrectly banned the retained orientation block required to test a Fourier kernel.

## Lens correction

The old diagonal lens remains valid for axis inheritance:

```text
axis stack = diagonal inherit-and-extend latch structure
```

It is not valid as a forced diagonal in the orientation index.

Corrected Orthad lens shape:

```text
Ω = AxisDiag ⊕ OrientationBlock
```

where `OrientationBlock` may contain dense retained pairings between orientation residues.

## Corrected generation test

For each level `N`:

```text
W_G_N ∈ {Q,B,L}*
W_F_N ∈ {Q,B,L}*
Ω_G_N = OrthadRead(W_G_N)
Ω_F_N = OrthadRead(W_F_N)

compare Ω_G_N to Weil_G_N only after readout
compare Ω_F_N to Weil_F_N only after readout
```

Required targets:

```text
Weil_G_N[r,s] = δ_rs exp(π i r²/N)
Weil_F_N[r,s] = N^(-1/2) exp(-2π i r s/N)
```

## Corrected verdict

No corrected boundary has been found.

The corrected comparison is blocked at the explicit-word and terminal-projection gate:

```text
W_G_N: UNDEFINED_PENDING_DERIVATION
W_F_N: UNDEFINED_PENDING_DERIVATION
P_N^Orthad: UNDEFINED_PENDING_DERIVATION
```

The admitted-pairing control reproduces both Weil targets with zero residual, but that is not a generation proof because the pairing has not yet been derived as an Orthad readout of explicit QBL words.

## Standing canon rule

Before testing whether `A` generates `B`:

1. Write the exact first-principles definition of `A`.
2. Write the exact independent definition of `B`.
3. Confirm no symbol means two objects.
4. Confirm `A` is not a primitive relabel.
5. Derive from QBL and Orthad first.
6. Compare to external targets only after the derived object exists on its own.

