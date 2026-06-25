# 43 — Orthad/Yi Operational Homology Pass

## Status

Continued from the corrected Phase/Orthad crosswalk and the carried-walk depth-6 artifact.

This pass does **not** claim identity between Ancient Yi and Phase Calculus. It preserves the strongest operational bridge under the corrected canon:

```text
retained carrier/state
-> admissible transition
-> finite/capacity/cycle completion
-> carry/lift/new domain
-> boundary readout/projection
-> scalar terminal output
```

## Input controls used

- Bridge-control document: `PHASE_TAO_v34_RELEVANCE_TO_ORTHAD_CANON.md`
- Corrected Phase/Orthad reference: `orthad_corrected_carried_walk_depth6_20260620T113500.zip`
- Existing extracted Ancient Yi files:
  - `ancient_yi_64_lsd_first_successor_table.csv`
  - `ancient_yi_place_domain_carry_model.csv`
  - `ancient_yi_successor_carry_spec.json`

## New artifacts from this pass

- `orthad_yi_transition_homology_table.csv`
- `orthad_yi_domain_completion_comparison.csv`
- `orthad_yi_operational_bridge_spec_v2.json`

## Main finding

The bridge is now sharper than “octal carry resembles L.”

The normalized form is:

```text
Ancient Yi octal-place carrier:
  state: d=(d0,...,d5), di in 0..7
  readout: value=sum_i d_i*8^i
  successor: increment d0, propagate carry upward
  completion: d=(7,...,7), value=8^k-1
  lift: reset lower places and append a new high place
        77 -> 001
        777 -> 0001

Corrected Orthad:
  state: Xi_hat=(A,q,theta,kappa,c)+word
  lap/domain: (BQ)^6 L
  depth 6: ((BQ)^6 L)^6
  B: q=(u,v)->sort(v,u+v), anchor updates
  Q: theta += pi/2
  L: q and theta carry; rank grows by one
  readout: Orthad reads boundary channel after emitted word exists
```

## Strongest bridge status

| Layer | Status | Reason |
|---|---:|---|
| Retained carrier before scalar readout | Strong | Ancient Yi symbol tuple is not identical to decimal readout; Orthad lens/channel is not scalar output. |
| Finite domain completion | Strong | Ancient Yi reaches `8^k-1`; Orthad completes a six-seat lap/domain. |
| Carry/lift/new domain | Strong | Ancient Yi opens a new high place; Orthad opens rank+1 active axis after L. |
| Projection/readout | Strong | Ancient Yi supports binary/octal/decimal readouts; Orthad supports channel/scalar terminal projections. |
| B/refinement | Open / not exhausted | Ancient Yi successor/carry is operationally B-like, but no external law matching `q -> sort(v,u+v)` or position-governed floor-anchor has been extracted. |

## Corrected comparison matrix

Do not compare by labels. Compare by operational role:

| Question | Ancient Yi | Corrected Orthad |
|---|---|---|
| What is retained? | line/place-symbol carrier | `Xi_hat` plus primitive word |
| What advances? | successor/carry over place tuple | BQ custody ticks |
| What completes? | finite k-place domain at `8^k-1` | six-seat lap/domain after `(BQ)^6` |
| What opens? | new high place | new rank/active axis after L |
| What is read out? | binary/octal/decimal scalar view | Orthad channel/lens, then terminal scalar/external comparison |
| What must not be confused with state? | decimal value | scalar Shadow comparison / visible projection |

## New precision on the Ancient Yi bridge

The Ancient Yi table is stronger as an **Orthad custody/readout analogue** than as an exact B proof.

It gives:

```text
carrier first
position convention second
numeric readout third
```

and:

```text
finite place-domain completion
-> no same-domain successor without overflow
-> carry/lift to new place domain
```

This directly supports the corrected L/carry comparison.

## Objective weak point

The B/refinement bridge remains open for an objective reason:

```text
Ancient Yi successor/carry currently gives base-8 place refinement.
Corrected Phase B gives Fibonacci/Farey balanced refinement q=(u,v)->sort(v,u+v).
```

This is not a negative result. It means the next comparison target must look for external mechanics where:

```text
current position/state governs whether refinement can continue;
refinement narrows or concentrates a burden;
blocked refinement forces continuation/lift.
```

Best remaining candidates:

- Dongyuan Jiurong / Ceyuan Haijing contact-state formula families.
- Liu 2022 QSL/HFT current-sheet threshold and topology transition data.
- Ancient Yi rule-governed situation transitions, if the text contains more than counting tables.

## Updated conclusion

Ancient Yi is now a strong operational bridge for:

```text
retained carrier
multiple readouts
finite domain completion
carry/lift/new domain
Orthad-style readout discipline
```

It remains an open candidate for exact B-like refinement. The bridge should be preserved, not narrowed, while the missing B-governance evidence is pursued.
