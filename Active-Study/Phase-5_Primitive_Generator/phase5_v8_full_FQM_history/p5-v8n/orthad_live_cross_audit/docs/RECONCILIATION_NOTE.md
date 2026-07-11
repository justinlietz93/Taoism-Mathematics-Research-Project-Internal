# ORTHAD_LIVE — Cross-Audit Reconciliation and Reversal

Date: 2026-07-10
First auditor: Claude (this relay). Second auditor: Codex 5.6 (independent,
with filesystem access to the canon documents). This note reverses the first
auditor's ADOPT verdict after independently replicating every decisive
experiment in the second audit.

## Corrected verdict: REJECT_COMPLETION / RETAIN_SCAFFOLD

The Canon First Experiment is NOT completed. The package is retained as a
same-chart cusp scaffold plus a correct finite chi12 identity.

## Replication results (all confirm the second audit)

E1 PAIR ABLATION. Replacing (34,55) with (1,1), (2,3), (100,101): character
   survival is 12/12 in every case. The crossing pair is not load-bearing.
E2 B ABLATION. The floor field is bit-identical with or without applying B
   (apply_floor never reads the state argument).
E3 RETAINED-BIT CORRUPTION. Corrupting the stored orientation bit for n=7
   yields 12/12 anyway — apply_floor recomputes the bit from term_n, so the
   corruption is silently repaired. The retained state is not consulted.
E4 EVIDENCE FALSIFICATION. Changing the far-side n=1 character from +1 to -1
   in the after CSV and re-running the package's own verifier still emits
   global_pass=true, zero gate failures: the survival gate trusts the CSV's
   precomputed booleans instead of recomputing from before/after evidence.
E5 PROOF ARTIFACTS. TransportSurvival.lean proves only
   seatCharacter(postSeat n) = chi12 n for 12 values by native_decide — no
   B, no L, no lifted state, no transport relation. The notebook constructs
   post_seats = n%12 inline and prints "i/4895" and "BL" as literals.

Net: the proved relation is n%6 + 6*((n%12)//6) = n%12 — a definitional
identity independent of B and L — plus the correct finite chi12 table. The
canon's Orthad (the lens matrix Omega, built tick-by-tick, "every entry the
forced consequence of the word" — canon v0.6.7 §6b) does not appear in the
code at all. ORTHAD_LIVE was an unearned name.

## First-audit failure accounting (exact, per check)

A1 WRONG TEETH. The first audit's adversarial probes corrupted the injected
   character and the floor RULE, proving the meta COMPARATOR can
   discriminate. They never ablated the claimed CAUSE (B, L, the pair, the
   retained bit). A comparator with teeth attached to a causally inert
   pipeline still certifies nothing. The first audit even recorded the
   mechanism correctly ("orientation bit recomputed from term_n... inverts
   a definition") and then adopted anyway — a described defect was
   normalized instead of weighed.
A2 LABEL-CHECKING PASSED AS STRUCTURE. "Readout domain from lift" was
   verified as absence-of-external-argument plus the package's own
   origin="lift_output" label — the same self-attestation class rejected in
   v8j. The canon requires the domain be FORCED BY THE ACCRUED WORD; a
   constant installed at empty word fails that on its face.
A3 NAMED OBJECT NOT CHECKED FOR EXISTENCE (P1). The ledger's naming
   registry — which this auditor custodians — defines the Orthad as an
   overset dual-lens system / word-built lens matrix. The audit verified
   LAW compliance of what the code contained without asking whether the
   named object was present. It is not.
A4 PROOF ARTIFACTS UNOPENED. The 200-byte Lean file and the notebook were
   not read. The Lean file's NAME claims transport; its theorem is a table
   lookup.
A5 VERIFIER NOT TESTED AGAINST EVIDENCE. The first audit checked the
   shipped evidence was internally consistent but never asked whether the
   verifier BINDS to evidence (E4 shows it does not). Rule 6 (GATE_TEETH)
   as first written was under-specified; the second audit's ablation
   standard is the correct form.

Convergent findings (both audits, independently): the vacuous LAW 0 lexeme
regex; magnitude/exponent survival being carried-by-copy. First-audit
contributions that stand: chi12 = (12|n) verified to n=120 from scratch;
Fibonacci/axis arithmetic; LAW 0b separation; deterministic reproduction of
outputs; artifact-of-record SHA (2697cb74..., which the second auditor could
not check); the agent-authored "canon v1.0" draft flagged as PROPOSAL
(authority ruling stands).

## New standing rule

RULE 7 — LOAD_BEARING_ABLATION. Any claim of the form "X survives / is
preserved through T" must ship ablation controls in which T is removed or
replaced (delete each event; replace the frame; corrupt each piece of
retained state) and the gate MUST fail under every ablation. A result that
survives ablation of its claimed cause is circular. This subsumes and
sharpens rule 6: comparator teeth are necessary but not sufficient.

## Commission-ambiguity repair (owned by the first auditor)

The forwarded commission said "inject the true (12|n)*n Shadow Residual."
The canon's Follow discipline requires the residual to remain an EXTERNAL
reference: the field must be generated solely from carried Orthad state and
word, and compared against the true law only in the meta layer. The corrected
commission adopts the second auditor's formulation.

## Meta-lesson

The two-auditor structure worked exactly as a Germinal constraint should:
the audits converged where the evidence was shared and diverged precisely
where one auditor lacked the canon documents and normalized a defect it had
itself described. Multi-auditor cross-checking is adopted as standing
practice where available; canon-bearing packages must embed the canon text
they claim to implement so no auditor is blind to the spec.
