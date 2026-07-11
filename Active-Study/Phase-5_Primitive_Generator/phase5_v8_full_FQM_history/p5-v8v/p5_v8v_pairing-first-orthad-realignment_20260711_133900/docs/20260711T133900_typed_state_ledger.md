# Typed State Ledger

| Symbol | Type boundary | Role | Status |
|---|---|---|---|
| `A_t` | `Nat` | domain counter | derived |
| `q_t=(u_t,v_t)` | ordered positive integer pair | carried balanced-refinement pair | derived |
| `theta_t` | exact quarter-turn count in `(pi/2)Z` | carried global phase | derived |
| `k_t` | `Fin(6*2^A)` | local phase-position index | derived |
| `j_t` | positive integer with `j=j_start(A)+k` | global phase-position index | derived |
| `W_t` | free monoid `{B,Q,L}*` | exact ordered word | derived |
| `Xi_t` | dependent custody state | primitive custody state | derived |
| `r_t` | separate natural-number rank symbol | architectural pairing rank | constrained, not algebraically instantiated |
| `P_t` | exact type not fixed | generative primary pairing | open |
| `Omega_t_plus/minus` | restrictions of `P_t` along underived chart maps | chart restrictions | open |
| directed transfers | mixed restrictions of `P_t` | cross-chart transfer | open |
| `Xi_hat_t` | dependent lifted record | fully retained lifted state | schema fixed, values open |
| `⌞Xi_hat_t⌝` | wrapper/reader over `Xi_hat_t` | Orthad | architectural law |

`k_t` is not pairing rank. A chart coordinate is not an active-axis index. `Xi_t` is not `Xi_hat_t`. `Xi_hat_t` is not the Orthad wrapper.
