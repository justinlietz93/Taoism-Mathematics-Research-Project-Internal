import Std

namespace Phase4

structure System where
  S : Type
  P : Type
  E : S -> S
  Pi : S -> P

/-- Custody-admissibility: projected state determines next retained state. -/
def CustodyAdmissible (sys : System) : Prop :=
  ∃ G : sys.P -> sys.S, ∀ x : sys.S, sys.E x = G (sys.Pi x)

/-- Projected quotient-admissibility: projected state determines next projected state. -/
def QuotientAdmissible (sys : System) : Prop :=
  ∃ H : sys.P -> sys.P, ∀ x : sys.S, sys.Pi (sys.E x) = H (sys.Pi x)

/-- Projection-loss witness: same projection, different next retained state. -/
def ProjectionLossWitness (sys : System) (x y : sys.S) : Prop :=
  sys.Pi x = sys.Pi y ∧ sys.E x ≠ sys.E y

theorem projection_loss_blocks_custody
  (sys : System) (x y : sys.S)
  (h : ProjectionLossWitness sys x y) :
  ¬ CustodyAdmissible sys := by
  intro hc
  rcases hc with ⟨G, hG⟩
  rcases h with ⟨hpi, hdiff⟩
  have hx : sys.E x = G (sys.Pi x) := hG x
  have hy : sys.E y = G (sys.Pi y) := hG y
  have hxy : G (sys.Pi x) = G (sys.Pi y) := by rw [hpi]
  have : sys.E x = sys.E y := by
    calc
      sys.E x = G (sys.Pi x) := hx
      _ = G (sys.Pi y) := hxy
      _ = sys.E y := hy.symm
  exact hdiff this

end Phase4
