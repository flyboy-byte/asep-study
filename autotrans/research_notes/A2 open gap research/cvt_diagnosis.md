# CVT operation and diagnosis (A2 depth, diagnosis-first)

Researched 2026-09-30 for Logan (GM dealership tech, 7 ASE passes, strong electrical). Basics skipped.
**Access note:** Full-page fetches were blocked by the egress proxy. I tried gearsmagazine.com and ase.com, and both returned EGRESS_BLOCKED. **Every finding below comes from search-result snippets** unless it is marked otherwise. "DOCUMENTED (snippet)" means the claim appeared in a search snippet attributed to that URL. Where possible it is corroborated by a second snippet. Open the page to verify before you put any claim in a printed guide. All URLs accessed 2026-09-30.
**Tag key:** DOCUMENTED (snippet) / INFERRED / OPEN. Scope is **U** = universal principle, **OEM** = OEM- or unit-specific, or **SI** = needs service information. Task numbers come from the A2 task map in `autotrans/research.md`. A.1 covers type ID (CVT named), A.4/B.12 fluid, A.8/A.9 road test/NVH, A.11 pressure tests, A.14 hydraulic diagrams, A.17 EPC pressure, A.19/A.26 electronic diagnosis, A.25/C.6 programming/relearn, and C.16 chains/belts/pulleys.
**Constraint reminders:** No ASE question bank is built here. The official sample question is described only as the learner summarized it (public study guide). Its official answer key could not be read (ase.com blocked), so it is OPEN below.

---

## 1. Pulley roles and hydraulic control: what sets ratio and what sets clamp

### Takeaway
Both pulleys have a fixed sheave and a hydraulically moved sheave. In the common design, **primary (drive) pulley pressure is used to set ratio** and **secondary (driven) pulley pressure is used to set belt clamping force (anti-slip)**. Ratio is really a force balance between the two. Lose secondary pressure and you get belt slip. Lose control of primary fill/exhaust and you lose ratio change in one direction.

### Cited Findings
- DOCUMENTED (snippet), U, C.16/A.14: Each pulley has a fixed disk and a moveable disk. Oil pressure in each pulley's cylinder chamber moves the moveable disk axially. This changes V-groove width, which changes the belt's running radius and so the ratio. — [US Patent 7074144 (hydraulic control, belt-drive CVT)](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/7074144); [US Patent 7039516](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/7039516)
- DOCUMENTED (snippet), U, A.17: Pulley thrust is controlled according to input torque, pulley ratio, oil temperature and target shift speed. Secondary-pulley hydraulic pressure is controlled to clamp the belt with a force that "will not cause belt slip". — [US Patent 7553256](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/7553256); [US Patent 6849030](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/6849030) (search-summary synthesis across listed patents; which patent says which line was not separable from the snippet)
- DOCUMENTED (snippet), OEM (Subaru Lineartronic), A.14: **Upshift / "ratio up":** line pressure enters the primary up shift valve and becomes primary pressure, controlled by the **primary up solenoid**. Pressure squeezes the primary pulley, which pushes the belt outward (larger primary radius) while the secondary pulley opens (smaller radius). **Downshift / "ratio down":** the **primary down solenoid** moves the primary down shift valve, which *lowers* primary pulley pressure. The primary opens, the belt rides lower, and the secondary closes. At steady ratio the up and down signals are balanced. — [Gears Magazine, "Subaru CVT Gen 2 Valve Body"](https://gearsmagazine.com/magazine/subaru-cvt-gen-2-valve-body/) (search result; exact source page within results not separable, and Gears is the most likely source)
- DOCUMENTED (snippet), OEM (Jatco), A.14: Jatco units position a ratio control valve with a **stepper motor** to "feed," "hold," or "vent" pressure to the primary pulley. — [Gears, "Jatco CVT Pressures Diagnostics"](https://gearsmagazine.com/magazine/jatco-cvt-pressures-diagnostics/); [Gears, "Stop Wasting Money on Jatco CVT Stepper Motors"](https://gearsmagazine.com/magazine/stop-wasting-money-on-jatco-cvt-stepper-motors/)
- DOCUMENTED (snippet), OEM (Honda), A.14: Honda CVTs use separate linear solenoids for the drive pulley (DR) and driven pulley (DN), a pulley side-pressure control valve, and a third linear solenoid for the start clutch. Start-clutch pressure varies with solenoid current. — [US Patent 5713815](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/5713815); [US Patent 6406402](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/6406402); [US Patent 5766110](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/5766110)
- DOCUMENTED (snippet), OEM (Toyota K313/K120), A.19: SLP controls primary pulley pressure and SLS controls secondary pulley pressure. Related DTCs include P2822 (Pressure Control Solenoid J, SLP, electrical) and P2829 (Pressure Control Solenoid K, SLS, performance). K120F adds an electric pump. — [Toyota-Club.Net DTC K313](https://toyota-club.net/files/techdata/dtc/tr_cvt_k313.htm); [Toyota-Club.Net Direct Shift-CVT FAQ](https://toyota-club.net/files/faq/21-01-10_faq_cvt_en.htm) (enthusiast site that reproduces Toyota data; needs SI)

### Inferences
- INFERRED, U: "Ratio up" in ASE and Subaru language means **upshift toward overdrive**: numerically lower ratio, primary groove narrowed and filled, secondary groove widened. "Ratio down" means downshift toward low: primary exhausted, secondary squeezes. This vocabulary is a trap if you think of "ratio number going up".
- INFERRED, U: To **downshift**, primary pressure must be *released* (exhausted), and the secondary's pressure plus spring pulls the belt to a larger secondary radius. So a fault that blocks primary *exhaust* (a failed primary-down solenoid or valve, or a stuck feed) prevents ratio-down while ratio-up still works. A fault that blocks primary *feed* prevents ratio-up.
- INFERRED, U: Secondary pressure is the anti-slip and clamp circuit. When it is low, the classic result is **belt slip, flare and judder under load** rather than a clean "won't change ratio in one direction."

### Gaps
- OPEN: Whether every OEM uses primary-for-ratio / secondary-for-clamp. Some designs (Honda DR/DN, Toyota SLP/SLS) control both pulleys with dedicated solenoids and a balance strategy. Needs SI per unit.
- OPEN: The Gears Subaru Gen 2 page text was not read directly (blocked).

---

## 2. The official sample question pattern: reasoning through a CVT circuit diagram

### Takeaway
The learner reports the public 2026 ASE study guide has a CVT that **ratios up but won't ratio down**, with a TCM diagram showing primary up, primary down, secondary, lock-up duty solenoids and an ATF temp sensor. This matches the Subaru Lineartronic architecture. The reasoning points to **the primary-down (exhaust) side** as the most likely fault, because ratio-down requires *releasing* primary pressure. The official answer was not verifiable here.

### Cited Findings
- DOCUMENTED (snippet), official public source, A.1/A.14/A.19: The official ASE study guide includes a sample question about a CVT that "will ratio-up during a test drive but will not ratio-down," with a diagram including a "PRIMARY UP SOLENOID." — [ASE Automobile Study Guide 2025](https://www.ase.com/uploads/ASE_Automobile_Study_Guide_2025.pdf); [ASE Automobile Study Guide (current)](https://ase.com/wp-content/uploads/ASE_Automobile_Study_Guide.pdf) (direct fetch blocked; the snippet did not include the answer choices or key)
- DOCUMENTED (snippet), OEM (Subaru), A.19/A.26: The lock-up duty, primary-up, primary-down and AWD transfer clutch solenoids are **PWM** solenoids. — [Gears, "Worth Another Look! Subaru Lineartronic Failures, Faults and Fixes"](https://gearsmagazine.com/magazine/worth-another-look-subaru-lineartronic-failures-faults-and-fixes/)
- DOCUMENTED (snippet), OEM (Subaru), A.26: Primary up and primary down solenoids are about **10.0–13.5 Ω** and **normally closed**. — Gears Subaru search result cluster ([Gen 2 Valve Body](https://gearsmagazine.com/magazine/subaru-cvt-gen-2-valve-body/)). Aftermarket listings show a 10–13.5 Ω range for some TR580 solenoids ([eBay listing summary](https://www.ebay.com/itm/395961867123)), which is weak corroboration. **Needs SI.**
- DOCUMENTED (snippet), OEM (Subaru), A.17/A.19: "Most sensor and solenoid electrical failures will result in the **Secondary Line Pressure solenoid defaulting to maximum pressure**." Test resistance is quoted as 12 Ω at 68 °F. — [Gears, Subaru Lineartronic Failures](https://gearsmagazine.com/magazine/worth-another-look-subaru-lineartronic-failures-faults-and-fixes/) (**number needs SI**)

### Inferences (how to reason the circuit question)
- INFERRED, U: **Map each solenoid to a direction.**
  - Primary up (feed primary): ratio **up**.
  - Primary down (exhaust primary): ratio **down**.
  - Secondary (line/clamp pressure): slip or harshness. It does not block one ratio direction by itself. Its electrical-fail default is maximum pressure, so a failed secondary tends *not* to cause slip.
  - Lock-up duty: TCC apply/release only. Symptoms are converter shudder, no lockup, or a stall at stop if it sticks applied. It does not affect ratio.
  - ATF temp sensor: an input. A failure causes default or failsafe strategy, not a direction-specific ratio loss.
  - "Ratios up, won't ratio down" therefore implicates the **primary down solenoid or its circuit/valve**. For normally closed solenoids, that means an open control circuit or the solenoid not opening, so primary pressure can't be vented.
- INFERRED, A.26/A.27: Electrical angle (Logan's strength). On a PWM, low-side-driven normally closed solenoid, an **open** anywhere in the feed, the solenoid winding or the TCM driver leg means that solenoid never acts. Check for which circuit's open/short would kill the *down* function only. A shared power feed would kill up *and* down, so it is a distractor if both solenoids share it.
- INFERRED, trap: A choice pointing to the **secondary** solenoid or **lock-up duty** solenoid is usually a distractor for a one-direction ratio fault. A choice pointing to the **ATF temp sensor** would give failsafe behavior, not a clean one-direction loss.
- INFERRED: Mechanical or hydraulic lookalikes for the same symptom include a stuck primary-down shift valve, or (Jatco) a stepper/ratio control valve stuck toward feed. On Jatco the scan tool shows the step motor commanded position moving while the actual ratio does not follow.

### Gaps
- OPEN: The official answer key and exact choices for the ASE sample question. Read it from the public ASE PDF on an unrestricted connection. **Do not guess.**
- OPEN: Whether the Subaru solenoids are high-side or low-side driven (affects which circuit fault matters). Needs SI or wiring diagram.

---

## 3. Ratio sensing, scan-data logic and ratio DTCs

### Takeaway
The TCM computes **actual ratio = primary pulley speed / secondary pulley speed**, compares it to target, and sets ratio or pressure DTCs when they diverge. Scan data is the core diagnostic: commanded vs actual ratio, step-motor position vs ratio, and (where fitted) actual primary and secondary pressure sensors. **The TCM often blames the actuator (e.g., stepper motor) for what is really a pressure problem.**

### Cited Findings
- DOCUMENTED (snippet), U/OEM (Nissan/Mitsubishi-Jatco), A.19/A.24: The CVT control unit calculates actual speed ratio from the primary and secondary pulley speed sensors and then the deviation from target. P0730 is set when the pulley ratio exceeds the standard value, and Mitsubishi describes the condition as the TCM judging line pressure abnormal. — [Mitsubishi TechInfo, P0730 Incorrect Gear Ratio](https://mitsubishitechinfo.com/data/RE/2019/23/HTML/M123122210001200USA.htm); [Nissan 2011 Versa CVT section (nicoclub)](https://www.nicoclub.com/manuals/Versa/2011/CVT.pdf)
- DOCUMENTED (snippet), U, A.19: A failed speed sensor or its wiring can produce a false P0730 on a mechanically sound unit. Compare the input and output speed signals under the freeze-frame conditions. — [RepairPal P0730](https://repairpal.com/obd-ii-code-p0730); [Go-Parts P0730](https://www.go-parts.com/garage/obd-p0730) (secondary-tier sources)
- DOCUMENTED (snippet), OEM (Jatco), A.24: The **stepper motor PID and gear ratio PID should be mirror images**. If step position changes but ratio doesn't follow, suspect **low pressure**. Primary and secondary pressure PIDs directly measure pulley pressures. — [Gears, Jatco CVT Pressures Diagnostics](https://gearsmagazine.com/magazine/jatco-cvt-pressures-diagnostics/)
- DOCUMENTED (snippet), OEM (Jatco), A.11: "Jatco CVTs require ~140 PSI at idle" (context of line/secondary pressure). — [Gears, Jatco CVT Pressures Diagnostics](https://gearsmagazine.com/magazine/jatco-cvt-pressures-diagnostics/) (**single-source; unit/model not stated in snippet; needs SI**)
- DOCUMENTED (snippet), OEM (Jatco/Nissan), A.19: P1778 (step motor) is commonly caused by **flow control valve wear, pulley leaks, worn or sticky valve body**, not the motor. The TCM sees a ratio issue and blames the stepper, so steppers are over-replaced. — [Go-Parts P1778](https://www.go-parts.com/garage/obd-p1778); corroborated by the title and thrust of [Gears, "Stop Wasting Money on Jatco CVT Stepper Motors"](https://gearsmagazine.com/magazine/stop-wasting-money-on-jatco-cvt-stepper-motors/)
- DOCUMENTED (snippet), OEM (GM VT40/CVT250), A.17/A.19: The VT40 valve body has **six VFS solenoids and two pressure sensors**. Sensor 1 reads drive-pulley pressure and sensor 2 reads driven-pulley pressure. Solenoids 1, 2, 3, 4 and 6 are **normally high** (more current, less pressure) and solenoid 5 is **normally low**. Most P2714-type issues are actual hydraulic pressure problems rather than solenoid or sensor electrical faults. — [Gears, "Moving Right Along: VT40/CVT-250"](https://gearsmagazine.com/magazine/moving-right-along-a-look-at-the-latest-cvt-the-vt40-cvt-250/); [Gears, "Still Slipping and Sliding: VT40"](https://gearsmagazine.com/magazine/still-slipping-and-sliding-a-look-at-issues-with-the-gm-vt40-cvt/); [Go-Parts P2714 Malibu](https://www.go-parts.com/garage/obd-p2714-chevrolet-malibu-2019-2023)
- DOCUMENTED (snippet), OEM (GM), A.3: GM TSB 24-NA-009 covers P2714 on VT40, with outcomes from sticking valve body to case wear requiring transmission replacement. — [Go-Parts VT40 summary](https://www.go-parts.com/garage/gm-vt40-transmission-chevrolet-trailblazer-buick-encore-gx-2020-2025) (secondary; TSB not read)

### Inferences
- INFERRED, U: Diagnostic order is (1) fluid level and condition, (2) commanded vs actual ratio, (3) actual pulley pressures vs commanded, and (4) only then electrical actuator tests. A ratio DTC with good electrical tests points hydraulic (pump flow control, regulator bore wear, pulley seal leak).
- INFERRED, U: GM's normally-high VFS logic (the learner's 6L80 EPC notes) carries over to VT40. An open VFS circuit gives *high* pressure (failsafe), not low.

### Gaps
- OPEN: GM VT40 solenoid-by-function map (which of the six is drive pulley, driven pulley, TCC, clutches). Needs GM SI.
- OPEN: Honda CVT speed-sensor naming and DTCs.

---

## 4. Belt vs chain, starting devices, forward/reverse and auxiliary gearing

### Takeaway
Two variator elements are in use. The **Van Doorne steel push belt** (compression; Nissan/Jatco, Toyota, Honda) and the **pull chain** (tension; LuK-derived in Subaru Lineartronic and Audi Multitronic, also GM VT40 and Ford CFT30 per snippets). Most modern CVTs launch through a **lockup torque converter**. Honda historically used a **start clutch**. Toyota K120 adds a **gear-driven launch gear**. Direction change is made by a planetary set with a forward clutch and reverse brake. Jatco JF015E adds a **two-speed Ravigneaux sub-gearbox** behind the variator.

### Cited Findings
- DOCUMENTED (snippet), U, C.16: A push belt transmits force through compression, with elements pushing each other. A chain transmits force through tension. Audi Multitronic and Subaru Lineartronic are pull-chain designs using LuK technology. — [Wikipedia, Multitronic](https://en.wikipedia.org/wiki/Multitronic); [CVT.co.nz belt vs chain](https://cvt.co.nz/cvt-belt-vs-chain-whats-the-difference-and-why-it-matters/); [Autozine belt-drive CVT](https://www.autozine.org/technical_school/gearbox/Gearbox_CVT.html)
  - Note: One snippet also lists "Audi Multitronic" as a Van Doorne push-belt user. That **conflicts** with Wikipedia and the other snippets, which describe Multitronic as a chain. Treat Multitronic as chain.
  - Torque figures such as "push belt ~400 N·m / LuK chain >600 N·m" appear in one enthusiast snippet only. **Do not use** without a better source.
- DOCUMENTED (snippet), OEM (Ford CFT30), C.16: The CFT30 uses a **drive chain** whose pins contact the variator faces, not a push belt, and it is paired with a torque converter. — [Transmission Digest, "CFT30 Variator Repair"](https://www.transmissiondigest.com/cft30-variator-repair/); [MOTOR, "CVT Diagnostics" (June 2007)](https://www.motor.com/magazine-summary/cvt-diagnostics-june-2007/)
- DOCUMENTED (snippet), OEM (GM VT40), C.16: The VT40 uses a CVT **chain** rather than a belt. — [Go-Parts VT40](https://www.go-parts.com/garage/gm-vt40-transmission-chevrolet-trailblazer-buick-encore-gx-2020-2025) (secondary; Gears VT40 article likely primary, not read)
- DOCUMENTED (snippet), OEM (Toyota K120 Direct Shift-CVT), A.1: A physical **launch gear** is used from a stop, at low speed and in reverse, then drive transitions to the belt. A synchronizer engages and disengages the gear path. Toyota cites reduced belt load, a narrower belt ratio range, and belt angle reduced from 11° to 9° for faster shifts. Production began October 2018. — [Toyota Global, Direct Shift-CVT](https://global.toyota/en/mobility/tnga/powertrain2018/cvt/); [Wikipedia, Toyota K CVT](https://en.wikipedia.org/wiki/Toyota_K_CVT_transmission); [Toyota-Club.Net FAQ](https://toyota-club.net/files/faq/21-01-10_faq_cvt_en.htm)
- DOCUMENTED (snippet), OEM (Jatco JF015E / RE0F11A, "CVT7"), A.1/C.13: A **Ravigneaux** set gives a two-speed sub-transmission with a **low brake**, **high clutch** and **reverse brake**, located between the pulleys and the differential. It replaced the JF011E. — [Transmission Digest, "The New Jatco JF015E: When is a CVT not a CVT?"](https://www.transmissiondigest.com/the-new-jatco-jf015e-when-is-a-cvt-not-a-cvt/); [FenderBender, "The JF011E to the JF015E"](https://www.fenderbender.com/running-a-shop/operations/article/33027541/the-jf011e-to-the-jf015e)
- DOCUMENTED (snippet), OEM (Nissan), A.9: **P17F1** = "Transmission Judder – Clutch A – Hydraulic System Performance," meaning abnormal slip or vibration at the clutch. Under Nissan's extended coverage, P17F1 typically calls for valve body replacement and P17F0 (judder, possible belt slip) for CVT replacement. Newer Sentra/Versa (2018–2019+) got added diagnostic programming. — [Gears, Nissan CVT Judder Codes](https://gearsmagazine.com/magazine/nissan-cvt-judder-codes-and-diagnostics-what-sets-p17fx-codes-and-how-to-repair-them/); [AxleAddict P17F1](https://axleaddict.com/repair-maintenance/p17f1-cvt-judder-code)

### Inferences
- INFERRED, U: Judder from a stop can come from the **torque converter lockup/slip-lock**, a **forward clutch** (P17F1-type), or the **belt**. Road test by condition. Launch-only judder with lockup off points to clutch or converter. Judder at steady moderate load with lockup on points to lockup or belt.
- INFERRED, A.1: For "identify type" items, CVT tells are a variator (pulleys plus belt or chain), usually no multi-clutch shift schedule, and a torque converter or start device. A sub-gearbox (JF015E) or launch gear (K120) does not make it "not a CVT."

### Gaps
- OPEN: The Honda start clutch vs torque converter transition by model year. Not found; needs Honda SI.
- OPEN: The GM CVT lineup beyond VT40 (e.g., which CVT the Spark used). No reliable snippet, so not asserted.

---

## 5. Failure symptoms and causes: judder, whine, slip, ratio errors, overheat/limp

### Takeaway
Most CVT "slip/judder/ratio" complaints trace to **pressure** (pump flow control valve, regulator-bore wear, pulley seal leaks), **fluid** (wrong type, degraded, wrong level), or **wear** (belt/pulley scoring, pulley-shaft bearings making metal). Whine usually comes from bearings (road-speed-linked) or the pump (engine-speed-linked). Overheat/limp is a strategy that cuts torque on high fluid temperature.

### Cited Findings
- DOCUMENTED (snippet), OEM (Jatco JF011E), A.11/B.6: Wear of the **secondary pressure regulator valve and bore** causes uncontrolled secondary pressure, **push-belt slippage and pulley fracture**. — [Sonnax Secondary Pressure Regulator Valve Kit 15741-11K](https://www.sonnax.com/parts/1789-secondary-pressure-regulator-valve-kit); [Sonnax Oversized kit 113741-21K](https://www.sonnax.com/parts/4641-oversized-secondary-pressure-regulator-valve-kit)
- DOCUMENTED (snippet), OEM (Jatco), A.11: Low line or secondary pressure typically comes from a **sticking pump flow control valve** or a massive leak such as a damaged pulley piston seal. With DTCs P0746, P0776, P0777 and P0868, evaluate actual secondary pressure. — [Gears, Jatco CVT Pressures Diagnostics](https://gearsmagazine.com/magazine/jatco-cvt-pressures-diagnostics/) (the cluster also includes Sonnax)
- DOCUMENTED (snippet), OEM (Nissan), A.19: **P0868** (fluid pressure low) means low pressure lasted long enough to possibly slip and damage the belt. — [Gears, Nissan CVT Judder Codes](https://gearsmagazine.com/magazine/nissan-cvt-judder-codes-and-diagnostics-what-sets-p17fx-codes-and-how-to-repair-them/) (via search summary)
- DOCUMENTED (snippet), OEM (Jatco), A.9/B.4: Bearing noise in Jatco CVTs. Pitted pulley-bearing races flake metal, and the pan magnet shows "steel hair." — [Sonnax, "Chasing Bearing Noise in Jatco CVT Units"](https://www.sonnax.com/tech_resources/1-chasing-bearing-noise-in-jatco-cvt-units); [Transmission Digest, "Chasing Bearing Noise in the JF011E CVT"](https://www.transmissiondigest.com/chasing-bearing-noise-in-the-jf011e-cvt/)
- DOCUMENTED (snippet), U, A.9: Whine that tracks **road speed** points to bearings or belt. Whine present from startup that changes little with road speed points more toward the hydraulic system or pump. — [CVT.co.nz bearings guide](https://cvt.co.nz/cvt-bearings-warning-signs-diagnosis-repair-vs-replace-guide-nz/) (repair-shop blog, lower tier)
- DOCUMENTED (snippet), U, A.9/A.22: Belt judder is load-linked: it shows under moderate acceleration and disappears on overrun. It is often misdiagnosed as a misfire, mounts or CV joints. — [CVT.co.nz pulley wear](https://cvt.co.nz/cvt-pulley-wear-early-warning-signs-and-what-they-mean/) (lower tier)
- DOCUMENTED (snippet), OEM (Nissan), A.10/B.5: When fluid temperature is high, the CVT fail-safe reduces engine power until the fluid cools. Nissan bulletins exist on CVT whine and fail-safe (NTB16-109b, ITB16-045). — [NHTSA-hosted Nissan NTB16-109b](https://static.nhtsa.gov/odi/tsbs/2018/MC-10141438-9999.pdf); [NHTSA-hosted ITB16-045](https://static.nhtsa.gov/odi/tsbs/2016/MC-10119262-9999.pdf) (bulletin content not read; titles and summary only)
  - Specific trigger temperatures ("~295 °F limp on 2016+ Maxima") came from **owner forums only**. **Not usable**; needs SI.
- DOCUMENTED (snippet), U, A.4/A.10: An overfilled CVT aerates or foams, loses hydraulic integrity, runs hot and can trigger fail-safe. — Forum and blog cluster ([nicoclub Rogue CVT thread](https://forums.nicoclub.com/rogue-cvt-issues-fail-safe-and-whining-sound-fixes-t563940-120.html)). Low-tier source. The principle matches general ATF overfill knowledge, but treat it as INFERRED-strength.

### Inferences
- INFERRED, U: **Belt slip vs clutch slip vs converter slip**:
  - Belt slip shows as a ratio error. Primary speed flares while secondary speed doesn't follow, and a P0730/P17F0/P0868-type code is common.
  - Clutch slip (forward or reverse) shows as engine speed flaring against turbine/primary speed at a fixed ratio, usually at launch or engagement.
  - Converter or lockup slip shows as engine speed vs primary (turbine) speed slip in lockup.
  - Speed-sensor PIDs let you split these three. That is the CVT equivalent of the apply-chart method.
- INFERRED, U: An **overheat message with normal ratio behavior** points to cooling (cooler, warmer/thermostat, restriction, overfill), the same logic as the step-auto sample question.

### Gaps
- OPEN: Authoritative CVT fluid-temperature thresholds for fail-safe. Needs SI per OEM.
- OPEN: The Transmission Digest and Gears judder article bodies were not read.

---

## 6. Fluid: CVT-specific (never ATF) and level check

### Takeaway
CVT fluid is formulated for **steel-on-steel friction** at the belt/pulley interface plus clutch friction. Conventional ATF is not a substitute, and even different CVT fluids (Nissan NS-2 vs NS-3) are not interchangeable. Level checks are **temperature-windowed** with a scan tool and use an overflow/check plug or an OEM gauge. The temperature windows are OEM-specific.

### Cited Findings
- DOCUMENTED (snippet), U, A.4/B.12: CVT fluid friction properties are engineered for the belt against the pulleys and for a specific transmission family, so **NS-3 and NS-2 are not interchangeable**. Conventional ATF lacks the CVT friction additive and damages a CVT. — [Oils Advisor NS-2/NS-3](https://oilsadvisor.com/nissan-cvt-fluid-ns-2-and-ns-3-alternative/); [helenamulkerns NS-3](https://helenamulkerns.com/cvt-fluid-ns-3/) (both lower-tier blogs; principle corroborated by patents below)
- DOCUMENTED (snippet), U, A.4: Belt-pulley fluid tests exist specifically to select push-belt CVT fluids (steel-on-steel friction). — [ResearchGate, "Van Doorne CVT Fluid Test"](https://www.researchgate.net/publication/241402457_Van_Doorne_CVT_Fluid_Test_A_Test_Method_on_Belt-Pulley_Level_to_Select_Fluids_for_Push_Belt_CVT_Applications); [US Patent 6337309 (zinc-free CVT fluid)](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/6337309)
- DOCUMENTED (snippet), OEM (Nissan), A.4/B.12, **needs SI**: Nissan **charging-pipe method** uses a CVT Charge Pipe Cap Release (J-52611) and a CVT Oil Level Quick Check Gauge (J-51155) with fluid at **170–180 °F (77–82 °C)**. — [Transmission Digest, "Keeping the right fluid level in Nissan CVTs"](https://www.transmissiondigest.com/keeping-the-right-fluid-level-in-nissan-cvts/); [Tomorrow's Technician, Nissan CVT Fluid Level Quick Check Gauge](https://www.tomorrowstechnician.com/nissan-tech-tip-cvt-fluid-level-quick-check-gauge/); [Underhood Service (same tip)](https://www.underhoodservice.com/nissan-tech-tip-cvt-fluid-level-quick-check-gauge/)
- DOCUMENTED (snippet), OEM, A.4, **needs SI**: An **overflow-plug** method with a **95–113 °F** scan-tool temperature window appears in snippets. The attribution is mixed (forum and Toyota-style procedure), so the vehicle is unclear. — [Maxima forums](https://maxima.org/forums/8th-generation-maxima-2016/698672-how-do-i-check-cvt-fluid-level.html); [BITOG thread](https://bobistheoilguy.com/forums/threads/auto-trans-temperature-scanner-help.291392/) (**low tier; do not print numbers**)

### Inferences
- INFERRED, U, A.4: The exam pattern (sample Q1) is: no dipstick, so use the **scan-tool fluid temperature**, vehicle level, engine running, and the OEM check method. The CVT twist is that the right fluid is **CVT-specific per OEM spec**. A choice that "tops off with multi-vehicle ATF" is wrong.
- INFERRED: Wrong fluid is a root cause of judder (P17F0/P17F1-type) because belt-pulley and clutch friction depend on the additive package.

### Gaps
- OPEN: The GM VT40 fluid spec and check procedure, and Subaru and Toyota CVT fluid check windows. Needs SI.

---

## 7. Calibration data, programming and relearn after valve body/TCM replacement

### Takeaway
CVT valve bodies are often **individually characterized**. Replacing the valve body or unit usually requires **loading matching calibration data** (Nissan), **reprogramming the TCM** (GM VT40 via SPS2), and then an initialization or learn procedure. Skipping this is a classic comeback cause (judder, harsh engagement, ratio DTCs).

### Cited Findings
- DOCUMENTED (snippet), OEM (Nissan), A.25/C.6: Per NTB12-103 (multiple revisions), replacing the **CVT assembly or control valve body** requires **erasing and writing calibration data**. The calibration numbers on the disc, the QR label and the case/valve body label must all match. **TCM-only replacement follows a different procedure** that does not need this step. A memory "Erase" / initialization and a warm-up learn follow (fluid warmer than 68 °F, sequenced pedal and scan-tool steps). — [Nissan NTB12-103f](https://www.nissan-techinfo.com/documents/NTB12-103f.pdf); [Nissan NTB12-103g](https://www.nissan-techinfo.com/documents/NTB12-103g.pdf); [NHTSA-hosted NTB12-103H (May 8, 2023)](https://static.nhtsa.gov/odi/tsbs/2023/MC-10237563-0001.pdf); [NHTSA-hosted NTB12-103e](https://static.nhtsa.gov/odi/tsbs/2017/MC-10109240-9999.pdf)
- DOCUMENTED (snippet), OEM (GM VT40), A.25/C.6: VT40 **valve body or transmission replacement requires TCM reprogramming** through GM SPS2 (J2534 or MDI 2). This downloads calibration matched to the replacement unit's solenoids. — [Go-Parts VT40 guide](https://www.go-parts.com/garage/gm-vt40-transmission-chevrolet-trailblazer-buick-encore-gx-2020-2025) (secondary); related GM service document hosted at [NHTSA MC-10212918](https://static.nhtsa.gov/odi/tsbs/2022/MC-10212918-0001.pdf) (content not read)
- DOCUMENTED (snippet), cross-reference: The companion file `tcm_programming_relearn.md` lists Nissan, Toyota and Honda CVT relearns as OPEN. This section partly closes the Nissan item.

### Inferences
- INFERRED, U, A.25: The exam-level rule is: after TCM or valve body replacement on an electronically controlled CVT, **program/calibrate per SI, then perform the relearn/initialization**, and verify with a road test and scan data. Choices like "disconnect the battery to reset adapts" are wrong (see sample Q7 logic).

### Gaps
- OPEN: Subaru, Toyota and Honda CVT learn procedures. Not found in this pass.

---

## Cross-cutting source-quality note
- Strongest sources reached (snippet-level): Nissan NTBs (OEM), Mitsubishi TechInfo (OEM), Toyota Global (OEM), Transmission Digest, Gears (ATRA), Sonnax, and patents (mechanism only).
- Lower tier, used only for corroboration: Go-Parts, RepairPal, CVT.co.nz, forums, and parts listings.
- Every spec number above is attributed and flagged. None should go in a printed guide without SI: 140 psi Jatco idle, 10–13.5 Ω, 12 Ω, 170–180 °F, 95–113 °F, and Honda M4VA pulley pressures. The Honda figures (drive 28–101 psi in N at 1,500 rpm, driven 218–334 psi, start clutch 35–40 psi in D at idle) come from a [FenderBender "Tackling CVTs"](https://www.fenderbender.com/running-a-shop/operations/article/33027501/tackling-cvts?page=0%2C2) snippet only.
