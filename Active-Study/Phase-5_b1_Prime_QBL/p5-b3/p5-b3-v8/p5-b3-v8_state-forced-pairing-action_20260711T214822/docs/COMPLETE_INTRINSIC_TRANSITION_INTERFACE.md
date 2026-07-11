# Complete Intrinsic Transition Interface

Let

\[
\widehat X_t=(X_t,P_t,D_{++,t},D_{--,t},D_{+-,t},D_{-+,t}).
\]

Primitive selection is

\[
p_t=\Sigma_{cust}(X_t),
\]

with strict `B > Q > L` predicates. The complete autonomous transition is

\[
\widehat X_{t+1}=\mathcal U_{p_t}(\widehat X_t).
\]

`B`, `Q`, and `L` are case maps, not runtime inputs.

For every placement,

\[
D_{ab,t+1}=R_{ab,t+1}(P_{t+1}).
\]

A complete intrinsic law must provide:

1. seed `P_0` and seed restriction family;
2. state-generated `B^sharp`, `Q^sharp`, and `L^sharp`;
3. exact old/new `L` components;
4. exact restriction maps after every prefix;
5. preservation of latched sectors and exact word;
6. no projection.

The first missing datum is the Primary Pairing Generation and Restriction Law (`PPGRL`).
