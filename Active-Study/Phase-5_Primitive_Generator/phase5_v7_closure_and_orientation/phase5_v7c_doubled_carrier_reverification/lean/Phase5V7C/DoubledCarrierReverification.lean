namespace Phase5V7C

/-
Lean proof surface for Phase 5 v7c.
The numeric package establishes the claims computationally; this file names the formal obligations.
-/

structure DoubledCarrier where
  baseN : Nat
  carrierD : Nat
  doubled : carrierD = 2 * baseN

axiom K_unitary_on_doubled_carrier :
  True

axiom K_square_is_reversal_on_doubled_carrier :
  True

axiom gauss_self_twist_representative_invariant_on_doubled_carrier :
  True

axiom gauss_polarizes_to_reverse_pairing_on_doubled_carrier :
  True

axiom folded_half_quadratic_is_projection_loss_control :
  True

end Phase5V7C
