# Phase 5 v1 Result Card

```text
STATUS: BROKE_AT_PRIMITIVE_TO_GENERATOR_JOIN
FALSIFIER: TRIGGERED_AT_SEATING_JOIN
PHASE_6_FORK: BOUNDARY_MAP
```

## Generated

The explicit Weil representation was constructed for χ12 (`N=12`) and χ8 (`N=8`).

## Broke

The native primitives did not generate the Weil generators.

```text
Q / Q² != T
B/L != S
Ancient Yi carry != S
Wilhelm line6 xor32 != S
```

## Exact failure

Q is residue-independent phase translation. T is residue-quadratic phase multiplication.

B/L are deterministic retained-state maps. S is a dense finite Fourier transform.

## Boundary map

The finite Fourier transform is currently a representation/projection-layer structure, not a primitive generated directly by the exact Q/B/L definitions.
