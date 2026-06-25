# Phase 3 v5 Result Card

```text
PHASE 3 v5: Wilhelm Six-Line Phase Ladder
STATUS: SIX_LINE_LADDER_CONFIRMED_TRANSITION_CUSTODY_CLOSED
GLOBAL_PASS: true
```

## Proved here

```text
Wilhelm line dynamics normalizes to a retained six-line carrier automaton.

Minimum transition state:
  six-line carrier + selected line + line-order convention

Projection-loss result:
  ordinal/name/text/category/carrier-only projections do not determine next transition.
```

## Hard numbers

```text
states: 64
directed line events: 384
undirected edges: 192
out-degree per state: 6
in-degree per state: 6
Hamming distance per event: 1
line action involution: true
```

## Falsification gates

```text
F1: event count differs from 64 x 6
F2: any line event is not a single retained-line flip
F3: ordinal/name/text/category projection determines all 384 transitions
F4: nonidentity line permutation preserves all transitions
F5: full semantic reparse flattens the line-position ladder
```
