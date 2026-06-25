namespace Phase5CanonRepair

inductive Prim where
  | Q | B | L
  deriving DecidableEq, Repr

abbrev Word := List Prim

inductive PCBranch where
  | PC_REF | PC_HOLD | PC_LFT
  deriving DecidableEq, Repr

inductive WeilTarget where
  | Weil_F_N | Weil_G_N
  deriving DecidableEq, Repr

structure CorrectedProtocol where
  hasWordG : Bool
  hasWordF : Bool
  hasProjection : Bool

def correctedFalsifierCanRun (p : CorrectedProtocol) : Bool :=
  p.hasWordG && p.hasWordF && p.hasProjection

theorem no_corrected_boundary_without_words
  (p : CorrectedProtocol)
  (hG : p.hasWordG = false) :
  correctedFalsifierCanRun p = false := by
  cases p
  simp [correctedFalsifierCanRun] at *
  simp [hG]

theorem suspended_degenerate_macro_not_word_derivation :
  (Prim.Q :: []) ≠ ([] : Word) := by
  decide

end Phase5CanonRepair
