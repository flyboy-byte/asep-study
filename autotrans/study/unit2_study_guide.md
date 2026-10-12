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

## 6. One-Page Cram

- **Hydraulics:** Pascal's law, pressure = force ÷ area, equal in all directions. **Pump makes flow; resistance makes pressure.** Positive displacement pumps: gear/crescent, gerotor, vane. **Variable displacement = vane housing pivots.**
- **Valves:** switch (routes), servo (moves a valve), regulator (pressure). Spool valves. **Manual valve = mechanical.** Every unit has a pressure regulator.
- **TV pressure** = throttle position.
- **Converter:** **impeller = engine**, **turbine = input shaft**, **stator = reaction, on a one-way clutch.** Engine rpm = impeller. Input speed sensor = turbine.
- **Stall:** stator locked, vortex flow, torque multiplied. **Coupling:** stator freewheels, rotary flow, no multiplication.
- **Stator freewheels (never holds):** poor launch, good highway, low stall. **Stator locked:** good launch, poor highway, heat.
- **Stall too HIGH = transmission slipping.** Nothing in the converter raises stall.
- **Most heat comes from the converter**, worst at stall. Cool by parking brake + idle.
- **TCC slip = engine − turbine.** TCC applied → near zero. Released by release passage (stator shaft/turbine shaft); applied by apply passage (hub/stator shaft). **PWM** solenoid. No lockup in overdrive → overheats.
- **Fluid:** underfilled → air in the pump, mushy, neutral, slip, TCC problems. Overfilled → foam, slip, fluid out the vent. Milkshake = coolant (failed cooler). Overheating = overflowing vent, purple converter, burned clutches.
- **Command is not pressure.** Scan tool = request; gauge = result.

*Source note: class notes (hydralics, torque-converters, ch15) and the GM technician transmission guide excerpt pasted in `notes/torque-converters.txt`. Items marked "outside" or "typical" are general knowledge, not from the notes. Not ASE content.*
