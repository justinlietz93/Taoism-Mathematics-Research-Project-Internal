import Std

namespace Phase3V4

def valueLsd : List Nat -> Nat
| [] => 0
| d :: rest => d + 8 * valueLsd rest

def succCarry : List Nat -> List Nat
| [] => [1]
| d :: rest =>
  if h : d < 7 then (d+1) :: rest
  else 0 :: succCarry rest

theorem seven_lifts_one : succCarry [7] = [0,1] := by
  native_decide

theorem seventy_seven_lifts_one : succCarry [7,7] = [0,0,1] := by
  native_decide

theorem seven_three_lifts_one : succCarry [7,7,7] = [0,0,0,1] := by
  native_decide

theorem low_digit_projection_loss :
  [7] ≠ [7,7] ∧
  ([7].headD 0 = [7,7].headD 0) ∧
  succCarry [7] ≠ succCarry [7,7] := by
  native_decide

theorem scalar_zero_projection_loss :
  valueLsd [0] = valueLsd [0,0] ∧
  succCarry [0] ≠ succCarry [0,0] := by
  native_decide

end Phase3V4
