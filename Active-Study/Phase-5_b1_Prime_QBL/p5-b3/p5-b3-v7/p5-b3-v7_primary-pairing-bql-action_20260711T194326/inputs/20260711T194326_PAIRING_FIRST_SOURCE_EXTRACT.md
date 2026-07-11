## 13. Pairing-first construction

The primary pairing is generative. The two diagonal chart matrices are its restrictions. They are not independently invented and then combined afterward.

The full dual-chart operator may be displayed schematically as

$$
\mathcal O_t=
\begin{pmatrix}
\Omega_t^+ & T_t^{-\to+}\\
T_t^{+\to-} & \Omega_t^-
\end{pmatrix}.
$$

The diagonal blocks are the two chart-local restrictions. The off-diagonal blocks are the transfers between charts.

A rigorous implementation should expose explicit chart maps `ι_+` and `ι_-` so that the relationship to one primary pairing is mechanically checkable. The intended algebraic shape is

$$
\Omega_t^+=\iota_+^*P_t\iota_+,
\qquad
\Omega_t^-=\iota_-^*P_t\iota_-,
$$

and

$$
T_t^{+\to-}=\iota_-^*P_t\iota_+,
\qquad
T_t^{-\to+}=\iota_+^*P_t\iota_-.
$$

These equations state the required direction of construction. The exact chart-map recurrence attached to the clean primitive law remains an explicit formalization obligation; it must not be replaced by constant matrices or origin labels.

---

