# ASE A2 Content Area A: Electronic Systems and Electrical Test Tasks (A.5–A.7, A.16, A.18–A.21, A.23, A.26–A.28)

Research date / access date for all sources: 2026-09-30. Researcher: Claude (subagent), for Logan's A2 open-gap research.

**Method and limits.** The egress proxy blocked full-page fetches. I tried obd-codes.com and a GM OBD-description PDF (gsitlc.ext.gm.com), and both returned EGRESS_BLOCKED. Every finding below is therefore **DOCUMENTED (snippet)**: I took it from WebSearch result text, not from a full page I read. Where I could, I corroborated a claim across two or more independent snippets, and each entry says so ("corroborated") or flags it as single-source. Many snippets came from generic DTC content farms (go-parts.com, icarsoft, apextechnation, autodtcs, and similar), and some of those read like auto-generated text. I treat them as weak and use them only when a stronger source agrees. The stronger sources are Pico Technology, California BAR, Snap-on, MOTOR magazine, Transmission Digest, Gears, Brake & Front End, aa1car, Kvaser, Toyota factory manual excerpts, and TI/ST application notes.

**Tag key.** DOCUMENTED (snippet) / INFERRED / OPEN. Scope: **U** = universal principle, **GM** = GM-specific, **SI** = needs service information for the actual number. Each finding also carries its task number (A.x).

**Already covered elsewhere, cross-reference only.** Scan-tool bidirectional controls → `scan_tool_bidirectional.md`. Programming/relearn → `tcm_programming_relearn.md`. EPC/line-pressure testing → `hydraulic_pressure_testing.md`. Also already in Logan's notes: NTC basics, pressure switches, Hall-type ISS/OSS, and the EPC current/pressure relationship.

---

## Key Question 1: What test methods and pass/fail patterns are taught for each component?

### Takeaway
The ASE-level test logic is consistent across components:
- Match the test to the sensor type. An ohmmeter and AC voltage suit a passive magnetic (VR) sensor. Reference, ground and signal toggling suit a Hall/MR sensor, and you never ohm-check one.
- Test circuits under load with voltage drop, not with resistance.
- Use an amp clamp and scope to see a solenoid's actual current signature.
- Read CAN resistance with the network powered down: 60 Ω is good, 120 Ω means one terminator is open, and near 0 Ω means CAN-H is shorted to CAN-L.
- Interpret DTCs by their suffix: "circuit/open/low/high/electrical" means an electrical fault; "performance/stuck/incorrect ratio" means a functional fault.

### Cited Findings

#### Speed sensors (ISS/OSS/VSS): A.5, A.19, A.26

**Passive magnetic / variable reluctance (VR) sensors**
- A VR sensor produces an AC signal and a Hall sensor produces a square wave. The Hall square wave switches from reference ground up to a DC level, typically 5, 8, 10 or 12 V. DOCUMENTED (snippet), U, corroborated — [Gears Magazine, Advanced Speed Sensors Pt 1](https://gearsmagazine.com/magazine/advanced-speed-sensors-part-1/); [Electronics360 VR vs Hall](https://electronics360.globalspec.com/article/12776/vr-vs-hall-effect-speed-sensors)
- In a VR sensor, both voltage output and frequency rise with speed. VR responds to the *rate of change* of flux, while Hall responds to the *magnitude* of flux, so a Hall sensor works at zero or very low speed. DOCUMENTED (snippet), U, corroborated — [Gears Magazine](https://gearsmagazine.com/magazine/advanced-speed-sensors-part-1/); [Electronics360](https://electronics360.globalspec.com/article/12776/vr-vs-hall-effect-speed-sensors); [Wikipedia VR sensor](https://en.wikipedia.org/wiki/Variable_reluctance_sensor)
- Mounting distance (air gap) to the reluctor is critical. As little as 1 mm can separate a good signal from no signal. DOCUMENTED (snippet), U — [Gears Magazine](https://gearsmagazine.com/magazine/advanced-speed-sensors-part-1/)
- A wide air gap weakens the field and lowers signal amplitude, which matters most at low speed where the signal is already weak. Metal debris on a magnetic sensor tip also reduces AC output, so pull the sensor, clean the tip and check the gap. DOCUMENTED (snippet), U, corroborated across the wheel-speed-sensor literature; the principle transfers to transmission VR sensors — [aa1car, Diagnosing ABS WSS](https://www.aa1car.com/library/diagnosing_abs_wheels_speed_sensors.htm); [Brake & Front End, Diagnosing Hub Units / Air Gap](https://www.brakeandfrontend.com/diagnosing-hub-units-and-wheel-speed-sensors-air-gap-issues-and-dtcs/)
- Example numbers, from ABS wheel-speed sensors only. Do NOT memorize these as transmission specs. Magnetic WSS resistance is "450 to 2200 ohms" (one source) or "800 to 1400 ohms" (another). AC output is "50 to 700 mV" when the wheel is spun by hand at about 1 rev/s. DOCUMENTED (snippet), SI (ISS/OSS resistance and output are application-specific) — [aa1car](https://www.aa1car.com/library/diagnosing_abs_wheels_speed_sensors.htm)

**Active sensors (Hall / magnetoresistive)**
- Do not test a Hall or other active sensor with an ohmmeter. The internal IC gives a meaningless high reading, and several sources say ohmmeter testing can damage an active sensor. The correct test has three steps:
  1. Check the reference voltage (commonly 5, 8, 9 or 10 V).
  2. Check the sensor ground.
  3. Check that the signal toggles cleanly from near 0 V (about 0.1 V) up to the pull-up voltage as the target turns slowly.
  
  A scope shows noise and erratic edges, but still confirm the voltage levels. DOCUMENTED (snippet), U, corroborated — [Gears Magazine](https://gearsmagazine.com/magazine/advanced-speed-sensors-part-1/); [Pico AGT-072 Hall wheel speed sensor](https://www.picoauto.com/library/automotive-guided-tests/sensors/wheel-speed/AGT-072-wheel-speed-sensor-hall-effect/); [industrialmonitordirect (weak)](https://industrialmonitordirect.com/blogs/knowledgebase/identifying-and-replacing-automotive-hall-effect-speed-sensors)
- Two-wire active sensors (MR or Hall, "current-interface" or AK-protocol) carry their signal as a *current*, not a voltage. Pico gives the spec as "7 mA, 14 mA and 28 mA", and the controller's crossing threshold is about 6 mA. Because the current is so low, Pico measures it with a current clamp through a ×10 multiplier loop and a B/10 math channel. The controller develops the signal across a sense resistor, for example 75 Ω, giving about 0.525 V low and about 1.05 V high. DOCUMENTED (snippet), U principle; SI/application-specific for the numbers — [Pico, AK protocol decoding](https://www.picoauto.com/library/product-news/ak-protocol-decoding-with-picoscope-oscilloscope); [Pico forum, 2-wire active WSS](https://www.picoauto.com/support/viewtopic.php?t=22863); [industrialmonitordirect (weak)](https://industrialmonitordirect.com/blogs/knowledgebase/wheel-speed-sensor-digital-output-design-guide-and-specs)
- An MR sensor can be two-wire (power and signal) or three-wire. DOCUMENTED (snippet), U — [Brake & Front End, Testing Active WSS](https://www.brakeandfrontend.com/testing-active-wheel-speed-sensors/); [Pico AGT-847 MR WSS](https://www.picoauto.com/library/automotive-guided-tests/sensors/wheel-speed/AGT-847-wheel-speed-sensor-magnetoresistive/)

**Scope expectations and DTC meanings**
- A good trace is a clean square/pulse wave (Hall) or sine wave (VR) with no dropouts or excess noise. A scan-data graph of input/turbine RPM can show a flat line, a spike or a dropout. Within the P0715–P0719 group, P0718 = intermittent signal. DOCUMENTED (snippet), U, weak sources — [staff-capital DTC P0715](https://digital.staff-capital.com/en/dtc/p0715/?manufacturer=GENERIC); [eeuroparts P0715](https://eeuroparts.com/blog/p0715-code-input-turbine-speed-sensor-issues)
- P0715 ("Input/Turbine Speed Sensor A Circuit") is an electrical-monitor fault and "not proof that the sensor failed". Wiring or connector faults are common causes. DOCUMENTED (snippet), U — [staff-capital](https://digital.staff-capital.com/en/dtc/p0715/?manufacturer=GENERIC); [AutoZone P0715](https://www.autozone.com/diy/diagnostic-trouble-codes/p0715-input-turbine-speed-sensor-a-circuit)

#### TFT sensor (NTC): A.19, A.26, cross-ref A.18

- Toyota factory repair manuals (A750E, and TFT "B" circuit P2740) say a reading of −40 °C (−40 °F) means an **open** circuit. A shorted sensor makes the module see 150 °C (302 °F) or higher. DOCUMENTED (snippet), manufacturer source (Toyota); the principle is U for a pull-up NTC circuit — [Toyota A750E RM (FJ Cruiser)](https://www.purefjcruiser.com/docs/2007%20Toyota%20FJ%20Cruiser%20Repair%20Manual/A750E%20Automatic%20Transmission/Automatic%20Transmission%20System/0160014.pdf); [Toyota RM P2740](https://toyotamanuals.gitlab.io/PZ471-Z00W0-CA/htmlweb/rm/rm1151e/m_05_1120.pdf)
- **Conflict.** One snippet (go-parts) says −40 °F "confirms a short to ground". That is backwards for a standard pull-up/NTC circuit. The Toyota manuals above say open = −40 and short = hot. Trust the factory source. DOCUMENTED conflict — [go-parts P0712 (weak)](https://www.go-parts.com/garage/obd-p0712)
- When the module sees high fluid temperature, it may apply the TCC sooner and/or disable overdrive to cut heat. This is a hot-mode strategy. DOCUMENTED (snippet), U-ish; strategy varies (SI) — [go-parts P0712 (weak)](https://www.go-parts.com/garage/obd-p0712); consistent with [Crown Auto TFT problems](https://crownautoservice417.com/automotive-knowledge-center/repair-library/transmission/transmission-fluid-temperature-sensor-problems/)
- DTC meanings: P0712 = TFT Sensor A Circuit **Low** Input, which is a low signal voltage, so the module reads HOT, typically from a short to ground. P0713 = Circuit **High** Input, a high signal voltage read as COLD, typically an open. DOCUMENTED (snippet), U (SAE J2012 generic titles) — [obd-codes P0712 (search listing)](https://www.obd-codes.com/p0712); [carfaultcodes P0713](https://www.carfaultcodes.co.uk/fault-codes/p0713/); [GM DTC P0713 page](https://www.ls2.com/boggs/a4/DTC%20P0713%205.7.htm)

#### Transmission range (TR) switch / GM internal mode switch (IMS): A.19, A.26, A.28

- P0705 = TR sensor circuit malfunction: the TCM cannot reliably tell the selected range. P0706 = range/performance, meaning an illogical or out-of-range signal. DOCUMENTED (snippet), U — [Edmunds P0705](https://www.edmunds.com/obd-dtc/p0705.html); [Carista P0705](https://carista.com/en-us/pages/obd2-diagnostic-trouble-codes/p0705); [go-parts P0706](https://www.go-parts.com/garage/obd-p0706-acura-tl-2007-2008-j35a8-3-5l)
- Symptoms of a failed or misadjusted TR switch:
  - no-crank in Park, or starts only in Neutral
  - blinking, blank, dashed or wrong gear display
  - the transmission defaulting to a fixed gear
  
  Test: compare the physical selector position with the TCM's reported range in scan data, and adjust or replace the switch if they disagree. DOCUMENTED (snippet), U, corroborated across several weak sources plus a Gearstar article — [Gearstar, Bad TR sensor symptoms](https://gearstar.com/blog/what-happens-when-a-transmission-range-sensor-goes-bad/); [Edmunds](https://www.edmunds.com/obd-dtc/p0705.html)
- The alignment-pin method (loosen, select Neutral, insert a gauge pin, tighten) appears in one snippet with a "5 mm" pin. The pin size is application-specific. DOCUMENTED (snippet), SI — [go-parts (weak)](https://www.go-parts.com/garage/obd-p0705-honda-civic-2006-2011)
- **GM IMS.** It is a sliding-contact switch on the manual valve with four TCM inputs: Signal A, B, C and P (parity). A fifth signal, "N" (P/N start), goes directly to the ECM for start enable. Each input reads high when its switch is open and low when it is closed to ground. The module decodes range from the HI/LOW combination with a lookup table, and the scan tool displays each input as HI/LOW. Related GM DTCs: P1825 (invalid range) and P1915 (start/wrong range). DOCUMENTED (snippet), GM — [Transmission Digest, A 6T70 IMS Invalid Range Signal](https://www.transmissiondigest.com/a-6t70-ims-invalid-range-signal/); [GM DTC P1825/P1915 page](https://gm.saturn.team/Chevrolet/Silverado___4WD/2009/dtc/143877); [GM 12OBDG01B Transmission Diagnostics (not fetched)](https://gsitlc.ext.gm.com/gmspo/mode6/pdf/2012/12OBDG01B%20Transmission%20Diagnostics.pdf)
- Other manufacturers use resistance-ladder TR sensors (a different resistance or voltage per range). I found no citable per-range numbers. OPEN / SI.

#### Solenoids (on/off, PWM, VFS/linear): A.5, A.19, A.20, A.26, A.27

- Current ramping: an amp clamp on a scope shows the solenoid's current rise. A normal trace shows a "pintle hump/bump", the dip where the plunger moves. A shorted winding shows a straight, near-vertical current rise and higher current. An open shows no current. DOCUMENTED (snippet), U, corroborated (injector and solenoid literature) — [MOTOR, Current Clamp On-Ramp](https://www.motor.com/magazine-summary/current-clamp-on-ramp-december-2007/); [VehicleServicePros, Benefits of Current Ramping](https://www.vehicleservicepros.com/service-repair/article/53089665/the-benefits-of-current-ramping); [VSP tech tip](https://www.vehicleservicepros.com/training-and-resources/tech-tips/article/12150146/tech-tip-current-ramping-as-a-useful-diagnostic-technique)
- A standard DMM can find opens and excessive resistance but is "not accurate enough to check for winding-to-winding shorts". Current testing is the better check for a partially shorted coil. DOCUMENTED (snippet), U — [Gears, Resistance: Multimeter Diagnostics Pt 2](https://gearsmagazine.com/magazine/resistance-multimeter-diagnostics-part-two/)
- PWM definitions:
  - Duty cycle is on-time as a percentage of the period (25% on / 75% off = 25% duty).
  - Frequency is cycles per second (for example, 30 Hz).
  - A transmission solenoid trace may show a "stroke" (a longer initial on-time), a "latch" (duty cycled at lower current) and a release (off).
  
  Pico's method: back-probe both pressure-control-solenoid wires at the transmission connector with the engine idling. DOCUMENTED (snippet), U — [Gears, Exploring PWM, Frequency and Duty Cycle](https://gearsmagazine.com/magazine/exploring-pwm-frequency-and-duty-cycle/); [Pico forum, PWM and duty cycle](https://www.picotech.com/support/viewtopic.php?t=42838); [diag.net transmission solenoid waveform](https://diag.net/msg/m2o0wx2gw68s07u3wmsl7mqrar/?m=m6hxwjvtcm83cqhxi07t3l2fy7)
- VFS logic: in a "normally low" (proportional) VFS, more current gives more pressure. In a "normally high" (inversely proportional) VFS, more current gives *less* pressure. On the GM 8L90, several clutch solenoids and the line-pressure solenoid are normally high. One Transmission Digest article gives a line-pressure-solenoid duty-cycle range of "5% to 62%" for its example application. DOCUMENTED (snippet); principle U; 8L90 detail GM; the duty range is SI — [Wikipedia VFS](https://en.wikipedia.org/wiki/Variable_force_solenoid); [Gears, 8L90 Solenoid Strategies](https://gearsmagazine.com/magazine/8l90-solenoid-strategies/); [Transmission Digest, Variable Line Pressure Solenoid](https://www.transmissiondigest.com/the-variable-line-pressure-solenoid/)
- Driver-side protection: a **high-side** driver can protect against a short to ground, and a **low-side** driver protects against a short to battery. DOCUMENTED (snippet), U electronics principle — [ST AN514 High Side Drivers](https://www.st.com/resource/en/application_note/an514-high-side-drivers-stmicroelectronics.pdf); [TI SLVAE59](https://www.ti.com/lit/pdf/slvae59)
- The inductive spike at turn-off (V = L·di/dt) is normally clamped by a flyback/freewheel path. A missing or abnormal spike points to a coil or circuit fault. DOCUMENTED (snippet), U — [Wikipedia Flyback diode](https://en.wikipedia.org/wiki/Flyback_diode); [TI SLVAE59](https://www.ti.com/lit/slvae59)
- DTC suffix meanings (SAE generic titles):
  - P0750 Shift Solenoid A (malfunction)
  - P0751 Performance/Stuck Off: the module commanded it and the ratio did not follow
  - P0752 Stuck On
  - P0753 Electrical: open or short
  - P0960 Pressure Control Solenoid A Control Circuit/Open
  - P0961 Range/Performance
  - P0962 Circuit Low (short to ground)
  - P0963 Circuit High (short to power / open, depending on driver design)
  
  DOCUMENTED (snippet), U, corroborated — [RepairPal P0753](https://repairpal.com/obd-ii-code-p0753); [obd-codes P0751/P0752 (listing)](https://www.obd-codes.com/p0751); [RepairPal P0960](https://repairpal.com/obd-ii-code-p0960-pressure-control-solenoid-a-control-circuit-open); [RepairPal P0962](https://repairpal.com/obd-ii-code-p0962-pressure-control-solenoid-a-control-circuit-low); [RepairPal P0963](https://repairpal.com/obd-ii-code-p0963-pressure-control-solenoid-a-control-circuit-high)
- I found no citable generic solenoid resistance specs (ohms by solenoid type) from a reliable source. OPEN / SI.

#### TCC electronic tests: A.18

- P0741 = TCC Circuit Performance or Stuck Off: the TCC was commanded on and slip stayed too high. One source gives the threshold as ">200 RPM" and another as "~100 RPM", and both say it varies by manufacturer. A diagnostic guide interprets TCC slip RPM this way:
  - 0–50: fully applied
  - 50–200 and fluctuating: applying but slipping (friction, apply pressure, fluid)
  - 200+ or equal to engine RPM minus turbine RPM: not applying (solenoid or hydraulic)
  
  DOCUMENTED (snippet); thresholds SI; the slip bands come from a weak source (apextechnation) — [YourMechanic P0741](https://www.yourmechanic.com/article/p0741-obd-ii-trouble-code-torque-converter-clutch-circuit-performance-or-stuck-off-by-jamahl-walker); [apextechnation P0741 (weak)](https://apextechnation.com/articles/p0741-torque-converter-clutch-code); [Edmunds P0741](https://www.edmunds.com/obd-dtc/p0741.html)
- P0742 = TCC Circuit Stuck On. The classic symptom: after highway driving, the engine stalls when coming to a stop, then restarts. It is common on some GM models, and causes include a debris-jammed TCC solenoid or valve-body wear (the 4L80-E is named). DOCUMENTED (snippet), U symptom; GM examples — [obd-codes P0742 (listing)](https://www.obd-codes.com/p0742); [RepairPal P0742](https://repairpal.com/obd-ii-code-p0742); [icarsoft P0742 (weak)](https://www.icarsoft-us.com/blogs/news/p0742-code-torque-converter-clutch-stuck-on-fix)
- The brake pedal position switch releases the TCC. On the older GM setup cited, the TCC circuit is +12 V with the brake released and open with the brake applied. A misadjusted brake switch can prevent lockup even when the brake lights and cruise cancel work. DOCUMENTED (snippet), U principle; circuit details GM/older — [67-72chevytrucks forum](https://67-72chevytrucks.com/vboard/showthread.php?t=732001); [dieselplace, brake switch & TCC](https://www.dieselplace.com/threads/brake-pedal-switch-failure-tcc-operation.398647/); [LiveAbout, Diagnosing GM converter lock-up](https://www.liveabout.com/diagnosing-gm-converter-lock-up-problems-262653)

#### Voltage drop / power and ground: A.21, A.27

- Voltage drop is measured with the circuit loaded and current flowing. It finds resistance that an ohmmeter misses, such as a few strands carrying current. DOCUMENTED (snippet), U, corroborated — [Fluke, Diagnosing Voltage Drops](https://www.fluke.com/en-us/learn/blog/automotive/electrical-automotive-troubleshooting); [aa1car Voltage Drop Testing](https://www.aa1car.com/library/voltage_drop_testing.htm); [ALLDATA Tech-Assist Voltage Drop PDF](https://www.alldata.com/sites/default/files/file-attachments/voltage_drop__test_122718.pdf)
- Commonly quoted maximum drops. These vary by source, so attribute any number to its source:
  - "0.1 V per connection maximum"; ground-side total "0.1 to 0.2 V"; "0.00 V across a connection, 0.10 V at a ground" (aggregated snippet)
  - starter ground cable "0.2 V or less"; "any reading above 0.1 V at a component's ground" means that ground is compromised (aa1car/others)
  
  A GM technical tip PDF on voltage-drop procedures is also indexed (TT 97-20-01 on NHTSA). I could not read its numbers. DOCUMENTED (snippet), SI (the OEM spec governs) — [aa1car](https://www.aa1car.com/library/voltage_drop_testing.htm); [Fluke PDF](https://media.fluke.com/d2ea9167-56d8-4bc4-b4cb-b1060066c4e0_original%20file.pdf); [NHTSA-hosted TT 97-20-01](https://static.nhtsa.gov/odi/tsbs/2020/MC-10174571-0001.pdf)
- ScannerDanner forum technique for module power and grounds:
  1. Back-probe with T-pins and read voltage.
  2. Load the circuit (a test light, a bigger bulb, or a Power Probe) and read again.
  
  High-current circuits need a test load close to real current. A Transmission Digest case: a TCM power wire dropped to 9.7 V under load, and load testing found it where a simple continuity test would not. DOCUMENTED (snippet), U — [ScannerDanner forum, Voltage Drop Testing Modules](https://www.scannerdanner.com/forum/diagnostic-tools-and-techniques/4909-voltage-drop-testing-modules.html); [ScannerDanner forum, Power probe v-drop test](https://www.scannerdanner.com/forum/diagnostic-tools-and-techniques/2385-power-probe-v-drop-test.html); [Transmission Digest, Intermittent TCM Operation](https://www.transmissiondigest.com/intermittent-tcm-operation-creates-diagnostic-puzzle/); [Transmission Digest, Staying Grounded](https://www.transmissiondigest.com/staying-grounded/)

#### Low system voltage: A.21, A.23

- P0562 (System Voltage Low) as it applies to an Allison TCM:
  - The TCM needs ignition voltage of 9–18 V.
  - The code sets below 5.0–9.0 V (temperature-dependent) for more than 5 seconds.
  - The TCM then inhibits TCC and freezes shift adapts.
  - Low voltage can drop the transmission into 3rd gear with rough engagements.
  
  Another source adds that a failing battery or alternator below 10.0 V for 15 s is a common cause. First steps: check the batteries, then measure voltage *at the TCM*. DOCUMENTED (snippet), Allison-specific / SI — [Transmission Digest, Multiple Causes for P0562](https://www.transmissiondigest.com/multiple-causes-for-p0562/); [Scribd DTC P0562 (GM/Allison doc)](https://www.scribd.com/document/472739356/dtc-p0562); [obd-codes P0562 (listing)](https://www.obd-codes.com/p0562)
- A weak battery or low voltage (especially a dip during cranking) can knock modules off the CAN network. That sets U0100 (Lost Communication with ECM/PCM "A") and can cause erratic shifting and several modules faulting at once. Check the battery, charging system, fuses and grounds before condemning modules. The "<10 V during cranking" figure comes from weak sources. DOCUMENTED (snippet), U, weak sources — [go-parts U0100 (weak)](https://www.go-parts.com/garage/obd-u0100); [AxleAddict U0100](https://axleaddict.com/repair-maintenance/u0100-code-lost-communication-with-ecm-pcm)

#### CAN / data communications: A.19, A.20

- High-speed CAN has a 120 Ω terminator at each end of the bus, and the two in parallel measure **about 60 Ω** between CAN-H and CAN-L with the bus **powered down**. A reading of about 120 Ω means one terminator is missing or open. An open-circuit or very high reading means neither terminator is connected. DOCUMENTED (snippet), U, corroborated — [Kvaser, How to test CAN termination](https://kvaser.com/developer-blog/how-to-test-your-can-termination-works-correctly/); [Enovation Controls CAN troubleshooting](https://support.enovationcontrols.com/hc/en-us/articles/360038856494-CAN-BUS-Troubleshooting-Guide-with-Video); [maxon CAN topology](https://support.maxongroup.com/hc/en-us/articles/360009241840-CAN-bus-topology-and-bus-termination); [obd-cable, 120 Ω on pins 6 & 14](https://obd-cable.com/can-bus-120-ohm-reading-missing-terminator/)
- Bus voltages: at rest (recessive) both lines sit at about 2.5 V. When a module transmits (dominant), CAN-H goes to about 3.5 V and CAN-L to about 1.5 V, a 2 V differential. Noise hits both lines equally, so the differential survives. Messages are too fast for a normal DMM, which is why a scope is the right tool. DOCUMENTED (snippet), U, corroborated — [Snap-on, Automotive Communication Networks Pt II CAN](https://www.snapon.com/EN/US/Diagnostics/News-Center/CAN-Bus); [Wikipedia CAN bus](https://en.wikipedia.org/wiki/CAN_bus); [Gears, Riding the CAN Bus to School](https://gearsmagazine.com/magazine/riding-the-can-bus-to-school/)
- Fault patterns:
  - both lines at 0 V: short to ground
  - both lines at battery voltage: short to power
  - one line flat while the other switches: open on the flat line
  - one module with an internal short: can take down the whole bus ("bus off")
  
  To isolate a bad module, unplug modules one at a time while watching resistance or signal at the DLC (pins 6/14). DOCUMENTED (snippet), U; weak-to-moderate sources — [apextechnation CAN diagnostics (weak)](https://apextechnation.com/articles/can-bus-diagnostics); [diagnosistips CAN step by step](https://www.diagnosistips.com/automotiveacademy/can-bus/)
- U-code identities (SAE J2012): U0100 = Lost Communication with ECM/PCM "A". U0101 = Lost Communication with TCM. DOCUMENTED (snippet), U — [go-parts U0100](https://www.go-parts.com/garage/obd-u0100); [go-parts U0101 Chrysler 200](https://www.go-parts.com/garage/obd-u0101-chrysler-200-2015-2017). Note: one shift-by-wire snippet mislabeled "U0100 (Lost Communication with TCM)", so watch for that error in secondary sources.
- If P0700 appears alongside U0100, the TCM reported a fault and lost contact with the ECM. DOCUMENTED (snippet), weak — [Yahoo/U0100 explainer](https://tech.yahoo.com/general/articles/u0100-code-explained-lost-communication-201500362.html)

#### OBD II DTC types, MIL, freeze frame, permanent DTCs: A.6, A.7

- A two-trip monitor stores a **pending** DTC and freeze frame on the first failure. If the fault repeats on the next trip where that monitor runs, the MIL comes on and the code becomes **confirmed**. If it does not repeat, the pending code clears itself. DOCUMENTED (snippet), U, corroborated — [Innova, MIL/Pending/Confirmed/Permanent](https://www.innova.com/blogs/fix-advices/mil-pending-confirmed-permanent-history-and-oem-dtcs); [MOTOR, OBD II Up Close (1998)](https://www.motor.com/magazine-summary/obd-ii-close-july-1998/)
- Freeze-frame timing (older MOTOR text): GM and Ford store freeze frame when the MIL is lit, while Chrysler stores it on the first failure of a two-trip DTC. DOCUMENTED (snippet), manufacturer-dependent / dated (1998), SI — [MOTOR, OBD II Up Close](https://www.motor.com/magazine-summary/obd-ii-close-july-1998/)
- MIL-off rule: the MIL goes out after **three consecutive trips** without the fault. After **40 warm-up cycles** without the fault, the history DTC and freeze frame are erased. A warm-up cycle means coolant rises at least 40 °F (22 °C) from start temperature and reaches at least 160 °F (70 °C). DOCUMENTED (snippet), U — [Jeep WK OBD systems](https://jeepspecs.com/models/jeep-grand-cherokee/jeep-grand-cherokee-wk/on-board-diagnostic-systems/); [AutoZone repair guide, OBD II terminology](https://www.autozone.com/repairguides/Toyota-Matrix-2003-06/OBD-System-Information/OBD-II-Systems-Terminology/_/P-0996b43f80382479)
- **Permanent DTCs (PDTC):**
  - They appeared on some 2009 vehicles and became required on 2010 and later.
  - They are stored in non-volatile memory. A scan-tool clear or a battery disconnect does not erase them.
  - Their purpose is to stop someone from clearing codes to pass an in-use/I-M inspection.
  - The module erases a PDTC itself once the monitor runs and finds the fault gone.
  
  DOCUMENTED (snippet), U, corroborated — [California BAR, PDTC workshop presentation](https://www.bar.ca.gov/pdf/pdtc-workshop-presentation-4.18.2018.pdf); [Underhood Service, Ford PDTCs](https://www.underhoodservice.com/ford-permanent-diagnostic-trouble-codes-dtcs/); [Auto Service World, First Look at PDTCs](https://www.autoserviceworld.com/features/taking-a-first-look-at-permanent-dtcs/)
- PDTCs clear by **two different paths**. Sources that seem to disagree are each describing one of them:
  1. **Self-healing path.** The MIL goes off after three consecutive passing trips, and the PDTC clears with it. Some text words this as erasing "at the beginning of the fourth fault-free consecutive monitoring cycle".
  2. **After a scan-tool clear.** The confirmed DTC clears immediately, but the PDTC stays until **one** fault-free monitoring cycle in which the monitor runs and passes. Underhood Service gives the qualifying drive cycle as more than 10 min since start, with more than 5 min above 25 mph (40 km/h).
  
  DOCUMENTED (snippet), U/regulatory — [Underhood Service, Ford PDTCs](https://www.underhoodservice.com/ford-permanent-diagnostic-trouble-codes-dtcs/); [xtoolonline, Pending vs Stored vs Permanent](https://www.xtoolonline.com/articles/pending-stored-vs-permane-code); [RLEscalambre $0A PDTC](https://www.rlescalambre.net/0a-permanent-diagnostic-trouble-code-pdtc); [lodishell, OBD2 permanent codes](https://lodishell.net/2026/09/29/obd2-permanent-codes/)
- Clearing codes, or disconnecting the battery, resets all readiness monitors to "not ready/incomplete". EPA added readiness checks to catch last-minute code clearing. Repair verification (A.7) therefore means driving until the relevant monitor completes and passes; a clear with no returning code is not enough. DOCUMENTED (snippet), U — [Tomorrow's Technician, Using Readiness Monitors to Verify Emissions Repairs](https://www.tomorrowstechnician.com/using-readiness-monitors-to-verify-emissions-repairs/); [MOTOR, Using Emissions Drive Cycles to Verify Repairs](https://www.motor.com/magazine-summary/using-emissions-drive-cycles-to-verify-repairs/)
- P0700 = "Transmission Control System (MIL Request)". The TCM asks the ECM to light the MIL, and the specific transmission codes live in the TCM. A generic code reader may show only P0700, so scan the TCM directly. DOCUMENTED (snippet), U, corroborated — [Edmunds P0700](https://www.edmunds.com/obd-dtc/p0700.html); [CARiD P0700 MIL Request](https://www.carid.com/articles/p0700-transmission-control-system-mil-request.html); [obd-codes P0700 (listing)](https://www.obd-codes.com/p0700)

#### Shift-by-wire / electronic shifter: A.28

- GM's ETRS (Electronic Transmission Range Select) arrived in 2017 on models such as the Buick LaCrosse and Cadillac XT5. It uses:
  - two shifter sensors sending X-Y position over four inputs to the Chassis Control Module (K38)
  - the CCM commanding a Transmission Range Control Module (TRCM, K173)
  - the TRCM moving the manual shaft, working with the TCM (K71)
  
  GM provides service modes for no-move or stuck-in-Park diagnosis, and bidirectional range commands exist (cross-ref `scan_tool_bidirectional.md`). DOCUMENTED (snippet), GM — [Gears, Shift Time: GM's New Electronic Shifter](https://gearsmagazine.com/magazine/shift-time-gms-new-electronic-shifter/); [Gears, 9T50 Problems and Diagnosing](https://gearsmagazine.com/magazine/9t50-problems-and-diagnosing/)
- Shift-by-wire shifters typically use redundant position sensors. A faulty park-position switch inside the shifter causes the GM "Shift to Park" message (2017–2024 Enclave, Traverse, Acadia, XT6). A gear-shift-position circuit fault (for example P0914) can cause no-start in Park, locked-out gears, or a PRNDL mismatch on the cluster. DOCUMENTED (snippet), GM example + patents — [go-parts, GM "Shift to Park"](https://www.go-parts.com/garage/transmission-shift-lever-buick-enclave-chevrolet-traverse-cadillac-xt6-2017-2024); [USPTO 9249877 position diagnostic for SBW](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/9249877); [icarsoft P0914 (weak)](https://www.icarsoft-us.com/blogs/news/p0914-code-gear-shift-position-circuit)

#### Inputs that change shift timing and quality: A.19, A.23

- The TCM uses TPS/load, ECT and vehicle speed to set shift points and apply pressure. A TPS with a dead spot or an erratic signal makes the TCM misjudge load, giving inconsistent quality (sometimes harsh, sometimes soft), late or harsh shifts, or early soft shifts, and it affects kickdown. DOCUMENTED (snippet), U, weak-to-moderate, corroborated across several sources — [apextechnation harsh shift (weak)](https://apextechnation.com/articles/harsh-shift-diagnosis); [General Transmission, What controls your transmission](https://generaltransmissionreno.com/what-controls-your-transmission/); [HondaCivicForum, TPS late/hard](https://www.hondacivicforum.com/forum/mechanical-problems-technical-chat-8/bad-tps-transmission-shifts-late-hard-87798/)

### Inferences
- **Driver type decides what a short does** (A.20, A.26; INFERRED from the ST/TI driver-protection principle, U; confirm the driver type in SI).
  - On a **low-side-driven** solenoid (fed B+ and grounded by the TCM), a control wire shorted to ground turns the solenoid **on** permanently and the TCM cannot turn it off. A short to B+ on that wire means the TCM sees overcurrent when it switches on, and the solenoid stays off.
  - On a **high-side-driven** solenoid, a control wire shorted to ground shows up as overcurrent or "circuit low" with the solenoid off. A short to B+ keeps it on.
- **Checking a PWM or low-side trace on a scope** (INFERRED, U):
  - For a low-side-driven solenoid, the control-wire trace sits at system voltage when off, is pulled near 0 V when on, and shows an inductive spike at turn-off. A voltage-only trace can look normal with a partially shorted coil, which is why the amp-clamp current ramp is the stronger test.
  - Duty cycle read on a scope depends on which side you measure. For a low-side driver, the low portion of the control-wire trace is the on-time.
- **Suffix logic for DTCs** (INFERRED from the SAE J2012 naming pattern seen across P07xx/P09xx, U):
  - "Circuit / Open / Low / High / Electrical" (P0753, P0960/62/63, P0712/13, P0715 circuit) are electrical, and a DMM or scope applies.
  - "Performance / Stuck Off / Stuck On / Incorrect Ratio" (P0751/52, P0741/42, P0731–36) are functional results inferred from speed ratios or slip, and the fault may be hydraulic or mechanical even with a good circuit.
- **A.7 verify-repair sequence** (INFERRED synthesis):
  1. Record the DTCs and freeze frame.
  2. Repair.
  3. Clear the codes.
  4. Drive under the freeze-frame conditions until the relevant monitor or DTC status reports "ran/passed". Transmission DTCs usually have their own "test passed this ignition" status in SI.
  5. Confirm no pending code.
  6. Expect any PDTC to stay until the monitor passes.

### Gaps
- No citable generic ISS/OSS resistance or AC output values. Only ABS WSS numbers were found. SI.
- No citable per-range resistance or voltage table for resistive TR sensors. SI.
- No citable solenoid resistance values (on/off vs PWM vs VFS), and no typical transmission solenoid current values. SI.
- GM enable criteria from the GM "OBDG" transmission-diagnostics PDF (ignition-voltage window, Type A/B/C DTC classes, TCC slip thresholds) could not be read because of the proxy. That document is the best GM-specific source to pull by hand: https://gsitlc.ext.gm.com/gmspo/mode6/pdf/2012/12OBDG01B%20Transmission%20Diagnostics.pdf
- The GM voltage-drop technical tip (TT 97-20-01) and any GM-specified max voltage drop were not readable.
- No ASE-published statement of "the" max voltage-drop number. ASE questions usually give the spec or compare readings.

---

## Key Question 2: What symptom patterns point to electrical vs. hydraulic/mechanical causes?

### Takeaway
Electrical control faults tend to be **erratic, intermittent, multi-symptom, and tied to voltage, temperature or vibration**. They set circuit-type DTCs and often force a fixed default gear with a firm or harsh feel. Hydraulic or mechanical faults are **consistent and repeatable** (the same slip on the same shift every time). They set ratio, performance or slip DTCs with no circuit code, and they often come with fluid condition clues. "Incorrect ratio" means the module measured slip, not that it found an electrical fault.

### Cited Findings
- **P0730–P0736 (incorrect gear ratio)**: the computer sees a mismatch between input and output speed for the commanded gear, and the cause may be hydraulic, mechanical or electronic. Listed causes: low or dirty fluid, worn clutches, broken bands, a failing pump, damaged planetaries, internal blockage, plus solenoid or TCM faults. DOCUMENTED (snippet), U, corroborated — [RepairPal P0730](https://repairpal.com/obd-ii-code-p0730); [YourMechanic P0730](https://www.yourmechanic.com/article/p0730-obd-ii-trouble-code-incorrect-gear-ratio-by-ian-swan); [eeuroparts P0730](https://eeuroparts.com/blog/p0730-code-incorrect-gear-ratio); [OBD2.com P0730](https://obd2.com/dtc/p0730-incorrect-gear-ratio/)
- "Erratic behavior points to the control side … module, its power and ground supply, or its sensor inputs … mechanical wear tends to produce consistent problems, while electronic faults produce random ones." A TCM brownout (reset during high electrical load, such as braking with the A/C on) causes erratic shifts. DOCUMENTED (snippet), U, weak source (a shop/blog aggregator; the principle fits the TD case studies) — [automodulelab, limp mode / harsh shifting TCM guide (weak)](https://www.automodulelab.com/blog/transmission-limp-mode-harsh-shifting-tcm-diagnosis-guide/); [Transmission Digest, Intermittent TCM Operation](https://www.transmissiondigest.com/intermittent-tcm-operation-creates-diagnostic-puzzle/)
- **Default/limp mode** on low voltage (Allison example): the TCM inhibits TCC, freezes adapts, and defaults to 3rd with rough engagements. With a failed TR sensor: blank or wrong PRNDL display and a fixed-gear default. DOCUMENTED (snippet), SI — [Transmission Digest P0562](https://www.transmissiondigest.com/multiple-causes-for-p0562/); [Gearstar TR sensor](https://gearstar.com/blog/what-happens-when-a-transmission-range-sensor-goes-bad/)
- **Mechanical failure that looks like an electrical default** (GM example): on the 6L80, a cracked 3-5-R wave plate causes loss of 3rd, 5th and reverse, with 2-3/4-5 flare, harsh engagement then no gear, and fine metal in the pan. P0776 (clutch pressure control solenoid stuck off) on this unit can indicate *anything* in the 3-5-R apply chain, including the TEHCM, valve body or pump stator sealing rings. So a solenoid-named DTC does not prove a bad solenoid. DOCUMENTED (snippet), GM — [silveradosierra 6L80 info thread](https://www.silveradosierra.com/threads/gm-6l80-transmission-information-thread.753826/); [Sonnax, 6L45/50/80/90 No Movement](https://www.sonnax.com/tech_resources/1216-gm-6l45-50-6l80-90-no-movement-conditions-analysis-repair-tips)
- **Solenoid mechanical sticking vs electrical failure**: P0742 TCC stuck on can come from debris jamming the solenoid plunger open, a hydraulic or contamination cause, with the circuit intact. DOCUMENTED (snippet), U — [icarsoft P0742 (weak)](https://www.icarsoft-us.com/blogs/news/p0742-code-torque-converter-clutch-stuck-on-fix); [RepairPal P0742](https://repairpal.com/obd-ii-code-p0742)
- **TCC slip pattern**: steady slip of 50–200 RPM while commanded on points to friction, apply pressure or fluid (hydraulic/mechanical). Slip equal to full engine-minus-turbine speed points to no apply at all (solenoid, circuit or apply circuit). DOCUMENTED (snippet), weak source, SI — [apextechnation P0741 (weak)](https://apextechnation.com/articles/p0741-torque-converter-clutch-code)
- **Line-pressure solenoids can fail electrically or mechanically**, and the symptoms depend on which solenoid (GM LPC example). DOCUMENTED (snippet), GM — [monstertransmission 6L80 guide (weak)](https://monstertransmission.com/blogs/news/the-ultimate-6l80-transmission-guide-common-problems-fixes-installation-tips)

### Inferences
- **Several unrelated U-codes plus erratic shifting plus a weak battery** means fixing the power supply or network first (battery, charging, grounds, CAN resistance) before any transmission work. (A.21, A.19/A.20; INFERRED from the U0100/P0562 findings, U)
- **Default-gear feel as a clue** (A.23; INFERRED, U/SI):
  - A fixed gear on the upshift side (commonly 2nd/3rd/4th depending on the design) plus a harsh engagement plus a circuit DTC suggests the TCM has de-energized its outputs and pressure control has defaulted to maximum.
  - Slipping or flaring only on specific shifts, with no circuit DTCs, suggests a hydraulic/mechanical cause.
  - Which gear is the default and whether the PC solenoid is normally high are unit-specific (SI).
- **TFT fault symptoms** (A.18/A.19; INFERRED from the Toyota open/short behavior plus hot-mode strategy, U):
  - Open (reads cold): the TCC may be inhibited, shifts may run late or firm on cold-strategy tables, and overdrive may be delayed.
  - Shorted (reads hot): early TCC, possible 4th/OD inhibit or hot-mode schedule.
  - Either way, the scan-data TFT reading stays pinned at −40 or 150+ °C regardless of actual temperature, which is the quick discriminator.
- **Before blaming a speed sensor, check the speed agreement pattern** (A.26; INFERRED):
  - ISS/OSS agree with engine RPM and VSS but a ratio code sets: slip (mechanical).
  - One speed signal drops to zero or spikes while the vehicle is steady: sensor or circuit, or air gap (VR), or wiring noise.

### Gaps
- I found no authoritative public table of default (limp) gears by transmission family. Mention the concept, but pull the actual gear from SI.
- I found no Motor Age or ASE-authored article giving a formal "electrical vs mechanical discrimination" checklist. The patterns above are synthesized.

---

## Key Question 3: Common reasoning traps?

### Takeaway
Most traps come from reading a DTC title as the cause, choosing a test that cannot detect the fault, or skipping power, ground and network checks. The findings below each rest on a cited source. Where a trap is my own synthesis, it is tagged INFERRED.

### Cited Findings
- **Trap: "P0700 means a TCM failure."** P0700 is only the TCM's MIL request. The real codes are in the TCM. DOCUMENTED (snippet), U — [Edmunds P0700](https://www.edmunds.com/obd-dtc/p0700.html); [CARiD](https://www.carid.com/articles/p0700-transmission-control-system-mil-request.html) (A.6)
- **Trap: "P0730–P0736 or a P075x 'performance/stuck' code means replace a solenoid."** Ratio and performance codes are functional, and they list low or dirty fluid and worn clutches, bands and pump among the causes. DOCUMENTED (snippet), U — [RepairPal P0730](https://repairpal.com/obd-ii-code-p0730); [go-parts P0751](https://www.go-parts.com/garage/obd-p0751) (A.19, A.23)
- **Trap: "P0715 means replace the sensor."** It is a circuit-monitor code and not proof the sensor failed; check wiring and connectors. DOCUMENTED (snippet) — [staff-capital P0715](https://digital.staff-capital.com/en/dtc/p0715/?manufacturer=GENERIC) (A.26)
- **Trap: ohm-checking a Hall/MR sensor.** It is invalid and can damage the sensor. Check reference, ground and signal toggle instead. DOCUMENTED (snippet), U — [Gears, Advanced Speed Sensors](https://gearsmagazine.com/magazine/advanced-speed-sensors-part-1/); [industrialmonitordirect (weak)](https://industrialmonitordirect.com/blogs/knowledgebase/identifying-and-replacing-automotive-hall-effect-speed-sensors) (A.26)
- **Trap: expecting a steady voltage from a two-wire active sensor.** Its signal is a 7/14 mA current, so measure current or read across the module's sense resistor. DOCUMENTED (snippet) — [Pico AK protocol](https://www.picoauto.com/library/product-news/ak-protocol-decoding-with-picoscope-oscilloscope) (A.26)
- **Trap: condemning a VR sensor for low output without checking air gap or debris.** A wide gap or a debris-coated tip lowers amplitude, especially at low speed. DOCUMENTED (snippet) — [aa1car](https://www.aa1car.com/library/diagnosing_abs_wheels_speed_sensors.htm); [Brake & Front End](https://www.brakeandfrontend.com/diagnosing-hub-units-and-wheel-speed-sensors-air-gap-issues-and-dtcs/) (A.26)
- **Trap: trusting an ohmmeter or continuity test on power/ground or harness.** Load or voltage-drop testing finds resistance that continuity misses (the TD TCM circuit dropped to 9.7 V under load). A DMM also cannot find winding-to-winding shorts. DOCUMENTED (snippet) — [Transmission Digest](https://www.transmissiondigest.com/intermittent-tcm-operation-creates-diagnostic-puzzle/); [Gears, Resistance Pt 2](https://gearsmagazine.com/magazine/resistance-multimeter-diagnostics-part-two/) (A.21, A.27)
- **Trap: measuring CAN termination with the key on, or misreading 120 Ω.** Measure with power off. 60 Ω is good and 120 Ω means one terminator is open. DOCUMENTED (snippet) — [Kvaser](https://kvaser.com/developer-blog/how-to-test-your-can-termination-works-correctly/); [Enovation](https://support.enovationcontrols.com/hc/en-us/articles/360038856494-CAN-BUS-Troubleshooting-Guide-with-Video) (A.19/A.20)
- **Trap: using a DMM to "see" CAN traffic.** Messages are too fast (about 215 µs), so use a scope. DOCUMENTED (snippet) — [Snap-on CAN Bus](https://www.snapon.com/EN/US/Diagnostics/News-Center/CAN-Bus) (A.5, A.20)
- **Trap: swapping modules on U-codes before checking the battery and charging system.** A weak battery or voltage dips commonly cause lost-communication codes. DOCUMENTED (snippet), weak-moderate — [AxleAddict U0100](https://axleaddict.com/repair-maintenance/u0100-code-lost-communication-with-ecm-pcm); [Transmission Digest P0562](https://www.transmissiondigest.com/multiple-causes-for-p0562/) (A.21)
- **Trap: mixing up U0100 and U0101.** U0100 = ECM/PCM and U0101 = TCM. At least one secondary source mislabels U0100 as the TCM. DOCUMENTED (snippet) — [go-parts U0100](https://www.go-parts.com/garage/obd-u0100); [go-parts U0101](https://www.go-parts.com/garage/obd-u0101-chrysler-200-2015-2017) (A.20)
- **Trap: "clear the codes and the permanent DTC is gone," or "clearing verifies the repair."** A PDTC survives a scan-tool clear and a battery disconnect, and clears only after the monitor runs and passes. Clearing also resets readiness to incomplete. DOCUMENTED (snippet), U — [California BAR PDTC](https://www.bar.ca.gov/pdf/pdtc-workshop-presentation-4.18.2018.pdf); [Underhood Service](https://www.underhoodservice.com/ford-permanent-diagnostic-trouble-codes-dtcs/); [Tomorrow's Technician](https://www.tomorrowstechnician.com/using-readiness-monitors-to-verify-emissions-repairs/) (A.6, A.7)
- **Trap: "the MIL goes off as soon as it's fixed."** It takes three consecutive fault-free trips, and the history code stays for 40 warm-up cycles. DOCUMENTED (snippet) — [Jeep WK OBD](https://jeepspecs.com/models/jeep-grand-cherokee/jeep-grand-cherokee-wk/on-board-diagnostic-systems/) (A.6)
- **Trap: "brake lights work, so the brake switch is fine" when the TCC won't apply.** Brake lamps and cruise cancel can work while the TCC-release contact or signal is wrong. DOCUMENTED (snippet), GM/older — [dieselplace](https://www.dieselplace.com/threads/brake-pedal-switch-failure-tcc-operation.398647/) (A.18)
- **Trap: reversing the TFT open/short interpretation.** Open = −40 (cold) and short = 150 °C+ (hot), per Toyota factory manuals. A secondary source has it backwards. DOCUMENTED (snippet) — [Toyota A750E RM](https://www.purefjcruiser.com/docs/2007%20Toyota%20FJ%20Cruiser%20Repair%20Manual/A750E%20Automatic%20Transmission/Automatic%20Transmission%20System/0160014.pdf) vs [go-parts P0712](https://www.go-parts.com/garage/obd-p0712) (A.19, A.26)
- **Trap: assuming more current always means more pressure on a VFS.** A normally high VFS lowers pressure as current rises. DOCUMENTED (snippet) — [Wikipedia VFS](https://en.wikipedia.org/wiki/Variable_force_solenoid); [Gears 8L90](https://gearsmagazine.com/magazine/8l90-solenoid-strategies/) (A.26; cross-ref `hydraulic_pressure_testing.md`)
- **Trap: blaming the transmission for TPS-driven shift complaints.** A bad TPS or load signal causes harsh, late, soft or erratic shifts. Check engine inputs and engine DTCs first. DOCUMENTED (snippet), weak-moderate — [General Transmission](https://generaltransmissionreno.com/what-controls-your-transmission/); [apextechnation (weak)](https://apextechnation.com/articles/harsh-shift-diagnosis) (A.19, A.23)
- **Trap (shift-by-wire): replacing the transmission or TR switch for a "Shift to Park" or no-start-in-Park complaint.** A park switch inside the shifter, or a shifter position circuit fault, is common. Diagnose the shifter and the CCM/TRCM network path first. DOCUMENTED (snippet), GM — [go-parts GM Shift to Park](https://www.go-parts.com/garage/transmission-shift-lever-buick-enclave-chevrolet-traverse-cadillac-xt6-2017-2024); [Gears, GM Electronic Shifter](https://gearsmagazine.com/magazine/shift-time-gms-new-electronic-shifter/) (A.28)
- **Trap: assuming a solenoid-named DTC means the solenoid is bad.** On the 6L80, P0776 can come from anything in the 3-5-R chain (TEHCM, valve body, stator sealing rings). DOCUMENTED (snippet), GM — [silveradosierra 6L80 thread](https://www.silveradosierra.com/threads/gm-6l80-transmission-information-thread.753826/) (A.19, A.23)

### Inferences
- **Trap: measuring voltage at the battery instead of at the TCM.** Only a reading at the TCM's power and ground pins, under load, rules out a circuit drop. (INFERRED from the P0562 "measure at the TCM" guidance, U; A.21)
- **Trap: calling a single high voltage-drop reading "bad" without context.** Voltage drop scales with current. Compare against the source's spec for that circuit, and remember an unloaded circuit shows about 0 V drop even with a bad connection. (INFERRED from the "test under load" principle, U; A.27)
- **Trap (driver type): assuming "short to ground" always means "solenoid dead."** On a low-side-driven solenoid, a grounded control wire makes it *always on*. (INFERRED, U; A.20/A.26)
- **Trap (road test, A.16): road-testing without reproducing the freeze-frame conditions.** Also: not graphing commanded gear vs actual ratio, TCC command vs slip, and ISS/OSS/TFT during the event, or road-testing an intermittent without a wiggle test or scope recording. (INFERRED synthesis, U)

### Gaps
- I found no public ASE-authored list of A2 electrical "traps". This list is built from test-method literature and DTC-definition sources, not from any ASE question source (none used, per constraints).
- ScannerDanner video and course content could not be read (search indexed only forum posts). Motor Age A2-specific electrical articles did not appear in results. Direct Pico guided-test pages for transmission ISS/OSS and solenoids surfaced only as titles, not content.
- The GM TechLink shift-by-wire and low-voltage articles did not surface in snippets beyond a TechLink PDF title.
