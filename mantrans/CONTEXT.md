# Project purpose and preparation context

Last updated: 2026-09-22

## Status update — 2026-09-22

The class final was taken Monday 2026-09-21. Logan is now in full professional-ASE-prep mode (no more class-final work expected). Logan reported the three areas missed on the final: driveline/working-angle questions, heel-and-toe ring & pinion contact-pattern reading, and (implicitly) transfer-case fork logic. A new raw note, `notes/transfercases-ujoints.txt`, captures Monday's in-class discussion of transfer-case range/mode forks, planetary gearset rules, and U-joint phasing/order-of-vibration.

**Version 3** of `study/ase/ase_a3_study_guide.md` / `study/ase/ase_a3_whitepaper.html` / `study/ase/ase_a3_study_guide.pdf` (18 pages) incorporates this directly into Sections D and F:

- Section D gained "Why a Cardan (cross-type) U-joint vibrates" (order-of-vibration, phasing, working-angle tolerance) and "Measuring and reading working angle" (how to compute a joint's working angle from two connected members, not shaft slope alone).
- Section E gained "Reading the contact pattern" — the depth-vs-backlash / face-flank-vs-heel-toe adjustment table, directly answering the missed ring & pinion question type.
- Section F gained "Range fork vs. mode fork" (with a Tech A/Tech B practice question) and "Planetary gearset — the three-member hold rule" (general hold/input/output pattern, not the instructor's specific numeric example — confirmed with Logan that A3 planetary content is transfer-case-based, not automatic-transmission-based).

Only the ASE guide was updated — the class final is over, so no changes were made to `study/class_final_study_guide.*`. Unit 2/Unit 3 guides were also left alone; this is new material, not a unit revision. The `study/ase/ase_a3_study_guide.pdf` was re-rendered and spot-checked (page count, section order via `pdftotext`). The three other already-rendered PDFs (`class_final_study_guide.pdf`, `unit3_study_guide.pdf`) still reflect the pre-2026-09-20 relative-link paths mentioned below and were not touched this session.

**Follow-up same day:** Logan clarified the procedural depth (contact-pattern adjustment direction, working-angle measurement) is wanted, not a mistake — the actual ask was to go deeper still, make the now-longer guide easier to navigate, and add two new outputs:

- Full nested table of contents added to `study/ase/ase_a3_whitepaper.html`/`.pdf` (every H2 under its section, not just the six lettered sections) — the guide is now 18 pages.
- New `study/ase/ase_a3_cram_sheet.md` — a standalone one-page-style dense reference covering all six categories plus exam mechanics and 20 instant answers, matching the `unit2_cram_sheet.md`/`unit3_cram_sheet.md` convention (md only, not separately rendered, same as those files).
- New `study/ase/ase_a3_simple_sheet.md` + `study/ase/ase_a3_simple_sheet.html` + `study/ase/ase_a3_simple_sheet.pdf` — a genuinely new document tier: a condensed, narrative (not just bulleted) pass through all six categories, deliberately mid-depth between the cram sheet and the full guide, with no setup-procedure detail. Rendered to exactly 4 letter pages.

**Second follow-up same day: graded class-final photos.** Logan sent a photo of his Scantron/answer sheet plus three photos of specific question text with the instructor's key (circled correct answers), and asked specifically for the hunting/non-hunting and heel/toe corrections, then flagged Q46/47/49 (clutch noise/chatter) as the ones he wanted, saying Q35/37 (unreadable from the Scantron alone) were "obvious" to him already — so those were left alone.

- Confirmed and incorporated (all three tiers — guide, simple sheet, cram sheet): a continuous-contact/self-adjusting (SAC) release bearing (common GM) is noisiest *engaged*, a traditional pedal-actuated one is noisiest *disengaged* (Q47); clutch **chatter** has its own cause map — contamination, uneven pressure-plate fastener torque, low clutch master-cylinder fluid — separate from slip/drag and free play (Q46, Q49); a 15–20 mph full-throttle high-gear road test checks both slippage and spin-down (Q48); air in the hydraulic clutch circuit is a drag cause requiring a bleed (Q51); a broken axle shaft on an **open** differential can cause a no-drive condition on both wheels, not just the broken side (Q59).
- **Not incorporated — flagged as open instead.** Q58 (heel/toe): the photographed key marks only "Student A" correct, which would mean "toe = inner end of the ring gear tooth" is being scored wrong — that contradicts standard terminology *and* Logan's own existing `drive-axles.txt` notes, so nothing was changed. Q60 (hunting/non-hunting): the key marks "Both A and B," but as worded, both technicians have the hunting/non-hunting definitions backwards from the standard trade definition (and from what's already documented in `unit3_cram_sheet.md`). Both were logged as open questions rather than silently trusted from a single photo read.
- **Q58 resolved same day.** Logan clarified he did not verify my flag against a scantron mark for that specific question (Q58/59/60 aren't on the Monday-final Scantron at all — that clutch/hypoid/hunting quiz packet is a separate document from the Scantron final). He then confirmed directly: **toe = inside, heel = outside** — matching what was already in the guide. So the guide's content was already correct; the photographed key's apparent contrary reading is set aside as a probable misread or key error, not acted on.
- **Q60 (hunting/non-hunting) added same day, not left open.** Logan said the concept isn't complex enough to keep flagging — added the standard definition directly to Section E in all three tiers ("Hunting vs. non-hunting gear sets"): hunting = tooth counts share no common factor, ratio doesn't reduce, no timing marks needed; non-hunting = ratio reduces to a whole number, repeating tooth-contact pattern, timing marks required at reassembly. The photographed key's "Both A and B" reading (which credits both technicians despite their statements having the definitions swapped relative to each other) is set aside, not reflected.

**Third follow-up same day: honest assessment + gap-check on B/C.** Logan asked for an honest opinion of the guide. Main critique given: it's grown *reactively* — Sections D/E/F got deep, repeated attention because Logan kept surfacing specific missed questions there, while B (Transmission, 17%) and C (Transaxle, 17%) — 34% combined, the largest chunk of the exam — hadn't been touched since the original Unit 2 pass, not because they're solid but because nothing had tested them recently.

Logan asked for the "low cost way to address that" and approved doing it: a **task-list gap-check**, not a rewrite — read the official 2026 ASE A3 task list (`sources/ase/ASE_Automobile_Study_Guide_2026.pdf`, pages 16-18) directly and diff it against what Sections B and C actually cover, rather than guessing or adding untargeted new material.

Findings and fixes (all three tiers — guide, simple sheet, cram sheet):
- **Real gaps found:** gaskets/seals/sealing surfaces and case bores/dowels/vents are explicit official task-list items for both B and C but weren't mentioned in either section. C additionally had no cross-reference to Section E's preload/backlash/contact-pattern setup logic even though the task list tests the transaxle's integrated final drive on that exact same logic, and no mention at all of lubrication/fluid level or electrical/electronic coverage (B had both).
- **Added to B:** new "Gaskets, seals, and case integrity" subsection — mating-surface seals, case bores/dowels/vents (blocked vent → leak past a good seal), mount inspection.
- **Added to C:** new "Setup, seals, fluid, and electronics" subsection — explicit cross-reference to Section E's setup/contact-pattern material for the transaxle's final drive, plus the same gasket/seal/vent, fluid/lube, and electrical/electronic coverage as B.
- Full guide is now 21 pages; simple sheet still renders to exactly 4 pages; cram sheet got one line added to each of B and C rather than new sections, to stay proportionate to its density.
- Added a new **"Confirmed weak spots"** section near the top of `ase_a3_study_guide.md`/`.html`/`.pdf` (right after "ASE question method," before Section A) at Logan's request — a table indexing every final-derived correction back to its normal category section, plus the Q58/Q60 open-item note. The guide is now 19 pages. The same facts were also added in-place inside their normal sections (A and E) in all three document tiers, not just the index.

## Intended end product

This folder contains two working preparation packages with different source priorities. Logan updated the schedule and requested inspectable drafts on Thursday, 2026-09-17:

- **Class final: Monday, 2026-09-21.** Preparation is based mostly on Logan's class notes, reflecting the textbook material used by the instructor. Instructor coverage and emphasis determine the scope. External research can resolve a specific uncertainty, but should not expand this into a professional ASE review.
- **ASE preparation:** Logan expects to take A3 during the week beginning 2026-09-21; friends are taking it during the preceding weekend and need a usable guide immediately. Use the entire current directory: notes, unit guides, the broad research report, official ASE guide, and Codex's supporting research. Logan's exact appointment remains unspecified.
- **Current work:** Version 2 drafts now exist for Unit 3, the class final, and ASE A3. The September 18 rear-axle additions have been incorporated. Notes may still grow before the final, including on Monday, so preserve these as updateable outputs.

The September 13 estimate that synthesis would happen the following week and the September 16 Friday-final date are superseded. Initial class-final and ASE packages were assembled on September 17 and revised to Version 2 on September 18 after new notes arrived. Refresh only the affected sections if later notes change the coverage.

The earlier “not ready yet” instruction referred to producing the packages before Logan requested them. On September 17 Logan explicitly requested both guides now, while noting that he may ask for another pass after additional notes. Continue research or revision when it answers a specific gap; do not delay a useful draft merely because the semester material may still change.

## Educational context

- This is Logan's **seventh ASE**, as clarified September 16, 2026. Logan is fairly adept at electronics and will rely on prior ASE study and other electrical experience. Do not infer a personal electrical weakness from a thin explanation in a document.
- For the later A3 package, keep electrical preparation brief and focused on drivetrain-specific sensors, actuators, engagement controls, module inputs/outputs, and calibration topics. Avoid a general electrical fundamentals course unless a particular question reveals a need. Published tasks establish eligible content, not a frequency ranking for individual electronic components.
- This is a GM ASEP class. Instruction and lab applications are GM-oriented.
- The course textbook is not GM-specific. Its general drivetrain teaching also contributes to the class final.
- ASE A3 is not GM-specific and has its own published coverage.
- Logan owns a Motor Age ASE preparation book/question source and also has GM training ASE practice questions. Their editions and exact contents have not been inspected. They can supply ASE practice independently; the local ASE document should remain a good study guide based on the class material, official scope, and supporting research rather than adding an invented question bank or a workflow for using the owned questions.
- Logan values the ASEP sequence of concentrated textbook study, shop examples, and taking ASE exams while that material is fresh. Build on those recent classroom and practical connections when synthesizing the later prep.
- Official A3 approximate weighting matters to Logan: clutch 16%, transmission 17%, transaxle 17%, shafts/joints 13%, drive axles 17%, and 4WD/AWD 20%. Preserve ASE's published percentages; use them with demonstrated strengths and weaknesses, not as rigid study-time allocations.
- The class-final package is primarily notes-based, with the instructor's textbook coverage and relevant GM classroom applications providing context. General ASE research can clarify an explanation, but ASE weighting does not establish the instructor's final-exam blueprint.
- Unit guides are scoped to their units. A subject absent from a Unit 2 sheet is not automatically a research or coursework gap.

## Roles and existing work

Claude's work on structure, formatting, basic corrections, and reasoning is satisfactory to Logan. Codex is contributing researched information, evidence, qualifications, mechanism explanations, and reusable supporting documents. This is preparation for a shared eventual output, not a request to replace or routinely critique Claude's role.

Preserve existing raw notes and unit guides. Record externally researched qualifications separately, with the source and the application boundary. Version 2 now combines selected researched distinctions with the class material where the September 18 notes needed a mechanism boundary; the raw notes remain unchanged.

## Evidence and synthesis rules

Distinguish documented manufacturer facts, general principles, recorded classroom emphasis, reasoned inference, and unresolved questions. A GM example may clarify a general mechanism without making its dimensions, lubricant, component arrangement, or test procedure universal. A different design is not evidence that the instructor described the lab unit incorrectly.

For each useful addition, record what it teaches, its source/date/application, where it helps the future class-final or ASE package, and any unresolved limitation. Prefer research that answers an identified question over additional generic summaries of already-covered subjects. Preserve the embedded synchronizer audit in `gears.txt` as part of the existing classroom material.

Research can combine broad public teaching resources, diagrams, and manuals with focused investigation of individual mechanisms or gaps. Logan asked about both approaches on September 16. Distinguish inspected material from a promising video/book/library that has only been located; do not count restricted content as reviewed.

At any later refresh, use the then-current complete folder. Do not mistake the files available on 2026-09-13 for all the material Logan will supply. Current format decisions are: letter-size PDFs for all three Version 2 packages; instructor-style original questions remain useful in the Unit 3 and class-final guides; the ASE guide does not include a locally invented practice bank because Logan already owns Motor Age and GM training questions.

## Supporting material now available

Folder layout (reorganized 2026-09-20 into the framework's standard course structure; nothing was renamed or edited): `notes/` holds the raw class notes plus class images and the instructor's Unit 2 exam; `study/` holds every generated guide, cram sheet, HTML and PDF (the former `prep/` contents moved here); `sources/` holds the outside references. This folder is `mantrans/` inside the ASEP study workspace, beside the other course folders. Paths in the table below are relative to this folder.

**`study/ase/` (added 2026-09-22):** all professional-ASE outputs (the three depth tiers — full guide, simple sheet, cram sheet) were split into their own subfolder, separate from the class-unit and class-final files that sit directly in `study/`. Its files' relative links to `notes/`/`sources/` go up two levels (`../../notes/...`) instead of one.

| File | Role |
|---|---|
| `notes/clutchsection.txt`, `notes/gears.txt` | Raw Unit 1 and Unit 2 notes; retain original wording. |
| `notes/drive-axles.txt` | Raw rear-axle notes, updated September 18 with open/limited-slip/locking designs, the GM/Eaton mechanical-locker sequence, and expanded gear/bearing/tire noise diagnosis. Logan may add more before the final. |
| `study/unit2_study_guide.md`, `study/unit2_cram_sheet.md` | Existing Unit 2 material derived from gear notes. HTML/PDF versions also exist. |
| `sources/deep-research-report (3).md` | Broad A3 research blueprint and initial practice questions. Project and Downloads copies matched on 2026-09-13. |
| `a3_research_foundation_2026-09-13.md` | Combined Codex research, updated September 18: original gap findings, worked examples, official-ASE research, broader teaching resources, and 49 indexed sources. The latest targeted continuation verifies the GM/Eaton G80/MLocker sequence, separates clutch/helical/selected/automatic traction devices, and qualifies the new bearing-noise observations. Filename retained to keep the directory tidy. |
| `notes/unit2 exam.pdf` | Present on 2026-09-16; not inspected or used as evidence in the official-ASE research pass. |
| `notes/transfercases-ujoints.txt` | Raw notes added 2026-09-21 from Monday's pre-final class discussion: transfer-case range/mode fork distinction, planetary gearset hold/input/output rules with a worked class example, and U-joint phasing/working-angle/order-of-vibration detail. Feeds the Version 3 ASE guide only. |
| `sources/ase/ASE_Automobile_Study_Guide_2026.pdf` | Unmodified official 2026 ASE Automobile guide, retrieved September 16. A3 is on printed pages 16–20. Available locally for the broader ASE prep. |
| `sources/drivetrain/` | Three unmodified public primary-source PDFs: KHK gear primer, BorgWarner AWD actuator paper, and TREMEC TR-3550/TKO service manual. Selected relevant sections inspected September 16; source links and page locations are in the research foundation. |
| `study/class_final_study_guide.md`, `study/class_final_whitepaper.html`, `study/class_final_study_guide.pdf` | **Version 2**, revised September 18. Notes-led Units 1–3 class-final package with the new differential/noise material and 24 original instructor-style questions. The 16-page letter PDF uses the `claude-paper` visual system and was visually checked. |
| `study/ase/ase_a3_study_guide.md`, `study/ase/ase_a3_whitepaper.html`, `study/ase/ase_a3_study_guide.pdf` | **Version 3**, revised September 22. Professional A3 guide organized by the official 2026 weights and task areas, with a broad exam-level traction-device map and no locally invented ASE question bank. Version 3 adds U-joint order-of-vibration/working-angle measurement, ring & pinion contact-pattern reading (depth vs. backlash), transfer-case range-fork-vs-mode-fork logic with a Tech A/Tech B question, and planetary gearset hold rules — targeted at topics Logan reported missing on the class final — plus a full nested table of contents for navigation. The 18-page letter PDF uses the `claude-paper` visual system and was spot-checked (page count, section order). |
| `study/ase/ase_a3_cram_sheet.md` | New September 22. Standalone one-page-style dense reference (all six categories, exam mechanics, 20 instant answers), same convention as the Unit 2/3 cram sheets — markdown only, not separately rendered. |
| `study/ase/ase_a3_simple_sheet.md`, `study/ase/ase_a3_simple_sheet.html`, `study/ase/ase_a3_simple_sheet.pdf` | New September 22. A third depth tier between the cram sheet and the full guide: narrative-paragraph coverage of all six categories with no setup-procedure detail. Renders to exactly 4 letter pages. |
| `study/unit3_study_guide.md`, `study/unit3_cram_sheet.md` | **Version 2**, revised September 18 from the current `drive-axles.txt` and its referenced class images. The guide includes 32 original instructor-style questions and keeps the GM/Eaton sequence because it was taught directly. |
| `study/unit3_whitepaper.html`, `study/unit3_study_guide.pdf` | Styled Version 2 Unit 3 artifact using the visual system from Logan's `scripts-and-docs/claude-paper/whitepaper-formatter.html`. The 18-page letter PDF was visually checked and ends with a one-page cram sheet. |

Unit 1 and Unit 3 guide/cram pairs, Unit 3 raw notes, the complete textbook, and an instructor final-review sheet were not present among the visible project files on 2026-09-13. That is an inventory observation, not a request to supply them before research can continue.

The September 13 observation about Unit 3 raw notes is historical: `drive-axles.txt` is now present and still developing. Keep new research in the existing research foundation where practical; Logan prefers a clean directory while taking notes. Logan reported on September 17 that a copied Unit 3 exam had been placed in the directory, but no such file was visible after checking the project and searching likely filenames under the home directory; only `unit2 exam.pdf` was present. The Unit 3 guide therefore remains pending an exam-coverage cross-check.

## Reusable framework and later courses — 2026-09-16

Logan requested documenting the approach, structure, source strategy, intent and design as a reusable Claude/Codex skill and public GitHub framework. The separate project is `/home/logan/projects/asep-study-workflow`; its shared skill is `skills/ase-study/SKILL.md`, linked into both personal skill directories. Public repository: https://github.com/flyboy-byte/asep-study-workflow (published 2026-09-16). This keeps the manual-transmission notes folder intact. The framework supports personal notes, public student/college teaching material, and hybrid research, with technical claims verified against suitable sources.

- Automatic transmissions comes next and runs approximately four weeks. **Do not start that course's work yet:** Logan will begin when the time comes and notes/material are available. No automatic-transmission course folder or study package was installed by this framework task.
- Engine performance and advanced engine performance are in the **spring semester**, per Logan. They are future uses of the framework, not current study tasks. Exact course and exam dates remain unspecified.
- Logan reports the college will pay for L1 if he passes all nine ASE exams. Record this as his institution's reported funding arrangement, conditional on those results. ASE's currently published L1 registration prerequisite is passing A8; that is a separate requirement. See the official L1 page linked in the public pathway reference.
- Logan is open to sharing selected personal course material on GitHub. Do not impose a blanket ban on original notes or guides. Review the actual proposed files for copied/restricted source content and identifying details; framework publication is not an instruction to upload this whole working folder.
- Logan requested small ASE, GM and GM ASEP logos with a prominent independent-project / unofficial-material disclaimer, and specifically prefers the blue GM logo. The published README includes that presentation, an original workflow graphic, organization links and separate artwork credits. The earlier recommendation to use text alone was superseded by this explicit design direction; no separately obtained trademark/artwork permission is claimed.

The earlier temporary A2-specific starter was superseded by the reusable public framework. Its preliminary A2 weighting check did not begin an A2 technical research program. Keep the user's course timing separate from framework development.
