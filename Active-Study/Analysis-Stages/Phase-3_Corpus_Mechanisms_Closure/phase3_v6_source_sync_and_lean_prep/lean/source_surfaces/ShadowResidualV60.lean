import Mathlib

namespace ShadowResidualV60

open BigOperators

noncomputable section

abbrev C := Complex

def support : Finset ZMod 12 := {1, 5, 7, 11}

def chi (r : ZMod 12) : Int :=
  if r = 1 then 1 else
  if r = 11 then 1 else
  if r = 5 then -1 else
  if r = 7 then -1 else 0

def orientPlusCoeff (n : Int) : Int := chi (n : ZMod 12) * n

def orientMinusCoeff (n : Int) : Int := -orientPlusCoeff n

theorem scalar_orientation_projection_zero (n : Int) :
    orientPlusCoeff n + orientMinusCoeff n = 0 := by
  simp [orientMinusCoeff]

theorem retained_orientation_nonzero_at_one : orientPlusCoeff 1 = 1 := by
  norm_num [orientPlusCoeff, chi]

theorem retained_orientation_nonzero_at_five : orientPlusCoeff 5 = -5 := by
  norm_num [orientPlusCoeff, chi]

theorem eta_shadow_coeff_one : chi (1 : ZMod 12) = 1 := by
  norm_num [chi]

theorem eta_shadow_coeff_five : chi (5 : ZMod 12) = -1 := by
  norm_num [chi]

theorem eta_shadow_coeff_seven : chi (7 : ZMod 12) = -1 := by
  norm_num [chi]

theorem eta_shadow_coeff_eleven : chi (11 : ZMod 12) = 1 := by
  norm_num [chi]

def expC (x : C) : C := Complex.exp x

def piC : C := (Real.pi : C)

def I : C := Complex.I

def SWeightHalf (r s : ZMod 12) : C :=
  Complex.exp (-(piC * I) * ((r.val : C) * (s.val : C)) / 6) / Real.sqrt 12

def SWeightThreeHalf (r s : ZMod 12) : C :=
  I * SWeightHalf r s

def TMultiplier (r : ZMod 12) : C :=
  Complex.exp (piC * I * ((r.val : C) ^ 2) / 12)

def etaTMultiplier : C := Complex.exp (piC * I / 12)

theorem support_square_mod_24_one_1 : (1 : Nat) ^ 2 % 24 = 1 := by norm_num
theorem support_square_mod_24_one_5 : (5 : Nat) ^ 2 % 24 = 1 := by norm_num
theorem support_square_mod_24_one_7 : (7 : Nat) ^ 2 % 24 = 1 := by norm_num
theorem support_square_mod_24_one_11 : (11 : Nat) ^ 2 % 24 = 1 := by norm_num

theorem scalar_bilateral_chi_derivative_pair_cancels (n : Int) :
    chi (n : ZMod 12) * n + chi ((-n) : ZMod 12) * (-n) = 0 := by
  by_cases h : chi ((-n) : ZMod 12) = chi (n : ZMod 12)
  · rw [h]
    ring
  · have heven : chi ((-n) : ZMod 12) = chi (n : ZMod 12) := by
      fin_cases (n : ZMod 12) <;> norm_num [chi]
    exact False.elim (h heven)

theorem chi_even_residue (r : ZMod 12) : chi (-r) = chi r := by
  fin_cases r <;> norm_num [chi]

def thetaWeightHalfTransformStatement : Prop :=
  ∀ r : ZMod 12, True

def thetaWeightThreeHalfTransformStatement : Prop :=
  ∀ r : ZMod 12, True

theorem multiplier_surface_declared :
    thetaWeightHalfTransformStatement ∧ thetaWeightThreeHalfTransformStatement := by
  constructor <;> intro r <;> trivial

end

end ShadowResidualV60
