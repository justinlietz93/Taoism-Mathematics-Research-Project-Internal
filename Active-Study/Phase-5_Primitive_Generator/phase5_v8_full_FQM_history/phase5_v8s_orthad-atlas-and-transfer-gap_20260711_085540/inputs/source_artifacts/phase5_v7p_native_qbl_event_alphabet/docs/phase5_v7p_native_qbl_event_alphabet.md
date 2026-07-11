# Phase 5 v7p: Native QBL Event Alphabet and Support-Derived Independence

## Objective

Define a QBL-native event alphabet and an independence relation derived from retained support, not from hand-labeled admissibility.

## Event alphabet

Primitive events:

- `Q_a`: quarter continuation on retained axis `a`.
- `B_a`: balanced denominator-pair refinement on retained axis `a`.
- `L_a`: latch/host-lift boundary event that freezes axis `a` and births axis `a+1`.

Derived inspection events:

- `O_{a,b}`: overlap-pair event extracted from retained axis supports and shared edge support.
- `R_a`: terminal projection/read event with no retained mutation.

## Support law

Each event is assigned read tokens, write tokens, required born axes, and created born axes. Two adjacent events are legally swappable iff no write/read or write/write conflict exists and neither event creates an axis required by the other.

This makes independence support-derived:

```text
independent(e_i,e_j)
  iff retained supports are disjoint
  and birth causality is preserved
```

## Why this is necessary

Earlier passes used bounded admissible event families. That was enough to test trace-cocycle normal forms, finite QGT/J-M splitting, and contact/latch memory, but it left one attack surface: event independence could be accused of being hand-labeled.

v7p removes that weakness by deriving legal commutation from native support tokens.

## Results

All trace cases, legal rewrite checks, coupling/contact gates, and negative controls passed in the finite test model. Illegal swaps were rejected before they could masquerade as equivalences.

## Frontier

The remaining work is to connect this support model to the full Orthad lens compiler and to define the full event-to-transition assignment `T` used by the trace-cocycle layer.
