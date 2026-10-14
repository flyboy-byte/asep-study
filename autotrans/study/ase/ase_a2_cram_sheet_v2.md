## 0. Confirmed weak spots (Unit 1 quiz, Unit 2 test)

- **Carrier holds the planets.** Ring = big outer gear, internal teeth = **the "internal gear."** Sun = center, never the internal gear.
- **Ratios in series multiply.** Ravigneaux = 2 suns, 2 planet sets, 1 carrier, 1 ring. LePelletier = simple + Ravigneaux.
- **Reaction clutch steels splined to the case.** Disconnected member = neutral. **Carrier held = reverse.**
- **Stall (missed both on the Unit 2 test): HIGH = transmission only. LOW = engine OR stator.** Converter can never make stall high.
- **Your risk on electronics:** a **performance** DTC with a good circuit = hydraulic or mechanical, not "solenoid OK, done."

| In | Held | Out | Result (30/70) |
|---|---|---|---|
| Sun | Ring | Carrier | Reduction 3.33 |
| Ring | Sun | Carrier | Reduction 1.43 |
| Carrier | Sun | Ring | Overdrive 0.70 |
| Carrier | Ring | Sun | Overdrive 0.30 |
| Sun | Carrier | Ring | **Reverse** 2.33 |
| Ring | Carrier | Sun | **Reverse** 0.43 |
| Any two driven | — | — | Direct 1:1 |

## 1. Reasoning moves

- **Exam:** 45 scored of 55, 75 min. Area A diagnosis 26 (58%), B in-vehicle 12 (27%), C R&I 7 (15%). Book answer beats shop habit. Tech A/B: judge each alone; "both" and "neither" are valid.
- **Strategy-based diagnosis (GM):** 1 verify → 2 operating as designed? (yes = stop, explain, compare to an identical vehicle) → 3 preliminary checks → 4 Diagnostic System Check → 5 bulletins, recalls, **software before a module** → 6 path: current DTC / symptom no DTC / no published diag / intermittent-history → 7 isolate, repair, **verify** → 8 re-examine; not fixed = back to 1.
- **Diagnostic order:** verify concern, fluid (level, type, condition), SI/codes, rule out engine and inputs, road test and scan data, line pressure, stall only if SI has one, repair, clear with scan tool, relearn, verify.
- **Apply chart:** several failed ranges, find the element in all of them. One failed range, the element unique to it. Anything applied in a working range is cleared. Slip or no drive = fails to hold. Tie-up or braked feel = seized or not releasing.
- **Planetary:** sun = center, external teeth. **Carrier holds the planets.** **Ring = outer gear with internal teeth = the "internal gear."** One driven, one held, one output. Two driven together = direct. Nothing held = neutral. Carrier held = reverse. Carrier output = reduction, carrier input = overdrive.
- **Ratios in series multiply.** 2:1 then 3:1 = 6:1. **Ravigneaux** = 2 suns, 2 planet sets, 1 carrier, 1 ring. **LePelletier** = simple planetary + Ravigneaux.
- **Reaction clutch:** steel plates splined to the **case**. One-way clutches: roller, sprag, mechanical diode; hold one way, overrun the other. Synchronous (clutch-to-clutch) shifts need timing, no one-way clutch. Nonsynchronous uses a one-way clutch.
- **Low roller clutch** = slip in D1 only, not every forward gear. **Allison 1000 reverse** = C3 + C5.

## 2. Mechanical and hydraulic

- **Fluid, no dipstick:** scan-tool temperature inside SI window, level vehicle, engine running, level plug. Drip = right, stream = overfull, none = low. Low or overfull (aeration) both slip. Cold slip or flare when cornering that clears warm = low level.
- **Milky pink ATF:** replace radiator/cooler, overhaul (seals, frictions, converter), flush. Flush and refill alone is the distractor. Cooler leak: coolant gets into the ATF (and ATF can reach the coolant).
- **Pan drop** replaces only part of the fluid. Pan debris: friction material black, steel magnetic, brass and aluminum not magnetic.
- **Shift terms:** flare = release before apply, rpm up. Tie-up = bind-up = overlap, output braked. Slide-bump = accumulator bottoms out early. One harsh shift = that shift's accumulator.
- **Pressure:** low in all ranges = supply (fluid, filter, pump, regulator). Low in one range = that circuit's leak. High in all = regulator or EPC failsafe. Reverse runs higher. Order: fluid, line pressure, then stall. Do not stall-test if line pressure is low.
- **Stall:** high = transmission element slipping. Low = weak engine (rule out first) or freewheeling stator. **Freewheeling stator:** poor launch, normal at speed, low stall. **Seized stator:** good launch, poor top end, overheating; stall test not diagnostic.
- **TCC won't apply** = usually an input blocking it (brake switch, TPS, cold temp reading, speed signal).
- **TCC:** stuck on = stalls at a stop. Commanded on and slip stays high = not holding (check apply pressure, bores, stator-support bushing, turbine seal). Shudder disappears with TCC off or fully locked. Misfire does not.
- **Valves:** switch routes, servo moves a valve, regulator controls pressure. Ruptured vacuum modulator = ATF in the vacuum hose, white smoke, fluid loss with no leak.
- **Not the transmission:** misfire, TPS/MAF/MAP, wheel-speed or ABS data, tire size, mounts. Test before replacing.

## 3. Electronic

- **Commanded vs. actual.** Current tracks the command but no pressure or ratio change = hydraulic or mechanical. No current tracking = electrical. A solenoid click proves only the coil moved.
- **Performance DTC (ratio, slip, stuck) with a good circuit** = hydraulic or mechanical. **Circuit DTC (open, low, high)** = test the circuit.
- **TFT (NTC):** open = very cold (high signal voltage, P0713). Short to ground = very hot (P0712).
- **EPC (classic):** more current = lower pressure. Unplugged = maximum pressure, harsh. Read the stem for another design.
- **ISS (turbine) and OSS (vehicle speed):** hall-effect, no ohmmeter. Ratio = ISS ÷ OSS. TCC slip = engine rpm − turbine rpm. Bad signal gives ratio DTCs on a healthy unit.
- **Pressure switches:** read as an on/off pattern to confirm the real gear. **TR/MLP:** compare range PID with the lever.
- **Voltage drop under load,** not ohms. Several U-codes at once = battery, power, ground or bus first.
- **OBD II:** MIL off after 3 clean trips. History erases at 40 warm-ups (many OEMs say 80 for misfire/fuel). **Permanent DTCs** are not cleared by a scan tool or battery pull. Clear with the scan tool, never a battery pull, then verify with monitors.
- **Adapts:** clearing is not a repair. Relearn after TCM, valve body or transmission replacement. Load solenoid-body characterization data. Programming needs a battery maintainer, not a charger.

## 4. Area B and Area C

- **B:** linkage, then TR switch, then module. Worn tailshaft bushing needs more than a new seal. ATF in a TCM connector means fix the pass-through leak too. Valve body: separator plate and gasket must match, check balls in place, torque from the center out, new slip after service = suspect the job. Accumulator is not a backup pressure store. TBV stuck in bypass = no cooler flow = overheats. After failure, flush and flow-check the cooler.
- **C:** cracked flexplate or case = alignment (dowels). Converter must seat in stages, never pull it on with the bellhousing bolts. Missing dowels or an unseated converter ruin the pump. End play with a dial indicator, fix with shims or thrust washers. Soak new frictions. Air test with low, clean, dry air: thud is good, hiss is a leak. One-way clutches can go in backward, bench-check rotation. Thrust washers: petroleum jelly, not white grease. Relearn after install.
- **Types:** DCT has no converter, no stall test, no apply chart. Odd-even shaft split is its chart. CVT: do not use generic ATF; one-direction ratio fault = that primary circuit; low clamp = belt slip.
