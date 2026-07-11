# p5_v8v Agent Instructions

[CURRENT STATE]

Use `QBL_PRIMITIVE_CUSTODY_AND_ORTHAD_LAW_v2.md` as the primary authority.

The primitive custody state is

```text
Xi_t = (A_t, q_t, theta_t, k_t, j_t, W_t)
q_t = (u_t, v_t)
```

`A` is the domain counter.

`q` is the carried balanced-refinement pair.

`theta` is the carried phase.

`k` is the local phase-position index inside the current domain.

`j` is the global phase-position index across all domains.

`W` is the exact ordered primitive word already executed.

Use

```text
j_t = j_start(A_t) + k_t
j_start(A) = 1 + 6(2^A - 1)
```

The state self-selects the next primitive through

```text
B > Q > L
```

The Orthad does not select, schedule, permit, or veto the primitive letter. It mutates with every selected primitive letter.

The fully retained lifted state is

```text
Xi_hat_t =
(
    Xi_t,
    P_t,
    Omega_t_plus,
    Omega_t_minus,
    T_t_plus_to_minus,
    T_t_minus_to_plus
)
```

`P_t` is the generative primary pairing.

`Omega_t_plus` and `Omega_t_minus` are chart restrictions intended to be derived from `P_t`.

`T_t_plus_to_minus` and `T_t_minus_to_plus` are directed transfers intended to be derived from `P_t`.

The Orthad is

```text
⌞Xi_hat_t⌝
```

`Xi_hat_t` is the fully retained lifted state.

`⌞Xi_hat_t⌝` is the Orthad wrapping and reading that state.

They are not identical objects.

The exact pairing type, pairing seed, pairing recurrence, chart maps, and transfer recurrences remain `NOT_YET_DERIVED`.

The recent successor search on `Z/12Z` did not derive those objects.

Treat `Z/12Z` as a finite doubled carrier, finite shadow skeleton, or local coordinate surface until a stronger type is proved.

Treat the supplied architecture diagram as conceptual orientation only.

Where an image glyph and this written notation disagree, the written notation controls.

Use these exact symbols:

```text
Primitive custody state:      Xi_t
Fully retained lifted state:  Xi_hat_t
Orthad:                        ⌞Xi_hat_t⌝
```

Apply these custody mutations.

```text
B:
    (u_t, v_t) -> (v_t, u_t + v_t)
    A, theta, k, and j are unchanged.

Q:
    theta_{t+1} = theta_t + pi/2
    k_{t+1} = k_t + 1
    j_{t+1} = j_t + 1
    q and A are unchanged.

L:
    A_{t+1} = A_t + 1
    k_{t+1} = 0
    j_{t+1} = j_start(A_t + 1)
    q and theta carry unchanged.
    W appends L.
```

Apply this Orthad mutation at `L`:

```text
latch the completed active axis
retain the complete old pairing block
append one new orthogonal active axis
increase pairing rank by one
extend both chart restrictions
extend both directed transfers
```

The complete retained object is `Xi_hat_t`, not `P_t` alone.

Use `p5_v8u` only as prior negative context and downstream local-carrier evidence.

[STRATEGIC QUESTION]

Determine the earliest internally generated Orthad object.

Assess whether the primary pairing seed and its `B/Q/L` mutation law can be derived directly from the primitive custody state and exact word prefix.

Do not begin from a successor on `Z/12Z`.

If a finite successor survives, determine its exact downstream role after the pairing-first construction is established.

Consider whether the strongest path is:

```text
pairing type
-> pairing seed
-> B/Q/L pairing mutations
-> chart restrictions
-> directed transfers
```

Propose a stronger dependency order if the evidence forces one.

[REASONING TASK]

1. Determine the corrected type ledger.

   Define the types of:

   ```text
   A
   q=(u,v)
   theta
   k
   j
   W
   Xi_t
   P_t
   Omega_t_plus
   Omega_t_minus
   T_t_plus_to_minus
   T_t_minus_to_plus
   Xi_hat_t
   ⌞Xi_hat_t⌝
   ```

   Distinguish:

   ```text
   domain counter A
   local phase-position index k
   global phase-position index j
   pairing rank
   active-axis index
   chart coordinate
   retained lifted state
   Orthad wrapper
   ```

   Confirm that `Xi_t` is the custody state.

   Confirm that `Xi_hat_t` is the fully retained lifted state.

   Confirm that `⌞Xi_hat_t⌝` wraps and reads `Xi_hat_t`.

   Report: `typed_state_ledger.md`.

2. Reproduce the canonical primitive trace.

   Start from:

   ```text
   A=0
   q=(1,1)
   theta=0
   k=0
   j=1
   W=empty
   ```

   Derive:

   ```text
   BQQBBBQBQBBQBBL
   ```

   Record every prefix.

   Record after every step:

   ```text
   A
   q
   theta
   k
   j
   W
   capacity
   CanB
   CanQ
   selected primitive
   ```

   Confirm:

   ```text
   floor pair = (55,89)
   product = 4895
   Q count = 5
   phase at first L = 5*pi/2
   phase modulo 2*pi = pi/2
   complex phase witness = i
   pair and phase carry through L
   k resets to 0 at L
   j becomes 7 after the first L
   first next-domain primitive = B
   next pair = (89,144)
   ```

   Report:

   ```text
   custody_trace.jsonl
   custody_snapshots.json
   custody_trace_summary.md
   ```

3. Retire the successor-first dependency.

   Examine the `p5_v8u` claims about `alpha_empty` and `S_empty`.

   Determine which claims remain useful as local-carrier observations.

   Determine which claims were placed too early in the dependency chain.

   Remove `alpha_empty` and `S_empty` from the first-gap position unless the current derivation forces them back there.

   Report:

   ```text
   FIRST_TRUE_GAP:
       PRIMARY_PAIRING_TYPE_SEED_AND_MUTATION

   Z12_SUCCESSOR_STATUS:
       DOWNSTREAM_COORDINATE_QUESTION
   ```

   Include the exact dependency argument.

   Report: `successor_path_reassessment.md`.

4. Determine the primary pairing type.

   Work out the domain and codomain of `P_t`.

   Determine what `P_t` pairs.

   Determine whether it is:

   ```text
   a bilinear form
   a sesquilinear form
   a quadratic refinement
   an operator-valued pairing
   a block pairing
   another exact object
   ```

   Determine its dimension before the first `L`.

   Determine how its rank relates to latched axes.

   Determine how the active axis is represented.

   Confirm that `P_t` is not a chart-local matrix.

   Confirm that `P_t` is not the Bloch sphere.

   Confirm that `P_t` is not `Z/12Z` itself.

   Report: `primary_pairing_type.md`.

   End with one result:

   ```text
   PRIMARY_PAIRING_TYPE: DERIVED
   ```

   or

   ```text
   PRIMARY_PAIRING_TYPE: NOT_YET_DERIVED
   MISSING_OBJECT: <one exact object>
   ```

5. Determine the primary pairing seed.

   Use only:

   ```text
   Xi_0
   W_0
   the primitive custody law
   previously licensed retained geometry
   ```

   Determine whether `P_0` is forced.

   Check whether each ingredient is licensed at this layer.

   Leave unlicensed ingredients out.

   Confirm for yourself why none of these may seed `P_0` without a derivation:

   ```text
   constant chart matrix
   imported Weil matrix
   finished FQM form
   Bloch coordinate
   terminal character
   affine 7/8/9 coordinate
   Z/12Z shadow skeleton
   ```

   Report: `primary_pairing_seed.md`.

   End with one result:

   ```text
   PRIMARY_PAIRING_SEED: DERIVED
   ```

   or

   ```text
   PRIMARY_PAIRING_SEED: NOT_YET_DERIVED
   MISSING_MAP: <one exact map>
   ```

6. Determine the `B` pairing mutation.

   Work from:

   ```text
   q_t=(u_t,v_t)
   q_{t+1}=(v_t,u_t+v_t)
   A, theta, k, and j are unchanged.
   ```

   Determine how the new arithmetic anchor mutates `P_t`.

   Determine how the new germ width mutates `P_t`.

   Preserve pairing rank.

   Preserve all latched axes.

   Preserve `theta`.

   Determine whether

   ```text
   a_t = exp(i*theta_t)/(u_t*v_t)
   ```

   is a lawful local trace of the larger pairing mutation.

   Keep the shorthand separate from the full pairing.

   Target:

   ```text
   P_{t+1} = B_pairing(P_t, Xi_t, Xi_{t+1})
   ```

   Report:

   ```text
   B_pairing_mutation.md
   B_pairing_trace.jsonl
   ```

   End with one result:

   ```text
   B_PAIRING_MUTATION: DERIVED
   ```

   or

   ```text
   B_PAIRING_MUTATION: NOT_YET_DERIVED
   MISSING_MAP: <one exact map>
   ```

7. Determine the `Q` pairing mutation.

   Work from:

   ```text
   theta_{t+1}=theta_t+pi/2
   k_{t+1}=k_t+1
   j_{t+1}=j_t+1
   q and A are unchanged.
   ```

   Determine how the quarter-turn witness mutates `P_t`.

   Preserve pairing rank.

   Preserve the arithmetic anchor.

   Preserve all latched axes.

   Determine whether the local shorthand rotates by multiplication with `i`.

   Keep the shorthand separate from the full pairing.

   Target:

   ```text
   P_{t+1} = Q_pairing(P_t, Xi_t, Xi_{t+1})
   ```

   Report:

   ```text
   Q_pairing_mutation.md
   Q_pairing_trace.jsonl
   ```

   End with one result:

   ```text
   Q_PAIRING_MUTATION: DERIVED
   ```

   or

   ```text
   Q_PAIRING_MUTATION: NOT_YET_DERIVED
   MISSING_MAP: <one exact map>
   ```

8. Determine the `L` pairing mutation.

   Separate custody mutation from Orthad mutation.

   Custody:

   ```text
   A_{t+1}=A_t+1
   k_{t+1}=0
   j_{t+1}=j_start(A_t+1)
   q_{t+1}=q_t
   theta_{t+1}=theta_t
   W_{t+1}=W_t L
   ```

   Orthad:

   ```text
   retain the complete old pairing block
   latch the completed active axis
   append one new orthogonal active axis
   increase pairing rank by one
   extend both chart restrictions
   extend both directed transfers
   ```

   Use a pairing-rank symbol separate from `k`:

   ```text
   r_t = rank(P_t)
   ```

   Determine whether

   ```text
   r_{t+1}=r_t+1
   ```

   at `L`.

   Target the block form:

   ```text
   P_{t+1} = [ P_t   C_t   ]
             [ C_t*  p_new ]
   ```

   Determine `C_t` from retained state.

   Determine `p_new` from retained state.

   If either is not forced, name the exact missing map.

   Report:

   ```text
   L_pairing_extension.md
   before_first_L.json
   immediately_after_first_L.json
   ```

   End with one result:

   ```text
   L_PAIRING_EXTENSION: DERIVED
   ```

   or

   ```text
   L_PAIRING_EXTENSION: NOT_YET_DERIVED
   MISSING_MAP: <one exact map>
   ```

9. Derive both charts from one pairing.

   Determine explicit chart maps:

   ```text
   iota_plus
   iota_minus
   ```

   Target:

   ```text
   Omega_t_plus = iota_plus* P_t iota_plus
   Omega_t_minus = iota_minus* P_t iota_minus
   T_t_plus_to_minus = iota_minus* P_t iota_plus
   T_t_minus_to_plus = iota_plus* P_t iota_minus
   ```

   Determine the domain and codomain of each map.

   Determine the overlap domain.

   Determine whether both charts cover one retained object.

   Determine whether both transfers arise from the same pairing.

   Confirm that no chart or transfer is independently seeded.

   Stop this layer if `P_t` is still underived.

   Report:

   ```text
   chart_maps.md
   overlap_domain.md
   chart_restriction_trace.jsonl
   transfer_trace.jsonl
   ```

   End with separate statuses:

   ```text
   CHART_MAPS: DERIVED or NOT_YET_DERIVED
   DIRECTED_TRANSFERS: DERIVED or NOT_YET_DERIVED
   ```

10. Check the one-tick causal order.

    For every prefix of

    ```text
    BQQBBBQBQBBQBBL
    ```

    record:

    ```text
    Xi_t
    CanB
    CanQ
    selected primitive U_t
    Xi_{t+1}
    P_t
    P_{t+1}
    Omega_t_plus
    Omega_{t+1}_plus
    Omega_t_minus
    Omega_{t+1}_minus
    T_t_plus_to_minus
    T_{t+1}_plus_to_minus
    T_t_minus_to_plus
    T_{t+1}_minus_to_plus
    Xi_hat_t
    Xi_hat_{t+1}
    ```

    Confirm this order:

    ```text
    Xi_hat_t
    -> state selects U_t
    -> Xi_t advances to Xi_{t+1}
    -> P_t mutates to P_{t+1}
    -> chart restrictions derive from P_{t+1}
    -> directed transfers derive from P_{t+1}
    -> Xi_hat_{t+1} is retained
    ```

    Confirm that this is one coupled lifted transition.

    Confirm that the Orthad is not a post-process.

    Confirm that no projection occurs during this transition.

    Report:

    ```text
    full_prefix_causal_trace.jsonl
    causal_order_certificate.md
    ```

11. Reassess `Z/12Z`.

    Determine whether it is:

    ```text
    a local doubled phase/orientation carrier
    a finite shadow skeleton
    a chart coordinate surface
    a finite quotient of a larger retained object
    something stronger
    ```

    Test each proposed type against the pairing-first architecture.

    Determine what information it retains.

    Determine what information it discards.

    Determine whether it can carry the full exact word history.

    Call it the full retained carrier only if the proof forces that result.

    Report: `z12_type_assessment.md`.

    End with one result:

    ```text
    Z12_TYPE: <exact derived type>
    ```

    or

    ```text
    Z12_TYPE: NOT_YET_DERIVED
    ```

12. Keep the affine Prime result downstream.

    Treat the proved affine `7/8/9` grammar and exact threshold bridge as a candidate domain-boundary factor.

    Confirm for yourself why the affine circle coordinate cannot be `P_0` without a derivation.

    Confirm for yourself why affine doubling cannot be the internal Orthad mutation without a derivation.

    Determine whether a future factor map could have one of these shapes:

    ```text
    Xi_hat_A -> (E_A, c_A)
    ```

    or

    ```text
    ⌞Xi_hat_A⌝ -> (E_A, c_A)
    ```

    Do not choose between them until the source object and quotient are derived.

    Record:

    ```text
    AFFINE_GLOBAL_THRESHOLD_BRIDGE: PROVED
    QBL_TO_AFFINE_FACTOR_MAP: NOT_YET_DERIVED
    INTERNAL_ORTHAD_SEED_FROM_AFFINE_MAP: NOT_LICENSED
    ```

    Report: `affine_factor_boundary.md`.

13. Define MHD readiness.

    Determine the minimum internal machinery needed before applying the Orthad to the Liu 2022 yin-yang overset-grid data.

    Require at least:

    ```text
    primary pairing recurrence
    two chart maps
    two directed transfer laws
    overlap-domain definition
    cocycle or route-consistency test
    vector component transformation law
    tensor component transformation law
    units and grid-geometry verification
    field-valued channel definition
    ```

    Separate:

    ```text
    data-reader readiness
    geometric readiness
    Orthad readiness
    projection readiness
    ```

    Report: `mhd_readiness_checklist.md`.

    End with one result:

    ```text
    MHD_ORTHAD_READINESS: READY
    ```

    or

    ```text
    MHD_ORTHAD_READINESS: NOT_READY
    MISSING: <exact objects>
    ```

14. Keep projection downstream.

    Determine whether every proposed projection input is generated from the exact QBL prefix.

    Confirm for yourself why terminal projection is licensed only after the complete lifted evolution.

    Leave projection closed when a required pairing, chart, or transfer object remains missing.

    Leave these downstream claims closed when their input objects are placeholders:

    ```text
    gauge class
    FQM
    Weil structure
    character
    Bloch state
    MHD field result
    ```

    Report separate statuses for:

    ```text
    primitive custody
    primary pairing type
    primary pairing seed
    B mutation
    Q mutation
    L extension
    chart maps
    directed transfers
    overlap domain
    cocycle
    terminal projection
    gauge/FQM/Weil descent
    affine factor
    MHD readiness
    ```

    Report: `status_boundary.md`.

15. Package the work.

    Use step ID:

    ```text
    p5_v8v
    ```

    Name the package:

    ```text
    p5_v8v_pairing-first-orthad-realignment_<YYYYMMDD_HHMMSS>.zip
    ```

    Include:

    ```text
    README.md
    FINDINGS.md
    MANIFEST.json
    lab-journal.md
    requirements.txt
    docs/
    inputs/
    scripts/
    notebooks/
    outputs/
    proofs/
    figures/
    trace/
    source_maps/
    ```

    Include the supplied architecture diagram in `inputs/`.

    Treat it as the prior layout master.

    Include a diagram correction sheet.

    State:

    ```text
    Where the image glyph and written notation disagree, the written notation controls.

    Primitive custody state:      Xi_t
    Fully retained lifted state:  Xi_hat_t
    Orthad:                        ⌞Xi_hat_t⌝
    ```

    Include `QBL_PRIMITIVE_CUSTODY_AND_ORTHAD_LAW_v2.md` in `inputs/` as the primary authority.

    Include `p5_v8u` only as prior negative context.

    Include `ASSUMPTION_LOCK.md`.

    List every forbidden import tested in this pass.

    Include a source notebook and a separately executed notebook.

    Use one code cell per claim.

    Use no notebook file I/O.

    Every claim cell must print:

    ```text
    PASS or FAIL
    exact values
    claim boundary
    ```

    Every claim cell must emit one figure with one axes.

    Include a negative control showing that one successor-first construction fails to derive the pairing-first objects.

    Include a Lean theorem surface for:

    ```text
    primitive custody transition typing
    Q index updates
    L custody carry
    pairing-rank separation from k
    one-tick causal ordering
    ```

    Compile Lean when available.

    Otherwise report:

    ```text
    LEAN SOURCE PRESENT; COMPILATION NOT VERIFIED
    ```

    `FINDINGS.md` must separate:

    ```text
    Proved abstractly
    Certified finitely
    Observed
    Open
    Retired path
    ```

    The package must state:

    ```text
    FIRST TRUE GAP:
        PRIMARY PAIRING TYPE, SEED, AND PER-LETTER MUTATION

    NATIVE SUCCESSOR ON Z/12Z:
        DOWNSTREAM COORDINATE QUESTION

    ORTHAD EXISTS FROM FIRST PRIMITIVE TICK:
        ARCHITECTURAL LAW

    PRIMITIVE CUSTODY STATE:
        Xi_t

    FULLY RETAINED LIFTED STATE:
        Xi_hat_t

    ORTHAD:
        ⌞Xi_hat_t⌝

    EXACT PRIMARY PAIRING TYPE:
        DERIVED or NOT_YET_DERIVED

    EXACT PRIMARY PAIRING SEED:
        DERIVED or NOT_YET_DERIVED

    EXACT PRIMARY PAIRING RECURRENCE:
        DERIVED or NOT_YET_DERIVED

    EXACT CHART MAPS:
        DERIVED or NOT_YET_DERIVED

    EXACT DIRECTED TRANSFERS:
        DERIVED or NOT_YET_DERIVED

    QBL_TO_AFFINE FACTOR MAP:
        NOT_YET_DERIVED

    MHD_ORTHAD_READINESS:
        READY or NOT_READY
    ```

    Return:

    ```text
    corrected research document
    experiment-package ZIP
    package SHA-256
    document SHA-256
    brief chat summary bounded by the packaged evidence
    ```