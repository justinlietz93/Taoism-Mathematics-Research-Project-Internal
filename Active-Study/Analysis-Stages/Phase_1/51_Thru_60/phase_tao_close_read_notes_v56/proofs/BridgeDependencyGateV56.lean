/-
BridgeDependencyGateV56
Companion proof surface for the v56 bridge-claim dependency gate.
This file attacks the core logical shape only: projection equivalence is not
state completeness unless next-transition behavior is preserved.
-/

structure BridgeState where
  carrier : Nat
  registry : Nat
  history : Nat
  deriving DecidableEq, Repr

structure Projection where
  visible : Nat
  deriving DecidableEq, Repr

def project (s : BridgeState) : Projection := { visible := s.carrier }

def nextCode (s : BridgeState) : Nat := s.carrier + 10*s.registry + 100*s.history

def sA : BridgeState := { carrier := 1, registry := 0, history := 0 }
def sB : BridgeState := { carrier := 1, registry := 1, history := 0 }

theorem same_projection_not_same_state : project sA = project sB ∧ sA ≠ sB := by
  constructor
  · rfl
  · intro h
    cases h

theorem same_projection_not_next_complete : project sA = project sB ∧ nextCode sA ≠ nextCode sB := by
  constructor
  · rfl
  · decide
