import Std

namespace Phase5V7X

def chi12 (n : Nat) : Int :=
  let r := n % 12
  if r == 1 || r == 11 then 1
  else if r == 5 || r == 7 then -1
  else 0

def support (n : Nat) : Bool :=
  Nat.gcd n 6 == 1

def preLSeat (n : Nat) : Nat := n % 6

def parityLatch (n : Nat) : Nat := (n % 12) / 6

def postLSeat (n : Nat) : Nat := preLSeat n + 6 * parityLatch n

def lapSign (lap n : Nat) : Int :=
  if lap % 2 == 1 then chi12 n else -(chi12 n)

example : preLSeat 1 = preLSeat 7 := by native_decide
example : postLSeat 1 ≠ postLSeat 7 := by native_decide
example : chi12 1 = 1 := by native_decide
example : chi12 7 = -1 := by native_decide
example : lapSign 2 7 = -(lapSign 1 7) := by native_decide

example :
  (List.range 256).all (fun n =>
    if support n then lapSign 2 n == -(lapSign 1 n) else true) = true := by
  native_decide

end Phase5V7X
