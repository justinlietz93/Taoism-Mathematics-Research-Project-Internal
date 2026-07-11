import Mathlib

namespace QBLCarryStructure

-- The full circle-refinement, non-soficity, and mixing arguments remain
-- theorem surfaces in Markdown. This Lean file records only the elementary
-- finite identities used by that argument.

theorem geometric_sum_two (n : ℕ) :
    (∑ k in Finset.range (n + 1), 2 ^ k) = 2 ^ (n + 1) - 1 := by
  induction n with
  | zero => norm_num
  | succ n ih =>
      rw [Finset.sum_range_succ, ih]
      omega

end QBLCarryStructure
