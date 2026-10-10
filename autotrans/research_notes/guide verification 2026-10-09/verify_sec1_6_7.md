# Verification: guide Sections 0, 1, 6, 7 (partial pass)

Run 2026-10-09 by one fork, scope cut short by the coordinator after about 14 sources. All excerpts are from pages read in full via WebFetch, or from the local ASE PDF (`mantrans/sources/ase/ASE_Automobile_Study_Guide_2026.pdf`, read with `pdftotext`). Wikipedia is used only for geometry and definitions (tier: encyclopedic). Quizlet-style sites were not used. **Not attempted in this pass** (still at their existing labels in the guide): 4L60-E low roller / overrun clutch / backward-sprag claims, reaction-clutch steels splined to case, CVT primary/secondary roles, Multitronic chain, DCT dry-clutch/fluid claims, hybrid row, and the traps in 7.7 that live in sibling sections (TFT, stall, stator, PDTC, EPC, milky ATF, pan drop).

Counts: CONFIRMED-FULL 9, CONFIRMED-INDIRECT 4, CORRECTED 2, UNVERIFIABLE 1, CONTRADICTED 0.

## Needs a change first

| ID | Guide location | Verdict | What to do |
|---|---|---|---|
| V9 | 1.1 compound sets table, Simpson row | CORRECTED (over-broad) | Wikipedia: Simpson "delivers three or four forward gears" and is "commonly employed in three- and four-speed automatic transmissions." Your class textbook says Simpson + a simple set gives 4–5. Replace "(3- to 5-speed)" with: `One sun, two carriers, two rings (3- and 4-speed; a Simpson plus a simple set gives 4–5 in your textbook)` |
| V8b | 1.1 compound sets table, LePelletier row | CORRECTED (wording) | Wikipedia lists "5 shifting elements (brakes and clutches combined)" and no bands. Your class textbook says "five multiplate clutches," which is also how it is taught. Replace "five clutches, no bands" with: `five shift elements (multiplate clutches/brakes), no bands` |
| V15 | 7.6 table, row 1, "Why it is a risk" | UNVERIFIABLE (soften) | "The one A2-specific 'hardest area' source names it" has no source I could find. Replace with: `Apply-chart reading is the skill the public sample items lean on, and your Unit 1 quiz misses were here.` |

## Verified

| ID | Guide location | Claim | Verdict | Source (accessed 2026-10-09) | Excerpt (≤25 words) | Tier |
|---|---|---|---|---|---|---|
| V1 | 0 Exam map; 7.1 | A2 = 55 total, 45 scored, 75 min; 10 unscored research questions not identified | CONFIRMED-FULL | Local ASE 2026 guide, p. 4 | "55 total/45 scored* 75 mins" … "you don't know which questions those are, you need to answer every question." | Official |
| V2 | 0 Exam map | Area weights A 26 / B 12 / C 7 = 45; 28 / 12 / 23 tasks | CONFIRMED-FULL | Local ASE 2026 guide, pp. 10–12 | "A. … 26 58% B. … 12 27% C. … 7 15% Total 45" | Official |
| V3 | 7.1 | Tech A/Tech B and EXCEPT formats; "Both" and "Neither" are answer options | CONFIRMED-FULL | Local ASE 2026 guide, pp. 12, 20 (sample questions; no item content reproduced) | "(C) Both A and B (D) Neither A nor B"; "This question contains the word EXCEPT." | Official |
| V4 | 7.1 | Each question has four options, one correct | CONFIRMED-FULL | https://ase.com/what-to-expect/ | "Every question has one single right answer, three wrong answers, and enough information to choose the right answer." | Official |
| V5 | 7.5 | Answer every question; guessing is not penalized; blanks score wrong | CONFIRMED-INDIRECT | https://ase.com/what-to-expect/ (the FAQ page's "unanswered = incorrect" line is about the Renewal App, not used) | "Your score is based on the number of correct answers, so it is to your advantage to answer every question." | Official |
| V6 | 7.5 | Flag a hard question, move on, review flagged items if time remains | CONFIRMED-FULL | https://ase.com/what-to-expect/ | "flag the question using the on-screen button, then go on" … "you may have time to go back to those flagged questions." | Official |
| V7 | 1.1 Ravigneaux | Two suns, two planet sets, one carrier, one ring | CONFIRMED-FULL | https://en.wikipedia.org/wiki/Ravigneaux_planetary_gearset | "two sun gears … and a single planet carrier, holding two sets of planet gears" plus a ring gear | Encyclopedic |
| V8a | 1.1 LePelletier | Simple planetary + Ravigneaux; used in GM 6L80, Ford 6R80, ZF 6HP; no bands | CONFIRMED-FULL | https://en.wikipedia.org/wiki/Lepelletier_gear_mechanism | "a combination of a planetary gearset and a compound Ravigneaux gearset"; lists ZF 6HP, Ford 6R, GM 6L | Encyclopedic |
| V10 | 1.1 identification | Ring gear = outer gear with internal teeth; carrier fixed + sun input = reverse reduction; ring fixed + sun input = reduction | CONFIRMED-FULL (geometry and formulas); the alias "internal gear" for the ring is CONFIRMED-INDIRECT, from your textbook notes | https://en.wikipedia.org/wiki/Epicyclic_gearing | "An outer ring with inward-facing teeth"; "Carrier fixed, sun input: ratio = −Nr/Ns" | Encyclopedic |
| V11 | 1.1 sample ratios | Sun 30 / ring 70: 3.33:1, 1.43:1, 2.33:1 reverse | CONFIRMED-INDIRECT | Derived from the V10 formulas (100/30, 100/70, 70/30) | n/a | Derived |
| V12 | 1.3, 7.7 #7 | Allison 1000 reverse = C3 + C5; C2 is not applied | CONFIRMED-FULL | Weber State ASEP chart, https://www.weber.edu/wsuimages/automotive/asep/allison%201000%20clutch%20application%20chart.pdf (PDF text extracted locally) | "Reverse  C5  C3 … 4.49"; C2 is "4-5-6* Clutch" | OEM-derived training chart |
| V13 | 1.3 | Apply-chart method: find the element common to failed ranges, clear those applied in working ranges | CONFIRMED-INDIRECT | https://www.freeasestudyguides.com/transmission-clutch-band-chart.html | "a process of elimination, find the faulty component using this handy tool" | Textbook-faithful |
| V14 | 7.5 | About 80 s per item | CONFIRMED-INDIRECT | Arithmetic: 75 × 60 ÷ 55 = 82 s | n/a | Derived |
