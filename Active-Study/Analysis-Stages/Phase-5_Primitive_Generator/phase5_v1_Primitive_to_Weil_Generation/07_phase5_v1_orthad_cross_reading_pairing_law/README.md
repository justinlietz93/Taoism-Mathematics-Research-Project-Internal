# Phase 5 v1 — Orthad Cross-Reading Pairing Law Attempt

Status: `BOUNDARY_NATIVE_CROSS_READ_FOUND_NOT_WEIL`

Phase 5 v1 remains open. This package keeps the previous mistakes and repair branches in the same track and adds the first native cross-reading attempt.

## One-line result

The Orthad does produce native cross-reading candidates from QBL word history, especially shared-prefix overlap, but the derived pairings are overlap/separation laws such as `min(r,s)`, not the bilinear `r*s` law required by the finite Fourier generator.

## Sealed discipline

Native QBL cross-read tables were written to `sealed/` and hashed before any Weil comparison target was constructed.

## Verdict

- Generated: no.
- Diagonal-only: no; nonzero off-diagonal native pair candidates exist.
- Boundary: yes. The boundary is located at the missing multiplicative pairing rule between independent orientation histories.

## Best native discovery

`shared_prefix_count(r,s) = min(r,s)`.

This is a true Orthad-style cross-read: it reads how much history two orientations share. It is not the Fourier pairing.
