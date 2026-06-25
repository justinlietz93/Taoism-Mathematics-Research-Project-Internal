inductive Sign where
  | pos
  | neg
  deriving DecidableEq

open Sign

def planar : Sign -> Nat
  | pos => 0
  | neg => 0

def retainedMoment : Sign -> Int
  | pos => 1
  | neg => -1

theorem planar_collision : planar pos = planar neg := rfl

theorem retained_moment_separates : retainedMoment pos != retainedMoment neg := by decide

structure Branch where
  hz : Int
  hy : Int
  deriving DecidableEq

def pz (s : Branch) : Int := s.hz

def Uy (beta : Int) (s : Branch) : Branch := { hz := s.hz + beta * s.hy, hy := s.hy }

def a : Branch := { hz := 0, hy := 0 }
def b : Branch := { hz := 0, hy := 1 }

theorem same_scalar_projection : pz a = pz b := rfl

theorem scalar_projection_not_complete : pz (Uy 1 a) != pz (Uy 1 b) := by decide
