namespace Phase5V7J

def M : Fin 3 -> Fin 3 -> Int
| 0, 0 => -1
| 0, _ => 0
| 1, 2 => 1
| 1, _ => 0
| 2, 1 => 1
| 2, _ => 0

def dotRowCol (A B : Fin 3 -> Fin 3 -> Int) (i j : Fin 3) : Int :=
  Finset.univ.sum (fun k : Fin 3 => A i k * B k j)

theorem M_sq_identity_diag_0 : dotRowCol M M 0 0 = 1 := by decide
theorem M_sq_identity_diag_1 : dotRowCol M M 1 1 = 1 := by decide
theorem M_sq_identity_diag_2 : dotRowCol M M 2 2 = 1 := by decide
theorem M_sq_identity_off_01 : dotRowCol M M 0 1 = 0 := by decide
theorem M_sq_identity_off_02 : dotRowCol M M 0 2 = 0 := by decide
theorem M_sq_identity_off_10 : dotRowCol M M 1 0 = 0 := by decide
theorem M_sq_identity_off_12 : dotRowCol M M 1 2 = 0 := by decide
theorem M_sq_identity_off_20 : dotRowCol M M 2 0 = 0 := by decide
theorem M_sq_identity_off_21 : dotRowCol M M 2 1 = 0 := by decide

theorem full_overlap_split : (1 : Rat) / 2 + (1 : Rat) / 2 = 1 := by norm_num

end Phase5V7J
