# ASE A3 Cram Sheet — All Six Categories

**Version 2 · September 22, 2026**

## Confirmed weak spots (graded final)

- Working angle = angle between the two connected members, not shaft slope. Cancel vibration with equal angles **and** ~180° phasing.
- Contact pattern: **depth** moves face↔flank, **backlash** moves heel↔toe.
- Range fork = high/low. Mode fork = 2WD/4WD. Separate actuators.
- Planetary: hold one member for a ratio, hold none = neutral, lock two = direct 1:1.
- **Chatter** ≠ slip/drag: contamination, uneven pressure-plate torque, low hydraulic fluid — not free play.
- Continuous-contact (self-adjusting) release bearing is noisiest **engaged**; traditional pedal-actuated bearing is noisiest **disengaged**.
- Heel/toe: toe = inside, heel = outside.
- **Hunting** = tooth counts share no common factor (e.g. 41/11), ratio doesn't reduce — no timing marks, each pinion tooth eventually meets every ring tooth. **Non-hunting** = ratio reduces to a whole number (e.g. 39/13 = 3) — repeating subset of tooth contacts, timing marks required at reassembly.

## A. Clutch — 16%

- **Slip** = will not hold torque (RPM flare under load). **Drag** = will not release (hard shift/clash while stopped).
- Too much free play → can cause drag. Too little free play → can cause slip.
- Engaged: flywheel → clamped disc → disc splines → input shaft. Released: linkage/hydraulics → release bearing → pressure-plate fingers → clamp force removed.
- Pulsation at pedal = rotating-component runout (flywheel/pressure plate/disc warp), not a hydraulic fault.
- Never air-blow clutch dust; use the required controlled cleaning method.
- **Chatter cause map (separate from slip/drag):** contamination (oil/grease/coolant on the disc) is the classic cause; uneven pressure-plate fastener torque and low clutch master-cylinder fluid can also cause it. Free play is not the chatter answer.
- **Noise timing:** traditional pedal-actuated release bearing → noisiest disengaged (pedal down). Continuous-contact/self-adjusting (SAC) release bearing (common GM) → noisiest engaged (rotates continuously with the engine).
- 15–20 mph full-throttle high-gear road test checks **both** slippage and spin-down, not just one.
- Air in the hydraulic clutch circuit = a **drag** cause; bleed after any repair that opens the circuit.

## B. Transmission — 17%

- Synchro sequence: **fork → sleeve/keys → blocker ring → gear-cone friction → speed match → sleeve engages the gear's dog teeth** (not the cone).
- One gear clashes = that synchro. Every gear clashes = check linkage/release/fluid first, not all synchros at once.
- Pop-out = engagement depth, detent/retention, or endplay.
- Also officially tested (easy to forget): gaskets/seals/sealing surfaces, case bores/dowels/vents (blocked vent → leak past a good seal), and mount inspection.

## C. Transaxle — 17%

- Same synchronizer logic as B, plus an integrated final drive/differential in the same case.
- Don't assume shaft naming/layout carries over from a RWD transmission — verify the specific unit's input/output arrangement.
- The transaxle's final drive is tested on the **same preload/backlash/contact-pattern logic as Section E's rear axle** — it's not a separate topic, just a different housing.
- Also officially tested: gaskets/seals/vents (same as B), fluid level/lube system, and sensor/actuator/control-module circuits.
- Differential logic is the same as Section E below.

## D. Shafts / U-CV joints — 13%

- **Outer CV** = fixed (no plunge), near the wheel, clicks/pops on turns. **Inner CV** = plunges, near trans/transfer case, shudders under acceleration.
- A Cardan (cross-type) U-joint has **inherent 2nd-order vibration** — output speed varies twice per revolution because its effective radius changes through the operating angle.
- Cancel it with **both**: joints phased ~180° apart, AND working angles matched (commonly within ~0.5° of each other). Missing either one leaves vibration.
- **Working angle** = the angle *between the two connected members* at that joint (e.g., trans output vs. driveshaft), not the shaft's slope off the ground.
- Typical joint operating range is roughly 0.5°–3°. A 0° angle is also a fault — no rocking motion means the needle bearings sit static and can brinell.
- Compound angles (vertical + horizontal together) don't simply add arithmetically.
- Four different things, four different checks: **balance ≠ runout ≠ phasing ≠ working angle.**

## E. Drive Axle — 17%

- Power flow: **pinion → ring gear → differential case → spider/pinion gears → side gears → axle shafts.**
- On an **open** diff, a broken axle shaft can cause a **no-drive condition on both wheels** — the broken side just spins free, so the intact side never gets reaction torque.
- **Heel** = outer tooth end. **Toe** = inner. **Face** = above pitch line. **Flank** = below.
- Contact pattern reading — two adjustments, two axes:
  - **Pinion depth** moves the pattern **face ↔ flank** (top ↔ root). High/face = pinion too shallow → move **in**. Low/flank = pinion too deep → move **out**.
  - **Backlash** (side-bearing shims) moves the pattern **heel ↔ toe** (outer ↔ inner). Toward toe = too much backlash → move ring **in**. Toward heel = too little backlash → move ring **out**.
- Preload is measured by **rotating torque**, not tightening torque. A crush sleeve is one-time use — exceed the preload spec and you need a new sleeve, not a loosened nut.
- **Semi-floating** shaft carries torque + vehicle weight. **Full-floating** shaft carries mainly torque; hub bearings carry the weight.
- Traction-device map: open (+ possible brake-traction-control) → clutch-type LSD/Posi (clutch packs) → helical/Torsen LSD (gear-thrust biasing, **no clutch pack, not a full locker**) → GM/Eaton-style automatic mechanical locker (governor/cam engagement at low speed) → electric or air locker (commanded, full lock).
- Whine/howl = gears. Growl/rumble = bearings. Clunk on reversal = lash/splines/joints. Chatter in tight turns = LSD fluid/friction condition.

## F. 4WD/AWD — 20% (largest single category)

- **Part-time 4WD**: no center differential — normal windup/bind/hop on dry-pavement turns is expected for this architecture, not automatically a fault.
- **Full-time 4WD/AWD**: a center differential or controlled coupling manages front/rear speed difference.
- **On-demand AWD**: one axle normally primary; a controlled coupling adds the other. May engage preemptively (throttle, steering angle, modeled demand) — don't assume it waits for wheelspin.
- **Range fork** = high/low (a gearing decision). **Mode fork** = 2WD/4WD (a coupling decision). Two separate actuators — a fault in one does not confirm the other.
- Planetary gearset: hold **one** of sun/ring/carrier for a fixed ratio; hold **none** = neutral; lock **any two** together = direct drive, 1:1.
  - Hold ring, sun in, carrier out = reduction.
  - Hold sun, ring in, carrier out = smaller reduction.
  - Hold carrier, ring in, sun out = overdrive, output can reverse direction.
- Engagement-failure diagnosis order: request/condition met → module has valid input → command issued → ground/return path carries current → actuator moves → mechanical engagement completes → position feedback agrees → calibration/init complete.
- Mismatched tire circumference (size, wear, spare) forces a persistent speed difference — rule it out before condemning a coupling or transfer case for bind/vibration.
- Transfer-case fluid is application-specific; never assume "all transfer cases use ATF."

## Exam mechanics

- 50 total questions, 40 scored, 60 minutes. Unscored research questions are **not identified** — treat every question as scored.
- **Technician A/B:** evaluate each statement independently; don't let one being obviously right or wrong bias the other.
- **Could cause** = one valid mechanism is enough. **Most likely** = compare frequency and the exact conditions given. **First** = the safest, simplest discriminating check before teardown. **EXCEPT/least likely** = find the shared rule, then pick the outlier.

## Twenty instant answers

1. Slip? **Won't hold torque.**
2. Drag? **Won't release.**
3. Sleeve locks onto? **The gear's dog teeth, not the cone.**
4. One gear clashes? **Local synchro problem.**
5. Outer CV joint? **Fixed, clicks on turns.**
6. Inner CV joint? **Plunges, shudders on accel.**
7. Cardan-joint vibration order? **2nd order — speed varies twice per rev.**
8. How to cancel it? **Phase ~180° apart AND match working angles.**
9. Working angle is measured between? **The two members the joint connects, not shaft slope alone.**
10. Heel? **Outer.** Toe? **Inner.**
11. Pattern toward toe? **Too much backlash — move ring gear in.**
12. Pattern high/toward face? **Pinion too shallow — move pinion in.**
13. Bearing preload measured with? **Rotating torque.**
14. Semi-floating shaft carries? **Torque and vehicle weight.**
15. Range fork controls? **High/low range.**
16. Mode fork controls? **2WD/4WD coupling.**
17. Planetary set with nothing held? **Neutral.**
18. Planetary set with two members locked? **Direct drive, 1:1.**
19. Whine vs. growl? **Whine = gears. Growl = bearings.**
20. Helical/Torsen LSD vs. clutch LSD? **Helical biases torque via gear geometry, no clutch pack — not a full locker.**
21. Classic chatter cause? **Contamination on the friction disc** (also: uneven pressure-plate torque, low hydraulic fluid).
22. SAC (self-adjusting) release bearing noisiest when? **Engaged** — it rotates continuously.
23. Open diff, broken axle shaft? **No-drive on both wheels**, not just the broken side.
24. Hunting set needs timing marks? **No** — no common factor, no repeating pattern to preserve.
25. Non-hunting set needs timing marks? **Yes** — ratio reduces, tooth pattern repeats, marks preserve original break-in contact.
