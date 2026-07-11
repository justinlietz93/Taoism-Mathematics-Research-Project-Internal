/- Phase 5 v7p Lean surface. -/

namespace Phase5V7P

inductive Kind where
  | Q | B | L | O | R
  deriving DecidableEq, Repr

structure Event where
  kind : Kind
  axis : Nat
  other : Nat := 0
  deriving DecidableEq, Repr

structure Support where
  reads : List String
  writes : List String
  birthsRequired : List Nat
  birthsCreated : List Nat
  deriving Repr

def disjointString (a b : List String) : Prop :=
  ∀ x, x ∈ a → x ∈ b → False

def disjointNat (a b : List Nat) : Prop :=
  ∀ x, x ∈ a → x ∈ b → False

structure Independent (a b : Support) : Prop where
  noLeftWriteConflict : disjointString a.writes (b.reads ++ b.writes)
  noRightWriteConflict : disjointString b.writes (a.reads ++ a.writes)
  noBirthCrossing1 : disjointNat a.birthsCreated b.birthsRequired
  noBirthCrossing2 : disjointNat b.birthsCreated a.birthsRequired

theorem independent_symm {a b : Support} : Independent a b → Independent b a := by
  intro h
  exact ⟨h.noRightWriteConflict, h.noLeftWriteConflict, h.noBirthCrossing2, h.noBirthCrossing1⟩

end Phase5V7P
