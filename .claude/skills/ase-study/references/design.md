# Intent and design

Established: 2026-09-16. These are workflow choices, not claims of measured learning effectiveness.

## The opportunity

A concentrated automotive course brings textbook explanations and hands-on shop examples close together. Preparing for the corresponding ASE exam while those connections are fresh can give the study process concrete material to work with. This framework preserves those connections and turns accumulated files into deliberate preparation.

It grew from a GM ASEP manual-drivetrain study project. The instructor's textbook coverage, GM lab applications, manufacturer-independent ASE scope, and outside research served different purposes. The design makes those purposes explicit so an assistant can combine the material without flattening those distinctions.

The learner supplies course material and practical experience. Assistants can organize explanations, locate research gaps, verify sources, build worked examples, and review each other's output. Either Claude or Codex can perform the full process; the approach also works manually or with another capable assistant. A particular model is not an authority on automotive facts.

## Two outputs from one body of material

The workflow supports three starting conditions: personal notes with targeted outside research, public teaching material when personal notes are unavailable, or a hybrid of both. Public student notes can reveal useful explanations, terminology, and common confusion; verify their important claims and identify whose course they describe. A web-first guide can follow ASE scope while the local instructor's final-exam scope remains unknown.

| Output | Determines scope | What outside research contributes |
|---|---|---|
| Class-final guide | Instructor emphasis, supplied textbook content, notes, labs, review sheets | Resolves uncertainty and clarifies mechanisms without silently expanding the assessed syllabus. |
| ASE guide | Current official task list, published category weights, entire relevant course folder, verified supporting sources | Fills coverage gaps and tests whether principles transfer to other identified designs. |

The final guide is a synthesis, not a concatenation. Remove repetition, reconcile terminology, retain useful shop examples, identify conflicts, and connect causes to confirming evidence. A cram sheet should compress an explanation already developed elsewhere rather than introduce an unsupported mnemonic.

## Layer depth for the reader

A research record and a study guide have different jobs. Research should retain exact source language, design differences, application limits and unresolved questions. The study guide should lead with the broad distinction the learner needs to recognize quickly, then add exact sequences only when the class or exam stem identifies that mechanism.

Use this order:

1. broad family or operating principle;
2. condition that changes the answer;
3. named design example when relevant;
4. confirming measurement or observation;
5. source boundary in the research record.

This keeps exam preparation accessible without laundering a simplification into a universal service rule.

## State matters

“Not ready” can mean different things. Distinguish them using the conversation and course context:

| State | Appropriate work |
|---|---|
| Designing a future workflow | Document the method, source strategy, and reusable scaffold. Keep future course work inactive. |
| Gathering notes and research | Process available material and research authorized questions; preserve incomplete notes. |
| Reviewing a lesson or unit | Build/update the relevant guide, rehearse mechanisms, and record observed confusion. |
| Final synthesis requested | Read the full relevant corpus and assemble the requested output with explicit coverage and sources. |

Do not ask the learner to reapprove established choices at each step. Ask only when missing information changes the substance of the work. A request for a partial guide can be fulfilled before the course ends; label the scope actually covered.

## Learner-specific decisions stay local

Keep experience, exam history, strong subjects, available prep books, exam dates, funding arrangements, instructor requirements, and named lab assemblies in the course context. Do not bake one learner's electrical competence, manufacturer preference, four-week schedule, or certification sequence into this public skill.

Existing competence should reduce repetitive fundamentals. It should not erase subject-specific applications that have not yet been assessed. A thin document is evidence about the document, not a diagnosis of the learner.

## Small, durable structure

| File or folder | Responsibility |
|---|---|
| `CONTEXT.md` | Purpose, actual dates, learner preferences, current state, and next action. |
| `WORKFLOW.md` | Reusable process; adjust locally where the course needs it. |
| `research.md` | Coverage, open questions, verified findings, source locations, and consequential practice errors. |
| Raw notes | Unedited source material, wherever the learner already keeps it. |
| `study/` | Guides, cram sheets, requested practice and final outputs. |
| `sources/` | Original reference documents and a record of what was actually inspected. |
| `AGENTS.md`, `CLAUDE.md` | Short entry pointers, with shared detail in the documents above. |

For existing folders, map these roles onto existing files. Keep a combined research file rather than creating an overlapping report for each session. Dated handoffs preserve the work across assistants and interruptions.

When a learner will keep several printed or downloaded copies, mark the cover with a simple version and absolute date. Keep the same filename for the current copy unless archival filenames are requested. Put a version on detachable sheets as well.

## Evidence of quality

More documents, questions or citations do not prove readiness. Look for explanations the learner can reconstruct, an unfamiliar diagram they can interpret, and a justified next test that separates plausible faults. Preserve meaningful misses and their corrected reasoning. A repeated question can help learning but is not an independent measure of improvement. If suitable owned question banks already exist, another assistant-written bank usually adds less value than a clearer guide.

This initial repository supplies workflow instructions and templates. Selected learner-authored notes and original guides may be added with authorization and a review of their source material and identifying details. It currently contains no complete curriculum, official practice question bank, individual student's records, or validated pass-rate claims. Official ASE materials and publishers retain their own rights; the framework links to them rather than redistributing commercial books or secure questions.
