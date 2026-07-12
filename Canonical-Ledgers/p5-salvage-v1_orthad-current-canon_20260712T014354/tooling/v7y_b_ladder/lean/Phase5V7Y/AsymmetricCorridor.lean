import Std

namespace Phase5V7Y

structure Pair where
  u : Int
  v : Int
  deriving DecidableEq, Repr

def B (p : Pair) : Pair := { u := p.v, v := p.u + p.v }

def Binv (p : Pair) : Pair := { u := p.v - p.u, v := p.u }

theorem Binv_B_identity (p : Pair) : Binv (B p) = p := by
  cases p
  simp [B, Binv]

theorem B_Binv_identity_on_image (p : Pair) : B (Binv p) = p := by
  cases p
  simp [B, Binv]

def wedge (p q : Pair) : Int := p.u*q.v - p.v*q.u

theorem wedge_B_flip (p q : Pair) : wedge (B p) (B q) = - wedge p q := by
  cases p
  cases q
  simp [wedge, B]
  ring

end Phase5V7Y
