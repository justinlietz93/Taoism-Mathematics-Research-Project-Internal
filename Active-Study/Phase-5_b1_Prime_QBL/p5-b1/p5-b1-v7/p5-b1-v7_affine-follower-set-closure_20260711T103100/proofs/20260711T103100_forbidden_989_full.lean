import Mathlib

namespace QBLCarry989

open Real

def I7 (a x : ℝ) : Prop := -1 < x ∧ x ≤ -(1 / 2 : ℝ) - a
def I8 (a x : ℝ) : Prop := -(1 / 2 : ℝ) - a < x ∧ x ≤ -a
def I9 (a x : ℝ) : Prop := -a < x ∧ x ≤ 0

def F7 (a x : ℝ) : ℝ := 2 * x + 1 + 2 * a
def F8 (a x : ℝ) : ℝ := 2 * x + 2 * a
def F9 (a x : ℝ) : ℝ := 2 * x - 1 + 2 * a

def Realizes98 (a x : ℝ) : Prop := I9 a x ∧ I8 a (F9 a x)

theorem prefix98_current_bounds
    {a x : ℝ}
    (ha : a < 1 / 4)
    (h98 : Realizes98 a x) :
    -(1 / 2 : ℝ) - a < F9 a x ∧ F9 a x ≤ -1 + 2 * a := by
  rcases h98 with ⟨hx9, hnext8⟩
  rcases hx9 with ⟨hxlo, hxhi⟩
  rcases hnext8 with ⟨h8lo, h8hi⟩
  constructor
  · exact h8lo
  · dsimp [F9] at *
    linarith

theorem image98_upper_bound
    {a x : ℝ}
    (ha : a < 1 / 4)
    (h98 : Realizes98 a x) :
    F8 a (F9 a x) ≤ -2 + 6 * a := by
  have h := (prefix98_current_bounds ha h98).2
  dsimp [F8] at *
  linarith

theorem image98_left_of_I9
    {a x : ℝ}
    (ha : a < 1 / 4)
    (h98 : Realizes98 a x) :
    F8 a (F9 a x) < -a := by
  have h := image98_upper_bound ha h98
  linarith

theorem forbidden_989
    {a x : ℝ}
    (ha_lo : 1 / 6 < a)
    (ha_hi : a < 1 / 4)
    (h98 : Realizes98 a x) :
    ¬ I9 a (F8 a (F9 a x)) := by
  intro h9
  have hleft := image98_left_of_I9 ha_hi h98
  exact (not_lt_of_ge h9.1.le) hleft

end QBLCarry989
