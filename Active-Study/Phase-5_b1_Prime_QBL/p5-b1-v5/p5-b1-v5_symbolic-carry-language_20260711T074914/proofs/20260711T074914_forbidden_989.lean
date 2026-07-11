import Mathlib

namespace QBLForbidden989

/-- After the prefix 9→8, the current point lies at most at -1+2a.
    Applying F8(x)=2x+2a then lands strictly left of -a when a<1/4. -/
theorem image_after_98_misses_I9
    {a x : ℝ}
    (ha : a < (1 : ℝ) / 4)
    (hx : x ≤ -1 + 2 * a) :
    2 * x + 2 * a < -a := by
  nlinarith

/-- Therefore no point in the 9→8 cylinder can satisfy the defining lower
    inequality for the next symbol 9. -/
theorem forbidden_989
    {a x : ℝ}
    (ha : a < (1 : ℝ) / 4)
    (hx : x ≤ -1 + 2 * a) :
    ¬ (-a < 2 * x + 2 * a ∧ 2 * x + 2 * a ≤ 0) := by
  intro h
  have hleft := image_after_98_misses_I9 ha hx
  linarith

end QBLForbidden989
