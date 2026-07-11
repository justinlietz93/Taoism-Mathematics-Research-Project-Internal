# Agent Instructions

[CURRENT STATE]

The prior package is reproducible, but its main result is not a canonical Orthad result. It runs one `B`, an invented `FLOOR` stage, and one `L` from `(34,55)`. The clean primitive law starts at `(1,1)`, self-selects every letter, and reaches the first lift through `BQQBBBQBQBBQBBL`. At `L`, only the dimensional counter increments. The pair and phase carry into the new domain.

Use `inputs/*QBL_PRIMITIVE_CUSTODY_AND_ORTHAD_LAW_v2.md` as the primary authority. Treat the old package as code provenance, not semantic authority.

[STRATEGIC QUESTION]

Assess whether the old implementation can be safely repaired or whether a clean primitive engine is simpler. Reuse only code whose meaning survives the recovered law. Explain that choice briefly before implementing it.

[REASONING TASK]

1. Work out the minimal custody state needed to self-select `B`, `Q`, or `L`. Include `A`, the carried pair, carried phase, local phase-position index, global position index, and exact ordered word.

2. Implement the strict priority law `B > Q > L`. Reevaluate it after every primitive step. Let the state derive the word. Do not feed the word into the engine.

3. Derive the first crossing from `(1,1)`. Record every prefix with the before-state, `CanB`, `CanQ`, selected primitive, after-state, capacity, pair product, local position, global position, phase quarter count, and word prefix.

4. Confirm this exact boundary:

```text
word: BQQBBBQBQBBQBBL
floor pair: (55,89)
Q steps: 5
phase at the boundary: i
L action: A increments; pair and phase carry; local position becomes 0
first next-domain step: B
next pair: (89,144)
```

Report: a machine-readable trace and tests that fail on any different word, reset, or next-domain pair.

5. Treat `FLOOR` as a state predicate only. Record `floor_reached=true` in the trace when `B` is blocked and no `Q` position remains. Do not implement it as an operator, field-emission stage, or word symbol.

6. Attach the Orthad from the first primitive tick. Keep one primary pairing, two chart restrictions, and two directed transfers in the lifted state. Mutate them on every `B`, `Q`, and `L` step. Let `L` inherit the completed block and add one new active axis.

7. Determine whether the provided sources are sufficient to derive exact chart maps and per-tick restriction equations. If they are sufficient, implement them and show the derivation. If they are not sufficient, stop that layer with `ORTHAD_CHART_RECURRENCE_NOT_YET_DERIVED`. Do not fill the gap with constant matrices or labels.

8. Make terminal projection depend on the completed Orthad. Add causal ablations for the primary pairing, each chart restriction, and each directed transfer. A successful projection claim requires each load-bearing ablation to change or invalidate the result for a stated reason.

9. Keep the external Shadow Residual reference outside the lift. Do not claim a character, gauge, FQM, isometry, Weil, Bloch-sphere, or MHD result until that object is explicitly constructed from the clean history and certified at the correct layer.

10. Rebuild the verifier so it recomputes all evidence from source inputs. Require complete matrices, unique channel addresses, complete trace prefixes, manifest integrity, and the exact acceptance boundary above. Add corruption tests for missing files, duplicate rows, pair reset, phase reset, hard-coded `i`, fixed `12` before `L`, and injected lap signs.

11. State separate statuses. Use these lines or stricter ones:

```text
PRIMITIVE_FIRST_CROSSING: PASS or FAIL
POST_L_CARRY: PASS or FAIL
ORTHAD_CHART_RECURRENCE: DERIVED or NOT_YET_DERIVED
ORTHAD_CAUSAL_PROJECTION: PASS, FAIL, or NOT_RUN
GAUGE_FQM_WEIL_DESCENT: PASS, FAIL, or NOT_RUN
```

Do not collapse them into one `global_pass`.

Report: one reproducible experiment package and a brief chat summary that points to its `FINDINGS.md` and `docs/<TS>_RESULTS.md`.

[PACKAGE THE WORK]

Use one run stamp everywhere and deliver:

```text
experiment_package_YYYYMMDD_HHMMSS/
  README.md
  FINDINGS.md
  MANIFEST.json
  lab-journal.md
  requirements.txt
  docs/
    <TS>_RESULTS.md
  inputs/
    <TS>_ASSUMPTION_LOCK.md
    <TS>_QBL_PRIMITIVE_CUSTODY_AND_ORTHAD_LAW_v2.md
    <other primary inputs actually used>
  scripts/
    <TS>_<name>.py
  notebooks/
    <TS>_<name>.ipynb
    <TS>_<name>_executed.ipynb
  outputs/
    <timestamped result files>
  proofs/
    <timestamped Lean files and compiler log, if formal proof is claimed>
  figures/
    <timestamped figures, if used>
  trace/
    <TS>_<name>_trace.jsonl
  source_maps/
    <TS>_SOURCE_MAP.md
```

`MANIFEST.json` must list every file except itself with byte count and SHA-256. Pin exact dependency versions. Include the source notebook and its executed copy. Put assumptions and forbidden imports in `ASSUMPTION_LOCK.md`. Split claims into `Proved abstractly`, `Certified finitely`, and `Open`. Include a single command that rebuilds all generated outputs and a second command that verifies the manifest and evidence from scratch.
