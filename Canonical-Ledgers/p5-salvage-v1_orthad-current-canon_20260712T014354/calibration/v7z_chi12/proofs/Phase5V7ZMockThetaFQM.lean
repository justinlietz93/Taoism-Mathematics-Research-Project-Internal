import Std

namespace Phase5V7Z

def chi12 : Fin 12 -> Int
| ⟨0, _⟩ => 0
| ⟨1, _⟩ => 1
| ⟨2, _⟩ => 0
| ⟨3, _⟩ => 0
| ⟨4, _⟩ => 0
| ⟨5, _⟩ => -1
| ⟨6, _⟩ => 0
| ⟨7, _⟩ => -1
| ⟨8, _⟩ => 0
| ⟨9, _⟩ => 0
| ⟨10, _⟩ => 0
| ⟨11, _⟩ => 1

-- Table-level theorem surface for the finite chi12 carrier.
theorem chi12_one_pos : chi12 ⟨1, by decide⟩ = 1 := rfl
theorem chi12_five_neg : chi12 ⟨5, by decide⟩ = -1 := rfl
theorem chi12_seven_neg : chi12 ⟨7, by decide⟩ = -1 := rfl
theorem chi12_eleven_pos : chi12 ⟨11, by decide⟩ = 1 := rfl

def qnum24 (r : Nat) : Nat := (r*r) % 24

theorem unit_one_qnum : qnum24 1 = 1 := by decide
theorem unit_five_qnum : qnum24 5 = 1 := by decide
theorem unit_seven_qnum : qnum24 7 = 1 := by decide
theorem unit_eleven_qnum : qnum24 11 = 1 := by decide

theorem mod6_collision_one_seven : (1 % 6 = 7 % 6) := by decide
theorem chi12_separates_one_seven : chi12 ⟨1, by decide⟩ ≠ chi12 ⟨7, by decide⟩ := by decide

end Phase5V7Z
