import Mathlib

/-!
# QBL B-count dyadic carry theorem surface

The analytic all-domain Fibonacci-threshold/ceiling bridge remains open.
The companion experiment certifies it through A = 10000.
No R/S/T scheduler is used.
-/
namespace QBLBDefect
variable (T : ℕ → ℤ)

def bCount (A : ℕ) : ℤ := T (A + 1) - T A
def carry (A : ℕ) : ℤ := T (A + 1) - 2 * T A
def defect (A : ℕ) : ℤ := bCount T (A + 1) - 2 * bCount T A

theorem defect_eq_carry_difference (A : ℕ) :
    defect T A = carry T (A + 1) - carry T A := by
  unfold defect bCount carry
  ring

theorem defect_bounded
    (A : ℕ)
    (h0lo : 7 ≤ carry T A) (h0hi : carry T A ≤ 9)
    (h1lo : 7 ≤ carry T (A + 1)) (h1hi : carry T (A + 1) ≤ 9) :
    -2 ≤ defect T A ∧ defect T A ≤ 2 := by
  rw [defect_eq_carry_difference]
  constructor <;> omega

theorem bCount_parity_eq_defect_parity (A : ℕ) :
    (bCount T (A + 1)) % 2 = (defect T A) % 2 := by
  unfold defect
  omega

end QBLBDefect
