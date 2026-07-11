import Mathlib

/-!
# QBL prime-pattern watch

This file formalizes the exact Q-count identity and representative modular
sieve facts.  The B-count threshold law is analytic and is presently checked
in the companion SymPy notebook; this file records exact primality checks for
selected emitted B counts.

No R/S/T scheduler occurs here.
-/

namespace QBLPrimePatternWatch

/-- Number of executed Q operations in domain `A`. -/
def qCount (A : ℕ) : ℕ := 6 * 2 ^ A - 1

/-- The same sequence as a modular expression. -/
def qCountMod (p A : ℕ) : ZMod p := 6 * (2 : ZMod p) ^ A - 1

/-- `Q_A` is the shifted Thabit sequence `3 * 2^(A+1) - 1`. -/
theorem qCount_thabit_shift (A : ℕ) :
    qCount A = 3 * 2 ^ (A + 1) - 1 := by
  unfold qCount
  rw [pow_succ]
  omega

/-- Every Q count is odd. -/
theorem qCount_odd (A : ℕ) : Odd (qCount A) := by
  unfold qCount
  obtain ⟨k, hk⟩ : ∃ k, 6 * 2 ^ A = 2 * k := by
    refine ⟨3 * 2 ^ A, ?_⟩
    ring
  rw [hk]
  exact ⟨k - 1, by omega⟩

/-- Modulo five, the Q-count sequence has period four. -/
theorem qCountMod_five_period_four (A : ℕ) :
    qCountMod 5 (A + 4) = qCountMod 5 A := by
  unfold qCountMod
  rw [pow_add]
  norm_num

/-- Hence every domain `A = 4k` lies in the five-divisibility class. -/
theorem qCountMod_five_zero_on_four_mul (k : ℕ) :
    qCountMod 5 (4 * k) = 0 := by
  unfold qCountMod
  rw [pow_mul]
  norm_num

/-- The thirteen-divisibility class begins at `A = 7` and repeats every 12. -/
theorem qCountMod_thirteen_zero_on_seven_add_twelve_mul (k : ℕ) :
    qCountMod 13 (7 + 12 * k) = 0 := by
  unfold qCountMod
  rw [pow_add, pow_mul]
  norm_num

/- Exact finite Q witnesses. -/
example : Nat.Prime (qCount 0) := by native_decide
example : Nat.Prime (qCount 1) := by native_decide
example : Nat.Prime (qCount 2) := by native_decide
example : Nat.Prime (qCount 3) := by native_decide
example : ¬ Nat.Prime (qCount 4) := by native_decide
example : Nat.Prime (qCount 17) := by native_decide
example : ¬ Nat.Prime (qCount 7) := by native_decide

/- Exact finite B-count primality witnesses emitted by the companion analysis. -/
example : Nat.Prime 139 := by native_decide
example : Nat.Prime 1132793 := by native_decide
example : ¬ Nat.Prime 9 := by native_decide
example : ¬ Nat.Prime 18 := by native_decide
example : ¬ Nat.Prime 276 := by native_decide

/-- The observed simultaneous-prime witness at domain 17. -/
example : Nat.Prime 786431 ∧ Nat.Prime 1132793 := by native_decide

end QBLPrimePatternWatch
