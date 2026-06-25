namespace Phase3V5Wilhelm

inductive Bit where | zero | one deriving DecidableEq, Repr

open Bit

def flipBit : Bit -> Bit
| zero => one
| one => zero

structure Carrier where
  b1 : Bit
  b2 : Bit
  b3 : Bit
  b4 : Bit
  b5 : Bit
  b6 : Bit
  deriving DecidableEq, Repr

inductive Line where | L1 | L2 | L3 | L4 | L5 | L6 deriving DecidableEq, Repr

open Line

def flipLine : Carrier -> Line -> Carrier
| c, L1 => { c with b1 := flipBit c.b1 }
| c, L2 => { c with b2 := flipBit c.b2 }
| c, L3 => { c with b3 := flipBit c.b3 }
| c, L4 => { c with b4 := flipBit c.b4 }
| c, L5 => { c with b5 := flipBit c.b5 }
| c, L6 => { c with b6 := flipBit c.b6 }

theorem flipBit_involutive (b : Bit) : flipBit (flipBit b) = b := by
  cases b <;> rfl

theorem flipLine_involutive (c : Carrier) (l : Line) : flipLine (flipLine c l) l = c := by
  cases c
  cases l <;> simp [flipLine, flipBit_involutive]

-- Projection-loss witness: carrier-only projection cannot determine the selected-line transition.
def allOnes : Carrier := ⟨one, one, one, one, one, one⟩

theorem carrier_only_projection_loss :
  flipLine allOnes L1 ≠ flipLine allOnes L6 := by
  decide

end Phase3V5Wilhelm
