# 59 — Wilhelm exhaustive line semantic automata pass

## Status

`v53` external research pass.

This pass closes the previous optional blocker:

```text
exhaustive semantic audit of all 384 Wilhelm line readings
```

The result is not a proof that Wilhelm/I Ching is Phase Calculus. It is a stronger external operational bridge because the corpus can be represented as a retained-state line-event automaton.

## 1. Automata normalization

```text
state set:      64 retained six-line carriers
alphabet:       selected line position 1..6
events:         64 x 6 = 384 line-event emissions
transition:     flip selected retained line under explicit line-order convention
readout:        Wilhelm line text/commentary and derived semantic category flags
```

The state-completeness result is strict:

```text
hexagram ordinal alone: not state-complete
hexagram name alone:    not state-complete
line text alone:        not state-complete
semantic flags alone:   not state-complete
carrier + selected line + line-order convention: minimum graph-transition state
```

## 2. New files

| File | Purpose |
|---|---|
| `wilhelm_384_line_semantic_flags_v53.csv` | all 384 line readings parsed into operational category flags |
| `wilhelm_line_position_semantic_profile_v53.csv` | line-position category totals and means |
| `wilhelm_line_semantic_zscore_profile_v53.csv` | line-position z-scores by category |
| `wilhelm_line_transition_semantic_edge_deltas_v53.csv` | semantic deltas across single-line transition graph |
| `wilhelm_state_completeness_gate_matrix_v53.csv` | state-completeness pass/fail matrix |
| `wilhelm_semantic_automata_spec_v53.json` | reusable automata normal form |
| `wilhelm_semantic_automata_summary_v53.json` | compact machine-readable summary |

## 3. Line-position semantic maxima

| Category | Max line | Hit count |
|---|---:|---:|
| `latent_waiting` | 1 | 44 |
| `emergence_manifestation` | 1 | 33 |
| `admissible_action` | 2 | 263 |
| `danger_risk` | 3 | 113 |
| `no_blame_repair` | 1 | 26 |
| `favorable_success` | 5 | 71 |
| `transition_choice` | 3 | 19 |
| `boundary_excess` | 6 | 28 |
| `return_withdrawal` | 4 | 45 |
| `relation_affinity` | 5 | 43 |
| `obstruction_blockage` | 2 | 10 |
| `carry_lift_rechart` | 6 | 25 |
| `invariant_custody` | 5 | 57 |
| `readout_oracle` | 2 | 14 |

## 4. Main bridge finding

The Wilhelm line corpus does not behave like a pure scalar/ordinal table. It is better treated as:

```text
retained six-line carrier
-> selected line event
-> transition target under retained-carrier convention
-> emitted line-readout channel
```

That is directly relevant to the current bridge method:

```text
carrier first;
event second;
readout third;
scalar/semantic interpretation last.
```

## 5. Revealing line-ladder pattern

The semantic profile supports a position-sensitive ladder:

```text
line 1: latent / hidden / waiting / premature-action control
line 2: emergence / field / relational accessibility
line 3: danger / transition / instability / no-blame repair
line 4: choice / crossing / approach to boundary
line 5: central expression / favorable action / high-function readout
line 6: boundary / excess / return-cycle / completion-warning
```

This does not identify the six lines with QBL seats. It gives an external operational analogue for the idea that a fixed finite carrier has position-dependent event semantics.

## 6. Projection-loss result

The following are terminal projections, not the carried object:

```text
hexagram number
hexagram name
binary scalar
line text
semantic category flags
```

The carried object for the audited transition graph is:

```text
six-line carrier + selected line + line-order convention
```

For semantic readout, the emitted text/commentary is a boundary projection over that event.

## 7. Bridge status update

```text
Retained carrier/readout:
  STRONG_OPERATIONAL_BRIDGE

Admissible selected-line event:
  STRONG_OPERATIONAL_BRIDGE

B-like refinement:
  STRONG_OPERATIONAL_CANDIDATE / NOT_EXHAUSTED

L/cycle/boundary line-position evidence:
  STRONG_EXTERNAL_CANDIDATE / NOT IDENTITY PROOF

Projection-loss/state-completeness:
  STRONG_CONFIRMED
```

## 8. Progress effect

```text
Internal Research: 98.8%
External Research: 98.0%
Overall: 98.4%
```

The remaining external blockers are now narrower:

```text
Ancient Yi full translation and exact line-order proof;
Liu2022 QSL/current/connectivity data;
optional full MFE/Pencil build tests.
```
