namespace Phase5V7O

structure Latch where
  p : Int
  dc : Int
  dz : Int
deriving Repr, DecidableEq

def alpha (e : Latch) : Int := e.dz - e.p * e.dc

def contactLatch (p dc : Int) : Latch :=
  { p := p, dc := dc, dz := p * dc }

theorem contact_alpha_zero (p dc : Int) :
    alpha (contactLatch p dc) = 0 := by
  unfold alpha contactLatch
  ring

def C_of_two (a b : Int) : Int := a + b
def Z_of_two (a b : Int) : Int := 1*a + 2*b

example : C_of_two 1 5 = C_of_two 5 1 := by decide
example : Z_of_two 1 5 ≠ Z_of_two 5 1 := by decide

end Phase5V7O
