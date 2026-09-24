# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

This is not a codebase — it's study material for a GM ASEP A3 (Manual Drive Train and Axles) semester,
split into three units (clutches, transmission/transaxle, differentials/axles). No build/lint/test
commands apply. Not a git repo.

## What's here

Layout: `notes/` (raw notes, class images, instructor exams), `study/` (generated guides, cram sheets, HTML/PDF), `sources/` (outside references). Raw notes, generated guides, and research files accumulate here as the semester progresses — don't
maintain a second file inventory in this doc. Read `CONTEXT.md`'s "Supporting material now available"
table for the current, kept-up-to-date list of every file and its role. Two things worth knowing before
you open that table:

- `gears.txt` includes a pasted ChatGPT audit correcting an earlier draft of the synchronizer-sequence
  explanation — that corrected version is the one to trust, and the raw notes files self-flag spots
  where Logan was confused, which are worth double-checking rather than treating as settled.
- `deep-research-report (3).md` is full-exam-scope ASE research and was deliberately *not* used as a
  source for the per-unit Unit 2 guides — see "Conventions" below for when broader ASE material is and
  isn't allowed to feed into a document.

## Conventions established so far

- Each unit gets a study guide + cram sheet pair, built from that unit's raw notes file — not from the
  deep-research report, unless the user asks to pull ASE-exam framing in explicitly.
- Never rewrite the raw notes. A generated guide may correct or narrow an over-broad statement when
  the user requests research and the correction is source-backed; keep the supporting evidence and
  application boundary in the research foundation rather than silently changing the note.
- Unit 3 notes live in `notes/drive-axles.txt` and may still grow. Version 2 of the Unit 3, class-final, and
  ASE packages incorporates the September 18 additions. Refresh only affected sections from later
  notes and cross-check the copied Unit 3 exam if it becomes visible. The guides in `study/` follow the
  separate source boundaries in `CONTEXT.md`.

## Current context and reusable workflow

Read `CONTEXT.md` for the current schedule, learner preferences, research role and later-course boundaries. The reusable public framework and shared `ase-study` skill live in `/home/logan/projects/asep-study-workflow`. Use that framework when relevant without reorganizing these existing notes or starting a future course before Logan requests it.
