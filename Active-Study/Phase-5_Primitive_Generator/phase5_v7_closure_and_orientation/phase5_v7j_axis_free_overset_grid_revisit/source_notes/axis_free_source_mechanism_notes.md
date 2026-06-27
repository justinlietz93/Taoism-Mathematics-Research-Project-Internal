# Axis-Free Overset Grid Source Mechanism Notes

Mechanisms extracted from Wongwathanarat, Hammer, and Müller (2010):

- A single spherical polar grid suffers pole convergence and axis-boundary artifacts.
- Yin-Yang uses two identical low-latitude spherical polar patches with overlap.
- Yang is obtained from Yin by rotations; the coordinate matrix satisfies M^-1 = M.
- Scalar and vector quantities need interpolation/transform across patch overlap.
- Angular boundary conditions are replaced by ghost-zone interpolation from neighboring patch interiors.
- Interpolation coefficients and overlap weights are retained in maps.
- Integrals over the overset domain need weights to avoid double counting.
- Scalar conservation can be restored by flux replacement from interior-derived fluxes.
- Momentum conservation remains harder due to vector-component mixing across rotated patches.
- Tests show no visible internal boundary artifacts and no preferred radial direction.
