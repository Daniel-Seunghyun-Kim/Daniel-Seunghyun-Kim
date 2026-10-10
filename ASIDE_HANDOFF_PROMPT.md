# Aside Portable Handoff Prompt (paste into a fresh Aside session on any computer)

Copy everything below this line into the first message of a new Aside session to resume this
research program without re-deriving prior work.

---

## Context

I am continuing an existing AlN thin-film / HBM hybrid-bonding research program. Do NOT restart
research from scratch. Read the attached/synced folder `research_working_set/` first, in this
order:

1. `reports/FINAL_TRANSFER_README.md` - what is decided vs not decided.
2. `algorithm_v0.10_claude_final/AlN_HybridBonding_Algorithm_v0.10/00_core/ALGORITHM_FINAL.md` - the frozen S0-S5 algorithm.
3. `algorithm_v0.10_claude_final/AlN_HybridBonding_Algorithm_v0.10/00_core/HANDOFF.md` - the 8 open inputs blocking further steps.
4. `algorithm_v0.10_claude_final/AlN_HybridBonding_Algorithm_v0.10/00_core/PREREG.md` (v0.10) - the single source of truth for all
   kill/go thresholds. Never silently change a frozen threshold; use PREREG's Change Log.
5. `reports/MASTER_Algorithm_v1.md` + `_v1_1_Claude_Update.md` - the multi-model design process
   (context only, not authoritative for values).

## Standing operating rules for this program

- Economy policy: reuse grounded results, avoid duplicate searches, prefer a fast/cheap model for
  extraction and a strong model for judgment. Do not spawn a subagent when a direct tool call or a
  single Claude chat message will do.
- Hallucination policy: AI chat output (ChatGPT/Claude/Gemini/Perplexity/Liner/NotebookLM) is never
  evidence by itself. Every publishable number must trace to a DOI/patent/official URL or a raw
  measured/computed file with provenance (see `automation/src/common/provenance.py` and
  `algorithm_v0.10_claude_final/AlN_HybridBonding_Algorithm_v0.10/S5_manuscript_pipeline/s5_tools.py`).
- Model roles established so far: Gemini Web = open-world kill-search; NotebookLM = closed-corpus
  evidence ledger; ChatGPT = orchestration/synthesis; Claude = red-team/reviewer AND, in the most
  recent phase, the primary quantitative-design partner (ran real Monte Carlo/FEM calculations,
  self-corrected 3 errors); Perplexity = fast current industry/patent landscape; Liner = paper-level
  verification with direct full-text cross-checks; Meta AI = excluded from core workflow.
- Token/usage economy: when possible, keep deep iterative design work in a single regular Claude
  web chat (not Claude Code/Cowork, which depends on a possibly-disconnected remote machine) to
  save tokens across models. Reconnect and resume with "이어서" if the chat disconnects; do not
  restart the whole design from zero.

## Current locked research direction (do not re-litigate without new evidence)

RF-sputtered AlN(0002) is NOT a universal SiO2 replacement in Cu hybrid bonding. It is a
narrow-regime, layer-level-only thermal benefit that survives mainly in low-Cu-coverage,
thick-bonding-layer, high-power scenarios (see PREREG v0.10 S0/S0b results). Three core papers are
locked: #6 (interface TBR/bonding, narrative under review - see open decision 1), #8 (reliability
go/no-go, non-inferiority framing), #12 (HBM applicability regime map). A 4th track quarantined:
SAM/organosilane functionalization (dead-end for HBM bonding, basic-science only).

## What I need from you right now

State explicitly which of these you want:
(a) Resume the frozen PREREG v0.10 algorithm execution once real equipment/literature inputs are
    available (S0 through S5, in order, respecting kill/go gates).
(b) Broaden the paper-portfolio search for additional AlN-thin-film heat-dissipation opportunities
    beyond HBM hybrid bonding (see `reports/AlN_Additional_Paper_Opportunities.md` for the first
    pass: BSPDN nano-TSV AlN-vs-oxide dielectric, GaN/AlN/diamond topside heterostructure
    integration, AlN passivation in AlGaN/GaN HEMTs).
(c) Something else - state it plainly.

Do not silently assume; if ambiguous, ask.
