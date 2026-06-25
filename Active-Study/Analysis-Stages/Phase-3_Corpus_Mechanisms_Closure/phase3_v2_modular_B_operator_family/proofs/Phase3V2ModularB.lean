namespace Phase3V2

structure PhasePair where
  u : Nat
  v : Nat
  deriving Repr, DecidableEq

def phaseB (p : PhasePair) : PhasePair :=
  if p.v <= p.u + p.v then
    { u := p.v, v := p.u + p.v }
  else
    { u := p.u + p.v, v := p.v }

def phaseProduct (p : PhasePair) : Nat := p.u * p.v

example : phaseProduct {u := 1, v := 6} = phaseProduct {u := 2, v := 3} := by
  decide

example : phaseB {u := 1, v := 6} = {u := 6, v := 7} := by
  decide

example : phaseB {u := 2, v := 3} = {u := 3, v := 5} := by
  decide

example : phaseB {u := 1, v := 6} != phaseB {u := 2, v := 3} := by
  decide

structure YiState where
  d0 : Nat
  d1 : Nat
  d2 : Nat
  len : Nat
  deriving Repr, DecidableEq

def yiValue (s : YiState) : Nat := s.d0 + 8 * s.d1 + 64 * s.d2

def yiSucc3 (s : YiState) : YiState :=
  if s.d0 < 7 then
    { s with d0 := s.d0 + 1 }
  else if s.d1 < 7 then
    { s with d0 := 0, d1 := s.d1 + 1 }
  else if s.d2 < 7 then
    { s with d0 := 0, d1 := 0, d2 := s.d2 + 1 }
  else
    { d0 := 0, d1 := 0, d2 := 0, len := s.len + 1 }

example : yiSucc3 {d0 := 7, d1 := 0, d2 := 0, len := 1} = {d0 := 0, d1 := 1, d2 := 0, len := 1} := by
  decide

example : yiSucc3 {d0 := 7, d1 := 7, d2 := 0, len := 2} = {d0 := 0, d1 := 0, d2 := 1, len := 2} := by
  decide

example : yiValue {d0 := 0, d1 := 0, d2 := 0, len := 1} = yiValue {d0 := 0, d1 := 0, d2 := 0, len := 2} := by
  decide

example : yiSucc3 {d0 := 0, d1 := 0, d2 := 0, len := 1} != yiSucc3 {d0 := 0, d1 := 0, d2 := 0, len := 2} := by
  decide

structure WilhelmState where
  bits : Nat
  selectedLine : Nat
  deriving Repr, DecidableEq

def wilhelmNext (s : WilhelmState) : Nat :=
  if s.bits = 63 ∧ s.selectedLine = 1 then 62
  else if s.bits = 63 ∧ s.selectedLine = 6 then 31
  else s.bits

example : ({ bits := 63, selectedLine := 1 } : WilhelmState).bits = ({ bits := 63, selectedLine := 6 } : WilhelmState).bits := by
  decide

example : wilhelmNext { bits := 63, selectedLine := 1 } != wilhelmNext { bits := 63, selectedLine := 6 } := by
  decide

structure ModularBDomain where
  Carrier : Type
  refine : Carrier -> Carrier
  project : Carrier -> Nat

structure ProjectionLossWitness (D : ModularBDomain) where
  x : D.Carrier
  y : D.Carrier
  sameProjection : D.project x = D.project y
  differentNext : D.refine x != D.refine y

end Phase3V2
