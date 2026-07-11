# v7p Protocol Definitions

## Native support tokens

- `born:a`: axis `a` exists in retained state.
- `theta:a`: quarter-phase coordinate of axis `a`.
- `q:a`: balanced denominator pair of axis `a`.
- `latch:a`: frozen boundary value of axis `a`.
- `edge:a:b`: overlap/coupling edge between axes `a` and `b`.
- `hol:a:b`: retained pair holonomy accumulator.
- `contact_clock`: latch event order coordinate.
- `contact_z`: contact/latch memory coordinate.

## Event support

- `Q_a`: reads/writes `theta:a`.
- `B_a`: reads/writes `q:a`.
- `L_a`: reads `theta:a`, `q:a`, `contact_clock`; writes `latch:a`, `edge:a:a+1`, `born:a+1`, `contact_clock`, `contact_z`.
- `O_ab`: reads both axis states and edge support; writes pair edge/holonomy support.
- `R_a`: reads only; no retained mutation.

## Legal swap

An adjacent swap is legal when:

1. no write/read or write/write support conflict exists;
2. no event is moved before the birth of an axis it requires;
3. running the swapped history is valid.

## Normal form

Foata layers are computed from dependency predecessors. Legal equivalent histories must share the same normal form and retained signature.
