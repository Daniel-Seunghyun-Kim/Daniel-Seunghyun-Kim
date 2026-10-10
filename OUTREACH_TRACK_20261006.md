# Outreach track starting 2026-10-06

Purpose: secure real analysis access for AlN/Si thermal transport work. This is separate from the Connect AI / JEV automation track.

## Work split

From Tuesday 2026-10-06:

| Track | Time share | Goal | Output |
|---|---:|---|---|
| Analysis-equipment outreach | 70-80% | Convert candidate list into real measurement routes | Contact DB, sent inquiries, reply tracker, cost/condition comparison, reservation path |
| Connect AI / JEV build | 20-30% | Automate repeatable parts of the outreach workflow | Human-approved draft generator, entity classifier, reply triage, DB updater |

Do not build automatic email sending first. Use human-in-the-loop: AI drafts and classifies, the user approves every outgoing message.

## Physical quantities, not equipment names

Track each inquiry by the physical quantity required:

| Need | Methods to ask about | Must ask |
|---|---|---|
| AlN thin-film cross-plane thermal conductivity | TDTR, FDTR, 3omega | Minimum identifiable thickness, required transducer/heater, roughness/specimen size, uncertainty budget |
| AlN/Si interface TBC/TBR | TDTR/FDTR with sensitivity analysis; thickness series; possibly 3omega differential analysis | Can they separate film kappa and interface G for top-Al/AlN/Si without buried metal? |
| Heater-line measurement on insulating film | 3omega | Can they fabricate/calibrate Al-only or recommended heater metal? What line width and TCR calibration are required? |
| Structural support evidence | TEM/STEM-EDS/EELS, FE-SEM/FIB, AFM, XRD/GIXRD, XPS/SIMS | Columnar morphology, oxygen/impurity, roughness, interlayer/native oxide, film thickness |

## Tuesday minimum action list

1. Freeze sample description in one sheet: Si(100), AlN thickness range, deposition history, surface roughness if known, allowed top metal, allowed dicing/chip size, maximum thermal budget.
2. Send first inquiry batch to the high-priority group only: SNU Kim Taeyong, SNU Jang Hyejin, IBS CINAP, SKKU Jungwan Cho, KAIST Bong Jae Lee, KAIST Joonsang Kang, CNU Yun Young Kim, GIST Jong Seok Lee, GIST Jae Hun Seol.
3. Ask for technical feasibility first, not a quote first: target quantity, stack sensitivity, required transducer/heater, sample prep, raw-data/model deliverables.
4. Record every reply into `outreach_tracker.csv` with status: NOT_CONTACTED / SENT / REPLIED / NEEDS_SAMPLE_INFO / QUOTE_REQUESTED / BOOKABLE / NOT_AVAILABLE / COLLAB_ONLY.
5. Use the Exa expansion file as a second-wave source only after first-wave replies clarify what method is actually needed.

## Candidate status policy

- `Priority A`: current visible equipment page, reservation page, or current lab activity directly tied to TDTR/FDTR/3omega thin-film thermal transport.
- `Priority B`: peer-reviewed or repository evidence of domestic prior use, but current apparatus or external intake not confirmed.
- `Hold`: method-adjacent or old historical evidence only.
- `Exclude`: Ajou University for this outreach cycle, per user instruction.

## Connect AI / JEV role

The first useful automation is not research reasoning. It is operational memory:

1. institution/entity extraction from search results;
2. method classification: TDTR / FDTR / 3omega / adjacent only;
3. evidence level classification;
4. inquiry draft generation with the user's sample facts;
5. duplicate-contact detection;
6. reply classification and next-action suggestion;
7. daily unresolved-list generation.

Human approval remains required before any message is sent.

## Daily check prompt

`JEV. 분석장비 outreach 트랙. 기존 DB/회신 기준. 오늘 연락할 대상과 후속조치만. 아주대 제외. 물리량 기준으로 정리.`

