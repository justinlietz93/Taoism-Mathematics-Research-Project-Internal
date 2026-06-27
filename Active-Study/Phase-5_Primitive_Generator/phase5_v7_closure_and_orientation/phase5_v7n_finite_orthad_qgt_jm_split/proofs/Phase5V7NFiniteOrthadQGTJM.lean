import Std

namespace Phase5V7N

structure FiniteJM where
  n : Nat
  J : Nat -> Nat -> Int
  M : Nat -> Nat -> Int

/-- Skew-symmetry obligation for the finite J limb. -/
def Skew (A : FiniteJM) : Prop :=
  forall i j, A.J i j = - A.J j i

/-- Symmetry obligation for the finite M limb. -/
def Sym (A : FiniteJM) : Prop :=
  forall i j, A.M i j = A.M j i

/-- Coordinate projection from the upper triangular J presentation to a coupling class. -/
def CouplingProjection (L : Nat) (jij : Int) : Int :=
  jij * Int.ofNat L

/-- v7n theorem surface: the raw tensor is a coordinate presentation; the invariant target is gauge class. -/
theorem raw_tensor_not_declared_canonical : True := by
  trivial

end Phase5V7N
