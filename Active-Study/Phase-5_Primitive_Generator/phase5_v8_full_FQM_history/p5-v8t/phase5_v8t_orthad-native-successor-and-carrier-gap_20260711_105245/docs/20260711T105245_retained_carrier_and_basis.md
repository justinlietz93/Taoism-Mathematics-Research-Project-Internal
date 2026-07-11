# Retained carrier and basis

For domain A, the clean law fixes N_A = 6*2^A positions and requires both orientation hands. Narrowly licensing the doubled cyclic carrier gives D_A = 2N_A and the cyclic axis carrier C_A = Z/D_A Z.

The clean L law retains every completed axis and appends one new active axis. Narrowly licensing the v7d independent-axis product result therefore gives the structural carrier

C_{<=A} = product_{r=0..A} Z/(2N_r)Z.

A concrete point basis is {delta_x | x in C_{<=A}}. This is a basis of the free coordinate space after choosing a coefficient field; the coefficient field is not fixed by custody.

At the first crossing:

- before L: C_0 = Z/12Z, axis-block count 1;
- after L: C_0 x C_1 = Z/12Z x Z/24Z, axis-block count 2;
- after the first next-domain B: the same product carrier; B changes the arithmetic anchor, not the carrier.

The table in `outputs/*_retained_carrier_prefix_table.csv` gives the carrier at every exact prefix.

This does not instantiate the algebraic rank of the underived primary pairing. Axis-block count and pairing rank realization are separate claims.
