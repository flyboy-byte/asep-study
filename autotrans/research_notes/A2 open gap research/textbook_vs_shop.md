# A2 textbook/ASE answer vs. shop habit (research notes, 2026-09-30)

Scope: where the by-the-book answer on ASE A2 differs from common shop or dealership habit, for a GM ASEP student with about 2 years of dealership experience, 7 ASE passes and strong electrical skills. This is research input only. It is not a guide and not a question bank. No secure ASE item was sought, copied or paraphrased. The only ASE item content referenced is the public sample-question topic list already summarized in `../../research.md` (lines 31-40), from the public ASE Automobile Study Guide.

Evidence tags: **DOCUMENTED** (a primary or reliable secondary source says it), **DOCUMENTED (snippet)** (seen only in search-result snippets because the proxy blocked full-page fetches; corroborated where noted), **INFERRED** (reasoning from documented facts), **OPEN** (unresolved), **ANECDOTAL** (forum or individual report). All URLs accessed 2026-09-30. Task numbers refer to the 2026 A2 task list mapped in `../../research.md`.

Network note: one WebFetch was tried (shoppress.dormanproducts.com), and the egress proxy blocked it. Everything below comes from search snippets, from the local ASE guide summary in `research.md`, or from reasoning. Verify any procedure number against GM SI before it goes into a guide.

---

## Q1. Which shop-habit vs. by-the-book contrasts apply to A2, and what is the correct reasoning for each?

### Takeaway
Most of the candidate contrasts hold up. The thread running through all of them: ASE rewards the documented diagnostic sequence (verify the concern, check fluid correctly, check SI/TSBs, scan, then test before replacing) and the manufacturer-approved procedure. It does not reward the fastest shop shortcut. Two candidates need care. "Pressure test before stall test" is not a universal order, and the stall test is manufacturer-dependent. Legacy hydraulic topics are only partly visible in the 2026 task list.

### Cited Findings

**C1. Clearing codes: battery disconnect vs. scan tool (A.6, A.7)**
- DOCUMENTED: One of the 8 public A2 sample questions in the ASE study guide makes this point. When DTCs need to be cleared, the correct method is the scan tool, not disconnecting the battery or the TCM or pulling the TCM fuse. — [ASE Automobile Study Guide (© ASE 2026)](https://ase.com/wp-content/uploads/ASE_Automobile_Study_Guide.pdf); summarized locally in `research.md` line 38; search snippet confirms the wording.
- DOCUMENTED (snippet): A battery disconnect may clear only volatile memory. Stored DTCs in non-volatile memory can remain, and a battery disconnect also resets readiness monitors and learned values. — [Battery Life Lab](https://batterylifelab.com/does-disconnecting-battery-clear-codes/); [Boston.com Car Doctor](https://www.boston.com/cars/how-to/2024/12/17/car-doctor-is-it-a-bad-idea-to-disconnect-a-battery-to-clear-a-check-engine-light/). Secondary sources. The monitor reset point is corroborated by the OBD II readiness sources already in `research.md` line 142.
- INFERRED: The book sequence is: record DTCs and freeze frame, repair, clear with the scan tool, run the monitors or drive cycle, then verify (A.7). Permanent DTCs on 2010+ vehicles clear only after the monitor passes, so a battery pull cannot "fix" them.

**C2. Verify the concern first (A.2, A.8, A.16)**
- DOCUMENTED (snippet): GM Strategy Based Diagnostics says the first step is always "Understand and Verify the Customer's Concern" and the last step is always "Repair Verification." In between come preliminary checks (visual inspection, vehicle history, sounds and odors, recording DTC information), a search of SI for bulletins and PI, and a Vehicle Diagnostic System Check. — [GM service bulletin hosted by NHTSA, 2019](https://static.nhtsa.gov/odi/tsbs/2019/MC-10168204-9999.pdf); [GM bulletin, 2022](https://static.nhtsa.gov/odi/tsbs/2022/MC-10210543-0001.pdf); [Saab (GM-era) WIS Strategy Based Diagnostics](https://saabwisonline.com/9-4x/2011/3-electrical-system/bus-and-diagnostics-communication/fault-diagnosis-general/strategy-based-diagnostics). The GM bulletins are primary sources seen via snippet, and two GM documents agree.
- INFERRED: The shop habit is to jump from the RO line to a known pattern failure. The ASE answer to "what should be done first" is usually to verify the concern, check fluid, or do a visual inspection, unless the stem says that has already been done.

**C3. Check SI, TSBs and history before diagnosing (A.3, A.14)**
- DOCUMENTED (snippet): The GM SBD preliminary checks include searching SI for bulletins and preliminary information. — [GM bulletin (NHTSA)](https://static.nhtsa.gov/odi/tsbs/2019/MC-10168204-9999.pdf).
- DOCUMENTED (snippet): A commonly cited pitfall is that techs draw on "a shortcut or an unapproved procedure that may have been developed in their shop or on social media" that is "not the industry-approved or manufacturer's way of doing it." — [Dorman Shop Press, "Seven tips to help you pass your ASE exams"](https://shoppress.dormanproducts.com/ase-test-taking-tips/) (full page blocked; snippet only).

**C4. Check fluid first, at the correct temperature and by the SI method (A.4, A.10, B.12)**
- DOCUMENTED: One public A2 sample question tests the fluid check on a unit with no dipstick: fluid temperature read on a scan tool, with the vehicle level. — `research.md` line 33, from the [ASE study guide](https://ase.com/wp-content/uploads/ASE_Automobile_Study_Guide.pdf).
- DOCUMENTED (snippet): GM 6L80/6L90 has no dipstick on some applications. Level is correct when fluid drips from the level-control (check) plug with the engine idling, the vehicle level, and the transmission shifted through the ranges. One aftermarket installation sheet lists an initial-fill TFT window of 86-122 °F and a Service Fast Learn window of 158-212 °F. — [Run-Rite 6L80/6L90 bulletin CPTB0059](http://run-rite.com/wp-content/uploads/2023/11/CPTB0059.pdf); [Summit / VRE installation sheet](https://static.summitracing.com/global/images/instructions/vre-8100a-jmb.pdf); [EFILive 6L80E fluid check](https://efilive.co.uk/6l80e-fluid-check.html). CONFLICT/OPEN: forum and GM-derived figures differ, and GM's commonly quoted check window is narrower. Take the exact TFT window from GM SI for the unit, not from these sheets.
- DOCUMENTED (snippet): "Before conducting a stall test, you should check the fluid level and condition." A general diagnostic sequence is fluid first, then scan data, then mechanical testing, then electrical testing. — [Apex Technation diagnostic workflow](https://apextechnation.com/articles/automatic-transmission-diagnostic-workflow) (secondary prep site); consistent with [AA1Car, Automatic Transmission Diagnosis & Repair](https://www.aa1car.com/library/2003/ic60340.htm).
- INFERRED: The shop habit is to eyeball the dipstick at any temperature, or to skip the check on a sealed unit. The book answer is: correct temperature from the scan tool, vehicle level, engine running if specified, the method the SI names, and fluid type confirmed (A.4 explicitly includes type). Low fluid is the "simplest cause consistent with the symptoms" for many slip, delay and noise stems.

**C5. Rule out engine and inputs before condemning the transmission (A.22, A.23, A.9)**
- DOCUMENTED: One public A2 sample question attributes a harsh upshift to a failed TPS input. — `research.md` line 35.
- DOCUMENTED (snippet): TCC shudder is easily confused with an engine misfire or a bad mount. Misfire vibration passes through a locked converter, and a P0300 can appear alongside a converter issue. The way to tell them apart is to compare engine and transmission data: TCC slip rpm during the event versus misfire counters, and whether the vibration follows lockup. — [Gears Magazine, "Shudder Diagnosis"](https://gearsmagazine.com/magazine/shudder-diagnosis/); [Auto Barn shudder page](https://www.autobarn.net/symptoms/transmission-shudder); [Monster Transmission 6L80E shudder](https://monstertransmission.com/blogs/news/6l80e-torque-converter-shudder-causes-fixes-monster). These are two or more secondary or industry sources.
- INFERRED: The ASE task wording itself ("differentiate between transmission and engine/ABS/ADAS/transfer case concerns," A.22) signals that ASE expects the non-transmission cause to be ruled out. The shop habit of "it's a trans RO, so it's the trans" works against this.

**C6. Don't reset adapts as a "fix" (A.23, C.6)**
- DOCUMENTED (snippet): Resetting adaptations when a mechanical fault is present can mask the problem or make it fail sooner. Don't reset with active DTCs, suspected internal damage, degraded fluid, or slipping from worn clutches. A reset belongs after an actual repair, when the learned values no longer match the hardware. — [Crown Auto adaptation reset guide](https://crownautoservice417.com/automotive-knowledge-center/repair-library/transmission/transmission-adaptation-reset-guide/); [Foxwell adaptation reset](https://www.foxwelldiag.com/blogs/car-diagnostic/transmission-adaptation-reset). Secondary sources; they agree.
- DOCUMENTED (snippet): GM units call for a Service Fast Learn after certain services and repairs. — [Summit / VRE 6L80 sheet](https://static.summitracing.com/global/images/instructions/vre-8100a-jmb.pdf). See also `tcm_programming_relearn.md`.
- INFERRED: Maxed-out adapt values are diagnostic data. They point to wear, a leak or low pressure. They are not the fault to clear. Learner's raw note (`electronics.txt`, "reset adapts after replacement") is consistent with this: a reset follows a repair.

**C7. Pressure test vs. stall test: order, when, and safety limits (A.11, A.12)**
- DOCUMENTED (snippet): Typical OEM stall-test procedures limit wide-open throttle to 5 seconds or less. Between tests, cool down in N or P at idle for at least 1 minute. Exceeding the limit damages the ATF, engine oil and clutches. Parking brake and service brake applied, wheels chocked. — [Subaru 4AT stall test (FSM)](http://ken-gilbert.com/wrx/STi_Manual/04.%20TRANSMISSION/02.%20AUTOMATIC%20TRANSMISSION/05.%20Stall%20Test.pdf); [Hyundai TSB via NHTSA](https://static.nhtsa.gov/odi/tsbs/2019/MC-10170511-9999.pdf); [Allison AT 540 manual](https://www.manualslib.com/manual/2887156/Allison-Transmission-At-540.html?page=49). Multiple OEM sources agree.
- DOCUMENTED (snippet): Guidance commonly says to check with the manufacturer before stall testing because the test stresses the transmission. — [freeasestudyguides, torque converter stall test](https://www.freeasestudyguides.com/torque-converter-stall-test.html) (secondary). OPEN: I found no GM document in snippets stating that GM prohibits stall testing on current units. Many shop techs believe GM doesn't publish stall tests for modern units. Treat that as unverified until checked in GM SI.
- DOCUMENTED (snippet): Pressure testing is indicated for hydraulic complaints (slip, no movement, a pressure-related code, maxed adapts, or a stall result suggesting slip). It isn't needed for every complaint; many electrical and solenoid faults are resolved without it. — [Apex Technation workflow](https://apextechnation.com/articles/automatic-transmission-diagnostic-workflow) (secondary).
- INFERRED: "Always pressure test before stall test" isn't a documented universal rule. The documented rules are: fluid level and condition first, then road test and scan data, then pressure test for hydraulic concerns. A stall test is done only if the manufacturer publishes one, with the time and cool-down limits observed. A stall-test question on ASE will reward knowing the safety limits and what high or low stall speed means (see `stator_owc_diagnosis.md` and `hydraulic_pressure_testing.md`).

**C8. Inspect and measure vs. replace the whole unit or valve body (A.11, B.6, B.8, C.8, C.10, C.19-C.21)**
- DOCUMENTED (snippet): An air test substitutes low-pressure air (about 20-50 psi, often 40 psi max to protect seals) for fluid, through the case passages with the valve body removed, to find a leaking clutch or servo circuit. Listen or feel for apply. It is done both in diagnosis and after rebuild. — [freeasestudyguides pressure tests](https://www.freeasestudyguides.com/automatic-transmission-pressure-tests.html); [Jeep/Mopar clutch air pressure test page](https://s3.amazonaws.com/jeepwranglerjk2010/7c033609.html). Two sources agree on the method; the psi figure varies by source.
- DOCUMENTED: The end-play and clutch-clearance measurement method (dial indicator, selective snap rings, washers or shims) is already logged in `research.md` line 146, sourced to [Sonnax](https://www.sonnax.com/tech_resources/81-clutch-release-clearance-101) and [Transmission Digest](https://www.transmissiondigest.com/all-work-and-no-play-setting-endplay-to-prevent-4l60-e-gear-train-failure/).
- INFERRED: Dealership warranty practice often replaces the transmission assembly or the control valve body/TEHCM, so a dealership tech may never measure clearance or air test. Area C (15%, 23 tasks) is written almost entirely as inspect, measure and adjust. Answers should assume the tech measures to spec and then decides. Weight check: Area C is lower-yield per task, so learn these as methods, not specs.

**C9. Flush and flow-test the cooler after a failure (B.5, C.4)**
- DOCUMENTED (snippet): A manufacturer TSB says that every labor operation that removes the transmission for an internal repair or converter replacement includes time to flow-check and flush the cooler system. In-car TCM, valve body or seal work does not require it. — [NHTSA-hosted TSB MC-10113664, "Automatic Transmission Oil Cooler Flow Test Essential"](https://static.nhtsa.gov/odi/tsbs/2015/MC-10113664-9999.pdf). OPEN: the snippet didn't name the OEM. INFERRED from the wording that it is likely GM; confirm.
- DOCUMENTED (snippet): Remanufacturer warranty sheets say a restricted or contaminated cooler system is the "#1 cause" of failure after replacement. Plate-type oil-to-air coolers must be replaced, and a cooler with hard-parts debris must be replaced. Skipping the flush voids the warranty. — [ETE 4L60 installation guide](https://s3.amazonaws.com/ete-assets/pdf/IG_4L60.pdf); [Summit/VRE installation guide](https://static.summitracing.com/global/images/instructions/vre-6900aa.pdf). Two reman sources agree.
- DOCUMENTED: One public A2 sample question ties an over-temperature message with normal shifting to a restricted cooler. — `research.md` line 36.

**C10. Converter seating and pump engagement (C.2, C.3, C.18)**
- DOCUMENTED (snippet): The converter must engage the input shaft splines, the stator support and the pump drive, usually felt as distinct "clunks" while rotating and pushing it in. After seating, measure from the bellhousing face to the converter mounting pads and compare with spec. Published figures vary (for example TCI 1-1/8 in and a Munroe text 0.500 in), so use the unit's spec. — [Ashcroft Transmissions technical library](https://ashcroft-transmissions.co.uk/technical-library/?technical_library_product=1298); [ClassicBroncos thread (ANECDOTAL)](https://classicbroncos.com/forums/threads/flexplate-torque-converter-distances-questions.265354/); [Trifive thread (ANECDOTAL)](https://www.trifive.com/threads/is-my-torque-converter-seated-in-far-enough.190154/).
- INFERRED: The book trap is that a converter pulled in with the bolts cracks the pump. The correct answer is to verify seating by measurement and check that the converter moves freely against the flexplate before installing bolts. Don't use the bolts to draw the transmission to the engine.

**C11. "Most likely" means the most common or simplest cause consistent with all the symptoms**
- DOCUMENTED (snippet): Prep guidance: when a question asks for the most likely cause, several answers may be technically possible; pick the most probable one given the stated symptoms. ASE tests competent-technician knowledge, not edge cases, and "if the straightforward answer seems too easy, it is probably correct." — [Apex Technation practice-test guide](https://apextechnation.com/articles/ase-certification-practice-test); [Apex Technation test-day strategy](https://apextechnation.com/articles/ase-test-day-strategy). This is a secondary commercial prep site; ASE itself doesn't word it this way, but the public sample questions follow this pattern (`research.md` line 40).
- INFERRED: Every symptom in the stem has to be explained. Example structure from the public samples: poor launch but normal above 35 mph fits a stator OWC, not general slip. A single-range failure is isolated to the element used only in that range (apply chart, sample no-reverse item). An experienced tech's "I've seen the rare one" answer usually fails to explain one of the stated symptoms, or ignores a simpler cause.

**C12. Replace vs. repair decisions**
- DOCUMENTED (snippet): Manufacturer warranty labor can require specific operations with replacement, such as the cooler flush above. — [NHTSA-hosted TSB](https://static.nhtsa.gov/odi/tsbs/2015/MC-10113664-9999.pdf).
- INFERRED: No public source was found stating an ASE "rule" on replace vs. repair. The task list verbs (inspect, measure, test, determine needed action) imply ASE wants replacement justified by a test result, not by labor-time economics.

### Inferences
- The largest scoring risk for a dealership tech is procedural sequence (C2-C4) and measurement-based Area C thinking (C8, C10). Electrical knowledge (the learner's strength) helps with C1, C5 and C6.
- Official ASE sample questions directly reflect C1, C4, C5, C9 and C11. Those contrasts carry the best evidence.

### Gaps
- No GM SI access, so the GM stall-test policy, the exact 6L80/8L/10L fluid-check TFT windows, and GM converter-seating specs aren't verified (OPEN).
- The OEM behind TSB MC-10113664 isn't confirmed (OPEN).
- No Halderman or Today's Technician text was reachable; textbook claims above rely on OEM and industry snippets.

---

## Q2. What do ASE, instructors or techs say about experienced techs failing because they answer from shop experience?

### Takeaway
There is consistent public commentary, mostly from secondary prep sites and forums (ANECDOTAL). It says ASE wants the theoretical, industry-approved or manufacturer answer, and that experienced techs lose points by applying shop shortcuts, overthinking, or misreading question style. I found no official ASE statement framing it as experienced techs failing.

### Cited Findings
- DOCUMENTED (snippet): "The ASE wants the theoretical book answer to verify that you know what to look for," and "the test is a standardized measure of knowledge — it does not measure how good you are in the shop." It also notes that the test uses stereotyped symptom sounds (ball joints "pop," outer CV "click," wheel bearings "roar"). — Snippets attributed to [Garage Journal "ASE Test" thread (ANECDOTAL)](https://www.garagejournal.com/forum/threads/ase-test.88358/) and [Garage Journal "About to take the ASE" (ANECDOTAL)](https://www.garagejournal.com/forum/threads/about-to-take-the-ase.158515/). The search result combined these, so attribution between the two threads isn't certain.
- ANECDOTAL (snippet): An ASE master tech said the answers ASE wants are "not how it works in the real world in the shop." Another poster failed 2 of 4 tests despite studying Motor Age guides. — [Garage Journal ASE threads](https://www.garagejournal.com/forum/threads/ase-test-review-book-recommendations.109786/).
- DOCUMENTED (snippet): Shop shortcuts or procedures "developed in their shop or on social media" may not be "the industry-approved or manufacturer's way of doing it." — [Dorman Shop Press](https://shoppress.dormanproducts.com/ase-test-taking-tips/).
- DOCUMENTED (snippet): "Many technicians fail the ASE test because they don't understand the question, not because they aren't good at mechanics." Retake failures often come from reading the textbook "without ever practicing the question style." — [PTT (Pittsburgh Technical) on failed ASE tests](https://ptt.edu/failed-your-ase-certification-test-5-ways-to-study-to-pass-the-second-time/); [Apex Technation](https://apextechnation.com/articles/ase-certification-practice-test).
- DOCUMENTED (snippet): "Don't read into the question or use prior experience to answer." — [Apex Technation test-day strategy](https://apextechnation.com/articles/ase-test-day-strategy) (secondary).
- DOCUMENTED (snippet): Technician A/B items are rated the hardest by techs. Judge each statement independently, as true or false, and don't let one influence the other. — [FenderBender, "Tips and tricks for ASE certification test taking"](https://www.fenderbender.com/running-a-shop/operations/article/33029517/tips-and-tricks-for-ase-certification-test-taking).

### Inferences
- INFERRED: The learner has already passed 7 ASE tests, so general question-style skill is proven. For A2 the risk is narrower: dealership habits specific to transmissions (assembly or valve body replacement, programming and relearn as the default fix, less exposure to legacy hydraulics).

### Gaps
- No Reddit or iATN thread specific to A2 surfaced (search returned none). No official ASE commentary on the topic was found.

---

## Q3. Legacy content (governor, TV cable, vacuum modulator, bands, Simpson apply charts): will it appear?

### Takeaway
The 2026 task list emphasizes electronic control, but hydraulic pressure testing (A.11), bands and drums (C.23), servos (B.8) and apply-chart reasoning (sample no-reverse question) remain. Governor, TV cable and modulator aren't named in the shortened 2026 task wording mapped in `research.md`. Their probability is therefore OPEN and likely low. The underlying principle (a load signal raises line pressure and delays shifts) is still testable.

### Cited Findings
- DOCUMENTED: The 2026 task list has "Hydraulic pressure tests" (A.11), "Pressure problems with electronic pressure control" (A.17), "Accumulator and servo inspection" (B.8) and "Bands and drums" (C.23). Apply-chart reasoning appears in a sample question. — `research.md` lines 59-112, from the [ASE study guide](https://ase.com/wp-content/uploads/ASE_Automobile_Study_Guide.pdf).
- DOCUMENTED (snippet): Vacuum modulator and TV cable theory. High vacuum (light load) gives low throttle pressure: early, soft shifts. Low vacuum (heavy load) gives later, firmer shifts. The governor produces pressure proportional to road speed, which opposes throttle pressure plus spring force at the shift valve. — [freeasestudyguides pressure control](https://www.freeasestudyguides.com/transmission-pressure-control.html); [Car Treatments modulator](https://cartreatments.com/automatic-transmission-vacuum-modulator-functions/). Two sources agree.
- DOCUMENTED (snippet): Modulator diagnosis. ATF in the vacuum hose means a ruptured diaphragm. It also causes low fluid, white exhaust smoke, and harsh or late shifts. Test with a hand vacuum pump. — [Hotrodders T-350 thread (ANECDOTAL)](https://www.hotrodders.com/threads/t-350-vacuum-modulator-transmission-fluid-in-the-vacuum-lines.545064/); [Oards modulator symptoms](https://oards.com/bad-vacuum-modulator-replacement-cost/). Consistent across 2+ sources.
- DOCUMENTED (snippet): Band adjustment is model-specific. Torque the adjuster to spec (for example 72 in-lb on Chrysler 47RE), back off the specified turns, which vary by year, then torque the locknut. — [DieselHub 47RH/47RE band adjustment](https://www.dieselhub.com/maintenance/47rh-47re-transmission-band-adjustment.html); [AutoZone repair guide](https://www.autozone.com/repairinfo/repairguide/repairGuideContent.jsp?pageId=0900c15280064364).
- DOCUMENTED (snippet): Motor Age's A2 guide still includes valve body, accumulator and line-pressure spec material. — [Motor Age Training A2 guide listing](https://motoragetraining.com/product/ase-study-guide-a2-automatic-transmission/).

### Inferences
- INFERRED: Learn the legacy devices as principles (load signal and speed signal against a spring at a shift valve; modulator leak symptoms; torque-and-back-off band adjustment) so that electronic-era questions phrased in hydraulic terms don't catch you out. Don't spend time on per-model specs.

### Gaps
- OPEN: Whether a band adjustment or in-vehicle modulator/TV task appears in the full (unshortened) 2026 task statements. Re-read pages 10-15 of the local ASE PDF for the words "band," "modulator," "governor" and "throttle valve." The PDF couldn't be text-extracted in this session (no poppler; pypdf failed).

---

## Q4. Terminology: textbook terms vs. shop slang

### Takeaway
The textbook defines shift-quality words precisely. Mixing up flare (underlap, a slip on the shift) with tie-up or bind-up (overlap) inverts the diagnosis.

### Cited Findings
- DOCUMENTED (snippet): **Flare**: the off-going element releases before the on-coming element holds, so engine rpm rises momentarily. **Tie-up**: two ratios are applied at once and the output is momentarily braked. **Bind-up** or excessive overlap: the on-coming element applies before the off-going one releases. Bind-up is the opposite of flare. — [Sonnax "Transmission Terms from A to Z"](https://www.sonnax.com/tech_resources/175-tranny-terms-from-a-to-z); [Gears Magazine, "The Definitions Are The Difference"](https://gearsmagazine.com/magazine/the-definitions-are-the-difference/); [BITOG slip vs. flare (ANECDOTAL)](https://bobistheoilguy.com/forums/threads/automatic-transmission-question-slipping-vs-flare.338792/).
- DOCUMENTED (learner's own notes): accumulator "slide-bump" and synchronous-shift mistiming causing harsh shifts or flare appear in `notes/powerflowetc.txt` (see `research.md` line 57).
- INFERRED: "Clutch-to-clutch" is the shop and OEM term for a shift made by releasing one friction element while applying another, with no one-way clutch. The textbook calls it a synchronous shift, and a shift made through a one-way clutch non-synchronous. The learner's notes already use the synchronous/nonsynchronous terms.

### Inferences
- INFERRED: On ASE, map the slang to the mechanism before answering: flare means underlap, low apply pressure, or a leaking or late on-coming circuit. Tie-up or bind-up means overlap or a late-releasing element.

### Gaps
- No public source defining "underlap" was found in snippets (OPEN, minor).

---

## Q5. How to switch into "textbook mode" (practical advice drawn from the sources)

### Takeaway
Answer as if you are following the SI flowchart on a vehicle you've never seen. Every symptom in the stem must be explained, and the lowest-cost verified step comes first.

### Cited Findings
- DOCUMENTED (snippet): Answer from the industry-approved or manufacturer procedure, not a shop shortcut. — [Dorman Shop Press](https://shoppress.dormanproducts.com/ase-test-taking-tips/).
- DOCUMENTED (snippet): Pick the most probable cause for the stated symptoms, don't read into the question, and don't use prior experience to add facts. — [Apex Technation](https://apextechnation.com/articles/ase-test-day-strategy).
- DOCUMENTED (snippet): Judge Technician A and Technician B independently, and mark T/F on scratch paper. — [FenderBender](https://www.fenderbender.com/running-a-shop/operations/article/33029517/tips-and-tricks-for-ase-certification-test-taking).
- DOCUMENTED (snippet): GM's own SBD order (verify, preliminary checks including SI/TSB, system check, diagnose, repair, verify) is a ready-made textbook sequence the learner already knows from the dealership. — [GM bulletin (NHTSA)](https://static.nhtsa.gov/odi/tsbs/2019/MC-10168204-9999.pdf).

### Inferences
- INFERRED checklist for the learner, not a question bank: (1) Has the concern been verified and has fluid been checked correctly? If not, that is often the answer to "first step." (2) Does the answer explain every symptom? (3) Is there a simpler input, engine or fluid cause? (4) Does the answer test before replacing? (5) Is a code cleared with the scan tool, and is the repair verified? (6) After a hard-parts failure, has the cooler been flushed and flow-tested?

### Gaps
- No instructor-authored A2-specific advice page was reachable. The learner's own ASEP instructor's view would be the most relevant source and should be asked for.
