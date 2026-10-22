# A8 study context

Status: **Ready for intake (2026-10-22).** Folder set up, preferences carried over from A2. Official ASE reference verified and task map built (2026-10-22). No notes received, no guides yet.
Created: 2026-09-20. Last updated: 2026-10-22.

## Intent

Build understanding from course notes, public teaching material, shop examples and verified research. Produce instructor-focused final prep and broader ASE prep when requested. Read `WORKFLOW.md` for the process and `research.md` for coverage and evidence.

## Current facts

- Exam/subject: A8 Engine Performance. The instructor syllabus and current official exam blueprint have not been reviewed.
- Timing: spring semester (per the repo `CLAUDE.md` as of 2026-09-30). Exact dates not stated.
- Relationship to L1: **passing A8 is required to register for L1** (DOCUMENTED, L1 guide p. 3). L1 goes deeper into the same material. If both are being studied, A8 research should be reusable for L1 and kept in this folder.
- Class start, class-final date and ASE appointment: unknown. Don't infer them; ask when planning needs them.
- Textbook/edition, prep books and named lab assemblies: not yet recorded.
- Current mode: **intake**. Raw notes go in `notes/` (see `notes/README.md`). Official-reference research done 2026-10-22 at Logan's request. Study packages start only when Logan asks.

## Carried over from A3/A2 (learner preferences, already decided; do not re-ask)

- Learner: GM ASEP student, about 2 years at a GM dealership. Passed A3 (class final 2026-09-21) and A2 (class final 2026-10-14, ASE 2026-10-15; reported passed 2026-10-22). Strongest at electrical/electronic reasoning. Weaker at chart/table-driven reasoning (A2: planetary apply charts) and at two-direction diagnostic logic (A2: stall speed high vs. low). Expect the same pattern on diagnostic-direction questions here and test for it early.
- ASE rewards textbook and service-manual reasoning over shop habit. Show it where the two differ.
- Two packages per course, kept separate:
  - **Class:** unit guides plus a tier-weighted class-final prep. These follow instructor scope, so they're built from the notes.
  - **ASE:** a three-layer package in `study/ase/`: a full guide, a simple sheet (the middle layer, with `[G x.x]` pointers into the guide) and a 2-3 page cram sheet. It follows the official task list and weights.
- No practice questions in guides. Logan owns Motor Age and GM-training banks, so never reproduce or substitute for them. Log missed concepts only.
- Test or quiz reviews become a "confirmed weak spots" block in every layer (A2's Unit 2 review is the model: `autotrans/notes/unit2.txt` → Section 0 of `autotrans/study/unit2_study_guide_v2.md`).
- Give important topics their own page. Don't paste whole source PDFs into guides.
- PDFs are letter size in the claude-paper style, each marked with a version and an absolute date. Build with `python3 tools/studybuild.py <file.md>` (header block format is in its docstring). Render the changed pages (`pdftoppm` + `montage`) and look at them before calling a PDF done. A rebuild Logan asks for gets a `_vN` filename and the old version is deleted (it stays in git history).
- No cloud or remote agents (no credits). Keep research small and anchored to the notes and the official task list.

## Decisions to preserve

Preserve raw notes and the learner's file arrangement. Class scope comes from the instructor; ASE scope comes from its verified official guide. Label outside qualifications and actual source access. Lead guides with broad exam-ready explanations and retain service-level detail in research unless a named design matters. Keep readiness separate from document coverage. Either assistant can draft or review, and should leave usable state here.

## Last work / next action

- 2026-09-20: Empty scaffold created.
- 2026-10-22: Environment prepped after A2 was passed. Added `notes/README.md` (intake rules), tracked `sources/` and `study/`, and recorded the carried-over preferences above. The shared PDF builder is `tools/studybuild.py` (generalized from the A2 builder; it rendered the A2 cram sheet identically in a test). No technical work done.
- 2026-10-22 (later): Official A8 reference verified and a weighted task map built in `research.md` (50 scored of 60, 75 min, ~1.25 min per question; E computerized controls 26% and B ignition 16% are the highest yield per task, EVAP is the top emissions topic). The ASE guide already in `../mantrans/sources/ase/` is the current edition (byte-identical download). Ten public sample questions summarized; several hinge on which direction a reading points (Logan's A2 weak spot).
- Next action: intake Logan's first notes and add a Notes column to the task map in `research.md`. **A8 must be passed before L1 can be booked** (DOCUMENTED, L1 guide p. 3). The A8 diagnostic-direction trap list is optional; Logan hasn't asked for it yet.
