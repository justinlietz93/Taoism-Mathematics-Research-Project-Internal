# Phase 5 v7x: Depth 3-6 Follow Channel-Field Readout

STATUS: `DEPTH_3_6_FOLLOW_CHANNEL_FIELD_READOUT_SUPPORTED_WITH_LAP2_NEGATION_ON_TESTED_RETAINED_LENS_MODEL`

GLOBAL_PASS: `true`

PHASE5_CLOSED: `false`

This package verifies Follow channel-field readouts at depths 3 through 6. It records support, magnitude, sign character, expansion width, inter-term phase, and exponent spacing without carrying scalar Shadow Residual cargo in the retained state.

Main positive closures:

- depth 3-6 Follow channel-field readout records are emitted;
- lap-2 equals negative lap-1 on the same support and magnitude channels;
- lap-1 matches external chi12 sign, while lap-2 matches the flipped orientation;
- depth nesting preserves earlier support-prefix channels.

Next target: `Phase 5 v7y: Asymmetric Corridor / Arbitrary Start Ladder`.
