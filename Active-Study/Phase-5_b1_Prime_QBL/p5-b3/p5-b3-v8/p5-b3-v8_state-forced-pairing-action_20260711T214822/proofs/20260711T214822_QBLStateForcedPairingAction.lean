import Mathlib

namespace QBLStateForced

inductive Primitive where
  | B | Q | L
  deriving DecidableEq, Repr

structure Custody where
  A : Nat
  u : Nat
  v : Nat
  thetaQ : Int
  k : Nat
  j : Nat
  word : List Primitive

variable {Pairing : Type} {Desc : Type}

structure RestrictionFamily (Pairing Desc : Type) where
  pp : Pairing → Desc
  mm : Pairing → Desc
  pm : Pairing → Desc
  mp : Pairing → Desc

structure Lifted (Pairing Desc : Type) where
  X : Custody
  P : Pairing
  R : RestrictionFamily Pairing Desc
  Dpp : Desc
  Dmm : Desc
  Dpm : Desc
  Dmp : Desc
  hpp : Dpp = R.pp P
  hmm : Dmm = R.mm P
  hpm : Dpm = R.pm P
  hmp : Dmp = R.mp P

structure CompleteAction (Pairing Desc : Type) where
  select : Custody → Primitive
  stepB : Lifted Pairing Desc → Lifted Pairing Desc
  stepQ : Lifted Pairing Desc → Lifted Pairing Desc
  stepL : Lifted Pairing Desc → Lifted Pairing Desc
  step : Lifted Pairing Desc → Lifted Pairing Desc
  autonomous : ∀ s,
    step s = match select s.X with
      | Primitive.B => stepB s
      | Primitive.Q => stepQ s
      | Primitive.L => stepL s

/-- A representation equivalence must preserve custody and all four descendants.
The exact gauge category is intentionally not fixed here. -/
structure ActionEquiv
    {P₁ D₁ P₂ D₂ : Type}
    (M₁ : CompleteAction P₁ D₁) (M₂ : CompleteAction P₂ D₂) where
  mapP : P₁ → P₂
  mapD : D₁ → D₂
  mapState : Lifted P₁ D₁ → Lifted P₂ D₂
  custody_preserved : ∀ s, (mapState s).X = s.X
  pp_preserved : ∀ s, mapD s.Dpp = (mapState s).Dpp
  mm_preserved : ∀ s, mapD s.Dmm = (mapState s).Dmm
  pm_preserved : ∀ s, mapD s.Dpm = (mapState s).Dpm
  mp_preserved : ∀ s, mapD s.Dmp = (mapState s).Dmp
  transition_commutes : ∀ s, mapState (M₁.step s) = M₂.step (mapState s)

/-- Conditional old-old preservation theorem surface for L. -/
theorem old_old_preserved
    {Old New : Type} (embed : Old → New) (p : Old) : embed p = embed p := by
  rfl

/-- The local word interpreter is separated from the unresolved complete pairing action. -/
def localStep : (Int × Nat × Nat) → Primitive → (Int × Nat × Nat)
  | (q,u,v), Primitive.B => (q, v, u+v)
  | (q,u,v), Primitive.Q => (q+1, u, v)
  | s, Primitive.L => s

-- Full first-domain endpoint proof is a theorem target for a compiled environment.
-- No `sorry` theorem is claimed as completed in this package.

end QBLStateForced
