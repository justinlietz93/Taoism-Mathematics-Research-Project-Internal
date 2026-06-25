/-
BranchGrammarStateCompletenessV47.lean

Attack surface for the v47 bridge claim:
primitive operator-word equality does not imply branch-state equality.
The script is intentionally minimal and mirrors the SymPy gate:
visible readout can collide while retained sheet/history differs.
-/

structure BranchState where
  A : Nat
  q1 : Int
  q2 : Int
  thetaMod4 : Int
  cDen : Int
  sheet : Int
  kappa : Int
  historyLen : Nat
  deriving DecidableEq, Repr

def visible (s : BranchState) : Nat × Int × Int × Int × Int :=
  (s.A, s.q1, s.q2, s.thetaMod4, s.cDen)

def s0 : BranchState :=
  { A := 5, q1 := 17711, q2 := 28657, thetaMod4 := 0, cDen := 507544127,
    sheet := 0, kappa := 0, historyLen := 0 }

def s1 : BranchState :=
  { A := 5, q1 := 17711, q2 := 28657, thetaMod4 := 0, cDen := 507544127,
    sheet := 1, kappa := 0, historyLen := 1 }

theorem visible_collision_v47 : visible s0 = visible s1 := by
  rfl

theorem retained_sheet_diff_v47 : s0.sheet ≠ s1.sheet := by
  decide

theorem retained_history_diff_v47 : s0.historyLen ≠ s1.historyLen := by
  decide

-- Interpretation: visible equality is not state completeness.
-- A terminal projection cannot replace the retained lifted branch state.
