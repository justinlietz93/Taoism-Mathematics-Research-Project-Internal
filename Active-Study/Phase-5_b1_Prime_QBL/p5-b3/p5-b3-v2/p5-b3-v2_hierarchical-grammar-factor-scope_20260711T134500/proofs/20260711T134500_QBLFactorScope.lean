import Mathlib

namespace QBLFactorScope

noncomputable section

open Real

/-- Cumulative phase-position index at the canonical pre-L boundary. -/
def J (A : ℕ) : ℕ := 6 * (2^(A+1) - 1)

/-- Exact arithmetic recurrence for the cumulative boundary index. -/
theorem J_succ (A : ℕ) : J (A+1) = 2 * J A + 6 := by
  simp [J, pow_succ]
  omega

/-- Abstract state-internal factor coordinate. -/
def piCoord (lam beta : ℝ) (j b : ℕ) : ℝ := lam * j + beta - b

/-- The boundary cocycle algebra gives the affine recurrence. -/
theorem boundary_factor_step
    (lam beta gamma : ℝ) (j b c : ℕ)
    (hgamma : gamma = 6 * lam - beta) :
    piCoord lam beta (2*j+6) (2*b+c)
      = 2 * piCoord lam beta j b + gamma - c := by
  simp [piCoord, hgamma]
  ring

/-- Surjectivity onto a codomain defined as the image is immediate. -/
theorem image_surjective {α β : Type} (f : α → β) :
    Function.Surjective (fun x : α => (⟨f x, ⟨x, rfl⟩⟩ : Set.range f)) := by
  intro y
  rcases y.property with ⟨x, rfl⟩
  exact ⟨x, rfl⟩

/-- No theorem in this file asserts a factor from a countable canonical orbit onto a real interval. -/

end

end QBLFactorScope
