# Verification round 2: remaining unverified claims (2026-10-09)

Rule used: keep the guide anchored to Logan's notes and the official ASE A2 task list. Each item below is in scope of a task (A.20, A.26, A.27, A.24, A.23, A.6, B.4, B.5, C.6). Where a source was found the claim stays; where it was only reasoned, it is labeled INFERRED or softened. Nothing was added beyond the task list.

| Claim (guide section) | Task | Result | Source (read 2026-10-09) |
|---|---|---|---|
| High-speed CAN has 120 ohm terminators at each end (3.2) | A.20 | CONFIRMED. The measured 60 ohm is parallel-resistor arithmetic; wording now says so | Wikipedia, CAN bus |
| CAN-H driven toward 3.5 V, CAN-L toward 1.5 V when transmitting (3.2) | A.20 | CONFIRMED. The 2.5 V rest level is marked "typically" | Wikipedia, CAN bus |
| U0101 = lost communication with the TCM (3.2) | A.20 | CONFIRMED | obd-codes.com U0101 |
| Voltage drop limits (3.2) | A.27 | Search results (youcanic, a repair-advice site) give 0.1 V per connection, 0.2 V ground cable, 0.3 V per side, 0.5 V circuit. Now worded "commonly cited"; OEM spec governs | search summary, not a primary page |
| Hall sensors: DMM cannot test the signal; scope shows a square wave (3.3) | A.26 | CONFIRMED (DMM checks reference and ground only) | VehicleServicePros speed-sensor article; Pico guided test |
| Amp-clamp current ramp: hump where the plunger moves; none = stuck (3.4) | A.26 | CONFIRMED hump/no hump. "Shorted winding = steep tall rise" was NOT supported, so it now says only that a short changes the trace | MOTOR "Current Clamp On-Ramp" (Dec 2007) summary |
| P0700 is only a pointer to codes stored in the TCM (3.6) | A.6 | CONFIRMED | obd-codes.com P0700 |
| P0731, P0751, P0960 definitions (3.1) | A.19, A.24 | CONFIRMED | obd-codes.com |
| TBV stuck in recirculation/bypass overheats the transmission (4.4) | B.5 | CONFIRMED (case reports, search level) | VehicleServicePros 4R75/5R55 article |
| Pan debris: fine gray dust normal; brass slivers and coarse steel abnormal; non-magnetic aluminum (4.3) | B.4 | CONFIRMED in general; table now says "typical sources, not exact" | search results (Rick's, forum posts, tool-source blog), low authority |
| Programming needs a battery maintainer, not a charger (3.8) | A.25, C.6 | CONFIRMED in general (stable voltage during programming) | VehicleServicePros tool review |
| GM pressure sweep "Park/Neutral below 1500 rpm" (3.7) | A.24 | NOT VERIFIABLE and outside the task list. Removed; guide now says tests are gated by range and speed per SI | none |
| Adapt-reading rules (3.8); electronic shift-quality cause table (3.9) | A.23 | NOT VERIFIABLE as stated. Kept as typical patterns, labeled INFERRED | none |

Not checked and left as written (principle-level, consistent with Logan's notes or the task wording): TR/MLP checks, DTC suffix groupings beyond the three above, A.22 examples, CVT/DCT contrasts (A.1 recognition only), friction soak time (no number is given), drum reject limits (guide says SI).
