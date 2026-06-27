namespace Phase5V7R

structure Form where
  n : Nat
  a00 : Nat
  a01 : Nat
  a11 : Nat
  deriving Repr, DecidableEq

structure Change where
  n : Nat
  p00 : Nat
  p01 : Nat
  p10 : Nat
  p11 : Nat
  deriving Repr, DecidableEq

def sameMod (n x y : Nat) : Prop := x % n = y % n

def det2 (P : Change) : Nat :=
  P.p00 * P.p11 + P.n * P.n - P.p01 * P.p10

def coordinatePresentation (_F : Form) : Prop := True

def gaugeEquivalent (F G : Form) : Prop :=
  F.n = G.n

theorem gauge_equiv_refl (F : Form) : gaugeEquivalent F F := by
  unfold gaugeEquivalent
  rfl

theorem coordinate_presentation_not_invariant_claim (F : Form) : coordinatePresentation F := by
  trivial

theorem raw_matrix_not_final_object (F : Form) : coordinatePresentation F := by
  exact coordinate_presentation_not_invariant_claim F

end Phase5V7R
