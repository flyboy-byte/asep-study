# asep-study

Logan's GM ASEP study workspace: one private repo holding every course's notes, generated study
material, and the reusable workflow that builds it. Last updated 2026-09-24.

## Layout

| Folder | Exam | State |
| --- | --- | --- |
| `mantrans/` | A3 Manual Drive Train & Axles | Done for the class final. ASE prep package (full guide, simple sheet, cram sheet, PDFs) in `study/ase/`. |
| `autotrans/` | A2 Automatic Transmissions | Note intake active (`note/`, `notes/`). No study package yet. |
| `engine-performance/` | A8 | Scaffold only (spring semester). |
| `l1/` | L1 | Scaffold only. |
| `l2/`, `l3/` | — | Empty placeholders. |
| `workflow/` | — | The reusable process and the `ase-study` skill (merged in 2026-09-24 from the former separate repo, history kept). |

Each course folder has `notes/` (raw notes, never rewritten), `study/` (generated guides, cram
sheets, HTML/PDF), `sources/` (outside references), and a `CONTEXT.md` that holds the current state.
Read a course's `CONTEXT.md` before touching it.

## Setting up on a new machine

```sh
gh auth login
gh repo clone flyboy-byte/asep-study ~/projects/asep-study
cd ~/projects/asep-study   # start Claude Code here or in a course folder
```

The `ase-study` skill loads automatically from `.claude/skills/ase-study`, a symlink to
`workflow/skills/ase-study`. Nothing else needs installing. Printable PDFs are already committed.

Not in the repo: Claude session history and memory (`~/.claude/`), your global `~/.claude/CLAUDE.md`,
and `~/Downloads/whitepaper-formatter.html` (the claude-paper styling reference, needed only to
make new PDFs match the existing ones).

## Notes on the repo

- Private. It includes instructor exams and a third-party PDF (`mantrans/sources/drivetrain/`), so do
  not make it public.
- `autotrans/note/` and `autotrans/notes/` both exist; `note/` is the organized intake from
  2026-09-22.
