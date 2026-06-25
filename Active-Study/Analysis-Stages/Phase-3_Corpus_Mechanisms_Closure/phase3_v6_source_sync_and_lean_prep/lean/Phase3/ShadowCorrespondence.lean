import Phase3.Core

namespace Phase3
namespace ShadowCorrespondence

structure FiniteQuadraticCarrier where
  modulus : Nat
  tPhase : Nat -> String
  sKernel : Nat -> Nat -> String
  deriving Repr

structure UnaryShadowCase where
  name : String
  m : Nat
  evenOrientation : Bool
  scalarProjectionCancels : Bool
  retainedPositiveReadoutNonzero : Bool
  coefficientStrippedShadow : Bool
  deriving Repr

def casePass (c : UnaryShadowCase) : Bool :=
  c.evenOrientation && c.scalarProjectionCancels &&
  c.retainedPositiveReadoutNonzero && c.coefficientStrippedShadow

-- Phase 3 v1/v62/v61 theorem target:
-- T_r = exp(pi*i*r^2/(2m)); S_rs = (2m)^(-1/2) exp(-pi*i*r*s/m).

end ShadowCorrespondence
end Phase3
