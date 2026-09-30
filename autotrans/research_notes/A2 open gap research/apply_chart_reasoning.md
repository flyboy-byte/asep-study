# Clutch/Band Apply-Chart and Power-Flow Reasoning for ASE A2 (A.8, A.9, A.14, C.13, C.19–C.23)

Researched 2026-09-30. All URLs accessed 2026-09-30. Network note: full-page fetches were blocked (ase.com and transmissiondigest.com both returned EGRESS_BLOCKED). Everything below comes from WebSearch snippets. Tags:
- **DOCUMENTED (snippet)**: corroborated in search snippets. Where only one snippet supports a claim, it says "single snippet".
- **INFERRED**: my reasoning, or standard textbook background I did not retrieve in this session. Verify it against SI or a textbook before putting it in a guide.
- **OPEN**: not resolved.

This extends `area_a_mech_hydraulic_diagnosis.md` (lines 59–67, the elimination method), `hydraulic_pressure_testing.md` and `area_c_overhaul.md` (C.19–C.23). It does not repeat them. Task numbers follow `autotrans/research.md` lines 56–111: A.8 road test mech/hydraulic, A.9 NVH/shift quality, A.14 SI/flow charts/hydraulic diagrams, C.19 clutch pack components, C.20 clearance, C.21 air test, C.22 one-way clutch, C.23 bands and drums. C.13 is used as the task number named in the assignment and was not re-checked here.

## 1. The official 2026 ASE sample item: what the chart is and how the method solves it

### Takeaway
The public 2026 ASE study guide sample uses a 5-speed RWD chart. Its elements are overdrive band, intermediate band, reverse band, forward clutch, direct clutch and coast clutch. That element set matches Ford's 5R55-family (C3/A4LD-derived) layout. Elimination points to the one element applied **only** in reverse, which is the reverse band. Every other element also works in some forward gear, so a working forward range clears it.

### Cited Findings
- DOCUMENTED (snippet): The 2026 guide's A2 sample describes an RWD 5-speed automatic that will not engage REVERSE and asks for the cause from the clutch/band apply chart. The choices are (A) a failed direct clutch, (B) a failed coast clutch, (C) a broken reverse band, (D) a seized forward clutch. — [ASE Automobile Study Guide 2026](https://www.ase.com/uploads/ASE_Automobile_Study_Guide_2026.pdf); also [ase.com wp-content copy](https://ase.com/wp-content/uploads/ASE_Automobile_Study_Guide.pdf). The chart columns are overdrive band, intermediate band, reverse band, forward clutch, direct clutch and coast clutch, set against R, 1st–5th and manual ranges (snippet). The exact cell pattern and the official answer key could not be read because the fetch was blocked. A.8, A.14.
- DOCUMENTED (snippet): The Ford 5R55W/S has three multi-plate clutches (coast, direct, forward), two one-way clutches (overdrive sprag, low sprag) and three bands (overdrive, intermediate, low/reverse). The same element names appear in the ASE chart. — [Scribd 5R55W/S Quick Reference](https://www.scribd.com/document/508965700/5R55W-S-QR); [S197 Forum, 5R55S operation](https://www.s197forum.com/threads/5r55s-operation-diagnostics-and-components.31995/).
- DOCUMENTED (snippet, single-source detail): 5R55 by gear, as the snippet gives it. 1st: forward + coast. 2nd: forward + overdrive band (coast releases). 3rd: forward + intermediate band (OD band releases). 4th: forward + coast + direct (intermediate releases). Reverse: the low/reverse servo applies the low/reverse band. — [S197 Forum](https://www.s197forum.com/threads/5r55s-operation-diagnostics-and-components.31995/). 5th was not given.
- DOCUMENTED (snippet): The ASE-style "process of elimination" use of application charts: find the devices applied in the problem gear(s), then rule out any that also apply in working gears. — [FreeASEStudyGuides, clutch and band charts](https://www.freeasestudyguides.com/transmission-clutch-band-chart.html).

### Inferences
- INFERRED (worked method; not the answer key): the steps below apply to the ASE item.
  1. Affected ranges: R only. Unaffected: 1–5 all normal. "Rolls in neutral" means there is no park or neutral bind and no tie-up.
  2. Candidates are the elements applied in R. In the 5R55 lineage these are the reverse band plus the rear-section clutch that drives the reverse sun (Ford calls it "direct"; in the C3/A4LD it was the reverse/high clutch). The OD section is probably also held at 1:1 through the coast clutch or the OD sprag. The direct clutch in reverse comes from the C3 lineage and is INFERRED/OPEN, not confirmed in a snippet.
  3. Exonerate anything applied in a working range. The direct clutch works in 4th/5th, so it is cleared. The coast clutch works in forward ranges, so it is cleared. The forward clutch is not used in R, and a *seized* forward clutch would cause a bind-up in R (the vehicle would not move and the engine would load down), not a free no-reverse. Choice D names a seized-element symptom that does not match the stem.
  4. What is left is the reverse band (or its servo circuit). It is the only element applied solely in R.
- INFERRED: Caveat. If the chart also shows the reverse band applied in manual 1 for engine braking, a broken reverse band would also remove manual-1 engine braking. ASE's "forwards all normal" probably means drive ranges. On a real car, check manual-1 coast braking. If it is also gone, that confirms the band or servo.
- INFERRED: The distractor design is instructive. Each wrong choice is an element that appears in R **and** in some working range (direct, coast), or a *seized* element whose symptom would be a bind-up. This is exactly the "applied in every affected range, not required in any working range" test.

### Gaps
- OPEN: The exact cell pattern of the ASE chart (5th gear, manual ranges, whether the reverse band is shaded in manual 1) and the official answer could not be read. The study guide PDF fetch was blocked. Get it from the local PDF or `research.md` if it was already transcribed.

## 2. A systematic method for apply-chart questions

### Takeaway
The method has four parts. (1) Sort ranges into affected and unaffected. (2) The culprit is applied in *every* affected range and in *no* working range. (3) Decide whether the symptom is **loss of hold** (slip, flare, no-drive, which means released or failed) or **extra hold** (tie-up, bind, harsh or braked feel, which means seized or dragging). (4) Use manual ranges and coast/engine-braking elements as separators between a one-way clutch and the friction element that backs it up.

### Cited Findings
- DOCUMENTED (snippet): If the vehicle moves in manual low but not in the other forward ranges, the low roller clutch was not holding. Manual low applies a friction element that holds the same member. — [search set incl. JustAnswer / Transmission Digest "Troubleshooting One-Way Clutches"](https://www.transmissiondigest.com/troubleshooting-one-way-clutches/) (snippet); matches [FreeASEStudyGuides](https://www.freeasestudyguides.com/transmission-clutch-band-chart.html) as already cited in `area_a_mech_hydraulic_diagnosis.md`. A.8, C.22.
- DOCUMENTED (snippet): A snippet from the one-way-clutch search describes a unit where the low band (B2) is ON in first and the OWC is holding. A slip there means either a hydraulic fault in that servo or a slipping OWC. It also describes isolating a 2-3 flare by selecting "D" or "3" (or pressing OD-cancel), which engages the overrun clutch. — [Transmission Digest, Troubleshooting One-Way Clutches](https://www.transmissiondigest.com/troubleshooting-one-way-clutches/) (snippet, single source). A.8, C.22.
- DOCUMENTED (snippet): Tie-up happens when an off-going element fails to release on time. Two gears at once happens when two hydraulic circuits are pressurized together (a stuck valve, or a solenoid that fails to close). — [FreePatentsOnline 5046175 (clutch tie-up detection)](https://www.freepatentsonline.com/5046175.html); [search snippet, two-gears-at-once](https://www.repcoservice.com/articles/common-automatic-transmission-problems). A.8, A.9.
- DOCUMENTED (snippet): The 4L60-E overrun clutch applies in the lower manual ranges and gives engine braking off-throttle. The low/reverse clutch has two jobs: it works in reverse and gives manual-1 engine braking. — [LS1Tech 700R4 clutch/band chart thread](https://ls1tech.com/forums/automatic-transmission/922575-700r4-clutch-band-chart.html); [TransGo 4L60 reference](https://www.thirdgen.org/forums/attachments/transmissions-drivetrain-19/pictures-every-component-700r4-700535/transmission-700r4-general-info-304625d1468509620).
- DOCUMENTED (snippet, 2 sources): 4L60-E with **no manual-1 engine braking and no reverse** means the low/reverse clutch pack. It is the only element common to both. — [GMT400 forum](https://www.gmt400.com/threads/4l60e-no-engine-braking-in-manual-2nd-and-1st-engine-goes-to-idle.76528/); [LS1Tech, no engine braking only in manual 1st](https://ls1tech.com/forums/automatic-transmission/1961139-4l60e-no-engine-braking-only-manual-1st.html). A.8.
- DOCUMENTED (snippet): Sonnax's 4L80-E "no reverse" procedure splits the problem three ways. **Hydraulic/chart:** if 3rd and 4th work, the direct clutch (also used in R) is proven. **Electrical:** unplug the transmission to force failsafe and see if reverse returns. **Mechanical:** block the low/reverse band, which is also used for manual-1 engine braking. — [Sonnax, Diagnosing the Elusive No Reverse with the 4L80-E](https://www.sonnax.com/tech_resources/88-diagnosing-the-elusive-no-reverse-with-the-4l80-e); same article at [Transmission Digest](https://www.transmissiondigest.com/diagnosing-the-elusive-no-reverse-with-the-4l80-e/). A.8, A.14.

### Inferences
- INFERRED (method checklist):
  1. **Tabulate** every range the customer or technician tried: P, R, N, D1–Dn, manual ranges, coast/engine braking in each manual range, and upshift/downshift quality.
  2. **Mark affected vs unaffected.** An element that works in any unaffected range is exonerated for *hold* faults. This is the most useful single rule.
  3. **Intersect.** Several affected ranges: find the element common to all of them. One affected range: find the element unique to it. No drive in any range: it is not a single element (think fluid, pump, converter, input shaft, manual valve or linkage, output/park).
  4. **Classify the symptom.** Slip, flare or no-drive means an element that has failed released (worn frictions, leaking seal, broken band or strut, cracked piston, low apply pressure). Tie-up, bind, harsh or "braked" feel, stall or rpm pulled down means an element that is seized, dragging or not releasing. A seized element causes trouble in ranges where the chart shows it **not** applied. So look for the range where its extra hold conflicts with the elements that are supposed to be on. Example: a seized forward clutch on a Simpson unit binds in R. A dragging low/reverse band binds on the upshift to 2nd.
  5. **Separate the OWC from its backup.** A one-way clutch holds in drive and freewheels on coast. The manual-range friction element (band or clutch) holds the same member in both directions. Slip in D1 but **not** manual 1 points to the OWC. No engine braking in manual 1 but D1 normal points to the friction element (low/reverse band or clutch) or its circuit. A "freewheel/no engine braking" complaint in drive is **normal** on units that use OWCs.
  6. **Check the pattern against controls.** Before blaming a friction element, rule out wrong commanded gear (scan data), range sensor/linkage, solenoids and TCM failsafe. Failsafe itself produces "only 2nd/3rd/4th" patterns that look like multi-element failure.
  7. **Confirm** with pressure by range (Section 5), then air testing on disassembly (C.21).
- INFERRED: When the same symptom appears in two ranges that share **two** elements, the chart alone cannot decide between them. Use a third range that uses only one of the two, or use pressure or air testing. Questions are usually written so that one working range settles it. Look for that range.

### Gaps
- OPEN: I did not find a public textbook page (Halderman/Hadfield, CDX, Erjavec) stating the "seized element → bind in non-applied ranges" rule in those words. It follows from power-flow logic, but it is INFERRED here.

## 3. Classic textbook charts and their diagnostic signatures

### Takeaway
Learn each family's **unique** elements (used in one range only) and **shared** elements (the ones that clear themselves when another range works). Signatures that are worth memorizing are listed below. The detailed cell patterns come mostly from background knowledge and should be verified against a textbook or SI before printing.

### Cited Findings
**Simpson 3-speed (THM350/400, TorqueFlite A727/A904)**
- DOCUMENTED (snippet): The TH350 uses four multi-disc clutches, two roller clutches (intermediate and low/reverse) and an intermediate overrun band. 1st = forward clutch + low roller. 2nd = forward + intermediate clutch through the intermediate roller (sprag), and the low roller freewheels. — [Scribd TH350 PDF](https://www.scribd.com/document/470210272/TH350-pdf); [TriFive, how do TH350s work](https://www.trifive.com/threads/how-do-th350s-work.30204/).
- DOCUMENTED (snippet): The TH400 is a Simpson-gearset 3-speed. — [Wikipedia Turbo-Hydramatic](https://en.wikipedia.org/wiki/Turbo-Hydramatic); [Ate Up With Motor, Simpson gearset](https://ateupwithmotor.com/terms-technology-definitions/simpson-gearset/).
- DOCUMENTED (snippet): The A727 service manual chart lists front clutch, rear clutch, kickdown (front) band, low-reverse (rear) band and overrunning clutch. All are off in neutral. — [Poly318, 1966–77 TorqueFlite 727/904 Service Manual](https://poly318.com/wp-content/uploads/2023/07/1966_1977_TorqueFlite_727_904_Service_Manual.pdf).
- DOCUMENTED (snippet): TH350 reverse is regulated to a higher pressure. Low reverse pressure (under ~200 psi cited for the TH350) suggests the regulator, boost, manual valve or pump. — [Industrial Monitor Direct, reverse line pressure](https://industrialmonitordirect.com/blogs/knowledgebase/reverse-line-pressure-in-automatic-transmissions-why-its-higher). This is a single, non-OEM source. The number needs SI.

**4-speed with overdrive: 700R4/4L60-E (also 4L80-E)**
- DOCUMENTED (snippet): The 4L60 elements are reverse input clutch, 2-4 band, overrun clutch, forward clutch, forward sprag, 3-4 clutch, low/reverse clutch and low roller clutch. The reverse input clutch applies **only in reverse**. The 2-4 band holds the reverse input drum for 2nd (and 4th). The overrun clutch applies in the lower manual ranges. The low/reverse clutch applies in R and manual 1 only. — [Scribd 700R4 general info](https://www.scribd.com/document/672158052/Transmission-700R4-General-Info); [TransGo 4L60 reference](https://www.thirdgen.org/forums/attachments/transmissions-drivetrain-19/pictures-every-component-700r4-700535/transmission-700r4-general-info-304625d1468509620); [LS1Tech chart thread](https://ls1tech.com/forums/automatic-transmission/922575-700r4-clutch-band-chart.html).
- DOCUMENTED (snippet): The OEM 4L60 applies the overrun clutch in D3 (1st–3rd) but not in D4. That leaves the forward sprag carrying the load in D4, which is why performance builds replace the sprag and low roller. — [USPTO 12007019, forward sprag protection](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/12007019); [TCI low roller clutch](https://www.tciauto.com/700-r4-4l60e-low-roller-clutch.html).
- DOCUMENTED (snippet): 4L80-E reverse = direct clutch (also used in 3rd/4th) + low/reverse band (also manual-1 engine braking). — [Sonnax 4L80-E no reverse](https://www.sonnax.com/tech_resources/88-diagnosing-the-elusive-no-reverse-with-the-4l80-e).

**Chrysler 41TE (all clutches, no bands; clutch-to-clutch)**
- DOCUMENTED (snippet): It has five clutches: low/reverse, underdrive, overdrive, 2/4 and reverse. UD is applied in 1st, 2nd and 3rd. 2nd = UD + 2-4. The 2-3 shift releases 2-4 and applies OD. A downshift to 1st keeps UD, releases 2-4 and applies L/R. — [Motor Magazine, "Transmission as a Second Language"](https://www.motor.com/magazine-summary/transmission-as-a-second-language/); [Allpar 41TE thread](https://www.allpar.com/threads/41te-slips-bumps-on-1-2-and-2-1.160701/); [Quizlet 41TE (lead only)](https://quizlet.com/704152352/41te-flash-cards/).
- DOCUMENTED (snippet): 41TE Clutch Volume Index (CVI) ranges: L/R 35–85, 2-4 20–77, UD 24–70, OD 75–135. The scan-tool CVI is a wear/clearance indicator per clutch (C.20). — [search snippet, Transmission Digest / Motor 41TE set](https://www.transmissiondigest.com/another-transmission-mutation-part-1/). Unit-specific, and the number needs SI.

**Ford AOD / AODE / 4R70W (Ravigneaux)**
- DOCUMENTED (snippet): The AOD/AODE has two bands (overdrive, low-reverse), two one-way clutches and four friction clutches (forward, reverse, intermediate, direct). Manual-1: forward clutch + low-reverse band (the band holds the carrier on coast for engine braking). Manual-2: forward + OD band. 4th: direct + OD band, with the intermediate clutch applied but not carrying torque. Reverse: reverse clutch + low-reverse band. No band adjustment. — [DIYFord AODE/4R70W guide](https://www.diyford.com/ford-aode4r70w-guide-calibration-building-troubleshooting/); [Wikipedia Ford AOD](https://en.wikipedia.org/wiki/Ford_AOD_transmission); [CarTech AOD/4R70W history](https://www.cartechbooks.com/blogs/techtips/ford-aod-and-4r70w-transmission-history-and-evolution).

**GM 4T65-E (FWD, chain drive)**
- DOCUMENTED (snippet): Elements are input clutch, second clutch, third clutch, fourth clutch, forward band, 1-2 (D-2) band, reverse band, input sprag, 1-2 roller clutch and third sprag. The input sun is driven by the input clutch and input sprag, and the reaction sun drum is held by the 1-2 roller clutch. — [Sonnax THM 4T65-E Update Handbook (APTTA mirror)](https://www.apttabrasil.com/wp-content/themes/aptta/pdf/sonnax/4T65GRN.pdf); [Transtar 4T60E/4T65E](https://shinseiauto.com/japanese/transtar/usgm4t60e04.pdf).

**Lepelletier 6-speed (GM 6L80, Ford 6R80, ZF 6HP)**
- DOCUMENTED (snippet): GM 6L80 clutches are 1-2-3-4, 2-6, low/reverse, 3-5-reverse and 4-5-6. There are no bands. The low sprag holds the output carrier in 1st, and the L/R clutch applies to help it on launch. — [Gears, Tackling Clutch Failure in the 6L80/90](https://gearsmagazine.com/magazine/tackling-clutch-failure-in-the-gm-6l80-90/); [Sonnax 6L80 unit page](https://www.sonnax.com/units/301-6l80); [SilveradoSierra 6L80 thread](https://www.silveradosierra.com/threads/gm-6l80-transmission-information-thread.753826/).
- DOCUMENTED (snippet): Ford 6R80 lettering: A = 1-2-3-4 (forward), B = 3-5-R (direct), C = 2-6 (intermediate), D = low/reverse, E = 4-5-6 (overdrive). A, B and E are driving clutches. C and D are brakes. 3-4 = release B, apply E, and A stays on. — [Raybestos 6R80 B clutch](https://www.raybestospowertrain.com/blog/6r60-6r80-6hp26-b-clutch-3-5-r-direct-installation-rtk-6r82); [Raybestos 6R80 E clutch](https://www.raybestospowertrain.com/blog/6r60-6r80-6hp26-e-clutch-4-5-6-overdrive-installation-rtk-6r85); [Sonnax 6R80 2-3 shift quality](https://www.sonnax.com/tech_resources/1141-troubleshooting-ford-6r80-6r140-2-3-shift-quality-issues).
- DOCUMENTED (snippet): The ZF 6HP26 has three rotating clutches (A, B, E) and two brakes (C, D). It is a Lepelletier layout (a simple planetary feeding a Ravigneaux). Ratios are 4.171 / 2.340 / 1.521 / 1.143 / 0.867 / 0.691, R 3.403. — [ZF 6HP26 description (Land Rover doc)](https://media.disco3.co.uk/gallery/albums/userpics/15405/ZF_6HP26X_LR_Description_and_Operation.pdf); [Wikipedia ZF 6HP](https://en.wikipedia.org/wiki/ZF_6HP_transmission); [Wikipedia Lepelletier gearset](https://en.wikipedia.org/wiki/Lepelletier_planetary_gearset).
- Correction to the assignment's framing: the sources show **letters A–E** (Ford/ZF) and **gear-named clutches** (GM 6L). They do not show "C1–C5". C1–C5 numbering does exist on some other units (e.g., the snippet below mentions "C2 1-2-3-4-5-Reverse" and "C5 4-5-6-8-Reverse" on a later GM or Ford unit). Do not assume it for 6-speeds.

**8/9/10-speed**
- DOCUMENTED (snippet): The 10R80/10L80 has four planetary sets and six clutches, A–F. A and B are brakes. C, D, E and F route power. — [Gears, The more you know about the 10R80](https://gearsmagazine.com/magazine/the-more-you-know-about-the-10r80-the-better-off-you-are/); [Ranger Station 10R80 PDF](https://www.therangerstation.com/resources/pdf_documents/Ford_10r80_automatic_transmission.pdf); [MathWorks 10-speed clutch schedule](https://www.mathworks.com/help/physmod/sdl/ref/10speed.html).
- DOCUMENTED (snippet, single source, **internally inconsistent**): A in R–6. B in R, 1, 2, 8, 9, 10. C in 2–5 and 7–10. D in P, R, 1, 2, 3, 4, 6, 7, 8, 10. E in 1, 3, 5, 6, 7, 8, 9. F in R, 4–9. — [Ranger5G forum, 10R80 shift strategy](https://www.ranger5g.com/forum/threads/my-research-into-the-10r80-shift-strategy.26732/) (snippet). Summed, this gives 5 elements in 8th, while the other gears get 4. At least one entry is wrong. **Do not print this without SI.**
- DOCUMENTED (snippet): GM 10L80 names its A clutch the "1-2-3-4-5-6-R" clutch (sold as "A Reverse (1-2-3-4-5-6)"). This agrees with "A applied in R–6". — [Global Transmission Parts, 10L80 1-2-3-4-5-6-R clutch D-ring](https://globaltransmissionparts.com/10l80-10l90-10r80-1-2-3-4-5-6-r-intermediate-clutch-outer-d-ring/); [Raybestos R577401](https://www.raybestospowertrain.com/friction-clutch-plates/r577401).
- DOCUMENTED (snippet): Transmission Digest has a GM 10L1000 casting-ID and clutch-application article (not readable). — [Transmission Digest 10L1000](https://www.transmissiondigest.com/gm-10l1000-casting-identification-and-clutch-application/).

### Inferences
- INFERRED (textbook background, verify before printing):
  - **Simpson 3-speed (GM naming):** D1 = forward clutch + low roller. D2 = forward + intermediate (TH350: intermediate clutch through the intermediate roller; TH400: intermediate clutch through the sprag). D3 = forward + direct. R = direct + low/reverse (TH350 L/R clutch, TH400 rear band). Manual 2 adds the intermediate overrun band (TH350) or front band (TH400) for coast braking. Manual 1 adds the L/R clutch or rear band. **Signatures:** direct is shared by 3rd and R, so "no 3rd and no reverse" = direct clutch. Forward is in all forward gears, so "no forward in any range, R OK" = forward clutch (or its circuit). "No manual-1 braking and no R" = L/R element. "Slip D1, OK manual 1" = low roller.
  - **TorqueFlite A727/A904 (Chrysler naming):** the rear clutch is the forward (input) clutch in all forward gears. The front clutch is used in 3rd and R. The kickdown band gives 2nd. The low-reverse band gives manual 1 and R. The overrunning clutch gives D1. Same signatures as the GM Simpson, with Chrysler names. "Front clutch" = the GM "direct" clutch. This name mismatch is a classic trap.
  - **4L60-E:** D1 = forward clutch + forward sprag + low roller. D2 = + 2-4 band. D3 = forward + sprag + 3-4 clutch. D4 = 3-4 clutch + 2-4 band (the forward clutch stays applied but the sprag overruns). R = reverse input + L/R clutch. The overrun clutch is on in D3 coast, manual 2 and manual 1. The L/R clutch is on in manual 1. **Signatures:** "no reverse only, forwards and manual-1 braking OK" = reverse input clutch (the only reverse-only element). "No R and no manual-1 braking" = L/R clutch. "Slips 2nd and 4th" = 2-4 band or servo (the common element). "Slips 3rd and 4th" = 3-4 clutch. "No coast braking in D3/2/1" = overrun clutch. "Slips in D1 and D2/3 only when forward-driven, OK in manual with overrun on" = forward sprag, because the overrun clutch bypasses the sprag.
  - **41TE:** 1 = UD + L/R. 2 = UD + 2-4. 3 = UD + OD. 4 = OD + 2-4. R = reverse + L/R. **Signatures:** UD is in 1–3, so "slips 1–3, 4th OK" = UD. OD is in 3–4. 2-4 is in 2 and 4. L/R is in 1 and R. There is no OWC in the basic chart for drive-vs-manual separation, so use CVI and pressure-tap tests instead.
  - **AOD:** D1 = forward clutch + planetary OWC. Manual 1 adds the low-reverse band. R = reverse clutch + low-reverse band. "No reverse, no manual-1 braking" = low-reverse band. "No reverse only, manual-1 braking OK" = reverse clutch. Per the snippet chart it appears only in R (manual 2 uses the OD band), so it is the AOD's reverse-only element.
  - **Lepelletier (6L80 names):** 1 = 1234 + L/R (low sprag in D). 2 = 1234 + 26. 3 = 1234 + 35R. 4 = 1234 + 456. 5 = 35R + 456. 6 = 26 + 456. R = 35R + L/R. **The gear-named clutch labels are the chart**: "no 3rd, no 5th and no reverse" = 35R. "No 5 and 6 and no 4" = 456. "No 1–4" = 1234. "No R and no manual-1 braking" = L/R. Every Lepelletier gear uses exactly two elements, so a single-element failure knocks out 2–4 ranges at once. That makes multi-range symptoms normal, not "multiple failures". Ford letters: A = 1234, B = 35R, C = 26, D = L/R, E = 456.
  - **8/9/10-speeds:** they apply 3 (8/9-speed) or 4 (10-speed) elements per gear. A single element failure removes a scattered set of gears (e.g., 10R80 A = R–6). GM's gear-listing names (e.g., "1-2-3-4-5-6-R") let you read the chart from the part name. Expect ASE to test the **method** (the element common to all failed gears), not memorized 10-speed cells. With the GM 10-speed chart Logan already knows, apply the same intersection rule.
- INFERRED: The "unique element" trap. Many units have **no** reverse-only element (Lepelletier: 35R also gives 3 and 5, and L/R also gives manual 1). On those units, "no reverse, all forwards normal" points to the element whose *other* job is the one nobody noticed (manual-1 engine braking), or to a reverse-specific hydraulic cause such as a reverse circuit leak, a manual-valve feed or a check ball.

### Gaps
- OPEN: Full cell-by-cell charts for the THM400, A727, 41TE 4th/R, 4T65-E and 10R80 were not retrievable (all fetches blocked). The patterns above labeled INFERRED are background and need checking against a textbook (Halderman *Automatic Transmissions*, Hadfield/CDX) or SI.
- OPEN: 5R55 5th gear and manual-range elements, and whether the direct clutch applies in R.
- OPEN: GM 8L90/9T50 clutch names were not searched.

## 4. Engine braking, coast elements and manual ranges as separators

### Takeaway
One-way clutches give drive-only hold and freewheeling coast. The coast/overrun friction element (band or clutch) gives hold in both directions in manual ranges. Comparing D vs manual, and drive vs coast, separates the OWC from the friction element that shares its reaction member.

### Cited Findings
- DOCUMENTED (snippet): The 4L60-E overrun clutch provides engine braking when off throttle in the lower manual ranges. — [LS1Tech 700R4 chart thread](https://ls1tech.com/forums/automatic-transmission/922575-700r4-clutch-band-chart.html).
- DOCUMENTED (snippet): The AOD low-reverse band holds the carrier during deceleration/coast in manual 1 for engine braking. — [DIYFord AODE/4R70W guide](https://www.diyford.com/ford-aode4r70w-guide-calibration-building-troubleshooting/).
- DOCUMENTED (snippet): The 4L80-E low/reverse band is used for manual-1 engine braking and also in R. — [Sonnax 4L80-E no reverse](https://www.sonnax.com/tech_resources/88-diagnosing-the-elusive-no-reverse-with-the-4l80-e).
- DOCUMENTED (snippet): The 6L80 applies the L/R clutch to help the low sprag on launch. — [Gears 6L80/90 clutch failure](https://gearsmagazine.com/magazine/tackling-clutch-failure-in-the-gm-6l80-90/).
- DOCUMENTED (snippet): Selecting D/3 or OD-cancel engages the overrun clutch and can isolate a 2-3 flare to the sprag side. — [Transmission Digest, Troubleshooting One-Way Clutches](https://www.transmissiondigest.com/troubleshooting-one-way-clutches/) (snippet).

### Inferences
- INFERRED (rules):
  - Slip/no-drive in D1, OK in manual 1: the **OWC** (low roller/sprag).
  - D1 OK, no engine braking in manual 1: the **manual-low friction element** (L/R band or clutch, servo, or apply circuit).
  - Both no-drive in D1 and M1: an element common to both (forward/input clutch or its OWC-independent path, pump or pressure).
  - A freewheel on coast in D is **normal** where an OWC carries the gear. Do not call it a fault.
  - An OWC that **locks both ways** (seized or installed backward) gives bind-up or harsh behavior on the upshift out of the gear it serves (the 1-2 shift feels like a tie-up), and possibly no freewheel. An OWC **installed backward** gives no drive in the gear it serves but OK drive in the manual range (C.22 assembly check).

### Gaps
- OPEN: No public source retrieved gives a specific "backward OWC" symptom list for a named unit.

## 5. Confirming chart suspicions: pressure by range and air testing

### Takeaway
The chart narrows the list to one or two elements or circuits. Pressure testing by range separates a supply/regulation fault (low pressure) from a friction/sealing fault (pressure OK but slips). Air testing on the bench (valve body off) proves each piston or servo applies and holds.

### Cited Findings
- DOCUMENTED (snippet): Test line pressure in R, 3rd, 4th and manual 1 (both low and high side at each shift) against the pressure chart. Slips in R with low pressure = regulator or pump. Slips in R with correct pressure = friction element. — [search set: FreeASEStudyGuides pressure tests](https://www.freeasestudyguides.com/automatic-transmission-pressure-tests.html); [Industrial Monitor Direct](https://industrialmonitordirect.com/blogs/knowledgebase/reverse-line-pressure-in-automatic-transmissions-why-its-higher). A.8, A.14 (and A.11).
- DOCUMENTED (snippet): Two-gauge method. Line pressure on one gauge and the holding element's circuit on the other. A difference beyond spec (often ~8–15 psi) = leak in that circuit. With the connector unplugged (max line pressure), a small leak can be **masked**. — same search set; see also [Sonnax 5L40-E loss of reverse](https://www.sonnax.com/tech_resources/132-5l40e-5l50-e-isolating-concerns-re-loss-of-reverse-or-tcc). The psi figure is a snippet generality. Needs SI.
- DOCUMENTED (snippet): Air test. Apply air to each clutch port. A dull thud or felt movement = the piston applied. Hissing = leaking seals or check ball. If air fails to apply a clutch, or applies two at once, inspect case passages (cross-leak). — [Chrysler/Jeep SI "Clutch Air Pressure Tests"](https://s3.amazonaws.com/jeepwranglerjk2010/7c033609.html); [Scribd air-pressure test guide](https://www.scribd.com/document/526092007/Auto-Transmission-Air-Pressure-Test). C.21.
- DOCUMENTED (snippet): Sonnax uses an electrical split (unplug the connector to force failsafe) and a mechanical split (block the band) to confirm a no-reverse. — [Sonnax 4L80-E](https://www.sonnax.com/tech_resources/88-diagnosing-the-elusive-no-reverse-with-the-4l80-e).

### Inferences
- INFERRED: Match each chart suspect to a test. A band suspect: air-test the servo apply, watch the band tighten, check strut/anchor (C.23). A clutch suspect: air-test for the thud, measure clearance (C.20), inspect frictions and steels (C.19). An OWC suspect: rotate by hand, it should hold one way and freewheel the other, and check the race and rollers (C.22). A multi-range suspect sharing a feed (e.g., the 4L80-E direct clutch in 3/4/R): check the feed's sealing rings and check ball before the friction pack.
- INFERRED: When two elements are applied from the same pressure circuit, a pressure tap on that circuit plus the chart can separate "the circuit leaks" (pressure drops in every range that uses it) from "the element's pack is worn" (pressure OK, slip in those ranges).

### Gaps
- OPEN: Per-unit pressure tap locations and specs were not collected (needs SI). They are out of scope for ASE, which gives specs when they are needed.

## 6. Common student mistakes with apply charts

### Takeaway
Most chart misses come from ignoring working ranges, confusing seized with released symptoms, mixing manufacturer names, or forgetting the OWC vs manual-range separation.

### Cited Findings
- DOCUMENTED (snippet): The elimination principle, used to avoid these misses, is to rule out devices that also apply in good gears. — [FreeASEStudyGuides clutch/band charts](https://www.freeasestudyguides.com/transmission-clutch-band-chart.html); [FreeASEStudyGuides solenoid charts](https://www.freeasestudyguides.com/transmission-solenoid-charts.html) (use the solenoid and clutch charts together to split electrical from mechanical).
- DOCUMENTED (snippet): Name collision. "Forward clutch" on AOD, 4L60-E and 5R55 vs "rear clutch" on the A727. "Direct clutch" on GM/Ford vs "front clutch" on Chrysler. Letters on Ford/ZF vs gear names on GM. — [Poly318 A727 manual](https://poly318.com/wp-content/uploads/2023/07/1966_1977_TorqueFlite_727_904_Service_Manual.pdf); [Raybestos 6R80](https://www.raybestospowertrain.com/blog/6r60-6r80-6hp26-b-clutch-3-5-r-direct-installation-rtk-6r82); [Gears 6L80](https://gearsmagazine.com/magazine/tackling-clutch-failure-in-the-gm-6l80-90/).

### Inferences
- INFERRED (mistake list):
  1. Picking an element applied in the failed range **and** in a working range. It is exonerated.
  2. Picking a "seized" element for a slip/no-drive symptom, or a "failed/broken" element for a bind-up symptom. The ASE sample's choice D ("seized forward clutch") tests this.
  3. Treating a normal OWC freewheel (no engine braking in D) as a fault.
  4. Forgetting that the manual-1 element and the reverse element are often the **same part** (L/R band or clutch). Always ask about manual-1 engine braking when reverse is lost.
  5. Reading the "applied but not transmitting torque" cells (e.g., the AOD intermediate clutch in 4th, the 4L60-E forward clutch in 4th) as load-bearing. An element that only prepares a downshift will not cause slip in that gear.
  6. Assuming a single failure means a single failed range. On clutch-to-clutch units (Lepelletier, 8/9/10-speed) one element spans 3–6 ranges.
  7. Blaming a friction element before checking fluid level, linkage/range sensor, commanded gear and failsafe.
  8. Carrying one unit's names into another (e.g., assuming "C1–C5" on a 6L80).
  9. Ignoring P and N information. "Rolls in neutral" and "no bind in park-to-reverse" rule out seized elements and output/park faults.

### Gaps
- OPEN: No instructor-published "common mistakes" list was found. The list above is INFERRED from the method and the ASE sample distractors.
