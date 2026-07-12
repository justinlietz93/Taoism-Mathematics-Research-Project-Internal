# p5-b3-v10 Agent Instructions

[CURRENT STATE]

Use `QBL_PRIMITIVE_CUSTODY_AND_ORTHAD_LAW_v2.md` as the primary authority.

Keep the accepted coupled retained state:

```text
Xhat_t =
(
    X_t,
    P_t,
    Omega_t_plus,
    Omega_t_minus,
    T_t_plus_to_minus,
    T_t_minus_to_plus
).
```

Custody alone selects the primitive through strict `B > Q > L`.

The selected primitive mutates the complete coupled retained state.

One primary pairing generates both chart restrictions and both directed transfers.

A bare equation `D = R(P)` is vacuous when `R` may encode an independently chosen target.

The pointwise formula

```text
D_ab(x,y) = P(iota_a(x), iota_b(y))
```

is an admissible non-smuggling realization. It is not yet the intrinsic QBL law.

Do not assume that argument and placement data exist before the primary pairing.

Do not introduce an independent architecture input that is absent from the retained state.

Keep `P_t` as retained state. Do not call it a cache unless reconstructibility from custody and exact history is proved.

Keep the Domain-0 scalar trace scoped to the completed old axis.

[STRATEGIC QUESTION]

Determine whether the authority forces argument and placement data before the primary pairing, derives them from the primary pairing, or generates them jointly with it.

Then locate the first exact unresolved edge at the initial state and first lawful `B` transition.

Propose a stronger route if these three cases do not exhaust the source-forced possibilities.

[REASONING TASK]

1. Reassess the dependency order.

   Compare these cases:

   ```text
   A. placements are generated before P_t;
   B. placements are derived from or contained in P_t;
   C. P_t and placements are jointly generated from retained state.
   ```

   Determine which cases are licensed by the primary authority.

   Give the exact authority clause for every accepted or rejected case.

   Report: `PAIRING_PLACEMENT_ORDER.md`.

2. Test every proposed architecture input against retained-state closure.

   For any object called `A_t`, `H_t`, `C_t`, or `iota_t`, determine how it is computed from the accepted retained state and exact word.

   Accept one of these outcomes only:

   ```text
   derived from retained state;
   internal structure of P_t;
   jointly generated with P_t;
   or exact proof that the retained state is incomplete.
   ```

   Do not pass an unlisted architecture object into the generator as an independent input.

   Report: the exact source of every input to the pairing update.

3. Separate the anti-smuggling theorem from the chosen realization.

   State a representation-neutral requirement that guarantees descendants cannot encode independent target values.

   Show that pointwise placement evaluation satisfies that requirement.

   Determine whether another lawful realization can also satisfy it.

   Do not report the pointwise formula as the unique or intrinsic QBL interface unless uniqueness is proved.

   Report: `NONSMUGGLING_REQUIREMENT.md`.

4. Determine the lawful role of retained `P_t`.

   Assess whether the next primary pairing may depend on `P_t` as retained state.

   Determine whether `P_t` is reconstructible from custody state and exact word alone.

   Require an all-prefix reconstruction proof before treating `P_t` as a cache.

   Report: `PRIMARY_RETENTION_ROLE.md`.

5. Apply the resulting dependency law to the exact initial state.

   Work from the accepted initial custody state and the first lawful `B` step.

   Determine whether the state forces:

   ```text
   P_0;
   the initial chart-access data;
   P_1 after B;
   the four descendants induced at that prefix.
   ```

   Do not move to `Q`, `L`, star semantics, or later domains in this pass.

6. End with exactly one result.

   ```text
   A. INITIAL PAIRING AND FIRST-B ACTION DERIVED

      Give P_0, the lawful chart-access construction, P_1, and all four
      induced descendants.

   B. PAIRING-FIRST OR JOINT GENERATION ORDER DERIVED

      Give the exact dependency theorem and the next concrete edge.

   C. FIRST MISSING RETAINED DATUM IDENTIFIED

      Name one exact datum.
      Show where the derivation stops.
      Prove that it is absent from the accepted retained state and authority.

   D. TRUE INDEPENDENCE AT THE INITIAL/FIRST-B STEP

      Give two complete lawful initial and first-B models.
      Make them agree on every accepted retained input.
      Prove that they are not coordinate-equivalent.
   ```

   A list of possible types is not a result.

   A new umbrella name is not a result.

7. Report these statuses separately.

   ```text
   POINTWISE PLACEMENT FACTORIZATION:
   REPRESENTATION-NEUTRAL NONSMUGGLING LAW:
   PAIRING/PLACEMENT DEPENDENCY ORDER:
   SOURCE OF ARGUMENT ARCHITECTURE:
   ROLE OF RETAINED P_t:
   INITIAL PAIRING P_0:
   FIRST-B PRIMARY ACTION:
   FIRST-B FOUR DESCENDANTS:
   FIRST EXACT MISSING DATUM:
   ```

8. Package the work.

   Write:

   `QBL_PRIMARY_PAIRING_INITIAL_STATE_BOUNDARY_v1.md`

   Build:

   `p5-b3-v10_initial-pairing-placement-order_<timestamp>.zip`

   Include source and executed notebooks, scripts, exact outputs, traces, formal sources, source map, assumption lock, findings, manifest, and SHA-256 sidecar.
