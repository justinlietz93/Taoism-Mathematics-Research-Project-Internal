namespace P5V8Y

structure CLike where
  re : Int
  im : Int
  deriving DecidableEq, Repr

def conj (z : CLike) : CLike := { re := z.re, im := -z.im }
def imagUnit : CLike := { re := 0, im := 1 }

theorem imagUnit_not_conj_fixed : conj imagUnit ≠ imagUnit := by decide

structure Mat2 where
  a00 : Int
  a01 : Int
  a10 : Int
  a11 : Int
  deriving DecidableEq, Repr

def oneSided : Mat2 := { a00 := 1, a01 := 1, a10 := 0, a11 := 1 }
theorem new_old_zero : oneSided.a10 = 0 := by decide
theorem old_new_nonzero : oneSided.a01 ≠ 0 := by decide
theorem one_sided_counterexample : oneSided.a10 = 0 ∧ oneSided.a01 ≠ 0 := ⟨new_old_zero, old_new_nonzero⟩

end P5V8Y
