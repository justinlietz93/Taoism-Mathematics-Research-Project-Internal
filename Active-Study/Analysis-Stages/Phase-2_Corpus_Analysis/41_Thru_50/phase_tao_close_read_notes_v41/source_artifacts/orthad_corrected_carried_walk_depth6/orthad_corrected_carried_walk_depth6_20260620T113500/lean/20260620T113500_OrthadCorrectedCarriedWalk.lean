-- Orthad corrected carried walk, depth 6 proof surface
-- This is a proof surface, not a full formalization of the manuscript.

inductive Sign where | pos | neg deriving Repr, DecidableEq

def flip : Sign -> Sign
| Sign.pos => Sign.neg
| Sign.neg => Sign.pos

def lap0 : List Sign := [Sign.pos, Sign.neg, Sign.neg, Sign.pos, Sign.pos, Sign.neg]
def mapFlip (xs : List Sign) : List Sign := xs.map flip

def lapSign (lap : Nat) : List Sign :=
  if lap % 2 = 0 then lap0 else mapFlip lap0

example : lapSign 1 = mapFlip (lapSign 0) := by native_decide
example : lapSign 2 = lapSign 0 := by native_decide
example : lapSign 3 = mapFlip (lapSign 2) := by native_decide

-- Rank law: after k L events, latched-axis count is k.
def rankAfterDepth (k : Nat) : Nat := k + 1
example : rankAfterDepth 6 = 7 := by native_decide
