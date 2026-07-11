# Source Map

| Audit claim | Source |
|---|---|
| Reported package SHA | Agent response recorded in `source-references/AGENT_RESPONSE.txt` |
| Actual uploaded package SHA | Direct SHA-256 of the uploaded ZIP |
| Document SHA | `docs/QBL_GLOBAL_EXACT_THRESHOLD_BRIDGE_v1.md` from the uploaded ZIP |
| Manifest verification | `MANIFEST.json` and every extracted package file |
| Mathematical theorem | Sections 2–7 of the research document, independently checked by `scripts/verify_threshold_core.py` |
| Notebook audit | Source and executed notebooks from the uploaded ZIP |
| Clean rebuild | Included package builder executed on a clean extracted copy |
| Orthad boundary | Included `QBL_PRIMITIVE_CUSTODY_AND_ORTHAD_LAW_v2.md` |
