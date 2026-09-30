# Scan-Tool Bidirectional Controls in Automatic Transmission Diagnosis (ASE A2 level)

Research date / access date for every source below: 2026-09-30.

**Read this before using anything here.** Every attempt to open a full page this session was blocked by the network egress proxy (ase.com, motor.com, vehicleservicepros.com, transmissiondigest.com, sonnax.com, gearsmagazine.com, static.nhtsa.gov, snapon.com, images.oreillyauto.com, ls2.com all returned EGRESS_BLOCKED). A local copy of the ASE study guide exists at `mantrans/sources/ase/ASE_Automobile_Study_Guide_2026.pdf`, but no working PDF text extractor was available (no pdftotext, and pypdf failed to import). So **every finding below was checked only against search-engine result text for the cited URL, not a full read of the page.** The tag rules are adjusted to match:
- **DOCUMENTED (snippet)**: the claim appeared in search text attributed to the cited URL, and ideally agrees with a second source. It should still be confirmed with a full read before it goes into a print guide.
- **INFERRED**: reasoned from the cited findings.
- **OPEN**: unresolved.
Scope labels: **Universal**, **GM-specific**, **Chrysler-specific**, and **SI** (needs the vehicle's Service Information to confirm).

---

## 1. What "bidirectional" means vs. a data-only scan tool, and how ASE frames it

### Takeaway
A bidirectional scan tool both reads module data and sends commands that make the module drive its outputs (solenoids, relays) or run tests. A data-only (code/PID) reader can only read. ASE's A2 task list names "bidirectional controls" next to scan data and DTCs as a way to diagnose transmission electronic systems, and pairs it with DMM testing before a solenoid is replaced.

### Cited Findings
- DOCUMENTED (snippet), Universal: ASE A2 task wording (Content Area A, Transmission/Transaxle Diagnosis) says to use scan tool data, bidirectional controls, and/or DTCs to diagnose electronic systems, interpret the readings, and decide what to do next. It also says to inspect and test solenoids and circuits (search summary of this item: "with a bidirectional scan tool and a multimeter before replacement"). — [ASE Automobile Study Guide PDF](https://ase.com/wp-content/uploads/ASE_Automobile_Study_Guide.pdf); [ASE Automobile Study Guide 2025 PDF](https://www.ase.com/uploads/ASE_Automobile_Study_Guide_2025.pdf). Exact verbatim wording and item numbers are **OPEN** because the PDF could not be read (see Gaps).
- DOCUMENTED (partial local read), Universal: the local ASE 2026 guide's readable page headers show "A. Transmission/Transaxle Diagnosis (26 questions)" on page 10 and "C. Transmission/Transaxle Removal, Inspection, and Installation (7 questions)" on page 12. The page-14 sample-question figure labels a TCM, ATF temperature sensor, lock-up duty solenoid, primary up/down solenoids, secondary solenoid, and control valve body. — local file `mantrans/sources/ase/ASE_Automobile_Study_Guide_2026.pdf` (raw stream text only; the body text is CID-encoded and could not be read).
- DOCUMENTED (snippet), Universal: Motor Age defines "bidirectional control" as sending and receiving information between two devices. It calls the scan tool "the primary bidirectional control device," because it sends information to vehicle control modules and receives information from them. — [Motor Age, "Bidirectional Scanner Controls: The 2-Way Diagnostic Highway" (Apr 2005)](https://www.motor.com/magazine-summary/bidirectional-scanner-controls-2-way-diagnostic-highway-april-2005/)
- DOCUMENTED (snippet), Universal: manufacturers call bidirectional controls by different names: functional tests, actuator tests, inspection tests, system tests. Tool makers set this against read-only OBD-II scanners, which can only read codes and data. — [SmartSafe bidirectional scanner explainer](https://www.newsmartsafe.com/industry-news/bidirectional-scanner); [Foxwell bidirectional explainer](https://www.foxwelldiag.com/blogs/car-diagnostic/obd2-scanner-with-bidirectional-controls). These are vendor/marketing sources, suitable for the definition only.
- DOCUMENTED (snippet), Universal: Motor Age's transmission scan-tool article says that a tool which gives both information and bidirectional control still leaves the tech to process and interpret the data. — [Motor Age, "Using a Scan Tool for Transmission Diagnosis"](https://www.motor.com/magazine-summary/using-a-scan-tool-for-transmission-diagnosis/) (PDF version: [motor.com/magazinepdfs/062010_08.pdf](https://www.motor.com/magazinepdfs/062010_08.pdf), which appears to be the June 2010 issue).
- GM tool names, GM-specific: GDS2 runs on GM's MDI pass-thru interface, and the SilveradoSierra 6L80 thread says GDS2 became necessary on trucks from about 2014. — [SilveradoSierra 6L80 information thread](https://www.silveradosierra.com/threads/gm-6l80-transmission-information-thread.753826/). This is a forum, so the date is low-confidence.

### Inferences
- INFERRED, Universal: for A2, the useful difference is not the tool's brand but what it can do. A code reader can tell you a circuit DTC set. Only a bidirectional tool lets you command a specific output and then watch what happens (a click, a pressure change, a ratio change, a change in current or slip PIDs). ASE pairs "bidirectional controls" with "multimeter," which points to the expected sequence: command the output, then meter the circuit before replacing the part.
- INFERRED: expect ASE questions to use generic terms ("bidirectional control," "output test," "commanded vs. actual"), not GDS2/Tech2 menu names.

### Gaps
- OPEN: exact verbatim A2 task wording and item numbers (for example, whether it is A.x "Diagnose electronic transmission control systems using a scan tool…" or similar). The ASE PDF was blocked online and unreadable locally. `autotrans/research.md` notes the task list was verified on 2026-09-29 (pages 10–15), so check the wording against that pass or open the local PDF in a viewer.
- OPEN: no NATEF/ASEP-specific curriculum text on bidirectional control was reached.

---

## 2. Which A2 diagnostic decisions depend on commanding outputs

### Takeaway
The main commanded tests are: (1) shift-solenoid and gear commands, to see whether the transmission follows the command; (2) line-pressure/PC (EPC) solenoid control with a mechanical pressure gauge installed, stepping pressure up and down; (3) TCC apply/release commands while watching TCC slip; (4) OEM clutch/slip tests (for example the Chrysler 41TE clutch test); and (5) special functions such as adapt reset and GM's Transmission Service Fast Learn after repairs.

### Cited Findings
- DOCUMENTED (snippet), Universal: use active tests to command solenoids on and off, and watch pressure, shift behavior, and live data (line pressure, clutch/gear engagement, solenoid status, RPM, VSS). — [Tire Review, "Diagnosing Electrical/Electronic Automatic Transmission Failures"](https://www.tirereview.com/diagnosing-automatic-transmission-failures/); [Motor Age, "Using a Scan Tool for Transmission Diagnosis"](https://www.motor.com/magazine-summary/using-a-scan-tool-for-transmission-diagnosis/)
- DOCUMENTED (snippet), GM-specific (Hydra-Matic 6-speed 6T70/6L80 family), SI: the scan tool can control the line pressure control solenoid **only in Park and Neutral with engine speed below 1500 RPM**. For a line-pressure check, raise and lower the solenoid command in steps of about **100 kPa (15 psi)** and let the pressure settle between steps. — search result text tied to [GM Tech Info 6T70/6L80 (Scribd)](https://www.scribd.com/document/79508773/Gm-Tech-Info-6t70-6l80) and a GM service document hosted at [NHTSA MC-10181692 (GM, ©2020)](https://static.nhtsa.gov/odi/tsbs/2020/MC-10181692-9999.pdf). The search tool merged several results, so it is not certain which of the two documents contains this sentence. Treat it as GM 6-speed SI-style text and confirm before quoting. It is not a universal rule.
- DOCUMENTED (snippet), GM-specific: the same Hydra-Matic 6-speed material says the TCM controls shift points, TCC apply/release, and line pressure. It lists line pressure control solenoid DTCs **P0961 (performance), P0962 (low voltage), and P0963 (high voltage)**. — [GM Tech Info 6T70/6L80 (Scribd)](https://www.scribd.com/document/79508773/Gm-Tech-Info-6t70-6l80). The P0962/P0963 circuit-low/high meanings follow generic SAE J2012 P096x structure, but confirm them per vehicle (SI).
- DOCUMENTED (snippet), Chrysler-specific (41TE/A604): Chrysler provides a "Clutch Test" that uses the rpm sensors plus bidirectional solenoid control to find a slipping clutch. The vehicle is brake-torqued at **no more than 20% throttle for no more than 5 seconds**. **Any scan-tool rpm reading other than 0 means that element is slipping.** — [Motor Age, "Using a Scan Tool for Transmission Diagnosis"](https://www.motor.com/magazine-summary/using-a-scan-tool-for-transmission-diagnosis/)
- DOCUMENTED (snippet), GM-specific (6-speed/later RWD and FWD), SI: GDS2 path for the post-repair special function: Module Diagnostics → Transmission Control Module → Configuration/Reset Functions → Transmission Service Fast Learn. It is done in the stall with no driving. After replacing a transmission, valve body, or TCM, refresh the characterization data and then run Fast Learn. **Clearing and relearning adapts "should not be considered a repair process"** and is only meant to follow an actual transmission repair. — GM bulletin [14-07-30-001G (Mar 2017) via NHTSA](https://static.nhtsa.gov/odi/tsbs/2017/MC-10138017-9999.pdf); [GM service documents via NHTSA 2019](https://static.nhtsa.gov/odi/tsbs/2019/MC-10169298-9999.pdf) and [2022](https://static.nhtsa.gov/odi/tsbs/2022/MC-10211684-0001.pdf); [GM TechLink "Transmission Adaptive Functions" (forum repost)](https://www.cadillacvnet.com/forums/threads/gm-techlink-transmission-adaptive-functions.1132/)
- DOCUMENTED (snippet), Universal: in road-test use, a scan tool lets you watch or control solenoids, TCC apply/release, line-pressure commands, adaptive resets/clutch learn, and shift timing. You can compare commanded gear, commanded shift pressure, actual line pressure, desired vs. actual TCC slip, OSS, and ISS. — [Gears (ATRA), "Road Test With A Purpose"](https://gearsmagazine.com/magazine/road-test-with-a-purpose/)

### Inferences
- INFERRED, Universal: the commanded tests line up with A2 decisions this way:
  - "Is the no-shift or wrong gear electrical or internal?" → shift-solenoid/gear command.
  - "Is the pressure complaint the solenoid/TCM or the pump/regulator/leak?" → PC/EPC command with a gauge.
  - "Is the converter clutch failing to apply or slipping?" → TCC command plus the slip PID.
  - "Which clutch is slipping?" → OEM clutch test or ratio/slip PIDs.
  - "Did the repair take?" → adapt reset or fast learn, then a verification drive.
- INFERRED, GM-specific: because the GM line-pressure control is limited to Park/Neutral and low RPM, a line-pressure sweep is a stationary test with the gauge installed. It is not a road test.

### Gaps
- OPEN: GDS2/Tech2 output-control menu names and preconditions for 6L80/6T-series/10L shift-solenoid and gear commands (for example, whether a gear command needs vehicle speed within a window). No public GM source was reached.
- OPEN: whether 10-speed (10L80/10L90) or 8-speed (8L90) output controls differ. A Gears article "[8L90 Solenoid Strategies](https://gearsmagazine.com/magazine/8l90-solenoid-strategies/)" exists but could not be read.

---

## 3. Interpretation rules (commanded vs. actual; electrical vs. hydraulic/mechanical)

### Takeaway
The main rule is that **a scan-tool "command" or "desired" PID is what the module is asking for, not proof that it happened.** If the module commands something and the transmission does not respond (no ratio change, no pressure change, slip stays high), suspect a hydraulic or mechanical fault. If the module never commands it, or a circuit DTC is present, look first at inputs, wiring, or the module. Confirm pressure with a gauge, and confirm circuits with a DMM.

### Cited Findings
- DOCUMENTED (snippet, two sources), Universal: if the PCM/TCM commands a shift and the ratio does not change, an internal hydraulic or mechanical failure is likely. If it does not command a shift, an input, sensor, or electrical problem is likely. — [Gears (ATRA), "Road Test With A Purpose"](https://gearsmagazine.com/magazine/road-test-with-a-purpose/); agrees with [Tire Review](https://www.tirereview.com/diagnosing-automatic-transmission-failures/): "If command shows active but no pressure/shift change, suspect hydraulic or mechanical failure."
- DOCUMENTED (snippet, two sources), Universal: a commanded pressure on the scan tool does not mean the actual transmission pressure matches it. The data shows the PCM's command to the EPC solenoid, which *should* match the gauge. — [Transmission Digest, "Verify What the Scan Tool Is Telling You"](https://www.transmissiondigest.com/verify-what-the-scan-tool-is-telling-you/); agrees with [Sonnax, "Transmission Pressure Gauge: Why You Need It"](https://www.sonnax.com/tech_resources/125-transmission-pressure-gauge-a-diagnostic-tool)
- DOCUMENTED (snippet), Universal: run the pressure gauge alongside the scan tool and check that pressure changes in proportion to the amperage the TCM commands. A mismatch points to a solenoid or wiring problem rather than a mechanical fault. A scan tool alone is not a complete diagnosis ("the gauge tells you what the scanner cannot"). An intermittent solenoid fault may not set a DTC but will still show up as pressure variation on a live hydraulic test. — [Sun Transmissions, "Transmission Pressure Testing Guide"](https://suntransmissions.com/blogs/news/transmission-pressure-testing-guide-diagnosing-hydraulic-failures). This is a rebuilder blog, a medium-to-low quality source. Note a tension: it says a mismatch means the *solenoid/wiring*, but a pressure mismatch could also be a pump, regulator, or leak problem. See Inferences.
- DOCUMENTED (snippet), Universal: bidirectional capability is especially useful for testing shift solenoids and their circuits. — [Tire Review](https://www.tirereview.com/diagnosing-automatic-transmission-failures/)
- DOCUMENTED (snippet), Chrysler-specific: 41TE adaptive "Clutch Volume Index" (CVI) values. High CVI means longer fill time (worn clutches or leaks). Below-minimum CVI is caused by problems such as valve-body cross leaks, over-tightened packs, seized accumulator pistons, or excessive line pressure. Quoted normal ranges: **L/R 35–83, 2/4 20–77, OD 75–150, UD 24–70** (41TE only). — [Motor Age, "Using a Scan Tool for Transmission Diagnosis"](https://www.motor.com/magazine-summary/using-a-scan-tool-for-transmission-diagnosis/) (snippet). Confirm the numbers in SI.
- DOCUMENTED (snippet), GM-specific: GM's TCM watches ISS and OSS during commanded shifts to judge whether a shift is too fast (harsh) or too slow (soft), and adjusts the matching PC solenoid signal to hold shift feel. That is the "adapt" process. — [GM TechLink "Transmission Adaptive Functions" (repost)](https://www.cadillacvnet.com/forums/threads/gm-techlink-transmission-adaptive-functions.1132/); GM service documents via NHTSA ([2019](https://static.nhtsa.gov/odi/tsbs/2019/MC-10169298-9999.pdf)).

### Inferences
- INFERRED, Universal: a working decision table for A2 questions:
  | Observation after the command | Most likely area |
  | --- | --- |
  | Command sent, solenoid clicks/current changes, ratio/pressure responds correctly | Output path OK. Look at inputs, calibration, adapts, or an intermittent fault |
  | Command sent, solenoid clicks or current tracks command, but no ratio/pressure change | Hydraulic/mechanical (stuck valve, cross-leak, clutch/seal, pump/regulator) |
  | Command sent, no click, actual current ≠ commanded, circuit DTC (open/short/high/low) | Electrical: solenoid coil, harness, connector, TCM driver. Confirm with DMM |
  | Module never commands the shift/apply | Enable conditions or inputs (TFT, VSS/OSS, TPS, brake switch, range switch) or the module |
  | Commanded pressure ≠ gauge pressure, solenoid current tracks command | Hydraulic supply/regulation or leak (pump, pressure regulator, seals) |
  | Commanded pressure ≠ gauge, current does not track command | Solenoid/circuit/driver |
- INFERRED: "solenoid clicks" only proves the coil and plunger moved. It does not prove the valve it feeds strokes or that fluid reaches the clutch. That is why ASE-style reasoning puts "clicks but no shift" in the hydraulic/mechanical category.
- INFERRED: the Sun Transmissions "mismatch = solenoid/wiring" claim is too narrow on its own. The actual-vs-commanded **current** comparison separates electrical faults. The gauge-vs-commanded **pressure** comparison separates hydraulic faults. Use both together.

### Gaps
- OPEN: no public source with verifiable authorship directly stated "no command response plus circuit DTC = electrical." It is inferred from the paired rule above and standard circuit-DTC meanings.

---

## 4. Safety preconditions

### Takeaway
OEM output tests are gated by module logic: range (Park/Neutral), engine speed, vehicle speed, and brake application. Scan tools will not end some tests until the lever is in Park. Specific limits are per OEM and per test, so they come from SI.

### Cited Findings
- DOCUMENTED (snippet), GM-specific, SI: line-pressure solenoid scan control is allowed only in **Park/Neutral, engine below 1500 RPM** (Hydra-Matic 6-speed material). — [GM Tech Info 6T70/6L80 (Scribd)](https://www.scribd.com/document/79508773/Gm-Tech-Info-6t70-6l80)
- DOCUMENTED (snippet), Chrysler-specific: the 41TE clutch test is a brake-torque test limited to **≤20% throttle for ≤5 seconds**. — [Motor Age](https://www.motor.com/magazine-summary/using-a-scan-tool-for-transmission-diagnosis/)
- DOCUMENTED (snippet), tool-specific (Snap-on domestic software, 2013 manual): during an "ATM" (actuator test mode) test that actuates transmission solenoids, the shift lever must be in Park to exit, and the scan tool does not exit the test until it is. — [Snap-on US Domestic Vehicle Communication Software Manual (Aug 2013)](https://www.snapon.com/Files/Diagnostics/UserManuals/USDomesticVehicleCommunicationSoftwareManual_EAZ0025B01H.pdf). The search tool merged several results, so check whether this ATM text is Chrysler-application text inside the Snap-on manual.
- DOCUMENTED (snippet), Universal: transmission control systems have built-in safety limits that restrict some operations based on vehicle speed and operating conditions. Verifying PARK function is described as a critical safety check before testing. — merged search result from [Snap-on manual](https://www.snapon.com/Files/Diagnostics/UserManuals/USDomesticVehicleCommunicationSoftwareManual_EAZ0025B01H.pdf) / [Gears "Road Test With A Purpose"](https://gearsmagazine.com/magazine/road-test-with-a-purpose/). Which source said it is uncertain.

### Inferences
- INFERRED, Universal: typical shop practice for stationary output tests: wheels chocked or parking brake set, foot on the brake, lever in P or N as the test requires, engine running only if the test needs hydraulic pressure, and a gauge installed for pressure tests. Commanding gears or TCC apply while driving needs a second person or a safe road-test setup, and the TCM may refuse a command outside its speed window.
- INFERRED: for ASE, the safe answer is "follow the scan tool/SI preconditions." Exact RPM, speed, or throttle limits are application-specific.

### Gaps
- OPEN: no public GM source for vehicle-speed limits on GDS2 shift-solenoid or gear commands, or on TCC commands.

---

## 5. Relevant scan data PIDs and GM vs. universal examples

### Takeaway
The core transmission PIDs are commanded gear vs. actual gear or ratio, ISS/OSS (and TSS or turbine speed on some units), TCC slip speed and TCC command or PC pressure command, PC/EPC solenoid commanded vs. actual current, TFT, shift time, and adapt values. GM's own names include "TCC PC Sol. Pressure Cmd." and "TCC Slip Speed." Chrysler's adapt PID is CVI.

### Cited Findings
- DOCUMENTED (snippet), GM-specific, SI: parameters listed in a GM service document (©2020 GM): Vehicle Speed, Engine Speed, Transmission ISS, Transmission OSS, Command Gear, TCC PC Sol. Pressure Cmd., TCC Slip Speed. When the TCM decides to shift, it varies current to the PC solenoids for the oncoming and off-going clutches. The oncoming clutch's PC solenoid pressure command should change to "YES," and the off-going one's to "NO." Watch TCC slip when the TCC PC pressure command shows apply. **With the TCC applied, not shifting, and steady throttle, slip should be controlled below 100 RPM.** — [GM service document via NHTSA, MC-10181692 (©2020)](https://static.nhtsa.gov/odi/tsbs/2020/MC-10181692-9999.pdf). Which transmission this applies to is **OPEN**, because the PDF could not be opened. Treat "<100 RPM" as that bulletin's criterion, not a universal spec.
- DOCUMENTED (snippet), GM-specific (Hydra-Matic 6-speed): the TCC may apply right after the 1-2 shift, and TCC events are not easily seen in engine speed alone. Use the TCC PC solenoid pressure command PID. — [GM Tech Info 6T70/6L80 (Scribd)](https://www.scribd.com/document/79508773/Gm-Tech-Info-6t70-6l80)
- DOCUMENTED (snippet), GM-specific (attributed to a GM 4-speed, 4L60-E-era scan data definition page; unit not confirmed), SI: PC solenoid **commanded current ranges 0.00–1.10 A**. Actual current is measured at the control module: **0 A = maximum (higher) line pressure, 1.1 A = lower line pressure.** — [Transmission Scan Tool Data Definitions (ls2.com/boggs/a4)](https://www.ls2.com/boggs/a4/transcantooldatadefinitions.htm) (the snippet text matched this page and the "a4" path points to a GM 4-speed). This inverse relationship (more current = less pressure) belongs to that normally-high-pressure design. **Do not generalize it.** Some newer solenoids are normally-low.
- DOCUMENTED (snippet, low-quality source), Universal-ish: at steady cruise, commanded lock should be followed by near-zero slip after a short ramp. One source states target slip "typically 0–40 RPM" and says >100 RPM at normal cruise points to TCC wear or low apply pressure. — merged search text from [Apex Technation diagnostic workflow](https://apextechnation.com/articles/automatic-transmission-diagnostic-workflow) / [iCarsoft P2762 article](https://www.icarsoft-us.com/blogs/news/p2762-code). Both are vendor/SEO-grade sources, so treat these numbers as not authoritative. The GM bulletin's "<100 RPM" above is the better-sourced figure, and it is unit-specific.
- DOCUMENTED (snippet), GM-specific: 6L80 shift solenoid resistance is 20–40 Ω, and line/clutch pressure control solenoid resistance is 3–8 Ω. — [SilveradoSierra 6L80 thread](https://www.silveradosierra.com/threads/gm-6l80-transmission-information-thread.753826/). This is a forum, so confirm in SI. It is included because DMM testing pairs with bidirectional testing in the ASE task.
- DOCUMENTED (snippet), GM-specific: TCM uses ISS/OSS for shift-time adapts (see Section 3). ISS/OSS basics are already in the learner's notes: `autotrans/research.md` and `note/issoss.pdf` (6L80 tech guide p.41: hall-effect ISS/OSS on an 8.3–9.3 V TCM supply; ISS is used for line pressure, shift timing, TCC slip, and ratio).
- DOCUMENTED (snippet), Chrysler-specific: CVI is the 41TE adapt PID (see Section 3 ranges). — [Motor Age](https://www.motor.com/magazine-summary/using-a-scan-tool-for-transmission-diagnosis/)

### Inferences
- INFERRED, Universal: how the PIDs are derived. TCC slip = engine rpm − turbine/input rpm (ISS or TSS). Actual gear ratio = ISS ÷ OSS. The TCM compares that ratio with commanded gear to set ratio or performance DTCs. Shift time = how long the ratio takes to move from old to new. TFT gates TCC apply, adapts, and some tests, so a cold or overheated TFT can explain "commanded but inhibited."
- INFERRED: "GM example vs. universal rule" split for the study guide:
  - Universal: commanded ≠ actual; use a gauge for pressure and a DMM for circuits; clicks without ratio change points to an internal fault.
  - GM-specific: GDS2 menu paths, "PC Sol. Pressure Cmd. YES/NO," Service Fast Learn, the P/N & <1500 RPM line-pressure control limit, and the <100 RPM TCC-slip criterion.

### Gaps
- OPEN: the actual GDS2 output-control list for the 6L80, 6T-series, and 10L (names such as "Shift Solenoid Valve Control," "TCC Solenoid Valve Control," "Line Pressure Control") could not be verified from any reachable public source.
- OPEN: which GM transmission the MC-10181692 "<100 RPM" criterion applies to.
- OPEN: Ford EPC-specific PIDs and output tests (for example, Ford "EPC" pressure PID vs. gauge). Transmission Digest's EPC article came up in search but could not be read.
- Recommended next step: open the local ASE PDF in a viewer for exact A2 wording, and rerun this with page access (or have Logan paste GDS2 output-control screenshots or instructor notes) before any of this goes into a print guide.
