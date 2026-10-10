# Verification of guide Sections 4-5 (Area B and Area C), 2026-10-09

Scope was cut short on request: 11 of the highest-risk claims were checked. **Everything not listed was not verified in this pass** (TR switch and cable logic, pan debris, ATF wicking, fretting corrosion, mounts, pan-drop percentage, friction soak, thrust-washer grease, lip-seal orientation, sealing rings, end-play and clearance methods, flexplate practice, OWC backward install, sprag/roller types). Those remain at the snippet-level evidence recorded in `research_notes/A2 open gap research/`.

**Method and limits.** WebFetch returns an answer drawn from the whole fetched page, not raw text; excerpts below are as returned. Two PDFs were read directly with `pdftotext`. Transmission Digest returned HTTP 403; Sonnax and Gears mirror the same articles. Tiers: FULL = page or PDF text read this session; SNIPPET = search-result summary only. Access date for all: 2026-10-09. No Quizlet or aggregator pages used as evidence.

## Needs a change first

| ID | Guide location | Claim | Verdict | Source | Excerpt (<=25 words) | Tier |
|---|---|---|---|---|---|---|
| V1 | 4.8 "Classic trap" (level check) | A hot check lets fluid run out and leaves the unit low once it cools | **CORRECTED** (incomplete, wrong emphasis) | [Gears, GM AF50 fluid level check](https://gearsmagazine.com/magazine/gms-af50-8-speed-transmission-fluid-level-and-condition-check/) | "if you don't check it at the right temperature, it'll create several problems." Overfilled "due to checking when too cold" aerates the fluid. | FULL |
| V2 | 5.4 Bands and drums | Replace a "scored, glazed, heat-discolored or damaged drum" | **UNVERIFIABLE** as a transmission criterion (only brake-drum sources list glazed/heat spots) | [Sonnax 4L80-E drum wear](https://www.sonnax.com/tech_resources/89-reverse-drum-wear-a-4l80-e-true-story); [freeasestudyguides, brake bands](https://www.freeasestudyguides.com/transmission-brake-band.html) | "grooved lining in the band typically leaves marks along the surface of the drum (like railroad tracks)." Worn band: "a gap forms between the band and the drum." | FULL |
| V3 | 4.4 Cooler breach | "Glycol breaks down the bonding and the friction-modifier additives (shudder, especially at TCC apply)" | **UNVERIFIABLE** from this source; soften | [Gears June 2014, Simple Tests for ATF Contamination (Acustrip PDF)](https://www.acustrip.com/res/pdf/CoolantContamination.pdf) | Says clutch material is hygroscopic and even a little coolant "can cause irreversible damage"; no bonding or TCC statement. | FULL |
| V4 | 4.4 Cooler breach | "With the engine running, ATF pressure in the cooler is higher, so ATF can go into the coolant" | **UNVERIFIABLE** this pass (only the opposite direction was confirmed) | same | Cooling system holds about "15-16 PSI" when hot and "can easily force coolant through even the smallest leak." | FULL |

### Ready-to-paste replacements

**V1 (Section 4.8 "Classic trap"):**

> **Classic trap:** checking outside the temperature window gives a wrong level either way. ATF expands as it warms, so a unit topped off while cold is **overfull** once hot (aeration, shudder, fluid out the vent), and a unit checked too hot can read false. Windows differ by unit (examples only: about 30-50 °C on a 6L80, 35-45 °C on an AF50). **Take the number from SI, the method from this page.**

**V2 (Section 5.4 Bands and drums):** replace the first sentence with:

> **Bands and drums:** inspect together. A worn band leaves a gap at the drum and the unit slips. On the drum, look for wear tracks from a grooved lining or a smooth worn area from a smooth lining. A drum worn undersized lets the band run out of travel and the range is lost, so replace the band **and** the drum. Reject limits and resurfacing are SI.

**V3/V4 (Section 4.4 first two bullets):** replace with:

> - **Cooler breach.** A leak in the radiator-tank cooler can let coolant into the ATF (the cooling system holds roughly 15-16 psi hot, which pushes coolant through even a tiny leak), and ATF can also reach the coolant. You may see milky pink fluid ("strawberry milkshake") in the ATF, the coolant, or both.
> - **Even a little coolant damages a transmission.** The clutch material absorbs water and glycol. Test for glycol with a strip before replacing parts.

## Confirmed

| ID | Guide location | Claim | Verdict | Source | Excerpt (<=25 words) | Tier |
|---|---|---|---|---|---|---|
| V5 | 4.4 Cooler flow | Flow-test warm; about a quart in 20 s on 5/16-in. lines; flusher is not the test; fin-type coolers get replaced | **CONFIRMED-FULL** | [Sonnax, Avoiding After-Overhaul Problems](https://www.sonnax.com/tech_resources/99-avoiding-after-overhaul-problems) | "The cooler flusher puts more pressure to the cooler than the transmission does, and many times a cooler will start to clog again" | FULL |
| V6 | 4.4 / 4.5 repair | Replace the radiator or cooler after coolant contamination; a fluid exchange only buys time | **CONFIRMED-FULL** (with nuance: the source says an exchange "may" extend life, no guarantee) | Gears June 2014 (V3 link) | Three choices: "Replace the radiator (or the cooler if the car uses an external one)." | FULL |
| V7 | 5.1 Converter seating | Seating is felt in stages (three clicks); measure from the bellhousing face and compare with the specification | **CONFIRMED-FULL** (OEM tech tip, VW; number is that unit's) | [VW Tech Tip 32-19-01TT (NHTSA mirror)](https://static.nhtsa.gov/odi/tsbs/2019/MC-10157344-9999.pdf) | "When reinstalling the torque converter, 3 clicks should be felt to ensure correct seating and pump engagement." | FULL (PDF text) |
| V8 | 4.5 Valve body | Torque in sequence, starting in the middle and spiraling out; mismatched separator plate or gasket sends pressure to the wrong circuit; check balls wear separator plates | **CONFIRMED-FULL** | [freeasestudyguides, Valve Body: Separator Plates](https://www.freeasestudyguides.com/valve-body-separator-plates.html); [Sonnax Replacing Valve Bodies Part II](https://www.sonnax.com/tech_resources/657-replacing-valve-bodies-dos-and-don-ts-part-ii) | "start in the middle and spiral outwards"; "Always use a torque wrench in sequence on all the valve body bolts to ensure they are equal." | FULL |
| V9 | 4.5 Accumulator | A broken accumulator spring gives harsh shifts | **CONFIRMED-FULL** | [freeasestudyguides, shift troubleshooting](https://www.freeasestudyguides.com/transmission-shift-troubleshooting.html) | "When an accumulator is faulty or has a broken spring, harsh shifting will occur." | FULL |
| V10 | 4.8 / 2.1 no-dipstick method | Scan-tool temperature window, vehicle level, engine running, open the level plug, a drip is correct | **CONFIRMED-FULL** (AF50 example; window numbers are unit-specific) | Gears AF50 (V1 link) | "The vehicle must be level, with the engine running and the shift lever in park." "see if the fluid dribbles out or not." | FULL |
| V11 | 1.2 / 4 shift terms | Flare = element released before the oncoming one holds; tie-up = bind-up = excessive overlap, can be a one-way element installed backward | **CONFIRMED-FULL** | [Sonnax, Transmission Terms A to Z](https://www.sonnax.com/tech_resources/175-transmission-terms-from-a-to-z) | "Can be caused by a one-way holding element installed backward or not allowed to freewheel." | FULL |

## Confirmed only indirectly (kept, not upgraded)

| ID | Guide location | Claim | Verdict | Source | Note | Tier |
|---|---|---|---|---|---|---|
| V12 | 4.2 Extension housing | Worn bushing wobbles the slip yoke and the seal leaks; check yoke play and pitting | **CONFIRMED-INDIRECT** | [freeasestudyguides, extension housing bushing](https://www.freeasestudyguides.com/automatic-transmission-extension-housing-bushing.html) | Full page: "Move the slip yoke up and down; there should be little play." "pitting causes premature wear and a leaking seal." The page links a worn bushing to driveshaft vibration; the bushing-to-seal-leak link appeared only in a search summary. | FULL / SNIPPET |
| V13 | 4.4 TBV | A thermal bypass valve stuck in bypass starves the cooler and overheats the unit | **CONFIRMED-INDIRECT** | Sonnax thermal-bypass kit pages (search results only) | Search summary: valve "stuck in recirculation mode, only allowing ATF to circulate in the transmission and not allowing flow through the cooler." Page not read in full. | SNIPPET |
| V14 | 5.1 Converter seating | Never use the bellhousing bolts to draw the unit on | **CONFIRMED-INDIRECT** | NHTSA GM/other bulletin results (search summary) | Summary: "DO NOT use the bolts to draw the bellhousing up to the engine." Not read in full; the VW tip (V7) covers the seating check. | SNIPPET |
| V15 | 5.4 Air test | Low, clean, dry air; thud is good, hiss is a leak | **CONFIRMED-INDIRECT** | [freeasestudyguides, pressure tests](https://www.freeasestudyguides.com/automatic-transmission-pressure-tests.html) | Page confirms "low pressure (20-50 psi)" and that "too much pressure can damage transmission seals." It does not mention thud or hiss; that comes from the earlier Chrysler SI mirror. | FULL / earlier |

## Failed or unusable fetches

- Transmission Digest article pages: HTTP 403 (used Sonnax and Gears mirrors instead).
- A search for Alto/Raybestos band and drum guidance returned only forum threads and an unrelated hood-banding PDF; no friction-maker criteria were found. The soak time and drum reject criteria remain STILL OPEN.
