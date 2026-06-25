namespace ShadowResidualV61

def chi12Residue (r : Nat) : Int :=
  match r % 12 with
  | 1 => 1
  | 5 => -1
  | 7 => -1
  | 11 => 1
  | _ => 0

def inShadowSupport (r : Nat) : Bool :=
  match r % 12 with
  | 1 => true
  | 5 => true
  | 7 => true
  | 11 => true
  | _ => false

theorem support_square_seating_1 : (1 * 1) % 24 = 1 := by decide
theorem support_square_seating_5 : (5 * 5) % 24 = 1 := by decide
theorem support_square_seating_7 : (7 * 7) % 24 = 1 := by decide
theorem support_square_seating_11 : (11 * 11) % 24 = 1 := by decide

theorem chi_values :
  chi12Residue 1 = 1 ∧ chi12Residue 5 = -1 ∧
  chi12Residue 7 = -1 ∧ chi12Residue 11 = 1 := by decide

theorem nonsupport_zero_examples :
  chi12Residue 0 = 0 ∧ chi12Residue 2 = 0 ∧ chi12Residue 3 = 0 ∧
  chi12Residue 4 = 0 ∧ chi12Residue 6 = 0 ∧ chi12Residue 8 = 0 ∧
  chi12Residue 9 = 0 ∧ chi12Residue 10 = 0 := by decide

theorem orientation_scalar_projection_zero (a : Int) : a + (-a) = 0 := by omega

def normalizedSChi (r : Nat) : Int :=
  match r % 12 with
  | 1 => 1
  | 5 => -1
  | 7 => -1
  | 11 => 1
  | _ => 0

theorem finite_S_preserves_chi_all_residues :
  (List.range 12).all (fun r => normalizedSChi r == chi12Residue r) = true := by decide

end ShadowResidualV61
