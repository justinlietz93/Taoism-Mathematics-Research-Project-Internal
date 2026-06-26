namespace Phase5V7RProofSurface

structure GaugeClass where
  carrierOrder : Nat
  canonicalKey : List Nat
  deriving Repr, DecidableEq

def sameGaugeClass (A B : GaugeClass) : Prop :=
  A.carrierOrder = B.carrierOrder ∧ A.canonicalKey = B.canonicalKey

theorem sameGaugeClass_refl (A : GaugeClass) : sameGaugeClass A A := by
  unfold sameGaugeClass
  exact And.intro rfl rfl

theorem coordinate_matrix_demoted (A : GaugeClass) : sameGaugeClass A A := by
  exact sameGaugeClass_refl A

end Phase5V7RProofSurface
