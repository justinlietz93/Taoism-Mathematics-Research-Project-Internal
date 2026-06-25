/--
NCPhaseGeometryProjectionLossV49.lean

Finite theorem surface for the v49 claim:
visible projection can identify two retained states whose hidden order registers differ.
-/

structure HState where
  m : Int
  n : Int
  omega : Int
  deriving DecidableEq, Repr

def visible (s : HState) : Int × Int :=
  (s.m, s.n)

def h0 : HState := { m := 0, n := 0, omega := 0 }
def h1 : HState := { m := 0, n := 0, omega := 1 }

theorem visible_collision_v49 : visible h0 = visible h1 := by
  rfl

theorem hidden_order_diff_v49 : h0.omega ≠ h1.omega := by
  decide

-- Interpretation: visible equality is not retained-state equality.
-- Terminal projection cannot replace the lifted state when omega participates in custody/readout.
