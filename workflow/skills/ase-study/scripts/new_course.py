#!/usr/bin/env python3
"""Create an empty local course scaffold; never merge into an existing folder."""
import argparse
from datetime import date
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("destination", type=Path)
    parser.add_argument("--exam", required=True, choices=[f"A{i}" for i in range(1, 10)] + ["L1"])
    args = parser.parse_args()
    destination = args.destination.expanduser().absolute()
    if destination.exists() or destination.is_symlink():
        parser.error(f"Destination already exists; nothing changed: {destination}")

    skill = Path(__file__).resolve().parents[1]
    today = date.today().isoformat()
    files = {}
    for name in ("CONTEXT.md", "research.md", "AGENTS.md"):
        content = (skill / "assets" / "course" / name).read_text(encoding="utf-8")
        files[name] = content.replace("{{EXAM}}", args.exam).replace("{{DATE}}", today)
    files["CLAUDE.md"] = files["AGENTS.md"]
    files["WORKFLOW.md"] = (skill / "references" / "workflow.md").read_text(encoding="utf-8")
    files[".gitignore"] = "# Keep personal coursework out of a parent repository by default.\n*\n"

    destination.mkdir(parents=True, exist_ok=False)
    for name, content in files.items():
        (destination / name).write_text(content, encoding="utf-8")
    for name in ("notes", "study", "sources"):
        (destination / name).mkdir()
    print(f"Created {args.exam} scaffold: {destination}")
    print("Ready for notes or a web-first research request. No study work started.")
    print("Start with CONTEXT.md. Existing folders are never overwritten.")


if __name__ == "__main__":
    main()
