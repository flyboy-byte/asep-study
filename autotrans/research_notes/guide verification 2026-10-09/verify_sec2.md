# Verification: Section 2 (mechanical and hydraulic diagnosis)

Access date for every URL: **2026-10-09**. Scope was cut short on request: 15 claims were checked, the rest of Section 2 was **not verified** (listed at the bottom). Fetches went through WebFetch, which summarizes the page, so excerpts are the tool's quoted text from the page, not a hand copy. Where the tool's first answer disagreed with a re-ask of the same page, only the re-ask counts and the conflict is noted. Flashcard and aggregator sites were not used as evidence.

Evidence tiers: **T1** OEM service text or a textbook instructor guide. **T2** rebuilder/industry technical page (Sonnax, aa1car, MOTOR). **T3** study-guide site that follows textbook wording. **T4** unattributed study site (context only).

## Needs action first

| ID | Guide location | Claim | Verdict | Source | Excerpt (<=25 words) | Tier |
|---|---|---|---|---|---|---|
| V1 | 2.6 stator table, "Stall test" row; also 7.7 trap 3, quick reference, cram sheet | A **seized stator gives a normal stall reading** | **UNVERIFIABLE** (keep as reasoning, soften) | [aa1car](https://www.aa1car.com/library/torque_converters.htm) | Re-asked directly: "does not specify whether stall speed would be high, normal, or low" for a seized stator. | T2 |
| V1b | same | Contrary claim: seized stator = high stall | **UNVERIFIABLE** (do not use) | [open-exam-prep A2 guide](https://open-exam-prep.com/study-guides/ase-a2/planetary-gears-mechanical/torque-converter-diagnosis) | "extreme fluid turbulence and drag during the coupling phase," resulting in unusually high stall speeds. | T4 |
| V13 | 2.4 "Reverse pressure runs higher" | Reason: reverse holding members carry the highest reaction torque | **UNVERIFIABLE** (soften) | search results only (patents US 6619323, US 6776736); [industrialmonitordirect](https://industrialmonitordirect.com/blogs/knowledgebase/reverse-line-pressure-in-automatic-transmissions-why-its-higher) not fetched | Snippet: reverse input pressure on the boost valve "increases the operating range of line pressure" in reverse. | search snippet only |

**V1 detail.** No page I could read states what stall rpm does with a *seized* stator. aa1car's first fetch answer said "abnormally high stall," but that was the summarizer's inference. The re-ask returned "No such statement." The only source that says "high" is a T4 study site with no attribution. Mechanically, a stator is held at stall anyway, so "normal" is the reasoned answer, but it is not documented. A search-result summary also said a seized stator makes the engine stall when shifted into gear; it had no checkable source, so it is not used. Symptoms (good launch, poor top speed, overheating) are CONFIRMED (V2).

Ready-to-paste replacement for the table row in 2.6:

```markdown
| Stall test | **Low** | **Not a reliable indicator.** A good stator is held at stall anyway, so expect little change (reasoned; no textbook page states it). Diagnose a seized stator from the symptoms and heat |
```

And in the `*ASE expects:*` line under that table, replace "...poor top speed, overheating, normal stall, is a **seized** stator" with "...poor top speed, overheating, is a **seized** stator". In 7.7 trap 3, the cram sheet (section 2 "Stall" bullet) and the Section 2 quick reference, drop "normal stall" the same way, or write "stall test not diagnostic".

Ready-to-paste for V13 (2.4):

```markdown
**Reverse pressure runs higher.** Reverse oil acts on the pressure regulator/boost valve and raises line pressure (documented in boost-valve patents). The usual explanation is that the reverse holding members carry the highest reaction torque (INFERRED, low-authority source). Low pressure in R only = a reverse-circuit leak or boost-valve fault. Low everywhere = supply.
```

## Confirmed

| ID | Guide location | Claim | Verdict | Source | Excerpt (<=25 words) | Tier |
|---|---|---|---|---|---|---|
| V2 | 2.6 stator table | Freewheeling stator: poor launch, normal at speed. Seized stator: good launch, poor high speed, overheating | CONFIRMED-FULL | [freeasestudyguides](https://www.freeasestudyguides.com/diagnose-one-way-stator-clutch.html); [aa1car](https://www.aa1car.com/library/torque_converters.htm); [MOTOR 1999](https://www.motor.com/magazine-summary/torque-converter-lock-may-1999/) | "a sprag clutch seized on its one-way clutch... allows satisfactory early acceleration, but prevents normal cruise speed." | T2/T3 |
| V3 | 2.6 stall test | High stall = transmission clutch/band slipping. Low stall = stator OWC slipping (or exhaust restriction) | CONFIRMED-FULL | [freeasestudyguides](https://www.freeasestudyguides.com/torque-converter-stall-test.html); [aa1car](https://www.aa1car.com/library/torque_converters.htm) | "Above specifications: the transmission's clutches and bands are slipping." Below: "stator one-way clutch is slipping, or there is a restriction in the exhaust system." | T2/T3 |
| V4 | 2.6 "rule out the engine first" | Weak engine also gives low stall | CONFIRMED-INDIRECT | same freeasestudyguides page (names an exhaust restriction only; misfire is not on the page) | "or there is a restriction in the exhaust system" | T3 |
| V5 | 2.6 | Stall about one-third of spec points to the stator; 5-second limit; cool down after | CONFIRMED-FULL | [Halderman, Automotive Technology 6e ch. 133 instructor lecture plan (PDF, read with pdftotext)](https://jameshalderman.com/wp-content/uploads/2019/07/at6_lp_ch_133.pdf) | "when stall speed is about 1/3 of specification, it is an indicator that one-way (Stator) clutch in converter is bad." | T1 (textbook) |
| V6 | 2.4 "Order" | Fluid, then line pressure, then stall; do not stall-test if line pressure is low | CONFIRMED-FULL | [1996 Ford SI mirror](https://www.diesel-dave.com/vehic/manual/stj/stj71a21.htm) | "Perform line pressure test prior to performing stall speed test. If line pressure is low at stall, do not perform stall speed test." | T1 (OEM) |
| V7 | 2.6 | Stall limit about 5 seconds WOT | CONFIRMED-FULL | same Ford SI; [freeasestudyguides](https://www.freeasestudyguides.com/torque-converter-stall-test.html); Halderman | "DO NOT MAINTAIN WIDE-OPEN THROTTLE in any gear range FOR MORE THAN FIVE (5) SECONDS." | T1 |
| V8 | 2.2 table | Flare = an element releases before the oncoming one holds. Bind-up = tie-up = two ratios at once | CONFIRMED-FULL | [Sonnax terms A to Z](https://www.sonnax.com/tech_resources/175-transmission-terms-from-a-to-z) | Flare: "A holding/driving element has released before an engagement of the oncoming element holds properly." Bind-up: drives "at two different ratios at one time." | T2 |
| V9 | 2.2 table | Slide-bump: smooth start, harsh finish; cause is the accumulator bottoming | CONFIRMED-INDIRECT (feel yes, mechanism not on the page) | Sonnax A to Z; mechanism is in Logan's class notes | "Shift is soft, engagement is delayed or 'slides' in with a noticeably firm finish or 'bump' on the end." | T2 |
| V10 | 2.2 accumulators | Accumulator cushions the apply; it does not store backup pressure | CONFIRMED-FULL | [Sonnax Hydraulics Fundamentals II](https://www.sonnax.com/tech_resources/675-hydraulics-fundamentals-part-ii-accumulators-shift-feel) | "acting as a shock absorber for the fluid pressure that is applying a clutch, brake or band." | T2 |
| V11 | 2.4 EPC | Classic EPC: more current = lower pressure; no current/unplugged = maximum | CONFIRMED-FULL | [freeasestudyguides EPC](https://www.freeasestudyguides.com/transmission-electronic-pressure-control.html) | "As the module increases current to the solenoid's windings... opening the exhaust port and reducing line pressure." | T3 |
| V12 | 2.2, 2.5 | Faulty accumulator or broken spring = harsh shift | CONFIRMED-FULL | [freeasestudyguides](https://www.freeasestudyguides.com/transmission-shift-troubleshooting.html) | "When an accumulator is faulty or has a broken spring, harsh shifting will occur." | T3 |
| V14 | 2.4 pressure table | Low at idle = pump/regulator; one circuit low vs line = leak | CONFIRMED-INDIRECT (broader cause list in the guide is not on the page) | [freeasestudyguides pressure tests](https://www.freeasestudyguides.com/automatic-transmission-pressure-tests.html) | "If the line pressure is low at idle, the pump or pressure relief valve is most likely the problem." | T3 |
| V15 | 2.2 "first engagement after sitting = drain-back" | Drain-back leaves components filled with air | CONFIRMED-INDIRECT (concept only, not the delay symptom) | Sonnax A to Z | "increase the amount of drainback, leaving components filled with air rather than fluid." | T2 |

## Not verified (cut by the scope change)

Ruptured vacuum modulator signs; TV/modulator/governor principles; TCC stuck-on vs. not-holding and shudder vs. misfire; the no-dipstick level procedure and the low/overfull table; milky-ATF handling; valve roles table; failsafe behavior; the "not the transmission" table. Section 2 still rests on the 9/30 snippet-level research for these.

## Notes on sources

- The `jameshalderman.com` PDF is an instructor lecture plan for Halderman's *Automotive Technology* 6e, so it paraphrases the text rather than reproducing it. It is the closest thing to a textbook line found for the one-third rule.
- The aa1car fetch gave two different answers on the seized stator; only the direct re-ask ("No such statement") is counted.
