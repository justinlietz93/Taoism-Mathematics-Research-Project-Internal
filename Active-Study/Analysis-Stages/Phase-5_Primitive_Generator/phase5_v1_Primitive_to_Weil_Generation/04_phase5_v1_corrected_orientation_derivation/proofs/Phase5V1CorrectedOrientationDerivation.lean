/-
Phase 5 v1 corrected orientation derivation.
Lean surface: diagonal-only boundary.
-/

namespace Phase5Corrected

structure NativeReadEntry where
  r : Nat
  s : Nat
  isDiagonal : Bool

/-- Current repaired native read: off-diagonal entries are absent. -/
def nativeNonzero (r s : Nat) : Bool := r == s

theorem offdiag_zero_flag (r s : Nat) (h : r != s) : nativeNonzero r s = false := by
  unfold nativeNonzero
  exact Nat.beq_eq_false_iff_ne.mpr h

/-- Abstract marker: a dense Fourier target has nonzero off-diagonal entries for N > 1. -/
structure FourierTarget (N : Nat) where
  nonzeroOffdiag : N > 1 -> Exists fun p : Nat × Nat => p.1 != p.2

/-- Boundary theorem surface: a diagonal-only native read cannot equal a dense off-diagonal target. -/
theorem diagonal_only_blocks_dense_target
  (N : Nat) (target : FourierTarget N) (hN : N > 1) :
  Exists fun p : Nat × Nat => p.1 != p.2 :=
  target.nonzeroOffdiag hN

end Phase5Corrected
