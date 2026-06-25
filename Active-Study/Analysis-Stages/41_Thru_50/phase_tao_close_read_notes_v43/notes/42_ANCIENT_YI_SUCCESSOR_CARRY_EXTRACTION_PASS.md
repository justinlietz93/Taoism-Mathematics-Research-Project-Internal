# 42. Ancient Yi successor/carry extraction and corrected Orthad normalization pass

## Purpose

Continue from the bridge-control document and the corrected carried-walk artifact by extracting the actual operational convention visible in the Ancient Yi octal tables.

This pass focuses on:

```text
retained carrier
-> digit/readout convention
-> successor/carry rule
-> finite place-domain completion
-> lifted place-domain opening
-> Orthad/corrected-walk normalization
```

## Key new finding: the Yi octal table is least-significant-place first

The rendered Ancient Yi examples do not use ordinary modern left-to-right octal notation. They display place values in least-significant-first order.

Extracted examples from the table pages:

```text
(10)  = 1*8^0 + 0*8^1 = 1
(67)  = 6*8^0 + 7*8^1 = 62
(77)  = 7*8^0 + 7*8^1 = 63
(001) = 0*8^0 + 0*8^1 + 1*8^2 = 64
(677) = 6*8^0 + 7*8^1 + 7*8^2 = 510
(777) = 7*8^0 + 7*8^1 + 7*8^2 = 511
(0001)= 0*8^0 + 0*8^1 + 0*8^2 + 1*8^3 = 512
(7777)= 7*8^0 + 7*8^1 + 7*8^2 + 7*8^3 = 4095
```

Interpretation:

```text
The carrier is not the scalar decimal number.
The carrier is an ordered place-symbol state.
The scalar is a readout after an order convention has been chosen.
```

This is directly useful for Orthad readout/custody comparison because it gives a clean non-Phase case where the same retained symbol object depends on a readout convention before becoming a scalar.

## Successor/carry rule extracted as operational model

State:

```text
(d0, d1, ..., d{k-1}), each di in {0,...,7}
```

Readout:

```text
value = Σ_i di * 8^i
```

Internal successor:

```text
increment d0;
if di overflows 7, reset di=0 and carry to d{i+1}.
```

Domain completion:

```text
all current k digits are 7.
```

Lift / new domain:

```text
77   -> 001
777  -> 0001
7777 -> 00001
```

This is a strong operational L/carry bridge because completion of the current finite place-domain does not remain inside the same domain. It opens a higher place-domain.

## Comparison to corrected Orthad carried walk

Corrected Orthad reference:

```text
each lap/domain: (BQ)^6 L
depth 6: ((BQ)^6 L)^6
B continues after every L
L carries q and theta
rank grows by exactly one per L
Orthad reads after the emitted walk exists
Shadow Residual remains external to the lift
```

Normalized comparison:

| Functional role | Ancient Yi octal-place table | Corrected Orthad carried walk |
|---|---|---|
| retained carrier | ordered line/place-symbol state | Ξ̂ plus accrued primitive word |
| local successor | increment/carry over ordered digit positions | BQ custody tick inside lap/domain |
| finite domain | fixed k-place octal carrier | six BQ positions per lap/domain |
| completion event | all k digits reach 7 | sixth BQ pair completes lap/domain |
| lift/carry | append new high place to the right | L carries q and θ, rank grows by one |
| readout | binary/octal/decimal projection | Orthad channel/lens readout |
| scalar status | terminal readout | terminal projection/external comparison |

## Strongest bridge status after this pass

```text
Ancient Yi retained carrier/readout:
  STRONG_OPERATIONAL_BRIDGE

Ancient Yi finite place-domain completion -> lift/carry:
  STRONG_OPERATIONAL_BRIDGE

Ancient Yi successor/carry as B-like refinement:
  STRONG_OPERATIONAL_CANDIDATE
  stronger than before because the internal successor rule is now explicit,
  but not exact Phase B because sort(v,u+v) is not extracted here.

Ancient Yi line-order/digit-order convention:
  PARTIALLY RESOLVED
  octal digit order is least-significant-first in the displayed formula examples.
  line-symbol-to-digit convention still requires table extraction/translation.
```

## Important nuance

Do not over-shrink the bridge by asking whether the Yi table literally contains `B(u,v)=sort(v,u+v)`. The operational question is broader:

```text
Does a retained finite carrier admit a successor/refinement rule?
Does that rule determine lawful continuation from the current state?
Does completion/blockage force a higher-place domain?
Does scalar readout happen only after the retained carrier is interpreted?
```

For these questions, the Yi table is now a strong operational bridge.

## New artifacts

```text
ancient_yi_64_lsd_first_successor_table.csv
ancient_yi_place_domain_carry_model.csv
ancient_yi_successor_carry_spec.json
```

## Remaining blockers

```text
1. Full machine-readable extraction of all 64 line-symbol rows.
2. Mapping of each line-symbol pattern to the displayed octal digits.
3. Confirmation of line order: lower-line first, upper-line first, or table-specific convention.
4. Whether the Yi table is only counting succession or also a situation/divination transformation grammar.
5. Whether a nontrivial B-like refinement law exists beyond ordinary digit successor/carry.
6. Latest Phase selector/floor source from HDD.
7. Dongyuan/Ceyuan formula-state graph for external B/refinement comparison.
```

## Current decision

```text
The Ancient Yi bridge is stronger after this pass.
The digit-order convention itself behaves like a readout/custody issue.
The octal successor/carry law is a concrete finite-state operational mechanism.
The lift/carry bridge is now high-confidence at the operational level.
The exact Phase B bridge remains open, not weakened.
```
