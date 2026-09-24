# GM ASEP and ASE A3 Research Foundation

Created: 2026-09-13. Last updated: 2026-09-17 (America/Denver). Filename retained for continuity.

**Current use:** The class final is Monday, 2026-09-21; its preparation is based mostly on class notes reflecting the instructor's textbook coverage. Logan expects to take A3 during the week beginning September 21, while friends are testing during the preceding weekend. Rear-axle notes may still grow. Working guides were assembled on September 17 (now in `study/`) and can be refreshed after new notes. See `CONTEXT.md` for the current schedule.

**Learner context, September 16:** This is Logan's seventh ASE. Logan reports substantial electrical competence from prior ASE preparation and other experience. G01 describes a limitation of the reviewed documents, not a diagnosis of Logan's abilities. Later electrical preparation should be a brief review of drivetrain-specific electronic applications, drawing on that existing knowledge.

## Assessment

The existing A3 research blueprint covers the major subject areas and provides a useful vocabulary of symptoms, components, and likely causes. Its largest weakness is the distance between identifying a suspect and interpreting the evidence needed to confirm it. Measurements, electrical diagnosis, and application differences receive substantially less development than symptom recognition.

The classroom notes add valuable mechanism explanations and identify genuine points of uncertainty. They also preserve broad classroom rules whose limits deserve separate investigation. This supplement identifies those limits without rewriting the notes or the study guides.

**Purpose:** supporting research for the eventual GM ASEP class-final and professional ASE A3 preparation packages. The class combines GM-oriented instruction and labs with a textbook that is not GM-specific. The final class package will draw on the complete semester material and instructor emphasis; the ASE package will also address its broader, manufacturer-independent coverage. Research is being accumulated now for that later synthesis.

**Scope:** the 2026 official ASE guide supplies the exam coverage reference. The original assessment and application findings were checked on September 13, 2026, America/Denver; the separately dated official-ASE addition below was checked September 16. The original gap register refers to the September 13 material, not the rear-axle notes now being written. This document does not establish the instructor’s final-exam blueprint or certify every statement in the original report.

Evidence labels used below:

- **DOCUMENTED:** supported by an inspected primary source, within its stated application.
- **INFERRED:** a diagnostic or educational conclusion drawn from that evidence.
- **OPEN:** an identified question that still needs application-specific documentation or further verification.

“Thin” means a subject is named or summarized but lacks a worked explanation. “Missing” refers to the reviewed material, not to what a student may already know.

## Material and baseline

The supplied `deep-research-report (3).md` in Downloads is byte-identical to the project copy. References to “Blueprint” below mean that file. Additional material examined: `clutchsection.txt`, `gears.txt`, `unit2_study_guide.md`, and `unit2_cram_sheet.md`. Local line numbers identify passages, not judgments about authorship.

The Blueprint's exam timing is supported: A3 has 40 scored questions, 10 additional unscored research questions, and 60 minutes. The recertification test has 20 scored questions and 30 minutes.[^1] Its published category table also matches ASE's guide. The percentages do not precisely equal each count divided by 40; that discrepancy is present in ASE's own table, not introduced by the Blueprint.[^2]

The evidence supports retaining the broad study structure. There is no basis here for a pass-probability estimate or a percentage score for completeness.

## Gap register

Priority is an educational judgment: **High** means a gap affects interpretation or could encourage an incorrect conclusion; **Medium** means useful additional coverage. ASE references use category letter and task number from the A3 section, printed pages 16–18.[^2]

| ID | Priority | Existing location | Gap or qualification | ASE anchor | Status |
|---|---|---|---|---|---|
| G01 | High | Blueprint: Electrical diagnosis, lines 475–485; questions 39, 41, 44 | Checks are listed, but meter readings and competing circuit faults are not worked through. | B17, C19, E16, F11 | Evidence and example below |
| G02 | High | Blueprint: Backlash/preload, lines 348–364 | Definitions do not teach shim calculation, measurement conditions, or verification after assembly. | B12, C16 | TREMEC example below |
| G03 | High | Blueprint: Ring-and-pinion patterns, lines 380–390 | No developed pattern-reading exercise; preload recovery and backlash variation need explanation. | E3–8 | Manufacturer example below; visual practice still open |
| G04 | High | Blueprint: Clutch bearing test, lines 114–134; clutch notes near opening | Pedal-position rules need release-system design qualifications. | A1, A4 | Qualified with ZF/EXEDY evidence |
| G05 | High | Unit 2 guide, lines 104–107; cram sheet, lines 43–45 | Equal CV angles are treated as sufficient to eliminate torque steer. | Related drivetrain reasoning | Universal claim not supported |
| G06 | High | Unit 2 guide, lines 81, 95–98 | Engine-off shifting and noise pitch are treated too conclusively. | B1, C1 | Inference limits and rotation/load example below |
| G07 | Medium | Blueprint: Transmission versus transaxle, lines 241–249 | Pumps/coolers are mentioned; almost no explanation of their diagnostic significance. | B15, C17 | Cooler and GM repeat-failure context documented; current test limits open |
| G08 | Medium | Blueprint: Limited slip, lines 392–400 | Clutch-type example lacks a comparison with helical limited slip and locking designs. | E13–16 | Eaton contrast below |
| G09 | Medium | Blueprint: U-joint angles, lines 312–324 | No slope-to-operating-angle calculation or compound-angle boundary. | D6 | Worked example below |
| G10 | Medium | Unit 2 guide, lines 22, 101–102; gears.txt opening | Gear topology and shaft names need a model-specific diagram; ratio notation deserves a worked example. | Supporting mechanism knowledge | Ratio and design contrasts documented; exact lab layout open |
| G11 | Medium | Blueprint: Axle leaks/vents and service-information list | Little developed inspection of axle flanges, retainers, hubs, studs, or case/subframe alignment. | A8–10, C4, D7, E18–21 | Coverage gap; procedures open |
| G12 | High | Blueprint throughout and self-quiz | Exported citations are unresolved markers; questions mainly test recognition. | Evidence/practice quality | Source replacements and practice criteria below |

The matrix is a targeted index, not a reproduction of every ASE task. Grouping several tasks into a row does not imply that those tasks have equal exam frequency.

## Electrical diagnosis and 4WD engagement

### G01: From a checklist to a measurable conclusion

The Blueprint sensibly asks for power, ground, command, and actuator checks. Its question 39, however, largely asks the reader to recognize that checklist. It does not establish whether the reader can distinguish supply resistance, a failed ground, an open load, or a missing command.

**DOCUMENTED:** Fluke explains that voltage-drop testing must evaluate an operating circuit; a meter's resistance test does not reproduce the circuit's normal load. Ground-side restrictions can impair a component and distort measurements. These are general electrical principles, not a universal wiring diagram for a transfer-case motor.[^3]

**Worked reasoning example — invented values, simple steady-DC load:** A connected actuator has 12.4 V at its supply terminal and 3.0 V at its ground terminal, both measured relative to battery negative while current flows. Voltage across the actuator is 12.4 − 3.0 = **9.4 V**. The ground path is losing 3.0 V. Investigate that path before condemning the actuator. This interpretation assumes the identified terminal is intended as a ground return, not a PWM-controlled or reversing-motor terminal.

The missing learning step is to explain the significance of each reading and the measurement reference. A voltage printed beside a connector is incomplete evidence without the probe locations, command state, and load state.

### Actual engagement faults beyond “replace the motor”

**DOCUMENTED:** GM described intermittent transfer-case faults on specified 2015–2017 trucks and SUVs caused by missing connector seals and moisture intrusion. The article also addresses corrosion of mating connections.[^4] This is a concrete reason to inspect the connector environment when symptoms are intermittent or weather-dependent.

**DOCUMENTED:** A Chrysler tip for a 2019 DT with C1403-92 directs attention to proper seating of the transfer-case range-position sensor before ordering the assembly.[^5] The tip demonstrates that a position-related fault can involve installation, not simply a failed electronic part.

**INFERRED:** A useful extension to the Blueprint would compare three cases with the same driver complaint: command never arrives, actuator receives inadequate usable voltage, and actuator/sensor installation prevents correct operation. Each requires different evidence. These historical examples establish possible failure mechanisms; they do not establish the most common cause on other vehicles or substitute for current service information.

## Measurements and assembly decisions

### G02: Endplay and shim selection

The Blueprint explains that endplay and preload matter but does not make the reader perform a selection calculation. Knowing the definition of endplay is different from deciding which shim to install.

**DOCUMENTED:** TREMEC's T5 WC countershaft procedure measures temporary-assembly endplay C, calculates shim thickness as C minus 0.0018 inch, then rechecks the completed assembly. Its specified final range is 0.0005–0.0040 inch.[^6]

**Worked example — invented measurement, actual procedure relationship:** If C is 0.0140 inch, calculated shim thickness is **0.0122 inch**. Selecting an available shim is not the final proof: the assembled endplay must be measured again. These numbers belong to this particular T5 WC procedure; they are not generic transmission specifications.

**INFERRED:** Add problems that supply the assembly drawing, the reference measurement, the manufacturer's equation, and the available shims. Ask for the selection and the verification step. Do not teach “add a shim” or “subtract a shim” without identifying where it fits and what dimension it changes.

### G03: Pinion preload and contact-pattern evidence

The Blueprint distinguishes backlash, preload, and pinion depth correctly at the vocabulary level. Its question 36 asks only whether the pattern evaluates gear setup. That does not demonstrate an ability to use a pattern or recover from an assembly error.

**DOCUMENTED:** Chrysler's P77 rear-axle procedure distinguishes pinion turning torque from the tightening operation. If turning torque becomes excessive, it calls for a new crush sleeve rather than loosening the nut. It also measures backlash at several positions and uses separate contact-pattern illustrations for adjustment decisions.[^7]

**INFERRED:** The important additions are three separate exercises: identify which torque is being measured; explain why an over-compressed sleeve is not corrected simply by backing off the nut; and compare backlash measurements around the ring gear rather than accepting one convenient reading.

The source provides an application-specific example, not authority for one universal axle setup sequence. A final study exercise should use a legible original pattern image with its drive/coast identification and matching procedure. This supplement does not invent a generic pattern chart or claim that every pattern can be reduced to a single mnemonic.

**Remaining gap:** practical discrimination among carrier runout, ring-gear mounting problems, depth, and backlash needs a dedicated illustrated exercise. The original report's contact-pattern coverage remains thin even after this evidence supplement.

## Clutch and transmission diagnostic qualifications

### G04: Release-bearing rotation versus loading

The clutch notes explicitly question whether a release bearing could make noise without pedal load. That is a productive uncertainty worth preserving.

**DOCUMENTED:** ZF describes concentric slave-cylinder arrangements in which the release bearing runs continuously while the clutch turns, with actuation-system preload maintaining contact.[^8] Pedal movement therefore does not always mark the instant the bearing first begins to rotate.

**DOCUMENTED:** EXEDY describes a release-mechanism squeak with the foot off the pedal that disappears under light or full pedal pressure. It associates that case with inadequate contact conditions from release-mechanism wear, and cautions against automatically identifying the bearing itself as faulty.[^9]

**DOCUMENTED:** ZF additionally links inadequate releaser preload, worn guide tubes, and off-center contact with noise and wear.[^10]

**INFERRED:** Preserve the report's pedal-position test as an observation framework, but separate three questions: What rotates? What load changes? What interface can move or rub? A noise disappearing with pedal pressure is evidence about the operating state, not a complete component diagnosis. The evidence answers the notes' broad concern about unloaded release-system noise; it does not prove that every such noise is damaged bearing balls.

### G06: Clues versus proof

The Unit 2 guide says that normal shifting with the engine off means “the transmission itself is fine.” That conclusion is stronger than the observation warrants. Removing the speed difference can make an engagement easier without demonstrating that every internal component is healthy.

**DOCUMENTED:** TREMEC's T5 troubleshooting list includes several causes of hard shifting and clash, including clutch release, lubricant, pilot support, alignment, and synchronizer problems.[^6]

**INFERRED:** The defensible learning rule is: normal engine-off shifting makes clutch release and rotation-related causes important checks; it does not certify the transmission. This preserves the diagnostic direction while removing an unsupported guarantee.

The constant-road-speed rule deserves the same treatment. A noise that stays tied to road speed does not, by that observation alone, isolate an output bearing. The Blueprint itself includes other road-speed-related components. Likewise, a pitch change when changing gears can track an engine/input-related speed change; it does not alone prove a particular selected gear is damaged.

This is a reasoning limitation, not a claim that the instructor's example was wrong. The missing context could have restricted the example to a known group of components. A better exercise supplies a second observation—load response, stationary behavior, turning response, or location—and asks how the suspect list changes.

### G06: Rotating parts and loaded parts

**Question:** Does a gear continuing to rotate mean it is carrying the selected drive torque?

**DOCUMENTED:** Eaton's UltraShift PLUS service description distinguishes the front-section direct-drive torque path from the gears that continue rotating. It explains that the direct path couples the input/main-drive gear through a sliding clutch to the front mainshaft while other gearing continues rotating without all of it being loaded.[^23]

**Scope:** This is a heavy-duty automated transmission example. It establishes a mechanical distinction; its range section, gear numbering, and controls are not being added as A3 class requirements.

**INFERRED:** A useful power-flow exercise needs separate labels for rotation and selected torque transmission. A gear may rotate without being the chosen ratio's loaded path. Here “unloaded” means not carrying that selected drive torque; it does not mean absolutely zero force, friction, or drag.

That distinction improves the interpretation of noise observations. A change in noise when changing ratios may reflect a change in speed, loading, or both. It should lead to another discriminating observation rather than automatically naming a single gear or bearing.

**Use in the eventual package:** On an application-matched diagram, mark which parts rotate and separately mark the main torque path. Repeat for neutral, a reduction ratio, and direct drive where the design has it. Explain why a part that is still moving can become quieter after its loading changes.

**OPEN:** The original “never fixed-to-fixed” wording still needs a course-relevant gear diagram and precise meaning of “fixed.” These sources clarify rotation and selection but do not complete that exact lab comparison. Do not mark the entire topology question closed.

## Design distinctions

### G05: Torque steer is broader than CV-angle equality

The raw notes and Unit 2 guide connect torque steer to unequal CV angles, shaft lengths, and twist. The stronger statement that equal angles eliminate torque steer needs qualification.

**DOCUMENTED:** Honda describes torque steer arising from unequal drive torques acting around the steering axis in its ATTS application, and explains that reducing kingpin offset reduces that effect.[^11] Honda's current Civic Type R description likewise identifies steering-axis geometry as a means of minimizing torque steer.[^12]

**INFERRED:** These sources support a broader explanation involving the relationship between drive forces and steering geometry. They do not support treating CV-angle equality as sufficient proof that torque steer is impossible. The wobble-socket analogy should not serve as the entire explanation of the phenomenon.

**OPEN:** “Unequal CV angles are the most common cause” is a frequency claim. No population-specific evidence establishing that ranking was found here. It can be retained as recorded classroom emphasis, but should not be promoted to a universal statistic. This does not establish a different universal “most common cause.”

### G07: Manual-transmission cooling

The Blueprint mentions pumps and coolers in its transaxle paragraph. The Unit 2 guide appropriately describes splash lubrication as typical rather than universal, but does not develop a contrasting arrangement.

**DOCUMENTED:** TREMEC describes the manual-equipped Mustang Dark Horse's TR-3160 with a factory transmission cooler.[^13] That is enough to establish that manual-transmission preparation cannot universally stop at splash lubrication and fluid level.

**INFERRED:** A useful addition would identify the actual lubricant route and ask what observation distinguishes inadequate quantity from inadequate circulation or heat rejection. A proper exercise needs a specific service diagram. Cooler existence alone does not establish pump drive, control logic, test pressure, or repair procedure.

#### GM service context: cooling and repeat failures

**Question:** What does cooler coverage add beyond knowing that some manual transmissions have a cooler?

**DOCUMENTED:** GM's January 2011 *TechLink* advises cooler flushing and flow testing after hard-part failure when a manual transmission has an external auxiliary cooler. It explains that a restricted cooler can produce excessive operating temperature and repeat failure. The same article cautions about fluid left in the cooler and lines from dealership flushing equipment.[^24]

**Application/date boundary:** This is historical GM service guidance. Its fluid statements are not presented here as a universal 2026 specification for every manual transmission. Current service information for the actual vehicle determines fluid, equipment, and procedure.

**INFERRED:** A repair can restore the gearbox's internal parts while leaving a problem elsewhere in its lubricant circuit. The teaching sequence should connect the original failure, possible remaining restriction or contamination, the specified flow/cleanliness checks, and repair verification.

**Reasoning example:** A hypothetical manual gearbox with an external cooler experiences a second heat-related failure after internal repair. Correct fluid quantity alone does not demonstrate adequate circulation through the external circuit. Review the specified cooler/line checks and their results before attributing the repeat failure solely to the replacement internal parts. This is a constructed learning example, not a diagnosis of an actual vehicle.

**Use in the eventual package:** Pair a lubricant-path diagram with service history. Ask what evidence is still missing after the internal repair. This adds diagnostic meaning to the earlier Blueprint's brief pump/cooler mention and supplies a GM-oriented example of the general principle.

**OPEN:** A specific current pump-drive arrangement, flow limit, or pressure-test procedure has not been established here. The historical source narrows G07; it does not finish a complete lubrication-system chapter.

### G08: Limited slip is not one mechanism

The Blueprint already limits its additive discussion to clutch-type units. That wording is valuable and should remain. The missing piece is an explicit contrasting example, which helps prevent a reader from forgetting the qualification.

**DOCUMENTED:** Eaton's Posi FAQ calls for friction modifier when it is not already in the selected lubricant.[^14] Eaton's Truetrac FAQ identifies that product as a helical limited-slip unit rather than a locker, and says friction modifier reduces its differential bias.[^15]

**INFERRED:** The additional learning objective is identification before diagnosis: establish the actual differential type before borrowing an additive, lockup, or service rule. The two examples demonstrate that “limited slip” is not enough information to choose a universal fluid treatment. Their instructions apply to those Eaton products; current instructions for the installed unit remain controlling.

## Geometry and ratios

### G09: Shaft slope is not joint operating angle

The report's phasing/balance/runout/angle distinctions are useful. It lacks a calculation that forces the learner to distinguish shaft inclination from the angle between adjacent shafts.

**DOCUMENTED:** Spicer defines operating angle through the relationship between component slopes, and recommends considering loaded as well as unloaded vehicle conditions.[^16] Its simple online calculator explicitly excludes compound angles involving horizontal offset.[^17]

**Worked example — invented, one vertical plane:** Looking from front to rear, assign upward slope positive. Transmission axis: −3°. Driveshaft: −1°. Pinion axis: −3°. The front joint's angle is |−3 − (−1)| = **2°**. The rear is |−1 − (−3)| = **2°**. A driveshaft slope of −1° is therefore not a 1° joint angle.

**INFERRED:** Matching calculated angles is only the result of this exercise; it is not proof of correct phasing, balance, allowable operating speed, or three-dimensional geometry. A separate side-view-only example should not be used to dismiss horizontal misalignment.

### G10: Ratio notation and topology

The notes' 10:7:20 example is useful for a simple idler train. The missing qualification is that a compound intermediate shaft carrying two different gears is a different arrangement.

**DOCUMENTED:** KHK distinguishes a simple train with an idler from a two-stage train whose intermediate gears share speed.[^18]

**Worked examples — speed ratios stated as input speed divided by output speed:** A 10-tooth driver, 7-tooth idler, and 20-tooth output give (7/10) × (20/7) = **2:1**. The intermediate count cancels. A 10-tooth gear driving a 20-tooth gear on a shaft that also carries a 15-tooth driver meshing with a 45-tooth output gives (20/10) × (45/15) = **6:1**. Here the intermediate shaft carries two different gears; it is not the simple idler example.

The follow-up evidence below qualifies the broad transaxle/pilot-bearing wording and provides a contrasting synchronizer location. **OPEN:** the exact lab transmission, its bearing-support diagram, and the intended scope of “never fixed-to-fixed” remain unidentified. Those application-specific questions are still open.

### G10: Transaxles and pilot bearings

**Question:** Is “transaxle means no pilot bearing” a general drivetrain rule, or a description of a particular classroom arrangement?

**DOCUMENTED:** Chevrolet's 2014 Corvette brochure explicitly describes the seven-speed manual car's rear transaxle location.[^19] Chevrolet's own parts catalog lists clutch pilot bearing 12557583 for Corvette applications including 2014.[^20]

**INFERRED:** A vehicle having a transaxle does not by itself establish that its entire clutch/driveline system has no pilot bearing. The sources provide a GM counterexample to that broad reading. This conclusion does not identify the exact member supported by the bearing in every Corvette arrangement; the generic parts-page description is insufficient for a full support diagram.

The useful distinction for study is between the assembly's location/integration and the way its rotating members are supported. Naming a unit “transaxle” is not a substitute for tracing that support. The class notes may be describing a conventional front-drive lab unit accurately while using broader wording than its actual scope.

**Use in the eventual package:** Add a labeled comparison of the actual lab transaxle and a rear-transaxle GM example. Identify the clutch location, shaft connections, and each bearing's supported member. Keep the lesson about support and relative motion; model-specific part numbers need not become memorization targets.

**OPEN:** The exact lab unit remains unidentified. Its pilot-support arrangement and shaft naming still require its own diagram. The universal wording issue is now bounded; the lab-specific question remains open.

### G10: Synchronizer location and shaft speed

**Question:** Can the usual output-shaft synchronizer explanation be applied literally to every gear of every manual transmission?

**DOCUMENTED:** TREMEC's synchronizer overview presents a common arrangement with the selected gear locked to the output shaft, and explains the sleeve/keys/blocker-ring sequence.[^21] TREMEC separately documents a fifth-gear synchronizer mounted on the countershaft in the TR-4050, offered in versions for GM and Ford applications.[^22]

**INFERRED:** The general principle survives a change in shaft location: the selected gear becomes coupled to the shaft carrying the relevant hub. “Output shaft” describes one arrangement; it should not replace identifying the actual shaft carrying the hub in the diagram. A countershaft-mounted synchronizer provides a concrete reason to avoid memorizing one shaft layout as universal.

This qualification is compatible with the corrected synchronizer sequence already embedded in `gears.txt`. It adds an application boundary to the explanation rather than undoing the useful distinction between friction at the cone and engagement at the teeth.

**Use in the eventual package:** Ask the learner to identify the hub's shaft first, then label what can rotate relative to it before engagement. Use the actual class diagram for class-specific naming, and a contrasting layout to check transfer of understanding for ASE preparation. The TR-4050 example is a manufacturer-documented design, not evidence that this transmission was used in the course or installed at the factory in a particular class vehicle.

## Practice and source quality

### G12: Recognition questions are not a readiness measure

The Blueprint contains 50 questions, but the count should not be mistaken for evidence of exam-equivalent difficulty. For example, question 49 contrasts driveshaft phasing with clutch-cylinder bore, synchronizer material, and differential additive. A learner may succeed through category elimination without understanding how phasing produces a complaint. Question 40 tests category weighting rather than a repair decision.

This does not make those questions useless. They can establish basic recognition. Their educational limitation is that they provide little evidence about measurement interpretation, diagram reading, or discrimination among plausible causes within the same system.

**Recommended next exercises, derived from the gaps rather than claimed as actual ASE questions:**

1. **Electrical evidence:** Give probe locations and loaded voltage readings; require identification of the suspect circuit section and a confirming test.
2. **Shim selection:** Supply the manufacturer's assembly relationship and available shims; require calculation and final verification.
3. **Axle setup:** Supply an identified contact-pattern image plus backlash readings; ask what remains unresolved before changing a setting.
4. **Clutch observation:** Compare continuous-contact and clearance-type release arrangements; explain why the same pedal observation may not isolate the same fault.
5. **Noise isolation:** Keep road speed constant but vary gear and load; require a bounded suspect list rather than one memorized answer.
6. **Application identification:** Give two named differential designs; ask why the same additive decision does not apply to both.

A satisfactory answer should explain what the evidence supports, what it does not establish, and the next discriminating observation. These are suggested learning checks, not validated exam questions or pass criteria.

### Citation traceability

The Markdown export contains internal citation markers without a usable bibliography or resolved links. That is a traceability defect, not proof that the cited claims are false. The sources below provide independently inspected support for this supplement only. They do not reconstruct every citation in the original report.

For future additions, retain the exact source, section/page, application, and access date. Keep unresolved claims visible. A manufacturer document can demonstrate a mechanism without proving that it is common or that its specifications apply to other units.

## Official ASE documents and study resources — September 16, 2026

### What this pass adds

This pass follows ASE's own publications and the ASE Education Foundation's linked resources. It adds a distinction between professional A3 and entry-level MD, checks the public A3 illustrations, identifies the official practice-test option, and records question-reading guidance for later use. It does not assess the completeness of the developing rear-axle notes or produce either prep package.

**Local context:** Logan's new `drive-axles.txt` says transfer cases received limited class attention and identifies planetary operation as an area needing study. Logan confirmed September 16 that these notes are unfinished. This is evidence of a future study need, not an independently verified technical claim or a judgment about the instructor's coverage.

### Professional A3 and entry-level MD have different blueprints

**DOCUMENTED:** ASE's professional Automobile Study Guide is dated 2026. The Education Foundation separately links an entry-level Automobile guide revised November 19, 2023, and individual-test specifications effective July 1, 2023. Those older-dated entry-level documents remain linked from its current resource page; their dates must not be relabeled as 2026 revisions.[^2][^27][^28][^29]

The following compares **scored-question allocations**, grouping transmission and transaxle for comparison. It is not the instructor's final-exam blueprint.[^2][^28]

| Subject | Professional A3 | Entry-level MD |
|---|---:|---:|
| General diagnosis as a separate category | None | 5 |
| Clutch | 6 | 7 |
| Transmission/transaxle | 7 + 7 | 8 combined |
| Shafts and joints | 5 | 6 |
| Differential/drive axles | 7 | 9 |
| 4WD/AWD | 8 | 5 |
| Total scored questions | 40 | 40 |

**DOCUMENTED:** The entry-level specifications publish a passing threshold of 21/40 for MD. ASE's 2026 entry-level technical report also identifies 21 as its MD threshold. That is an entry-level result; it does not establish the professional A3 passing standard or Logan's class grading requirement.[^28][^30]

**INFERRED — use in this project:** Keep professional A3 as the governing exam reference for the planned ASE package. Entry-level material is a supplementary explanation of question formats and foundational coverage. The different grouping means a letter/task number from one program must not be pasted into the other's checklist. An entry-level result, if Logan later supplies one, should be identified by its actual program before drawing conclusions about readiness.

### Two public A3 examples directly support the earlier gaps

**DOCUMENTED, visually checked:** On printed page 19, question 4 uses a gear-contact photograph and identifies pinion depth as the cause. On page 20, question 5 shows 12.4 V from the coupler's control-side terminal to ground; ASE identifies an open at Y. These are public sample items.[^2]

**INFERRED:** In that circuit, an open return can leave the terminal near supply voltage through the coil without useful coil current. Reading battery voltage at one terminal does not establish voltage across the load. The photograph question does not supply a complete shim-adjustment procedure.[^2]

**Use for G01/G03/G12:** The source now provides located, inspected illustrations for the earlier measurement and pattern gaps. Later practice should require explaining the probe reference and what measurement would separate competing faults. For the axle example, progress from recognizing an abnormal pattern to using an identified manufacturer's adjustment procedure. The official answer alone does not resolve every setup decision.

A separate application-matched exercise is still needed before G03 can be marked complete. The September 13 Chrysler procedure remains a service example; the ASE photograph is a test-format example. Neither should silently inherit the other's vehicle or specifications.

### What to carry forward into the ASE coverage check

**DOCUMENTED:** Additional task anchors worth retaining are calibration/communications (B14/B17/C19), transaxle differential diagnosis (C12–16), axle measurements (E2–8/E12/E20), and engagement systems plus tire matching (F11–12).[^2]

**INFERRED — proposed organization, not a finished study plan:**

| Future study block | Why it belongs in the later synthesis | Evidence to request from the learner |
|---|---|---|
| Transfer-case and AWD operation | The unfinished notes explicitly identify this as unfamiliar. | Trace a named design's torque path and explain what changes between operating modes. |
| Drivetrain electrical applications — brief review | Logan's electrical foundation is established; use G01 to locate drivetrain examples, not to prescribe remedial study. | Identify the actuator, control/feedback signals, operating state, and any required calibration in the named system. |
| Axle setup and failure isolation | The new notes record class emphasis on preload and noise; G03 still needs developed practice. | Distinguish the measurements and justify the next check from the given evidence. |
| Transmission/transaxle mechanisms | Existing guides and research contain useful explanations with documented design boundaries. | Transfer the mechanism to a different labeled layout without assuming identical shaft names. |

For each later coverage entry, retain the source passage, the learner's explanation, and any unresolved point. A topic appearing in a document is evidence of coverage, not evidence Logan can yet solve a problem about it. Conversely, no omission in an unfinished notes file should be used as evidence that the subject will never be taught.

**Electrical scope refinement from Logan:** Favor a compact application map covering shift sensing/actuation, differential or transfer-case engagement, control-module communication, and service initialization. Use the verified task anchors above to select topics. They establish testable subjects; the official documents do not assign a question frequency to each sensor or actuator. Existing electrical knowledge supplies the circuit fundamentals. No remedial electrical sequence is planned.

### Official practice tests: useful external calibration, one question set

**DOCUMENTED:** ASE offers an official A3 practice test with 20 questions. ASE describes its questions as matching certification-test format and difficulty. It provides explanations for correct and incorrect options and a printable performance report. There is currently one question set per subject; another voucher for A3 does not provide a fresh set. Access lasts 60 days after voucher redemption.[^25]

The current price listed by ASE for one or two vouchers is **$14.95 per test**, checked September 16, 2026. ASE also publishes requirements for an officially licensed test-prep partnership, including review of content/style and alignment with current task lists.[^26]

**INFERRED — how it would help next week:** If Logan chooses to use the official practice test, preserve the first attempt before reading explanations. Its report can identify priorities for the directory-based study package. Later repeats remain useful for learning, but remembered answers cannot serve as independent evidence of improvement. A 20-question result also cannot demonstrate every listed task.

The existing locally generated questions can provide additional explanation and practice, but should continue to be labeled original practice. ASE's January 2026 certification guide describes technical review and statistical pretesting before items become scored questions.[^31] **INFERRED:** Plausible wording and an answer key do not provide that validation for our own items, or support a promised probability of passing.

**Access boundary:** This pass inspected the public program description, not the paid question set or a personal score report. No voucher was purchased or redeemed. The earlier Blueprint's specific statement about Motor Age licensing was not independently re-established from an individual partner listing in this pass; ASE's partnership criteria alone do not prove a particular publisher's current status.

### Question-reading methods and testing-interface familiarity

**DOCUMENTED:** The entry-level guide's printed pages 4–7 explain direct questions, Technician A/B questions, and EXCEPT/least-likely questions. Evaluate A and B independently; one being correct does not make the other incorrect. For an exception question, identify the option that fails the stated condition. Answer within the provided choices rather than substituting an unlisted real-world possibility.[^29]

**INFERRED — useful practice design:** A later explanation should connect each rejected option to the condition in the question. Distinguish “could cause” from a request for the most likely cause. Record whether an error came from a mechanism misunderstanding, reading the operating condition incorrectly, misreading a diagram, or missing the exception instruction. That tells us what to reteach more clearly than a total score alone.

**DOCUMENTED:** ASE's current test-center guidance recommends choosing the best available answer, flagging a difficult item, and returning if time remains. Scoring counts correct answers, so every question should be answered; a submitted test cannot be reopened.[^32] Its Free Test Drive page provides a video demonstration and a platform webinar.[^33]

**Use in the later package:** Keep a short interface/orientation link beside technical practice. The platform resource is for familiarity with test operation; it does not establish A3 knowledge. No claim is made here that the linked videos were watched or that this pass completed a testing-platform simulation.

### Result of this research pass

Nine additional official sources are indexed below. The professional guide and A-series page were rechecked. The new findings strengthen source selection, evidence-based practice, and the distinction between the two ASE programs. They do not close the remaining manufacturer-specific procedure gaps listed later in this document.

The Monday class-final package remains primarily notes-based. The professional ASE package serves immediate weekend review and Logan's following test week. Working versions of both were created on September 17 (now in `study/`); this research file remains their supporting evidence record.

## Broader teaching resources and weighted topic research — September 16 continuation

This pass combines general teaching material with individual mechanism and inspection examples. The broader sources help explain how assemblies work; the specific examples establish how to interpret a measurement or distinguish designs. These are supporting ingredients for the later package, not a replacement set of unit guides.

### Use ASE's published weighting to choose coverage

**DOCUMENTED:** The professional A3 guide publishes the following approximate percentages. Preserve the published values rather than recalculating percentages from question counts.[^2]

| Category | Published approximate share |
|---|---:|
| Clutch | 16% |
| Transmission | 17% |
| Transaxle | 17% |
| Drive shafts and universal joints | 13% |
| Drive axles | 17% |
| Four-wheel drive/all-wheel drive | 20% |

**INFERRED — research priority:** Transmission and transaxle together represent a published 34%; 4WD/AWD is the largest individual category. That justifies gathering stronger explanations in both areas. These percentages establish coverage priorities, not fixed study-time allocations. Logan's existing competence and later practice results should determine where additional time helps. Electrical applications sit within these categories; no separate electronics percentage is established here. Monday's instructor-led final retains its own notes-based scope.

### Broad resources now available

| Resource | Material inspected and likely use | Boundary |
|---|---|---|
| KHK illustrated gear primer | Gear forms and planetary layout; printed pp. 6–7 visually checked. A source for labeled gear explanations and ratio examples.[^34] | General gearing, not an automotive exam blueprint. |
| BorgWarner AWD actuator paper | Front-drive-based and rear-drive-based AWD layouts; figure 1 visually checked. Helps trace the primary and secondary axle paths.[^35] | Describes selected coupling architectures, not every AWD design. |
| TREMEC TR-3550/TKO service manual | Full manual saved; contents and printed inspection page 43 visually checked. Useful for connecting component condition to an actual inspection limit.[^36] | Historical application-specific reference; the whole manual has not been audited or established as current repair guidance. |

Unmodified PDFs are stored together under `sources/drivetrain/`; local links are in their source entries. Only selected relevant sections were reviewed, so having the full file locally must not be mistaken for validating every procedure.

**Additional resource leads:** Weber State's John Kelly faculty page links to his teaching channel and documents his transmission-teaching background; individual videos have not been reviewed in this pass.[^41] Halderman's A3 animation library redirected to a restricted-access page. Its animations were not inspected and are not technical evidence here.[^42] If later course access makes a useful resource available, assess the actual lesson before incorporating it. This research does not identify Logan's textbook or edition.

### Planetary reduction: establish the members before calculating

**DOCUMENTED:** KHK illustrates sun input, fixed internal ring, and carrier output. For that arrangement, reduction is `1 + ring teeth / sun teeth`. Its example uses 48 ring teeth and 16 sun teeth, giving 4:1.[^34]

**INFERRED — constructed calculation:** At a hypothetical 1,800 rpm sun input, the carrier turns at `1,800 / 4 = 450 rpm`. Ideal output torque is four times input torque when losses are ignored. The fixed ring supplies reaction torque; the planets both rotate and travel with the carrier. Identify the held, input, and output members before applying a formula. This example illustrates a reduction mechanism that can help explain low range; it does not identify the ratio or arrangement of a particular transfer case. Reduction ratio and front/rear torque distribution answer different questions.

### AWD architecture: locate the coupling in the actual torque path

**DOCUMENTED:** BorgWarner's paper contrasts these representative arrangements:[^35]

| Layout in the paper | Primary axle | Route to the secondary axle |
|---|---|---|
| Front-drive-based AWD | Front | Transaxle/PTU, propeller shaft, rear-axle coupling |
| Rear-drive-based AWD | Rear | Transmission/transfer case, controlled connection to the front driveline |

The paper explains hydraulically loaded wet multi-disc clutch packs and a generation of actuator in which motor speed controls pump pressure. **INFERRED:** A request for torque, actuator operation, clutch pressure, and actual torque transfer are related but distinct observations. A motor receiving a command does not alone prove mechanical transfer. Keep the electrical review at that drivetrain-application level. Do not add a pressure sensor or a particular valve arrangement to a diagram unless the identified design contains it.

**DOCUMENTED — contrasting actuation:** BorgWarner's 2018 announcement for the 2019 Ram 1500 describes a motor-driven rotary cam serving clutch control and range shifting, with preemptive clutch locking available before rear-wheel slip.[^37] **INFERRED:** On-demand engagement need not wait for visible wheelspin. Range selection and axle coupling are different functions even when one actuator mechanism serves both. This is a named design example, not an exam-frequency prediction.

### GM operating modes: requested state versus completed state

**DOCUMENTED:** GM's February 2023 mode overview distinguishes 2HI, AUTO, 4HI, and 4LO on the systems discussed. AUTO engages the front axle while varying delivered torque as needed; 4HI is intended for appropriate low-traction conditions. The indicator flashes during a shift, and an unsuccessful shift leaves the previous setting active.[^38]

**INFERRED — diagnostic use:** Establish the road surface, requested mode, completed mode, and required shift conditions before treating a complaint as a broken component. A flashing selection is evidence of an attempted transition, not proof of completed engagement. Learn the function of low range and the need for shift conditions, but obtain the exact neutral/speed sequence from the identified vehicle's instructions. AUTO behavior here must not be generalized to every manufacturer's selector label.

### Synchronizer inspection: interpret the limit, not just the symptom

**DOCUMENTED:** TREMEC's TR-3550/TKO inspection page specifies a minimum 0.50 mm (0.020 in) gap between the blocker-ring face and gear clutch teeth with the ring seated on the cone. It also calls for inspection of ring slots, teeth, and friction-surface grooves.[^36]

**INFERRED — constructed measurement example:** For this stated procedure, 0.34 mm fails the minimum; 0.68 mm meets that clearance criterion but does not prove the whole synchronizer is serviceable. Wear can let the ring seat farther down the cone, reducing remaining separation. This gives later practice a concrete measurement to explain. Do not apply the TKO number to an unidentified lab unit, another synchronizer design, or every ring in a multi-cone assembly.

### Shift quality and staying engaged are different diagnostic questions

**DOCUMENTED:** Mazda bulletin 05-001/15 addresses specified SKYACTIV six-speed applications with difficult shifts and, in some cases, third-gear hop-out. It identifies revised 3–4 and 5–6 clutch-hub shapes and a 3–4 hub surface-treatment change.[^39]

**INFERRED:** Here, “clutch hub” belongs to the internal shift assembly; it does not mean the engine clutch pressure plate. Separate frictional speed matching from the positive engagement that holds a selected gear. Grinding and jumping out may involve different parts of that sequence. The bulletin demonstrates a real design-related case, not a universal diagnosis for either symptom.

**DOCUMENTED:** TREMEC's support FAQ lists clutch actuation/adjustment, synchronizer damage, and incorrect lubricant among causes of gear clash. It explains that some manuals use ATF for shifting/friction requirements and notes that some reverse gears are synchronized.[^40]

**INFERRED — later synthesis:** Use symptom conditions to choose the next check, rather than automatically assigning every clash to a worn ring. Fluid selection involves synchronizer friction as well as lubrication. The actual transmission specification governs; neither “manual means gear oil” nor “reverse is always unsynchronized” is a reliable universal rule. These additions support mechanism-based diagnosis without rewriting the existing classroom explanations.

## Targeted rear-axle continuation — September 18, 2026

The September 18 additions to `drive-axles.txt` made a new broad research pass unnecessary, but they exposed several mechanism boundaries worth checking before the class and ASE guides reused the notes. The raw notes group “Positraction,” limited-slip units, helical units, and lockers closely enough that a later summary could accidentally treat them as synonyms. They also record a detailed GM/Eaton governor-and-cam sequence and a useful bearing-noise pitch comparison.

### GM/Eaton mechanical locker: the class sequence is substantially correct

**DOCUMENTED:** GM's 2026 Sierra 2500/3500HD service material describes the G80 locking differential as having clutch packs, a governor, latching bracket, and cam plate. Under normal conditions it has some limited-slip action from side-gear separating force. At a wheel-to-wheel difference of 100 rpm or more, a governor flyweight catches the stationary bracket, slows the cam plate relative to the cam side gear, moves the cam out of detent and up its ramps, and applies the clutch packs with a self-energizing action. Above approximately 20 mph, the latching bracket is moved out of the flyweight path so lockup cannot begin.[^43]

**DOCUMENTED:** Eaton's current MLocker description independently states the same high-level chain: more than 100 rpm wheel-speed difference opens the flyweight mechanism, the latching bracket stops it, a self-energizing clutch system ramps the cam plate against a side gear, and ramping continues until both axles reach the same speed. Eaton describes the normal state as light-bias limited slip and the lock/unlock action as automatic.[^44]

**INFERRED — class-guide use:** The notes' event order is sound after tightening the wording. The governor does not simply “lock itself”; the caught flyweight/latch changes the relative cam motion that starts self-energizing clutch apply. “Open until wheel slip” is a useful simplification, but the cited versions describe light-bias limited-slip action in normal operation. Preserve the instructor's roughly-20-mph lockout point as application-specific GM/Eaton logic, not a universal locker rule.

### Limited slip, selected lock, and automatic lock are different mechanisms

**DOCUMENTED:** Eaton says its ELocker is open until commanded and uses electromagnetic actuation to lock one side gear to the differential case. Eaton explicitly notes that the locking components vary between models and generations.[^45] Eaton separately distinguishes MLocker, ELocker, and Detroit Locker behavior: MLocker normally runs open/light-bias and automatically locks after low-speed wheel difference, ELocker is driver-selectable, and Detroit Locker is normally locked with automatic differentiation/unlocking behavior in turns.[^46]

**DOCUMENTED:** Torsen describes its unit as a helical-gear, torque-biasing differential. Applied torque produces gear thrust against the case, creating proportional friction; the unit can bias torque while still differentiating smoothly at low torque. That supports classification as a helical limited slip, not a full locker.[^47]

**DOCUMENTED:** GM's 2026 Yukon service material supplies another useful contrast: one electronically controlled limited-slip design uses a control module and motor to apply a multidisc friction clutch through reduction gearing. That is an electronically controlled clutch limited slip, not evidence that every electrically actuated locker uses clutch packs.[^48]

**INFERRED — correction boundary:** Keep the raw notes unchanged, but future guides should not teach that “Positraction,” Torsen, ELocker, air locker, and Detroit Locker are one mechanism. A clutch limited slip resists differentiation, a helical limited slip creates a torque-bias ratio through gear thrust/friction, and a locker positively couples both outputs to the case when locked. Electric or pneumatic describes the actuator; it does not by itself establish the internal locking member.

### Noise observations choose the next check; they do not finish the diagnosis

**DOCUMENTED:** Timken's wheel-hub diagnostic material tells the technician to consider road surface, tread design, wear, and alignment before condemning a hub, then check the wheel/hub for roughness, looseness, and noise. Its symptom guide says a bearing-related rumble/growl may intensify with a slight steering input, while a clunk on acceleration/coast reversal more strongly suggests driveline play than a hub bearing.[^49]

**RECORDED CLASS EMPHASIS:** The updated notes distinguish the faster pinion-bearing pitch from slower carrier and axle-bearing sounds because the pinion rotates faster. They also say carrier noise may require load and may fade on a lift, while axle/wheel-bearing noise can respond to a controlled swerve. These are useful first directions. This pass did not locate a current manufacturer source that makes the pitch-rate observation a universal component-identification rule.

**INFERRED — guide use:** Present the sound, speed relationship, torque condition, cornering load, road surface, and lift result as a bundle. “Whine equals gears” and “growl equals bearings” are starting classifications. A load-sensitive whine fading in float strengthens a tooth-contact direction; a faster speed-linked growl strengthens a pinion-bearing direction; a cornering response keeps axle/wheel bearings high on the list. None is a one-observation teardown authorization.

### What these continuations add and leave open

Fourteen technical sources and two resource leads have been added across the September 16 and September 18 continuations, for 49 indexed sources total. Three primary-source PDFs are available locally. The useful additions are a worked planetary reduction, contrasting AWD torque paths and actuators, mode-state interpretation, a located synchronizer measurement, examples separating shift complaints, a current GM/Eaton locker sequence, traction-device boundaries, and source-backed wheel-bearing confirmation checks.

This narrows the mechanism and inspection work supporting G02/G06/G10 and the transfer-case engagement questions. It does not close G03's need for application-matched axle-pattern practice, identify the lab transmission, establish current vehicle-specific service instructions, or audit the unfinished rear-axle notes. Source count is an inventory, not a measure of readiness.

## Use in the eventual preparation packages

| Future output | Contribution | Boundary |
|---|---|---|
| Class-final preparation, 2026-09-21 | Primarily the completed class notes and the instructor's textbook coverage; researched GM examples can clarify a specific mechanism. | Do not expand the Monday review to match professional ASE breadth. |
| ASE A3 preparation | Contrasting designs test whether the explanation transfers beyond one manufacturer or assembly. | A manufacturer example establishes possibility, not exam frequency. |
| Power-flow visuals | Separate shaft support, relative rotation, and torque transmission. | Build the final diagram from an identified design. |
| Diagnostic practice | Use service history and observations to identify the next confirming check. | Do not present constructed examples as real ASE questions. |

These additions are source-backed ingredients for later synthesis. They should be combined with the complete semester material when it becomes available, with application-specific details labeled at the point of use.

## Remaining research boundaries

The September 13 assessment prioritized worked diagrams and measurements for G01–G03. **Refined September 16 after Logan's experience clarification:** focus additional depth on mechanical measurements, axle setup, and unfamiliar transfer-case mechanisms. Keep G01 as a brief drivetrain application check that uses Logan's established electrical knowledge. Another broad rewrite of the clutch and synchronizer explanations is not justified by these findings.

The open work is specific: application-matched contact-pattern practice; the exact lab shaft-layout/pilot-support diagram; current application-specific pump/cooler tests and limits; axle/hub/retainer inspection procedures; and distinct viscous, vacuum, hydraulic, and electrical engagement examples. The Corvette, TR-4050, rotation/load, and historical GM cooler findings above narrow several questions without closing these remaining items. No access to the course's complete textbook, lab transmission identification, or current paid OEM service system was assumed.


## Sources

Sources 1–24 were accessed September 13, 2026 (America/Denver); sources 1–2 were rechecked September 16. Sources 25–42 were accessed September 16. Sources 43–49 were accessed September 18. Undated pages are identified as such. Historical service documents support only their stated applications; no claim is made that they are the latest repair instructions for every affected vehicle.

[^1]: National Institute for Automotive Service Excellence. [Automobile & Light Truck Certification Tests, A1–A9](https://ase.com/tests/a1-a9/), current page, “Test Times and Number of Questions.” Exam timing and scored/research-question distinction.

[^2]: National Institute for Automotive Service Excellence. [ASE Automobile Study Guide](https://ase.com/wp-content/uploads/ASE_Automobile_Study_Guide.pdf), ©2026, printed pp. 16–20. A3 coverage anchors, published category table, and sample-question scope. Consult the original for full task wording.

    Local unmodified copy: [ASE Automobile Study Guide 2026](sources/ase/ASE_Automobile_Study_Guide_2026.pdf), retrieved September 16, 2026. A3 example pages 19–20 were rendered and visually inspected during this pass.

[^3]: Fluke. [Diagnosing Voltage Drops: Electrical Automotive Troubleshooting](https://www.fluke.com/en/learn/blog/automotive/electrical-automotive-troubleshooting), undated, “Voltage Drop Tests” and “Basic Procedures.” Loaded-circuit measurement principles.

[^4]: General Motors. [GM TechLink, Mid-March 2017](https://gm-techlink.com/wp-content/uploads/2017/05/GM_TechLink_06_Mid-March_2017.pdf), Vol. 19, No. 6, p. 2, “Missing Connector Seals.” Historical, specified 2015–2017 4WD applications.

[^5]: Chrysler/Mopar. [Tech Tip TT9003917: DT Transfer Case](https://starparts.chrysler.com/tech_tips/en/TT9003917_en_US.html), undated, 2019 DT application. Range-position sensor seating and C1403-92.

[^6]: TREMEC. [T-5 Service Manual](https://tremec.com/wp-content/uploads/2023/05/TRSM-T5-0510-R1_173.pdf), identifier TRSM-T5-0510-R1; issue date not independently established. Table 2-1 and §§6-8–6-9 (printed pp. 6-3; PDF p. 54). T5-specific troubleshooting and WC countershaft shim calculation.

[^7]: Chrysler. [Safety Recall P77: Rear Axle Pinion Nut](https://static.nhtsa.gov/odi/rcl/2014/RCRIT-14V796-3657.pdf), NHTSA campaign 14V-796, service instructions, pp. 24 and 27–31. Historical, application-specific turning-torque, backlash, and pattern procedures; not a recall-status assessment.

[^8]: ZF Aftermarket/SACHS. [Clutches for Passenger Cars and Light Commercial Vehicles](https://aftermarket.zf.com/en/aftermarket-portal/our-portfolio/passenger-cars/products/clutches/), undated, “Function of a hydraulic release system with CSC.” Continuous-contact release-bearing design.

[^9]: EXEDY Aftermarket. [Abnormal sound with foot off clutch pedal](https://www.exedy-aftermarket.com/en/troubleshooting/abnormal-sound/?from_cate=35), undated, cause and solution. Release-mechanism noise disappearing with pedal pressure.

[^10]: ZF Aftermarket/SACHS. [Clutch Noise](https://aftermarket.zf.com/en/aftermarket-portal/knowledge-hub/clutch-noise/), undated, “Wear-induced grooves on inner ring of clutch releaser.” Preload, guide-tube wear, and alignment effects.

[^11]: Honda. [Active Torque Transfer System (ATTS) Technology – 1996](https://global.honda/en/tech/serial/Honda_Super_Handling_part02/?from=serial_top), undated retrospective, discussion of dedicated front suspension and kingpin offset. Torque-steer mechanism in that application.

[^12]: American Honda. [2026 Civic Type R: Dual-Axis Front Suspension](https://www.hondainfocenter.com/2026/Civic-Type-R/Feature-Guide/Engine-Chassis-Features/Dual-Axis-Front-Suspension/), 2026 model feature guide. Steering geometry and torque-steer reduction.

[^13]: TREMEC. [Up Close Look at the TREMEC-equipped Ford Mustang Dark Horse](https://tremec-blog.com/up-close-look-at-the-tremecequipped-ford-mustang-dark-horse/), article concerning the 2024 model; publication date not established from retrieved text. Used solely for the manual-transmission cooler example.

[^14]: Eaton. [Eaton Posi FAQs](https://automotive.eaton.com/us/en-us/products/differentials-traction-control/aftermarket-differentials/posi-faqs.html), undated, lubricant/additive question. Product-specific friction-modifier guidance.

[^15]: Eaton. [Detroit Truetrac FAQs](https://automotive.eaton.com/us/en-us/products/differentials-traction-control/aftermarket-differentials/detroit-truetrac-faqs.html), undated, lubricant and lockup questions. Helical limited-slip operation and modifier qualification.

[^16]: Dana/Spicer. [Measuring Angles](https://spicerparts.com/anglemaster/measuring-angles), undated. Shaft slopes, joint angles, and vehicle loading.

[^17]: Dana/Spicer. [Driveline Operating Angle Calculator](https://spicerparts.com/en-emea/calculators/driveline-operating-angle-calculator), undated. Explicit limitation regarding horizontal offsets/compound angles.

[^18]: Brian Dengel, KHK-USA. [What Is a Gear Engineer?](https://khkgears.us/media/k3ffqesf/gear-solutions_khk_what-is-a-gear-engineer.pdf), *Gear Solutions*, September 2019, pp. 32–33. Manufacturer-authored explanation of simple and two-stage trains and idler behavior.

[^19]: Chevrolet. [2014 Corvette brochure](https://cdn.dealereprocess.org/cdn/brochures/chevrolet/2014-corvette.pdf), 2014 model publication, PDF p. 13, “7 Speeds, One Driver.” Manufacturer-authored brochure accessed through a dealer-publication mirror; supports rear-transaxle configuration.

[^20]: Chevrolet / GM Genuine Parts. [Manual Transmission Clutch Pilot Bearing, 12557583](https://parts.chevrolet.com/product/gm-genuine-parts-manual-transmission-clutch-pilot-bearing-12557583), undated current catalog page, “Fits these vehicles.” Used for the listed Corvette application, not as a vehicle-specific installation drawing or purchasing recommendation.

[^21]: Team TREMEC. [Manual Transmission Synchronizers 101](https://tremec-blog.com/manual-transmission-synchronizers-101/), January 31, 2019; page also displays October 25, 2023. Typical synchronizer sequence and common output-shaft arrangement.

[^22]: TREMEC. [TREMEC Two-Wheel-Drive TR-4050 5-Speed Transmission Available Soon](https://tremec-blog.com/tremec-two-wheel-drive-tr-4050-5-speed-transmission-available-soon/), 2022 announcement referring to May 30 availability. Countershaft-mounted fifth-gear synchronizer and GM/Ford application variants. Used for design, not current availability.

[^23]: Eaton. [UltraShift PLUS Service Manual TRSM0940: Power Flow](https://productinfo.serviceranger4.com/books/TRSM0940/lang/en-us/section/SM0940PowerFlow), March 2024-A, front-section power flow and direct gear. Heavy-duty application used only to explain rotation versus load.

[^24]: General Motors. [GM TechLink, January 2011](https://static.oemdtc.com/TechLink/TechLink2011Jan.pdf), printed p. 5, “Manual Transmission Service Tips.” Manufacturer-authored newsletter accessed through OEMDTC's mirror. Historical cooler restriction, repeat failure, and fluid-handling context; not confirmation of current application-specific instructions.

[^25]: ASE. [Official ASE Practice Test Program](https://ase.com/official-ase-practice-test-program/), current public page. A3 length, explanations/report, single question set, and redemption window. Paid test content was not accessed.

[^26]: ASE. [Test Prep & Training Overview](https://ase.com/test-prep-and-training/), current public page, “Practice Test Pricing” and “Officially Licensed Test Prep Partners.” Price is a dated observation, not a purchase or a guarantee of future pricing.

[^27]: ASE Education Foundation. [Entry-Level Testing](https://www.aseeducationfoundation.org/schools/entry-level/), current resource hub. Establishes the separate program and links to the documents in sources 28–30.

[^28]: ASE / ASE Education Foundation. [Automobile Entry-Level Individual Test Specifications and Task Lists](https://www.aseeducationfoundation.org/wp-content/uploads/Auto_Test_Specs_Individual-8_2022.pdf), effective July 1, 2023, revised May 8, 2023; printed pp. 6–8. The filename contains 2022; the internal effective/revision dates govern this description. MD allocation and threshold are entry-level only.

[^29]: ASE. [Study Guide for the Automobile Entry-Level Certification Tests](https://www.aseeducationfoundation.org/wp-content/uploads/Auto-Study-Guide_.pdf), revised November 19, 2023; specifications effective July 1, 2023. Printed pp. 4–7 explain question formats and test-taking methods; pp. 13–15 cover MD. PDF page numbers are two higher than printed numbers. Linked by the Foundation as of September 16, 2026.

[^30]: ASE. [Guide for Interpreting Results and Technical Data for the 2026 ASE Entry-Level Certification Tests](https://www.aseeducationfoundation.org/wp-content/uploads/GuideforInterpretingResults.pdf), ©2026. Preface and printed p. 18 (PDF p. 19), MD table and passing threshold. Not a professional A3 score-conversion guide.

[^31]: ASE. [ASE Certification: Need to Know](https://ase.com/wp-content/uploads/ASE_CertificationNeedtoKnow.pdf), revised January 2026, printed pp. 3 and 5. Professional test purpose, task relationships, technical review, and statistical pretesting. Current link followed from the A-series page.

[^32]: ASE. [What to Expect at the Testing Center](https://ase.com/what-to-expect/), current page, “Test Questions,” “Taking the Test,” and “Test Time Limit.” Answering, flagging, review, and submission behavior.

[^33]: ASE. [Free Test Drive](https://ase.com/free-test-drive/), current page. Locates the testing-platform video demonstration and webinar; linked videos were not reviewed during this pass.

[^34]: KHK. [ABCs of Gears](https://khkgears.us/media/fqrlut1m/abcs-of-gearing-b.pdf), undated illustrated manufacturer primer; printed pp. 6–7, formula 1.4 and figure 1.5 (PDF p. 4). Planetary page visually inspected. [Local unmodified PDF](sources/drivetrain/KHK_ABCs_of_Gears.pdf).

[^35]: Christian Månsson, Måns Ranåker, and Per Söderberg, BorgWarner. [Next Generation AWD Actuators](https://www.borgwarner.com/docs/default-source/default-document-library/next-generation-awd-actuators.pdf), BorgWarner Knowledge Library, 2020, printed pp. 1–4; figure 1 on PDF p. 2 visually inspected. [Local unmodified PDF](sources/drivetrain/BorgWarner_AWD_Actuators_2020.pdf).

[^36]: TREMEC. [TR-3550 and TKO Transmissions Service Manual](https://tremec.com/wp-content/uploads/2023/05/TRSM-TKO-0711-R1_3.pdf), identifier TRSM-TKO-0711-R1; issue date not independently established. Printed p. 43, inspection items 11–12 (PDF p. 46), visually inspected. The web upload path is not treated as a revision date. [Local unmodified PDF](sources/drivetrain/TREMEC_TR3550_TKO_Service_Manual.pdf).

[^37]: BorgWarner. [New Electro-Mechanical On-Demand Transfer Case Powers 2019 Ram 1500 4x4 Pickup Trucks](https://www.borgwarner.com/newsroom/press-releases/2018/03/27/borgwarner-s-new-electro-mechanical-on-demand-transfer-case-powers-2019-ram-1500-4x4-pickup-trucks), March 27, 2018. Named EMOD actuation and preemptive clutch control; not current product availability.

[^38]: General Motors. [GM TechLink, February 2023](https://gm-techlink.com/wp-content/uploads/2023/05/GM_TechLink_03_February_2023.pdf), printed pp. 4–5, “When to Operate Four-Wheel Drive.” Mode operation and completion indicators for the systems discussed. Text reviewed; no vehicle-specific shift procedure is prescribed here.

[^39]: Mazda. [Service Bulletin 05-001/15](https://static.nhtsa.gov/odi/tsbs/2015/SB-10100794-2532.pdf), January 5, 2015, pp. 1–3, via NHTSA. Specified 2012–2015 Mazda3, 2013–2015 CX-5, and 2014–2015 Mazda6 SKYACTIV six-speed applications with VIN limits. Used for the documented complaint/design relationship, not to authorize a repair on other vehicles.

[^40]: TREMEC. [Product Support FAQ](https://tremec.com/aftermarket/resources/product-support-faq/), undated current page; gear clash, lubricant compatibility, and reverse-gear design explanations. Actual application specifications remain necessary.

[^41]: Weber State University. [Professor John D. Kelly](https://www.weber.edu/automotive/j_kelly.html), current faculty page and linked teaching channel. Resource discovery only; no individual video's claims were reviewed in this pass.

[^42]: James Halderman. [A3 Animation Library access route](https://jameshalderman.com/a3_anim_lib_page/), attempted September 16, 2026; redirected to restricted-access notice. Resource lead only, not inspected instructional content or evidence for a technical claim.

[^43]: General Motors. [2026 Sierra 2500/3500HD Electrical Body Builder Manual / Service Manual](https://www.gmupfitter.com/wp-content/uploads/2025/09/Sierra-2500-3500HD-Electrical-Body-Builder-Manual-Service-Manual-2026_en_US.pdf), Rear Drive Axle, printed pp. 4-4–4-5. Current application-specific G80 components, limited-slip action, governor/latch/cam sequence, full lock, and approximately-20-mph lockout.

[^44]: Eaton. [MLocker mechanical locking differential](https://www.eaton.com/nz/en-gb/catalog/differentials/MLocker.html), current product page, “Automatic operation.” Wheel-speed threshold, flyweight/latch, self-energizing cam-and-clutch action, automatic full lock and release.

[^45]: Eaton. [Eaton ELocker FAQs](https://automotive.eaton.com/us/en-us/products/differentials-traction-control/aftermarket-differentials/elocker-faqs.html), current page, “What locking mode(s) does an ELocker have?” Open normal state, electromagnetic actuation, side-gear-to-case lock, and model/generation variation.

[^46]: Eaton. [What is a locking differential?](https://automotive.eaton.com/us/en-us/products/differentials-traction-control/locking-differentials.html), current page. Distinguishes MLocker, Detroit Locker, and driver-selectable locker operating strategies. Used for product-family contrast, not a universal service procedure.

[^47]: JTEKT Torsen. [How It Works](https://torsen.com/how-it-works/), current page. Helical gearing, torque bias ratio, gear thrust, case friction, and continued low-torque differentiation.

[^48]: General Motors. [2026 Yukon/Yukon XL Electrical Body Builder Manual / Service Manual](https://www.gmupfitter.com/wp-content/uploads/2025/09/Yukon-Yukon-XL-Electrical-Body-Builder-Manual-Service-Manual-2026_en_US.pdf), Rear Drive Axle, printed p. 4-5, G96 description. Current GM example of module/motor-controlled multidisc-clutch limited slip.

[^49]: Timken. [Checking a Hub Bearing Assembly](https://www.timken.com/resources/md15-checking-a-hub-bearing-assembly/) and [Symptoms of a Worn Wheel Hub Bearing](https://www.timken.com/wp-content/uploads/2017/08/LV5-Symptoms-of-a-Worn-Wheel-Hub-Bearing.pdf), current resource page and light-vehicle TechTip. Road/tire confounders, turning response, and physical roughness/looseness/noise checks.

Local evidence: `deep-research-report (3).md` (Downloads and identical project copy), `clutchsection.txt`, `gears.txt`, `unit2_study_guide.md`, and `unit2_cram_sheet.md`, as present September 13, 2026. Section names and line references are provided in the gap register. These files document the existing material; their contents are not treated as independent verification of technical claims.

September 18 local context: `drive-axles.txt` was reviewed through the newly added locker and expanded noise-diagnosis material. `unit2 exam.pdf` was observed in the directory and was previously inspected for instructor question style, not as technical evidence for the official-ASE research. No copied Unit 3 exam was visible during this update.
