# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

This is not a codebase. It is Logan's GM ASEP study workspace, with one folder per course/ASE exam, in one private git repo (`flyboy-byte/asep-study`). See `README.md`.
There are no lint or test commands. PDFs for new courses build with `python3 tools/studybuild.py <file.md>` (A2 and A3 keep their own builders). Only `workflow/.gitignore` exists (Python caches, `.env`, `courses/`, `local/`).

## Layout

| Folder | Exam | State (2026-10-22) |
| --- | --- | --- |
| `mantrans/` | A3 Manual Drive Train & Axles | Most complete. Class final taken 2026-09-21. ASE prep (Version 3 guide, simple sheet, cram sheet, PDFs) lives in `study/ase/`, separate from class-unit guides in `study/`. |
| `autotrans/` | A2 Automatic Transmissions | **Passed (reported 2026-10-22).** Closed. Final v2 package (guide, simple sheet, cram) in `study/ase/`, class guides in `study/`. |
| `engine-performance/` | A8 Engine Performance | Ready for intake. Official task list verified and weighted task map in `research.md` (2026-10-22). No notes or guides yet. Spring semester. |
| `l1/` | L1 Advanced Engine Performance | Ready for intake. Official guide + Composite Vehicle Type 4 booklet in `sources/ase/`, task map in `research.md` (2026-10-22). Passing A8 required to register. |
| `l2/`, `l3/` | — | Empty placeholders. |
| `workflow/` | — | Reusable process and `ase-study` skill source (not a course). |
| `bay-gen/` | — | Random GM vehicle + customer-concern generator (tkinter), for shop practice. Not a course. See its `README.md` (2026-10-22). |
| `tools/` | — | `studybuild.py`: shared md → claude-paper HTML + letter PDF builder for new courses (2026-10-22). |

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
github.com/flyboy-byte/asep-study-workflow) and the `ase-study` skill, which loads from `.claude/skills/ase-study` (a symlink into `workflow/skills/ase-study`). `WORKFLOW.md` in each
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

## Repo and new machines

Private repo: it includes instructor exams and a third-party PDF, so never make it public. Session history
and memory live in `~/.claude/`, not here; the state docs (`CONTEXT.md`) are how a fresh session resumes.
PDF rendering: `google-chrome-stable --headless --no-sandbox --print-to-pdf=<out>.pdf --no-pdf-header-footer file://<abs path>.html`
(each guide's `.html` is hand-mirrored from its `.md`; re-render after editing either). `README.md` has clone/setup steps.
