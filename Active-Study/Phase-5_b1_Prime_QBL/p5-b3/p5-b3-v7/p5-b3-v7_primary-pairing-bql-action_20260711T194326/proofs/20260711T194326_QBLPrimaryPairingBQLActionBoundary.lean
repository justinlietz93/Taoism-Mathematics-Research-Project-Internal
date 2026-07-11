import Mathlib

namespace QBLPrimaryPairingBQL

inductive Op where
  | B | Q | L
  deriving DecidableEq, Repr

structure TwoSlotState (Arg Pair : Type) where
  leftArg : Arg
  rightArg : Arg
  pairing : Pair
  archRank : Nat
  word : List Op

structure BSignature (Arg Pair : Type) where
  step : TwoSlotState Arg Pair → TwoSlotState Arg Pair
  rank_preserved : ∀ s, (step s).archRank = s.archRank
  appends_B : ∀ s, (step s).word = s.word ++ [Op.B]

structure QSignature (Arg Pair : Type) where
  step : TwoSlotState Arg Pair → TwoSlotState Arg Pair
  rank_preserved : ∀ s, (step s).archRank = s.archRank
  appends_Q : ∀ s, (step s).word = s.word ++ [Op.Q]

structure LComponents (OldOld OldNew NewOld NewNew : Type) where
  oldOld : OldOld
  oldNew : OldNew
  newOld : NewOld
  newNew : NewNew

structure LSignature (Arg Pair : Type) where
  step : TwoSlotState Arg Pair → TwoSlotState Arg Pair
  rank_raises : ∀ s, (step s).archRank = s.archRank + 1
  appends_L : ∀ s, (step s).word = s.word ++ [Op.L]
  oldPairingRetained : ∀ s, (step s).pairing = s.pairing

-- Conditional realization lemma: zero mixed blocks require explicit hypotheses.
theorem zeroMixed_of_assumptions
    {V : Type} [Zero V] (oldNew newOld : V)
    (hON : oldNew = 0) (hNO : newOld = 0) :
    oldNew = 0 ∧ newOld = 0 := by
  exact ⟨hON, hNO⟩

structure LocalState where
  u : Rat
  v : Rat
  re : Rat
  im : Rat

def qStep (s : LocalState) : LocalState :=
  { s with re := -s.im, im := s.re }

def bStep (s : LocalState) : LocalState :=
  let f := s.u / (s.u + s.v)
  { u := s.v, v := s.u + s.v, re := s.re * f, im := s.im * f }

def stepLocal : Op → LocalState → LocalState
  | Op.B, s => bStep s
  | Op.Q, s => qStep s
  | Op.L, s => s

def firstWord : List Op :=
  [Op.B, Op.Q, Op.Q, Op.B, Op.B, Op.B, Op.Q, Op.B,
   Op.Q, Op.B, Op.B, Op.Q, Op.B, Op.B, Op.L]

def runLocal : List Op → LocalState → LocalState
  | [], s => s
  | o :: os, s => runLocal os (stepLocal o s)

-- The intended executable theorem surface. Compilation was unavailable.
example :
    let out := runLocal firstWord {u := 1, v := 1, re := 1, im := 0}
    out.u = 55 ∧ out.v = 89 ∧ out.re = 0 ∧ out.im = 1/4895 := by
  norm_num [runLocal, firstWord, stepLocal, bStep, qStep]

end QBLPrimaryPairingBQL
