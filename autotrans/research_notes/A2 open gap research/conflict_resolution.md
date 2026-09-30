# A2 Cross-File Conflict Resolution Pass

Researched 2026-09-30. **Access date for every URL below: 2026-09-30.** Scope: all 19 files in this folder, read in full. The goal was to collect every flagged conflict and every "needs verification" claim that matters, remove duplicates, search again for each one, and give it a verdict. Task numbers follow the verified 2026 map in `autotrans/research.md` (A.1–A.28, B.1–B.12, C.1–C.23).

**Method and limits.** As before, the egress proxy blocked full-page fetches, so none were tried. Everything below comes from WebSearch result text. A source seen only as a snippet is tagged **DOCUMENTED (snippet)**. No Halderman or Today's Technician text was reachable. "Textbook" below means OEM service-manual text, Sonnax/Transmission Digest/Gears, freeasestudyguides (which follows textbook wording), and aa1car, used in that order of trust. No secure ASE content was used. No question bank was built, and no spec number here was invented. Where a number appears, it is quoted from its source and should not be used as a spec without SI.

**Verdict key.**
- **RESOLVED**: the correct statement is backed by at least two independent sources, or by one OEM source plus one industry source.
- **LIKELY**: one strong source, or several weak ones that agree.
- **STILL OPEN**: needs SI, a textbook, or a primary document.

"ASE expects" says which answer a by-the-book item would most likely reward, and why. It is INFERRED from the public sample-question style in `research.md` and from the sources. It is not taken from any ASE item.

---

## Q1. What are the cross-file conflicts and open verification claims, and how does each resolve?

### Takeaway
There are 38 distinct items after de-duplication. **16 are RESOLVED**: TFT open/short, high vs. low stall, the freewheeling vs. seized stator symptom sets, permanent-DTC clearing, MIL and history erase, pan-drop fraction, the fact that P0741 thresholds are calibration-specific, the Ford solenoid ID digit count, pressure test before stall test, the flare/tie-up definitions, the modulator diaphragm leak, EPC polarity, the Allison reverse clutches, Multitronic, the 6L80 thermal bypass valve temperatures, and accumulator spring direction (resolved as design-dependent). **10 are LIKELY**, including cooler cross-contamination direction, the reason for reverse boost, the 4L60-E backward sprag, and CVT pulley roles. C3's "seized stator gives normal stall" is also LIKELY, although its symptom set is resolved. **12 are STILL OPEN**, mostly OEM numbers that ASE will not test, such as Service Fast Learn temperature windows, the brake-tap rpm rise, and drum-inspection wording.

In almost every case, what ASE tests is the direction of cause and effect: open means reads cold, high stall means clutch slip, adapts need relearning, pressure test comes first. The OEM numbers that caused most of the conflicts are not tested.

| # | Item (tasks) | Verdict | By-the-book answer in one line |
|---|---|---|---|
| C1 | TFT open vs. short reading (A.19, A.26) | RESOLVED | Open reads cold (−40); short to ground reads hot (150 °C+) |
| C2 | High stall = stator? (A.12, A.11) | RESOLVED | High stall = transmission holding element slipping; low stall = stator freewheeling, weak engine or restricted exhaust |
| C3 | Seized stator symptoms and stall (A.12) | RESOLVED (symptoms) / LIKELY (normal stall) | Normal launch, poor top end, overheating; stall reads normal |
| C4 | How far below spec means stator (A.12) | LIKELY | Far below (roughly ⅓, "30–50%") = stator; slightly low = engine. No universal rpm |
| C5 | Permanent DTC clearing (A.6, A.7) | RESOLVED | Scan tool and battery pull don't erase it; the module erases it when the monitor passes |
| C6 | MIL-off and history-erase counts (A.6) | RESOLVED | MIL off after 3 fault-free trips; history erased after 40 warm-ups (80 for misfire/fuel) |
| C7 | When freeze frame is stored (A.6) | LIKELY | Stored when the DTC is set; misfire/fuel trim take priority |
| C8 | Fluid a pan drop replaces (B.12) | RESOLVED (as a range) | Only part of it, often ~25–50%, because the converter and cooler keep fluid |
| C9 | P0741 slip threshold (A.18, A.13) | RESOLVED: no universal number | Commanded on + slip stays high = TCC not holding; the threshold is calibration-specific |
| C10 | Brake-tap rpm rise (A.13) | STILL OPEN | RPM rises on tap and falls on re-apply; no spec |
| C11 | Service Fast Learn TFT window (C.6, A.25) | STILL OPEN | Relearn inside the SI temperature window |
| C12 | SFL "after a shift-concern repair" vs. "not for a shift concern" (C.6) | LIKELY (reconciled) | Relearn follows a repair; clearing adapts isn't a repair |
| C13 | Ford solenoid body ID digit count (C.6) | RESOLVED | Depends on family: 13-digit strategy; 8-digit ID (6R140), 12-digit ID (10R) |
| C14 | Does a battery disconnect clear Ford TCM KAM? (C.6) | STILL OPEN (by model) | Use the scan-tool reset, not a battery pull |
| C15 | Cooler breach: ATF into coolant, or coolant into ATF? (B.5, A.10) | LIKELY | Both. Engine running, ATF is at higher pressure and goes into the coolant. Engine off, coolant is pressurized and goes into the ATF |
| C16 | Accumulator spring rate and shift feel (B.8, A.17) | RESOLVED: design-dependent | Faulty accumulator or broken spring = harsh shift (textbook). Stiffer spring = firmer in a 4L60-E |
| C17 | Why reverse line pressure is boosted (A.11, A.14) | LIKELY | Reverse holding members carry the highest reaction torque |
| C18 | 4L60-E backward forward sprag (C.22) | LIKELY | No drive in D (D4 and D3 takeoff); manual 2 and 1 drive through the overrun clutch |
| C19 | Drum inspection criteria (C.23) | STILL OPEN | Inspect the band surface and replace a damaged drum (inferred list) |
| C20 | Air-test pressure (C.21) | LIKELY | Low, regulated, clean dry air (Chrysler example: 30 psi); dull thud = good, hiss = leak |
| C21 | Friction soak time (C.19) | STILL OPEN | Presoak per the friction maker or SI (Alto: 15 min minimum) |
| C22 | 6L80/AF50/10L fluid-check windows (A.4, B.12) | LIKELY (6L80 30–50 °C) | Check at the SI TFT from the scan tool, level vehicle, engine idling, plug just drips |
| C23 | 6L80 thermal bypass valve opening temperature (B.5) | RESOLVED (snippet) | Original fully open ~194 °F; 21-NA-199 replacement opens 158 °F (70 °C) |
| C24 | 41TE CVI ranges (A.23, C.20) | LIKELY | L/R 35–83, 2/4 20–77, OD 75–150, UD 24–70 (SI) |
| C25 | Pressure test before stall test? (A.11, A.12) | RESOLVED | Yes. Line pressure first, and don't stall-test if pressure is low |
| C26 | Does GM publish stall tests for current units? (A.12) | STILL OPEN | Stall test only where the OEM specifies one |
| C27 | EPC polarity (A.17) | RESOLVED: design-dependent | Classic Ford/GM EPC is inverse (0 A = max pressure); read the stem |
| C28 | "Normal at idle, low at WOT = pump" (A.11) | STILL OPEN | Inferred only |
| C29 | Flare / tie-up / bind-up definitions (A.9) | RESOLVED | Flare = release before apply (rpm up). Tie-up = bind-up = overlap (output braked) |
| C30 | Ruptured modulator diaphragm (A.14, A.10) | RESOLVED (snippet) | ATF in the vacuum hose, fluid loss with no leak, white smoke |
| C31 | Audi Multitronic: belt or chain? (A.1, C.16) | RESOLVED (earlier file) | Chain |
| C32 | CVT: primary = ratio, secondary = clamp? (A.14, A.17) | LIKELY | Common design, but some units control both pulleys (SI) |
| C33 | Allison 1000 reverse clutches (A.8, A.14) | RESOLVED | R = C3 + C5; C2 isn't applied in R |
| C34 | 10R80 apply-chart cells (A.14) | STILL OPEN | Use the method, not memorized cells |
| C35 | Does tire size change TCM shift decisions? (A.22) | STILL OPEN | Recalibrate tire size and axle ratio before diagnosing |
| C36 | GM IMS/range DTC numbers (A.28, B.1) | STILL OPEN | Compare range PIDs with selector position |
| C37 | 09-07-30-004 revision letters; 4L60-E servo pin ring ID (GM) | STILL OPEN | GM-only; not ASE content |
| C38 | TCC slip "normal" at lock (A.18) | STILL OPEN (numbers) | Near zero at full lock; small steady slip is normal under controlled slip |

### Cited Findings

#### C1. TFT sensor: open reads cold, short reads hot (A.19, A.26). **RESOLVED**
Source files: `area_a_electronic_diagnosis.md` (Toyota vs. go-parts conflict).
- Toyota factory manuals: with P0713 and a −40 °C (−40 °F) reading, the circuit is open. With P0712 and 150 °C (302 °F) or more, it is shorted. Below 79 Ω, the ECM shows 150 °C+ regardless of the actual temperature. The sensor is an NTC whose resistance and voltage fall as temperature rises. — DOCUMENTED (snippet), OEM: [Toyota A750E RM](https://www.purefjcruiser.com/docs/2007%20Toyota%20FJ%20Cruiser%20Repair%20Manual/A750E%20Automatic%20Transmission/Automatic%20Transmission%20System/0160014.pdf); [Toyota UB80F RM (Mitchell)](https://estimateca.mymitchell.com/t3Portal/document/rm/RM3510U/xhtml/RM100000001ETSD.html?linkId=d4849e770&hashId=RM100000001ETSD); SAE titles P0712 "Low Input" / P0713 "High Input" at [obd-codes P0712](https://www.obd-codes.com/p0712), [obd-codes P0713](https://www.obd-codes.com/p0713).
- The contrary claim ("a short reads −40") still circulates in go-parts/aggregator text: [go-parts P0712](https://www.go-parts.com/garage/obd-p0712). It is wrong for a pull-up NTC circuit.
- **ASE expects:** open (or high signal voltage) = reads very cold. Short to ground (low signal voltage) = reads very hot. That follows from the standard pull-up/voltage-divider circuit, which fits Logan's electrical strength.

#### C2. High stall means a slipping holding element, not the stator (A.12, A.11). **RESOLVED**
Source files: `hydraulic_pressure_testing.md` (flagged conflict), `stator_owc_diagnosis.md` (the "200 rpm above = stator" flashcard).
- OEM (Mitsubishi) stall table: higher than spec means a transaxle clutch or overrunning clutch is slipping. Lower than spec means low engine output or a faulty converter, so check the engine first. — DOCUMENTED (snippet): [Mitsubishi SI stall test](https://mitsubishitechinfo.com/data/RE/2019/23/HTML/M123100540066300USA.htm); [newtonnet (Mitsubishi) Converter Stall Test](https://www.newtonnet.co.uk/coupe/service/webtech/iindex.asp@id=12164).
- Textbook-style: above spec, clutches and bands are slipping. Below spec, the stator OWC is slipping or the exhaust is restricted. — DOCUMENTED (snippet): [freeasestudyguides stall test](https://www.freeasestudyguides.com/torque-converter-stall-test.html); [aa1car Torque Converter Basics](https://www.aa1car.com/library/torque_converters.htm).
- The "200 rpm above spec = stator" card ([Quizlet](https://quizlet.com/481410090/at-414-auto-transmission-21-flash-cards/), [Brainscape](https://www.brainscape.com/flashcards/automatic-transmissions-1273406/packs/2531089)) contradicts the OEM tables. Discard it.
- **ASE expects:** high stall = a slipping band, clutch or transmission OWC in the tested range (compare D and R to find the shared element). Low stall = a freewheeling stator, or an engine that isn't making power, including a restricted exhaust. Rule out the engine first.

#### C3. Seized stator: symptom set and stall reading (A.12). **Symptoms RESOLVED; "normal stall" LIKELY**
Source files: `stator_owc_diagnosis.md`, `hydraulic_pressure_testing.md` (both OPEN on the textbook statement).
- A seized sprag gives satisfactory early acceleration but prevents normal cruise speed and builds heat fast, bluing the converter. Stuck locked gives poor high-speed performance and converter overheating. — DOCUMENTED (snippet): [freeasestudyguides, Overrunning One Way Stator Clutch](https://www.freeasestudyguides.com/diagnose-one-way-stator-clutch.html); [MOTOR, Torque Converter Lock-up (1999)](https://www.motor.com/magazine-summary/torque-converter-lock-may-1999/); [aa1car](https://www.aa1car.com/library/torque_converters.htm) (lack of power at highway speed, overheating).
- Normal stall with a seized stator: no source states it in words. It follows from the mechanism, because at stall a good stator is held anyway, so a locked one behaves the same. **Conflicting snippet:** the MOTOR 1999 result summary contained "a stall flash low indicates a seized stator and engine down on power." That contradicts the mechanism and every other source. It looks garbled ("seized" in place of "slipping"), so don't use it.
- **ASE expects:** the public sample item (poor launch, normal above 35 mph) points to a **freewheeling** stator. The mirror image (good launch, poor top speed, overheating, normal stall) is a **seized** stator. That pairing is the standard textbook contrast.

#### C4. How far below spec means a stator (A.12). **LIKELY**
Source files: `hardest_topics_and_strategy.md` (aa1car "30–50%"), `stator_owc_diagnosis.md` (no universal margin).
- aa1car: when stall is 30–50% below normal (roughly a third lower), a freewheeling stator almost always causes it. — DOCUMENTED (snippet), single source: [aa1car](https://www.aa1car.com/library/torque_converters.htm).
- A "250–350 rpm below" band sometimes attributed to textbooks did not surface in any search. — [search result set, e.g. JEGS converters](https://helpcenter.jegs.com/hc/en-us/articles/115012167348-Torque-Converters) (no match).
- **ASE expects:** qualitative reasoning. Moderately low stall means check the engine first. Very low stall with a poor launch means the stator. If an item gives numbers, it will also give the spec.

#### C5. Permanent DTC clearing rules (A.6, A.7). **RESOLVED**
Source files: `area_a_electronic_diagnosis.md`, `textbook_vs_shop.md`.
- Two paths, both from CARB rules as industry sources report them:
  - **Self-heal path.** The MIL goes out after three consecutive fault-free cycles, and the PDTC is erased at the start of the fourth.
  - **After a scan-tool clear.** The confirmed DTC clears, but the PDTC stays until one driving cycle in which the monitor runs and passes, with more than 10 minutes total run time and more than 5 minutes above 25 mph (40 km/h).
  
  — DOCUMENTED (snippet): [Underhood Service, Ford PDTCs](https://www.underhoodservice.com/ford-permanent-diagnostic-trouble-codes-dtcs/); [Auto Service World, First Look at PDTCs](https://www.autoserviceworld.com/features/taking-a-first-look-at-permanent-dtcs/); [CARB 13 CCR 1968.2 (regulation text)](https://ww2.arb.ca.gov/sites/default/files/barcu/regact/obd02/fro1968-2.pdf) (MIL-off after three sequential passing cycles).
- A scan tool or battery disconnect can't erase a PDTC. — DOCUMENTED (snippet): [Underhood Service, Using Readiness Monitors](https://www.underhoodservice.com/using-readiness-monitors-to-verify-emissions-repairs/); [California BAR PDTC workshop](https://www.bar.ca.gov/pdf/pdtc-workshop-presentation-4.18.2018.pdf) (from the earlier file).
- **ASE expects:** clear with a scan tool (public sample question), then verify the repair by running the monitor or drive cycle. A PDTC isn't removed by clearing codes or by a battery pull.

#### C6. MIL-off and history-erase counts (A.6). **RESOLVED**
- MIL off after three consecutive trips without the fault. A history DTC and its freeze frame self-erase after 40 warm-up cycles, or **80 for misfire and fuel-system faults**. — DOCUMENTED (snippet): [ALLDATA OBD II System Operation](http://repair.alldata.com/online2help/techRef/Accessing,_Interpreting_and_Clearing_DTCs/OBDII_Overview/Introduction/OBDII_System_Operation/Additional_OBD_II_System_Operation.htm); [RLEscalambre OBD II terminology](https://www.rlescalambre.net/obd-ii-terminology-1-1); earlier-file sources [Jeep WK OBD](https://jeepspecs.com/models/jeep-grand-cherokee/jeep-grand-cherokee-wk/on-board-diagnostic-systems/).
- Correction to `area_a_electronic_diagnosis.md`: add the 80-warm-up exception for misfire and fuel system.

#### C7. When freeze frame is stored (A.6). **LIKELY**
- Freeze frame is captured when the DTC is set, not when the problem started. Misfire and fuel-trim freeze frames have priority and overwrite others. — DOCUMENTED (snippet): [ALLDATA OBD II](http://repair.alldata.com/online2help/techRef/Accessing,_Interpreting_and_Clearing_DTCs/OBDII_Overview/Introduction/OBDII_System_Operation/Additional_OBD_II_System_Operation.htm); [OBD Auto Doctor freeze frame](https://www.obdautodoctor.com/tutorials/obd-freeze-frame-explained/).
- The 1998 MOTOR note (GM/Ford store freeze frame when the MIL lights; Chrysler on the first failure) is dated and manufacturer-specific. Don't teach it as a rule.

#### C8. How much fluid a pan drop replaces (B.12). **RESOLVED as a range**
Source files: `area_b_in_vehicle.md` ("30–50%" vs. "¼–⅓"), `gm_failure_patterns.md` (8L exchange).
- A drain and fill replaces only part of the fluid. Examples: about 3 of 12 quarts (~25%); "15–50% new fluid" dilution; one vehicle at ~64% new after a drain and fill. A machine exchange reaches 95–99%. The converter keeps much of the old fluid. — DOCUMENTED (snippet): [US Patent 5291968](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/5291968); [BITOG, fluid remaining after drain and fill](https://bobistheoilguy.com/forums/threads/post-how-much-fluid-remains-in-trany-torque-converter-during-a-drain-and-fill.326593/); [K&K Richardson](https://www.kkrichardson.com/kwik-blog/transmission-flush-vs-drain-and-fill) (earlier file).
- GM's 8L TSB 18-NA-355 needs an exchange procedure because a drain and fill doesn't reach enough new-fluid concentration: [GM Authority](https://gmauthority.com/blog/2019/08/tsb-seems-to-fix-8-speed-automatic-gm-transmission-problems/) (earlier file).
- **ASE expects:** "a pan drop replaces only a portion; the converter, cooler and lines retain fluid." Don't pick a single percentage.

#### C9. P0741 slip thresholds (A.18, A.13). **RESOLVED: no universal number exists**
Source files: `area_a_electronic_diagnosis.md`, `area_a_mech_hydraulic_diagnosis.md`, `tcc_diagnosis.md`, `gm_failure_patterns.md`, `scan_tool_bidirectional.md` (">200", "~100", "0–50/50–200/200+", GM "<100").
- GM set criteria vary by model and year. Examples: slip > 180 rpm for 7 s; ≥ 130 rpm for 20 s, three times (2004 Suburban); > 80 rpm for 15 s. The PCM sets P0741 when it sees high slip while the TCC is commanded on. — DOCUMENTED (snippet): [autocodes P0741 GMC](https://www.autocodes.com/p0741_gmc.html); [JustAnswer 2004 Suburban](https://www.justanswer.com/chevy/5eptn-2004-suburban-torque-converter-clutch-circuit-performace-stuck-heck.html); [Sonnax, Beyond 1870](https://www.sonnax.com/tech_resources/120-beyond-1870-gm-converter-codes-p0741-p0742-and-1887).
- The 0–50/50–200/200+ "bands" come only from an aggregator ([apextechnation](https://apextechnation.com/articles/p0741-torque-converter-clutch-code)). Don't use them.
- **ASE expects:** TCC commanded on and slip stays high means the TCC isn't holding. Check apply pressure and leaks (valve bores, stator-support bushing, turbine-shaft seal) before condemning the converter. Any threshold will be given in the stem.

#### C10. Brake-tap rpm rise (A.13). **STILL OPEN**
- Sources quote 100–200, 200–300 and ~400 rpm ([LiveAbout](https://www.liveabout.com/diagnosing-gm-converter-lock-up-problems-262653); [Roadrunner Converters](https://www.roadrunnerconverters.com/testing-diagnosing-torque-converters/)). The rise depends on gear, load and converter, so no spec exists. **ASE expects** only the direction: rpm rises when the TCC releases and falls when it re-applies.

#### C11. Service Fast Learn temperature windows (C.6, A.25). **STILL OPEN**
Source files: `tcm_programming_relearn.md`, `gm_failure_patterns.md`, `textbook_vs_shop.md`.
- 6L family: TFT 70–115 °C in one GM-derived document and 70–100 °C in another. — DOCUMENTED (snippet): [GM TB #1392 (forum-hosted)](https://www.e90post.com/forums/attachment.php?attachmentid=3482186&d=1718730748); [GM Doc ID 1688788 (forum-hosted)](https://www.gm-trucks.com/forums/applications/core/interface/file/attachment.php?id=106422); [VRE 6L80 sheet (158–212 °F)](https://static.summitracing.com/global/images/instructions/vre-8100a-jmb.pdf). Sonnax gives 75–85 °C "depending on current TCM programming" ([Sonnax Fast Learn tips](https://www.sonnax.com/tech_resources/1322-tips-for-success-with-the-gm-transmission-fast-learn-process)). The 8L TechLink gives an abort window of 55–96 °C ([corvetteactioncenter TechLink](https://www.corvetteactioncenter.com/tech/knowledgebase/print-1380.html)).
- These are probably different calibrations and different kinds of limit (window to start vs. window to abort). Only GM SI for the VIN resolves it. **ASE expects** only that relearns have a fluid-temperature precondition; no number will be tested.

#### C12. SFL after a shift-concern repair vs. "don't SFL for a shift concern" (C.6). **LIKELY (reconciled)**
- GM TechLink: clearing and relearning adapts "should not be considered a repair process". If there is a specific shift concern, don't perform SFL; use the driving learn. The trigger lists include "any service in response to a shift quality concern." — DOCUMENTED (snippet): [TechLink repost](https://www.cadillacvnet.com/forums/threads/gm-techlink-transmission-adaptive-functions.1132/); [GM bulletin via NHTSA MC-10178286](https://static.nhtsa.gov/odi/tsbs/2020/MC-10178286-9999.pdf); [Sonnax](https://www.sonnax.com/tech_resources/1322-tips-for-success-with-the-gm-transmission-fast-learn-process).
- Reconciliation (INFERRED): SFL follows a *repair* done for a shift concern. SFL used as the fix itself is what GM rules out.
- **ASE expects:** relearn after the TCM, valve body or transmission is replaced or repaired. Resetting adapts is not a repair for a worn or leaking unit.

#### C13. Ford solenoid body ID digit count (C.6). **RESOLVED**
Source file: `tcm_programming_relearn.md` (8 vs. 12 vs. 7).
- 10R80: the service kit tag carries a **12-digit solenoid body ID and a 13-digit solenoid body strategy**. Only the 13-digit strategy is entered; entering the 12-digit ID gives a partial download. — DOCUMENTED (snippet): [Transmission Digest, 10R80/10L90 Solenoid Function](https://www.transmissiondigest.com/10r80-10l90-10-speed-solenoid-function/); [Gears, 10R solenoids](https://gearsmagazine.com/magazine/direct-connection-10r60-10r80-and-10r140-solenoids-make-shifts-happen/).
- 6R140: 13-digit strategy plus an 8-digit ID. — DOCUMENTED (snippet): [Transmission Digest TASC Force (6R140)](https://www.transmissiondigest.com/tasc-force-tips-4/); [Sonnax 6R140](https://www.sonnax.com/tech_resources/848-6r140-transmission-solenoid-strategy-code-don-t-break-up-the-band).
- The "7 digit" figure was a single forum post. Verdict: the ID length depends on the family, and the 13-digit strategy is the constant. **ASE expects** only the principle: load the solenoid/valve-body characterization data after replacing it.

#### C14. Does a battery disconnect clear Ford TCM KAM? (C.6). **STILL OPEN (by model)**
- Forum reports on Super Duty/IDS say a battery disconnect does **not** clear TCM KAM; use IDS/PDS "Reset KAM." — DOCUMENTED (snippet), forum: [PowerstrokeArmy](https://powerstrokearmy.com/threads/tcm-adaptive-learning-reset-ford-ids.81682/); [Ford Raptor Forum](https://www.fordraptorforum.com/threads/can-tcm-relearn-bad-habits.69097/). The Ford owner-manual wording that the transmission relearns after a battery disconnect ([Ford owner manual](https://www.fordservicecontent.com/Ford_Content/vdirsnet/OwnerManual/Home/Content?variantid=2926&languageCode=en&countryCode=USA&Uid=G1592460&ProcUid=G1592461&userMarket=usa&div=f&vFilteringEnabled=False&buildtype=web)) likely applies to other modules or years.
- **ASE expects:** reset adapts with the scan tool. The public sample question already treats "disconnect the battery" as the wrong way to clear things.

#### C15. Cooler breach: ATF into coolant, or coolant into ATF? (B.5, A.10). **LIKELY: both, depending on engine state**
Source files: `area_b_in_vehicle.md` (OPEN), `area_a_mech_hydraulic_diagnosis.md`.
- Cooler-line ATF pressure with the engine running can reach about 60 psi (pump-generated). With the engine off, transmission pressure is zero while the cooling system holds about 16 psi, which pushes coolant into the transmission lines. — DOCUMENTED (snippet), forum/technician level: [Ford-Trucks forum, cooler leaking coolant](https://www.ford-trucks.com/forums/1361007-transmission-cooler-leaking-coolant.html); [BITOG, cooler leak](https://bobistheoilguy.com/forums/threads/transmission-cooler-leak-bad.267843/).
- Both outcomes are documented: ATF in the coolant (pink, foamy coolant; [GMB](https://gmb.net/blog/oil-in-the-coolant/)) and glycol in the ATF (friction bond damage, shudder; [Gears/Acustrip June 2014](https://www.acustrip.com/res/pdf/CoolantContamination.pdf); [GM bulletin MC-10234619](https://static.nhtsa.gov/odi/tsbs/2023/MC-10234619-0001.pdf), which recommends a glycol test kit before radiator replacement).
- Why LIKELY and not RESOLVED: the pressure mechanism rests on technician forums. The pressures are consistent with general knowledge, but no textbook states it.
- **ASE expects:** milky or pink ATF means coolant contamination from the in-radiator cooler. The repair is to replace the radiator or cooler, overhaul the transmission (seals, frictions, converter) and flush. "Flush and refill" alone is the distractor.

#### C16. Accumulator spring rate and shift feel (B.8, A.17). **RESOLVED: design-dependent**
Source files: `hydraulic_valves_circuits.md` (CONFLICT/OPEN), `area_b_in_vehicle.md` (slide-bump).
- 4L60-E: the Sonnax enhanced 1-2 accumulator spring gives **firmer** 1-2 shifts. In 1994-and-later units it must be installed against the separator plate, **or a softer-than-OE shift results**. So orientation and design decide the direction. — DOCUMENTED (snippet): [Sonnax 77704S](https://www.sonnax.com/parts/2433-enhanced-performance-accumulator-spring); [Sonnax 74926](https://www.sonnax.com/parts/1660-1-2-or-3-4-accumulator-spring).
- A broken spring can make shifts firmer or softer depending on which spring breaks and which side it sits on. — DOCUMENTED (snippet), forum: [TCCoA broken accumulator spring](https://www.tccoa.com/threads/broken-accumulator-spring.130878/). The textbook line is "a faulty accumulator or broken spring causes harsh shifts" ([freeasestudyguides, faulty accumulator](https://www.freeasestudyguides.com/transmission-shift-troubleshooting.html)). The rate of pressure rise sets shift feel ([Sonnax Hydraulics Fundamentals II](https://www.sonnax.com/tech_resources/675-hydraulics-fundamentals-part-ii-accumulators-shift-feel)).
- **ASE expects:** a harsh single shift points to that shift's accumulator (broken spring, stuck piston, leaking seal). Don't memorize a spring-rate direction unless the stem gives the layout.

#### C17. Why reverse line pressure is boosted (A.11, A.14). **LIKELY**
Source file: `hydraulic_valves_circuits.md` (the design reason was OPEN).
- The reverse holding element (band or clutch) must resist a reaction torque on its planetary member that can exceed 3× engine torque, so line pressure is raised in R. — DOCUMENTED (snippet), low-authority source: [Industrial Monitor Direct](https://industrialmonitordirect.com/blogs/knowledgebase/reverse-line-pressure-in-automatic-transmissions-why-its-higher). A Nissan-style patent says servo pressure "has to be high enough to meet the demand imposed on the low-reverse band brake" (reverse circuit): [US 4306469](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/4306469) (snippet). The boost mechanism (reverse oil on the spring end of the PR valve) is documented in [US 6619323](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/6619323) (earlier file).
- **ASE expects:** reverse needs more holding force, so reverse oil acts on the boost valve and raises line pressure. Low pressure in R only means a reverse-circuit leak or a boost-valve fault. Low pressure everywhere means supply (pump, PR, filter).

#### C18. 4L60-E backward forward (input) sprag (C.22, A.8). **LIKELY**
Source files: `area_c_overhaul.md` (forum-only), `apply_chart_reasoning.md`.
- Backward forward sprag: it acts like neutral in **D4 and D3**, while manual 2 and 1 still move (weakly), because the overrun clutch carries the load. — DOCUMENTED (snippet), forum (several threads agree): [LS1Tech rebuild no drive](https://ls1tech.com/forums/automatic-transmission/1978622-4l60e-rebuild-no-drive-but-have-reverse-manual-1st-2nd.html); [SilveradoSierra "No D,3 from takeoff but can manual shift"](https://www.silveradosierra.com/threads/4l60e-no-d-3-from-takeoff-but-can-manual-shift-d-3-2-1.730573/); [GMT400 no first after rebuild](https://www.gmt400.com/threads/4l60e-no-first-gear-in-drive-after-rebuild.56146/).
- This fits the stock overrun-clutch schedule: the overrun clutch is applied in manual 3, 2 and 1 but not in D4, and in D3 it is on only in 3rd gear in stock form (so a D3 takeoff has no overrun clutch). — DOCUMENTED (snippet), forum/rebuilder: [LS1Tech overrun clutch](https://ls1tech.com/forums/automatic-transmission/1970382-overrun-clutch-4l60e.html); [Sonnax 4L60E HP/HD build guide](https://www.sonnax.com/tech_resources/617-4l60e-performance-heavy-duty-transmission-build-guides) (performance versions add overrun apply in D3 1st/2nd).
- **ASE expects:** the principle. A backward OWC gives no drive in the range it carries and still drives in ranges where a parallel friction element holds. It can also cause a tie-up (Sonnax lists "one-way element installed backward" as a bind-up cause: [Sonnax terms](https://www.sonnax.com/tech_resources/175-transmission-terms-from-a-to-z)). Bench-check rotation direction before installing.

#### C19. Drum inspection criteria (C.23). **STILL OPEN**
Source file: `area_c_overhaul.md` (only brake-drum sources found).
- Transmission-specific snippets found: soft-iron drums have a dimpled surface and hard drums a smooth one; a worn band leaves a gap and slips. — DOCUMENTED (snippet): [freeasestudyguides, brake bands](https://www.freeasestudyguides.com/transmission-brake-band.html). No transmission source gave drum reject criteria (scoring, glazing, heat checks, out-of-round) this session. The brake-drum criteria ([Meritor](https://cbsparts.ca/admin/bulletins/trouble_shooting_brake_drum_wear_by_meritor.pdf)) are not A2 sources.
- **ASE expects (INFERRED):** inspect band and drum together. Replace a drum that is scored, glazed, heat-discolored, distorted, or has damaged splines, bushing or check ball. Replace a band that is burned, worn to the grooves or delaminated. Confirm the wording against Halderman or Today's Technician.

#### C20. Air-test pressure (C.21). **LIKELY**
- Chrysler 42RLE SI: about 30 psi, clean and dry air, listen for a "slight thud"; large air escape means disassemble. Generic sources give 20–50 psi, and a 40 psi maximum is mentioned to protect seals. — DOCUMENTED: [Jeep JK SI mirror (fetched in an earlier session)](https://s3.amazonaws.com/jeepwranglerjk2010/7c033609.html); [freeasestudyguides pressure tests](https://www.freeasestudyguides.com/automatic-transmission-pressure-tests.html) (snippet).
- **ASE expects:** low, regulated, clean, dry air. A dull thud or apply is good; hissing means a leaking seal or ring.

#### C21. Friction soak time (C.19). **STILL OPEN**
- Alto gives a 15-minute minimum; a rebuilder blog says 30 minutes; Raybestos says only "presoak" (earlier-file sources). No new source was found. **ASE expects:** soak new frictions in the specified ATF before assembly.

#### C22. No-dipstick fluid-check windows (A.4, B.12). **LIKELY (per unit)**
- 6L80/6L90: TFT 30–50 °C (86–122 °F), level vehicle, engine idling, shift through the ranges, fluid drips from the level-control plug; a steady stream means overfull. — DOCUMENTED (snippet): [Run-Rite CPTB0059](http://run-rite.com/wp-content/uploads/2023/11/CPTB0059.pdf); [EFILive 6L80E](https://efilive.co.uk/6l80e-fluid-check.html). AF50: 35–45 °C ([Gears AF50](https://gearsmagazine.com/magazine/gms-af50-8-speed-transmission-fluid-level-and-condition-check/)). The 10L80 75–80 °C figure is forum-level only.
- **ASE expects** the procedure (public sample item): scan-tool TFT inside the SI window, vehicle level, engine running, and the specified plug or method. No number.

#### C23. 6L80 thermal bypass valve temperatures (B.5). **RESOLVED (snippet)**
- The original TBV was not fully open until 194 °F. The 21-NA-199 replacement (stamped "70", P/N 86774933) opens at 158 °F. 22-NA-182 also cites 158 °F (70 °C). — DOCUMENTED (snippet): [gm-trucks 21-NA-199 thread](https://www.gm-trucks.com/forums/topic/256594-6l80e-thermostatic-bypass-valve-replacement-and-bulletin-21-na-199/); [SilveradoSierra 70 °C TBV review](https://www.silveradosierra.com/threads/70-c-158-f-thermal-bypass-valve-review.743498/); [GMTruckClub](https://www.gmtruckclub.com/threads/transmission-6l80e-6-speed-lower-fluid-temp-upgrade.1473466/); [GM bulletin MC-10242240 (22-NA-182)](https://static.nhtsa.gov/odi/tsbs/2023/MC-10242240-0001.pdf) (earlier file). The "at least 180 °F" forum claim is unsupported. The existence of 21-NA-199 is now corroborated by several threads, but the bulletin text wasn't read.
- **ASE expects:** a TBV stuck in bypass (no cooler flow) causes overheating, and fixing it is part of B.5 cooler-circuit checks. No temperature.

#### C24. 41TE CVI ranges (A.23). **LIKELY**
- `apply_chart_reasoning.md` gives OD 75–135 and L/R 35–85; `scan_tool_bidirectional.md` gives OD 75–150 and L/R 35–83. A new search returns **L/R 35–83, 2/4 20–77, OD 75–150, UD 24–70**. — DOCUMENTED (snippet): [Motor Age/VehicleServicePros, Fundamentals or Forgetamentals Part 3](https://www.vehicleservicepros.com/service-repair/underhood/article/21183426/fundamentals-or-forgetamentals-part-3-chrysler-and-dodge); [MOTOR, Transmission as a Second Language](https://www.motor.com/magazine-summary/transmission-as-a-second-language/). The apply-chart file's figures are probably a transcription variant. Chrysler-only, so SI.

#### C25. Pressure test before stall test (A.11, A.12). **RESOLVED**
Source files: `hydraulic_pressure_testing.md` (says yes), `textbook_vs_shop.md` (called it "not universal").
- "Perform the line pressure test before performing the Stall test. If the line pressure is low at Idle, DO NOT perform the Stall test." — DOCUMENTED (snippet): [ATSG Ford 4R100 manual p.21](https://www.manualslib.com/manual/1189091/Atsg-Ford-4r100.html?page=21); [1996 Bronco/F-Series SI](https://www.diesel-dave.com/vehic/manual/stj/stj71a21.htm); [Chrysler-style diagnosis PDF](https://www.justanswer.com/uploads/kennyz1963/2008-12-29_043754_line.pdf). The 5-second WOT limit appears in the same set and in Subaru SI ([Subaru 4AT stall test](http://ken-gilbert.com/wrx/STi_Manual/04.%20TRANSMISSION/02.%20AUTOMATIC%20TRANSMISSION/05.%20Stall%20Test.pdf)).
- **ASE expects:** fluid check, then line pressure, then stall test (if the OEM specifies one), with a 5 s WOT limit and a cool-down between ranges. `textbook_vs_shop.md` C7 is overcautious: several OEM manuals do state the order.

#### C26. Does GM publish stall tests for current units? (A.12). **STILL OPEN**
- `hardest_topics_and_strategy.md` says "many OEMs, GM included, no longer publish stall tests." `stator_owc_diagnosis.md` and `textbook_vs_shop.md` call it unverified. A new search returned only forum threads ([SilveradoSierra 6L80 thread](https://www.silveradosierra.com/threads/gm-6l80-transmission-information-thread.753826/)). GM SI must settle it. Don't state it as fact.

#### C27. EPC polarity (A.17). **RESOLVED: design-dependent**
- Ford EPC and GM 4L60-E PCS are inverse: 0 A (unplugged) gives maximum pressure and ~1.1 A gives minimum. GM 8L90 and VT40 have both normally-high and normally-low VFS. — DOCUMENTED (snippet): [freeasestudyguides EPC](https://www.freeasestudyguides.com/transmission-electronic-pressure-control.html); [ls2.com GM scan-data definitions](https://www.ls2.com/boggs/a4/transcantooldatadefinitions.htm); [Gears 8L90 solenoid strategies](https://gearsmagazine.com/magazine/8l90-solenoid-strategies/) (earlier files).
- **ASE expects:** the classic textbook EPC (more current means less pressure; unplugged means maximum pressure and harsh engagement) unless the stem describes another design.

#### C28. "Normal at idle, low at WOT = worn pump" (A.11). **STILL OPEN**
- A search found no transmission source, only fuel- and oil-pump analogies. It remains INFERRED (a worn pump can't keep up with demand, or a leak grows with pressure). Don't print it as documented.

#### C29. Flare, tie-up and bind-up definitions (A.9, A.23). **RESOLVED**
Source files: `textbook_vs_shop.md` (splits tie-up from bind-up), `area_a_mech_hydraulic_diagnosis.md`, `shift_phases_adapts.md`, `gm_failure_patterns.md`.
- Sonnax glossary: **bind-up is also called excessive clutch overlap or tie-up**. The unit drives at two ratios at once, and the causes are apply/release timing or a one-way element installed backward or not free to freewheel. **Flare**: an element releases before the oncoming one holds, so rpm rises. — DOCUMENTED (snippet): [Sonnax, Transmission Terms A to Z](https://www.sonnax.com/tech_resources/175-transmission-terms-from-a-to-z); consistent with the tie-up patents [US 7559873](https://patents.google.com/patent/US7559873B2/en) and [US 5046175](https://www.freepatentsonline.com/5046175.html).
- `textbook_vs_shop.md` Q4 treats tie-up and bind-up as different things (output braked vs. oncoming early). Sonnax treats them as synonyms, and the diagnosis is the same.
- **ASE expects:** flare means rpm rises, from underlap or low apply pressure. Tie-up/bind-up means the output drags and feels braked, from overlap or a late-releasing element.

#### C30. Ruptured vacuum modulator (A.14, A.10). **RESOLVED (snippet)**
- A ruptured diaphragm lets the engine draw ATF through the vacuum hose. Signs: ATF in the hose at the modulator, fluid loss with no visible leak, white or blue-white smoke, and shift-feel changes. Test with a hand vacuum pump or check the hose for fluid. — DOCUMENTED (snippet): [Sun Transmissions, modulator valve](https://suntransmissions.com/blogs/news/what-is-a-transmission-modulator-valve-and-what-function-does-it-perform); [Oards modulator symptoms](https://oards.com/bad-vacuum-modulator-replacement-cost/); [El Camino Central TH350](https://www.elcaminocentral.com/threads/t-h-350-trans-modulator-engine-smoke.7790/) (forum). This closes the OPEN in `hydraulic_valves_circuits.md` §9.

#### C31. Audi Multitronic: belt or chain (A.1, C.16). **RESOLVED**
- It is a LuK pull chain ([Wikipedia Multitronic](https://en.wikipedia.org/wiki/Multitronic); [CVT.co.nz](https://cvt.co.nz/cvt-belt-vs-chain-whats-the-difference-and-why-it-matters/)), as `cvt_diagnosis.md` concluded.

#### C32. CVT: primary pulley = ratio, secondary pulley = clamp (A.14, A.17). **LIKELY**
- Primary pulley pressure regulates the ratio. The secondary pulley gets pressure "sufficient to prevent slippage of the belt" (clamping force). — DOCUMENTED (snippet), patents: [US 5168778](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/5168778); [US 7201684](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/7201684); [US 7435200](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/7435200). Honda and Toyota designs command both pulleys through separate solenoids (earlier file), so the split varies by design.
- **ASE expects** (for the public CVT sample question): a one-direction ratio fault points to the primary pulley circuit for that direction. Low secondary pressure means belt slip.

#### C33. Allison 1000 reverse clutches (A.8, A.14). **RESOLVED**
- Reverse = C3 + C5; C2 is not applied in reverse. — DOCUMENTED (snippet): [Weber State ASEP apply chart](https://www.weber.edu/wsuimages/automotive/asep/allison%201000%20clutch%20application%20chart.pdf); [Transmission Technologies chart](https://transmissiontechnologies.com/allison-1000-clutch-apply-chart.aspx). The claim that "C2 handles reverse" (`gm_failure_patterns.md`) is wrong.

#### C34–C38. Remaining OEM-detail items. **STILL OPEN**
- **C34, 10R80 cells:** the Ranger5G chart puts 5 elements in 8th gear, so it contains an error ([Ranger5G](https://www.ranger5g.com/forum/threads/my-research-into-the-10r80-shift-strategy.26732/)). Needs SI. ASE tests the intersection method, not the cells.
- **C35, tire size and TCM:** forums conflict, and HP Tuners rescales shift tables ([HP Tuners](https://www.hptuners.com/articles/gear-tire-adjustment-guide-for-vcm-suite/)). ASE expects the tire size and axle ratio calibration to match the hardware before diagnosing.
- **C36, GM IMS/range DTCs:** P1825, P1819 (4L60-E), P182E (6L80) and P1915 (6T70) come from consumer or single sources. Needs SI. ASE tests PID-vs-selector logic.
- **C37:** the 09-07-30-004 revision letters and the 4L60-E servo-pin ring coding (3 rings shortest?) are GM/forum only, and not ASE content.
- **C38, "normal" TCC slip at lock:** a GM document gives <100 rpm for one unit ([GM MC-10181692](https://static.nhtsa.gov/odi/tsbs/2020/MC-10181692-9999.pdf)); 6L80 forums say 0–50 rpm. Controlled-slip strategies (EC3) are normally non-zero ([VehicleServicePros 4L60-Evolution](https://www.vehicleservicepros.com/service-repair/underhood/article/21182663/4l60-evolution)). ASE expects near zero at full lock, and slip that follows desired slip.

### Inferences
- INFERRED: Nearly every conflict falls into one of two kinds. (a) **Garbled or low-authority study material that reverses a direction.** Examples: TFT short reads cold, high stall = stator, "stall low = seized stator," C2 applied in reverse. The OEM or rebuilder source wins each time, and the correct direction is the one ASE tests. (b) **OEM numbers that differ between units or calibrations.** Examples: SFL windows, fluid-check windows, P0741 thresholds, CVI ranges, Ford ID digits, brake-tap rpm. These don't need resolving for ASE. Learn the principle and take any number from the stem.
- INFERRED: The fixes worth carrying into a guide:
  - Add the 80-warm-up exception for misfire and fuel system (C6).
  - State that line pressure comes before stall as an OEM rule (C25).
  - Treat tie-up and bind-up as synonyms (C29).
  - Present "seized stator = normal stall" as reasoning from the mechanism (C3).
  - Correct the Allison reverse clutch statement (C33).
- INFERRED: For Logan's electrical strength, C1, C9, C27 and C38 are "commanded vs. actual" or "signal voltage vs. reading" problems. The by-the-book answer always follows the circuit or command logic, never a remembered number.

### Gaps
- No textbook (Halderman or Today's Technician) text was reachable, so C3's "normal stall," C17's design reason, C19 drum criteria and C28 still lack a textbook citation.
- C15's pressure-direction mechanism rests on technician forums. A Gears or Transmission Digest article on engine-off cross-contamination was not found.
- C11, C14, C26 and C36 need GM or Ford SI, which isn't publicly reachable.

---

## Q2. Which claims in the notes contradict standard textbook automatic-transmission theory?

### Takeaway
Six claims contradict standard theory or apply-chart logic and should be corrected before any guide uses them. The most important is in `area_a_mech_hydraulic_diagnosis.md`, which lists the **low roller clutch** as a cause of slip in **all forward gears**. A 1st-gear-only OWC can't do that. Two more are wording problems that invert or blur a principle.

### Cited Findings
- **T1. The low roller clutch can't cause slip in all forward gears** (`area_a_mech_hydraulic_diagnosis.md`, "Slips in all forward gears, reverse OK: suspect the forward clutch … or the low roller clutch"). In the 4L60-E the low roller clutch holds only in 1st in Drive and freewheels otherwise. Manual 1 adds the low/reverse clutch to back it up. A failed low roller gives slip in D1 only, with manual 1 OK. — DOCUMENTED (snippet), forum/rebuilder: [LS1Tech 4L60E low/reverse clutch](https://ls1tech.com/forums/automatic-transmission/1977125-4l60e-low-reverse-clutch.html); [GMT400, low works in drive](https://www.gmt400.com/threads/4l60e-wont-shift-to-low-manually-but-low-works-fine-in-drive.74857/); textbook elimination method at [freeasestudyguides clutch/band charts](https://www.freeasestudyguides.com/transmission-clutch-band-chart.html). **Correction:** slip in all forward gears with reverse OK points to the forward/input clutch or its circuit (on the 4L60-E, also the forward sprag in D ranges). The low roller explains only a D1 slip.
- **T2. "The OEM 4L60 applies the overrun clutch in D3 (1st–3rd)"** (`apply_chart_reasoning.md` §3). Rebuilder and forum sources say the stock 4L60-E applies the overrun clutch in D3 only in 3rd gear, and in manual 2 and 1. Applying it in D3 1st and 2nd is a performance modification. — DOCUMENTED (snippet): [LS1Tech overrun clutch](https://ls1tech.com/forums/automatic-transmission/1970382-overrun-clutch-4l60e.html); [Sonnax 4L60E HP/HD build guide](https://www.sonnax.com/tech_resources/617-4l60e-performance-heavy-duty-transmission-build-guides). The same file's backward-sprag logic (C18) only makes sense if D3 1st has no overrun apply. Verdict LIKELY wrong as written; confirm against the GM range reference chart in Logan's GM training material.
- **T3. "High stall = stator not holding"** (flashcards cited in `stator_owc_diagnosis.md` / `hydraulic_pressure_testing.md`) and **"stall flash low indicates a seized stator"** (MOTOR 1999 snippet, this pass). Both contradict converter theory: freewheeling = low stall; seized = normal stall; high stall = transmission element slip (C2, C3).
- **T4. "A TFT short to ground reads −40"** (go-parts, cited in `area_a_electronic_diagnosis.md`). This contradicts pull-up NTC circuit theory and the Toyota SI (C1).
- **T5. "Pressure test before stall test isn't a documented rule"** (`textbook_vs_shop.md` C7). This contradicts OEM/ATSG service text that states the order (C25). It is overcautious rather than wrong about theory, but a guide should give the OEM order.
- **T6. "C1 handles forward ranges, and C2 handles reverse" (Allison)** (`gm_failure_patterns.md`, already flagged). This contradicts the apply chart: R = C3 + C5 (C33).
- **Wording issues (fix, not wrong theory):**
  - `area_c_overhaul.md` quotes "a sprag or roller clutch cannot be assembled in either direction." The textbook point is that it *won't work* if assembled in either direction. It *can* be installed backward, which is the classic C.22 error (C18).
  - `area_b_in_vehicle.md` Inferences says the TBV "works the opposite way from an engine thermostat." It actually works the same way: a thermostat stuck closed (no radiator flow) overheats the engine, just as a TBV stuck in bypass (no cooler flow) overheats the transmission. Only the "stuck open" comparison differs.
  - `scan_tool_bidirectional.md` already flags Sun Transmissions' claim that a pressure mismatch means the solenoid or wiring. A gauge-vs-command pressure mismatch with the current tracking the command means hydraulic supply or a leak.

### Inferences
- INFERRED: T1 and T2 matter most, because apply-chart reasoning is a top-ranked A2 skill (public sample item 8) and both errors would teach a wrong elimination. Every other apply-chart statement in `apply_chart_reasoning.md` that I checked agrees with standard Simpson, Ravigneaux and Lepelletier logic: TH350/TH400 2nd-gear elements, the A727 front/rear clutch naming, 4L60-E D4 = 3-4 clutch + 2-4 band, and 6L80 two elements per gear.
- INFERRED: No note contradicted core converter, EPC, TCC two-pass/three-pass, pressure-test interpretation, or OBD II theory, apart from the items above.

### Gaps
- T2 needs the GM Hydra-Matic 4L60-E range reference chart (in GM training, the ATSG manual or SI) for a definitive answer.
- The seized-stator stall statement (T3) needs a textbook sentence to close it formally.

---

## Q3. What internal inconsistencies (task numbers, duplicated numbers) exist across the files?

### Takeaway
Two files use task numbers that don't match the verified 2026 map in `research.md`, and one number conflicts between two files (41TE CVI, C24). Fix these before the notes feed a weighted guide, because the guide prioritizes by task.

### Cited Findings
- **`hardest_topics_and_strategy.md` ranked table:**
  - It maps symptom diagnosis to "A.1–A.3," electronic diagnosis to "A.4–A.8," stall to "A.10" and the TCC solenoid to "B.x." Per `research.md`: A.1 = type ID; A.2 = verify concern; A.3 = SI/TSB research; A.4 = fluid type and level; A.5–A.7 = DMM/DSO/scan and OBD II; A.8–A.10 = road test, NVH, fluid loss; A.11 = pressure tests; A.12 = stator/OWC (the stall topic); A.13/A.18 = TCC mechanical/electronic; A.19–A.28 = electronic systems. The file's "CVT/DCT on the list? OPEN" is already answered: A.1 names TC auto, DCT, CVT and hybrid/electrified. — local `autotrans/research.md` (task map).
  - The same file asserts GM doesn't publish stall tests (C26, unverified).
- **`hydraulic_valves_circuits.md` §8** tags the converter-out/cooler/lube circuit {B.8}. B.8 is accumulator and servo inspection. The cooler tasks are **B.5** (in-vehicle) and **C.4** (flush/test on R&I). — local `research.md`.
- **`apply_chart_reasoning.md` vs. `scan_tool_bidirectional.md`:** 41TE CVI OD 75–135 / L/R 35–85 vs. OD 75–150 / L/R 35–83. The search supports the second set (C24).
- **`stator_owc_diagnosis.md` Gaps** asks whether the task list names "stall test." Per `research.md`, the shortened wording is A.12 "Torque converter stator/OWC failure" and A.11 "Hydraulic pressure tests". Stall is not named in the shortened text, so check the full statement in the local PDF.
- **`scan_tool_bidirectional.md` §1** leaves the task wording OPEN. `research.md` maps it to **A.24** (scan data, bidirectional controls, DTCs) and **A.26** (DMM/DSO test of solenoids).
- **`apply_chart_reasoning.md` header** uses "C.13" for the chart work. C.13 is planetary gear assembly, which fits, and the file notes it wasn't re-checked. No change needed.

### Inferences
- INFERRED: Once these re-tags are made, every research file maps cleanly onto the 63-task list, and the weighted priorities in `research.md` (Area B highest yield per task) can be applied without double counting.

### Gaps
- The full (unshortened) 2026 task statements weren't re-read here. Re-verify the wording of A.11/A.12 and C.23 against the local PDF pages 10–15 before a final guide.
