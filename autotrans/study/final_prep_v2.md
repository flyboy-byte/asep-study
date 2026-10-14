## 1. How to Use This (read first)

Built for the **class final on 2026-10-14**, assuming it covers **Unit 1 and Unit 2** (instructor scope: your class notes, not the ASE task list). It is a compression of the Unit 1 guide, the Unit 2 guide and your own quiz misses. Version 2 adds your **Unit 2 test review**: the stall-speed misses are now Tier A, Section 2.

**Weighting.** Time goes where the points are likely and where you have already missed:

| Tier | What | Why it's weighted this way |
|---|---|---|
| **A: lock in** | **Stall speed high vs. low**; planetary parts and rules; reaction clutch; converter; line pressure high/low | You missed both stall questions on the Unit 2 test and planetary items on the Unit 1 quiz |
| **B: know cold** | TCC apply/release; pressure test logic; fluid level and condition; sensors and solenoids | Straight recall from your notes |
| **C: recognize** | 10-speed chart pattern; gear set families; shift types; accumulators | The instructor said recognize, don't memorize |

---

## 2. Tier A: Stall Speed (your Unit 2 misses)

### Missed twice: stall speed, in opposite directions
| Question | You chose | Correct | Why |
|---|---|---|---|
| Stall **higher** than spec. A: stator one-way clutch. B: slipping clutch in the transmission | Both | **B only** | Nothing in the converter can raise stall. Higher stall means the turbine is being allowed to turn, so a **transmission** holding element is slipping |
| Stall **lower** than spec. A: stator one-way clutch. B: engine performance problem | Neither | **Both** | Low stall means the engine can't pull the rpm up: a **weak engine**, or a **stator that won't hold** (no torque multiplication) |

> **Rule:** **HIGH stall = transmission only. LOW stall = engine OR stator.** The converter can only ever make stall **low**, never high. Read every stall stem with this one line.

**Picture it (your Malibu note):** a healthy Malibu stood on hard enough chirps the tires off the line. Run the same car badly and stand on it, and it won't chirp: the engine can't pull the converter up to its normal stall rpm. **Weak engine = low stall.**

### Got right, worth keeping
- **More mainline pressure** gives **firmer shifts, better shift feel and more holding power** ("all of the above"). Apply force = pressure × piston area, so more pressure clamps the clutch harder. Too much is harsh.
- **Positive displacement** = **a fixed volume per revolution**. A water pump is not: it moves fluid by whirlpool (centrifugal) action. Because a positive-displacement pump **can't be deadheaded** without breaking something, it needs **pressure regulation and relief**. A vane pump can be **variable** positive displacement.
- **Converter fluid path:** impeller → turbine → **stator** → back to the impeller. Fluid leaving the turbine **must pass through the stator** before it reaches the impeller. The stator turns that fluid so it pushes the impeller **the way the crankshaft turns**.

---

## 3. Tier A: Planetary Gears (your Unit 1 misses)

### 3.1 The four names
| Part | Memory hook |
|---|---|
| **Sun** | Small gear in the **center**. External teeth |
| **Planets / pinions** | Orbit the sun, mesh with sun **and** ring |
| **Carrier** | **Holds the planets.** It is not the big outer gear |
| **Ring (annulus, internal gear)** | **Big outer gear, teeth on the inside** |

> **Wrong direction:** "Sun gear is also called the internal gear" is **false**. Internal gear = **ring**. Carrier ≠ ring.

### 3.2 The rules
| Result | Condition |
|---|---|
| **Neutral** | No driving member or no reaction (held) member: nothing connects input to output |
| **Direct drive 1:1** | **Any two members driven together** |
| **Reduction (forward)** | **Carrier is the output** |
| **Overdrive (forward)** | **Carrier is the input** |
| **Reverse** | **Carrier is held**, always reversed |
| Sun input → reduction | Sun output → overdrive |

One member **driven**, one **held**, one **output**. Extra pinions add strength, not ratio. Planetary ratios from sun/ring: 30-tooth sun, 70-tooth ring, ring held and sun driven = (30+70)/30 = **3.33:1**.

### 3.3 Gear sets
- **Simpson:** one sun, two carriers, two rings (4–5 speed).
- **Ravigneaux:** **two suns, two planet sets, one carrier, one ring.**
- **LePelletier:** a **simple planetary + a Ravigneaux** (6–8 speed; 6L80E).
- **Total ratio of stages in series: multiply, don't add.** A big number is not a reason to reject it. (2:1 then 3:1 = 6:1.)

### 3.4 Clutches and holding devices
- **Reaction (holding) multi-disc clutch:** the unlined **steel plates are splined to the transmission case**. Not a drum, not a carrier.
- **Band** wraps a drum; a **servo** applies it.
- **One-way clutches:** roller, sprag (hourglass), mechanical diode (strongest, like a ratchet). Holds one way, freewheels the other.
- **Synchronous** shifts (clutch-to-clutch): timed, **no one-way clutch**; mistimed = harsh/tie-up or flare. **Nonsynchronous:** one-way clutch self-releases.
- **Garage shift:** at rest, static friction. **Power shift:** under load, dynamic friction.

---

## 4. Tier A: Torque Converter (Unit 2)

| Part | Connected to | Rule |
|---|---|---|
| **Impeller** (pump) | **Engine** | Engine rpm = impeller speed |
| **Turbine** | **Input shaft** | Input speed sensor = turbine speed |
| **Stator** | One-way clutch (reaction) | Redirects fluid back to the impeller |

| | **Stall / launch** | **Coupling** |
|---|---|---|
| Stator | **Locked** by the one-way clutch | **Freewheels** |
| Flow | Vortex | Rotary |
| Multiplication | **Yes** | **None** |

- **Stator freewheels both ways:** poor launch, good highway, **low stall**.
- **Stator locked both ways:** good launch, poor highway, overheating.
- **High stall = transmission only. Low stall = engine OR stator** (Section 2). Nothing inside the converter raises stall.
- **Fluid path:** impeller → turbine → **stator** → impeller.
- **Most transmission heat comes from the converter**, especially at stall. Limit stall tests. Cool it with the parking brake and idle.
- **Creep** with brakes released is normal. A non-lockup converter always slips.

### TCC
- **TCC slip = engine rpm − turbine rpm.** Applied: ~200 → **0**. PWM solenoid. Damper springs cushion the apply.
- **Release oil** (stator shaft/turbine shaft passage) pushes the plate **off**. **Apply oil** (converter hub/stator shaft passage) **clamps** it.
- **No TCC apply:** electrical (connector, harness, solenoid), internal converter damage, TCC control or regulator valve worn or sticking, cut turbine-shaft O-ring.
- **Overdrive transmission that won't lock the converter overheats.**

---

## 5. Tier A/B: Hydraulics and Pressure

- **Pascal's law:** equal everywhere; **pressure = force ÷ area** (10 lb on 1 sq in = 10 psi; 4 sq in at 10 psi = 40 lb).
- **Positive displacement** = fixed volume per revolution (a water pump is not); can't be deadheaded, so it needs regulation and relief. **More line pressure** = firmer shifts, better feel, more holding power.
- **Pump creates flow. Resistance creates pressure.** Internal pump, always. Gear/crescent, gerotor, vane. **Variable displacement: vane housing pivots.**
- **Valves:** switch (routes), servo (moves a valve), regulator (pressure). **Spool valves.** Manual valve = mechanical. Every unit has a pressure regulator.
- **TV pressure** = throttle position.

### Line pressure: high or low
| Reading | Cause |
|---|---|
| **Low in every range** | Low fluid, foamy/aerated fluid, clogged filter or suction air leak, worn pump, weak regulator, big common leak |
| **Low in one range** | Leak in **that** circuit: piston seal, sealing ring, servo seal |
| **Fails with all valves closed (P/N)** | **Upstream:** pump, filter, regulator |
| **OK until a range is selected, then drops** | That range's circuit leaks |
| **High** | Stuck regulator; EPC/pressure solenoid failsafe (**no current = max** on classic design); TV cable too tight; modulator vacuum lost |
| **High/low in neutral** | Throttle valve, converter or cooler circuits |

- **Reverse reads higher by design** (textbook example 150–250 psi; P/N/D idle 50–60).
- Mainline test gauge: **0–300 psi**. Electronic gauge on a scope shows small changes. If line pressure is low, **don't stall test**.

---

## 6. Tier B: Fluid, Heat and Diagnosis (Ch 15)

| Condition | Result |
|---|---|
| **Underfilled** | Air at the filter and pump intake: mushy, may go to neutral, slip, TCC won't lock or unlock right |
| **Overfilled** | Fluid reaches the spinning gear sets and **foams**: slip, mushy, fluid out the **vent or filler pipe** |
| **Milkshake fluid** | Water/coolant, usually a **failed transmission cooler** in the radiator |
| **Overheating signs** | Fluid out the vent, **purple converter**, burned clutches |

- **Cold slip or flare while cornering, fine warm** → **low fluid level**.
- A poorly running **engine** can feel like a shift problem. **Wrong fluid** causes shift problems.
- **Cooler flow** is measured as **flow rate**.
- **Cracked flexplate or case** = **alignment**. Alignment dowels stay in the engine; reinstall them if they come out with the old transmission.
- Shift terms: **flare** = rpm rises (released early); **tie-up** = rpm pulled down (overlap); **slide-bump** = accumulator bottoms out (smooth start, harsh finish). **Accumulator** smooths pressure rise and doesn't store backup pressure.

---

## 7. Tier B: Electronics

| Item | Remember |
|---|---|
| **ISS = TSS** | Input/turbine speed. Also gives TCC slip |
| **OSS = VS** | Output/vehicle speed |
| Both | **Hall-effect**, can use a clutch drum as reluctor, share **8.3-9.3 V** from the TCM |
| **TR / MLP switch** | Tells the TCM the selected range |
| **Pressure switches** | On/off; read as a **pattern** to confirm the gear |
| **TFT sensor** | NTC thermistor: resistance **drops** as fluid warms |
| **EPC / PCS** | Normally closed, PWM, **more current = lower pressure** |
| **GM line PC** | Normally high: ~0.1 A max pressure, ~1.0 A min |
| **TCC PC solenoid** | PWM; controls and ramps TCC apply |
| **Shift solenoids** | On/off combination picks the gear |
| **Adapts (TAP)** | Reset after transmission replacement or clutch-to-clutch work |

> **Rule:** the scan tool shows the **command**, not the pressure. Only a gauge shows actual pressure.

---

## 8. Tier C: Recognition

- **10-speed pattern:** high reduction (1st ~4.70:1) → direct at **7th (1.000:1)** → overdrive through 10th (~0.64:1). One-way clutch holds 1st–2nd, overruns 3rd–7th, unused 8th–10th. **Neutral has three clutches applied but no output path.**
- 8/9/10-speed sets combine more than one compound set; check SI for the real design.
- Governor pressure (road speed) opposes throttle valve pressure; the TCM replaced that logic.

---

## 9. Before the Test

- Say aloud: **HIGH stall = transmission only; LOW stall = engine or stator.** Then: **engine → impeller, transmission → turbine; carrier holds planets; ring = internal gear; two members driven = direct; carrier held = reverse.**
- Redo the tier A tables from memory, then check this sheet.
- Stop early. You know hydraulics and diagnosis from the shop; the points you lose are the **naming and direction** ones.

*Source: class notes, `unit1_study_guide.md`, `unit2_study_guide.md`, and your Unit 1 quiz misses. Not ASE content.*
