# Phase 5 v1: Orthad Overset Quadratic Self-Twist Gauss Test

## Claim

The Gauss diagonal is the same-chart self-twist induced by the Orthad overset dual-lens transfer pairing.

## Native construction

The previous Phase 5 v1 overset branch generated the chart transfer coefficient between complementary Orthad charts. The forward transfer gave the finite Fourier kernel with negative sign:

K_- (r,s) = N^(-1/2) exp(-2*pi*i*r*s/N).

The reverse transfer is equally native because the overset grid has two legal transfer directions:

K_+ (r,s) = N^(-1/2) exp(+2*pi*i*r*s/N).

Strip the normalization and read the phase exponent as the native bilinear pairing:

B_+(r,s) = r*s/N.

The same-chart self-twist is the quadratic refinement of that bilinear pairing:

q(r) = 1/2 B_+(r,r) = r^2/(2N).

The generated self-channel is:

G_native(r) = exp(2*pi*i*q(r)) = exp(pi*i*r^2/N).

This was derived and written to the sealed files before the external target was built.

## Polarization gate

The construction is not an isolated fit. It must polarize back to the native reverse transfer:

G(r+s)/(G(r)G(s)) = exp(2*pi*i*r*s/N).

This gate passed for N=8 and N=12 to numerical tolerance.

## Collapse-consistency

The self-twist acts on the retained residue/orientation layer. Under scalar collapse to the neutral residue component r=0, G_native(0)=1, so the existing scalar diagonal trace is preserved:

L1 = i/4895
L2 = -i/(196418*317811)

with 196418*317811 = 62423800998.

## Post-seal verdict

After the sealed native tables were written and hashed, the external target was constructed:

Weil_G_N(r) = exp(pi*i*r^2/N).

Residuals:

N=8: 0
N=12: 0

Combined with the previous overset branch that generated Weil_F, Phase 5 v1 reaches the generated verdict for the finite Weil representation generators at N=8 and N=12.
