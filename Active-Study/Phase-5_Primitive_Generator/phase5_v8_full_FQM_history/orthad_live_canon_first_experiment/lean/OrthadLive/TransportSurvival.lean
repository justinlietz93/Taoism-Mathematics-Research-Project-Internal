namespace OrthadLive

def chi12 (n : Nat) : Int :=
  if Nat.gcd n 6 != 1 then 0
  else if n % 12 = 1 ∨ n % 12 = 11 then 1 else -1


def preSeat (n : Nat) : Nat := n % 6

def orientationBit (n : Nat) : Nat := (n % 12) / 6

def postSeat (n : Nat) : Nat := preSeat n + 6 * orientationBit n


def seatCharacter (seat : Nat) : Int :=
  if seat = 1 ∨ seat = 11 then 1
  else if seat = 5 ∨ seat = 7 then -1
  else 0


def channelSurvives (n : Nat) : Bool :=
  decide (seatCharacter (postSeat n) = chi12 n)


def firstPeriodSurvives : Bool :=
  (List.range 12).all (fun seat => channelSurvives (if seat = 0 then 12 else seat))


theorem first_period_survives : firstPeriodSurvives = true := by
  native_decide

end OrthadLive
