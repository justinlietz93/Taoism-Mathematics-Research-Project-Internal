from __future__ import annotations

from dataclasses import dataclass, asdict


@dataclass(frozen=True, slots=True)
class RecurrenceAssessment:
    primary_pairing_status: str
    chart_recurrence_status: str
    rank_extension_status: str
    projection_status: str
    gauge_fqm_weil_status: str
    smallest_missing_equation: str
    reason: str
    old_bridge_disposition: str

    def to_dict(self) -> dict[str, object]:
        return asdict(self)


def assess_recurrence() -> RecurrenceAssessment:
    missing = (
        "Specify tau_0 and tau_{t+1}=Phi_{U_t}(X_{t+1},W_{t+1},tau_t), "
        "where tau_t=P_t(iota_plus(e_t),iota_minus(e_t)) is the mixed cross-chart "
        "pairing on the active axis. The sources fix a_t=i^(local_Q)/(u*v) and the "
        "restriction direction, but do not fix tau_0 or Phi_B/Phi_Q/Phi_L."
    )
    reason = (
        "The diagonal active-axis trace does not determine the mixed pairing. Two bilinear "
        "forms may agree on both chart restrictions and differ on mixed chart arguments. "
        "The historical v7u compiler cannot fill the gap because it adds an O event and an "
        "ad hoc pair_c rule outside the clean QBL alphabet."
    )
    return RecurrenceAssessment(
        primary_pairing_status="NOT_YET_DERIVED",
        chart_recurrence_status="NOT_YET_DERIVED",
        rank_extension_status="NOT_YET_DERIVED",
        projection_status="NOT_RUN",
        gauge_fqm_weil_status="NOT_RUN",
        smallest_missing_equation=missing,
        reason=reason,
        old_bridge_disposition="REJECT_AS_SEMANTIC_BRIDGE_RETAIN_AS_PROVENANCE",
    )
