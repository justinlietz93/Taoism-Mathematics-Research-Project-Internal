# Phase 5 v1 — Corrected Orientation Derivation

Status: `DIAGONAL_ONLY_BOUNDARY`

The pass keeps the canon repairs and performs the corrected derivation instead of returning pending boards.

Result: the full orientation-vector read derived from the exact Q/B/L definitions and the current Orthad read is diagonal-only. It recovers the same-orientation diagonal lens trace but produces zero off-diagonal coupling. Therefore it does not generate the finite Fourier generator. The native Q diagonal phase is linear fourth-root phase, not the N-dependent quadratic Gauss phase, so it does not generate the quadratic Gauss generator for χ12 or χ8 either.

The original Phase 5 residuals remain preserved as banned-method controls. The hand-admitted dense block path is removed and forbidden.
