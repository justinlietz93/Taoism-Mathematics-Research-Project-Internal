import Mathlib

namespace P5V8X

abbrev Matrix2 := Fin 2 → Fin 2 → ℤ

/-- A nonsymmetric pairing with P(new,old)=0 and P(old,new)=1. -/
def oneSided : Matrix2
  | 0, 0 => 1
  | 0, 1 => 1
  | 1, 0 => 0
  | 1, 1 => 1

theorem one_sided_does_not_force_both :
    oneSided 1 0 = 0 ∧ oneSided 0 1 = 1 := by
  native_decide

/-- A two-by-two block is diagonal once both mixed blocks are zero. -/
theorem block_diagonal_of_both_mixed_zero
    (P : Matrix2)
    (h01 : P 0 1 = 0)
    (h10 : P 1 0 = 0) :
    P = fun i j => if i = j then P i i else 0 := by
  funext i j
  fin_cases i <;> fin_cases j <;> simp [h01, h10]

/-- The size-two extension diag(1,0) is singular. -/
def zeroBirth : Matrix2
  | 0, 0 => 1
  | 0, 1 => 0
  | 1, 0 => 0
  | 1, 1 => 0

def det2 (P : Matrix2) : ℤ := P 0 0 * P 1 1 - P 0 1 * P 1 0

theorem zero_birth_size_two_but_singular :
    det2 zeroBirth = 0 ∧ zeroBirth 0 0 = 1 := by
  native_decide

end P5V8X
