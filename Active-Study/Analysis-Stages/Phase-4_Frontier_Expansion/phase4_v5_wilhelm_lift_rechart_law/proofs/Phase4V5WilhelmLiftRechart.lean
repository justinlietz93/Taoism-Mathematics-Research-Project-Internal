namespace Phase4V5Wilhelm

inductive Bit where | zero | one deriving DecidableEq, Repr
open Bit

def flipBit : Bit -> Bit
| zero => one
| one => zero

theorem flipBit_involutive (b : Bit) : flipBit (flipBit b) = b := by
  cases b <;> rfl

structure Carrier where
  b1 : Bit -- bottom / line 1
  b2 : Bit
  b3 : Bit
  b4 : Bit
  b5 : Bit
  b6 : Bit -- top / line 6
  deriving DecidableEq, Repr

inductive Line where | L1 | L2 | L3 | L4 | L5 | L6 deriving DecidableEq, Repr
open Line

def step : Carrier -> Line -> Carrier
| c, L1 => { c with b1 := flipBit c.b1 }
| c, L2 => { c with b2 := flipBit c.b2 }
| c, L3 => { c with b3 := flipBit c.b3 }
| c, L4 => { c with b4 := flipBit c.b4 }
| c, L5 => { c with b5 := flipBit c.b5 }
| c, L6 => { c with b6 := flipBit c.b6 }

theorem line6_involutive (c : Carrier) : step (step c L6) L6 = c := by
  cases c
  simp [step, flipBit_involutive]

/-- Line 6 is the top-axis re-chart on the retained six-line carrier. -/
def line6Rechart (c : Carrier) : Carrier := step c L6

theorem line6_rechart_eq_step (c : Carrier) : line6Rechart c = step c L6 := rfl

end Phase4V5Wilhelm
