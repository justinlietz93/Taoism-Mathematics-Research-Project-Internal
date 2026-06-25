# 45 — I Ching Wilhelm transition graph / line-position operational pass

## Purpose

Continue the external-corpus analysis using the corrected operational comparison rules:

```text
Do not require the external corpus to reproduce Phase-specific labels or one fixed canonical B origin path.
Compare retained carrier, admissible transition, local operation, finite/capacity completion, lift/re-chart, readout, and projection discipline.
```

This pass examines `code/iching-wilhelm-dataset-master`, especially:

```text
README.md
data/i-ching-basic.js
data/iching_wilhelm_translation.js
```

## New result

The Wilhelm dataset is not just a static 64-hexagram table. It exposes a retained six-line carrier with at least three operational structures:

```text
1. single-line mutation graph
2. opposite/complement involution
3. King Wen adjacent-pair operation law
```

This materially strengthens the Ancient Yi / Yijing bridge because it adds an explicit transition graph over the retained carrier.

---

## 1. Retained carrier

Each hexagram carries:

```text
hex number
hex glyph
Chinese name
English name
binary six-line carrier
od field
upper trigram / lower trigram data in the full translation file
six line-position readings
```

The binary carrier is not the scalar output. It is the retained line-symbol field from which multiple readouts can be made.

### Readout convention

For the Wilhelm dataset, the binary string behaves as:

```text
binary string = top-to-bottom line string
line 1       = bottom line
line 6       = top line
```

So a bottom-indexed line flip uses:

```text
bit_index = 6 - line_number
```

This matters for Orthad/Yi comparison because readout is convention-sensitive:

```text
same retained carrier
-> chosen line order convention
-> scalar / transition / trigram readout
```

---

## 2. Single-line mutation graph

I built the full single-line flip graph from the 64 retained carriers.

Output:

```text
iching_wilhelm_single_line_flip_graph.csv
```

Graph facts:

```text
nodes: 64 hexagrams
directed single-line transitions: 384
undirected single-line edges: 192
outdegree per node: 6
```

Interpretation:

```text
A hexagram is a retained six-line state.
Each of the six line positions is a local admissible mutation site.
Flipping one line moves to another retained hexagram.
```

This gives a concrete finite-state transition system:

```text
retained carrier
-> choose line position
-> local mutation
-> new retained carrier
-> line-specific readout
```

This is a stronger bridge than the earlier static 64-state observation.

---

## 3. `od` field is exact complement

I verified the dataset’s `od` field against bitwise complement of the six-line carrier.

Output:

```text
iching_wilhelm_transition_graph_summary.json
```

Result:

```text
od_field_matches_bitwise_complement: true
opposite pairs: 32
bad matches: 0
```

Operational interpretation:

```text
od is a global six-line involution:
  000111 -> 111000
  010101 -> 101010
  111111 -> 000000
```

Bridge use:

```text
This is a clean retained-carrier operation, not a scalar operation.
It helps separate complement from reversal, readout, successor, and lift.
```

---

## 4. King Wen adjacent-pair operation law

I tested all 32 adjacent pairs:

```text
(1,2), (3,4), ..., (63,64)
```

Output:

```text
iching_wilhelm_kingwen_pair_operations_v2.csv
```

Results:

```text
reverse only: 24 pairs
reverse + complement: 4 pairs
complement + reverse_then_complement: 4 pairs
other: 0 pairs
```

Meaning:

```text
Every King Wen adjacent pair is governed by a retained-carrier involution class.
No pair is arbitrary under this binary carrier.
```

This is a major operational bridge:

```text
retained six-line carrier
-> adjacent paired state
-> operation is determined by carrier geometry
```

The operational family is not plain binary successor. It is a structured pairing rule over the six-line carrier.

---

## 5. Line-position readings are local operation channels

The full translation file contains six line-position readings for each retained carrier.

Output:

```text
iching_wilhelm_key_line_dynamics.csv
iching_wilhelm_line_position_keyword_counts.csv
iching_wilhelm_line_position_keyword_examples.csv
iching_wilhelm_dynamic_keyword_hits.csv
```

Bridge interpretation:

```text
The six line positions are not interchangeable scalar bits.
Each line position has its own local reading / risk / transition logic.
```

This supports the operational comparison:

```text
Q/support-channel:
  six-position carrier with position-sensitive local channels

B/refinement:
  local line mutation graph over retained state; not Phase-B identity, but operational refinement candidate

L/carry/lift:
  line-position cycle, adjacent-pair involutions, and place-domain carry remain separate but compatible bridge layers

Orthad readout:
  retained state first; line-position readout afterward
```

---

## 6. Hexagram 1 gives a six-position cycle reading

The Wilhelm comments for hexagram 1 explicitly discuss six positions/steps and sequence through time. Its line texts also form a staged ascent:

```text
line 1: Hidden dragon. Do not act.
line 2: Dragon appearing in the field.
line 3: All day long ... creatively active. Danger. No blame.
line 4: Wavering flight over the depths. No blame.
line 5: Flying dragon in the heavens.
line 6: Arrogant dragon will have cause to repent.
```

Operational reading:

```text
line positions are phase/position channels;
advancing through positions changes admissibility and danger;
the top line represents overreach/excess rather than simple continuation.
```

This is relevant to the corrected Phase criterion:

```text
cycle completion / exhausted continuation
-> no lawful same-domain continuation without excess/repetition
-> re-chart/lift/new domain becomes meaningful
```

Do not overclaim this as literal QBL. Use it as operational support for six-position phase-channel comparison.

---

## 7. Bridge update

### Stronger than before

```text
Ancient Yi / Wilhelm I Ching now supplies:
  retained six-line carrier
  local six-position transition graph
  exact complement operation
  King Wen paired-state operation law
  line-position-specific readout channels
```

### Corrected bridge labels

```text
Q/support-channel:
  STRONG_OPERATIONAL_BRIDGE

B/refinement:
  STRONG_OPERATIONAL_CANDIDATE / NOT_EXHAUSTED
  because single-line mutation and carrier-governed pairing are real refinement/transition mechanisms
  but not yet mapped to current Phase B admissibility/floor mechanics

L/re-chart/lift:
  STRONG_OPERATIONAL_CANDIDATE
  from finite place-domain carry + cycle/excess/top-line semantics

Orthad readout:
  STRONG_OPERATIONAL_BRIDGE
  same retained carrier supports multiple non-equivalent readouts
```

---

## 8. Sticky research pathway: modular B arithmetic

User-provided correction preserved:

```text
Base-8 successor/carry may open a research path where B-like refinement can modularly switch arithmetic under a different retained carrier, if Ancient Yi fits.
```

This is not closed in this pass. It becomes a later test:

```text
Can B be generalized as a refinement operator schema over a retained carrier,
with the arithmetic law supplied by the active carrier domain?
```

Test frame:

| Domain | Retained state | Refinement arithmetic | Completion law | Lift event |
|---|---|---|---|---|
| Corrected Phase canonical origin | `(u,v)` pair | Farey/Fibonacci balanced refinement | Q/B saturation | L carries q/theta, rank+1 |
| Ancient Yi place carrier | octal digit tuple / six-line field | base-8 successor/carry and line mutation | `8^k-1` / six-line limits | higher-place domain / changed carrier |
| Candidate generalized B schema | domain-carried state | domain-specific refinement law | domain-specific excess/capacity | lift/re-chart/new domain |

---

## 9. New missing pieces

To resolve the B bridge further:

```text
1. Confirm whether Wilhelm line-change operation follows a fixed successor rule, divination rule, or only local mutation.
2. Determine whether King Wen pair law is sufficient as an operational transition law or only a pairing/readout convention.
3. Compare single-line mutation graph to corrected `(BQ)^6 L` lap structure.
4. Build a six-line/lap table:
     line 1..6 semantics
     bottom/top convention
     mutation target
     cycle/excess marker
5. Test whether Ancient Yi place-domain carry and six-line mutation are one joined system or two separate systems.
6. Keep modular-B arithmetic as a research pathway, not a present conclusion.
```

---

## 10. Corpus status update

Updated coverage:

```text
source/code/iching-wilhelm-dataset-master/data/i-ching-basic.js: 100%
source/code/iching-wilhelm-dataset-master/data/iching_wilhelm_translation.js: 90%
source/code/iching-wilhelm-dataset-master/README.md: 95%
```

The dataset is no longer just “read.” It now has extracted transition artifacts.
