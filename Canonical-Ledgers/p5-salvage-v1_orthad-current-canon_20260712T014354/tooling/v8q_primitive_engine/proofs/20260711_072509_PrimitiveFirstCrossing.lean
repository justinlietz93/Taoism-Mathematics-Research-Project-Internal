import Std

namespace CanonFirst

structure State where
  A : Nat
  u : Nat
  v : Nat
  phaseQ : Nat
  k : Nat
  j : Nat
  word : String
  deriving Repr, DecidableEq

def positions (A : Nat) : Nat := 6 * 2^A

def capacity : Nat -> Nat
  | 1 => 2
  | 2 => 4
  | j => 2^(2*j)

def nextPair (s : State) : Nat × Nat := (s.v, s.u + s.v)

def canQ (s : State) : Bool := s.k < positions s.A - 1

def canB (s : State) : Bool :=
  if s.k < positions s.A - 1 then
    let p := nextPair s
    p.1 * p.2 <= capacity s.j
  else
    s.u * s.v < capacity s.j

def step (s : State) : State :=
  if canB s then
    let p := nextPair s
    {s with u := p.1, v := p.2, word := s.word ++ "B"}
  else if canQ s then
    {s with phaseQ := s.phaseQ + 1, k := s.k + 1, j := s.j + 1, word := s.word ++ "Q"}
  else
    {s with A := s.A + 1, k := 0, j := 1 + 6 * (2^(s.A+1)-1), word := s.word ++ "L"}

def run : Nat -> State -> State
  | 0, s => s
  | n+1, s => run n (step s)

def init : State := {A:=0,u:=1,v:=1,phaseQ:=0,k:=0,j:=1,word:=""}

theorem firstCrossingWord : (run 15 init).word = "BQQBBBQBQBBQBBL" := by native_decide
theorem firstCrossingCarry :
  let s := run 15 init
  s.A = 1 ∧ s.u = 55 ∧ s.v = 89 ∧ s.phaseQ = 5 ∧ s.k = 0 ∧ s.j = 7 := by native_decide
theorem firstNextDomainPair :
  let s := run 16 init
  s.u = 89 ∧ s.v = 144 := by native_decide

end CanonFirst
