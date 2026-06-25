import Phase3.Core

namespace Phase3

structure ModularBDomain (Carrier Projection : Type) where
  refine : Carrier -> Carrier
  complete : Carrier -> Bool
  lift : Carrier -> Carrier
  project : Carrier -> Projection

namespace ModularBDomain

def step {Carrier Projection : Type} (D : ModularBDomain Carrier Projection) (x : Carrier) : Carrier :=
  if D.complete x then D.lift x else D.refine x

structure GateReport where
  retainedCarrier : Bool
  localRefinement : Bool
  completionLaw : Bool
  liftLaw : Bool
  projectionDiscipline : Bool
  deriving Repr

def GateReport.pass (g : GateReport) : Bool :=
  g.retainedCarrier && g.localRefinement && g.completionLaw && g.liftLaw && g.projectionDiscipline

end ModularBDomain

end Phase3
