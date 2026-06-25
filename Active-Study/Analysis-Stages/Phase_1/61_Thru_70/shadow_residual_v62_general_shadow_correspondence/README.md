# Shadow Residual v62 — General Shadow Correspondence Push

Status: SECOND_CASE_WORKS_ON_FULL_RETAINED_RESIDUE_CARRIER

This package pushes beyond the closed χ12/level-12 Shadow Residual instance.

It tests a second unary false-theta channel:
- m = 4
- residue carrier Z/8Z
- even character χ8 = (2/n)
- positive retained readout: R8(τ) = Σ_{n≥1} χ8(n) n q^(n²/16)
- coefficient-stripped shadow channel: G8(τ) = Σ_{n≥1} χ8(n) q^(n²/16)

Result:
- bilateral n-weighted scalar projection cancels by orientation loss
- positive-orientation readout is nonzero
- S kernel is forced by the retained residue carrier
- T phases are forced by square seating
- scalar χ8 compression fails under T
- the full retained residue carrier closes the case

This is a useful boundary: the general mechanism is vector-valued. The χ12 case has an extra scalar eigenclosure property that χ8 does not.
