# Protocol Definitions

## Admissible retained history

A retained history is admissible when:

1. all referenced axes have already been born,
2. primitive `Q`, `B`, and `L` act only on the active axis,
3. `L` creates the next active axis exactly once,
4. `O_ab` may only read born axes,
5. `R` is terminal readout and mutates nothing.

## Support-derived independence

Two events are independent when their read/write/birth supports do not conflict.

Legal adjacent swaps are generated only from this support-disjointness law.

## Confluence gate

For an adjacent legal swap:

```text
compile(h1) and compile(h2)
```

must yield the same transition-derived classifier key.

## Cocycle gate

For all compiler-created chart triangles in the tested support cover:

```text
T_ab T_bc T_ca = 1
```

## Gauge gate

Axis relabeling / permutation must preserve the classifier key.

## Large-rank gate

For rank above brute-force feasibility, the classifier must not enumerate full module elements or full isometry orbits. It must compute structural p-primary signatures directly.
