# p5-b2-v2 Agent Instructions

[CURRENT STATE]

Branch 1 is closed and accepted.

The `p5-b2-v1` response did not execute the assigned research task. It only restated prior results.

The global exact-threshold bridge remains open:

```text
GLOBAL T_A=ceil(y_A) BRIDGE: NOT YET PROVED
```

The complete accepted Branch 2 task is included as:

```text
inputs/p5-b2-v1_ACCEPTED_TASK.md
```

[REASONING TASK]

1. Work from `inputs/p5-b2-v1_ACCEPTED_TASK.md`.

2. Perform the research task now.

3. Determine whether the exact Fibonacci threshold count equals the affine ceiling law for every `A`.

4. Carry out the Binet reduction, the correction bound, the distance-to-integers reduction, the logarithmic lower-bound route, and the finite remainder check required by the accepted task.

5. If the global proof closes, state:

   ```text
   GLOBAL T_A=ceil(y_A) BRIDGE: PROVED
   ```

6. If it does not close, identify the exact missing theorem, inequality, constant, or nonzero condition. Retain:

   ```text
   GLOBAL T_A=ceil(y_A) BRIDGE: NOT YET PROVED
   ```

7. Keep the Orthad boundary unchanged:

   ```text
   GAUGE/FQM MAP FROM d_A=±1: NOT YET DERIVED
   ```

8. Produce the full document, computational companions, proof surfaces, finite certificates, traces, and reproducible experiment package required by the accepted task.

9. Name the experiment package:

   ```text
   p5-b2-v2_global-threshold-bridge_<YYYYMMDDTHHMMSS>.zip
   ```

10. Return:

    - the completed research document;
    - the experiment-package zip;
    - the exact SHA-256 of both;
    - the requested status lines.

Do not only acknowledge, adopt, summarize, or describe the next step. Execute it and return the artifacts.
