## 0. How to Use This Sheet

This is the middle layer between the 34-page study guide and the cram sheet. It has enough explanation to reason through a Tech A/B or "most likely" stem, without the guide's depth. Everything here comes from the study guide; section numbers in brackets (**[G 2.4]**) point to the full explanation.

**The exam:** 55 questions, **45 scored**, 75 minutes, about 80 seconds each. Unscored items aren't marked, so treat every one as scored. No penalty for guessing: never leave one blank.

| Area | Scored Qs | Share | Questions per task | What it rewards |
|---|---:|---:|---:|---|
| **A. Diagnosis** | 26 | **58%** | ~0.9 | Symptom → cause → the check that separates causes |
| **B. In-vehicle maintenance and repair** | 12 | **27%** | **1.0 (best yield)** | Verify the cheap root cause before replacing the expensive part |
| **C. Removal, inspection, installation** | 7 | 15% | ~0.3 | Order of steps and classic mistakes, not specs |

**Two nights left:**

| When | Do this |
|---|---|
| **Tonight (Tue)** | Read this sheet start to finish. For anything that doesn't click, open the guide section in brackets. Spend extra time on **A.3 (apply chart + planetary)**, your biggest miss area |
| **Wed night (after the class final)** | Send me what the final exposed. Then the cram sheet, then the trap list in Section 5 here |
| **Thu morning** | Cram sheet only. Stop early |

---

## 1. Area A: Diagnosis (58%, 26 questions)

### A.1 The method that answers "first" and "next" stems
**Diagnostic order [G 7.4]:** verify the concern → fluid level, condition and type (the SI way) → SI, bulletins, DTCs (the code is the starting point, not the diagnosis) → rule out engine, inputs, cooler and electrical supply → road test and scan data → **line pressure** → stall test only if the OEM publishes one → repair, clear with the scan tool, relearn, **verify**.

**GM strategy-based diagnosis [G 8]:** 1 verify the concern → 2 is it operating as designed? (if **yes, stop and explain**, compare with an identical vehicle) → 3 preliminary checks (visual, history, sounds and smells, DTCs) → 4 Diagnostic System Check → 5 bulletins, recalls, **software** (check for an update **before** replacing a module) → 6 diagnostic path: **6.1 current DTC**, **6.2 symptom no DTC**, **6.3 no published diagnostic** (build a plan from schematics), **6.4 intermittent/history** → 7 isolate, repair, **verify** → 8 re-examine; not fixed = **back to step 1**. A "what next" stem is asking where you are on this chart.

**Question words:** *could cause* = one valid mechanism is enough. *Most likely* = the choice that explains **every** symptom in the stem. *First/next* = cheapest, least invasive, most informative. *EXCEPT* = mark each "yes/no"; the single "no" wins. *Tech A/B* = judge each alone; "both" and "neither" are real answers.

**Book answer beats shop habit.** Clear codes with the scan tool (never a battery pull). Check the level the SI way. Test before replacing. Reset adapts is not a repair.

### A.2 Classify the symptom first [G 2]
Before reading the choices, ask what the symptom **follows**:

| Follows… | Think first of… |
|---|---|
| Engine rpm (also in P/N) | Pump, converter, flexplate |
| Road speed | Gear train, output, final drive, tires, driveline |
| One gear or range only | The element **unique** to that range (apply chart) |
| Every range | Fluid, pump/pressure, input clutch, manual valve/linkage |
| Cold only, clears warm | Fluid level, thick-fluid or bore-leak effects |
| First engagement after sitting | Converter drain-back |
| Engine data or wheel-speed data | **Not the transmission** (misfire, TPS, MAF, ABS, tire size, mounts) |

### A.3 Apply chart and planetary: your biggest risk [G 1]
**The names (Unit 1 misses):** **sun** = small center gear, external teeth. **Carrier holds the planets** (it is not the big outer gear). **Ring = big outer gear with internal teeth = the "internal gear."** The sun is **never** the internal gear.

**The rules:** one member **driven**, one **held**, one **output**. Find the carrier: **output = reduction, input = overdrive, held = reverse.** Any **two** members driven together = **direct 1:1**. Nothing held or a member disconnected = **neutral**.

| Input | Held | Output | Result | 30/70 example |
|---|---|---|---|---|
| Sun | Ring | Carrier | Reduction (steepest) | 3.33:1 |
| Ring | Sun | Carrier | Reduction | 1.43:1 |
| Carrier | Sun | Ring | Overdrive | 0.70:1 |
| Carrier | Ring | Sun | Overdrive (steepest) | 0.30:1 |
| Sun | Carrier | Ring | **Reverse**, reduction | 2.33:1 |
| Ring | Carrier | Sun | **Reverse**, overdrive | 0.43:1 |
| Any two driven | Nothing | Whole set | Direct | 1:1 |

Swap input and output and the ratio flips to its reciprocal. **Ratios in series multiply, never add** (2:1 then 3:1 = 6:1; a big number is not a mistake). **Ravigneaux** = two suns, two planet sets, one carrier, one ring. **LePelletier** = simple planetary + Ravigneaux. **Reaction (holding) clutch:** steel plates splined to the **case**.

**Apply-chart elimination [G 1.3]:**

1. Sort ranges into **affected** and **working** (include Park, Neutral, manual ranges, engine braking).
2. Several failed ranges → the element applied in **all** of them. One failed range → the element used **only** there.
3. Anything applied in a **working** range is cleared.
4. **Slip, flare, no drive** = an element that fails to **hold**. **Tie-up, bind, braked feel** = an element **seized or not releasing**, showing up where the chart says it should be off.
5. **Slip in D1 but fine in manual 1** = the one-way clutch (manual 1 backs it up with a friction element).

*Worked example:* no 3rd and no reverse, 1st and 2nd fine. 3rd = forward + direct; reverse = direct + low/reverse. Common to both: **direct**. Forward is cleared because it works in 1st and 2nd.

> **ASE trap:** a first-gear-only one-way clutch can't cause slip in **every** forward gear. Slip in all forward gears with reverse OK = forward/input clutch or its circuit. A seized element binds; it doesn't leave you without a range.

### A.4 Line pressure [G 2.4]
**Order:** fluid → line pressure → stall only if SI has one. **Low line pressure: don't stall test.**

| Reading | Most likely |
|---|---|
| **Low in all ranges** | Common supply: low fluid, clogged filter or suction air leak, worn pump, weak/stuck regulator, big common leak |
| **Low in one range** | Leak in the circuit fed only in that range (piston seal, sealing ring, servo seal) |
| **High in all ranges** | Stuck regulator; **EPC in failsafe** (unplugged/open = **maximum**); TV cable tight or modulator vacuum lost (older units) |
| **Normal pressure, no engagement** | Routing (manual valve, shift valve, check ball) or mechanical (broken clutch, sprag) |

- **Reverse reads higher by design.** Low in reverse only = reverse circuit.
- **Classic EPC: more current = lower pressure.** The scan tool shows the **command**; only a gauge shows **pressure**.
- **Vacuum modulator:** low vacuum (load, leak, disconnected hose) = high pressure, firm late shifts. Ruptured diaphragm = ATF in the vacuum hose, white smoke, fluid loss with no visible leak.

### A.5 Torque converter, stall and TCC [G 2.6, 3.5]
**Impeller = engine. Turbine = input shaft.** Engine rpm = impeller; ISS = turbine. **TCC slip = engine rpm − turbine rpm.** Most heat comes from the converter, worst at stall.

| | Stator **freewheels** (won't hold) | Stator **seized** (won't release) |
|---|---|---|
| Launch | **Poor** | Normal |
| Highway | Normal (above ~35 mph) | **Poor**, overheats |
| Stall test | **Low** | Not diagnostic |

- **High stall = a transmission element slipping.** Nothing inside the converter raises stall. "200 rpm high = stator" is backwards.
- **Low stall** = weak engine (rule out first, incl. restricted exhaust) or freewheeling stator.
- **TCC stuck on:** engine stalls or nearly stalls at a stop; slip ~0 at a stop.
- **TCC commanded on, slip stays high** = the **apply side** isn't holding. Check apply pressure and leaks before the piston (TCC valve bores, stator-support bushing, turbine-shaft seal) before condemning the converter.
- **TCC won't apply** usually means an **input** blocks it: brake switch reads "applied," TP dead spot, cold-reading temp sensor, no speed signal.
- **Shudder vs. misfire:** true TCC shudder is gone with the TCC **off** and gone fully **locked**. A misfire follows firing frequency, shows in misfire data, and is often **worse** locked. **Fluid** is the first suspect for shudder.

### A.6 Shift quality [G 2.2]
Every shift is a handoff.

| Term | Cause | Rpm |
|---|---|---|
| **Flare** | Off-going releases **before** on-coming holds | Rises briefly |
| **Tie-up = bind-up** | Overlap: two ratios at once, or an element won't release | Pulled **down**, output braked |
| **Slide-bump** | Accumulator bottoms out before the shift ends | Smooth start, harsh finish |
| **One harsh shift** | That shift's accumulator (spring, piston, seal) | — |
| **All shifts harsh** | High line pressure | — |

**Noise:** whine in P/N that rises with rpm = pump (or clogged filter, air at pickup). Clunk only after an auto-restart = stop/start hold system.

### A.7 Electronic: commanded vs. actual [G 3]
Your strongest area. One habit answers most items: **what did the TCM command, and what actually happened?**

| After the command | Area |
|---|---|
| Current tracks command, pressure/ratio responds | Output path fine: look at inputs, adapts, intermittents |
| Current tracks command, **no** pressure/ratio change | **Hydraulic or mechanical** |
| Current doesn't track, circuit DTC | **Electrical** (coil, harness, connector, driver) |
| No command sent | Enable conditions or inputs (TFT, OSS, TPS, brake switch, range) |

> **ASE trap (your risk):** "circuit tests good, so the solenoid is good." A **performance** DTC (ratio, slip, stuck on/off) with a good circuit = **hydraulic or mechanical**. A solenoid click only proves the coil moved.

- **TFT (NTC thermistor):** **open = reads very cold** (P0713, high signal voltage). **Short to ground = reads very hot** (P0712).
- **ISS/OSS:** Hall-effect: **no ohmmeter**; check reference, ground, and scope the square wave. Ratio = ISS ÷ OSS. A bad signal gives ratio DTCs on a healthy unit.
- **TR/MLP:** compare range PID with the physical lever. Bad = no-crank in Park, wrong display, default gear.
- **Voltage drop under load,** not ohms. **Several U-codes at once** = battery, power, ground or bus first.
- **OBD II:** MIL off after 3 clean trips; history erases after 40 warm-ups (OEMs often say 80 for misfire/fuel). **Permanent DTC: not cleared by scan tool or battery pull**; it clears when the monitor passes. **P0700** = go scan the TCM.
- **Adapts:** clearing is **not** a repair. **Relearn** after TCM, valve body or transmission replacement; load solenoid characterization data. Programming needs a **battery maintainer, not a charger**.

### A.8 Not the transmission [G 2.7, 3.10]
Misfire mimics TCC shudder. TPS reading closed = early soft shifts; open = late harsh. Wheel-speed/ABS failure = no upshift, dead speedometer, no TCC. Traction control feels like slip but the ratio stays correct. Mismatched tires bind AWD. Rough shifts right after a reflash = zeroed adapts. **The answer must explain every symptom in the stem.**

### A.9 Other types: recognize only [G 6]
**DCT:** no converter, no stall test, no TCC; odd/even shaft split is its "apply chart"; judder from a stop = launch clutch; dry clutch has **no fluid to change**. **CVT:** pulleys and belt/chain; never generic ATF; one-direction ratio fault = that direction's primary circuit; low clamp = belt slip. **Don't carry one type's logic into another.**

---

## 2. Area B: In-Vehicle Maintenance and Repair (27%, 12 questions)

Best yield on the test: one question per task. The pattern everywhere: **verify the cheap root cause before replacing the expensive part.**

| Shop shortcut | ASE wants |
|---|---|
| Replace the TR switch | Check cable/linkage and detent first, then index the switch |
| Replace the tailshaft seal | Check the **bushing** and yoke seal surface too |
| Flush milky fluid | Replace the cooler, rebuild (seals, frictions, converter), then flush |
| Replace the TCM with ATF in the connector | Fix the leaking case pass-through too |
| Add fluid because it slips | Check the level the SI way: overfull slips too |

**Fluid level, no dipstick [G 4.8]:** scan-tool fluid temperature **inside the SI window**, **vehicle level**, engine idling, shift through the ranges, open the check plug. **Drip = correct, stream = overfull, nothing = low.** Topped off cold = overfull hot (ATF expands). **Overfull:** foam, slip, heat, fluid out the vent. **Underfull:** pump pulls air, delayed engagement, whine, slip worse cold or in turns. **Pan drop** replaces only part of the fluid.

**Fluid condition [G 2.1]:** dark/burnt = overheated or burned frictions. **Milky pink = coolant from the radiator cooler** (cooling system pressure pushes it through a tiny leak). Even a little damages frictions.

**Pan debris [G 4.3]:** a little gray paste on the magnet = normal. Steel = magnetic (gears, bearings). **Brass and aluminum don't stick to the magnet**: a clean magnet doesn't mean no metal.

**Cooling [G 4.4]:** overheating with **normal shifting** = restricted cooler/lines or **TBV stuck in bypass** (works like a thermostat). After any failure, flush and **flow-test warm with the transmission's own pump**.

**Valve body [G 4.5]:** separator plates and gaskets are application-specific (compare hole for hole). Missing check balls = no shift or no move. Torque **center outward** with an inch-pound wrench. **A new problem right after valve body work = the job itself** (torque, check balls, gasket), not a new failure.

**Linkage and TR switch [G 4.1]:** **linkage → switch → module.** Cranks in N but not P = switch index or cable. Creep in neutral or delayed engagement = manual valve between detents.

**Leaks [G 4.2]:** clean, dye, find the **highest** wet point. Bellhousing = front seal (or engine rear main; identify the fluid). Rear = tailshaft seal **and** bushing/yoke.

**Electrical [G 4.6]:** ATF wicks up the harness from a failed pass-through. Fretting corrosion causes intermittents. Don't spread terminals with meter probes. **Mounts [G 4.7]:** clunk on engagement, vibration; settle the powertrain before torquing.

---

## 3. Area C: Removal, Inspection, Installation (15%, 7 questions)

Only ~0.3 questions per task. Learn the **order and the classic mistakes**; numbers are SI.

- **Converter install [G 5.1]:** turn it while pushing in until it drops through **stages** (input splines, stator splines, pump lugs). Free play to the flexplate before bolting. **Never pull the unit in with the bellhousing bolts.** Dowels present. **Front pump damage right after an R&I = installation first.** Flexplate cracks knock like an engine; don't impact the bolts. Cracked flexplate or case = **alignment** (reinstall the dowels).
- **After install [G 5.2]:** flush and flow-check the cooler, load calibration/characterization data, **relearn**, check level at SI temperature.
- **Clutch packs [G 5.4]:** soak new frictions. Lip seals face **toward the pressure**. Piston check ball stuck = burned clutch.
- **Air test** with low, clean, dry air: **thud = good, hiss = leak.**
- **One-way clutches can go in backward:** no drive in the range they carry, or a tie-up. Bench-check rotation.
- **Thrust washers:** petroleum jelly, **not white grease**. **End play:** dial indicator, correct with selective washers or snap rings. **Pump clearance:** straightedge and feeler gauge.
- **Bands:** a worn drum lets the band run out of travel: replace **both**.

---

## 4. Your Weak Spots (graded quizzes)

| Missed | Correct |
|---|---|
| Carrier vs. ring layout (twice) | Carrier **holds the planets**; ring is the big outer gear |
| "Sun gear = internal gear" | **False.** Ring = internal gear |
| Ravigneaux | 2 suns, 2 planet sets, 1 carrier, 1 ring |
| Total ratio | **Multiply** stages |
| Reaction clutch steel plates | Splined to the **case** |
| Disconnected member | **Neutral**, no torque flow |

---

## 5. Wrong-Direction Traps

Each is a place where a flashcard, website or shop slang has it backwards.

1. **TFT:** open = reads **cold**; short to ground = reads **hot**.
2. **Stall:** high = **transmission** slipping; low = engine or freewheeling stator.
3. **Stator:** freewheeling = poor launch; seized = poor top end + heat.
4. **Order:** fluid → line pressure → stall. Never stall-test with low line pressure.
5. **Codes:** clear with the scan tool; a battery pull doesn't clear a permanent DTC.
6. **Adapts:** reset is verification, not repair.
7. **EPC:** more current = **less** pressure; unplugged = **maximum** (classic design; read the stem).
8. **Flare vs. tie-up:** opposites. Flare rpm up; tie-up output braked.
9. **First-gear one-way clutch** can't cause slip in every forward gear.
10. **Milky ATF:** replace cooler + rebuild + flush. "Flush and refill" is the distractor.
11. **Pan drop** changes only part of the fluid.
12. **Ratios in series multiply.**
13. **Circuit good ≠ solenoid good** when the DTC is a performance code.
14. **Operating as designed** ends the diagnosis at strategy step 2: explain it, don't replace parts.
