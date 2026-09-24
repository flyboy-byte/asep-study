# Unit 2 Cram Sheet — Transmission/Transaxle Internals

**RATIOS:**
Reduction = more torque, less speed (numerically high).
Overdrive = less torque, more speed (numerically <1).
Direct = 1:1.
Idler = direction only, never changes ratio, even if it's a different size.
10:7:20 gearset still reduces to 2:1 overall.

**CONSTANT MESH:**
Never fixed-to-fixed. Always fixed gear ↔ speed gear (freewheeling until locked).
Only one gearset locked at a time.
Helical gears = quiet, but cause endthrust → need thrust surfaces.
Splash lubricated: countershaft throws oil onto mainshaft.

**SYNCHRONIZER — memorize this chain:**
Fork → sleeve → keys → blocker ring → gear cone (friction, speed match) → ring unblocks → sleeve engages gear's **dog teeth** (not the cone).
Hub = fixed to shaft. Sleeve = slides on hub. Ring = blocks until speed matches. Keys = move ring before sleeve.
Synchronizer syncs the *freewheeling gear* to hub speed — not "sleeve to gear."
Wrong fluid → fast blocker-ring wear (esp. paper-coated steel rings).

**SHIFT MECHANISM:**
Detent = holds gear selected, can be overcome by force.
Interlock = physically prevents two gears engaging at once.
Fork-to-sleeve groove clearance must be correct or sleeve won't fully seat.

**SYMPTOM LOGIC:**
One gear grinds → that gear's synchronizer/blocker ring.
All gears grind → clutch drag first, not every synchro at once.
Won't shift at all, but fine w/ engine off → clutch drag (input shaft still turning).
Pops out of gear → fork-to-sleeve clearance (top answer) → shaft endplay → worn dog teeth → detent → linkage.

**NOISE TEST (constant road speed, shift through gears):**
Pitch same in every gear at same road speed → output shaft/bearing.
Pitch changes gear-to-gear at same road speed → that gear's gearset.
Master question always: *what's rotating, and at what speed, when the noise happens?*

**TRANSAXLE:**
Input shaft = "clutch shaft," part of mainshaft assembly → no pilot bearing needed (self-supported).
Longitudinal (non-transaxle) trans → input shaft separate from mainshaft → needs pilot bearing (3rd support point).
Transaxle final-drive output = treat like a differential (bridges into Unit 3).

**TORQUE STEER:**
Most common cause = unequal CV joint operating angles (also: unequal shaft length/twist).
Equal angles on both sides → no torque steer, even with imperfect mounts.
Cousin concept: bump steer (suspension/steering geometry).
