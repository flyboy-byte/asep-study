# Automatic Transmission Hydraulic (Line) Pressure Testing, Stall Testing, and Air Testing (ASE A2 level)

Research date: 2026-09-30. All sources accessed 2026-09-30.

**Method limitation, read first:** The network egress proxy blocked full-page fetches for almost every source in this session (freeasestudyguides.com, gearsmagazine.com, sonnax.com, transmissiondigest.com, motor.com, aa1car.com, mitsubishitechinfo.com, trucktransdiag.com, static.nhtsa.gov). Only two pages fetched in full, both Chrysler/Jeep service-manual mirrors on s3.amazonaws.com. Every other finding comes from **search-engine result summaries/snippets**. Those are marked "(snippet)". They must be treated as leads to verify against the full page or textbook before they go into a guide. No Halderman or Today's Technician text was reachable. No GM TechLink article on pressure testing surfaced.

Tags: **DOCUMENTED** = stated by the cited source. **INFERRED** = my reasoning from cited material. **OPEN** = not resolved. Scope tags: **[Universal]**, **[GM-specific]**, **[Other OEM example]**, **[Needs SI]**.

---

## 1. What is the standard procedure and what are the preconditions?

### Takeaway
The widely taught procedure: check fluid level and condition first. Bring fluid to operating temperature. Install a high-range gauge (about 300 psi or more) at the line/mainline pressure tap. Set the parking brake and hold the service brake. Read pressure at idle and at increased throttle or stall in each range the manufacturer specifies (typically P/N, D, and R, sometimes manual low ranges). Compare against the SI spec chart for that unit. Do the pressure test before a stall test, and skip the stall test if pressure is low.

### Cited Findings
- DOCUMENTED [Universal]: Equipment is a high-pressure gauge rated to at least 300 psi plus the manufacturer's pressure specs for that transmission. An accurate tachometer is also required. — [TCI Auto Transmission Line Pressure](https://www.tciauto.com/trans-line-pressure); [Explorer Forum how-to](https://www.explorerforum.com/forums/threads/using-a-transmission-pressure-gauge.117998/) (snippet; the search summary blended these results, so exact attribution per sentence is uncertain)
- DOCUMENTED [Universal]: Run the engine until fluid reaches normal operating temperature (the snippet says "typically 160–200 °F / 70–95 °C"). Apply the brake pedal and set the parking brake. Readings should be taken with fluid level full and at operating temperature. — same search result set as above, incl. [Sun Transmissions guide](https://suntransmissions.com/blogs/news/transmission-pressure-testing-guide-diagnosing-hydraulic-failures) (snippet; commercial blog, low authority)
- DOCUMENTED [Other OEM example / Needs SI]: One OEM-style procedure specifies engine at 1500 rpm for readings. Another specifies "fast idle (700–1000 rpm) in each position." These rpm values are procedure-specific, not universal. — same search result set (snippet; source per value not separable)
- DOCUMENTED [Universal]: "Perform line pressure test prior to performing stall test. If line pressure is low at stall, do not perform stall test or further transmission damage will occur." — same search result set (snippet; reads as OEM service-manual wording)
- DOCUMENTED [Universal]: For an older unit, each range is checked at slow idle, fast idle, and WOT with a foot firmly on the brake. — [67-72chevytrucks.com TV cable / line pressure thread](https://67-72chevytrucks.com/vboard/showthread.php?t=526152) (snippet; enthusiast forum, low authority)
- DOCUMENTED [Universal]: If fluid is dirty or low when checked hot, correct the fluid condition or level first. Low line pressure at idle points to the pump or pressure relief valve. Check whether pressure increases when the engine is idled up. — [Ford-Trucks F-250 how-to](https://www.ford-trucks.com/how-tos/a/ford-super-duty-how-to-check-transmission-line-pressure-361492) / [freeasestudyguides pressure tests](https://www.freeasestudyguides.com/automatic-transmission-pressure-tests.html) (snippet)
- DOCUMENTED [Other OEM example]: Chrysler/Jeep SI has a dedicated "Pressure Test Port Locations" page, so tap location is unit-specific and comes from SI. — [Jeep JK SI mirror, Pressure Test Port Locations](https://s3.amazonaws.com/jeepwranglerjk2010/7c028738.html) (title only; not fetched)
- DOCUMENTED [GM-specific]: On the 6L80, the gauge goes on the mainline port on the passenger side of the transmission. — search summary of [Sonnax "Transmission Diagnostics Using Pressure Gauges"](https://www.sonnax.com/tech_resources/314-transmission-diagnostics-using-pressure-guages) / [Gears 6L80/6L90 issues](https://gearsmagazine.com/magazine/6l80-6l90-issues-that-could-drive-you-crazy/) (snippet; verify tap location in GM SI)
- DOCUMENTED [Universal]: Pressure testing individual clutch/servo circuits uses two 400 psi gauges. One goes on line pressure and one on the holding device's circuit, and both are monitored at the same time. — search summary including [Transmission Digest "Diagnosis with Pressure Gauges"](https://www.transmissiondigest.com/diagnosis-with-pressure-gauges/) (snippet)

### Inferences
- INFERRED [Universal]: A sensible ASE-level precondition list is: correct fluid level and condition, operating temperature, engine running properly (idle to spec), parking and service brakes applied, wheels chocked, gauge of adequate range routed where it can be read, and tach connected. Every item above appears in at least one cited snippet. The exact rpm and temperature values are [Needs SI].
- INFERRED: "Other taps" (governor, TV, cooler, individual clutch taps) exist on many units. The only other tap the found sources support is the per-circuit clutch/servo tap used with the two-gauge method.

### Gaps
- OPEN: Governor-pressure tap testing on older hydraulic units (a governor-pressure vs. road-speed check) was not covered by any source reached.
- OPEN: No full-text textbook (Halderman, Today's Technician) confirmation was obtainable. Fetch the freeasestudyguides and Sonnax pages from an unblocked network to confirm wording.
- OPEN: The exact source for each rpm and temperature value in the blended snippet cannot be separated.

---

## 2. What are the widely taught interpretation patterns, and which sources support them?

### Takeaway
The core pattern is consistent across sources:
- **Low in all ranges** means a common supply problem: pump, filter/pickup, pressure regulator, low fluid, or a large leak.
- **Low in one range** means a leak in a circuit used only in that range. Confirm it with the apply chart and by testing another range that uses the same element.
- **High in all ranges** means a regulator or pressure-control problem. On electronic units this is often the EPC/PCS or its circuit (failsafe high). On older units it is the TV/modulator.
- **Pressure doesn't rise with throttle/command** means a TV/modulator problem, or a PCS/command problem on EPC units.

### Cited Findings
- DOCUMENTED [Universal]: Line pressure consistently below minimum in all ranges has these probable causes: clogged filter, worn pump, or stuck pressure regulator valve. — [freeasestudyguides, Automatic Transmission Pressure Tests](https://www.freeasestudyguides.com/automatic-transmission-pressure-tests.html) (snippet)
- DOCUMENTED [Universal]: On electronically controlled transmissions, worn pump gears, pump cavitation, or pressure regulator wear produce insufficient base pressure across all ranges. Low-at-idle readings point to pump wear, a clogged filter, or a stuck regulator valve. — [Sun Transmissions pressure testing guide](https://suntransmissions.com/blogs/news/transmission-pressure-testing-guide-diagnosing-hydraulic-failures) (snippet; commercial blog)
- DOCUMENTED [Universal]: For single-shift or single-range failures, test in that specific gear. Use the clutch/band apply chart to see whether the suspect component is also used in another range, and test that range too. — search summary including [Transmission Digest "Diagnosis with Pressure Gauges"](https://www.transmissiondigest.com/diagnosis-with-pressure-gauges/) and [freeasestudyguides](https://www.freeasestudyguides.com/automatic-transmission-pressure-tests.html) (snippet)
- DOCUMENTED [Universal, value Needs SI]: With two gauges (line and the clutch circuit), a clutch-circuit pressure more than about 10% below line pressure indicates a leak. Another phrasing: a difference beyond spec, "usually 8–15 psi," indicates a hydraulic leak. — same search result set (snippet; the two thresholds come from different, unseparated sources. Treat them as rules of thumb, not specs.)
- DOCUMENTED [Universal, electronic units]: Unplugging the case connector drives line pressure to an uncontrolled maximum. That can overcome and **mask** a subtle circuit leak. — same search result set (snippet)
- DOCUMENTED [Universal]: High line pressure indicates either a worn pressure regulator or an EPC solenoid failsafe condition. It is often the result of an unplugged or damaged solenoid circuit. — [freeasestudyguides, Transmission Electronic Pressure Control](https://www.freeasestudyguides.com/transmission-electronic-pressure-control.html) (snippet)
- DOCUMENTED [Other OEM example: Chrysler 45RFE/545RFE]: DTC P0869 "Line Pressure High" possible causes include PCS control circuit open/short, line pressure sensor faults, TCM/PCM, and a **"stuck or sticking main regulator valve."** The diagnostic compares actual pressure (from a line pressure sensor) with desired pressure, and includes a step comparing sensor reading to a gauge. — [Jeep JK SI mirror, P0869](https://s3.amazonaws.com/jeepwranglerjk2010/7c038f97.html) (full page fetched)
- DOCUMENTED [Universal]: If line pressure is out of spec (above or below) on an EPC unit, test the EPC solenoid and circuit with a scan tool and a high-impedance DMM/ohmmeter. — [freeasestudyguides EPC](https://www.freeasestudyguides.com/transmission-electronic-pressure-control.html) (snippet)

### Inferences
- INFERRED [Universal]: Summary table for a study guide (each row is supported by the snippets above):

  | Reading | Most likely area |
  | --- | --- |
  | Low, all ranges | Low fluid, clogged or leaking filter/pickup (aeration), worn pump, stuck/weak pressure regulator, large common leak |
  | Low, one range only | Leak in circuit unique to that range: piston seal, sealing rings, servo seal, valve body/case leak for that circuit |
  | High, all ranges | Regulator valve stuck; EPC/PCS failsafe (unplugged, open circuit, or stuck solenoid); older units: TV cable misadjusted, or modulator vacuum loss |
  | Doesn't rise with throttle/command | TV linkage or cable disconnected/misadjusted, modulator/boost valve stuck; EPC units: PCS not responding, command not changing, regulator/boost valve stuck |
  | Normal at idle, low at stall/WOT | Pump can't keep up (wear), or internal leak that shows under high demand (INFERRED; not explicitly stated in the fetched sources) |
- INFERRED: The "low in one range" logic rests on the apply chart. The element unique to the low range is the suspect. If a range sharing that element also reads low, the suspicion is confirmed.

### Gaps
- OPEN: No fetched textbook states the "normal at idle, low at WOT" pattern. It is widely taught, but I could not source it this session.
- OPEN: The rule-of-thumb leak thresholds (10%, 8–15 psi) need a verified primary source.

---

## 3. How does this differ between older TV/modulator units and electronically controlled (EPC) units?

### Takeaway
On older units, line pressure rises with throttle because of a TV cable/linkage or a vacuum modulator. Low vacuum or high throttle means high pressure. High pressure all the time points to TV misadjustment or a leaking modulator or vacuum line. On EPC units, the PCM/TCM varies current to a variable-force or PWM pressure control solenoid. Common Ford/GM designs are "inverse": high current means low pressure, and low or no current means maximum (failsafe) pressure. The test then compares the gauge reading with the scan tool command (current or desired pressure), often while the scan tool commands pressure up and down.

### Cited Findings
- DOCUMENTED [Universal, older units]: A vacuum modulator converts manifold vacuum into an engine-load signal. Low or zero vacuum lets spring force raise modulator (and thus line) pressure. High vacuum gives low pressure. — [Brainscape A2 flashcards](https://www.brainscape.com/flashcards/automatic-transmissions-1273406/packs/2531089) / [Quizlet valvebody and pressures](https://quizlet.com/390973383/valvebody-and-pressures-automatic-transmissiontransaxle-flash-cards/) (snippet; student flashcards, low authority, but they reflect textbook wording)
- DOCUMENTED [Universal, older units]: To check for maximum pressure rise, move a cable or linkage to the max-pressure position. On a modulator unit, disconnect the vacuum to get max pressure. If pressure doesn't drop when the TV cable is disconnected, pull the inner cable by hand to isolate the linkage from the valve. — [67-72chevytrucks.com thread](https://67-72chevytrucks.com/vboard/showthread.php?t=526152) / [Sonnax pressure gauge article](https://www.sonnax.com/tech_resources/125-transmission-pressure-gauge-a-diagnostic-tool) (snippet)
- DOCUMENTED [Universal, older units]: For modulator vacuum supply, tee a gauge into the modulator hose and compare it with manifold vacuum. A lower reading at the end of the line means a leaking line. — same search result set (snippet)
- DOCUMENTED [Ford example, principle broadly Universal]: The EPC is a variable-force solenoid that regulates line pressure and line modulator pressure. The PCM varies current, not voltage: **high current means low pressure, low current means high pressure.** Unplugged, it gives maximum pressure. — [freeasestudyguides EPC](https://www.freeasestudyguides.com/transmission-electronic-pressure-control.html) (snippet)
- DOCUMENTED [GM-specific]: GM uses engine data to set desired line pressure, raising and lowering it through the pressure control solenoid for shift quality and clutch holding force. The scan tool usually shows engine load (%) and PCS command (amps). Snippet values: about 10% load and **0.9–1.1 A** at idle. Near WOT just before the 1-2 shift, 90–100% load and **0.2–0 A**. An amp clamp on the PCS wire verifies the signal, and a gauge on the tap verifies the pressure response. — [Gears Magazine, "Controlling Pressure General Motors"](https://gearsmagazine.com/magazine/controlling-pressure-general-motors/) (snippet; amperage values [Needs SI] per unit)
- DOCUMENTED [Universal, electronic units]: With a bi-directional scan tool, command EPC/PCS amperage up and down with the engine running and watch the gauge for proper hydraulic response. The scan tool value is a **command**, and you cannot assume actual pressure matches it. If gauge and command agree, the solenoid, regulator/boost valves, and pump are working. — search summary of [Sonnax pressure-gauge articles](https://www.sonnax.com/tech_resources/314-transmission-diagnostics-using-pressure-guages) and [Transmission Digest "The Variable Line Pressure Solenoid"](https://www.transmissiondigest.com/the-variable-line-pressure-solenoid/) (snippet)
- DOCUMENTED [Universal]: If command is high but actual is near zero, the solenoid is mechanically stuck or the pump has failed. — [Sonnax pressure gauge article](https://www.sonnax.com/tech_resources/125-transmission-pressure-gauge-a-diagnostic-tool) (snippet)
- DOCUMENTED [Other OEM example: Chrysler 45RFE/545RFE]: This unit has a **line pressure sensor**, so the TCM compares actual with desired pressure and sets P0869 (high) or P0868 (low). Preset desired levels are listed as 827–931 kPa during shifts and in P/N. — [Jeep JK SI mirror, P0869](https://s3.amazonaws.com/jeepwranglerjk2010/7c038f97.html) (fetched; value is 45RFE/545RFE only, [Needs SI])

### Inferences
- INFERRED: On units without a line pressure sensor (many GM units), the scan tool shows only the **commanded** PCS current or desired pressure. A mechanical gauge is the only way to see actual pressure. On sensor-equipped units (for example, Chrysler RFE), a scan PID for actual pressure exists but should still be gauge-verified, as the P0869 procedure does.
- INFERRED: Diagnostic split on EPC units. Correct command and correct electrical signal (amp clamp) with wrong gauge reading means a hydraulic/mechanical problem (solenoid valve, regulator, pump, leak). Wrong or no command change means a TCM input/strategy or circuit problem.

### Gaps
- OPEN: Not every EPC design is inverse. Some newer normally-low or normally-high solenoids behave differently. [Needs SI] for each unit.

---

## 4. Stall test: procedure, safety limits, and interpretation

### Takeaway
Stall test procedure: engine and fluid at operating temperature, service and parking brakes applied (wheels chocked), selector in D (and R, and other ranges if specified). Floor the throttle only long enough to read the maximum rpm, **no more than about 5 seconds**. Cool between ranges in N at about 1000 rpm. Interpretation:
- **High stall rpm** = transmission holding element slipping (clutch/band/OWC) in that range.
- **Low stall rpm** = engine not making power (including a restricted exhaust), or stator one-way clutch freewheeling.
- If stall is normal but acceleration is poor above about 30–45 mph, suspect a stator seized. This is a textbook pattern; I could not source it this session.

Do the pressure test first. Don't stall-test with low line pressure.

### Cited Findings
- DOCUMENTED [Universal]: Engine coolant and fluid at operating temperature. Firmly apply service and parking brakes. In D, 2, 1, and R, floor the accelerator just long enough to reach full rpm. — search summary including [freeasestudyguides Torque Converter Stall Test](https://www.freeasestudyguides.com/torque-converter-stall-test.html), [Mitsubishi SI stall test](https://mitsubishitechinfo.com/data/RE/2019/23/HTML/M123100540066300USA.htm), [Subaru 4AT stall test PDF](http://ken-gilbert.com/wrx/STi_Manual/04.%20TRANSMISSION/02.%20AUTOMATIC%20TRANSMISSION/05.%20Stall%20Test.pdf) (snippet)
- DOCUMENTED [Universal; duration value is common but confirm per SI]: Do not hold the throttle open for more than **5 seconds** or transmission damage may result. After each range, move to N and run at about **1000 rpm for about 15 seconds** to cool the converter. — same search set (snippet; this reads as OEM SI wording, likely the Mitsubishi/Subaru pages)
- DOCUMENTED [Universal]: Stall rpm **below** spec means the stator one-way clutch is slipping, or there is an exhaust restriction. — [freeasestudyguides stall test](https://www.freeasestudyguides.com/torque-converter-stall-test.html); [Brainly A2-style question](https://brainly.com/question/37584132) (snippets)
- DOCUMENTED [Universal]: Stall rpm **above** spec means the transmission's clutches/bands are slipping. — [Brainscape A2 flashcards](https://www.brainscape.com/flashcards/automatic-transmissions-1273406/packs/2531089) (snippet)
- CONFLICT, needs resolution: One search summary also said "higher than specified engine rpm during a stall test would indicate the stator one-way clutch will not lock or hold." Most sources assign a freewheeling stator to **low** stall rpm (loss of torque multiplication). Treat the "high = stator" phrasing as suspect until a textbook is checked. — search summary attributed to the [freeasestudyguides stall test](https://www.freeasestudyguides.com/torque-converter-stall-test.html) result set (snippet)
- DOCUMENTED [Universal]: The stall test checks converter OWC operation, forward/reverse clutch holding, low/reverse bands, the planetary OWC, and engine performance. — same stall-test search set (snippet)
- DOCUMENTED [Universal]: Run the line pressure test before the stall test. If line pressure is low at stall, don't do the stall test. — line-pressure procedure search set (see Section 1) (snippet)

### Inferences
- INFERRED [Universal]: Pressure and stall tests work together. The pressure test says whether the apply element is getting enough oil. The stall test says whether it holds under full engine torque. High stall in one range with normal pressure in that range points to a mechanical holding problem (worn friction, burnt band, OWC). High stall with low pressure in that range points to the hydraulic circuit.
- INFERRED: On many modern units, OEMs have de-emphasized or dropped stall testing. Check SI before assuming a stall spec exists.

### Gaps
- OPEN: No source reached this session states the "stator seized: normal stall, poor high-speed acceleration / overheating" pattern. It is standard textbook content; verify in Halderman or Today's Technician.
- OPEN: The "high stall = stator" conflict noted above needs textbook confirmation.
- OPEN: Stall rpm specs are unit- and engine-specific. [Needs SI]. None are given here.

---

## 5. Air pressure (air check) testing and how it relates to pressure testing

### Takeaway
Air checks are done with the valve body removed (on the vehicle, or during assembly). Apply low-pressure, clean, dry shop air, commonly about 30 psi per the one OEM procedure fetched, to each clutch/servo passage. Listen and feel for a thud or apply and a clean release. Excessive air escaping means a seal or ring leak. Air testing confirms a leak that pressure testing suggested (for example, low in one range) and pinpoints which element leaks.

### Cited Findings
- DOCUMENTED [Other OEM example: Chrysler 42RLE]: Remove the oil pan and valve body. Apply air through special tool plate set 6599 at **30 psi**, clean and dry. Listen for "a slight thud sound." The piston should move and return when air is released. If "a large amount of air is heard escaping, the transmission must be removed from vehicle, disassembled and all seals inspected." The underdrive clutch is checked by locking the output and attempting to turn the input by hand. — [Jeep JK SI mirror, Clutch Air Pressure Tests (42RLE)](https://s3.amazonaws.com/jeepwranglerjk2010/7c033609.html) (full page fetched)
- DOCUMENTED [Universal]: Air tests use low pressure (the snippet gives 20–50 psi). Check the manufacturer's spec because too much pressure can damage seals. Servos can be air-tested (about 30 psi) at the apply holes before the valve body goes on, with short bursts, watching for band apply. — search summary including [IH Parts America forum "Servo air test?"](https://forums.ihpartsamerica.com/threads/servo-air-test.5875/) and [freeasestudyguides](https://www.freeasestudyguides.com/automatic-transmission-pressure-tests.html) (snippet; the 20–50 psi range is not from an OEM source)

### Inferences
- INFERRED [Universal]: Workflow: fluid check, then line pressure test (identify the range or circuit), then stall test (if pressure OK, check holding ability), then air check (locate the leaking element). Road test and scan data come before or alongside these. This order follows directly from Sections 1, 2, and 4.

### Gaps
- OPEN: No GM-specific air-check procedure was reached. GM unit repair manuals have air-check plates and passage IDs [Needs SI].

---

## 6. GM-specific examples vs. universal principles

### Takeaway
GM electronic units (4L60-E, 6L80) have no line pressure sensor. Pressure is tested with a mechanical gauge at the mainline tap, compared against scan-tool PCS command (amps) or desired pressure, and the PCS can be commanded with a bi-directional tool (Tech 2 / GDS2). The 4L60-E PCS is inverse: low current means maximum pressure. Every specific number below is secondary-source and **needs verification in GM SI**.

### Cited Findings
- DOCUMENTED [GM-specific, Needs SI]: 4L60-E PCS: fixed frequency **292.5 Hz**, **4.5–6 Ω**. About 5% duty / **0.1 A** gives maximum line pressure. About 40% duty / **1.1 A** gives minimum line pressure. The PCS acts on line pressure through the boost valve and pressure regulator. — [trucktransdiag 4L60E technical information PDF](https://www.trucktransdiag.com/downloads/4l60e-technical-information.pdf) (snippet; aftermarket tech sheet, not GM)
- DOCUMENTED [GM-specific, Needs SI]: 4L60-E pressure-test ranges from the same aftermarket sheet: **P/N/D 55–189 psi (min–max)**, **R 64–324 psi (min–max)**. Conditions (rpm, commanded current) were not given in the snippet. — [trucktransdiag 4L60E PDF](https://www.trucktransdiag.com/downloads/4l60e-technical-information.pdf) (snippet; do NOT use as a spec without GM SI)
- DOCUMENTED [GM-specific]: A Tech 2 can force different current levels to the PCS to see whether line pressure changes. About 1 A should bring pressure down to idle-level pressure. — [Holley forum 4L60E line pressure](https://forums.holley.com/forum/holley-efi/terminator-x-efi/415058-4l60e-line-pressure) / [hotrodders "4L60E no change in line pressure"](https://hotrodders.com/forum/4l60e-no-change-line-pressure-258522.html) (snippet; forum, low authority)
- DOCUMENTED [GM-specific]: GM scan data typically shows PCS command in amps. About 0.9–1.1 A at idle, falling toward 0–0.2 A near WOT. — [Gears Magazine, Controlling Pressure General Motors](https://gearsmagazine.com/magazine/controlling-pressure-general-motors/) (snippet)
- DOCUMENTED [GM-specific]: 6L80: gauge at the passenger-side mainline port. Observe scan-tool PC solenoid command vs. gauge. A search snippet quoted a GM SM fragment, "commanded state of the pc solenoid: None 45-80psi 200," which is too garbled to use. — search summary of [Gears 6L80/6L90](https://gearsmagazine.com/magazine/6l80-6l90-issues-that-could-drive-you-crazy/) / [Sonnax pressure gauges](https://www.sonnax.com/tech_resources/314-transmission-diagnostics-using-pressure-guages) (snippet; [Needs SI])
- DOCUMENTED [GM-specific]: Community discussion notes disagreement about 6L80/6L90 line pressure behavior and values. — [HP Tuners "6L80/6L90 Line pressure. Everyone is wrong"](https://forum.hptuners.com/showthread.php?93840-6L80-6L90-Line-pressure-Everyone-is-wrong&p=673597) (title only; forum)

### Inferences
- INFERRED: Universal principle vs. GM example. The low/high/one-range interpretation logic and the "gauge vs. command" method are universal. Inverse PCS behavior (low current means high pressure) is GM and Ford practice, but not guaranteed on every design. The GM "Line Pressure Check" scan-tool procedure and all psi and amp figures are GM-specific and [Needs SI].
- INFERRED: For A2 exam purposes, the likely tested concepts are the patterns, the failsafe-high behavior of an unplugged inverse EPC, and "don't trust the command, verify with a gauge." Specific psi values are unlikely to be tested.

### Gaps
- OPEN: No GM TechLink article on pressure testing surfaced in searches. The GM SI "Line Pressure Check" procedure (Tech 2 / GDS2 commanded pressure steps and spec table) for the 4L60-E and 6L80 was not reachable. Logan's GM training material or ACDelco TDS would be the proper source.
- OPEN: All GM numeric values here are secondary and unverified.
