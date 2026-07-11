# Phase 5 v8a Protocol Definitions

## Retained event types

```text
Q_a:
  rotate/phase-update chart a

B_a:
  refine chart/corridor a

L_a:
  latch/lift from a to successor host

O_ab:
  overlap lens transition between charts a and b

R_a:
  terminal readout from chart a
```

## Support rule

Each event carries read/write/birth/edge tokens. Legal independence is defined only by token non-conflict.

## Confluence gate

Adjacent independent swaps must preserve:

```text
Foata normal form
retained compiler signature
transition cocycle class
```

## Cocycle gate

For every triangle `(a,b,c)`:

```text
T_ab + T_bc + T_ca = 0 mod 12
```

## Gauge gate

Local frame changes may alter coordinate edge values but must preserve cycle residuals.

## Negative controls

```text
mutated cocycle edge
illegal same-axis latch swap
terminal R retained mutation
birth-edge conflict
```
