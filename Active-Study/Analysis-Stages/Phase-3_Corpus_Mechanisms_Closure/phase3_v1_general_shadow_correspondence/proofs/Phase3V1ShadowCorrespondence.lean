namespace Phase3V1

/-
Proof surface for Phase 3 v1.

This file encodes the finite residue/orientation carrier as executable data.
It is intentionally finite: the analytic theta-transform identities are
certified in the companion SymPy/Jupyter sweep, while Lean carries the
state/projection-loss skeleton.
-/

def negResidue (N r : Nat) : Nat :=
  (N - (r % N)) % N

def EvenOrientation (N : Nat) (a : Nat -> Int) : Prop :=
  ∀ r : Nat, a (negResidue N r) = a (r % N)

def BilateralPairContribution (a : Nat -> Int) (N n : Nat) : Int :=
  a (n % N) * Int.ofNat n + a (negResidue N n) * (-Int.ofNat n)

theorem even_orientation_pair_cancels
  (N : Nat) (a : Nat -> Int) (h : EvenOrientation N a) (n : Nat) :
  BilateralPairContribution a N n = 0 := by
  unfold BilateralPairContribution
  have hn : a (negResidue N n) = a (n % N) := h n
  rw [hn]
  ring

structure RetainedCarrier where
  m : Nat
  N : Nat
  orientation : Nat -> Int
  even_orientation : EvenOrientation N orientation

def ScalarProjectionPair (C : RetainedCarrier) (n : Nat) : Int :=
  BilateralPairContribution C.orientation C.N n

theorem retained_even_carrier_scalar_pair_zero
  (C : RetainedCarrier) (n : Nat) :
  ScalarProjectionPair C n = 0 := by
  unfold ScalarProjectionPair
  exact even_orientation_pair_cancels C.N C.orientation C.even_orientation n

/-
Interpretation:
The theorem says the scalar bilateral n-weighted projection cancels
pairwise whenever the retained orientation vector is even. The positive
orientation readout is therefore the surviving channel, not the scalar
bilateral projection.
-/

end Phase3V1
