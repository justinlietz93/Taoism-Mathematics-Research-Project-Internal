import Std

namespace P5V8V

inductive Primitive where
  | B | Q | L
  deriving DecidableEq, Repr

structure Custody where
  A : Nat
  u : Nat
  v : Nat
  phaseQuarters : Int
  k : Nat
  j : Nat
  word : List Primitive
  deriving DecidableEq, Repr

def qStep (x : Custody) : Custody :=
  { x with
    phaseQuarters := x.phaseQuarters + 1
    k := x.k + 1
    j := x.j + 1
    word := x.word ++ [Primitive.Q] }

def jStart (A : Nat) : Nat := 1 + 6 * (2^A - 1)

def lStep (x : Custody) : Custody :=
  { x with
    A := x.A + 1
    k := 0
    j := jStart (x.A + 1)
    word := x.word ++ [Primitive.L] }

theorem q_updates_indices (x : Custody) :
    (qStep x).k = x.k + 1 ∧ (qStep x).j = x.j + 1 := by
  simp [qStep]

theorem q_preserves_pair_and_domain (x : Custody) :
    (qStep x).u = x.u ∧ (qStep x).v = x.v ∧ (qStep x).A = x.A := by
  simp [qStep]

theorem l_carries_pair_and_phase (x : Custody) :
    (lStep x).u = x.u ∧ (lStep x).v = x.v ∧
    (lStep x).phaseQuarters = x.phaseQuarters := by
  simp [lStep]

theorem l_resets_local_index (x : Custody) : (lStep x).k = 0 := by
  simp [lStep]

structure LiftedMeta where
  custody : Custody
  pairingRank : Nat

def changeLocalIndex (x : LiftedMeta) (kNew : Nat) : LiftedMeta :=
  { x with custody := { x.custody with k := kNew } }

theorem pairing_rank_separate_from_k (x : LiftedMeta) (kNew : Nat) :
    (changeLocalIndex x kNew).pairingRank = x.pairingRank := by
  rfl

inductive Stage where
  | retainedBefore
  | primitiveSelected
  | custodyAdvanced
  | pairingAdvanced
  | chartsDerived
  | transfersDerived
  | retainedAfter
  deriving DecidableEq, Repr

def causalOrder : List Stage :=
  [ Stage.retainedBefore,
    Stage.primitiveSelected,
    Stage.custodyAdvanced,
    Stage.pairingAdvanced,
    Stage.chartsDerived,
    Stage.transfersDerived,
    Stage.retainedAfter ]

theorem one_tick_causal_order : causalOrder.length = 7 := by
  decide

def BilinInt := Int → Int → Int

def pOne : BilinInt := fun x y => x * y

def pTwo : BilinInt := fun x y => 2 * x * y

theorem pairing_seed_witness_distinct : pOne 1 1 ≠ pTwo 1 1 := by
  decide

end P5V8V
