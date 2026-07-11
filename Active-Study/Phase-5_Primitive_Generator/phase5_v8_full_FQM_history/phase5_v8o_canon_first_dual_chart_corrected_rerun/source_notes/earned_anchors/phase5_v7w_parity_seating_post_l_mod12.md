# Phase 5 v7w: Parity Seating / Post-L Mod-12 Reverification

## Objective

Recover and close the earlier target:

```text
parity seating across 12 from the lens matrix parity latch
post-L mod-12 sign/readout separation from n=7
```

## Definitions

The pre-L carrier sees only a mod-6 seat:

```text
s6(n) = n mod 6
```

The L event adds a retained parity latch from the lens orientation:

```text
pL(n) = floor((n mod 12)/6)
εL(n) = (-1)^pL(n)
```

The post-L seat is reconstructed from retained data:

```text
s12(n) = s6(n) + 6*pL(n)
```

or equivalently:

```text
s12(n) = s6(n) + 3*(1 - εL(n))
```

The Shadow Residual support character is tested as:

```text
χ12(n) = +1 for n ≡ 1,11 mod 12
χ12(n) = -1 for n ≡ 5,7 mod 12
χ12(n) = 0 otherwise
```

## Result

The mod-6 carrier cannot define χ12, because the same pre-L seat has contradictory lifts:

```text
1 ≡ 7 mod 6, but χ12(1)=+1 and χ12(7)=-1
5 ≡ 11 mod 6, but χ12(5)=-1 and χ12(11)=+1
```

The post-L retained latch reconstructs all twelve seats exactly and recovers χ12 on tested terms.

## Closure status

CLOSED_POSITIVE:

```text
parity seating across 12 from lens matrix parity latch
post-L mod-12 n=7 separation
```

Still open for next package:

```text
depth 3-6 Follow channel-field readout
lap-2 = -lap-1 behavior
```
