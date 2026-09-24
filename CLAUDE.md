# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

This is not a codebase. It is Logan's GM ASEP study workspace, with one folder per course/ASE exam, in one private git repo (`flyboy-byte/asep-study`). See `README.md`.
There are no build, lint, or test commands. Each course's leftover `.gitignore` is
`*`, so use `git add -f` for new files there.

## Layout

| Folder | Exam | State (2026-09-22) |
| --- | --- | --- |
| `mantrans/` | A3 Manual Drive Train & Axles | Active/most complete. Version 2 class-final + ASE packages built 2026-09-18. |
| `autotrans/` | A2 Automatic Transmissions | Framework scaffold. `notes/` has class screenshots from 2026-09-20; `CONTEXT.md` still says course work has not started. |
| `engine-performance/` | A8 | Framework scaffold only (spring semester). |
| `l1/` | L1 | Framework scaffold only. |
| `l2/`, `l3/` | — | Empty placeholders. |

Each course folder is self-contained and has its own `CLAUDE.md`/`AGENTS.md`, `CONTEXT.md`, and
standard subfolders: `notes/` (raw notes and images), `study/` (generated guides, cram sheets,
HTML/PDF), and `sources/` (outside references). **Work from inside the relevant course folder and
read its `CONTEXT.md` first.** That file is the state doc. It records dates, learner preferences,
source boundaries, and the file inventory. If it conflicts with this file, `CONTEXT.md` wins.

`mantrans/` predates the framework and was moved here from `~/projects/manual-transmissions` on
2026-09-20. Its research lives in `a3_research_foundation_2026-09-13.md`. The scaffolded folders use
`research.md` + `WORKFLOW.md` instead.

## Reusable framework

The process is defined in `workflow/` (merged into this repo 2026-09-24 from the former public repo
github.com/flyboy-byte/asep-study-workflow) and the `ase-study` skill. `WORKFLOW.md` in each
scaffolded folder is a copy of that process. Use it, but don't reorganize existing notes to fit it.

## Rules that apply across every course

- **Don't start a future course's work until Logan asks.** Having a scaffold, or talking about a
  course, does not authorize research or study packages. Check the `Status:` line in `CONTEXT.md`.
- **Never rewrite raw notes** in `notes/`. Put corrections and outside qualifications in the research
  file, with the source and where they apply. A generated guide may narrow a claim only when the
  correction is backed by a source.
- **Class-final guides follow instructor scope** (the notes). **ASE guides follow the official ASE
  task list and weights** and use the whole folder. Don't let broad ASE research drive a class-unit guide.
- Keep documented fact, general principle, classroom emphasis, inference, and open questions
  distinct. A GM example isn't a universal rule. Findings from Codex/ChatGPT are inputs to verify.
- Logan owns Motor Age and GM-training ASE practice questions. Don't build a substitute ASE question
  bank. Original instructor-style questions belong in class-final/unit guides.
- Print outputs are letter-size PDFs using the `claude-paper` visual system
  (formatter: `~/Downloads/whitepaper-formatter.html`). Mark each one with a version and an
  absolute date. Render and visually check each changed PDF.
- After meaningful work, update the course's `CONTEXT.md` with the date, files processed, outputs
  changed, and next action.
