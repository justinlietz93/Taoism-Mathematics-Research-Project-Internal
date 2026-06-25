# Phase 3 v5: Wilhelm Six-Line Phase Ladder

## Claim

Wilhelm line dynamics is a retained six-line carrier automaton with a selected-line event. The minimum transition-complete state is:

```text
S = (six-line carrier, selected line, line-order convention)
```

The terminal readout can be a hexagram ordinal, name, line text, or semantic category vector, but those readouts are not transition-complete unless they preserve the retained carrier and selected line.

## Finite transition law

Use a six-bit carrier written top-to-bottom. Bottom-indexed line `1` flips the rightmost bit; line `6` flips the leftmost bit.

```text
E(carrier, line_i) = carrier with bit i flipped
```

This gives exactly:

```text
64 states
6 selected-line events per state
384 directed events
192 undirected edges
Q6 hypercube transition graph
```

Each line event is an involution:

```text
E(E(carrier, i), i) = carrier
```

## Closed results

1. The transition graph has `384` directed events.
2. Every event changes Hamming distance exactly `1`.
3. Every selected-line action is locally reversible.
4. Carrier-only projection fails custody.
5. Selected-line-only projection fails custody.
6. Semantic-role-only projection fails custody.
7. Nonidentity line relabeling changes transition law.
8. Line-position semantics are non-flat.
9. Line 6 is the excess/completion/carry-pressure position.

## Projection-loss witnesses

The strongest witness is immediate:

```text
state_x = 111111:line1
state_y = 111111:line6
projection = carrier only = 111111
next_x = 111110
next_y = 011111
```

So the carrier alone is not transition-complete. The selected line is not a comment on the carrier; it is part of transition custody.

## Line ladder

The line-position ladder used in this package:

| Line | Operational reading |
|---:|---|
| 1 | admission / hidden origin |
| 2 | manifesting field |
| 3 | danger / transition stress |
| 4 | branch choice / boundary test |
| 5 | full expression / central authority |
| 6 | excess / completion / carry pressure |

The extracted maxima support the ladder: line 3 maximizes `danger_risk`, line 5 maximizes `favorable_success`, `relation_affinity`, and `invariant_custody`, and line 6 maximizes `boundary_excess` and `carry_lift_rechart`.

## General interpretation

The Wilhelm line corpus is not a flat scalar table. It is a retained transition system:

```text
carrier first
selected event second
transition target third
semantic/oracular readout fourth
```

This directly supports Phase 3's projection-loss theorem: bridge-admissible projections must preserve the retained state needed to determine the next admissible transition.

## Next target

The next target is source synchronization and proof execution prep:

```text
Phase 3 v6: Latest Phase Source Synchronization and Lean/Lake Execution Prep
```

The Wilhelm boundary target remains active:

```text
Find or derive the explicit post-line-6 lift/re-chart rule connecting upper-excess pressure to a new retained carrier domain.
```
