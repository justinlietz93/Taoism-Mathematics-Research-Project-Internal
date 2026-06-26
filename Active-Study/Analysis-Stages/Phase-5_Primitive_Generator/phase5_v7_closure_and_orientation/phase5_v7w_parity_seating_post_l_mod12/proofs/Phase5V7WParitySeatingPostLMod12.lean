namespace Phase5V7W

def chi12 (n : Nat) : Int :=
  match n % 12 with
  | 1 => 1
  | 5 => -1
  | 7 => -1
  | 11 => 1
  | _ => 0

def seat6 (n : Nat) : Nat := n % 6

def parityLatch (n : Nat) : Nat := (n % 12) / 6

def seat12FromLatch (n : Nat) : Nat := seat6 n + 6 * parityLatch n

theorem pre_l_collision_1_7 : seat6 1 = seat6 7 := by native_decide

theorem post_l_separates_1_7 : seat12FromLatch 1 ≠ seat12FromLatch 7 := by native_decide

theorem chi12_1_pos : chi12 1 = 1 := by native_decide

theorem chi12_7_neg : chi12 7 = -1 := by native_decide

theorem post_l_1 : seat12FromLatch 1 = 1 := by native_decide

theorem post_l_7 : seat12FromLatch 7 = 7 := by native_decide

theorem mod6_obstruction_pair_1_7 : seat6 1 = seat6 7 ∧ chi12 1 ≠ chi12 7 := by native_decide

end Phase5V7W
