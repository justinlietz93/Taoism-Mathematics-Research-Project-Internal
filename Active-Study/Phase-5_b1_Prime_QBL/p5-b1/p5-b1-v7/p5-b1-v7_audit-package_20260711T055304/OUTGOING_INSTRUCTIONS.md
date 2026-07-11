# p5-b2-v1 Agent Instructions

[CURRENT STATE]

Branch 1 is closed.

The affine carry model now has an exact interval presentation, one-step Lebesgue law, complexity `p(n)=2^(n+1)-1`, entropy `log(2)`, non-soficity, no finite Markov order, and topological mixing.

These results apply to the affine ceiling sequence.

The exact QBL threshold sequence is linked to that model only on the finite certified range `A=0..10000`.

The global identity

\[
T_A=\lceil y_A\rceil
\]

is still not proved.

[STRATEGIC QUESTION]

Determine whether the exact Fibonacci threshold count equals the affine ceiling law for every `A`.

Target the global bridge before using the affine-language theorems as all-depth QBL theorems.

Consider both routes:

1. a direct exact Binet estimate;
2. a lower bound for the distance of the affine main term from the integers.

Use the strongest route that produces explicit constants and a finite remainder check.

[REASONING TASK]

1. Define the exact threshold quantity.

   State the exact Fibonacci product or inequality that defines `T_A`.

   State the affine main term `y_A` with every constant defined.

   Report: the exact identity that must be proved.

2. Expand the exact quantity with Binet's formula.

   Separate it into:

   ```text
   affine leading term
   exponentially decaying correction
   ```

   Keep the correction signed and exact before bounding it.

   Report: a closed formula and a uniform absolute upper bound.

3. Reduce the ceiling equality to a separation inequality.

   Determine a sufficient condition of the form

   \[
   \operatorname{dist}(y_A,\mathbb Z)>|\varepsilon_A|,
   \]

   where `epsilon_A` is the Binet correction.

   Treat exact integer hits separately.

   Report: the precise implication from the separation bound to the ceiling identity.

4. Work out the logarithmic linear form.

   Express the relevant distance to an integer as a nonzero linear form in logarithms of explicit algebraic or rational numbers.

   Determine which theorem applies.

   Give every degree, height, coefficient, and nonzero condition needed by that theorem.

   Report: the theorem statement used and the instantiated bound.

5. Compare the bounds.

   Find an explicit `A_0` such that the logarithmic lower bound exceeds the Binet upper bound for every `A>=A_0`.

   Use rigorous arithmetic.

   Report: `A_0` and the full inequality chain.

6. Verify the finite remainder.

   Check every `A<A_0` by exact integer arithmetic or outward-rounded interval arithmetic.

   Include the first and smallest separation cases.

   Report: a machine-readable finite certificate and a trace.

7. Preserve the branch boundary.

   If the global theorem closes, state:

   ```text
   GLOBAL T_A=ceil(y_A) BRIDGE: PROVED
   ```

   Otherwise state the exact missing theorem or failed bound and keep:

   ```text
   GLOBAL T_A=ceil(y_A) BRIDGE: NOT YET PROVED
   ```

8. Keep the Orthad boundary unchanged.

   Count laws do not determine chart matrices, gauge values, holonomy, FQM classes, or Weil projections.

   Retain:

   ```text
   GAUGE/FQM MAP FROM d_A=±1: NOT YET DERIVED
   ```

9. Add formal and computational companions.

   Produce a Lean 4 theorem surface for the exact algebraic reduction and finite-range implication.

   Produce a no-I/O SymPy notebook with one code cell per claim, one figure per cell, explicit thresholds, and PASS/FAIL output.

   Do not claim Lean verification unless it compiles.

10. Package the work.

    Produce:

    ```text
    p5-b2-v1_global-threshold-bridge_<YYYYMMDDTHHMMSS>.zip
    ```

    Use the reproducible experiment-package format.

    Include the exact source formulas, assumption lock, source map, derivation script, source and executed notebooks, proof surfaces, outputs, traces, figures, deterministic builder, and manifest.

    Return the document and package SHA-256 hashes.
