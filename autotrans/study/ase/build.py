#!/usr/bin/env python3
"""Build the A2 ASE guide/cram sheet HTML from markdown parts, then print to PDF.

Usage: build.py guide|cram   (reads study/ase/*.md, writes study/ase/*.html and *.pdf)
Markdown conventions: '## N. Title' starts a section; blockquotes that begin
with '**Label:**' become callouts; '[[FIGURE: file | caption]]' embeds a figure.
"""
import re, subprocess, sys
from pathlib import Path
import markdown

HERE = Path(__file__).resolve().parent
CHROME = "google-chrome-stable"

CSS = r"""
:root{--bg:#fff;--surface:#fff;--surface-2:#eef1ee;--ink:#14191b;--muted:#4d5659;--faint:#7c8688;--line:#d2d8d3;--line-hi:#b6bfb9;--accent:#c8481c;--accent-ink:#fff6f1;--accent-2:#2c4a4a;--trap:#9b2c2c}
*,*::before,*::after{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);font-family:'IBM Plex Sans',system-ui,sans-serif;-webkit-font-smoothing:antialiased;font-size:12.5px;line-height:1.55}
.wrap{max-width:760px;margin:0 auto;padding:0 6px}
h1,h2,h3,h4{font-family:'Oswald','Arial Narrow',sans-serif;text-transform:uppercase;letter-spacing:.02em;color:var(--ink);font-weight:600;text-wrap:balance}
p{margin:0 0 .7em}
strong{font-weight:600}
code,.mono{font-family:'IBM Plex Mono',ui-monospace,monospace;font-size:.92em}
a{color:inherit}
.masthead{border:1px solid var(--line-hi);border-radius:3px;padding:1.2rem 1.4rem 1rem;margin-bottom:.9rem;position:relative;overflow:hidden}
.masthead::before{content:"";position:absolute;left:0;top:0;bottom:0;width:6px;background:var(--accent)}
.eyebrow{font-family:'IBM Plex Mono';font-size:10.5px;font-weight:600;letter-spacing:.14em;text-transform:uppercase;color:var(--accent);margin-bottom:.5rem}
.eyebrow .sep{color:var(--faint)}
.masthead h1{font-size:30px;line-height:1.1;margin:0 0 .3rem}
.masthead .sub{font-size:13px;color:var(--muted);font-style:italic;margin-bottom:.8rem}
.meta-row{display:flex;flex-wrap:wrap;gap:.3rem 1.2rem;font-family:'IBM Plex Mono';font-size:10.5px;color:var(--muted);border-top:1px solid var(--line);padding-top:.6rem}
.meta-row b{color:var(--ink)}
.toc{border:1px solid var(--line);border-radius:3px;padding:.9rem 1.2rem;margin-bottom:1.2rem}
.toc-title{font-family:'IBM Plex Mono';font-size:10px;font-weight:600;letter-spacing:.14em;text-transform:uppercase;color:var(--faint);margin-bottom:.5rem}
.toc ol{list-style:none;margin:0;padding:0;display:grid;gap:.25rem}
.toc a{display:flex;gap:.6em;text-decoration:none;font-size:13px}
.toc a .tn{font-family:'IBM Plex Mono';font-size:10.5px;color:var(--accent);flex:none}
section{margin-bottom:1.4rem}
.sec-head{display:flex;align-items:baseline;gap:.7rem;border-bottom:2px solid var(--ink);padding-bottom:.3rem;margin:0 0 .8rem;break-after:avoid}
.sec-num{font-family:'IBM Plex Mono';font-size:12px;font-weight:600;color:var(--accent)}
h2{font-size:19px;margin:0}
h3{font-size:14px;margin:1.1rem 0 .4rem;color:var(--accent-2);letter-spacing:.03em;break-after:avoid}
h3 .n{font-family:'IBM Plex Mono';color:var(--faint);font-weight:500;margin-right:.4em}
h4{font-size:12px;margin:.8rem 0 .3rem;color:var(--muted);break-after:avoid}
.tbl-wrap{margin:.6rem 0 .9rem;border:1px solid var(--line);border-radius:3px;overflow:hidden}
table{width:100%;border-collapse:collapse;font-size:11.5px}
thead th{text-align:left;font-family:'IBM Plex Mono';font-size:9.5px;font-weight:600;letter-spacing:.07em;text-transform:uppercase;color:var(--faint);padding:.4rem .6rem;border-bottom:1px solid var(--line-hi);background:var(--surface-2)}
td{padding:.4rem .6rem;border-bottom:1px solid var(--line);vertical-align:top}
tbody tr:last-child td{border-bottom:none}
tr{break-inside:avoid}
td:first-child{font-weight:500}
ul,ol{padding-left:1.2rem;margin:0 0 .8rem}
li{margin-bottom:.25rem}
.note{display:flex;gap:.7rem;border:1px solid var(--line);border-left:3px solid var(--accent);border-radius:2px;padding:.55rem .8rem;margin:.7rem 0;font-size:12px;break-inside:avoid}
.note .tag{font-family:'IBM Plex Mono';font-size:9.5px;font-weight:600;letter-spacing:.08em;color:var(--accent);text-transform:uppercase;flex:none;padding-top:.1rem;min-width:4.6em}
.note.rule{border-left-color:var(--accent-2)} .note.rule .tag{color:var(--accent-2)}
.note.trap{border-left-color:var(--trap)} .note.trap .tag{color:var(--trap)}
.note .nb p:last-child,.note .nb ul:last-child{margin-bottom:0}
.note .nb{flex:1}
.tasks{font-family:'IBM Plex Mono';font-size:10px;color:var(--faint);margin:-.2rem 0 .8rem}
.figure{border:1px solid var(--line);border-radius:3px;padding:.7rem;margin:.9rem 0;break-inside:avoid}
.figure img{width:100%;max-width:360px;display:block;margin:0 auto;border:1px solid var(--line)}
.figure figcaption{font-family:'IBM Plex Mono';font-size:10px;color:var(--faint);margin-top:.5rem;line-height:1.5}
footer{margin-top:1.6rem;padding-top:.7rem;border-top:1px solid var(--line);font-family:'IBM Plex Mono';font-size:10px;color:var(--faint);display:flex;justify-content:space-between;gap:.5rem;flex-wrap:wrap}
@page{size:Letter;margin:.55in}
@media print{.toc{break-after:auto}}
"""

LABEL_CLASS = {"rule": "rule", "learner": "rule", "your quiz": "rule",
               "asetrap": "trap", "ase trap": "trap", "trap": "trap", "wrong direction": "trap",
               "classic mistake": "trap"}


def figure(m):
    fname, cap = [s.strip() for s in m.group(1).split("|", 1)]
    return (f'\n<figure class="figure"><img src="{fname}" alt="{cap}">'
            f'<figcaption>{cap}</figcaption></figure>\n')


def callouts(html):
    def repl(m):
        body = m.group(1)
        lab = re.match(r"\s*<p><strong>([^<]+?)[:.]?</strong>\s*", body)
        label, cls = "Note", ""
        if lab:
            label = lab.group(1).strip().rstrip(":.")
            cls = LABEL_CLASS.get(label.lower(), "")
            body = body[:lab.start()] + "<p>" + body[lab.end():]
        return (f'<div class="note {cls}"><div class="tag">{label}</div>'
                f'<div class="nb">{body.strip()}</div></div>')
    return re.sub(r"<blockquote>(.*?)</blockquote>", repl, html, flags=re.S)


def md_to_html(text):
    text = re.sub(r"\[\[FIGURE:\s*(.*?)\]\]", figure, text)
    html = markdown.markdown(text, extensions=["tables", "sane_lists"])
    html = html.replace("<table>", '<div class="tbl-wrap"><table>').replace("</table>", "</table></div>")
    html = callouts(html)
    html = re.sub(r"<h3>(\d+(?:\.\d+)+)\s+(.*?)</h3>", r'<h3><span class="n">\1</span>\2</h3>', html)
    html = re.sub(r"<p>\s*<em>(Tasks?:[^<]*)</em>\s*</p>", r'<p class="tasks">\1</p>', html)
    return html


def sections(md):
    parts, cur = [], None
    for line in md.splitlines():
        if line.startswith("## "):
            cur = [line[3:].strip(), []]
            parts.append(cur)
        elif cur is not None:
            cur[1].append(line)
    return [(t, "\n".join(b)) for t, b in parts]


def build(kind):
    cfg = {
        "guide": dict(files=["sec0_front", "sec1_foundations", "sec2_mech_hydraulic", "sec3_electronic",
                             "sec45_area_b_c", "sec67_types_strategy"],
                      src="ase_a2_study_guide_v2.md", out="ase_a2_study_guide_v2", ver="2.0",
                      title="ASE A2 Study Guide", h1="Automatic Transmission / Transaxle",
                      sub="Weighted to the official 2026 A2 task list. Class notes, the Unit 1 quiz misses and the research pass, in one guide."),
        "simple": dict(files=[], src="ase_a2_simple_sheet_v2.md", out="ase_a2_simple_sheet_v2", ver="2.0",
                     title="ASE A2 Simple Sheet", h1="A2 Simple Sheet",
                     sub="The middle layer: enough reasoning for a Tech A/B or most-likely stem, weighted to the official areas. [G x.x] = study guide section."),
        "cram": dict(files=[], src="ase_a2_cram_sheet_v2.md", out="ase_a2_cram_sheet_v2", ver="2.0",
                     title="ASE A2 Cram Sheet", h1="A2 Cram Sheet",
                     sub="Compressed from the A2 study guide. Read the guide first; this is for the last pass."),
    }[kind]
    md = (HERE / cfg["src"]).read_text()
    html_sections, toc = [], []
    for i, (title, body) in enumerate(sections(md)):
        m = re.match(r"(\d+)\.\s*(.*)", title)
        num, name = (m.group(1), m.group(2)) if m else (str(i), title)
        sid = f"s{i}"
        toc.append(f'<li><a href="#{sid}"><span class="tn">{int(num):02d}</span>{name}</a></li>')
        html_sections.append(
            f'<section id="{sid}"><div class="sec-head"><span class="sec-num">{int(num):02d}</span>'
            f'<h2>{name}</h2></div>{md_to_html(body)}</section>')
    toc_html = ('<nav class="toc"><div class="toc-title">Contents</div><ol>' + "".join(toc) + "</ol></nav>") if kind in ("guide", "simple") else ""
    page = f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><title>{cfg['title']}</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Oswald:wght@500;600;700&family=IBM+Plex+Sans:ital,wght@0,400;0,500;0,600;1,400&family=IBM+Plex+Mono:wght@500;600&display=swap">
<style>{CSS}</style></head><body><div class="wrap">
<div class="masthead"><div class="eyebrow">GM ASEP <span class="sep">/</span> ASE A2 <span class="sep">/</span> VERSION {cfg['ver']}</div>
<h1>{cfg['h1']}</h1><p class="sub">{cfg['sub']}</p>
<div class="meta-row"><span><b>Prepared</b> October 14, 2026</span><span><b>Exam</b> October 15, 2026</span>
<span><b>Scope</b> ASE A2, official 2026 task list (45 scored questions)</span></div></div>
{toc_html}{''.join(html_sections)}
<footer><span>{cfg['title']} &middot; v{cfg['ver']} &middot; 2026-10-14</span><span>Private study material. Not ASE content.</span></footer>
</div></body></html>"""
    out = HERE / f"{cfg['out']}.html"
    out.write_text(page)
    pdf = HERE / f"{cfg['out']}.pdf"
    subprocess.run([CHROME, "--headless", "--no-sandbox", f"--print-to-pdf={pdf}",
                    "--no-pdf-header-footer", f"file://{out}"], check=True,
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print("wrote", out.name, pdf.name)


def assemble(scratch):
    parts = []
    for name in ["sec0_front", "sec1_foundations", "sec2_mech_hydraulic", "sec3_electronic",
                 "sec45_area_b_c", "sec67_types_strategy"]:
        p = Path(scratch) / f"{name}.md"
        parts.append(p.read_text().strip() + "\n")
    (HERE / "ase_a2_study_guide_v2.md").write_text("\n".join(parts))


if __name__ == "__main__":
    if sys.argv[1] == "assemble":
        assemble(sys.argv[2])
    else:
        build(sys.argv[1])
