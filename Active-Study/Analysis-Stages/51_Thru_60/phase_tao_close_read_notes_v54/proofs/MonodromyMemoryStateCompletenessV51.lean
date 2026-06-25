-- v51 Monodromy memory state-completeness companion attack.
-- The local container used for this pass does not provide Lean/lake execution.
-- This file records the finite theorem shape attacked by Python/SymPy.

structure FullRegister where
  sheet : Nat
  kappa : Int
  history_len : Nat
  deriving Repr, DecidableEq

structure Visible where
  tag : Nat
  deriving Repr, DecidableEq

def visible (_s : FullRegister) : Visible := { tag := 0 }

def emptyLoop : FullRegister := { sheet := 0, kappa := 0, history_len := 0 }
def twoTurnLoop : FullRegister := { sheet := 0, kappa := 2, history_len := 2 }

theorem visible_collision : visible emptyLoop = visible twoTurnLoop := by
  rfl

theorem full_register_changed : emptyLoop ≠ twoTurnLoop := by
  intro h
  cases h
  contradiction

def commImages : List Nat := [0, 2, 4, 3, 1]
def idImages : List Nat := [0, 1, 2, 3, 4]

theorem commutator_nonidentity : commImages ≠ idImages := by
  decide
