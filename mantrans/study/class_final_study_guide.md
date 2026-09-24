# GM ASEP A3 Class Final Study Guide

**Version 2 · Working draft — revised September 18, 2026**  
**Final: Monday, September 21, 2026**

This guide is built for the **class final**, so it follows the material your instructor emphasized in the notes and on the Unit 2 exam. It is not organized by the professional ASE percentages. It now includes the September 18 additions on differential types and bearing-noise localization. Refresh it again if Monday's notes add or change final-exam material.

## Source boundary

- **Primary:** [`clutchsection.txt`](../notes/clutchsection.txt), [`gears.txt`](../notes/gears.txt), [`drive-axles.txt`](../notes/drive-axles.txt), the whiteboard photo, the noise chart, and the inspected Unit 2 exam.
- **Clarification:** the corrected synchronizer explanation already embedded in `gears.txt` and narrowly used technical qualifications from the research foundation.
- **Not used to set class emphasis:** professional ASE category weights. Your instructor's coverage controls this guide.
- **Still developing:** any additional Unit 3 material taught after the September 18 locker and noise-diagnosis notes.

## How your instructor appears to test

The Unit 2 exam used 30 multiple-choice questions and repeatedly asked you to do four things:

1. **State the part's job.** Example pattern: detent versus interlock, blocker ring versus sleeve.
2. **Follow power flow.** Example pattern: why one range is quiet, why direct drive still works when the countershaft path does not.
3. **Connect a symptom to the affected mechanism.** Example pattern: one-gear clash, all-gear hard shifting, or jump-out.
4. **Identify what a measurement checks.** Example pattern: radial clearance, axial clearance, blocker-ring clearance, or endplay.

Expect Technician A/B, **EXCEPT**, **least likely**, and picture-based questions. Evaluate Technician A and Technician B independently. In an exception question, first say what the other three choices have in common, then find the choice that does not fit.

## The master mental model

For almost every question, run this chain:

**Operating condition → parts rotating → parts carrying torque → load direction → symptom → next confirming check**

A part may rotate without carrying the selected drive torque. A symptom can point in a direction without proving one exact failed part. On this final, use the simplified classroom rule when the question clearly supplies the matching conditions, but pay attention to words such as **could**, **most likely**, and **only**.

---

# Unit 1 — Clutch

## Torque path and terminology

With the pedal **up**, the clutch is **engaged**:

**Crankshaft/flywheel → clamped clutch disc → splined input shaft → transmission**

With the pedal **down**, the clutch is **disengaged/released**. The release mechanism loads the pressure-plate fingers and removes clamp force so engine torque is disconnected from the transmission.

The language feels backward because pressing the pedal *releases* the clutch. Keep these pairs together:

| Pedal | Clutch state | Torque transfer |
|---|---|---|
| Up | Engaged | Engine connected to transmission |
| Down | Disengaged/released | Engine disconnected from transmission |

## Components and jobs

| Component | Job | Test clue |
|---|---|---|
| Flywheel | Stores inertia, damps engine pulses, provides friction surface, absorbs heat, carries starter ring gear | Check surface condition and runout when chatter or odd wear is present |
| Pressure plate | Clamps the disc to the flywheel | Weak or incomplete clamp can cause slip |
| Clutch disc | Transfers torque through its splined hub to the input shaft; hub springs help damp torsional pulses | Contamination may produce slip, grab, or chatter |
| Release bearing | Transfers release force to pressure-plate fingers | Noise beginning as pedal force loads the release system points here in the classroom model |
| Pilot bearing/bushing | Supports the engine end of a separate transmission input shaft | A seized pilot can continue driving the input shaft with the pedal down and imitate clutch drag |
| Linkage/hydraulics | Moves the release bearing far enough to disengage the clutch | Lost travel causes drag; incorrect adjustment may leave constant release load |
| Clutch pedal switch | Starter-interlock input | Vehicle normally should not crank unless the pedal is depressed |

Some concentric release-bearing designs rotate continuously, so pedal position changes **load** more reliably than it proves the bearing's first instant of rotation. For a simple classroom question, use the stated operating condition and the instructor's release-bearing/pilot-bearing distinction.

## Slip versus drag

This is the most important Unit 1 split.

### Slip: the clutch will not hold

- Engine rpm rises without a matching rise in vehicle speed.
- Most obvious when torque demand is high: high gear, heavy acceleration, or lugging load.
- Shop check from the notes: warm vehicle, block wheels, apply parking brake, select a high gear, and release the pedal smoothly. A healthy clutch should stall the engine promptly. Follow the actual shop procedure and safety rules.
- Causes in the notes: worn or contaminated disc, weak pressure plate, incorrect adjustment, or incorrect flywheel height.

### Drag: the clutch will not let go

- Difficult first/reverse engagement while stopped.
- Gear clash because the input shaft continues rotating.
- Severe case: vehicle tries to move while cranking in gear with the clutch pedal down.
- Causes: too little release travel, excessive free play, warped disc/pressure-plate fingers, hydraulic or linkage fault, or seized pilot bearing/bushing.

### Free-play relationship

| Condition | What happens | Likely symptom |
|---|---|---|
| **Too much free play** | Pedal travel is used before the release mechanism moves; it may hit the floor before full release | **Drag / hard shifting / clash** |
| **Too little free play** | Release mechanism can remain partially loaded with pedal up; full clamp may not return | **Slip** and release-component wear |

Remember: clutch wear does **not** automatically mean the hydraulic reservoir level drops. Fluid movement with wear depends on system design; a leak is different from normal wear compensation.

## Noise and chatter logic

- Noise that begins as the pedal starts loading the release system: release-bearing/release-mechanism direction.
- Noise strongest with the clutch fully disengaged, when the engine and input shaft have relative motion: pilot-bearing direction.
- Noise with pedal up and the input shaft rotating can involve the transmission input/front bearing.
- Chatter or pulsation: inspect disc contamination, flywheel/pressure-plate surface condition, runout, alignment, and mounts.
- A seized pilot bearing can keep the input shaft turning even when the disc itself is released.

## Unit 1 answers you should be able to explain aloud

1. Why does high gear expose clutch slip better than first gear?
2. Why can a seized pilot bearing cause hard shifting?
3. Why does excessive free play cause drag rather than slip?
4. Why can insufficient free play cause slip with the driver's foot off the pedal?
5. Which parts turn together with the pedal up, and which can turn at different speeds with it down?

---

# Unit 2 — Manual Transmission and Transaxle

## Ratio and power flow

- **Reduction:** output slower, torque multiplied; numerical ratio greater than 1:1.
- **Direct:** input and output same speed; 1:1.
- **Overdrive:** output faster than input; numerical ratio less than 1:1.
- Ratio for a simple external pair: **driven teeth ÷ drive teeth**.
- An idler adds another direction reversal, changing the output direction compared with a simple two-gear pair, but it does not change the overall input-to-output ratio. A 10:7:20 train still gives `20 ÷ 10 = 2:1`.
- Helical gears are quiet but create axial/end thrust.

In a constant-mesh transmission, the gear teeth remain meshed. The shift does not slide one full-size gear into another. The synchronizer locks the selected freewheeling speed gear to its shaft.

## Synchronizer sequence

Know the parts separately:

| Part | Function |
|---|---|
| Hub | Splined to the shaft; rotates with it |
| Sleeve | Slides on the hub and provides positive engagement |
| Keys/struts and springs | Move/preload the blocker ring before the sleeve reaches the gear teeth |
| Blocker ring | Uses friction at the gear cone to change gear speed and blocks sleeve engagement while speeds differ |
| Gear cone | Friction surface used for speed matching |
| Gear dog/clutch teeth | Teeth the sleeve finally engages to lock the gear to the shaft |

Correct chain:

**Fork moves sleeve → keys/struts push blocker ring → ring contacts gear cone → friction speeds or slows the freewheeling gear → ring blocks while speeds differ → speeds match → sleeve passes the ring and engages the gear's dog teeth**

The sleeve does **not** engage the cone. The cone is a friction surface. The synchronizer changes the freewheeling gear's speed to match the hub/sleeve/shaft.

During a normal upshift, the next gear normally must be slowed to the new lower shaft-speed relationship. Do not answer a power-flow question by memorizing “upshift means slow” alone; identify which shaft and gear the question names.

## Shift controls

- **Detent:** helps hold a rail/gear in its selected position.
- **Interlock:** prevents two gears from being selected at the same time.
- **Reverse lockout:** prevents accidental reverse selection.
- **Shift fork:** positions the sleeve. Excessive fork-to-sleeve groove clearance can prevent full dog-tooth engagement.

Resting a hand on the shifter can maintain force on the fork/sleeve interface and increase wear.

## Symptom map

| Symptom | First direction | Why |
|---|---|---|
| One gear clashes | That gear's synchronizer/blocker ring | Localized speed-matching fault |
| Most or all gears clash | Clutch drag/release problem first | Input shaft remains driven |
| Hard shift with engine running but easier with engine off | Clutch release/rotation-related cause moves high on list | Removing engine-driven shaft speed removes one condition; it does not prove every internal part is good |
| Pops out of gear | Incomplete engagement or axial movement | Fork/groove wear, linkage, worn engagement teeth, detent, bearing wear/endplay |
| Noise only in one ratio | Components uniquely loaded or turning at that ratio | Use the power-flow diagram |
| No drive in reduction gears but direct drive works | Countershaft/input drive path fault can be bypassed in direct | Follow torque path, not the gear name alone |
| Hard shift after fluid service | Wrong fluid or level | Synchronizer friction depends on the specified lubricant |

The Unit 2 exam treated both excessive selected-gear axial clearance and worn synchronizer engagement parts as possible causes of jump-out. Keep **speed matching** separate from **positive engagement/retention**: a worn blocker surface causes clash; worn hub/sleeve/dog engagement can contribute to jump-out.

## Inspection and measurements

- **Radial clearance/runout:** movement or deviation across the shaft's radius; dial-indicator stylus is positioned to detect side-to-side movement.
- **Axial clearance/endplay:** movement along the shaft axis; dial indicator is positioned to detect in-and-out movement.
- **Blocker-ring clearance:** seat the ring on the gear cone and measure the specified remaining gap. Less gap can indicate wear, but the exact limit is application-specific.
- **Oil grooves in a blocker ring:** cut through the lubricant film so the friction surfaces can act; the grooves are not simply a universal wear gauge.
- Select-fit thrust washers or snap rings may be used to set axial clearance on some designs.

## Lubrication and towing

Most class examples use splash lubrication: the lower gear/countershaft distributes oil. Some manual transmissions should not be flat towed because the output may turn without the normal parts that throw lubricant. Use the vehicle's actual towing instructions.

Wrong viscosity or wrong fluid type can change shift effort and synchronizer behavior. “Manual transmission” does not automatically mean one universal gear oil.

## Transaxle

- A transaxle combines the transmission and final drive/differential in one assembly.
- The final-drive pinion is on the transaxle's output path.
- Synchronizers can appear on different shafts depending on design; use the diagram rather than a universal shaft-name shortcut.
- Half-shafts connect through the differential side gears.
- Differential noise when cornering points toward the parts that permit left/right speed difference.
- Low lubricant can overheat and damage the whole transaxle.
- In the typical classroom transverse-transaxle layout, the final-drive ring gear and pinion are **helical gears** on parallel shafts, not the offset hypoid arrangement used in a RWD rear axle. Identify the actual gear type shown or specified because layouts can differ.

---

# Unit 3 — Drive Axles and Rear Final Drive

## Why the rear axle changes direction

In a typical longitudinal RWD layout, the engine, transmission output, and propeller shaft rotate along the vehicle. The ring-and-pinion set turns the torque path approximately 90 degrees so it can reach the left and right axle shafts.

Torque path:

**Driveshaft → pinion → ring gear → differential case → spider/pinion gears → side gears → axle shafts**

The differential case turns with the ring gear. In a straight line, the side gears rotate together. In a turn, spider-gear action permits one side gear/axle to turn faster than the other.

## Semi-floating versus full-floating

| Design | Axle shaft carries | Vehicle load path | Failure implication |
|---|---|---|---|
| Semi-floating | Torque **and** vehicle weight/load | Wheel load passes through axle shaft and outer bearing into housing | Depending on retention design, a broken shaft can allow wheel/shaft separation |
| Full-floating | Primarily torque | Wheel hub bearings carry vehicle load into the housing/spindle | Axle shaft can be removed without supporting vehicle weight |

Memory: **semi = shaft carries two jobs; full = shaft carries torque while the hub carries load.**

## Hypoid gear terminology

- A hypoid pinion meshes below the ring-gear centerline in the class example.
- The offset helps lower the driveshaft and permits a strong, quiet gear arrangement, but creates sliding action that requires the specified lubricant.
- Ring and pinion are lapped as a matched set. If one gear is damaged, the matched set is normally replaced together.
- **Heel:** outer end of the ring-gear tooth.
- **Toe:** inner end.
- **Face:** above the pitch line.
- **Flank:** below the pitch line.
- In the class/textbook description, the ring gear's **drive side is convex** and the **coast side is concave**.

Load states:

| State | What is happening | Lash/load idea |
|---|---|---|
| Drive | Engine drives vehicle | Drive side loaded; clearance at coast side |
| Coast | Vehicle drives engine during closed-throttle deceleration | Coast side loaded; clearance shifts to drive side |
| Float | Enough throttle to remove most drive/coast load | Lash is effectively split between both sides |

## Hunting, non-hunting, and partially non-hunting

- **Hunting:** tooth-count fraction cannot be reduced. Each pinion tooth eventually contacts every ring-gear tooth. No timing marks required for tooth pairing.
- **Non-hunting:** ratio is a whole number, such as `40/10 = 4`. A pinion tooth repeatedly meets the same subset of ring-gear teeth. Timing/alignment marks matter.
- **Partially non-hunting:** reducible fraction that does not reduce to a whole number. Each pinion tooth meets only part of the ring gear before the pattern repeats. Timing marks matter.

Examples:

- `41/11 = 3.73` and the fraction cannot reduce → hunting.
- `39/13 = 3` → non-hunting.
- `42/12 = 3.5`, reducible to `7/2` → partially non-hunting.

## Reverse-cut concept

A front axle built from a standard rear-drive gear arrangement can force the ring gear to work on its weaker coast side. A purpose-built reverse-cut gear set reverses the spiral direction so the intended drive side carries forward load in the front-axle installation. Housing oiling and pinion position are design-specific; do not treat a standard gear set as interchangeable merely because it physically fits.

## Open, limited-slip, and locking differentials

Use the broad classification first: **open permits differentiation, limited slip resists it, and a locker can couple both axle outputs.** Trace the exact parts only when the question names a design. The GM/Eaton sequence deserves extra attention because the instructor taught it directly.

Start with the differential's job. The case turns with the ring gear. With equal wheel speeds, the spider/pinion gears travel with the case without rotating on their own shaft. When the wheel speeds differ, the spiders rotate on their shaft so the two side gears can turn at different speeds.

| Design | Class-ready mechanism |
|---|---|
| Open + brake traction control | ABS-based brake action can slow a spinning wheel and create reaction torque; the carrier remains mechanically open |
| Clutch-type limited slip / Posi example | Side-gear separating thrust loads clutch packs, resisting left/right speed difference while still allowing turns |
| Helical/Torsen limited slip | Helical-gear thrust and internal friction bias torque; it is not a fully locked axle |
| GM/Eaton mechanical locker | Wheel-speed difference spins governor → flyweight catches latch → cam ramps → clutches self-apply → side gears lock to case; high-speed lockout prevents engagement above roughly 20 mph |
| Eaton ELocker | An electromagnetic actuator locks a side gear to the case when commanded |
| Air locker | Pneumatic actuator commands lock; do not assume its internal locking member is the same as an ELocker or clutch LSD |
| Detroit Locker | Automatic-locking design with a different operating strategy from the GM/Eaton governor-and-cam unit |

Do not use **limited slip**, **Positraction**, and **locker** as interchangeable mechanism names. First identify the design, then apply its fluid, actuation, and diagnostic rule.

## Noise diagnosis

Road-test under four load conditions:

1. **Drive:** light/moderate acceleration.
2. **Cruise:** enough throttle to hold speed.
3. **Float:** just enough throttle to remove most load while speed falls slowly.
4. **Coast:** closed-throttle deceleration.

Use coast-in-neutral as an extra isolation step when safe and permitted by procedure.

| Noise/condition | Direction to investigate |
|---|---|
| Howl/whine that changes between drive and coast | Ring-and-pinion wear or setup; identify the loaded tooth side |
| Rough growl/rumble, sometimes “wow-wow” | Bearing direction |
| Faster-pitched growl rising quickly with speed and changing little with throttle | Pinion-bearing direction; the pinion turns faster than carrier or axle bearings |
| Slower growl that changes with carrier load | Carrier/side-bearing direction; lack of noise on a lightly loaded lift is only a clue |
| Road-speed growl changing during a controlled swerve | Axle/wheel-bearing load response; confirm by location, feel, looseness, and roughness |
| Low rumble above road speed threshold | Carrier or other rotating bearing direction; confirm with loading/location |
| Clunk on torque reversal | Excess lash/clearance, U-joints, splines, or differential parts |
| Chatter in tight turns | Clutch-type limited-slip fluid/friction condition or worn clutch pack |
| Noise changes with road surface | Tire direction |
| Noise changes with cornering load | Wheel/axle/carrier bearing or differential direction; use location and other conditions to narrow it |

The chart gives **directions**, not automatic verdicts. Ask what changed: speed, torque direction, cornering load, or the engaged torque path.

Pitch rate helps because pinion bearings rotate faster than carrier and axle bearings. Tire noise can still imitate bearing noise; use road-surface response, tire rotation/inspection, and lift behavior. A gear whine is usually load-sensitive and may fade in float. A bearing growl is usually more speed-linked, although load can still change it.

## Backlash, depth, and preload

- **Backlash:** clearance between ring and pinion teeth.
- **Pinion depth:** pinion position relative to the ring gear.
- **Pinion-bearing preload:** controlled initial bearing load, checked by **rotating torque**, not by confusing it with the high torque used to tighten/crush components.
- **Carrier/side-bearing preload:** initial load supporting the differential carrier.
- **Contact pattern:** evidence of where the teeth meet under marking compound; interpret it with the axle's procedure.

### Collapsible/crush sleeve

The new sleeve begins too long. Tightening the pinion nut collapses it until the bearings seat and the specified rotating preload is reached. Once over-crushed, it is not repaired by simply backing off the nut; use a new sleeve and repeat the setup. When a service procedure permits seal replacement without changing the sleeve, measure the original rotating torque and follow that application-specific procedure precisely.

## Lower-yield but testable Unit 3 points

- Semi-floating axle retention may use an inner C-lock or an outer bearing retainer.
- Integral/Salisbury-style carrier: removable rear cover; housing and tubes form the main assembly.
- Removable/banjo-style carrier: center carrier assembly removes from the housing.
- Axle fluid level is not universally exactly even with the fill hole; use the specification.
- Metal debris can disturb magnetic wheel-speed sensors in or near an axle housing.
- Inspect a repeated axle-seal leak for shaft movement, vent restriction, or surface damage instead of replacing the seal blindly.

---

# High-value distinctions

| Do not mix up | Correct distinction |
|---|---|
| Clutch slip / drag | Slip will not hold; drag will not release |
| Engaged / released | Engaged is pedal up; released/disengaged is pedal down |
| Pilot / release bearing | Pilot supports input shaft; release bearing operates pressure plate |
| Blocker ring / sleeve | Ring matches speed and blocks; sleeve locks gear to hub |
| Detent / interlock | Detent holds a selection; interlock prevents two selections |
| Gear teeth / dog teeth | Gear teeth stay meshed; dog teeth provide selected engagement |
| Radial / axial | Radial is side-to-side; axial is along the shaft |
| Backlash / preload | Gear clearance / bearing load |
| Pinion depth / backlash | Pinion position / tooth clearance |
| Heel / toe | Outer end / inner end of ring-gear tooth |
| Gear whine / bearing growl | Tooth contact / rough bearing sound |
| Semi-float / full-float | Shaft carries load + torque / shaft mainly carries torque |
| Limited slip / locker | Resists differentiation / mechanically couples outputs for full lock |
| Clutch / helical limited slip | Clutch-pack friction / gear-thrust friction |
| GM/Eaton mechanical locker / ELocker | Automatic governor-cam sequence / commanded electromagnetic actuation |
| Pinion / carrier / axle-bearing speed | Fastest / case speed / wheel speed |

---

# Original class-style practice

Answer these without the key. For Technician A/B questions, decide whether each statement is true before looking at the four choices.

1. A clutch has excessive pedal free play. Which complaint is most likely?  
   A. Slip under load  
   B. Drag and difficult first/reverse engagement  
   C. Wheel-bearing growl  
   D. Differential chatter

2. Technician A says a seized pilot bearing can keep the input shaft turning with the clutch pedal down. Technician B says this can cause gear clash while the vehicle is stopped. Who is correct?  
   A. A only  
   B. B only  
   C. Both A and B  
   D. Neither A nor B

3. A vehicle accelerates in a high gear and engine rpm rises sharply without a matching speed increase. This is:  
   A. Clutch drag  
   B. Clutch slip  
   C. Interlock failure  
   D. Excessive axle preload

4. Which clutch component supports the engine end of a separate transmission input shaft?  
   A. Release bearing  
   B. Pilot bearing/bushing  
   C. Detent ball  
   D. Blocker ring

5. A 12-tooth drive gear turns an idler and then a 36-tooth driven gear. The overall ratio is:  
   A. 1:3 and reversed at the output  
   B. 3:1 with the output rotating in the same direction as the input  
   C. Determined by the idler tooth count  
   D. 1:1

6. Technician A says the synchronizer sleeve engages the speed gear's cone. Technician B says the blocker ring uses the cone to match speed before the sleeve engages dog teeth. Who is correct?  
   A. A only  
   B. B only  
   C. Both A and B  
   D. Neither A nor B

7. Which part prevents two gears from being selected simultaneously?  
   A. Detent  
   B. Interlock  
   C. Blocker ring  
   D. Pilot bearing

8. A transmission grinds only during the 3–4 shift. The most direct first suspect is:  
   A. Clutch release system  
   B. 3–4 synchronizer/blocker mechanism  
   C. Differential side bearings  
   D. Pinion crush sleeve

9. All of these can contribute to a transmission jumping out of one gear **EXCEPT**:  
   A. Worn fork-to-sleeve interface  
   B. Excess shaft endplay  
   C. Worn engagement teeth  
   D. A correctly operating interlock

10. Technician A says blocker-ring oil grooves help cut through the oil film. Technician B says less blocker-ring-to-gear clearance can indicate wear when the service procedure uses that measurement. Who is correct?  
    A. A only  
    B. B only  
    C. Both A and B  
    D. Neither A nor B

11. A vehicle has no drive in the reduction ranges but still drives in a direct 1:1 range. Which idea best explains the symptom?  
    A. Direct drive can bypass the failed countershaft reduction path  
    B. The clutch is completely released  
    C. Both axle shafts are broken  
    D. The transfer case must be in neutral

12. A dial indicator is positioned to measure in-and-out movement along a shaft. It is measuring:  
    A. Radial runout  
    B. Axial endplay  
    C. Gear ratio  
    D. Pinion tooth depth

13. In a typical manual transaxle, the half-shafts are splined to the differential:  
    A. Spider gears  
    B. Side gears  
    C. Case only  
    D. Ring-gear teeth

14. Which statement describes a full-floating axle?  
    A. The axle shaft carries vehicle weight and torque  
    B. The axle shaft carries primarily torque while hub bearings carry vehicle load  
    C. The axle has no differential  
    D. The pinion is centered with the ring gear

15. Technician A says the heel is the outer end of a ring-gear tooth. Technician B says the class/textbook describes the drive side as convex and the coast side as concave. Who is correct?  
    A. A only  
    B. B only  
    C. Both A and B  
    D. Neither A nor B

16. A ring gear has 41 teeth and the pinion has 11. The fraction cannot be reduced. This is a:  
    A. Non-hunting set requiring tooth-pair timing  
    B. Hunting set in which each pinion tooth eventually meets every ring tooth  
    C. Partially non-hunting set  
    D. Direct-drive set

17. A rear axle produces a whine on acceleration but becomes much quieter during float. Which condition changed most directly?  
    A. Road surface  
    B. Gear-tooth load  
    C. Tire circumference  
    D. Clutch free play

18. A new crush sleeve is tightened until rotating preload is far above specification. What is the correct direction?  
    A. Back off the nut until the reading drops  
    B. Reuse the sleeve with extra lubricant  
    C. Replace the sleeve and repeat the setup  
    D. Increase backlash

19. A clutch-type limited-slip differential chatters during tight turns shortly after service. What should be checked before overhaul?  
    A. Correct axle lubricant/friction modifier for the application  
    B. Clutch pedal free play  
    C. Synchronizer sleeve clearance  
    D. Transmission pilot bearing

20. Technician A says pinion-bearing preload is checked using rotating torque. Technician B says the torque used to collapse the sleeve and the final rotating-torque measurement are the same quantity. Who is correct?  
    A. A only  
    B. B only  
    C. Both A and B  
    D. Neither A nor B

21. In a conventional open differential moving straight ahead with equal wheel speeds, the spider/pinion gears normally:  
    A. Spin on their shaft at twice axle speed  
    B. Travel with the case without spinning on their shaft  
    C. Lock one side gear to the case  
    D. Stop the ring gear

22. Which sequence describes the GM/Eaton mechanical locker discussed in class?  
    A. Wheel-speed difference → governor/flyweight latch → cam ramp → clutch apply/full lock  
    B. Driver pedal → hydraulic slave → blocker ring  
    C. Tire wear → wheel bearing → pinion depth  
    D. Electromagnet → transfer-case fork → planetary reduction

23. Technician A says a helical/Torsen differential biases torque using gear thrust and internal friction. Technician B says it is the same mechanism as a clutch-type Posi unit. Who is correct?  
    A. A only  
    B. B only  
    C. Both A and B  
    D. Neither A nor B

24. A rough growl rises in pitch quickly with road speed, changes little between drive and coast, and is faster than a wheel-speed rumble. Which class-note direction is strongest?  
    A. Pinion bearings  
    B. Clutch release bearing  
    C. Synchronizer blocker ring  
    D. Tire tread only

## Answer key and reasoning

1. **B** — excessive free play reduces release travel and causes drag.  
2. **C** — the seized pilot can continue driving the input shaft, producing clash.  
3. **B** — the clutch is failing to hold torque.  
4. **B** — the pilot bearing/bushing supports the input-shaft end.  
5. **B** — `36 ÷ 12 = 3:1`; two external meshes return the output to the input's direction.  
6. **B** — the cone is the friction surface; the sleeve ultimately engages dog teeth.  
7. **B** — an interlock prevents simultaneous selection.  
8. **B** — a one-shift complaint localizes the synchronizer direction.  
9. **D** — a correctly operating interlock prevents conflicting selections and does not cause single-gear jump-out.  
10. **C** — both describe valid functions/inspection logic, with the actual clearance limit coming from service information.  
11. **A** — direct drive can couple input to output while bypassing the failed reduction path.  
12. **B** — along-axis movement is axial endplay.  
13. **B** — side gears connect the differential to the half-shafts.  
14. **B** — hub bearings support vehicle load; the shaft primarily transfers torque.  
15. **C** — both match the current class notes/textbook wording.  
16. **B** — irreducible tooth counts produce a hunting set.  
17. **B** — float removes most tooth load, so a load-sensitive gear noise changes.  
18. **C** — an over-collapsed sleeve is replaced.  
19. **A** — correct limited-slip lubricant/additive is the first check after service.  
20. **A** — tightening effort collapses the sleeve; bearing rotating torque is the controlled result being measured.
21. **B** — equal side-gear speeds let the spiders travel with the case without rotating on their shaft.  
22. **A** — the governor/latch triggers cam-and-clutch full lock in the class-taught unit.  
23. **A** — helical and clutch-type limited slips use different friction mechanisms.  
24. **A** — pinion bearings rotate faster, so their growl can climb in pitch more quickly and be less throttle-sensitive than gear whine.

---

# Study sequence through Monday

## Through the last note update

- Read this once and mark every statement you cannot explain without looking.
- Add new class notes normally; do not rewrite them into this guide during lecture.
- If Monday adds material before the final, refresh Unit 3 and the practice questions once more.

## Saturday

- Draw three paths from memory: clutch torque path, one selected transmission ratio, and rear-axle torque path.
- Work the 24 questions closed-book.
- For every miss, write one sentence stating **what condition in the question mattered**.

## Sunday

- Explain the high-value distinctions aloud without the table.
- Redo only missed questions, then make yourself explain why each rejected option is wrong.
- Spend the largest block on the newest Unit 3 material unless the practice results show another weakness.

## Monday quick review

- Slip versus drag.
- Synchronizer sequence.
- Detent versus interlock.
- Radial versus axial.
- Semi-float versus full-float.
- Heel/toe, drive/coast, convex/concave.
- Hunting-set classification.
- Backlash versus depth versus preload.

Stop learning new details immediately before the exam. Use the final minutes to recall mechanisms and diagnostic conditions.
