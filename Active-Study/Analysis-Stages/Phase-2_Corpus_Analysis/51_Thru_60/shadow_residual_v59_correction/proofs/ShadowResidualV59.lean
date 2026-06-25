namespace ShadowResidualV59

inductive Orientation where
  | plus
  | minus
  deriving DecidableEq, Repr

open Orientation

def chi12Residue (r : Fin 12) : Int :=
  if r.val = 1 ∨ r.val = 11 then 1
  else if r.val = 5 ∨ r.val = 7 then -1
  else 0

def orientedNWeight (o : Orientation) (r : Fin 12) : Int :=
  match o with
  | plus => chi12Residue r * r.val
  | minus => -(chi12Residue r * r.val)

def orientedShadowWeight (_o : Orientation) (r : Fin 12) : Int :=
  chi12Residue r

theorem pair_cancel (r : Fin 12) :
    orientedNWeight plus r + orientedNWeight minus r = 0 := by
  simp [orientedNWeight]

theorem scalar_bilateral_derivative_zero_on_residue_pairs :
    (orientedNWeight plus ⟨1, by decide⟩ + orientedNWeight minus ⟨1, by decide⟩) +
    (orientedNWeight plus ⟨5, by decide⟩ + orientedNWeight minus ⟨5, by decide⟩) +
    (orientedNWeight plus ⟨7, by decide⟩ + orientedNWeight minus ⟨7, by decide⟩) +
    (orientedNWeight plus ⟨11, by decide⟩ + orientedNWeight minus ⟨11, by decide⟩) = 0 := by
  decide

theorem positive_half_nonzero_first_term :
    orientedNWeight plus ⟨1, by decide⟩ = 1 := by
  decide

theorem eta_shadow_first_four_residues :
    orientedShadowWeight plus ⟨1, by decide⟩ = 1 ∧
    orientedShadowWeight plus ⟨5, by decide⟩ = -1 ∧
    orientedShadowWeight plus ⟨7, by decide⟩ = -1 ∧
    orientedShadowWeight plus ⟨11, by decide⟩ = 1 := by
  decide

theorem orientation_is_required :
    orientedNWeight plus ⟨5, by decide⟩ ≠ orientedNWeight minus ⟨5, by decide⟩ := by
  decide

theorem scalar_zero_does_not_imply_channel_zero :
    orientedNWeight plus ⟨1, by decide⟩ + orientedNWeight minus ⟨1, by decide⟩ = 0 ∧
    orientedNWeight plus ⟨1, by decide⟩ ≠ 0 := by
  decide

end ShadowResidualV59
