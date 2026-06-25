import Phase3.Core

namespace Phase3

namespace ProjectionLoss

/-- A concrete two-point witness shape used throughout Phase 3. -/
structure CollisionWitness (S P : Type) where
  x : S
  y : S
  proj : S -> P
  step : S -> S
  sameProjection : proj x = proj y
  differentNext : step x ≠ step y

def toSystem {S P : Type} (w : CollisionWitness S P) : TransitionSystem S P :=
  { step := w.step, proj := w.proj }

theorem witness_implies_projection_loss {S P : Type} (w : CollisionWitness S P) :
    TransitionSystem.ProjectionLoss (toSystem w) := by
  exact ⟨w.x, w.y, w.sameProjection, w.differentNext⟩

theorem witness_blocks_custody {S P : Type} (w : CollisionWitness S P) :
    ¬ TransitionSystem.CustodyAdmissible (toSystem w) := by
  exact TransitionSystem.projection_loss_not_custody (toSystem w) (witness_implies_projection_loss w)

end ProjectionLoss

end Phase3
