# A8 coverage and research

Status: **Official reference verified; weighted task map built (2026-10-22).** No class notes yet, so nothing is mapped to notes. No guide built.
Created: 2026-09-20. Last updated: 2026-10-22.

## Official reference

Verified 2026-10-22: [ASE Automobile Study Guide PDF](https://ase.com/wp-content/uploads/ASE_Automobile_Study_Guide.pdf) (© ASE 2026, created 2025-12-05), pages 44–49, "Test Specifications and Task List — Engine Performance (Test A8)". The copy downloaded 2026-10-22 is byte-identical to the one already saved at `../mantrans/sources/ase/ASE_Automobile_Study_Guide_2026.pdf` (sha256 `3a5a4f36…`), so that copy is current. It is not duplicated here.

**Format (page 43):** 60 questions, 50 of them scored; the other 10 are unscored trial questions you can't tell apart, so answer all 60. 75 minutes, which is about 1.25 minutes per question. That's tighter than A2 (55 questions in 75 minutes). Recertification is 25 questions in 45 minutes.

| Content area | Questions | % of test | Tasks | Questions per task (average) |
|---|---:|---:|---:|---:|
| A. General Diagnosis | 12 | 24% | 23 | ~0.52 |
| B. Ignition System Diagnosis and Repair | 8 | 16% | 7 | ~1.14 |
| C. Fuel, Air Induction and Exhaust Systems | 9 | 18% | 14 | ~0.64 |
| D. Emissions Control Systems | 8 | 16% | 12 | ~0.67 |
| &nbsp;&nbsp;D.1 PCV | 1 | | 2 | 0.50 |
| &nbsp;&nbsp;D.2 EGR | 2 | | 3 | ~0.67 |
| &nbsp;&nbsp;D.3 Secondary AIR and catalytic converter | 2 | | 4 | 0.50 |
| &nbsp;&nbsp;D.4 EVAP | 3 | | 3 | **1.00** |
| E. Computerized Engine Controls | 13 | 26% | 11 | **~1.18** |
| **Total** | **50** | 100% | 67 | |

INFERRED: ASE does not publish weights per task, so the per-task figure is only an average. It's the same method used for A2. Takeaways:

- **E (computerized controls) and B (ignition) give the most questions per task.** Together they are 21 of 50 questions, and both play to Logan's electrical strength. Area C fuel injection includes GDI and port injection, and the question says which system the vehicle has (page 45 note).
- **EVAP is the highest-yield emissions topic** (3 questions from 3 tasks).
- **A is the biggest area but the thinnest per task** (23 tasks). Engine mechanical tests (vacuum, compression, leak-down, power balance) plus cooling, battery, starting and charging all sit here. Learn the principle and which direction each reading points, not the procedures.

**The 10 public sample questions (pages 47–49) show the style.** Summarized here, not copied:

1. **Ignition schematic:** a misfire traced to high resistance at one point in the coil circuit. (Reading a schematic.)
2. **PCV, Tech A/B:** the valve is pulled and plugged with no change in how the engine runs. A plugged hose to the manifold explains it; a stuck-open valve doesn't. (Two-direction reasoning.)
3. **Compression:** one cylinder low, and the wet test doesn't change the reading. That points to a valve, not the rings. (Which direction the wet test points.)
4. **Blue smoke, Tech A/B:** blocked head oil-return passages, not the thermostat.
5. **"Coolant temperature below thermostat regulating temperature" DTC:** thermostat stuck open.
6. **Vacuum gauge** fluctuating rapidly at 2,000 rpm: a broken valve spring.
7. **No spark and no injector pulse:** the CKP sensor. (The common input to both.)
8. **Returnless EFI with fuel pressure above spec:** a failed regulator.
9. **EVAP small-leak DTC:** a torn fuel-cap O-ring.
10. **EXCEPT question on EGR insufficient flow:** a stuck-open valve is the one that can't cause it.

INFERRED from those: as on A2, most questions start from a symptom and ask for the cause, and several hinge on **which direction a reading points** (wet vs. dry compression, gauge behavior, pressure high vs. low). That is the same kind of reasoning as Logan's A2 stall-speed misses. EXCEPT questions appear.

### Full task list (2026-10-22)

Task wording is shortened from the ASE guide. **Carryover** marks overlap with completed courses (A2 `autotrans/`, A3 `mantrans/`) or Logan's stated strengths. **L1** marks a matching L1 task (`../l1/research.md`); A8 study for those tasks feeds L1 directly. A **Notes** column gets added when class notes arrive.

| Task | Shortened statement | Carryover | L1 | Priority |
|---|---|---|---|---|
| A.1 | Verify complaint, visual, road test | A2 A.2 (same reasoning) | A.1 | Low |
| A.2 | Research SI, history, TSBs, recalls | A2 A.3 | A.3–A.4 | Low |
| A.3 | Diagnose base engine mechanical | — | A.9 | Medium |
| A.4 | Noise and vibration | A3 vibration reasoning | — | Low |
| A.5 | Exhaust color, odor, sound | — | — | **High** (sample Q4) |
| A.6 | Manifold vacuum/pressure tests | — | — | **High** (sample Q6) |
| A.7 | Cylinder power balance | — | — | Medium |
| A.8 | Cranking, relative, running compression | — | — | **High** (sample Q3) |
| A.9 | Leak-down test | — | — | Medium-high (pairs with A.8) |
| A.10 | Scope / analyzer / scan tool diagnosis | Electrical strength | B.17–B.18 | Medium |
| A.11 | Verify valve adjustment | — | — | Low |
| A.12 | Cam timing, VVT, VVL | A2 hydraulic solenoid control is similar | A.7 | Medium |
| A.13 | Oil-related emissions/driveability (pressure, quality, type) | — | — | Medium (feeds VVT) |
| A.14 | Operating temp, coolant, pressure test | — | A.8 | Medium (sample Q5) |
| A.15 | Fans, fan clutch, active grille shutters | Electrical strength | — | Low |
| A.16 | Read schematics and symbols | Electrical strength | — | Medium (sample Q1) |
| A.17 | Battery condition, connections, key-off drain | Electrical strength | — | Low-medium |
| A.18 | Starting-system failures causing performance problems | Electrical strength | — | Low |
| A.19 | Starter current draw | Electrical strength | B.15 | Low |
| A.20 | Starter/charging voltage drop | Electrical strength | B.14 | Medium |
| A.21 | Charging-system failures | Electrical strength | — | Low |
| A.22 | Belts, pulleys, tensioners | — | — | Low |
| A.23 | Starter/charging control circuits | Electrical strength | — | Low |
| B.1 | Ignition symptoms → root cause | — | C.8, C.12 | **High** |
| B.2 | Ignition DTCs | — | C.6 | **High** |
| B.3 | Primary circuit | Electrical strength | C.7 | Medium-high |
| B.4 | Secondary circuit | — | C.10 | Medium-high |
| B.5 | Coils | — | C.10 | Medium-high |
| B.6 | Ignition sensors (CKP/CMP) | A2 speed-sensor (reluctor) theory | B.17 | **High** (sample Q7) |
| B.7 | ICM/PCM, programming | A2 A.25 | B.6 | Low-medium |
| C.1 | Fuel symptoms → root cause | — | D.10 | **High** |
| C.2 | Fuel/air DTCs, **fuel trim** and scan data | — | **D.5** | **Highest in C** (core L1 skill too) |
| C.3 | Tank, filler neck, cap, lines | — | — | Low |
| C.4 | Pump, pump assembly, filter | — | D.12 | Medium |
| C.5 | Pump control circuits | Electrical strength | D.12 | Medium |
| C.6 | Pressure regulation, fuel quality, pressure/volume test | — | D.11 | **High** (sample Q8) |
| C.7 | Throttle body service, relearn | — | D.9 | Medium |
| C.8 | Injectors, high-pressure lines, rails (GDI) | — | D.12 | Medium |
| C.9 | Air filtration | — | — | Low |
| C.10 | Intake, runners, vacuum pumps | — | — | Low |
| C.11 | Vacuum leaks, restrictions, unmetered air | — | D.9 | **High** (links to fuel trim) |
| C.12 | Exhaust parts, O2 and A/F sensors | — | D.5 | Medium |
| C.13 | Exhaust restriction/leak tests | — | A.11 | Medium |
| C.14 | Turbo/supercharger | — | — | Low-medium |
| D.1.1–2 | PCV diagnosis, components | — | E (subsystem list) | Medium (sample Q2) |
| D.2.1–3 | EGR diagnosis, scan data/DTCs, components | — | E | Medium-high (sample Q10) |
| D.3.1–4 | Secondary AIR, catalytic converter | — | E | Medium |
| D.4.1–3 | EVAP diagnosis, scan data/DTCs, components | — | E, F.16 | **High** (3 questions, sample Q9) |
| E.1 | Retrieve DTCs, monitor status, freeze frame | A2 A.6 | B.8 | **High** |
| E.2 | OBD II enable criteria, permanent DTCs, MIL | A2 A.6 | B.7 | **High** |
| E.3 | Diagnose with DTCs | — | B.11 | **High** |
| E.4 | Diagnose without DTCs | — | B.11 | **High** |
| E.5 | Scan tool / DMM / DSO on sensors, actuators, circuits | Electrical strength; A2 A.5 | B.17–B.19 | **High** |
| E.6 | Voltage, voltage drop, amps, resistance | Electrical strength | B.14–B.16 | Medium (likely a strength) |
| E.7 | Power and ground distribution | Electrical strength | B.14 | Medium |
| E.8 | PCM replace and program | A2 A.25 | B.6 | Low |
| E.9 | Interrelated systems (cruise, theft, traction, torque management, A/C, aftermarket) | — | B.13 | Medium |
| E.10 | Network/bus failures | Electrical strength | B.12 | Medium |
| E.11 | Clear DTCs, run monitors, verify repair | A2 sample Q7 (clear with scan tool) | B.24 | Medium |

Priority here comes from the official weights, the sample questions and Logan's known pattern only. Revisit when class notes show what the instructor emphasizes.

## Source map and coverage

Add rows as personal notes or public resources are actually inspected. A source on disk isn't automatically reviewed, and a missing lesson isn't automatically a learner weakness.

| Topic / task anchor | Source/file and location | Access / evidence quality | Learner evidence | Next question |
|---|---|---|---|---|
| Whole test (spec, tasks, samples) | `../mantrans/sources/ase/ASE_Automobile_Study_Guide_2026.pdf` pp. 43–49 | Official, full PDF read 2026-10-22 | None yet | Map class notes when they arrive |

## Findings and meaningful practice misses

Record the question, the finding (DOCUMENTED / INFERRED / OPEN), source and where it applies, the explanation or a worked example, and what's still uncertain. Keep student reports and teaching analogies separate from verified mechanisms. Keep resolved findings visible with dated outcomes.

If the learner uses an owned question bank, record only the source/question identifier, the concept missed, and the corrected reasoning needed here. Do not copy the full proprietary question or answer explanation.

- None yet.

## Sources

- [ASE Automobile Study Guide PDF](https://ase.com/wp-content/uploads/ASE_Automobile_Study_Guide.pdf): © ASE 2026, A8 on pp. 43–49. Accessed 2026-10-22. Identical to the local copy in `../mantrans/sources/ase/`.
