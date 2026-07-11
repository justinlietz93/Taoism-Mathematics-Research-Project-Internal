# Findings

## Proved abstractly

1. The affine ceiling recurrence gives
   `c_A = ceil(2 E_(A-1) + gamma)` and
   `E_A = 2 E_(A-1) + gamma - c_A` for `A>=1`.
2. The half-open partition and one-step matrices `J` and `P` are exact.
3. `M` is only the pairwise-support envelope.
4. `989` is impossible for every `a<1/4`.
5. At the current constant, `787` is also impossible because `a>3/14`.
6. The affine word complexity is exactly `p(n)=2^(n+1)-1`.
7. The affine coding entropy is exactly `log(2)`.
8. The pairwise envelope entropy is `log(1+sqrt(2))`.

## Certified finitely

1. The imported trace has one row for every `A=0..10000`, every carry lies in `{7,8,9}`, and there are 9999 transitions.
2. The derived transition table exactly matches `PRIOR_TRANSITION_COUNTS.csv`.
3. Direct interval cylinders agree with the complexity theorem through length 12.
4. Outward interval arithmetic certifies all 10000 imported affine carry steps and no boundary hit for `E_A`, `A=0..10000`.
5. Exact finite cylinders disprove Markov orders 1 through 10.

## Observed

1. The finite edge distribution is much closer to `J` than to envelope baseline `K`.
2. Finite state and defect frequencies are close to the Lebesgue benchmarks.

## Open

```text
ACTUAL CARRY LANGUAGE PRESENTATION: NOT YET DERIVED
ACTUAL CARRY LANGUAGE MIXING: NOT YET DERIVED
SPECIFIC-ORBIT EQUIDISTRIBUTION: NOT PROVED
GLOBAL T_A=ceil(y_A) BRIDGE: NOT YET PROVED
GAUGE/FQM MAP FROM d_A=±1: NOT YET DERIVED
```
