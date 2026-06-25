/-- v50 projector hygiene and selector demotion witness surface.
This file is intentionally small: it attacks the claim that visible phase alone
or the old macro T can replace the corrected carried state. -/

structure State where
  A : Nat
  u : Nat
  v : Nat
  theta : Nat
  rank : Nat
  deriving DecidableEq, Repr

def visible (s : State) : Nat := s.theta % 4

def correctedL (s : State) : State :=
  { A := s.A + 1, u := s.u, v := s.v, theta := s.theta + 1, rank := s.rank + 1 }

def oldT (s : State) : State :=
  { A := s.A + 1, u := 1, v := s.A + 1, theta := s.theta + 1, rank := s.rank + 1 }

def nonOrigin : State := { A := 6, u := 55, v := 89, theta := 30, rank := 6 }

theorem visible_not_q_complete :
    ∃ a b : State, visible a = visible b ∧ a.u ≠ b.u := by
  refine ⟨{A:=0,u:=1,v:=1,theta:=0,rank:=1}, {A:=5,u:=55,v:=89,theta:=4,rank:=6}, ?_, ?_⟩
  · rfl
  · decide

theorem correctedL_carries_u : (correctedL nonOrigin).u = nonOrigin.u := by
  rfl

theorem correctedL_carries_v : (correctedL nonOrigin).v = nonOrigin.v := by
  rfl

theorem oldT_does_not_carry_u_on_nonOrigin : (oldT nonOrigin).u ≠ nonOrigin.u := by
  decide
