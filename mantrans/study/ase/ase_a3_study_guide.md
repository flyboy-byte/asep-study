# ASE A3 Manual Drive Train and Axles Study Guide

**Version 3 · Working draft — revised September 22, 2026**  
**Post-final ASE refresh — adds transfer-case fork logic, planetary gearset rules, U-joint order-of-vibration/working-angle detail, and ring&pinion contact-pattern adjustment, based on missed final-exam topics**

This guide is for the **professional ASE A3 exam**. It combines the official 2026 task list with the current GM ASEP notes, the existing Unit 2 guide, the deep-research blueprint, and the sourced research foundation. Class examples help explain mechanisms, but ASE questions are manufacturer-independent unless the question identifies an application.

## Source boundary

- Governing blueprint: [`ASE_Automobile_Study_Guide_2026.pdf`](../../sources/ase/ASE_Automobile_Study_Guide_2026.pdf), A3 printed pages 16–20.
- Classroom foundation: [`clutchsection.txt`](../../notes/clutchsection.txt), [`gears.txt`](../../notes/gears.txt), [`drive-axles.txt`](../../notes/drive-axles.txt), and [`transfercases-ujoints.txt`](../../notes/transfercases-ujoints.txt).
- Broader explanations and research blueprint: [`deep-research-report (3).md`](../../sources/deep-research-report%20%283%29.md).
- Qualifications, worked measurements, official-source audit, and application boundaries: [`a3_research_foundation_2026-09-13.md`](../../a3_research_foundation_2026-09-13.md).

## Exam map

The 2026 guide lists **50 total questions, 40 scored, 60 minutes**. Ten questions are unscored research items, but they are not identified during the test, so treat every question as scored.

| Official category | Scored questions | Published share |
|---|---:|---:|
| A. Clutch diagnosis and repair | 6 | 16% |
| B. Transmission diagnosis and repair | 7 | 17% |
| C. Transaxle diagnosis and repair | 7 | 17% |
| D. Drive/half-shafts and U/CV joints | 5 | 13% |
| E. Drive axle diagnosis and repair | 7 | 17% |
| F. 4WD/AWD diagnosis and repair | 8 | 20% |
| **Total** | **40** | **100%** |

The percentages are ASE's published figures. Use them to make sure every category is covered, not as a rigid minute-by-minute study formula.

## Priority for this folder

1. **4WD/AWD:** largest individual category and thinnest area in the current class notes.
2. **Transmission + transaxle:** 34% combined. Classroom coverage is strong, but ASE transfers the same mechanisms to unfamiliar layouts and includes measurements, coolers, controls, and the transaxle differential.
3. **Drive axle:** currently fresh and detailed. Preserve the new locker and bearing-localization material, then add setup measurements, shafts/retainers, vents, and design-specific controls.
4. **Drive/half-shafts:** a smaller category, but phasing, working angle, balance, runout, CV symptoms, and wheel bearings are easy points if kept separate.
5. **Clutch:** mechanisms are already familiar; review measurement, contamination/alignment, hydraulics, and design qualifications.

For Logan, this is a seventh ASE and electrical fundamentals are already established. The useful electrical review here is the drivetrain application chain:

**Request/input → module decision → output command → usable voltage/current at the load → actuator movement → position/engagement feedback → calibration or initialization**

## ASE question method

Before choosing a component, identify:

1. **Operating state:** stopped, accelerating, coasting, turning, one gear, every gear, 2HI/AUTO/4HI/4LO, front axle engaged or disengaged.
2. **Torque path:** which parts carry the selected torque?
3. **Rotation:** which parts rotate even if they are not carrying the selected torque?
4. **Load change:** engine speed, road speed, torque direction, cornering load, or engagement state.
5. **Best next check:** prefer the check that separates the remaining causes.

Words matter:

- **Could cause:** one valid mechanism is enough.
- **Most likely:** compare frequency and the exact conditions supplied.
- **First:** choose the safest, simplest discriminating check before teardown.
- **EXCEPT / least likely:** identify the shared rule, then find the choice outside it.
- **Technician A/B:** evaluate each statement independently.

---

## Confirmed weak spots — pulled from the graded class final

These are logged in one place because they're the specific points Logan lost on the graded final, cross-checked against the key. Each fact also lives in its normal category section below — this is a index/focus list, not a duplicate source of truth.

| Missed area | Category | Where it's covered below |
|---|---|---|
| Working angle = angle between the two connected members, not shaft slope; canceling needs equal angles **and** ~180° phasing | D — Shafts/U-CV joints | [Why a Cardan U-joint vibrates](#doc-why-a-cardan-u-joint-vibrates), [Measuring and reading working angle](#doc-measuring-working-angle) |
| Ring & pinion contact pattern: pinion depth moves face↔flank, backlash moves heel↔toe | E — Drive Axle | [Reading the contact pattern](#doc-reading-contact-pattern) |
| Transfer-case range fork (high/low) vs. mode fork (2WD/4WD) are separate actuators | F — 4WD/AWD | [Range fork vs. mode fork](#doc-range-fork-vs-mode-fork) |
| Planetary gearset: hold one member for a ratio, hold none = neutral, lock two = direct 1:1 | F — 4WD/AWD | [Planetary gearset](#doc-planetary-gearset) |
| Clutch chatter has its own cause map (contamination, uneven pressure-plate torque, low hydraulic fluid) — separate from slip/drag and free play | A — Clutch | [Chatter — a second, distinct cause map from slip/drag](#doc-chatter-a-second-distinct-cause-map-from-slip-drag) |
| Continuous-contact (self-adjusting) release bearing noise is most noticeable **engaged**, not disengaged like a traditional pedal-actuated bearing | A — Clutch | [Bearing qualification](#doc-bearing-qualification) |
| Heel = outer tooth end, toe = inner — confirmed correct as already documented | E — Drive Axle | [Hypoid terminology and load](#doc-hypoid-terminology-and-load) |
| Hunting = no common tooth-count factor, no timing marks. Non-hunting = ratio reduces to a whole number, timing marks required | E — Drive Axle | [Hunting vs. non-hunting gear sets](#doc-hunting-vs-non-hunting-gear-sets) |

**Heel/toe (Q58) — resolved:** Logan confirmed directly (2026-09-22) — **toe = inside (inner end), heel = outside (outer end)**. That matches what was already documented below, so nothing changed there; the confusion was real but the guide's content was already right. The photographed key's apparent "Student A only" reading (which would have scored "toe = inner" wrong) doesn't square with this and is set aside as a probable misread or key error, not acted on.

**Hunting/non-hunting (Q60) — added:** the standard definition is now documented in Section E ("Hunting vs. non-hunting gear sets") — hunting = tooth counts share no common factor, no timing marks; non-hunting = ratio reduces to a whole number, repeating tooth contact pattern, timing marks required at reassembly. The photographed key's "Both A and B" reading, which would credit both technicians despite the two statements having the definitions swapped relative to each other, is set aside rather than reflected here.

---

# A. Clutch Diagnosis and Repair — 16%

## What ASE can test

Diagnosis of noise, binding, slip, pulsation, chatter, pedal effort, and release faults; mechanical linkage and pedal switches; hydraulic masters/slaves/lines/dampers; release and pilot bearings; disc/pressure plate; flywheel, dual-mass flywheel, ring gear, runout and crankshaft endplay; contamination sources; bellhousing/case alignment and dowels; and powertrain mounts.

## Mechanism

Pedal up and engaged:

**Flywheel → clamped disc → disc splines → input shaft**

Pedal down and released:

**Pedal/linkage or hydraulic pressure → release bearing → pressure-plate fingers → clamp force removed**

## Diagnostic map

| Complaint | Strong direction | Confirm before replacement |
|---|---|---|
| RPM flare under load | Slip: clamp, friction material, adjustment, contamination | Verify free play/release position, leak source, disc/pressure-plate/flywheel condition |
| Hard first/reverse or clash while stopped | Drag: incomplete release or pilot support | Release travel, hydraulics/linkage, disc warp, pilot bearing, alignment |
| Pulsation at pedal | Rotating release/flywheel/pressure-plate geometry | Runout, warped/uneven surfaces, release components |
| Chatter on takeoff | Uneven friction or powertrain movement | Contamination source, hot spots/runout, mounts, alignment |
| Noise as release load begins | Release-system direction | Bearing, retainer/guide tube, fork/pivot, preload/contact design |
| Noise with full release and relative engine/input-shaft motion | Pilot-bearing direction | Confirm input-shaft state and support condition |

### Slip versus drag

- **Slip = will not hold torque.** High load makes it obvious.
- **Drag = will not release torque.** Stopped shifts and reverse make it obvious.
- Too much free play can reduce release travel and cause drag.
- Too little free play can maintain release load and cause slip.

### Bearing qualification

Pedal position is an observation framework, not a universal proof of when a bearing starts rotating. Some concentric release systems maintain bearing contact and rotation. Ask what changed: rotation, release load, or relative speed.

**Resolving "when is it noisiest" (a missed question type):** a traditional, pedal-actuated release bearing normally only contacts the pressure-plate fingers when the pedal is pressed — so its noise is typically most noticeable **disengaged**. A **continuous-contact/self-adjusting clutch (SAC) release bearing**, common on GM vehicles, rides against the fingers and rotates with the engine essentially all the time the engine runs — so its noise is typically most noticeable **engaged** (normal driving), since that's when it's continuously loaded and turning, not just during the moment of a shift. Identify which design is in the vehicle before picking an answer; don't assume the pedal-actuated pattern is universal.

### Chatter — a second, distinct cause map from slip/drag

Chatter (a shudder/judder on engagement, not simple slip or drag) has its own set of causes, and a class question testing chatter is not testing the same thing as one testing slip vs. drag:

- **Contamination** — oil, grease, or coolant on the friction disc causes uneven grab as the disc engages. This is the classic chatter cause, not a free-play problem.
- **Uneven pressure-plate clamp load** — pressure-plate fasteners tightened unevenly (not to the sequence/torque spec) load the diaphragm/springs unevenly, so clamp force isn't uniform around the disc as it engages.
- **Inconsistent hydraulic apply** — a low clutch master-cylinder fluid level can produce inconsistent release/engagement travel and contribute to chatter, separately from contamination or fastener torque.
- Free play (too much or too little) is a **slip/drag** cause, not the standard chatter explanation — don't reach for it first on a chatter question.

### Measurements and service logic

- Flywheel runout and crankshaft endplay require a dial indicator and an application specification.
- Inspect the rear main seal and other contamination sources before installing a new clutch.
- Bellhousing/case mating surfaces and alignment dowels matter because misalignment can load the pilot/input shaft and cause repeated symptoms.
- Dual-mass flywheel movement and reuse limits are application-specific.
- Do not blow clutch dust with compressed air; use the required controlled cleaning method.
- A road test at 15–20 mph, full throttle, in high gear checks for **both** clutch slippage and clutch spin-down (deceleration) behavior — it's not a single-purpose test.
- Air in a hydraulic clutch system is a **drag** cause (incomplete release from a spongy/inconsistent hydraulic apply); a repair that opens the hydraulic circuit should be followed by a bleed procedure.

---

# B. Transmission Diagnosis and Repair — 17%

## What ASE can test

Noise, clash, hard shifting, jump-out, leaks and fluid; external linkages/cables and mounts; disassembly and inspection; forks, rails, sleeves, detents and interlocks; input/output/countershaft/reverse components; synchronizers and blocking-ring clearance; bearing preload/endplay and shim selection; cases/bores/vents; lubrication pumps/coolers; sensors/actuators; and circuit/module/data diagnosis.

## Constant-mesh and synchronizer operation

- Gear pairs remain meshed.
- A freewheeling speed gear becomes the selected ratio when the sleeve locks its dog teeth to the shaft-mounted hub.
- Hub = fixed to shaft; sleeve = slides; ring = matches speed and blocks; keys/struts = apply the ring first.

Sequence:

**Fork → sleeve/keys → blocker ring → gear cone friction → speed match → sleeve engages gear dog teeth**

## Diagnostic map

| Symptom | First direction | Required caution |
|---|---|---|
| One gear clashes | Its synchronizer/blocker mechanism | Inspect fluid and linkage too; “most likely” depends on conditions |
| All/most gears clash | Clutch drag or global linkage/fluid fault | Do not condemn every synchronizer |
| Hard shift, engine-on worse than engine-off | Release/rotation cause high on list | Engine-off success does not certify every internal part |
| Pops out | Incomplete engagement or axial movement | Linkage, fork/groove, hub/sleeve/dogs, detent, bearings/endplay, mounts |
| Noise in one gear | Parts uniquely loaded/speeded in that power path | A rotating part may be unloaded; trace actual torque path |
| Noise in every ratio | Common rotating support, fluid, or broad wear | Use input/output speed and load changes to narrow |
| Complaint after fluid change | Wrong type/viscosity/level | Use exact specification |

## Measurements

- **Endplay/preload:** identify the temporary assembly, measurement points, shim/spacer location, and final verification. Never apply a remembered shim formula to a different unit.
- **Blocking-ring clearance:** seat the ring as the procedure states; compare measured remaining gap with the model's limit.
- **Radial versus axial:** side-to-side/runout versus along-axis/endplay.
- **Pump/cooler:** a manual transmission may have an active lubrication/cooling circuit. A restricted cooler can create high temperature and repeat failure on an equipped application.

## Electrical/electronic coverage

The official task list includes sensors, actuators, switches, modules, solenoids, connectors, harnesses, module inputs/outputs, and data communication. Use circuit fundamentals in the actual operating state. Resistance checks on an unpowered circuit may miss voltage loss that appears only under load.

## Gaskets, seals, and case integrity

Officially tested and easy to skip past: gaskets, sealants, seals, and fasteners at every mating joint, plus the sealing surfaces themselves — a good gasket on a warped or damaged surface still leaks. The case/extension-housing mating surfaces, bores, dowels, bushings, and **vents** are also explicit task-list items. A blocked vent pressurizes the case as it heats up and pushes fluid past a seal that may be perfectly good — check the vent before condemning a seal on a repeat leak. Transmission mounts are inspected/replaced under this category too; a failed mount can present as noise or vibration that looks like an internal fault.

---

# C. Transaxle Diagnosis and Repair — 17%

## What changes from the transmission category

A transaxle integrates the geartrain and final-drive differential. The same shift diagnosis still applies, but the suspect path expands to:

**Clutch/input → selected gear path → output/final-drive pinion → ring gear/differential case → side gears → half-shafts**

ASE also includes the transaxle differential, side bearings, preload/endplay, limited-slip diagnosis, subframe/cradle alignment, pumps/coolers, sensors/actuators, and electronic controls.

## Do not overgeneralize shaft names

Transaxle layouts differ. Synchronizers can be on input or output shafts; the final-drive pinion is placed in the output path; some units use an intermediate shaft. Use the labeled diagram and determine which member is fixed, freewheeling, or delivering final-drive torque.

## Transaxle diagnostic map

| Symptom | Direction |
|---|---|
| One ratio noisy | Selected gear pair/support before the always-active final drive |
| Noise in all ratios and tied to vehicle speed | Final drive, differential, output/intermediate support, half-shaft, or wheel bearing |
| Noise only while cornering | Differential gears/bearings or wheel-bearing load response |
| Gear clash in all shifts | Clutch drag, linkage/fluid, or other global cause |
| Low-fluid overheat | Broad bearing/gear damage possible; find the leak/source |
| Torque steer | Compare tire/steering geometry, mounts, half-shaft/CV geometry, shaft stiffness and actual drive torque; unequal CV angle is one cause, not the only universal cause |

## Differential and limited slip

- Side gears connect to half-shafts.
- Spider/pinion gears allow left/right speed difference.
- Open-differential torque is limited by the low-traction side; avoid saying it “sends all power” without defining torque and speed.
- Limited-slip chatter on tight turns after service: verify specified fluid/additive before teardown.
- Limited-slip designs vary: clutch packs, helical/geared units, viscous or controlled couplers, and lockers do not share one service method.
- Brake-based traction control may use the ABS hydraulic unit to slow a spinning wheel, creating reaction torque without mechanically locking the carrier.

## Setup, seals, fluid, and electronics — same logic as Sections B and E

The official task list tests the transaxle's integrated final drive on the **same measurement and adjustment logic as Section E's rear axle** — differential pinion (spider) gears/shaft/side gears/thrust washers, case/carrier runout, and shaft/differential bearing preload and endplay via shim/spacer selection. Don't treat the transaxle differential as untested just because it isn't a separate rear axle housing; apply Section E's "Setup variables" and "Reading the contact pattern" material directly.

Also explicitly on the task list and easy to overlook here: gaskets/seals/sealing surfaces and case bores/dowels/bushings/vents (same logic as Section B's note above — a blocked vent can push fluid past a good seal); the lubrication system, pumps, coolers, and plumbing; checking and refilling transaxle fluid; and transaxle sensors, actuators, switches, and control-module circuits/data communication (same approach as Section B's electrical coverage — use circuit fundamentals under the actual operating state, not just resistance checks on a dead circuit).

---

# D. Drive/Half-Shafts and U/CV Joints — 13%

## Symptom anchors

| Symptom | Strong direction |
|---|---|
| Clicking/popping on turns | Outer CV joint |
| Shudder under acceleration | Inner/plunging CV joint |
| Clunk on accel/decel or forward/reverse | U/CV joint, splines, slip joint, or driveline lash |
| Speed-related vibration | Tire/wheel, shaft balance/runout, working angle, phasing, or stiff joint |
| Growl changing with cornering load | Wheel bearing direction |

A torn CV boot proves a contamination/lubricant-loss risk, not automatically that the joint is already unusable. Inspect the joint and follow the service criteria.

## Four different vibration terms

| Term | Meaning | Typical check |
|---|---|---|
| Balance | Uneven mass distribution | Balance procedure/weights and physical damage |
| Runout | Shaft does not rotate true | Dial indicator at specified locations |
| Phasing | Relationship of yokes on a multi-joint shaft | Compare yoke orientation to design marks/specification |
| Working angle | Angle through which each joint operates | Measure member slopes and calculate/compare actual joint angles |

A conventional two-joint shaft relies on suitable working angles and correct phasing so the speed variation from one Cardan joint can be canceled by the other. Do not use one universal maximum angle; shaft speed and the manufacturer's design govern.

## Why a Cardan (cross-type) U-joint vibrates

A standard Cardan/cross-type U-joint's output speed varies twice per revolution because the joint's effective radius changes as it rotates through an angle — the greater the angle, the greater the speed variation. This is an inherent design characteristic, not a fault by itself. Framed in vibration-order terms: 1st order = vibration at the same frequency as the shaft's rotation speed; 2nd order = a multiple (here, 2×) of rotation speed. A Cardan-joint driveshaft's angle-driven vibration is inherently 2nd order.

**Canceling it on a two-joint shaft requires both conditions, not just one:**

- **Phasing:** the yokes at each end of the shaft are oriented so the two joints' speed variations are out of step with each other — commonly described as the joints phased 180° apart — so one joint's speed-up cancels the other's slow-down.
- **Equal working angles:** the two joints' operating angles must also match (commonly cited within about half a degree of each other), or the cancellation is incomplete even with correct phasing.

A widely cited rule of thumb keeps each joint's working angle in roughly the 0.5°–3° range: too small an angle and the joint's needle bearings ride on the same contact point without the slight rocking motion that distributes wear, risking brinelling/false-brinelling damage; too large an angle increases the speed variation (and vibration/wear) each joint must cancel. Treat these as general working-angle guidance, not a universal spec — always check the manufacturer's actual angle and phasing tolerance. **CV joints do not share this problem** — a constant-velocity joint is designed to hold the output speed constant through its operating angle, which is why they are used near the wheel instead of a plain cross-type joint.

**Fixed versus plunging location, as a general layout pattern:** the wheel-end joint is typically a fixed-type CV joint (no in/out travel), and the driveline/transmission-side or transfer-case-side joint is typically a plunging design (a tripod plunge joint is one common plunging type) that absorbs the shaft-length change as suspension travels. Verify the specific vehicle's layout rather than assuming this split always holds.

## Measuring and reading working angle (a missed area — go slow here)

A joint's **working angle** is not the shaft's slope off the ground by itself — it's the angle *between the two members the joint connects* (e.g., transmission/transfer-case output shaft centerline vs. driveshaft centerline at the front joint; driveshaft centerline vs. pinion-yoke/companion-flange centerline at the rear joint). Practical method: an angle finder/protractor (digital or bubble type) is set on each component's flat, machined reference surface (companion flange, shaft, or a specified reference point) with the vehicle at normal ride height, and each member's angle relative to level/horizontal is recorded. The **working angle at a joint = the difference between the angles of the two members it connects**, not either member's raw angle alone.

Two separate conditions must both be evaluated — missing either one is the classic way to miss these questions:

1. **Equal (canceling) angles:** the front and rear joint working angles on a given shaft segment should match within the manufacturer's tolerance (commonly cited around 0.5°) so their speed variations cancel, per the phasing discussion above.
2. **Angle exists in the correct plane, and isn't excessive or too small:** compound angles (vertical **and** horizontal offset together) don't simply add arithmetically — a joint can be within a "vertical-only" spec but still be out of tolerance once horizontal misalignment is included. A U-joint also needs *some* angle (generally that same rough 0.5°–3° range cited above) to keep its bearings rocking instead of sitting static under load; a working angle of 0° is also a fault, not an ideal.

When a question gives you two or three measured angles (e.g., transmission output, driveshaft, pinion/axle) and asks whether the driveline is correct: compute each joint's working angle as the difference between the two members it joins, compare the front and rear joint angles to each other for cancellation, and only then judge whether either is within the reasonable operating range. A shaft that "looks level" can still have a working-angle problem if the transmission and axle mounting angles don't produce matching joint angles.

## Wheel bearing logic

Wheel-bearing noise follows wheel speed and often changes when cornering transfers load. Which side becomes louder is not a perfect universal rule; use the load change, location, looseness, roughness, and service procedure together.

---

# E. Drive Axle Diagnosis and Repair — 17%

## Official coverage groups

1. Ring/pinion diagnosis, runout, depth, pinion preload, carrier preload, backlash, pattern, crush sleeve/shims.
2. Differential carrier, spider/side gears, bearings, thrust washers, and carrier runout.
3. Limited-slip/locking diagnosis, lubricant, internal parts, sensors/modules/actuators/calibration.
4. Axle shafts, studs, splines, seals, bearings, retainers, flange runout, endplay, housing and vent.

## Differential power flow

**Pinion → ring gear → differential case → spider/pinion gears → side gears → axle shafts**

Straight ahead, side gears rotate together. During a turn, spider gears rotate on their shaft and allow the outer wheel to travel farther/faster than the inner wheel.

On an **open** differential, a broken axle shaft on one side can produce a **no-drive condition on both wheels** — with no resistance on the broken side, the case just spins that side gear freely and the intact side never sees enough reaction torque to drive the vehicle. Don't assume a broken axle only affects its own wheel.

## Exam-level traction-device map

Start broad: **open**, **limited slip**, or **locker**. Then use the named parts or control system to identify the subtype. ASE prep needs recognition and diagnostic direction; it does not require memorizing every product's internal service sequence.

| Design | Recognition clue | First direction |
|---|---|---|
| Open + brake traction control | ABS brakes a spinning wheel; carrier stays open | Check wheel-speed input and commanded brake action |
| Clutch limited slip / Posi | Clutch packs resist left/right speed difference | Verify specified fluid/additive before teardown |
| Helical/Torsen limited slip | Helical gears bias torque; no clutch pack | Do not apply a clutch-LSD rule automatically |
| GM/Eaton MLocker/G80 example | Automatic low-speed governor/cam lock | Use the named design's engagement conditions |
| Electric or air locker | Commanded actuator produces full lock | Check command, actuator, and actual completion |
| Other automatic locker | Locks/unlocks without driver command | Identify the design before borrowing G80 logic |

ASE can ask identification, diagnosis, internal inspection, sensors/actuators, calibration, or lubricant selection. “Limited slip” and “locker” are not enough information to select one universal test.

## Axle support types

- **Semi-floating:** shaft carries torque and vehicle load.
- **Full-floating:** hub bearings carry vehicle load into housing; shaft mainly carries torque.

Know retainers and service implications: C-lock versus outer retainer, shaft/bearing/seal inspection, flange runout, and endplay.

## Hypoid terminology and load

- Heel = outer tooth end; toe = inner.
- Face = above pitch line; flank = below.
- In the current class material, drive side is convex and coast side is concave.
- Hypoid sliding action requires the specified lubricant.
- Ring and pinion are a matched set.

## Hunting vs. non-hunting gear sets

Whether a given ring-and-pinion tooth count combination is "hunting" or "non-hunting" comes down to whether the tooth-count ratio reduces to a whole number:

- **Hunting set:** the ring/pinion tooth counts share no common factor — the fraction can't reduce (e.g., `41/11`). Because of that, a given pinion tooth doesn't return to the same ring-gear tooth on any short, predictable cycle; over enough revolutions, each pinion tooth eventually contacts every ring-gear tooth in turn. No factory timing marks are needed at assembly, since there's no single "correct" relative tooth position to preserve.
- **Non-hunting set:** the tooth counts share a common factor and the ratio reduces to a whole number (e.g., `39/13 = 3`). A given pinion tooth repeatedly re-contacts the same limited subset of ring-gear teeth on a short, fixed cycle. Because that original tooth-to-tooth relationship was what the gear set was originally lapped/matched to, **factory timing marks matter** — the set must be reassembled with the marks aligned to preserve the original break-in contact pattern.
- **Partially non-hunting** is the in-between case: the ratio reduces, but not to a whole number (e.g., `42/12 = 7/2`) — still a repeating pattern, still needs timing marks.

Ring and pinion sets are matched/lapped as a set regardless of type; hunting vs. non-hunting affects reassembly (timing marks) and long-run wear distribution, not whether the set is replaced as a pair.

## Setup variables

| Variable | What it controls/measures | Evidence source |
|---|---|---|
| Pinion depth | Pinion position relative to ring gear | Setup dimension and tooth-contact pattern |
| Backlash | Clearance between mating teeth | Dial indicator at multiple ring-gear positions |
| Pinion-bearing preload | Initial load on pinion bearings | Rotating torque under the specified seal/lubrication conditions |
| Side-bearing preload | Initial load supporting carrier | Shim/adjuster procedure and assembly checks |
| Ring-gear runout | Variation in ring-gear mounting/rotation | Dial indicator around ring gear |
| Carrier runout | Carrier rotation/mounting accuracy | Dial indicator per procedure |
| Contact pattern | Actual tooth-contact location | Marking compound under the procedure's load direction |

Do not diagnose a pattern from one mnemonic without identifying drive/coast side, pinion depth, backlash, and the manufacturer's adjustment sequence. Measure backlash at several positions; one convenient point can hide runout or mounting problems.

### Reading the contact pattern (a missed area — the two adjustments control different axes)

Two separate adjustments move the pattern in two separate directions. Keep them apart:

| Adjustment | Moves the pattern... | Because it changes... |
|---|---|---|
| **Pinion depth** (shim under/behind the pinion head) | Toward **face** (top of tooth) or **flank** (toward the root) | How deep the pinion meshes into the ring gear |
| **Backlash** (side-bearing shims — moves the ring gear itself) | Toward **heel** (outer end) or **toe** (inner end) | The radial distance between ring gear and pinion |

| Pattern observed | Read as | General correction |
|---|---|---|
| High on the tooth, toward the **face** | Pinion too far from ring gear (too shallow) | Move pinion **in** (deeper mesh) |
| Low on the tooth, toward the **flank/root** | Pinion too close to ring gear (too deep) | Move pinion **out** (shallower mesh) |
| Toward the **toe** (small end) | Excess backlash / ring gear too far from pinion | Move ring gear **in** toward pinion (reduce backlash) |
| Toward the **heel** (large end) | Insufficient backlash / ring gear too close to pinion | Move ring gear **out** away from pinion (increase backlash) |
| Centered on the tooth, correct face-to-flank height, correct heel-to-toe position | Good pattern | No correction needed |

Read the pattern on the **drive side** (the loaded side used to diagnose setup); a pattern check normally records both drive and coast sides, and the coast-side pattern should move consistently with the drive-side correction. Because pinion depth and backlash are not independent (moving one shifts backlash and can shift the pattern read for the other), re-check backlash after any depth shim change, and always finish against the manufacturer's specific pattern illustration and adjustment sequence — this table is the general mnemonic, not a substitute for the axle-specific chart.

### Crush sleeve

The tightening operation collapses the sleeve; the target is specified bearing **rotating torque**. If preload is exceeded, a typical crush-sleeve procedure requires a new sleeve rather than loosening the nut. A seal-only procedure may specify recording original rotating torque and adding a small amount, but only use that when the identified service procedure says so.

## Noise/load map

| Condition | Direction |
|---|---|
| Whine/howl changing between acceleration and deceleration | Ring/pinion contact or setup; note which tooth side is loaded |
| Rough growl/rumble | Bearing direction |
| High-frequency growl whose pitch rises quickly and changes little with drive/coast | Pinion-bearing direction; pinion bearings rotate faster than carrier or axle bearings |
| Lower-frequency growl affected by carrier load | Carrier/side-bearing direction; a no-load hoist result is a clue, not a verdict |
| Road-speed growl changing during cornering | Axle/wheel-bearing load response; confirm with location, feel, looseness, and roughness |
| Bearing-like pitch changing with road surface or tire rotation | Tire direction before internal axle teardown |
| Clunk on torque reversal | Backlash/lash, spider/side gears, splines, U/CV joints |
| Chatter on tight turns | Clutch-type LSD lubricant/friction or clutch condition |
| Repeated seal leak | Vent restriction, shaft/runout/bearing movement, or damaged sealing surface before another seal |

---

# F. Four-Wheel Drive / All-Wheel Drive — 20%

## Start by identifying the architecture

### Part-time 4WD

When engaged, front and rear output paths may be positively coupled without a center differential. On high-traction pavement, the axles need different average speeds in a turn. If the system cannot accommodate that difference, torque winds up in the driveline and produces bind, hop, steering effort, or difficult disengagement.

### Full-time 4WD/AWD

Uses a center differential or controlled coupling that allows or manages front/rear speed difference. The mechanism may be geared, viscous, hydraulic, electromagnetic, electromechanical, or multi-plate-clutch based.

### On-demand AWD

One axle is normally primary; a controlled coupling adds the secondary axle. Locate the coupling in the real torque path:

- Front-drive-based example: transaxle/PTU → propeller shaft → rear coupling.
- Rear-drive-based example: transmission/transfer case → controlled front connection.

Do not assume engagement waits for wheelspin. Some systems use preemptive inputs such as throttle, steering angle, or modeled demand.

## High and low range

- High range is near direct transfer-case ratio.
- Low range is torque multiplication/reduction for low-speed operation.
- A planetary example may use sun input, fixed ring, and carrier output. For that stated arrangement, ratio is `1 + ring teeth/sun teeth`. Always identify input, output, and held member before using a formula.
- Range selection and axle coupling are separate functions even if one actuator mechanism serves both.

## Range fork vs. mode fork — two different actuators

Many transfer cases use two distinct forks driven by two distinct actuators, and ASE-style questions test whether you keep them separate:

- **Range fork:** selects direct drive (**high range**) or reduction (**low range**). This is a gearing decision — it does not by itself decide 2WD/4WD.
- **Mode fork:** selects **2WD or 4WD** (i.e., whether the secondary output is coupled at all). This is a coupling decision — it does not by itself decide range.

Framed this way, 2HI and 4HI share the same range (no reduction); they differ only in whether the mode fork has coupled the second output. A concern in one function does not confirm the other function's hardware.

> **Tech A/Tech B — worn transfer-case fork:** A vehicle will not shift into 4WD. Technician A says a worn range fork could be the cause. Technician B says a worn mode fork could be the cause. Who is right?
> Correct approach: separate the symptom (won't engage 4WD — a *mode* function) from the mechanism named. A worn **mode** fork directly explains a failure to couple 4WD. A worn **range** fork governs high/low reduction, not 2WD/4WD coupling, so it does not directly explain this symptom unless the question's wiring ties the same actuator to both. Default answer with two independent forks: **Technician B only.** Re-read the question for any statement that the same fork/actuator serves both functions before answering — that detail changes the conclusion.

## Planetary gearset — the three-member hold rule

A simple planetary set has three members: the **sun gear** (center), the **ring/internal gear** (outer, teeth cut on the inside), and the **planet carrier** (holds the planet pinions, which mesh with both sun and ring simultaneously).

**Core rule:** the set only produces a fixed, predictable ratio when exactly one of the three members is **held stationary**. Apply input to a second member and take output from the third. If nothing is held, torque still transfers but there is no fixed output ratio — the set is effectively in neutral. If any two members are locked together, the whole set turns as a unit: **direct drive, 1:1**.

| Held member | Input | Output | Result (general pattern) |
|---|---|---|---|
| Ring | Sun | Carrier | Reduction (torque multiplication); output turns same direction as input |
| Sun | Ring | Carrier | Reduction, but a smaller ratio than holding the ring |
| Carrier | Ring | Sun (or reverse) | Overdrive (output faster than input); output can reverse direction |
| Any two locked together | — | — | Direct drive, 1:1 |

The exact numeric ratio in any case depends on the sun/ring tooth counts for that specific gearset — do not carry a specific class example's ratio (e.g., a particular 4:1 or 1.3:1 figure worked from one instructor's tooth counts) into a different planetary set. The **pattern** of which member is held, and what that produces (reduction, overdrive, or reverse), is the transferable, exam-relevant part.

## GM-oriented mode example

On the GM systems described in the research source:

- **2HI:** rear-drive mode.
- **AUTO:** front axle can be engaged while delivered torque is varied as needed.
- **4HI:** front and rear driveline engaged for suitable low-traction conditions.
- **4LO:** low-range reduction with vehicle-specific shift conditions.

A flashing lamp can indicate an attempted shift; if the shift fails, the prior mode may remain active. This is a GM example, not a universal meaning for every manufacturer's labels or lamps.

## Engagement diagnosis

For “will not engage,” separate these layers:

1. Driver request or automatic request recognized?
2. Required speed/gear/brake/neutral conditions met?
3. Module has valid inputs and no inhibiting fault?
4. Command reaches actuator under load?
5. Ground/return path can carry current?
6. Motor/solenoid/vacuum/hydraulic mechanism moves?
7. Fork/cam/clutch/axle disconnect completes mechanical engagement?
8. Position feedback agrees?
9. Calibration/initialization complete after repair?

A meter showing battery voltage at one motor terminal does not prove correct voltage **across** the motor or useful current through it. Measure with the circuit operating and use the actual reversing/PWM/ground-control design.

## Tire circumference

Different tire circumference can force persistent front/rear or left/right speed difference. Before replacing an AWD coupling or transfer case for binding or vibration after tire service, check:

- Placard/application size.
- All four installed sizes.
- Inflation and load.
- Tread depth/circumference.
- Temporary spare use.

## Complaint map

| Complaint | First questions |
|---|---|
| Binds/hops only in engaged part-time 4WD on dry turns | Is this normal windup for this architecture and surface? Are tires matched? |
| Vibration only when front axle engages | Front shaft/CV/U-joint/angle/runout; front axle; tire mismatch |
| Will not shift into 4LO | Are required shift conditions met? Did request, command, movement, and feedback occur? |
| Stuck in 4WD | Actuator/shift mechanism versus driveline windup preventing release |
| Chatter/bind after fluid service | Correct fluid, fill procedure, adaptation/reset, and tire match |
| Repeated transfer-case or axle seal leak | Vent, shaft movement/runout, surface condition, and fluid level |

## Fluid and service

Transfer-case lubricant is application-specific; “all transfer cases use ATF” is unsafe. The official task list includes fluid level/type and resetting service parameters. It also includes transfer-case internals, shifting mechanisms, shafts/joints, wheel hubs, vents, and calibration/initialization.

---

# Measurement and specification table

| Item | Instrument/evidence | Meaning | Trap |
|---|---|---|---|
| Flywheel runout | Dial indicator | Face/axial deviation | Do not reuse one universal limit |
| Shaft endplay | Dial indicator along axis | Axial clearance | Do not confuse with radial clearance |
| Blocking-ring clearance | Feeler gauge or specified method | Remaining friction/engagement geometry | One passing gap does not prove every synchronizer part good |
| Driveshaft runout | Dial indicator at specified points | Shaft rotation truth | Balance and runout are different |
| Working angle | Angle measurements/calculation | Joint operating geometry | Shaft slope alone is not always the compound joint angle |
| Backlash | Dial indicator at ring gear | Tooth clearance | Check at multiple positions |
| Pinion preload | Inch-pound rotating torque method | Bearing load | Tightening torque is not the measured preload |
| Ring/carrier runout | Dial indicator | Mounting/rotation variation | Can distort backlash readings/pattern |
| Contact pattern | Marking compound under specified loading | Tooth relationship | Use the axle-specific adjustment chart |
| Circuit voltage drop | Voltmeter on operating circuit | Voltage lost in supply/return path | Open-circuit resistance or one terminal voltage may mislead |

---

# Rapid-recall sheet

> **CLUTCH**  
> Slip = will not hold. Drag = will not release.  
> Release travel, pilot support, contamination, runout, alignment, mounts.
>
> **TRANSMISSION**  
> Ring friction matches speed; sleeve engages dog teeth.  
> One gear clash = local synchro direction. All gears = global release/linkage/fluid first.  
> Pop-out = engagement depth/retention/endplay.
>
> **TRANSAXLE**  
> Add final drive, differential, half-shafts, wheel bearings, cradle/mounts, and controls to the same logic.
>
> **SHAFTS**  
> Outer CV fixed, near wheel; inner CV plunges, near trans/transfer case.  
> Balance ≠ runout ≠ phasing ≠ working angle.  
> Cardan joint = inherent 2nd-order vibration (speed varies 2×/rev). Cancel with equal working angles **and** ~180° phasing.  
> Working angle = angle between the *two connected members*, not shaft slope alone. Compound (vertical + horizontal) angles don't add arithmetically.
>
> **AXLE**  
> Backlash = tooth clearance. Preload = bearing load. Depth = pinion position. Pattern = contact evidence.  
> Whine = gears; growl = bearings; clunk = lash; turn chatter = LSD fluid/friction.  
> Pattern: **depth** moves face↔flank (top↔root); **backlash** moves heel↔toe (outer↔inner).  
> High/face = pinion too shallow, move in. Low/flank = pinion too deep, move out.  
> Toe = too much backlash, move ring in. Heel = too little backlash, move ring out.
>
> **4WD/AWD**  
> Largest category. Identify architecture and completed mode.  
> Range fork = high/low. Mode fork = 2WD/4WD. Two different actuators — don't blame one for the other's symptom.  
> Planetary: hold one of sun/ring/carrier for a ratio; lock two together = direct 1:1; hold none = neutral.  
> Tire circumference and fluid type matter.  
> Request → command → loaded circuit → actuator → mechanical engagement → feedback/calibration.
