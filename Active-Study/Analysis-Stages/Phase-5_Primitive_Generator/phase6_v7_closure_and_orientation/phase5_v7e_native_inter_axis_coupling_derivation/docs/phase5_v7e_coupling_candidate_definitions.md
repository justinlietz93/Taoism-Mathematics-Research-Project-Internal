# Coupling Candidate Definitions

## c_boundary / selected v7e extractor

`c_boundary` is read from shared `L`-boundary latch events:

```text
c_boundary = Σ sign_b (q_i(b)+1)(q_j(b)+1) mod lcm(D_i,D_j)
```

where `q_i(b)` and `q_j(b)` are retained Q-depths before the shared latch on each axis.

## c_overlap

Shared prefix overlap without a shared latch is recorded but does not generate cross-axis coupling in v7e.

## c_commutator

Deferred to the next audit. v7e records branch-order controls but does not claim a complete commutator theorem.

## c_transfer

After sealing `c_boundary`, the product-module transfer is built from that native value and tested. It is not used to choose the value.
