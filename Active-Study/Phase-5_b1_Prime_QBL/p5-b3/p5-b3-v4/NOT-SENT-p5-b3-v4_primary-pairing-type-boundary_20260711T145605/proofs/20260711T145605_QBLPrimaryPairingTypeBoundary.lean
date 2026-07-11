import Mathlib

namespace QBLPrimaryPairingTypeBoundary

/-- Architectural rank information forced by the current Orthad law. -/
structure ArchitecturalState where
  rank : Nat

/-- The authority-level L signature only records rank extension and old-structure retention. -/
structure LSignature (r : Nat) where
  newRank : Nat := r + 1
  oldStructureRetained : Prop
  newAxisAppended : Prop

/-- A candidate scalar-module realization. Existence is not asserted by the current authority. -/
structure ScalarPairingRealization (K H V : Type*) [Semiring K]
    [AddCommMonoid H] [Module K H] [AddCommMonoid V] [Module K V] where
  pair : H → H → V
  add_left : ∀ x₁ x₂ y, pair (x₁ + x₂) y = pair x₁ y + pair x₂ y
  add_right : ∀ x y₁ y₂, pair x (y₁ + y₂) = pair x y₁ + pair x y₂

/-- Ordinary and conjugate scalar variance are separate candidate branches. -/
inductive Variance where
  | ordinary
  | conjugate
  deriving DecidableEq

theorem variance_branches_distinct : Variance.ordinary ≠ Variance.conjugate := by decide

/-- Fixed one-dimensional seed coefficient is unique once the type, basis, and normalization are fixed. -/
theorem rankOneSeedCoefficientUnique {K : Type*} [One K] (α : K) (h : α = 1) : α = 1 := h

/-- Conditional old-block preservation theorem. -/
theorem oldBlockPreserved_of_hypothesis
    {H A V : Type*} [Zero H] [Zero A]
    (Pold : H → H → V) (Pnew : (H × A) → (H × A) → V)
    (hOld : ∀ x y, Pnew (x, 0) (y, 0) = Pold x y) :
    ∀ x y, Pnew (x, 0) (y, 0) = Pold x y := hOld

/-- Both mixed blocks vanish only under two explicit orthogonality hypotheses. -/
theorem mixedBlocksZero_of_twoSidedOrthogonality
    {H A V : Type*} [Zero H] [Zero A] [Zero V]
    (Pnew : (H × A) → (H × A) → V)
    (hRight : ∀ x a, Pnew (x, 0) (0, a) = 0)
    (hLeft : ∀ x a, Pnew (0, a) (x, 0) = 0) :
    (∀ x a, Pnew (x, 0) (0, a) = 0) ∧
    (∀ x a, Pnew (0, a) (x, 0) = 0) := ⟨hRight, hLeft⟩

/-- Exact nonsymmetric control: left orthogonality does not imply right orthogonality. -/
def oneSidedMatrix : Matrix (Fin 2) (Fin 2) ℤ :=
  !![1, 1; 0, 2]

theorem oneSided_not_twoSided :
    oneSidedMatrix 1 0 = 0 ∧ oneSidedMatrix 0 1 ≠ 0 := by decide

inductive Primitive where
  | B | Q | L
  deriving DecidableEq, Repr

structure LocalState where
  u : Nat
  v : Nat
  qmod : Fin 4
  deriving DecidableEq, Repr

private def qNext : Fin 4 → Fin 4
  | ⟨0, _⟩ => 1
  | ⟨1, _⟩ => 2
  | ⟨2, _⟩ => 3
  | ⟨3, _⟩ => 0

private def localStep : LocalState → Primitive → LocalState
  | s, Primitive.B => { s with u := s.v, v := s.u + s.v }
  | s, Primitive.Q => { s with qmod := qNext s.qmod }
  | s, Primitive.L => s

private def runWord (s : LocalState) (w : List Primitive) : LocalState :=
  w.foldl localStep s

private def firstWord : List Primitive :=
  [Primitive.B, Primitive.Q, Primitive.Q,
   Primitive.B, Primitive.B, Primitive.B,
   Primitive.Q, Primitive.B, Primitive.Q,
   Primitive.B, Primitive.B, Primitive.Q,
   Primitive.B, Primitive.B, Primitive.L]

private def firstResult : LocalState :=
  runWord { u := 1, v := 1, qmod := 0 } firstWord

theorem firstDomainPairAndQuarter :
    firstResult.u = 55 ∧ firstResult.v = 89 ∧ firstResult.qmod.val = 1 := by
  native_decide

/-- The active denominator is derived from the recursive interpreter. -/
theorem firstDomainActiveDenominator : firstResult.u * firstResult.v = 4895 := by
  native_decide

/-- Open obligations are represented as data, not asserted as completed theorems. -/
structure OpenObligations where
  carrierChosen : Bool
  codomainChosen : Bool
  varianceChosen : Bool
  orthogonalityChosen : Bool
  seedChosen : Bool
  valueRecurrenceChosen : Bool

def currentOpenObligations : OpenObligations :=
  { carrierChosen := false
    codomainChosen := false
    varianceChosen := false
    orthogonalityChosen := false
    seedChosen := false
    valueRecurrenceChosen := false }

#eval currentOpenObligations

end QBLPrimaryPairingTypeBoundary
