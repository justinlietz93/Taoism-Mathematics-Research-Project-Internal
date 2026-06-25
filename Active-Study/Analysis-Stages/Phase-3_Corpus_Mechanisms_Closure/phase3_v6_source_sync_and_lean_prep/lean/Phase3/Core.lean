namespace Phase3

universe u v

structure TransitionSystem (S : Type u) (P : Type v) where
  step : S -> S
  proj : S -> P

namespace TransitionSystem

def CustodyAdmissible {S : Type u} {P : Type v} (T : TransitionSystem S P) : Prop :=
  ∃ G : P -> S, ∀ x : S, T.step x = G (T.proj x)

def ProjectionLoss {S : Type u} {P : Type v} (T : TransitionSystem S P) : Prop :=
  ∃ x y : S, T.proj x = T.proj y ∧ T.step x ≠ T.step y

def QuotientAdmissible {S : Type u} {P : Type v} (T : TransitionSystem S P) : Prop :=
  ∃ H : P -> P, ∀ x : S, T.proj (T.step x) = H (T.proj x)

theorem projection_loss_not_custody {S : Type u} {P : Type v} (T : TransitionSystem S P) :
    ProjectionLoss T -> ¬ CustodyAdmissible T := by
  intro hloss hcust
  rcases hloss with ⟨x, y, hproj, hneq⟩
  rcases hcust with ⟨G, hG⟩
  have hx : T.step x = G (T.proj x) := hG x
  have hy : T.step y = G (T.proj y) := hG y
  have hGxy : G (T.proj x) = G (T.proj y) := by
    rw [hproj]
  have hstep : T.step x = T.step y := by
    calc
      T.step x = G (T.proj x) := hx
      _ = G (T.proj y) := hGxy
      _ = T.step y := hy.symm
  exact hneq hstep

end TransitionSystem

inductive PhaseStatus where
  | proved
  | conditional
  | openTarget
  | dataBlocked
  deriving Repr, DecidableEq

structure ClaimCard where
  id : String
  title : String
  status : PhaseStatus
  falsifier : String
  deriving Repr

end Phase3
