# A2 coverage and research

Status: Full task list mapped per task with weights; weighted research pass in progress. Created: 2026-09-20. Last updated: 2026-09-30.

## Official reference

Verified 2026-09-29: [ASE Automobile Study Guide PDF](https://ase.com/wp-content/uploads/ASE_Automobile_Study_Guide.pdf) (© ASE 2026, pages 10–15, "Test Specifications and Task List — Automatic Transmission/Transaxle (Test A2)"). 45 scored questions of 55 total, 75-minute test.

| Content area | Questions | % of test |
|---|---:|---:|
| A. Transmission/Transaxle Diagnosis (General; Mechanical/Hydraulic Systems; Electronic Systems) | 26 | 58% |
| B. In-Vehicle Transmission/Transaxle Maintenance and Repair | 12 | 27% |
| C. Transmission/Transaxle Unit Removal, Inspection, and Installation (Removal/Install; Disassembly/Assembly; Friction and Reaction Units) | 7 | 15% |

Full task statements are in the saved PDF; re-verify before a final ASE package is built in case ASE revises the 2026 task list further (a press release notes A-series task lists are under periodic survey-driven revision).

### Weight per task (2026-09-30)

Read from the local copy `mantrans/sources/ase/ASE_Automobile_Study_Guide_2026.pdf`, pages 10–15. The guide lists 28 Area A tasks, 12 Area B tasks and 23 Area C tasks.

| Area | Questions | Tasks | Questions per task (average) | Study implication |
|---|---:|---:|---:|---|
| A. Diagnosis | 26 | 28 | ~0.93 | Biggest block; symptom → cause reasoning |
| B. In-vehicle maintenance/repair | 12 | 12 | 1.00 | Highest yield per task; currently the thinnest coverage |
| C. Removal/inspection/installation | 7 | 23 | ~0.30 | Learn principles and classic mistakes, not full procedures |

INFERRED: ASE does not publish per-task weights, so the per-task figure is only an average. It is still the best available way to set study priority.

**Topics a 2026-09-30 research pass gave too much weight.** Hybrid/electrified identification (part of A.1), bidirectional controls (A.24), module programming (A.25) and calibration ID/relearn (C.6) are all on the task list. Together they are 4 of 63 tasks, so study them briefly and don't let them drive the plan.

**The official sample questions (pages 13–15, public) show the question style.** There are 8. They test:
- a fluid check on a unit with no dipstick (scan-tool temperature, vehicle level);
- poor launch but normal above 35 mph, which points to the torque converter;
- slipping when cold, from low line pressure;
- a harsh upshift from a failed TPS input;
- an over-temperature message with normal shifting, from a restricted cooler;
- a CVT that won't ratio down, read from a circuit diagram;
- clearing codes with a scan tool, not by disconnecting the battery;
- no reverse, isolated with a clutch/band apply chart (the element used only in reverse).

INFERRED from those: most questions start from a symptom and ask for the most likely cause, often by reading a chart or schematic. They test reasoning, not procedure detail or spec numbers.

### Full task list, mapped to notes and research (2026-09-30)

Task wording is shortened from the ASE guide. Notes coverage means what the learner's raw notes contain: **S** strong, **P** partial (theory only, no diagnosis or procedure), **—** none. Research means entries in this file or in `research_notes/A2 open gap research/`. Research-notes files from 2026-09-30 are snippet-level (full pages were blocked by the session's network policy), so verify before using in a guide.

| Task | Shortened statement | Notes | Research | Priority |
|---|---|---|---|---|
| A.1 | Identify type: TC auto, DCT, CVT, hybrid/electrified | — | 09-29 pass (TC/DCT/CVT) | Low-medium |
| A.2 | Verify concern, visual inspection | — | Area A mech/hydraulic pass | Medium |
| A.3 | Research SI, TSBs, recalls, history | P (`note/notes.md`: "use the exact SI chart") | — | Low |
| A.4 | Determine fluid type and level | — | Area A/B passes | **High** (sample Q1) |
| A.5 | Diagnose with DMM, DSO, scan tool | P (`electronics.txt` sensor theory) | Area A electronic pass | Medium |
| A.6 | OBD II: DTC set/clear enable criteria, permanent DTCs, MIL | — | 09-29 pass (monitors) | Medium (sample Q7) |
| A.7 | Clear DTCs, run monitors, verify repair | — | 09-29 pass | Medium |
| A.8 | Road test for mechanical/hydraulic concerns | P (`note/notes.md` shared-element fault isolation) | Area A mech/hydraulic pass | **High** |
| A.9 | NVH and shift-quality diagnosis | P (`powerflowetc.txt`: shift quality, accumulator slide-bump, synchronous mistiming → harsh/flare) | Area A mech/hydraulic pass | **High** |
| A.10 | Fluid loss and condition | — | Area A mech/hydraulic pass | **High** (sample Q5) |
| A.11 | Hydraulic pressure tests | P (`hydralics.txt` theory) | `hydraulic_pressure_testing.md` | **High** (sample Q3) |
| A.12 | Torque converter stator/OWC failure | — | `stator_owc_diagnosis.md` | **High** (sample Q2) |
| A.13 | TCC mechanical/hydraulic tests | — | stator file (TCC section); Area A mech/hydraulic pass | High |
| A.14 | Diagnose with SI, flow charts, hydraulic diagrams | P | — | Medium |
| A.15 | Stop/start auxiliary pump/accumulator | — | Area A mech/hydraulic pass | Low-medium |
| A.16 | Road test electronic concerns | — | Area A electronic pass | Medium |
| A.17 | Pressure problems with electronic pressure control | **S** (`electronics.txt`: EPC normally high, more current = less pressure, 6L80 ~0.1 A max / 1.0 A min) | `hydraulic_pressure_testing.md` | High |
| A.18 | TCC electronic tests | P (`electronics.txt`: TCC PC solenoid, brake-switch input) | Area A electronic pass | High |
| A.19 | Diagnose electronic control systems | **S** (inputs/outputs, pressure-switch logic, TFT NTC) | Area A electronic pass | Medium (learner strength) |
| A.20 | Electrical circuits incl. data communications | P ("TCM is on the CAN network") | Area A electronic pass | Medium |
| A.21 | Charging system, battery, power/ground circuits | — | Area A electronic pass | Medium |
| A.22 | Transmission vs. engine/ABS/ADAS/transfer case concerns | P (shared PCM inputs: APP, TP, ECT, MAP/MAF) | Area A passes | **High** (sample Q4) |
| A.23 | Shift quality from electronic faults | P (adaptive learning) | Area A electronic pass | High |
| A.24 | Scan data, bidirectional controls, DTCs | — | `scan_tool_bidirectional.md` | Low-medium |
| A.25 | Control modules: test/replace/program/setup | P (one line: calibrations can be reprogrammed) | `tcm_programming_relearn.md` | Low |
| A.26 | DMM/DSO test sensors, solenoids, actuators | P | Area A electronic pass | Medium |
| A.27 | Measure voltage, voltage drop, amperage, resistance | — (learner self-reports strength) | Area A electronic pass | Low-medium |
| A.28 | Electronic shift selectors, switches, displays | P (`electronics.txt`: TR/MLP switch) | Area A electronic pass | Medium |
| B.1 | Shift linkage, cables, TR/neutral-safety switch | P (TR switch theory) | Area B pass | **High** |
| B.2 | External seals and gaskets | — | Area B pass | High |
| B.3 | Driveshaft yoke, drive axle joints, bushings, seals | — | Area B pass | Medium |
| B.4 | Pans and covers; what pan debris means | — | Area B pass | High |
| B.5 | Engine cooling; transmission cooler, thermostat, bypass valve, lines | — | Area B pass | **High** (sample Q5) |
| B.6 | Valve body inspection | — | 09-29 pass (bore technique) | High |
| B.7 | Valve body torque sequence | — | Area B pass | Medium |
| B.8 | Accumulator and servo inspection | P (`powerflowetc.txt`: accumulator purpose, slide-bump; servo applies band) | 09-29 pass | High |
| B.9 | Electrical components, terminals, connectors, harnesses | P | Area B pass | High |
| B.10 | Module inputs, outputs, data communications | P | Area B pass | Medium |
| B.11 | Powertrain mounts | — | Area B pass | Medium |
| B.12 | Fluid/filter service; level and type with or without dipstick | — | Area B pass | **High** (sample Q1) |
| C.1 | Remove/install; core plugs, rear main, dowels | — | Area C pass | Low |
| C.2 | Flexplate, converter bolts/pilot, crank pilot bore and end play | — | Area C pass | Low-medium |
| C.3 | Converter installation and pump engagement | — | Area C pass | Medium (classic trap) |
| C.4 | Cooler flush/test/replace | — | Area B/C passes | Medium |
| C.5 | Routing of harnesses, lines, vents, mounts | — | — | Low |
| C.6 | Software calibration, solenoid/valve body ID, relearn | P (`electronics.txt`: reset adapts after replacement) | `tcm_programming_relearn.md` | Low |
| C.7 | Disassemble, clean, inspect; threads | — | Area C pass | Low |
| C.8 | Pump and drive inspection/measurement | P (`hydralics.txt`: gear/crescent, gerotor, vane, variable-displacement) | Area C pass | Low-medium |
| C.9 | Transaxle differential bearing preload | — | Area C pass | Low |
| C.10 | End play, input and output shaft | — | 09-29 pass | Low-medium |
| C.11 | Shafts, splines, lube holes, bushings | P (sealing rings from shaft to drum) | Area C pass | Low |
| C.12 | Bushings, thrust washers, bearings | — | Area C pass | Low |
| C.13 | Planetary gear assembly | **S** (`powerflowetc.txt` gear sets, ratio rules; `note/notes.md` 10-speed chart) | — | Low-medium (covered) |
| C.14 | Case bores, passages, vents, dowels | — | — | Low |
| C.15 | Valve body inspection (overhaul) | — | 09-29 pass | Low (same as B.6) |
| C.16 | Chains, sprockets, belts, pulleys/sheaves, gears | — | Area C pass | Low |
| C.17 | Transaxle final drive | — | Area C pass | Low |
| C.18 | Install transmission | — | Area C pass | Low |
| C.19 | Clutch pack components | P (frictions/steels, pressure plate, snap ring, return springs, running clearance) | Area C pass | Medium |
| C.20 | Clutch pack clearance | P (why clearance matters) | 09-29 pass | Medium |
| C.21 | Air test clutches and servos | — | `hydraulic_pressure_testing.md`; Area C pass | Medium |
| C.22 | One-way clutch inspection | **S** (roller, sprag, mechanical diode; OWC roles in 10-speed chart) | Area C pass | Low-medium (covered) |
| C.23 | Bands and drums | P (band types, servo) | Area C pass | Low-medium |
| (all) | Clutch/band apply-chart reasoning | **S** (`note/notes.md` range chart, shared-element isolation) | — | **High** (sample Q8) |

INFERRED from the map:
- **Your notes are strongest** on planetary/power flow, one-way clutches, apply-chart reasoning, EPC and the electronic sensor/solenoid theory. Those cover sample-question types 3, 4 and 8 in principle.
- **The weighted gaps** are the symptom-diagnosis tasks (A.4, A.8–A.10, A.12–A.13, A.22) and nearly all of Area B (fluid service, cooler, linkage/TR, seals, pans/debris). Both carry more exam weight than the topics left open on 2026-09-29.

## Source map and coverage

Add rows as personal notes or public resources are actually inspected. A source present on disk is not automatically reviewed; an absent lesson is not automatically a learner weakness.

| Task area | Source/file and location | Access / evidence quality | Learner evidence | Next question |
|---|---|---|---|---|
| A - General Transmission/Transaxle (type ID, visual inspection, service info research, OBD II monitor/DTC basics) | None yet | Not reviewed | Unassessed | No notes cover transmission-type identification (torque converter auto vs. DCT vs. CVT vs. hybrid) or OBD II monitor/DTC clearing procedure specifics. Pending class coverage. |
| A - Mechanical/Hydraulic Systems (road test, NVH/shift quality, fluid loss/condition, pressure tests, torque converter/stator one-way clutch, TCC hydraulic tests) | `notes/hydralics.txt` (2026-09-23); `note/notes.md` image notes (2026-09-22, OWC states per gear, ratio progression) | Learner's own condensed textbook/instructor notes; partial (hydraulics file stops mid pump-design discussion) | Learner reports confidence reasoning through electrical questions, not stated for hydraulic/mechanical | Hydraulic pressure test procedure, TCC lock-up hydraulic test steps, and torque converter stator one-way-clutch failure diagnosis not yet in notes. |
| A - Electronic Systems (scan tool/DMM/DSO diagnosis, TCC electronic tests, electronic pressure control, control module inspect/reprogram, sensor/solenoid testing) | `notes/electronics.txt` (2026-09-29, TCM inputs, ISS/OSS/TSS/VSS, pressure switches, EPC/PC/TCC PC solenoids, adaptive learning); `note/issoss.pdf` (2026-09-29, read in full — technician-guide page 41, "Electrical Components/Transmission Speed Sensors": ISS and OSS are both hall-effect sensors on an 8.3–9.3V TCM supply circuit; ISS is triggered by splines on the 1-2-3-4 and 3-5-R clutch-housing OD, OSS by slots machined into the output shaft; TCM uses ISS for line pressure/shift timing/TCC slip speed/gear ratio and OSS for line pressure/shift timing/vehicle speed/gear ratio; an improper signal from either sets a DTC) | Learner's own notes plus pasted textbook/6L80 tech-guide excerpts; learner states this is his strongest reasoning area | Learner self-reports highest confidence here | Scan-tool bidirectional control use, control-module reprogram/relearn procedure detail, and DMM/DSO test method specifics (not just sensor theory) are not yet in notes. **Learner asked (2026-09-29) to carry the `issoss.pdf` diagrams (clutch-housing spline ISS trigger, output-shaft slot OSS trigger) into whichever future guide covers speed sensors — as a figure, not just cited text.** |
| B - In-Vehicle Maintenance and Repair (shift linkage/range sensor, external seals, cooler/thermostat, valve body inspection, accumulator/servo, electrical component service, fluid/filter service) | `notes/electronics.txt` (TCM-connected sensors/solenoids, partially relevant); `notes/hydralics.txt` (pump types, partially relevant) | Indirect — notes explain component theory, not in-vehicle service/inspection procedure | Unassessed | No notes yet address valve body mating-surface inspection, accumulator/servo bore inspection, or fluid/filter replacement procedure — this is a full gap. |
| C - Removal, Inspection, and Installation (R&I procedure; disassembly/assembly; planetary gear assembly, bushings/bearings, drive chains/belts, final drive; friction/reaction units — clutch pack, one-way clutch, bands/drums) | `note/notes.md` (2026-09-22, clutch/band application chart across all ranges, OWC role by gear, general planetary-gear input/reaction/output rules); `notes/powerflowetc.txt` (2026-09-23, simple/Simpson/Ravigneaux/Lepelletier gear sets, gear-ratio calculation method, synchronous vs. nonsynchronous shift design) | Learner's own condensed instructor/textbook notes; strong conceptual coverage of planetary gear assembly and friction/reaction theory | Unassessed on procedure (torque converter install, end-play/preload measurement, clutch pack clearance) | Good foundation for "inspect components of the planetary gear assembly" and one-way-clutch/band-drum theory; no notes yet on R&I procedure, end-play/preload measurement, or clutch-pack clearance measurement. |

## Findings and meaningful practice misses

Record the question, DOCUMENTED / INFERRED / OPEN finding, source and application, explanation or worked example, and remaining limitation. Distinguish student reports and teaching analogies from verified mechanisms. Keep resolved findings visible with dated outcomes.

If the learner uses an owned question bank, record only the source/question identifier, the concept missed, and the corrected reasoning needed here. Do not copy the full proprietary question or answer explanation.

### Web-first research pass, 2026-09-29 (gap-filling, no guide built)

Targets were the three gaps already named in the coverage table above. This is public teaching/technician material only — verify against a primary manufacturer source (SI, ATSG, or the specific unit's tech manual) before it goes into any procedure-level guide, and treat any number below as a starting point to confirm, not a spec to quote as-is.

**A - General: transmission type identification.** DOCUMENTED (consistent across multiple independent public sources, accessed 2026-09-29): torque-converter automatics use a fluid coupling (pump/turbine) into a planetary gearset — this is what all of Logan's current notes describe. A dual-clutch transmission (DCT) has no torque converter; it's mechanically two manual gearboxes (odd/even gear sets) each with its own clutch, and it should not be idled/crept at very low speed the way a torque-converter auto can be, since that loads the clutch instead of a fluid coupling. A CVT uses no fixed gear ratios at all — two variable-diameter pulleys and a belt/chain — so questions about "gear ratio" or planetary members don't apply to it. Application boundary: this is enough to answer an A2 "identify transmission type" question at the classification level; it says nothing about hybrid/electrified drive integration, which stayed OPEN (not covered in this pass). Sources: [Motor1 automatic transmission types explainer](https://www.motor1.com/features/798467/automatic-transmission-types-explained/), [CarsGuide torque converter/CVT/dual-clutch comparison](https://www.carsguide.com.au/car-advice/torque-converter-cvt-dual-or-single-clutch-autos-whats-the-difference-33411).

**A - General: OBD II monitor readiness and DTC clearing.** DOCUMENTED: a "monitor" is a PCM self-test for an emissions-related system that reports Ready/Complete only after its specific enable criteria (temperature, load, speed, timing conditions) are met during a drive cycle; clearing DTCs (or a battery disconnect/reprogram) resets all monitors to "Incomplete," and a drive cycle must be re-run to set them again before an inspection or repair-verification will read clean. Application boundary: this is the general OBD II principle behind A2 task-list item A.6-A.7 (enable criteria, MIL operation, clearing/verifying via a scan tool); it is not transmission-specific and doesn't cover which drive-cycle conditions a particular TCM/PCM requires — that needs the vehicle's own SI. Sources: [OBD Auto Doctor readiness monitors explainer](https://www.obdautodoctor.com/tutorials/obd-readiness-monitors-explained/), [AutoDTCs OBD-II readiness monitors explained](https://autodtcs.com/obd2-readiness-monitors-explained/).

**B - Valve body / accumulator / servo inspection.** DOCUMENTED (general procedure, from rebuilder-industry technical sources, not a specific transmission's manual): valve bore inspection starts with the most active valves (main regulator first), removing the end plug and pushing the valve to the end of travel to check for smooth movement and even spring compression, then withdrawing it with a slight rotation — a catch or drag indicates a worn bore or bent valve; bore openings should be checked for nicks/ridges by dragging a pick along the chamfer edge. Accumulator/servo bores wear or score and their seals age, which shows up as harsher/inconsistent shifts (lost cushioning) or bang-shifts/flare if a piston sticks. Application boundary: this is generic technique language from Sonnax/Transmission Digest rebuilder content, useful for understanding *what* an A2 question is asking about and *why* a symptom points to this area — it is not a step-by-step service procedure for any one valve body and does not replace SI torque specs or bore-tolerance numbers. Sources: [Sonnax valve body inspection and rebuilding](https://www.sonnax.com/tech_resources/172-valve-body-inspection-and-rebuilding), [Transmission Digest valve-body bore preparation](https://www.transmissiondigest.com/valve-body-bore-preparation/).

**C - End play and clutch-pack clearance measurement.** DOCUMENTED (general method): end play is measured with a dial indicator and corrected by changing thrust-washer/shim thickness if out of spec; clutch-pack clearance is adjustable by three methods — shims, selective snap rings, or (on some units) an adjustment screw — where shims/snap rings take up the extra space so the apply piston travels a controlled distance before the pack engages. INFERRED, flagged as a shop rule of thumb rather than a verified universal spec: one rebuilder source states "about .008–.009 in of clearance per friction plate" as a starting point; another source's ".005–.036 in" end-play range reads as a specific transmission's number picked up mid-context, not a universal spec — do not treat either figure as authoritative for any given unit without checking that unit's SI. Application boundary: this covers the *method* A2 task-list items C.8–C.10/C.19–C.20 ask about (how end play and clutch-pack clearance are measured and adjusted) but supplies no verified numeric spec for any specific transmission. Sources: [Sonnax clutch release clearance 101](https://www.sonnax.com/tech_resources/81-clutch-release-clearance-101), [Transmission Digest — setting endplay on the 4L60/E](https://www.transmissiondigest.com/all-work-and-no-play-setting-endplay-to-prevent-4l60-e-gear-train-failure/).

**General A2 exam strategy (not content, not a question bank).** DOCUMENTED, publicly available test-taking advice, not secure ASE content: evaluate each Technician A/Technician B statement independently — read and judge Tech A alone, then Tech B alone, before comparing them, since letting one statement color the other is the most commonly reported mistake; "both are correct" and "both are wrong" are legitimate answers, not automatic traps; if a question is a hydraulic/mechanical clutch-and-band chart with a Tech A/B pair, cross-check both against the same range/chart rather than relying on memory of it. This is process advice only — no ASE questions were copied or paraphrased. Sources: [Apex Technation ASE test day strategy](https://apextechnation.com/articles/ase-test-day-strategy), general A2-focused practice-test framing at [freeasestudyguides.com A2 practice test](https://www.freeasestudyguides.com/a2-automatic-transmission-test.html).

**Still open after this pass:** scan-tool bidirectional control usage, TCM/module reprogram-and-relearn procedure detail, hydraulic pressure test procedure/spec interpretation, torque converter stator one-way-clutch failure diagnosis, and hybrid/electrified drive transmission identification — none of these got real research coverage this round and remain gaps in the coverage table above.

## Sources

Record only what was actually accessed. Public notes, lessons and videos may supply leads; verify important technical claims with applicable primary sources. Link commercial sources and record any user-supplied edition/pages without assuming access to the rest of the book.

- [ASE Automobile Study Guide PDF](https://ase.com/wp-content/uploads/ASE_Automobile_Study_Guide.pdf) — © ASE 2026, A2 task list pages 10–15. Accessed 2026-09-29.
- [Motor1 — automatic transmission types explained](https://www.motor1.com/features/798467/automatic-transmission-types-explained/) — accessed 2026-09-29.
- [CarsGuide — torque converter/CVT/dual-clutch comparison](https://www.carsguide.com.au/car-advice/torque-converter-cvt-dual-or-single-clutch-autos-whats-the-difference-33411) — accessed 2026-09-29.
- [OBD Auto Doctor — OBD2 readiness monitors explained](https://www.obdautodoctor.com/tutorials/obd-readiness-monitors-explained/) — accessed 2026-09-29.
- [AutoDTCs — OBD-II readiness monitors explained](https://autodtcs.com/obd2-readiness-monitors-explained/) — accessed 2026-09-29.
- [Sonnax — valve body inspection and rebuilding](https://www.sonnax.com/tech_resources/172-valve-body-inspection-and-rebuilding) — accessed 2026-09-29.
- [Transmission Digest — valve-body bore preparation](https://www.transmissiondigest.com/valve-body-bore-preparation/) — accessed 2026-09-29.
- [Sonnax — clutch release clearance 101](https://www.sonnax.com/tech_resources/81-clutch-release-clearance-101) — accessed 2026-09-29.
- [Transmission Digest — setting endplay to prevent 4L60/E gear train failure](https://www.transmissiondigest.com/all-work-and-no-play-setting-endplay-to-prevent-4l60-e-gear-train-failure/) — accessed 2026-09-29.
- [Apex Technation — ASE test day strategy](https://apextechnation.com/articles/ase-test-day-strategy) — accessed 2026-09-29.
- [freeasestudyguides.com — A2 practice test page](https://www.freeasestudyguides.com/a2-automatic-transmission-test.html) — accessed 2026-09-29 (framing/strategy only, no questions copied).
