import Mathlib

open Real

namespace QBLThreshold

/-- Abstract integer-gap sign transfer. This is the load-bearing finite-range implication
    used after the exact Binet identity has been established. -/
theorem integer_gap_sign_transfer
    (P X : ℤ) (L r : ℝ)
    (hdecomp : (P : ℝ) = L + r)
    (hr : |r| < (1 : ℝ) / 4)
    (hne : P ≠ X) :
    (((P : ℝ) > (X : ℝ)) ↔ L > (X : ℝ)) := by
  have hgap : |(P : ℝ) - (X : ℝ)| ≥ 1 := by
    have hz : P - X ≠ 0 := sub_ne_zero.mpr hne
    have habs : |P - X| ≥ 1 := Int.one_le_abs hz
    exact_mod_cast habs
  constructor
  · intro hPX
    have hunit : (P : ℝ) - (X : ℝ) ≥ 1 := by
      have hz : P - X ≥ 1 := by omega
      exact_mod_cast hz
    rw [hdecomp] at hunit
    linarith [abs_lt.mp hr]
  · intro hLX
    by_contra hnot
    have hle : P ≤ X := by exact_mod_cast (not_lt.mp hnot)
    have hunit : (P : ℝ) - (X : ℝ) ≤ -1 := by
      have hz : P - X ≤ -1 := by omega
      exact_mod_cast hz
    rw [hdecomp] at hunit
    linarith [abs_lt.mp hr]

/-- The same hypotheses give a uniform 3/4 separation of the affine leading term. -/
theorem leading_term_separation
    (P X : ℤ) (L r : ℝ)
    (hdecomp : (P : ℝ) = L + r)
    (hr : |r| < (1 : ℝ) / 4)
    (hne : P ≠ X) :
    |L - (X : ℝ)| > (3 : ℝ) / 4 := by
  have hgap : |(P : ℝ) - (X : ℝ)| ≥ 1 := by
    have hz : P - X ≠ 0 := sub_ne_zero.mpr hne
    have habs : |P - X| ≥ 1 := Int.one_le_abs hz
    exact_mod_cast habs
  have hrel : (P : ℝ) - (X : ℝ) = (L - (X : ℝ)) + r := by linarith [hdecomp]
  have htri := abs_sub_abs_le_abs_sub ((P : ℝ) - (X : ℝ)) (L - (X : ℝ))
  have hr' : |((P : ℝ) - (X : ℝ)) - (L - (X : ℝ))| < (1 : ℝ) / 4 := by
    rw [show ((P : ℝ) - (X : ℝ)) - (L - (X : ℝ)) = r by linarith [hdecomp]]
    exact hr
  nlinarith [abs_nonneg (L - (X : ℝ))]

/-- Downstream ceiling implication, stated abstractly so the analytic exponential monotonicity
    and exact Binet identity can be connected without hiding assumptions. -/
theorem threshold_from_ceiling
    (y : ℝ) (T : ℕ)
    (hy : y ∉ Set.range (fun z : ℤ => (z : ℝ)))
    (hT : T = Nat.ceil y) :
    (T : ℤ) > Int.floor y := by
  subst T
  have hlt : y < Nat.ceil y := by
    exact_mod_cast (Nat.lt_ceil.mpr (by
      intro h
      apply hy
      refine ⟨Int.ofNat (Nat.ceil y), ?_⟩
      simpa using h))
  have hf : (Int.floor y : ℝ) ≤ y := Int.floor_le y
  omega

end QBLThreshold
