# 26 - Rigor correction: Liu 2022 bridge is not exhausted

Source corrected:

`Prospect-Leads/Liu_2022_ApJ_940_62.pdf`

Correction target:

`25_LIU_2022_DATA_CONSTRAINED_MHD_SQUEEZE_DRY.md`

## Hard correction

The previous classification used language like:

```text
Q-side: weak direct support
B-side: weak direct support
```

That wording is too final. It sounds like the comparison was exhausted and found weak. It was not.

Correct status:

```text
Q-side: DIRECT_MATCH_UNPROVEN; BRIDGE_OPEN
B-side: DIRECT_MATCH_UNPROVEN; BRIDGE_OPEN
L-side: TOPOLOGICAL_CUSTODY_BRIDGE_OPEN
Projection-side: STRONG_CONFIRMED
```

Do not use `weak` as a verdict unless the comparison class has been exhausted and a negative criterion is explicitly met.

## Correct distinction

The following remains true:

```text
Solar-physics Q = squashing factor / magnetic-connectivity diagnostic.
Primitive Phase Q = quarter-turn custody operation.
```

But that only blocks a **name-level conflation**. It does not exhaust structural comparison.

The right rule is:

```text
Name collision rejected.
Structural bridge still open.
```

## Why Liu 2022 may still matter to Q/B/L physics bridges

Liu 2022 contains real physics mechanisms that should not be thrown away because they do not map immediately to the current Phase notation.

### 1. Squashing-factor Q as channel/lens diagnostic bridge

Solar squashing-factor Q measures strong gradients in field-line mapping and highlights quasi-separatrix layers / high-Q footprints.

Possible bridge:

```text
retained magnetic connectivity
-> diagnostic field over boundary/support
-> projected ribbon/channel structure
```

This is not primitive Phase Q, but it may be relevant to:

```text
Orthad readout support channel
lens-projected boundary support
terminal projection from retained topology
```

Status:

```text
Q_NAME_MATCH_FALSE
Q_DIAGNOSTIC_BRIDGE_OPEN
```

### 2. HFT/null-point topology as boundary/lift candidate

Liu 2022's HFT/null-point system is not a pure coordinate re-chart. It is a physical topological transition structure.

Possible bridge:

```text
retained topology reaches unstable transition architecture
-> reconnection changes connectivity class
-> upper/lower structures separate
-> one channel promotes/erupts while another remains retained/stable
```

This could be relevant to:

```text
L as boundary event
active/latched separation
state-selective promotion
not-all-state-lifts
```

Status:

```text
PURE_RECHART_MATCH_FALSE
TOPOLOGICAL_LIFT_BRIDGE_OPEN
```

### 3. Reconnection as admissibility-change, not re-chart

Do not force reconnection into the Yin-Yang grid bucket. It belongs to a different bucket.

Current buckets:

```text
1. Pure re-chart:
   same state, different legal chart, invariants preserved.

2. Topological reconnection:
   connectivity changes under physical laws; retained field reorganizes.

3. Orthad latch/lift:
   active axis freezes, carried q remains, new active axis opens.
```

Liu 2022 belongs mainly to bucket 2, but bucket 2 may still be relevant to physics bridges if Phase Calculus has a real topological transition interpretation.

### 4. B-side bridge is not exhausted

Earlier note said no floor-anchor analogue. Corrected:

```text
No explicit B floor-anchor analogue has been identified yet.
This is not a negative proof.
```

Open B-related bridge questions:

```text
Does the retained magnetic topology contain a capacity/floor-like stability threshold?
Does decay index / torus instability act as a domain-specific admissibility bound?
Does reconnection start only after a local/topological condition exceeds a threshold?
Can the erupting/non-erupting mass-element split be read as admitted vs non-admitted promotion?
```

Status:

```text
B_FLOOR_ANCHOR_NOT_IDENTIFIED
B_THRESHOLD_BRIDGE_OPEN
```

### 5. Projection-side remains strong

This part is solid and should stay:

```text
retained 3D magnetic state first
-> synthetic AIA / observed channel projection afterward
```

The 94 Å / 304 Å distinction is important because the same retained evolution produces different terminal readouts depending on channel and line of sight.

## Corrected classification table

| Side | Previous wording | Corrected wording | Reason |
|---|---|---|---|
| Q | weak direct support | `DIRECT_MATCH_UNPROVEN; Q_DIAGNOSTIC_BRIDGE_OPEN` | Squashing-factor Q is not primitive Q, but it may be a readout/support-channel diagnostic. |
| B | weak direct support | `B_FLOOR_ANCHOR_NOT_IDENTIFIED; B_THRESHOLD_BRIDGE_OPEN` | No floor-anchor match found yet, but stability/decay-index/reconnection thresholds remain live. |
| L | medium support | `TOPOLOGICAL_CUSTODY_BRIDGE_OPEN` | Reconnection is not pure re-chart or Orthad latch, but active/retained separation is real. |
| Projection | strong | `STRONG_CONFIRMED` | Retained 3D state precedes synthetic/observed projection. |
| Code | medium-high | `BOUNDARY_CUSTODY_USEFUL; NOT_FULL_PHASE_MATCH` | Ghostzone/base-state handling is useful but not full QBL evidence. |

## Rigor rule added

For all future papers:

```text
Never downgrade to WEAK just because direct notation does not match.
Use:
  DIRECT_MATCH_UNPROVEN
  BRIDGE_OPEN
  NOT_YET_EXHAUSTED
unless an explicit negative test has been performed.
```

A paper is only `WEAK` after the relevant comparison axes have been named, checked, and found absent or contradictory.

## Updated research pressure

Return to Liu 2022 later with a bridge-specific pass:

```text
1. Extract the topology-transition thresholds:
   decay index, force-free quality, HFT/null structure, QSL/squashing-factor concentrations.

2. Compare thresholds to B/Q admissibility:
   local continuation, blocked transition, stability loss, promotion/non-promotion.

3. Compare active/lower split to latch/lift:
   what erupts, what remains, what changes connectivity, what remains anchored.

4. Compare squashing-factor Q to Orthad lens support channel:
   retained topology -> boundary diagnostic -> projected ribbon support.
```

