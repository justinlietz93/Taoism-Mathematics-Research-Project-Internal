import Mathlib

open Real

noncomputable section

namespace QBLGlobalThreshold

/-- Golden ratio. -/
def phi : ℝ := (1 + Real.sqrt 5) / 2

/-- Exact indexed Fibonacci product. -/
def P (n : ℕ) : ℕ := Nat.fib (n + 1) * Nat.fib (n + 2)

/-- QBL threshold exponent. -/
def mA (A : ℕ) : ℕ := 12 * (2 ^ (A + 1) - 1)

/-- Exact QBL threshold. -/
def X (A : ℕ) : ℕ := 2 ^ mA A

/-- Binet leading term. -/
def L (n : ℕ) : ℝ := phi ^ (2 * n + 3) / 5

/-- Signed Binet correction. -/
def rho (n : ℕ) : ℝ := (((-1 : ℝ) ^ n) - phi ^ (-(2 * (n : ℤ) + 3))) / 5

/-- Affine threshold coordinate. -/
def y (A : ℕ) : ℝ :=
  ((mA A : ℝ) * Real.log 2 + Real.log 5) / (2 * Real.log phi) - 3 / 2

/-- Generic integer-gap sign transfer. -/
theorem integer_gap_sign_transfer
    (p x : ℤ) (l r : ℝ)
    (hdecomp : (p : ℝ) = l + r)
    (hr : |r| < (1 : ℝ) / 4)
    (hne : p ≠ x) :
    (((p : ℝ) > (x : ℝ)) ↔ l > (x : ℝ)) := by
  constructor
  · intro hpx
    have hunit : (p : ℝ) - (x : ℝ) ≥ 1 := by
      have hz : p - x ≥ 1 := by omega
      exact_mod_cast hz
    rw [hdecomp] at hunit
    linarith [abs_lt.mp hr]
  · intro hlx
    by_contra hnot
    have hle : p ≤ x := by exact_mod_cast (not_lt.mp hnot)
    have hunit : (p : ℝ) - (x : ℝ) ≤ -1 := by
      have hz : p - x ≤ -1 := by omega
      exact_mod_cast hz
    rw [hdecomp] at hunit
    linarith [abs_lt.mp hr]

/-- The same hypotheses force a uniform 3/4 separation. -/
theorem leading_term_separation
    (p x : ℤ) (l r : ℝ)
    (hdecomp : (p : ℝ) = l + r)
    (hr : |r| < (1 : ℝ) / 4)
    (hne : p ≠ x) :
    |l - (x : ℝ)| > (3 : ℝ) / 4 := by
  have hgap : |(p : ℝ) - (x : ℝ)| ≥ 1 := by
    have hz : p - x ≠ 0 := sub_ne_zero.mpr hne
    have habs : |p - x| ≥ 1 := Int.one_le_abs hz
    exact_mod_cast habs
  have hdiff : |((p : ℝ) - (x : ℝ)) - (l - (x : ℝ))| < (1 : ℝ) / 4 := by
    rw [show ((p : ℝ) - (x : ℝ)) - (l - (x : ℝ)) = r by linarith [hdecomp]]
    exact hr
  have htri := abs_sub_abs_le_abs_sub ((p : ℝ) - (x : ℝ)) (l - (x : ℝ))
  nlinarith [abs_nonneg (l - (x : ℝ))]

/-- Exact Binet product identity. Full proof obligation stated for compilation. -/
theorem exact_binet_product_identity (n : ℕ) :
    (P n : ℝ) = L n + rho n := by
  sorry

/-- Exact parity sign of the correction. -/
theorem correction_sign (n : ℕ) :
    (Even n → 0 < rho n) ∧ (Odd n → rho n < 0) := by
  sorry

/-- Uniform correction bound. -/
theorem correction_abs_lt_quarter (n : ℕ) :
    |rho n| < (1 : ℝ) / 4 := by
  sorry

/-- Indexed consecutive Fibonacci products are powers of two only at n=0 or n=1. -/
theorem fibonacci_product_power_two_only (n m : ℕ)
    (hpow : P n = 2 ^ m) : n = 0 ∨ n = 1 := by
  sorry

/-- No indexed Fibonacci product equals a QBL threshold. -/
theorem threshold_equality_obstruction (A n : ℕ) :
    P n ≠ X A := by
  sorry

/-- The affine threshold is never integral. -/
theorem y_nonintegral (A : ℕ) (z : ℤ) :
    y A ≠ z := by
  sorry

/-- Final global bridge, stated using the least-threshold characterization. -/
theorem global_threshold_bridge
    (A T : ℕ)
    (hcross : X A ≤ P T)
    (hminimal : ∀ n < T, P n < X A) :
    T = Nat.ceil (y A) := by
  sorry

end QBLGlobalThreshold
