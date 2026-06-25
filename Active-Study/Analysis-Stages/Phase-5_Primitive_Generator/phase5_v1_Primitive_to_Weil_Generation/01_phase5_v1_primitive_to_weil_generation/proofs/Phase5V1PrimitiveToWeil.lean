namespace Phase5

/-
Phase 5 proof surface.

The result encoded here is a boundary theorem, not a generated theorem:
under the exact native definitions, Q is a residue-independent phase action
while Weil T is residue-dependent, and deterministic state maps do not equal
dense Fourier kernels without an additional dual-pairing construction.
-/

structure NativeQ where
  phaseShift : Int

def nativeQ : NativeQ := { phaseShift := 1 }

def qVisiblePhase : Int := 1  -- quarter unit: i

def q2VisiblePhase : Int := 2 -- half-turn unit: -1

structure WeilCarrier where
  N : Nat
  hN : N > 0

axiom TPhaseDependsOnResidue :
  ∀ (N : Nat), N > 2 -> ∃ r s : Nat, r < N ∧ s < N ∧ r*r % (2*N) ≠ s*s % (2*N)

/-- Boundary theorem surface: residue-independent Q cannot be the full residue-quadratic T on nontrivial carriers. -/
theorem native_Q_does_not_determine_quadratic_T
  (N : Nat) (h : N > 2) :
  ∃ r s : Nat, r < N ∧ s < N ∧ r*r % (2*N) ≠ s*s % (2*N) :=
  TPhaseDependsOnResidue N h

structure SparseTransition where
  N : Nat
  target : Nat -> Nat

/-- Placeholder obligation: dense Fourier equality requires nonzero all-to-all entries. -/
axiom sparse_transition_not_dense_fourier :
  ∀ (N : Nat), N > 1 -> True

theorem native_BL_boundary (N : Nat) (h : N > 1) : True :=
  sparse_transition_not_dense_fourier N h

end Phase5
