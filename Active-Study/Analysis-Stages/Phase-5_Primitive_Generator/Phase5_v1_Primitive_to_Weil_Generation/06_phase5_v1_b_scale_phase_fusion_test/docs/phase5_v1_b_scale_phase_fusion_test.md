# Phase 5 v1: B-Scale-as-Phase Fusion Test

## Claim under test

The quadratic should not be assigned to the flat Q count. Q carries the root-of-unity character. B carries refinement scale. This pass tests whether the B refinement scale, fused into phase and read by the Orthad, generates the quadratic Gauss diagonal, with the Fourier pair-channel forced by polarization of the frozen self-channel.

## Primitive definitions used

- `Q`: phase advance by `π/2`; q preserved.
- `B`: `(u,v) -> sort(v,u+v)`; germ width becomes `1/[v(u+v)]`.
- `L`: host lift; q carried; phase advances by `π/2`.

No new primitive is introduced.

## Derived B-scale law

After r native B refinements from `(1,1)`, the denominator pair is Fibonacci-corridor:

    (u_r, v_r) = (F_{r+1}, F_{r+2})

and the B-carried scale is:

    w_r = 1/(u_r v_r).

The fused B-scale phase exponent is:

    phi_r = Σ_{j=1}^r w_j.

Therefore the same-orientation fused read is frozen as:

    z_r = w_r · i^r · exp(2πi phi_r).

This is not a quadratic law. It is a convergent reciprocal Fibonacci-product sum.

## Pair-channel

The off-diagonal pair-channel is not inserted. It is forced from the frozen self-channel by polarization of `phi`:

    K(r,s) = exp(-2πi [phi_{r+s} - phi_r - phi_s]).

No `1/sqrt(N)` normalization is earned by this construction.

## Collapse consistency

Existing trace targets:

    L1 = i/4895
    L2 = -i/(196418 · 317811)

The corrected decimal product is:

    196418 · 317811 = 62423800998

Results:

    L1 error = 0.0002665683230432261
    L2 error = 1.2707727021899486e-14

The repair fails collapse-consistency before it can become a valid Phase 5 closure.

## Post-seal comparison

The self and pair entries were written and hashed before Weil targets were constructed. Post-seal comparison records nonzero residuals for both χ12 and χ8.

## Verdict

BOUNDARY_DIFFERENT_GROWTH.

B germ width as phase does not generate the quadratic Gauss diagonal. Its polarization does not generate the Fourier kernel. The located boundary is B-scale growth: the exact germ-width accumulation is reciprocal Fibonacci-product summation, not the required quadratic orientation form.
