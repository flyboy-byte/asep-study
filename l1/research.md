# L1 coverage and research

Status: **Official reference verified; weighted task map built (2026-10-22).** No class notes yet. No guide built.
Created: 2026-09-20. Last updated: 2026-10-22.

## Official reference

Verified 2026-10-22, both saved in `sources/ase/`:

- [ASE L1 Study Guide PDF](https://ase.com/wp-content/uploads/ASE_L1_Study_Guide.pdf) → `ASE_L1_Study_Guide_2026.pdf` (© ASE 2026, created 2025-12-04, 15 pp). An older 2025 edition exists on es.ase.com; use the 2026 one.
- [L1 Composite Vehicle Type 4 Reference Booklet](https://ase.com/wp-content/uploads/L1_CV4.pdf) → `L1_Composite_Vehicle_Type_4.pdf` (created 2025-04-09, 36 pp).

**Format and eligibility (guide pp. 3–4, DOCUMENTED):**

- 60 questions, 50 of them scored. **150 minutes**, double A8's time per question, because many questions require looking things up in the reference booklet. Recertification (L1R) is 50 questions in 135 minutes.
- **You must have passed A8 before you can register for L1.** So A8 comes first, whatever the class order.
- Certification also requires **3 years of documented work experience**, and appropriate vocational training may count toward part of it. Whether ASEP training plus Logan's dealership time is enough is **OPEN**; check `workexp.ase.com` when it matters.
- **"A significant number of the test questions will require you to use this reference."** The booklet is shown as an electronic pop-up during the test, with no printed copy, so learning its layout beforehand is part of the prep.
- Terms follow SAE J1930/J2012. A DTC in a question always comes with its number and description. The guide's glossary (pp. 8–10) defines fuel trim: above 0% means the ECM is adding fuel (longer injector pulse); STFT reacts to the O2 or A/F sensor; LTFT is the learned correction.

| Content area | Questions | % of test | Tasks | Questions per task (average) |
|---|---:|---:|---:|---:|
| A. General Powertrain Diagnosis | 6 | 12% | 15 | 0.40 |
| B. Computerized Powertrain Controls (incl. OBD II) | 16 | **32%** | 24 | ~0.67 |
| C. Ignition System Diagnosis | 6 | 12% | 15 | 0.40 |
| D. Fuel and Air Induction Systems | 8 | 16% | 16 | 0.50 |
| E. Emission Control Systems | 8 | 16% | 16 | 0.50 |
| F. I/M Failure Diagnosis | 6 | 12% | 17 | ~0.35 |
| **Total** | **50** | 100% | 103 | |

The text extraction scrambles the weights table, so the counts were checked against each area's heading in the task list ("(6 questions)" and so on). They add up to 50.

**How L1 is built (INFERRED from the task list):**

- **Every area repeats the same generic tasks:** verify the concern, check for tampering, find service information, research how the system works, pick a procedure, judge which data matters, root cause (single, multiple and repeated failures), and verify the repair. That is about 8–9 of each area's tasks, so the content-specific tasks get more questions than the averages suggest. They are:
  - **B** (largest area): reprogramming, OBD II enable criteria and readiness, the network, the immobilizer, voltage-drop/current/resistance tests, sensor and actuator tests by scan data or waveform, and confirming scan data by measuring directly (B.19).
  - **C:** ignition under load, ignition waveforms, timing control.
  - **D:** **fuel trim versus O2/A/F sensors versus other sensor data (D.5)**, TAC, fuel quality and pressure/volume, injector and pump evaluation (including digitally controlled pumps).
  - **E:** what effect each emission-control fault has on exhaust gases, and using the gas analyzer.
  - **F:** **five-gas analysis**: HC, CO, NOx, CO2 and O2 relationships, no-load versus loaded-mode HC/CO/NOx failures, OBD I/M (MIL, readiness, communication), and the fuel cap test.
- **New compared with A8:** five-gas analysis (F, E.11) and the reference booklet. Everything else goes deeper into the same A8 topics.

**Sample questions (guide pp. 11–13; 7 in total, summarized):** Questions 1–4 need the reference booklet. They read injector voltages on the composite vehicle (Tech A/B on open coil vs. stuck-on), a MAF range/performance DTC with scan data, and an EVAP P0442. Questions 5–7 are answered without it: a P0301 misfire, a port-injected engine that runs rough at idle but smooths out with rpm, and lack of power at high speed and load.

**The reference booklet (CV4) contains** (from its table of contents):

- **Vehicle and modules:** the engine and transmission, then the modules (ECM, fuel pump control module, TCM, instrument cluster, immobilizer).
- **Systems:** electronic throttle, exhaust, fuel delivery, ignition, immobilizer, ORVR EVAP, fuel injection, VVL, VVT.
- **Inputs and outputs:** every sensor, with its range and behavior, and every actuator.
- **OBD:** the monitors, readiness, warm-up cycle, trip and drive cycle, freeze frame, and the rules for storing and clearing DTCs and turning the MIL on and off.
- **Wiring:** a pin/component cross-reference.
- **Scan tool data chart** with normal values (pp. 28–29).
- **Four electrical diagrams** (pp. 30–33) and a system cutaway (p. 34).

INFERRED: the highest-yield L1 prep is learning to *use* this booklet quickly: knowing where the normal-value chart, monitor rules and diagrams are, so a question becomes a lookup plus one reasoning step.

### Overlap with A8

L1 tasks that match an A8 task are marked in `../engine-performance/research.md` (L1 column). For A8 material, point to A8 research and guides rather than copying them here. L1-only material goes in this folder:

- five-gas / I/M (F; E.10–E.11)
- the reference booklet and how to navigate it
- confirming scan data by direct measurement (B.19–B.20)
- root cause of multiple and repeated failures
- tampering and modifications (tire size, transmission, final drive: A.10)

## Source map and coverage

| Topic / task anchor | Source/file and location | Access / evidence quality | Learner evidence | Next question |
|---|---|---|---|---|
| Whole test (spec, tasks, glossary, samples) | `sources/ase/ASE_L1_Study_Guide_2026.pdf` | Official, full PDF read 2026-10-22 | None yet | — |
| Composite vehicle (contents, sensors, OBD rules, data chart, diagrams) | `sources/ase/L1_Composite_Vehicle_Type_4.pdf` | Official; table of contents read 2026-10-22, body not yet studied | None yet | Walk through it once A8 study is under way |

## Findings and meaningful practice misses

Record the question, the finding (DOCUMENTED / INFERRED / OPEN), source and where it applies, the explanation or a worked example, and what's still uncertain. Keep student reports and teaching analogies separate from verified mechanisms. Keep resolved findings visible with dated outcomes.

If the learner uses an owned question bank, record only the source/question identifier, the concept missed, and the corrected reasoning needed here. Do not copy the full proprietary question or answer explanation.

- OPEN: does Logan's ASEP training plus dealership time meet the 3-year L1 work-experience requirement? Check `workexp.ase.com`. This only affects when certification is awarded, not taking the test.

## Sources

- [ASE L1 Study Guide](https://ase.com/wp-content/uploads/ASE_L1_Study_Guide.pdf): © ASE 2026. Accessed 2026-10-22. Saved locally.
- [L1 Composite Vehicle Type 4 Reference Booklet](https://ase.com/wp-content/uploads/L1_CV4.pdf): accessed 2026-10-22. Saved locally.
- [ASE L1 test page](https://ase.com/tests/l1/): A8 prerequisite, seen in search results only (the guide p. 3 says the same, and that is the citation).
