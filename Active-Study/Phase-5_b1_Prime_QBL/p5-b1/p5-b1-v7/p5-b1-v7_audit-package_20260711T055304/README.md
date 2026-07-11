# p5-b1-v7 Audit Package

This package audits `p5-b1-v7_affine-follower-set-closure_20260711T103100.zip`.

## Verdict

```text
ADOPT
p5-b1 BRANCH STATUS: CLOSED
```

The audit verifies package integrity, the deterministic clean rebuild, the notebook execution record, the finite exact outputs, and the load-bearing proof steps for the half-open follower bridge, non-soficity, absence of finite Markov order, and topological mixing.

## Run

From this audit-package root:

```bash
python scripts/p5-b1-v7_verify_agent_package.py \
  /mnt/data/p5-b1-v7_affine-follower-set-closure_20260711T103100.zip

python scripts/p5-b1-v7_follower_structure_audit.py \
  /mnt/data/p5-b1-v7_affine-follower-set-closure_20260711T103100.zip
```

Both scripts use only the Python standard library.
