## 0. Unit 2 Test Review (read first)

From your graded Unit 2 review (`notes/unit2.txt`). The stall-speed logic is the one thing to fix before the final.

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

## 1. Hydraulic Principles (Chapter 4)

**Instructor scope for Unit 2:** TCC and hydraulic principles, Chapters 4, 6, 10 and 15 (hydraulic system, torque converters, electronic controls, condition diagnosis). Built from your class notes and the textbook text you pasted. Outside additions are labeled.

### 1.1 What the hydraulic system does

- **Applies the clutches and bands**, which controls the transmission's power flow.
- Delivers enough force and motion to apply those units **completely**, so they don't slip.
- Keeps fluid flowing **through the torque converter** so it can work.
- Keeps fluid flowing to **lubricate and cool** the gear train.

### 1.2 Pascal's law and the pump
**Pascal's law:** pressure applied to a confined fluid is transmitted **equally and undiminished in every direction**. Liquids flow through complicated paths but **cannot be compressed**, so force and motion carry to every connected part.

**Pressure = force ÷ area** (psi = lb ÷ sq in). Example from the text: 10 lb on a 1 sq in piston makes 10 psi, and that 10 psi acts on **every** square inch it touches. A 5 sq in apply piston on the same 10 psi pushes with 50 lb (simple arithmetic: force = pressure × area). A bigger piston means more apply force at the same pressure.

> **Rule:** **The pump does not create pressure. Pressure comes from resistance to flow.** The pump creates flow. No resistance (a big leak) means low pressure.

Every automatic transmission has an **internal** pump, driven through the converter hub, so it turns whenever the engine runs. Three common types, all **positive displacement** and all working on the same principle, an expanding cavity that draws fluid in and a shrinking cavity that pushes it out:

| Pump | Note |
|---|---|
| **Internal–external gear (crescent / gear)** | Gears with a crescent-shaped seal between them |
| **Gerotor (rotor)** | Inner rotor turns inside an outer rotor that has one more lobe than the inner |
| **Vane** | Vanes slide in a rotor inside an offset housing |

**Positive displacement** means one revolution moves a **fixed volume**; a water pump (whirlpool/centrifugal flow) does not. Since it can't be deadheaded, it needs pressure **regulation and relief**.

**Variable-displacement pump.** Still positive displacement, but the **vane housing pivots on a hinge** to shrink or grow the pumping chambers, so the volume per revolution changes. It matches output to need instead of wasting engine power moving excess fluid.

### 1.3 Valves
Most transmission valves are **spool valves**: a shaped plunger (like a thread spool) that slides in a bore and opens or closes passages. Most are moved by fluid pressure and returned by a spring. The **manual valve** is the main exception: the driver moves it mechanically with the shifter.

| Category | Job |
|---|---|
| **Switch valve** (flow control valve) | Directs fluid into different circuits |
| **Servo valve** | Moves another valve (some move switch valves, some help control pressure regulators) |
| **Regulator valve** | Controls fluid pressure |

Pumps can build pressure far too high, too fast, so **every transmission has a pressure regulator (pressure control) valve**, usually a spool valve plus a spring.

### 1.4 Pressure signals
**TV (throttle valve) pressure** is pressure that relates to **throttle position**: more throttle, more TV pressure. Older units made it mechanically or with vacuum; electronic units get the same idea from the TCM reading the throttle or pedal sensor.

> **Wrong direction:** two common mix-ups. (1) "The pump makes pressure" is false; resistance does. (2) A bigger apply piston does not need more pressure; it makes **more force** at the same pressure.

---

## 2. Torque Converters (Chapter 6)

### 2.1 What it does and where it sits
The converter is bolted to the **flexplate**, so it spins at **engine speed**. Jobs:

1. Smoothly **transfer** engine torque to the transmission.
2. **Multiply torque** when the vehicle needs it (launch).
3. Turn the **pump** through the converter hub.
4. Provide a **direct mechanical link** to the transmission through the **TCC**.

**Failure can cause loss of drive or loss of power.**

### 2.2 The three parts
| Part | Does what | Connected to |
|---|---|---|
| **Impeller** (pump) | Driving member. Throws fluid at the turbine. Turns whenever the housing turns | **Engine** |
| **Turbine** | Driven by the fluid. Sits on the engine side of the converter. Like the disc in a manual clutch | Splined to the **transmission input shaft** |
| **Stator** (reactor) | Reaction member. Redirects returning fluid back into the impeller | Rides on a **one-way clutch** on the stator shaft |

> **Rule:** **Engine → impeller. Transmission → turbine.** Scan data: **engine rpm = impeller speed**. **Turbine speed = transmission input speed sensor**. (You mixed these once; use the table.)

### 2.3 Torque multiplication and coupling
| | **Stall / launch** | **Coupling** |
|---|---|---|
| Turbine speed | Low or zero | Close to impeller speed |
| Fluid hits stator | Front of the blades | **Back** of the blades |
| Stator one-way clutch | **Locks** the stator | **Overruns** (freewheels) |
| Flow pattern | **Vortex** flow (in a circle through the vanes) | **Rotary** flow (around the circumference) |
| Torque multiplication | **Yes** | **None**: turbine speed ≈ impeller speed |

**Fluid path:** impeller → turbine → **stator** → impeller. Fluid leaving the turbine must pass through the stator before it reaches the impeller.

At stall the locked stator turns the fluid so it **assists the impeller**, which multiplies torque. At coupling the stator must freewheel or it would block the flow. Coupling is the closest the speeds come **without** the TCC (a couple hundred rpm of slip).

- **Creep:** shifting from P/N into a drive range at idle sends a little torque to the input shaft, so the vehicle moves slightly with the brakes released. **Normal.**
- A **non-lockup converter** always has some slip; the turbine almost never matches engine speed.
- **Stall speed** is a manufacturer design value. Maximum stall = engine at full throttle, brakes holding, turbine stopped.

### 2.4 Stator one-way clutch failures (two opposite faults)
| | **Freewheels both ways** (never holds) | **Locked both ways** (never releases) |
|---|---|---|
| Launch | **Poor** (no multiplication, flow not redirected) | Normal / good |
| Highway | Normal / good | **Poor** (blocks flow at coupling) |
| Stall rpm | **Can't reach max stall** (low) | Not a useful indicator |
| Memory aid | Lose the **low end** | Lose the **high end** and run hot |

> **Rule:** **Nothing inside the converter makes stall speed HIGHER than spec.** A stall speed above spec means something in the **transmission** is slipping (clutch, band, one-way clutch).

> **Your Unit 2 test:** high stall, Tech A says stator, Tech B says slipping clutch: **B only**. Low stall, Tech A says stator, Tech B says engine: **both**. See Section 0.

### 2.5 Heat
**Most heat in an automatic transmission comes from the torque converter**, especially at **stall**. A stall test creates a lot of heat: limit how long and how many times (follow SI; a typical limit is about 5 seconds per test with a cool-down between). **Best way to cool the fluid: apply the parking brake and let the engine idle** in neutral/park.

---

## 3. Torque Converter Clutch (TCC)

### 3.1 What it is for
The TCC applies a **pressure plate** against the converter cover for a **mechanical link** from engine to input shaft, which makes the lockup **100% efficient**. Slip goes from about 200 rpm to **zero**. The pressure plate is splined to the turbine hub. A **spring-loaded damper** lets the plate turn independently of the damper hub (about 45°) so lockup is cushioned and engine and road torque pulses are absorbed. Without lockup, an **overdrive transmission runs hot** (constant slip makes heat).

### 3.2 TCC slip speed
**TCC slip speed = engine speed (impeller) − turbine speed (input speed sensor).**

- Open converter at cruise: some slip (coupling).
- TCC applied: slip → **near zero**.
- Commanded on but slip stays high → the **apply side** has failed, not the command.
- Slip near zero while stopped → TCC **stuck on** (will stall or nearly stall the engine at a stop).

### 3.3 Release and apply flow
| State | Fluid path (GM 6-speed-style text; passages vary by unit, check SI) |
|---|---|
| **Released** | Pump sends oil into the **release passage** (between the **stator shaft and turbine shaft**). It enters on the release side of the pressure plate and pushes the plate **away** from the cover. Turbine can turn at any speed |
| **Applied** | TCM signals the **TCC PC solenoid**; it regulates line oil into the **regulated apply passage** (between the **converter hub and stator shaft**). Apply oil goes into the converter on the **apply side** of the plate and clamps it to the cover. Release oil exits between the **turbine shaft and stator shaft** |

The TCC solenoid is **PWM controlled** (duty cycle sets apply pressure), which allows a smooth, ramped apply and release. Remember the sides: *release oil holds the plate off; apply oil clamps it.*

### 3.4 No TCC apply: possible causes (from the text)

- Electrical: damaged connector, harness or solenoid
- Torque converter internal damage
- TCC control valve and spring worn, damaged or sticking
- Turbine shaft O-ring or seal cut or damaged
- TCC regulator apply valve worn, damaged or sticking

---

## 4. Electronic Transmission Controls (Chapter 10)

Covered in Unit 1; the parts that matter most for Unit 2:

| Item | What to remember |
|---|---|
| **TCM inputs** | Input speed (ISS/TSS) and output speed (OSS/VSS), TFT sensor, throttle/pedal position, engine temp and load, brake switch, range/pressure switch signals |
| **TFT sensor** | NTC thermistor: resistance **drops** as fluid warms. Used for shift and TCC quality |
| **TCC PC solenoid** | PWM, normally low; controls TCC apply and release. Can ramp apply for smoothness |
| **EPC / line pressure solenoid** | EPC: normally closed, **more current = lower pressure**. GM line PC: normally high, ~0.1 A max pressure, ~1.0 A min. Opposite-sounding; read the stem |
| **Shift solenoids** | On/off; TCM picks the on/off combination for the commanded gear |
| **Brake switch** | A TCM input that can release the TCC |
| **Adaptive learning (TAP)** | TCM adjusts shift timing to keep shift time in range; reset after transmission replacement or clutch-to-clutch work |

> **Rule:** command is not pressure. The scan tool shows what the TCM **asked** for; only a gauge shows what the hydraulics **did**.

---

## 5. Condition Diagnosis (Chapter 15)

### 5.1 Fluid level
| Condition | Why it causes trouble | Symptoms |
|---|---|---|
| **Underfilled** | Air enters the **filter and pump intake**; pressure drops and is erratic | Mushy operation, may drop into neutral, slip, TCC fails to lock or unlock properly |
| **Overfilled** | Fluid level reaches the **spinning gear sets**, which whip it into foam (aeration) | Slip, mushy operation; foamy fluid may flow out the **vent or filler pipe** |

Clue from the GM training: slip or flare in **cornering when cold** that clears warm → **low level**. An overfull unit can slip from **aeration**. Also from that training: a **poorly running engine** can feel like a shift concern, and the **wrong fluid** can cause shift problems.

### 5.2 Fluid condition

- **"Milkshake" ATF = water (coolant) in the fluid.** It can come from **outside** into the transmission, but the common source is a **failed transmission cooler** in the radiator. (Outside note: coolant contamination damages the friction material, so the repair is the cooler plus a rebuild, not just a drain and fill.)
- **Burnt smell, dark fluid, burned clutches** → overheating.

### 5.3 Overheating
Causes: the torque converter (stall, no TCC lockup in overdrive), restricted cooling, worn parts that slip. **Symptoms to know:**

- **Fluid overflowing from the vent**
- **Purple (heat-stained) torque converter**
- **Burned clutches**

**Cooler flow** is checked by measuring **flow rate** through the cooler, not just seeing fluid come out.


### 5.4 Reading the scan data

- **Engine rpm** = impeller speed. **Input speed sensor** = turbine speed.
- **TCC slip = engine rpm − turbine rpm.** Near zero with TCC applied; a couple hundred at coupling.
- A **stall test** result below spec: stator freewheeling (or a weak engine, check that first). Above spec: transmission slipping.

---

### 5.5 Hydraulic pressure tests
A **pressure gauge** checks the health of the hydraulic system, and some problems can be fixed with the transmission still in the vehicle.

**Mainline (line) pressure test.** The test taps the pump's output, **mainline pressure**, which feeds the control valves and solenoids downstream. Think of it as watching what the circuits do to the pump's pressure:

- **All valves closed (park/neutral) and pressure is in spec:** the pump, filter and regulator are doing their job.
- **Shift into a range:** a valve opens and sends fluid to a clutch or servo. If everything downstream of that valve is leak-free, mainline pressure **stays in spec**.
- **A leak downstream of that valve:** opening it makes mainline pressure **drop out of spec** (Pascal's law: the system is one connected circuit, so a leak anywhere in the circuit lowers the pressure everywhere it's connected). The range where it fails tells you **which circuit** leaks.
- **Fails with all valves closed:** the problem is **upstream** of the control system, so the pump, intake filter or pressure regulator.

| Gauge | Notes |
|---|---|
| **Analog** | Normally **dampened**, so minor pressure fluctuations are lost |
| **Electronic (transducer)** | Connects to a **scope** so you can watch small pressure changes, an important clue to some problems |
| **Range** | Use **0 to 300 psi** so reverse pressure doesn't damage the gauge |

On transmissions where the TCM controls pump or pressure-solenoid duty cycle, you can **command the duty cycle and watch how pressure reacts**.

**Interpreting readings.** Compare to specifications. In **park and neutral**, the likely causes of a pressure problem are the **pump, intake filter and pressure regulator**, because the fluid path is through the filter, valve body, case, pump and back, and the manual valve shuts off flow to the rest of the transmission. High or low pressure in **neutral** is usually the **throttle valve, torque converter or cooler** circuits (those stay open to flow in P/N).

Textbook example pressures, **only if no specifications are available** (from your notes; use SI first):

| Range | Approximate pressure |
|---|---|
| Neutral, park, drive at idle | 50-60 psi (350-400 kPa) |
| M1 and M2 | 50-60 psi (some transmissions 100-125 psi) |
| Reverse | **150-250 psi** |

### 5.6 Cracked flywheel or case: alignment
A cracked flywheel (flexplate) or cracked transmission case points to an **engine-to-transmission alignment problem**. The **alignment dowels** usually stay in the **engine block**. If the old transmission comes out with the dowel pins in it, they must go back into the engine side. **Install the new transmission without them and you create an alignment problem.**

---

<div style="break-before:page"></div>

## 6. Line Pressure: High or Low

**Line pressure** (mainline) is what the pump and pressure regulator send to every circuit. Most pressure questions come down to one move: **ask whether the reading is wrong in every range or only one.** Use the mainline test from 5.5.

### 6.1 Low line pressure
| Pattern | Likely causes |
|---|---|
| **Low in every range** (something common to the whole supply) | • **Low fluid level** or **foamy, aerated fluid** (overfill)<br>• **clogged intake filter** or an air leak on the suction side (the pump draws air)<br>• **worn pump**, including a worn pump bushing or stator-support bore<br>• **weak or stuck-open pressure regulator**, or a worn regulator bore<br>• a **large common leak** (a seal or sealing ring that feeds every range)<br>• thin, degraded or wrong fluid (worse hot) |
| **Low in one range only** | A leak in the circuit fed **only in that range**: the clutch or servo **piston seal**, a **sealing ring** on the shaft, a servo seal, or that range's valve or passage |
| **Fails with all valves closed** (P/N) | **Upstream** of the control system: pump, intake filter, pressure regulator |
| **Fine until you select a range, then drops** | Leak in **that range's circuit** (Pascal's law: the circuit is connected to mainline) |

### 6.2 High line pressure
| Cause | Notes |
|---|---|
| **Stuck regulator valve** | Pressure can't be relieved, so it rises in every range |
| **Pressure solenoid (EPC) in failsafe** | Classic design: **no current = maximum pressure**, so an unplugged, open or stuck solenoid gives high pressure and harsh shifts. Command is not pressure: more current = lower pressure |
| **TV cable too tight** (older units) | Raises the TV signal: high pressure, firm and late shifts |
| **Vacuum modulator problem** (older units) | Lost vacuum or a disconnected hose = high pressure; a ruptured diaphragm also pulls fluid into the intake |
| **High or low in neutral** | Usually the **throttle valve, torque converter or cooler** circuits (those stay open to flow in P/N) |

### 6.3 Quick rules
- **Reverse reads higher by design.** Textbook examples: P/N/D idle 50-60 psi, **reverse 150-250 psi** (use SI first). Low in reverse only = reverse-circuit leak. Low everywhere = supply.
- **Low pressure + slip or mushy feel** points first to fluid level, filter, pump or regulator, then to the range-specific seal if only one range is affected.
- **Pump does not make pressure; resistance does.** A leak anywhere in a connected circuit lowers pressure.
- **If line pressure is low, do not stall test.**

---

## 7. Expanded Theory (from the ASE research)

Your notes set the topics; this section adds depth under them, mostly for Chapters 15, 6 and 4. It comes from the ASE A2 guide and its research pass, so it goes further than your class notes. Specs and examples vary by unit: **SI decides**.

### 7.1 Shift-quality vocabulary (Ch 15)
Every shift is a **handoff**: the off-going element releases while the on-coming one applies. The terms describe what rpm does.

| Term | What it is | Rpm / feel |
|---|---|---|
| **Slip** | Friction element not holding; can occur while cruising | Rpm up, no matching speed gain |
| **Flare** | Off-going releases **before** the on-coming holds (underlap, low apply pressure) | Rpm rises briefly during the shift |
| **Tie-up (bind-up)** | Two ratios applied at once (overlap), or an element fails to release | Output feels braked; rpm pulled **down** |
| **Harsh / bump** | Apply pressure rises too fast | Firm, abrupt shift |
| **Slide-bump** | Accumulator bottoms out before the shift ends, so pressure spikes | Smooth start, harsh finish |
| **Delayed engagement** | Lag from P/N into D or R | Low fluid or pump pressure, worn seals, clogged filter; worse cold |

> **Rule:** flare is the **opposite** of tie-up. Released too soon = flare. Applied too soon or released late = tie-up. A faulty accumulator gives harsh shifts for the shift it belongs to (hard N-D points to the N-D accumulator).

**Noise:** does it follow engine rpm or road speed? A whine in P/N that rises with rpm is usually the **pump** (or a clogged filter, or air at the pickup). Vibration in P/N at a fixed rpm points to the flexplate or converter.

### 7.2 Valves in diagnosis (Ch 4)
| Valve / part | Fault picture |
|---|---|
| **Pressure regulator** | Worn bore: low or erratic line pressure, soft shifts, worse hot |
| **Manual valve** | Misadjusted linkage: creep in neutral, delayed engagement |
| **Shift valve** | Stuck valve acts like a solenoid stuck on or off. A good solenoid circuit test with a wrong-gear symptom points to the **valve** |
| **Accumulator** | Broken spring or bad seal: harsh shift in that circuit |
| **Orifice and check ball** | Missing ball or enlarged orifice: harsh, fast apply; plugged orifice: slow or delayed |

**Sticking vs. wear:** debris and varnish cause **intermittent, cold-worse** wrong-gear, no-shift or TCC problems. Bore wear is **progressive and worse hot** and can set several pressure-control codes at once.

### 7.3 Converter and TCC diagnosis (Ch 6)

- **Stall test:** high stall = transmission slipping; low stall = weak engine **or** freewheeling stator. Rule out the engine first. A TCC stuck on can stall the engine in gear, so don't stall-test that complaint.
- **TCC does not apply** when an input prevents it: brake switch reading "applied," a throttle dead spot, a cold-reading temperature sensor, no speed signal. Check inputs and TCC enable data before condemning the solenoid or converter.
- **Commanded on, slip stays high** = the **apply side** failed. Many "bad converter" cases are leaks **before** the piston: worn TCC regulator or apply valve bores, a worn stator-support bushing, or a damaged turbine-shaft seal. Low pressure while commanded = supply or leak; normal pressure and high slip = the lining.
- **Slip near zero at a stop** = TCC stuck on (engine stalls or nearly stalls).
- **Shudder vs. misfire:** true TCC shudder goes away with the TCC **off** and also fully **locked**. A misfire follows firing frequency, shows in misfire data, and is often worse when locked. **Fluid condition** is the first suspect for shudder.
- **Bench check:** the stator should turn one way and lock the other. Free both ways or locked both ways: replace the converter.

### 7.4 Cooling and overheating (Ch 15)

- Overheating with **normal shifting** points to a restricted cooler or lines, or a **thermal bypass valve (TBV)** stuck in bypass. The TBV works like a thermostat: stuck in bypass starves the cooler and overheats the transmission.
- **Milky ATF:** replace the radiator cooler **and** the damaged parts (seals, frictions, converter), clean and flush. "Drain and refill" or "flush only" is the wrong answer.
- After a failure, flush the cooler and lines and **flow-test warm using the transmission's own pump**.

---

## 8. One-Page Cram

- **Hydraulics:** Pascal's law, pressure = force ÷ area, equal in all directions. **Pump makes flow; resistance makes pressure.** Positive displacement pumps: gear/crescent, gerotor, vane. **Variable displacement = vane housing pivots.**
- **Valves:** switch (routes), servo (moves a valve), regulator (pressure). Spool valves. **Manual valve = mechanical.** Every unit has a pressure regulator.
- **TV pressure** = throttle position.
- **Converter:** **impeller = engine**, **turbine = input shaft**, **stator = reaction, on a one-way clutch.** Engine rpm = impeller. Input speed sensor = turbine.
- **Stall:** stator locked, vortex flow, torque multiplied. **Coupling:** stator freewheels, rotary flow, no multiplication.
- **Stator freewheels (never holds):** poor launch, good highway, low stall. **Stator locked:** good launch, poor highway, heat.
- **Stall HIGH = transmission only. Stall LOW = engine OR stator.** (Your Unit 2 misses: high → Tech B only; low → both.) Nothing in the converter raises stall.
- **Fluid path:** impeller → turbine → stator → impeller. **Positive displacement** = fixed volume per rev; needs regulation and relief. **More line pressure** = firmer shifts, more holding power.
- **Most heat comes from the converter**, worst at stall. Cool by parking brake + idle.
- **TCC slip = engine − turbine.** TCC applied → near zero. Released by release passage (stator shaft/turbine shaft); applied by apply passage (hub/stator shaft). **PWM** solenoid. No lockup in overdrive → overheats.
- **Fluid:** underfilled → air in the pump, mushy, neutral, slip, TCC problems. Overfilled → foam, slip, fluid out the vent. Milkshake = coolant (failed cooler). Overheating = overflowing vent, purple converter, burned clutches.
- **Command is not pressure.** Scan tool = request; gauge = result.
- **Low in all ranges:** fluid level, filter/air, pump, regulator. **Low in one range:** that circuit's seal. **High:** stuck regulator, pressure solenoid failsafe (no current = max), TV cable tight or modulator vacuum lost.
- **Mainline pressure test:** taps pump output. Valves closed and fails = upstream (pump, filter, regulator). Fine until a range is selected, then drops = leak in **that** circuit. Use a **0-300 psi** gauge. Textbook examples: P/N/D idle 50-60, reverse 150-250.
- **Cracked flexplate/case = alignment.** Dowel pins stay in the engine; reinstall them with a new transmission.

*Source note: class notes (hydralics, torque-converters, ch15) and the GM technician transmission guide excerpt pasted in `notes/torque-converters.txt`. Section 7 comes from the ASE A2 guide and research pass (partly verified; see its CONTEXT/verification notes). Items marked "outside" or "typical" are general knowledge, not from the notes. Not ASE content.*
