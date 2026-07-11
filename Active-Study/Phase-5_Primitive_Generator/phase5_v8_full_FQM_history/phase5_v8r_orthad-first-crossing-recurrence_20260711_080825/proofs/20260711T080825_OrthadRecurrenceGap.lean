structure PairingData where
  plusRestriction : Nat
  minusRestriction : Nat
  plusToMinus : Nat
  minusToPlus : Nat

def SameRestrictions (p q : PairingData) : Prop :=
  p.plusRestriction = q.plusRestriction ∧
  p.minusRestriction = q.minusRestriction

theorem restrictions_do_not_determine_transfer (a : Nat) :
    ∃ p q : PairingData,
      SameRestrictions p q ∧ p.plusToMinus ≠ q.plusToMinus := by
  refine ⟨{ plusRestriction := a, minusRestriction := a, plusToMinus := 0, minusToPlus := 0 },
          { plusRestriction := a, minusRestriction := a, plusToMinus := 1, minusToPlus := 0 }, ?_, ?_⟩
  · exact ⟨rfl, rfl⟩
  · decide
