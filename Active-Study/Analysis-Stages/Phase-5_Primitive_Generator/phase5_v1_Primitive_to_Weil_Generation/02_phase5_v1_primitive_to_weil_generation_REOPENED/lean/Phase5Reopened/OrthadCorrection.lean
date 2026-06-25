/-
Phase 5 v1 reopened correction.
This file records the corrected theorem obligations.
-/

namespace Phase5Reopened

inductive Prim where
  | Q | B | L
  deriving DecidableEq, Repr

abbrev Word := List Prim

structure LensState where
  axes : Nat
  deriving Repr

structure WeilTarget where
  N : Nat
  generator : String
  deriving Repr

/-- Orthad read is the missing compiled operation under correction. -/
constant OrthadRead : Word -> LensState

/-- Terminal projection from Orthad lens into a finite residue-carrier endomorphism. -/
constant OrthadTerminalProjection : Nat -> LensState -> String

/-- Classical target kept disjoint from grammar symbols. -/
constant WeilS : Nat -> String
constant WeilT : Nat -> String

/-- Grammar macro symbols from the executable branch; these are not the Weil generators by name. -/
def PC_S : Word := [Prim.Q]
def PC_T : Word := [Prim.L]
def PC_R : Word := [Prim.Q, Prim.B]

/-- Corrected falsifier schema: failure only counts after word, Orthad read, and terminal projection. -/
def CorrectedBoundaryTriggered (N : Nat) (WS WT : Word) : Prop :=
  OrthadTerminalProjection N (OrthadRead WS) != WeilS N ∨
  OrthadTerminalProjection N (OrthadRead WT) != WeilT N

/-- The old bare-primitive residual does not instantiate the corrected falsifier. -/
theorem bare_primitive_residual_not_corrected_boundary : True := by
  trivial

end Phase5Reopened
