namespace Phase5V8T
structure Sym2 where a : Int; b : Int; d : Int

def P0 : Sym2 := {a:=1,b:=0,d:=1}
def P2 : Sym2 := {a:=1,b:=2,d:=1}
def det (p : Sym2) : Int := p.a*p.d-p.b*p.b

theorem same_diagonal_restrictions : P0.a = P2.a ∧ P0.d = P2.d := by decide
theorem different_mixed_terms : P0.b ≠ P2.b := by decide
theorem P0_nondegenerate : det P0 ≠ 0 := by decide
theorem P2_nondegenerate : det P2 ≠ 0 := by decide
end Phase5V8T
