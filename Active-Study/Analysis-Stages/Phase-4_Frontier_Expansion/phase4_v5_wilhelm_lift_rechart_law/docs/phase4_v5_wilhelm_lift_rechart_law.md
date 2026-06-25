# Phase 4 v5: Wilhelm Lift/Re-Chart Law

## Claim

Wilhelm line 6 closes as a same-carrier re-chart law:

```text
E_6(binary) = binary with the top bit toggled
             = (source_index - 1) xor 32, then +1 for one-based index
```

This law is exact over all 64 retained six-line carriers.

## Result

```text
STATUS: SAME_CARRIER_RECHART_LAW_CLOSED_NEW_DOMAIN_LIFT_REJECTED
GLOBAL_PASS: True
```

## What is proved

```text
1. Every carrier has exactly one line-6 event.
2. Every line-6 event changes exactly one retained line.
3. Line 6 is involutive.
4. Line 6 is exactly XOR 32 on zero-based carrier index.
5. Line 6 always crosses the lower/upper carrier hemisphere.
6. Line 6 remains inside the same 64-state carrier.
7. Boundary/excess/carry pressure is concentrated at line 6.
```

## Interpretation

Wilhelm line 6 is not ordinary commentary and not a generic selected-line flip only. It is the top-bit host-axis crossing of the six-line carrier.

The finite transition table does not contain a higher-domain lift event. It contains a same-carrier re-chart event whose semantic readout carries excess/completion/carry pressure.

That places Wilhelm precisely in the Phase 4 v2 classification:

```text
CARRIER_TRANSITION_BOUNDARY_NOT_FULL_B
```

It does not upgrade to full Modular-B because the finite Wilhelm table supplies no intrinsic progress/completion/new-domain lift operator.

## Law

For a zero-based six-bit carrier `x in {0,...,63}`:

```text
E_i(x) = x xor 2^(i-1)
E_6(x) = x xor 32
```

For one-based hexagram index:

```text
target_index = ((source_index - 1) xor 32) + 1
```

## Boundary closed

The earlier open target was:

```text
Find or derive the explicit post-line-6 lift/re-chart rule.
```

Phase 4 v5 closes it:

```text
The explicit rule is same-carrier top-bit re-chart, not new-domain lift.
```

## Falsification targets

See `outputs/phase4_v5_falsification_targets.csv`.
