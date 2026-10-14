#!/usr/bin/env python3
"""Build the class final prep sheet (final_prep_v2.md) to HTML + PDF.
Reuses the CSS/markdown helpers from ase/build.py. Usage: build_unit2.py"""
import re, subprocess, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent / "ase"))
import build as b

HERE = Path(__file__).resolve().parent
VERSION, DATE = "2.0", "2026-10-14"
md = (HERE / "final_prep_v2.md").read_text()
secs, toc = [], []
for i, (title, body) in enumerate(b.sections(md), 1):
    m = re.match(r"(\d+)\.\s*(.*)", title)
    if m: i, name = int(m.group(1)), m.group(2)
    else: name = title
    toc.append(f'<li><a href="#s{i}"><span class="tn">{i:02d}</span>{name}</a></li>')
    secs.append(f'<section id="s{i}"><div class="sec-head"><span class="sec-num">{i:02d}</span><h2>{name}</h2></div>{b.md_to_html(body)}</section>')
page = f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Class Final Prep</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Oswald:wght@500;600;700&family=IBM+Plex+Sans:ital,wght@0,400;0,500;0,600;1,400&family=IBM+Plex+Mono:wght@500;600&display=swap">
<style>{b.CSS}</style></head><body><div class="wrap">
<div class="masthead"><div class="eyebrow">GM ASEP <span class="sep">/</span> A2 <span class="sep">/</span> CLASS FINAL <span class="sep">/</span> VERSION {VERSION}</div>
<h1>Class Final Prep</h1><p class="sub">Units 1 and 2, weighted by priority and your quiz misses.</p>
<div class="meta-row"><span><b>Prepared</b> {DATE}</span><span><b>Scope</b> Instructor scope (class notes), not the ASE task list</span></div></div>
<nav class="toc"><div class="toc-title">Contents</div><ol>{''.join(toc)}</ol></nav>
{''.join(secs)}
<footer><span>Class Final Prep &middot; v{VERSION} &middot; {DATE}</span><span>Private study material.</span></footer>
</div></body></html>"""
out = HERE / "final_prep_v2.html"; out.write_text(page)
pdf = HERE / "final_prep_v2.pdf"
subprocess.run([b.CHROME, "--headless", "--no-sandbox", f"--print-to-pdf={pdf}", "--no-pdf-header-footer", f"file://{out}"], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
print("wrote", out.name, pdf.name)
