# shadow_residual_v61_primitive_modular_derivation

Status: CLOSED_PRIMITIVE_MULTIPLIER_DERIVATION / RETAINED_ORIENTATION_CHANNEL

This package upgrades v60 from calibration closure to primitive generator closure. It derives the level-12 S/T multiplier surface from the Phase Calculus retained-state carrier:

- Q square seating gives T_r = exp(pi*i*r^2/12).
- B/L orthogonal retained seating gives S_{r,s} = 12^{-1/2} exp(-pi*i*r*s/6).
- The derivative channel gives the weight-3/2 factor i(-i*tau)^(3/2).
- Coefficient stripping gives the weight-1/2 eta shadow.

Main files:

- docs/v61_primitive_modular_derivation.md
- outputs/v61_verification_summary.json
- outputs/v61_result_card.json
- scripts/primitive_modular_derivation_v61.py
- notebooks/shadow_residual_primitive_modular_derivation_v61.ipynb
- proofs/ShadowResidualV61.lean
- patches/v60_to_v61_positive_framing.patch
