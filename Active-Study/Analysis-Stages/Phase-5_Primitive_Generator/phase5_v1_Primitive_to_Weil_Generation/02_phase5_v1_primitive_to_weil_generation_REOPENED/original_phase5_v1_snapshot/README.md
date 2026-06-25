# Phase 5 v1 — Primitive-to-Weil Generation Attempt

Status: `BROKE_AT_PRIMITIVE_TO_GENERATOR_JOIN`

The exact Q/B/L primitives currently do not generate the Weil representation under the non-retuning constraint.

This package runs the Phase 5 test directly: can the exact native Q/B/L primitives generate the Weil representation generators S and T without adding a fresh dual-seating primitive?

Verdict: the attempt breaks at the generator join. The explicit Weil representation still reproduces the χ12 and χ8 multiplier surfaces, but the exact native primitives do not generate those S/T matrices value-for-value.
