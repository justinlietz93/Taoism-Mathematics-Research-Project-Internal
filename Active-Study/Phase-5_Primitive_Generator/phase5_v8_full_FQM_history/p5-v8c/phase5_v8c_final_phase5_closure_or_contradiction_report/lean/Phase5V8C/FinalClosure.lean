/-
Phase 5 v8c theorem surface.
This file attacks the closure gate as a finite status classification object.
It does not claim a universal FQM classifier.
-/

inductive ClosureStatus where
  | closedPositive
  | closedNegative
  | supersededWithExplicitReplacement
  | deferredOutOfPhaseWithReason
  | blockingOpen
  deriving DecidableEq, Repr

structure TargetRow where
  status : ClosureStatus
  hasHardReason : Bool

-- Phase 5 closure gate: no blocking-open rows and every deferral has a hard reason.
def closureRowOK (r : TargetRow) : Bool :=
  match r.status with
  | ClosureStatus.blockingOpen => false
  | ClosureStatus.deferredOutOfPhaseWithReason => r.hasHardReason
  | _ => true

theorem blocking_open_rejects (h : TargetRow) :
  h.status = ClosureStatus.blockingOpen -> closureRowOK h = false := by
  intro hs
  cases h
  simp [closureRowOK] at *
  cases hs
  rfl

theorem deferral_requires_reason (h : TargetRow) :
  h.status = ClosureStatus.deferredOutOfPhaseWithReason -> h.hasHardReason = false -> closureRowOK h = false := by
  intro hs hr
  cases h
  simp [closureRowOK] at *
  cases hs
  simp [hr]
