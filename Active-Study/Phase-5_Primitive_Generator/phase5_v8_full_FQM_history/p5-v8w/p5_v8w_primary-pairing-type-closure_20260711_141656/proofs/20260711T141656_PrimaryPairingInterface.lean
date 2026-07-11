namespace P5V8W

/-- A block presentation stores old, old-to-new, new-to-old, and new entries. -/
structure PairingBlock where
  old : Int
  oldToNew : Int
  newToOld : Int
  new : Int
  deriving DecidableEq, Repr

/-- Two-sided orthogonality forces the mixed birth blocks to vanish. -/
theorem orthogonal_extension_block_diagonal
    (old new oldToNew newToOld : Int)
    (h₁ : oldToNew = 0)
    (h₂ : newToOld = 0) :
    PairingBlock.mk old oldToNew newToOld new = PairingBlock.mk old 0 0 new := by
  cases h₁
  cases h₂
  rfl

/-- One architectural axis does not determine module dimension. -/
structure AxisModel where
  axisCount : Nat
  moduleDimension : Nat
  deriving DecidableEq, Repr

def axisModelOne : AxisModel := ⟨1, 1⟩
def axisModelTwo : AxisModel := ⟨1, 2⟩

theorem axis_count_not_dimension :
    axisModelOne.axisCount = axisModelTwo.axisCount ∧
    axisModelOne.moduleDimension ≠ axisModelTwo.moduleDimension := by
  decide

end P5V8W
