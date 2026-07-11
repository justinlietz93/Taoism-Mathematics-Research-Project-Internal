import Std

namespace CanonFirst

structure PairState where
  u : Nat
  v : Nat


def refine (p : PairState) : PairState :=
  { u := p.v, v := p.u + p.v }


def floorBit (p : PairState) : Nat :=
  let q := refine p
  (q.u * q.v) % 2


def shift6 (p : PairState) : Nat :=
  let q := refine p
  (q.u + q.v) % 6


def phaseOrientation (seat : Nat) : Int :=
  match seat % 6 with
  | 1 => 1
  | 2 => 1
  | 4 => -1
  | 5 => -1
  | _ => 0


def floorOrientation (p : PairState) (seat : Nat) : Int :=
  if seat % 2 = floorBit p then
    phaseOrientation ((seat + shift6 p) % 6)
  else
    0


def lapSign (hand : Nat) : Int :=
  if hand % 2 = 0 then 1 else -1


def carrierResidue (p : PairState) (seat hand : Nat) : Nat :=
  (seat + 6 * (hand % 2) + shift6 p) % 12


def transportedCharacter (p : PairState) (seat hand : Nat) : Int :=
  floorOrientation p seat * lapSign hand


def chi12Residue (r : Nat) : Int :=
  match r % 12 with
  | 1 => 1
  | 5 => -1
  | 7 => -1
  | 11 => 1
  | _ => 0


def targetPair : PairState := { u := 34, v := 55 }


def targetRelation : Bool :=
  (List.range 6).all fun seat =>
    (List.range 2).all fun hand =>
      transportedCharacter targetPair seat hand =
        chi12Residue (carrierResidue targetPair seat hand)


theorem target_relation_holds : targetRelation = true := by
  native_decide


theorem refined_pair_is_55_89 : refine targetPair = { u := 55, v := 89 } := by
  rfl


theorem pair_1_1_control_fails :
    transportedCharacter { u := 1, v := 1 } 1 0 ≠
      chi12Residue (carrierResidue { u := 1, v := 1 } 1 0) := by
  native_decide


theorem pair_100_101_control_fails :
    transportedCharacter { u := 100, v := 101 } 1 0 ≠
      chi12Residue (carrierResidue { u := 100, v := 101 } 1 0) := by
  native_decide


theorem severed_transfer_control_fails :
    (0 : Int) ≠ chi12Residue (carrierResidue targetPair 1 0) := by
  native_decide

end CanonFirst
