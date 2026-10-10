# Multi-Agent & Multi-Model Guidance

## 0. Role (verbatim from rules)
- Orchestrator / reviewer / curator / reproducibility manager. **Not** scientific owner.
- **Verify, do NOT accept/promise.** Do not auto-pass, auto-approve, or fabricate a PASS grade.
- Report from **real tool output** only. Log/hash/logs/decision-JSON/checkpoint over AI-hallucinated summaries.

## 1. Model responsibilities

| Model | Role | Constraint (transparency watermark) |
|-------|------|------|
| **Claude** | Research / idea generation. Search sources, propose hypotheses, judge plausibility. | For any PPT/report, Claude must be marked as **research source only** (transparent watermark: `research-source-only`). Claude provides search + ideas + judgment; it does NOT produce final numbers. |
| **ChatGPT (GPT-5 / MiniMax M1)** | Agent orchestration, multi-agent control flow, parallel task dispatch. |
| **Perplexity Pro** | Grounded web search with citations. Facts that must be cited (literature, parameters, prior art). |

## 2. Grounding & evidence-gating (hard gates)

1. **Evidence > summary.** Local logs / input-hash / decision-JSON / checkpoint over AI summaries.
2. **Missing data = `BLOCKED_missing_DATA`**, not an assumption. Do NOT guess missing boundary conditions (temperature/direction/convergence).
3. **Fabricated synthesis report hallmarks** (detect & exclude):
   - "88/100", "🟢 ACADEMIC VALIDATION COMPLETE 88%".
   - CSV where Predicted == Actual for every row (auto-pass).
   - Claim without citing the underlying log.
4. **First-principles only** — no AI-generated figures standing in for real computation.

## 3. Multi-computer readiness

### 1) Local Windows agent (host) — Hermes
- `DESKTOP-2VICUCU`, i9-13900F, ~31.8 GiB RAM, **RTX 4070 Ti**.
- CWD `D:/AlN` (700k+ entries).

### 2) WSL 2 backend (/home — QE compute node)
- QE `pw.x` (pwscf): `/home/nano/qe-7.4.../bin/pw.x` **NOT installed here** -> `BLOCKED_missing_SOLVER`.
- Real research corpus only at `D:/AlN/AlN_Simulation_Core`.

### 3) Windows ↔ WSL 2 bridges
- `/mnt/d/` (Windows D: -> /mnt/d)
- `/mnt/c/` (Windows C:/ -> /mnt/c)
- Cross-machine sync via `cp`/`scp` or Python os module (`os`, `shutil`).

## 4. Workflow (verbatim: "제안주는 모든 내용들에 대해 즉시 순차 작업")

1. **Proposal** → 2. **Evidence-gate** → 3. **Sequential execution** → 4. **Record outputs** → 5. **Report** (no PASS guarantee; verify from real output only).
