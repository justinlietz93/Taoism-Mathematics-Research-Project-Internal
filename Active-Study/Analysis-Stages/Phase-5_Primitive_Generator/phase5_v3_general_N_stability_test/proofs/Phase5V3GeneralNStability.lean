import Std

namespace Phase5V3

/-- Carrier size. In the canonized Gauss self-twist law this is even: N = 2m. -/
def EvenCarrier (N : Nat) : Prop := N % 2 = 0 ∧ N > 0

/-- Symbolic Fourier transfer entry. The complex analytic semantics are attacked in SymPy/Jupyter. -/
def FourierEntry (N r s : Nat) : String := "N^(-1/2) * exp(-2*pi*i*r*s/N)"

/-- Symbolic Gauss self-twist entry. -/
def GaussEntry (N r : Nat) : String := "exp(pi*i*r^2/N)"

/-- Canonical gate: the Phase 5 v3 Gauss self-twist canon is asserted only for even cyclic carriers. -/
theorem odd_boundary_gate (N : Nat) (h : N % 2 = 1) : ¬ EvenCarrier N := by
  intro hc
  exact Nat.mod_two_not_eq_one_of_mod_eq_zero hc.left h

end Phase5V3
