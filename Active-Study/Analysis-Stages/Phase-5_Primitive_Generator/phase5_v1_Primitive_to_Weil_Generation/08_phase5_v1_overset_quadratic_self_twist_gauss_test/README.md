# Phase 5 v1: Orthad Overset Quadratic Self-Twist Gauss Test

Status: GENERATED_GAUSS_DIAGONAL_FROM_OVERSET_SELF_TWIST

Phase 5 v1 closure: GENERATED_WEIL_REPRESENTATION_GENERATORS_WITH_ORTHAD_OVERSET_LENS

This package continues Phase 5 v1 after the overset dual-lens branch generated the finite Fourier transfer. It tests the remaining diagonal generator.

The native rule is not a new primitive. It uses the reverse direction of the generated overset chart transfer, then takes the same-chart self-twist as the quadratic refinement of that native bilinear pairing:

q_N(r) = 1/2 B_+(r,r) = r^2/(2N)

G_native(r) = exp(2*pi*i*q_N(r)) = exp(pi*i*r^2/N)

The native entries were sealed before the external Weil_G target was constructed.
