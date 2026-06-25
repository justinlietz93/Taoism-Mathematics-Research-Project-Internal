# 47. Orthad/Yi/Wilhelm growth-law and modular-B pass

## Purpose

Make genuine progress beyond the prior correction that B should not be reduced to the canonical-origin Fibonacci corridor. This pass compares the corrected Orthad carried-walk growth law, Ancient Yi base-8 carry/lift, and Wilhelm line-position transition dynamics as operational systems.

## New artifacts

- `orthad_lap_growth_profile.csv`
- `orthad_yi_growth_law_comparison.csv`
- `wilhelm_line_ladder_evidence_zscores.csv`
- `wilhelm_line_ladder_category_maxima.csv`
- `b_modular_refinement_operator_schema_v2.csv`
- `pass47_summary.json`

## Corrected Orthad growth law extracted

From the corrected carried-walk artifact, each lap has word:

```text
BQBQBQBQBQBQL = (BQ)^6 L
```

Across depth 6, the lap endpoints are:

```text
lap 0: q (1,1)             -> (13,21),             uv=273
lap 1: q (13,21)           -> (233,377),           uv=87841
lap 2: q (233,377)         -> (4181,6765),         uv=28284465
lap 3: q (4181,6765)       -> (75025,121393),      uv=9107509825
lap 4: q (75025,121393)    -> (1346269,2178309),  uv=2932589879121
lap 5: q (1346269,2178309) -> (24157817,39088169), uv=944284833567073
```

The q endpoint indices advance by six Fibonacci/Farey B-steps per lap:

```text
(F7,F8), (F13,F14), (F19,F20), (F25,F26), (F31,F32), (F37,F38)
```

The uv growth ratio between completed laps tends toward \(arphi^{12}\):

```text
87841 / 273              ≈ 321.76
28284465 / 87841         ≈ 321.99
9107509825 / 28284465    ≈ 321.996
2932589879121 / 9107509825 ≈ 321.997
944284833567073 / 2932589879121 ≈ 321.997
```

This is a precise corrected-Phase reference point:

```text
six BQ seats per lap
-> B continues through L
-> q/theta carry
-> rank +1 per L
-> uv capacity grows multiplicatively by the carried refinement arithmetic
```

## Ancient Yi growth law extracted

Ancient Yi's LSD-first octal place-domain carry has a different arithmetic but the same operational stack:

```text
1-place: 7       -> 01        ; domain max 8^1 - 1 = 7
2-place: 77      -> 001       ; domain max 8^2 - 1 = 63
3-place: 777     -> 0001      ; domain max 8^3 - 1 = 511
4-place: 7777    -> 00001     ; domain max 8^4 - 1 = 4095
5-place: 77777   -> 000001    ; domain max 8^5 - 1 = 32767
6-place: 777777  -> 0000001   ; domain max 8^6 - 1 = 262143
```

This gives a strong operational L/carry bridge:

```text
finite admitted domain completes
-> same-domain successor would overflow/repeat
-> lower places reset
-> new high place/domain opens
-> scalar readout remains terminal
```

## The important comparison

The new result is not that Ancient Yi uses Phase B arithmetic. It does not.

The new result is that both systems show:

```text
retained carrier/state
-> successor/refinement inside finite/admitted domain
-> multiplicative capacity growth under repeated completion/lift
-> boundary/carry/lift after no same-domain continuation remains admissible
-> scalar/readout after carrier convention is fixed
```

The refinement arithmetic differs:

```text
Corrected Orthad:
  Fibonacci/Farey carried-pair refinement;
  six BQ seats per lap;
  uv growth ~ phi^12 per lap.

Ancient Yi:
  base-8 place-value carry;
  8^k-1 domain completion;
  capacity growth exactly x8 per place.
```

This supports the sticky research path:

```text
B-like refinement may be an operator schema whose arithmetic is selected by carrier/domain.
```

## Wilhelm line ladder evidence strengthened

Using the Wilhelm line text/comment data, line positions are not flat binary bits. They show a position-sensitive operational ladder.

Category maxima by line:

```text
hidden/admission:          line 1
manifestation/visibility:  line 2
transition/danger:         line 3
branch/boundary:           line 2, with line 4 as boundary-role candidate
central expression:        line 5
threshold/excess:          line 6
return/cycle:              line 6
carry/lift/promotion:      line 6
constraint/invariant:      line 1
projection/readout:        line 2
```

Most relevant result:

```text
line 6 has the strongest threshold/excess, return/cycle, and carry/lift signal.
line 3 has the strongest danger/transition signal.
line 1 has the strongest hidden/admission and invariant signal.
```

This is not a proof of QBL. It is operational evidence that the six-line carrier encodes a phase ladder with different admissible meanings by line position.

## Modular-B operator family matrix v2

The new matrix separates arithmetic identity from operational homology:

```text
Phase canonical B:
  carried pair q=(u,v), successor q -> sort(v,u+v), arbitrary seeds allowed.

Ancient Yi base-8 carry:
  retained digit tuple, successor/carry, arbitrary k-place state allowed.

Wilhelm single-line mutation:
  retained six-line carrier, arbitrary node and selected line mutation.

King Wen pair transforms:
  retained carrier with reverse/complement pair law, not numeric successor.

Dongyuan/Ceyuan:
  admitted geometric position selects legal formula family; transition graph still missing.
```

## Updated understanding

The overall research picture has sharpened:

```text
Phase Calculus is not being compared by labels.
It is being tested as a primitive discrete framework that may normalize multiple external systems by function:

retained state
-> admissible operation
-> refinement/transition
-> completion/blockage/threshold
-> carry/lift/re-chart
-> boundary readout
-> scalar only as terminal projection
```

The latest revealing finding is that corrected Orthad and Ancient Yi both have explicit multiplicative capacity growth under completion/lift, but with different refinement arithmetic. That difference is not a bridge failure. It points to a modular-B research program.

## Objective remaining blockers

1. Latest Phase selector/floor source from the HDD.
2. Full Ancient Yi table translation and line-order convention.
3. Formal modular-B tests over arbitrary seeds and base-N/place/refinement families.
4. Dongyuan/Ceyuan formula-state graph for position-governed non-place-value refinement.
5. Liu 2022 data for QSL/current/reconnection/topology timing.

## Progress percentage update

Current corpus completion is approximately:

```text
paper/resource first-pass coverage: ~94%
code/data bridge coverage: ~78%
overall project research pass: ~89%
```

This is not final proof status. It is close-read / bridge-prospecting completion status.
