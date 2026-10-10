# AlN First-Principles Calculation — Physically Correct Design

## 0. Status
- **BLOCKED_missing_SOLVER** (real tool output grounds):
  - WSL 2: QE `pw.x` at `/home/nano/qe*.../bin/` **NOT installed in this instance** (`/home/nano` gone).
  - Windows: no QE install.
  - WSL→`/mnt/d/AlN` **403 FORBIDDEN** (WSL-side mount permission).
- Real corpus only: `D:/AlN/AlN_Simulation_Core` (verified `.in/.out`, `crystal_lattice_aln.png`, `phonon_dispersion_aln.png`).
- `Research_Topic_1/2/3` folders are AI-generated figures/text over valid topics, NOT verified calculations.

## 1. Model / agent & multi-computer readiness
- **Claude = research source only** (transparent watermark). Verify, don't auto-pass.
- Agents: Hermes on `DESKTOP-2VICUCU`, WSL 2 compute, `/mnt/d`/`/mnt/c` bridges.
- Grounding: local logs / decision-JSON over AI summaries. Missing data = `BLOCKED_missing_DATA`.

## 2. Physically-correct inputs (verified)
| Model system | Structure (wurtzite) | Lattice & atomic positions (a~5.88 Å, c/a 1.600, Al–N 1.91 Å) — physically correct |
|---|---|---|
| AlN bulk (AlN_bulk_test.in) | Wurtzite (`ibrav=4`, `celldm(1)=5.8789`, `celldm(3)=1.600`) | 4 atoms, Al-N bond 1.91 Å (real data). Physically valid. |

## 3. Calculation workflow (QE)
1. `pw.x` SCF/relax (`xc calc`, `calculation = 'scf'` / `'vc-relax'`): equilibrium E(a, c).
2. Phonon (`ph.x`, finite-displacement or DFPT `acph`): lattice-dynamical frequencies / Raman-active modes.
3. Lattice thermal conductivity (`BTE`, solution): k(T), ~300 W/mK single crystal.
4. (Validation) Compare k(a,b,c) with measured ~300 W/mK before submission.

## 4. Interface data (Cu / SiO2)
- **Cu** = heat spreader / interconnect **comparison** (Cu-AlN hybrid).
- **amorphous SiO2** = dielectric interface insulator / stress.

## 5. Next step (real computation)
- Install QE (`pw.x`, `ph.x`) for RTX 4070 Ti GPU acceleration, then re-run these inputs.
- Deliver a real lattice-dynamical frequency / Raman-active-mode result that matches measured single-crystal AlN thermal conductivity.
