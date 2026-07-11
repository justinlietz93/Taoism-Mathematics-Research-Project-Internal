# Causal Order Certificate

The written architecture fixes this order for each primitive tick:

```text
Xi_hat_t
-> custody state selects U_t
-> Xi_t advances to Xi_{t+1}
-> P_t mutates to P_{t+1}
-> both chart restrictions derive from P_{t+1}
-> both transfers derive from P_{t+1}
-> Xi_hat_{t+1} is retained
```

The primitive portion is executed for every first-crossing prefix. The pairing and chart fields are recorded as uninstantiated rather than replaced with constants. No projection is performed.
