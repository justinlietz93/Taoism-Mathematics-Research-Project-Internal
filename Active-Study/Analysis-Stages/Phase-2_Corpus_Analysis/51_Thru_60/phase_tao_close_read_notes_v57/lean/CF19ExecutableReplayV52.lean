/-
CF19 executable/data replay gate v52.
This Lean file is a lightweight companion attack surface, not a full formalization of the assembly runners.
It pins the finite arithmetic claims used by the research pass.
-/

namespace CF19V52

abbrev Pair := Nat × Nat

def B (p : Pair) : Pair :=
  let u := p.fst
  let v := p.snd
  if v <= u + v then (v, u + v) else (u + v, v)

def uv (p : Pair) : Nat := p.fst * p.snd

def iterB : Nat -> Pair -> Pair
| 0, p => p
| n+1, p => iterB n (B p)

#eval iterB 9 (1,1)   -- expected (55, 89)
#eval iterB 8 (1,2)   -- expected (55, 89)
#eval uv (iterB 9 (1,1)) -- expected 4895
#eval iterB 8 (1,3)   -- non-origin corridor, expected (76,123)
#eval iterB 5 (2,13)  -- non-origin corridor, expected (71,114)

example : iterB 9 (1,1) = (55,89) := by native_decide
example : iterB 8 (1,2) = (55,89) := by native_decide
example : uv (iterB 9 (1,1)) = 4895 := by native_decide
example : iterB 8 (1,3) = (76,123) := by native_decide
example : iterB 5 (2,13) = (71,114) := by native_decide

end CF19V52
