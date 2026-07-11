from orthad_v8r.assessment import assess_recurrence


def test_primary_pairing_hard_stop() -> None:
    a = assess_recurrence()
    assert a.primary_pairing_status == "NOT_YET_DERIVED"
    assert "tau_0" in a.smallest_missing_equation
    assert "Phi_B/Phi_Q/Phi_L" in a.smallest_missing_equation


def test_projection_and_descent_not_run() -> None:
    a = assess_recurrence()
    assert a.projection_status == "NOT_RUN"
    assert a.gauge_fqm_weil_status == "NOT_RUN"


def test_old_o_event_bridge_rejected() -> None:
    a = assess_recurrence()
    assert a.old_bridge_disposition == "REJECT_AS_SEMANTIC_BRIDGE_RETAIN_AS_PROVENANCE"
