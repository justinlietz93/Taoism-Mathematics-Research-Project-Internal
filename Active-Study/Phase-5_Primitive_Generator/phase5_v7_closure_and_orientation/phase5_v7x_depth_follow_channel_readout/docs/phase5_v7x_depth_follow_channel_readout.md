# Phase 5 v7x: Depth 3-6 Follow Channel-Field Readout

## Verdict

`DEPTH_3_6_FOLLOW_CHANNEL_FIELD_READOUT_SUPPORTED_WITH_LAP2_NEGATION_ON_TESTED_RETAINED_LENS_MODEL`

The tested Follow readout now has explicit depth records for depths 3, 4, 5, and 6.

## Readout discipline

The retained state carries:

```text
word/history support
cursor n
post-L seat
parity latch
lap orientation
```

The retained state does not carry:

```text
Shadow Residual scalar coefficient
mock-theta scalar cargo
external q-series object
```

External comparison is terminal and channel-based only.

## Channel field

For each support term `n` with `gcd(n,6)=1`, the readout emits:

```text
support channel: gcd(n,6)=1
magnitude channel: |n|
sign channel: post-L chi12 seat sign
expansion width: depth-dependent n_max
inter-term phase: delta post-L seat mod 12
exponent spacing: delta n^2/24
```

## Lap behavior

```text
lap 1: sign(n)
lap 2: -sign(n)
```

This closes the recovered target:

```text
lap-2 = -lap-1 behavior
```

for the tested depth 3-6 Follow records.
