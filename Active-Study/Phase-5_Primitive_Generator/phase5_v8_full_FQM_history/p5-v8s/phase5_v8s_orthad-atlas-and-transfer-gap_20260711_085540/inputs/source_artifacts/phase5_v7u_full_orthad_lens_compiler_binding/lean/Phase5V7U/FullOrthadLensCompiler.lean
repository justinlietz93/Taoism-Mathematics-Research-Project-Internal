namespace Phase5V7U

inductive Kind where | Q | B | L | O | R deriving DecidableEq, Repr

structure Support where
  read : List Nat
  write : List Nat
  birth : List Nat
  deriving Repr

def disjoint (xs ys : List Nat) : Prop := ∀ x, x ∈ xs → x ∉ ys

def independent (a b : Support) : Prop :=
  disjoint a.write (b.read ++ b.write ++ b.birth) ∧
  disjoint b.write (a.read ++ a.write ++ a.birth) ∧
  disjoint a.birth (b.read ++ b.write ++ b.birth) ∧
  disjoint b.birth (a.read ++ a.write ++ a.birth)

structure LensAxis where
  uv : Nat
  phase : Nat
  deriving Repr

structure Ratio where
  num : Nat
  den : Nat
  phase : Nat
  deriving Repr

def idRatio : Ratio := ⟨1,1,0⟩

def mulRatio (a b : Ratio) : Ratio :=
  ⟨a.num * b.num, a.den * b.den, (a.phase + b.phase) % 4⟩

theorem terminal_readout_identity : mulRatio idRatio idRatio = idRatio := by
  rfl

theorem legal_swap_schema
  (sa sb : Support)
  (h : independent sa sb) : independent sb sa := by
  constructor
  · exact h.2.1
  constructor
  · exact h.1
  constructor
  · exact h.2.2.2
  · exact h.2.2.1

end Phase5V7U
