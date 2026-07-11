universe u v w

namespace QBLPPGRL

structure PlacementArchitecture where
  Ambient : Type u
  PlusArg : Type v
  MinusArg : Type v
  iotaPlus : PlusArg -> Ambient
  iotaMinus : MinusArg -> Ambient

structure PairingPresentation (A : PlacementArchitecture) where
  Value : Type w
  eval : A.Ambient -> A.Ambient -> Value

def restrictPlusPlus (A : PlacementArchitecture) (P : PairingPresentation A) :
    A.PlusArg -> A.PlusArg -> P.Value :=
  fun x y => P.eval (A.iotaPlus x) (A.iotaPlus y)

def restrictPlusMinus (A : PlacementArchitecture) (P : PairingPresentation A) :
    A.PlusArg -> A.MinusArg -> P.Value :=
  fun x y => P.eval (A.iotaPlus x) (A.iotaMinus y)

def restrictMinusPlus (A : PlacementArchitecture) (P : PairingPresentation A) :
    A.MinusArg -> A.PlusArg -> P.Value :=
  fun x y => P.eval (A.iotaMinus x) (A.iotaPlus y)

def restrictMinusMinus (A : PlacementArchitecture) (P : PairingPresentation A) :
    A.MinusArg -> A.MinusArg -> P.Value :=
  fun x y => P.eval (A.iotaMinus x) (A.iotaMinus y)

theorem restriction_extensional
    (A : PlacementArchitecture) (P Q : PairingPresentation A)
    (h : P.eval = Q.eval) :
    restrictPlusPlus A P = restrictPlusPlus A Q := by
  cases P
  cases Q
  simp_all [restrictPlusPlus]

theorem placed_difference_survives
    (A : PlacementArchitecture) (P Q : PairingPresentation A)
    (x y : A.PlusArg)
    (h : P.eval (A.iotaPlus x) (A.iotaPlus y) !=
         Q.eval (A.iotaPlus x) (A.iotaPlus y)) :
    restrictPlusPlus A P x y != restrictPlusPlus A Q x y := by
  exact h

structure OldNewArchitecture where
  Old : Type u
  New : Type u
  Extended : Type u
  oldIn : Old -> Extended
  newIn : New -> Extended

structure OldNewPairing (A : OldNewArchitecture) where
  OldValue : Type v
  NewValue : Type v
  oldPair : A.Old -> A.Old -> OldValue
  extendedPair : A.Extended -> A.Extended -> NewValue
  carryValue : OldValue -> NewValue
  oldOldRetention : forall x y,
    extendedPair (A.oldIn x) (A.oldIn y) = carryValue (oldPair x y)

theorem old_old_is_actual_retention
    (A : OldNewArchitecture) (P : OldNewPairing A) (x y : A.Old) :
    P.extendedPair (A.oldIn x) (A.oldIn y) = P.carryValue (P.oldPair x y) := by
  exact P.oldOldRetention x y

inductive Primitive where
  | B | Q | L

structure CustodyState where
  wordLength : Nat
  canB : Bool
  canQ : Bool

def custodySelect (x : CustodyState) : Primitive :=
  if x.canB then Primitive.B else if x.canQ then Primitive.Q else Primitive.L

theorem custody_only_selection (x y : CustodyState)
    (hB : x.canB = y.canB) (hQ : x.canQ = y.canQ) :
    custodySelect x = custodySelect y := by
  simp [custodySelect, hB, hQ]

end QBLPPGRL
