namespace Phase5V1

structure ZModCarrier where
  N : Nat
  pos : N > 0

/-- Native reverse overset bilinear pairing, represented by numerator r*s. -/
def Bplus (N r s : Nat) : Nat := r * s

/-- Quadratic self twist numerator before division by 2N. -/
def qnum (N r : Nat) : Nat := r * r

/-- Polarization identity at numerator level. -/
theorem polarization_num (N r s : Nat) :
  (r + s) * (r + s) = r*r + s*s + 2*(r*s) := by
  ring

/-- Phase 5 v1 closure theorem surface: self-twist polarizes to reverse transfer. -/
theorem self_twist_polarizes_to_pairing (N r s : Nat) :
  (r + s) * (r + s) - r*r - s*s = 2*(r*s) := by
  omega

end Phase5V1
