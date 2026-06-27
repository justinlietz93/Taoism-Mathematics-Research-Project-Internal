namespace Phase5V7T

structure Presentation where
  rank : Nat
  symmetric : Bool
  radicalDim : Nat
  twoPrimaryPolicyApplied : Bool
  deriving Repr, DecidableEq

def admissible (p : Presentation) : Bool :=
  p.symmetric && p.twoPrimaryPolicyApplied && (p.radicalDim == 0)

theorem admissible_implies_symmetric (p : Presentation) : admissible p = true -> p.symmetric = true := by
  intro h
  unfold admissible at h
  exact Bool.and_eq_true.mp (Bool.and_eq_true.mp h).1 |>.1

theorem admissible_implies_policy (p : Presentation) : admissible p = true -> p.twoPrimaryPolicyApplied = true := by
  intro h
  unfold admissible at h
  exact Bool.and_eq_true.mp (Bool.and_eq_true.mp h).1 |>.2

theorem admissible_implies_radical_zero (p : Presentation) : admissible p = true -> p.radicalDim = 0 := by
  intro h
  unfold admissible at h
  have h2 := Bool.and_eq_true.mp h
  exact Nat.eq_zero_of_beq_eq_true h2.2

def rawTensorIsInvariant : Bool := false

theorem coordinate_demotion : rawTensorIsInvariant = false := rfl

end Phase5V7T
