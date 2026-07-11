import Mathlib

open Matrix

namespace QBLCarryJ

/-- One-step Lebesgue joint transition-mass matrix, ordered by carry states 7,8,9. -/
def J (a : ℝ) : Matrix (Fin 3) (Fin 3) ℝ :=
  !![0, (1 - 3 * a) / 2, a / 2;
     (1 - 2 * a) / 4, 1 / 4, a / 2;
     (1 - 2 * a) / 4, 3 * a / 2 - 1 / 4, 0]

variable {a : ℝ} (haL : (1 : ℝ) / 6 < a) (haU : a < (1 : ℝ) / 4)

 theorem J77_zero : J a 0 0 = 0 := by simp [J]
 theorem J99_zero : J a 2 2 = 0 := by simp [J]
 theorem J78_pos : 0 < J a 0 1 := by simp [J]; nlinarith
 theorem J79_pos : 0 < J a 0 2 := by simp [J]; nlinarith
 theorem J87_pos : 0 < J a 1 0 := by simp [J]; nlinarith
 theorem J88_pos : 0 < J a 1 1 := by norm_num [J]
 theorem J89_pos : 0 < J a 1 2 := by simp [J]; nlinarith
 theorem J97_pos : 0 < J a 2 0 := by simp [J]; nlinarith
 theorem J98_pos : 0 < J a 2 1 := by simp [J]; nlinarith

 theorem row7_sum : J a 0 0 + J a 0 1 + J a 0 2 = 1 / 2 - a := by simp [J]; ring
 theorem row8_sum : J a 1 0 + J a 1 1 + J a 1 2 = 1 / 2 := by simp [J]; ring
 theorem row9_sum : J a 2 0 + J a 2 1 + J a 2 2 = a := by simp [J]; ring
 theorem col7_sum : J a 0 0 + J a 1 0 + J a 2 0 = 1 / 2 - a := by simp [J]; ring
 theorem col8_sum : J a 0 1 + J a 1 1 + J a 2 1 = 1 / 2 := by simp [J]; ring
 theorem col9_sum : J a 0 2 + J a 1 2 + J a 2 2 = a := by simp [J]; ring
 theorem total_mass :
    J a 0 0 + J a 0 1 + J a 0 2 +
    J a 1 0 + J a 1 1 + J a 1 2 +
    J a 2 0 + J a 2 1 + J a 2 2 = 1 := by simp [J]; ring

 theorem defect_neg2 : J a 2 0 = (1 - 2 * a) / 4 := by simp [J]
 theorem defect_neg1 : J a 1 0 + J a 2 1 = a := by simp [J]; ring
 theorem defect_zero : J a 0 0 + J a 1 1 + J a 2 2 = 1 / 4 := by norm_num [J]
 theorem defect_pos1 : J a 0 1 + J a 1 2 = 1 / 2 - a := by simp [J]; ring
 theorem defect_pos2 : J a 0 2 = a / 2 := by simp [J]

/-- Pairwise-support edge-shift envelope. This is not the full carry language. -/
def M : Matrix (Fin 3) (Fin 3) ℝ :=
  !![0, 1, 1;
     1, 1, 1;
     1, 1, 0]

 theorem M_sq_entrywise_positive : ∀ i j, 0 < (M * M) i j := by
  intro i j
  fin_cases i <;> fin_cases j <;>
    norm_num [M, Matrix.mul_apply, Fin.sum_univ_succ]

/-- Perron vector of the pairwise edge-shift envelope. -/
def perronVec : Fin 3 → ℝ := ![1, Real.sqrt 2, 1]

 theorem perron_eigenvector :
    M.mulVec perronVec = (1 + Real.sqrt 2) • perronVec := by
  have hs : (Real.sqrt 2) ^ 2 = (2 : ℝ) := by norm_num
  funext i
  fin_cases i <;>
    simp [M, perronVec, Matrix.mulVec, dotProduct, Fin.sum_univ_succ] <;>
    nlinarith

end QBLCarryJ
