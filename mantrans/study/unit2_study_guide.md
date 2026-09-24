# Unit 2 Study Guide — Manual Transmission & Transaxle Internals
*(GM ASEP A3, Unit 2 — everything up to the Unit 2 quiz. Clutch = Unit 1, done. Diffs/axles = Unit 3, not yet covered.)*

---

## Page 1 — Gear Theory & Power Flow

### The transmission's job
Think of the transmission as a **selective torque multiplier**: low gears = more torque, less speed (harder to turn engine, easier to move car); high/overdrive gears = less torque, more speed. Every ratio is a trade between the two — you never get both for free.

### Gear ratio basics
- **Reduction** — output turns slower than input, torque increases (numerically higher ratio, e.g. 3.5:1).
- **Direct drive** — 1:1, input shaft speed = output shaft speed, no multiplication.
- **Overdrive** — output turns faster than input, torque decreases below engine output (ratio less than 1:1, e.g. 0.8:1).
- Know **which ratios increase torque** (numerically higher, reduction) vs **which increase speed** (numerically lower, overdrive).
- Ratio math: gear ratio = driven teeth ÷ drive teeth. A **10:7:20** three-gear train still reduces to **2:1** end-to-end — the idler's own tooth count doesn't change the overall ratio.
- **Idler gear**: reverses rotational direction only. If it's a *different size* than the drive/driven gears, it still does **not** change the ratio — only direction.

### Constant-mesh principle
In a constant-mesh transmission, gear pairs are **always meshed**; nothing physically slides into tooth-to-tooth mesh during a shift. What changes is which gear gets **locked to its shaft** by a synchronizer sleeve.

Rule to remember: **it is never a fixed gear meshed to a fixed gear.** It's always fixed gear ↔ speed gear (a gear that freewheels on the shaft until the synchronizer locks it). If a gear has a synchronizer sleeve near it in a diagram, that's your speed gear.

Only **one gearset is engaged at a time** — one sleeve locked to one speed gear per shift.

### Gear type note
**Helical gears** are the common type — quiet running, but they generate **endthrust** (axial load), which is why the shafts need thrust surfaces/washers to control that end-loading.

### Lubrication
Most manual transmissions are **splash lubricated** — the countershaft dips into the oil, spins, and throws oil up onto the mainshaft and other components. No oil pump in a typical setup.

*(Side note, not core ASE material: this is why towing a manual-trans RWD vehicle with all 4 wheels down can be a problem — output shaft spins, input shaft doesn't, so a speed gear's synchronizer sleeve spins metal-on-metal without splash lubrication reaching it properly. On a 4x4, putting the transfer case in neutral disconnects this.)*

---

## Page 2 — Synchronizer Assembly & Shift Mechanism

### Synchronizer assembly — the core Unit 2 topic
**Complete assembly** = hub + sleeve + blocker/synchronizer ring(s) + keys/struts + springs. (The speed gear and shift fork are associated with it but are *not* part of the synchronizer assembly itself.)

| Part | What it does |
|---|---|
| **Hub** | Splined solid to the shaft — never moves independently of the shaft. |
| **Sleeve** | Slides axially on the hub's external splines; the shift fork moves it. |
| **Speed gear** | Freewheels on the shaft until locked; has a **cone** (friction surface) and **dog/clutch teeth** on its side. |
| **Blocker/synchronizer ring** | Friction ring with limited rotational play on the hub. Contacts the gear's cone, and while a speed difference exists, friction twists the ring just enough to **misalign its teeth from the sleeve's** — physically blocking premature engagement. This is why it's called a *blocker* ring. |
| **Keys/struts + springs** | Spring-loaded, seated in slots under the sleeve. As the fork starts moving the sleeve, the keys transfer that motion to the blocker ring *first*, so the ring contacts the gear cone before the sleeve can reach the gear's dog teeth. |

**Correct sequence** (this is the part worth memorizing precisely — a common way to get it wrong):

Fork moves sleeve → keys push blocker ring toward gear cone → friction speeds up or slows down the freewheeling speed gear to match hub/shaft speed → while speed differs, the ring's teeth stay misaligned (blocked) → once speeds match, the twisting force disappears and the ring re-centers → sleeve passes over the ring's teeth and engages the **gear's dog/clutch teeth** (NOT the cone — the cone is only ever a friction surface, the sleeve never "engages" it).

**Important reframe:** the synchronizer isn't "synchronizing the sleeve to the gear." The sleeve/hub are already at shaft speed. It's using friction to bring the *freewheeling gear* up/down to hub speed. That's a distinction a test question can exploit.

**Material note:** paper-coated steel blocker rings wear fast if the wrong fluid is used — reinforces why manual-trans fluid type is a real ASE topic, not "gear oil is gear oil."

### Shift mechanism
- Purpose: transfers driver's shift-lever motion to the shift forks.
- As the lever moves, it moves one (or, on some interlocked designs, prevents a second) synchronizer sleeve to engage the correct gear.
- **Fork-to-sleeve groove clearance matters.** If the fork or the sleeve's groove wears on the leading edge, the fork can't push the sleeve far enough to fully seat the dog teeth — a partially engaged gear can then pop back out (the dog teeth are shaped like arrows/angled, so partial engagement doesn't hold under load).
- Shift shafts are typically named by the gear pairs they control: **1–2 shift shaft, 3–4 shift shaft, 5–R shift shaft.** Older designs may use external linkage instead of internal shift rails.

### Detents and interlocks
- **Detent**: a spring-loaded ball (or similar) that holds a shift rail/fork in its selected position. Detents can be overcome by force — they hold the gear in place, they don't lock it rigidly.
- **Interlock**: mechanically prevents **two gears from being selected at the same time** (a pin-and-ball design is common). This is a safety/mechanical-integrity feature, not a shift-feel feature.
- **Reverse lockout**: a mechanism specifically preventing accidental reverse engagement.

---

## Page 3 — Symptom Diagnosis & Transaxle-Specific Concepts

### The three classic gear/shift symptom categories

**1. Grinding / gear clash**
- The sleeve is grinding against dog teeth because they can't engage cleanly — classic cause is a **worn synchronizer blocker ring** (can't build enough friction to match speeds in time).
- **One gear grinds** → suspect that gear's synchronizer/blocker ring specifically.
- **Every gear grinds** → suspect **clutch drag** (input shaft never actually stops/slows) before condemning every synchronizer at once.
- Grinding damage shows up on the **dog teeth**, not the gear-tooth flanks.

**2. "Block out" (won't go into gear at all / shifter won't move)**
- If it shifts perfectly with the engine off, but not with it running, the transmission itself is fine — the problem is that the **input shaft is still rotating when it shouldn't be** (classic clutch drag / speed mismatch). Ask: *while sitting still, is my synchronizer assembly still rotating, or truly stopped?*
- This is a clutch/release-system diagnosis wearing a "transmission" costume — don't open the transmission first.

**3. Pops out of gear**
- Root causes to check, in rough order of what the teacher emphasized:
  - **Fork-to-sleeve groove clearance** — worn fork/groove means the sleeve doesn't get pushed far enough onto the gear's dog teeth, so it doesn't fully seat and pops back out under load. *(This was called out as the answer the instructor specifically wanted — know it.)*
  - **Shaft endplay** — if shaft bearings are worn, the shaft can move axially. Since the fork and sleeve position are fixed relative to the shift rail, excess shaft endplay can pull a properly-engaged gear back out of mesh.
  - Worn dog teeth (not enough remaining engagement length to stay connected).
  - Detent wear/weak detent spring.
  - Shift linkage wear/misadjustment (external-linkage designs).

### Noise diagnosis — the road-speed test
The key diagnostic move: **hold a constant road speed and shift through the gears**, listening to how the noise changes.

- If a noise's **pitch tracks road/output speed** regardless of which gear you're in (same pitch in 3rd, 4th, 5th at the same road speed) → the noisy component is turning at **output-shaft speed** → suspect the **output shaft/output bearing**, not a specific gearset.
- If the noise's pitch is **different in each gear** at the same road speed (e.g., higher-pitched in 3rd than in 4th/5th) → the noisy component's speed is changing with gear ratio → suspect a **specific gearset** (the gear pair engaged in that range), not the output bearing.
- Bearing noise vs. gear noise both follow this same logic — figure out *what's rotating and at what speed* when the noise happens (this is the same master diagnostic question used across all of A3, not just Unit 2).
- A noise that behaves like a **clutch symptom** (present with the clutch engaged, changes with clutch pedal position) points back to input-shaft-area bearings, not internal gearset bearings — don't assume every "transmission noise" is inside the transmission.

### Transaxle-specific concepts
- In a transaxle, the **input shaft is also called the clutch shaft**, and it's not a separate piece from the mainshaft — it *is* part of the mainshaft assembly. What would be a separate countershaft in a longitudinal transmission effectively becomes the transaxle's output path here.
- **No pilot bearing needed** in a transaxle: because the input shaft is integral to the mainshaft assembly (not a separate free-floating shaft reaching into the engine), the whole assembly is fully supported by its own bearings. Compare: in a longitudinal (non-transaxle) transmission, the input shaft *is* separate from the mainshaft and needs a **third bearing** (the pilot bearing, supported at the crankshaft/flywheel) to support that free end.
- Because A3 treats the whole drivetrain as one system, a transaxle's **final-drive output should be treated the same way you'd treat a differential's output** — same diagnostic logic carries over into Unit 3.
- **Torque steer**: the car pulls to one side under hard acceleration.
  - **Most common cause: unequal CV joint operating angles** between the two half-shafts.
  - Contributing factors: unequal half-shaft lengths, and the tendency of a longer shaft to twist more under load than a shorter one.
  - Mental model: a wobble socket on an extension still transmits torque at an angle, but loses efficiency as the angle increases — past some angle, it "whips" and stops transmitting effectively. Equal angles on both sides = no torque steer, even if the mounts/geometry aren't perfect, because the losses cancel out symmetrically.
  - Conceptual cousin: **bump steer** in suspension/steering — same idea (geometry change causing an unwanted directional effect) applied to a different system.
- Corvette dual-clutch trivia (low-yield, know conceptually only): 2 mainshafts + 1 countershaft, 2 input shafts (one visibly larger, sticking out), no separate clutch pedal but still mechanically a manual — interesting design, not core ASE material.
