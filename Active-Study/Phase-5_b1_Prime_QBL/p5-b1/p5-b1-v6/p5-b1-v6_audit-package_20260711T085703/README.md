# p5-b1-v6 Audit Package

This package audits `p5-b1-v6_affine-language-structure_20260711T083401.zip`.

## Verdict

```text
REVISE

AFFINE COMPLEXITY AND ENTROPY: ADOPT
ACTUAL AFFINE LANGUAGE MIXING: ADOPT
FINITE BOUNDARY CERTIFICATE: ADOPT
NON-SOFICITY: WITHHOLD PENDING FOLLOWER-SET BRIDGE
FINITE MARKOV ORDER NONE: WITHHOLD AS DEPENDENT CLAIM
```

The experiment archive, document hash, 57-file manifest, notebook execution, and byte-identical clean rebuild all verify.

The remaining proof gap is exact and local. The document proves that continuation languages of distinct open arcs differ, then states that those open-arc languages are exactly the standard follower sets of boundary-adjacent half-open cylinder words. That endpoint bridge is not proved. The non-soficity theorem is plausible and appears repairable, but it is not closed on the page yet.

## Contents

- `AUDIT_RESULTS.md`: full audit verdict and findings.
- `OUTGOING_INSTRUCTIONS.md`: the `p5-b1-v7` task package.
- `scripts/`: independent package and output verifiers.
- `outputs/`: machine-readable audit results and clean rebuild log.
- `source-extracts/`: the audited document and agent summaries.
- `source-references/`: artifact hashes and provenance.
