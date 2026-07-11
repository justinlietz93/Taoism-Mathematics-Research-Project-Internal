# Assumption Lock

Timestamp: `20260710T234301`

This experiment uses only the clean primitive/domain count laws:

- `N_A = 6*2^A` phase positions in Domain `A`;
- `Q_A = N_A - 1`;
- balanced `B` follows the Fibonacci corridor;
- `T_A = min m : F_(m+1)F_(m+2) >= 2^(12*(2^(A+1)-1))`;
- `B_A = T_A - T_(A-1)`;
- `d_A = B_A - 2B_(A-1)`.

Forbidden imports:

- no R/S/T selector;
- no 64-tick window;
- no arbitrary scheduler;
- no terminal projection;
- no Orthad matrix claim is inferred from count primality.
