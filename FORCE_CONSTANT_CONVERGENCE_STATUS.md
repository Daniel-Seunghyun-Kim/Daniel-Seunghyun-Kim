# Force Constant and Computational Convergence Status

This document establishes the independent convergence status of the force constant matrices, interaction cutoffs, and Brillouin-zone sampling grids for Wurtzite AlN calculations in this project. 

**Zero-Hallucination Policy**: No convergence property is assumed or inferred. Every classification is strictly grounded in verifiable raw calculations and files present in this workspace.

---

## 1. Executive Status Matrix

| Convergence Dimension | Classification | Basis & Scope | Workspace Evidence |
| :--- | :---: | :--- | :--- |
| **`QMESH_CONVERGENCE`** | **`VERIFIED`** | For *fixed* second- and third-order force constants (72-atom, 4.0 bohr cutoff), RTA thermal conductivity converges within 0.16% between 20x20x14 and 27x27x15 meshes. | 7 HDF5 files in `campaign/A7_fc3/` (`kappa-m11116.hdf5` to `kappa-m272715.hdf5`). |
| **`FC2_SUPERCELL_CONVERGENCE`** | **`PARTIAL`** | Verified consistency between DFPT zone-center frequencies and frozen-phonon 72-atom supercell (0.99 cm⁻¹ agreement). Two distinct 72-atom displacement sets (`A7_fc3` vs `A11_fc2_443`) agree within 0.2% on $\kappa_{xx}$ and 0.5% on $\kappa_{zz}$. However, larger supercells (e.g. 4x4x3 or 4x4x4) testing real-space force constant decay have not been computed. | `A11_fc2_443/FORCES_FC2`, `A8_on_A11_fc2/kappa-m272715.hdf5`, `A5_phonon/b_grid/ph/wz.fc`. |
| **`FC3_SUPERCELL_CONVERGENCE`** | **`NOT_DEMONSTRATED`** | Only a single $3\times 3\times 2$ (72-atom) supercell size has been evaluated for third-order anharmonic forces. No larger supercells exist in the workspace to test supercell size convergence of the anharmonic tensor. | `campaign/A7_fc3/FORCES_FC3` is the sole third-order force set. |
| **`FC3_CUTOFF_CONVERGENCE`** | **`NOT_DEMONSTRATED`** | The third-order pair cutoff was executed with `--cutoff-pair 4.0` in Quantum ESPRESSO atomic units (bohr), corresponding to $r_{\text{cut}} = 2.1167\ \text{Å}$ (nearest-neighbor shell at $1.904\ \text{Å}$). Tensor magnitude decomposition proves this captures 67.0% of cumulative $\sum \|fc3\|$. Second-shell expansion to $4.0\ \text{Å}$ (86.2% of $\|fc3\|$, 466 supercells) was costed and prepared (`prepare_a10_fc3.py`) but has NOT been executed. A prepared calculation is not convergence evidence. | `AlN_Simulation/docs/FC3_CUTOFF_UNIT_ERROR_20260906.md`, `prepare_a10_fc3.py`. |

---

## 2. Detailed Technical Evidence

### 2.1 Q-Mesh Convergence (for Fixed IFCs)
- **Label**: `QMESH_CONVERGED_FOR_FIXED_IFCS`
- **Condition**: Fixed harmonic ($3\times 3\times 2$, 72 atoms) and third-order anharmonic IFCs ($r_{\text{cut}} = 4.0\ \text{bohr}$).
- **Mesh progression at 300 K (PBE, RTA + isotope)** — values and irreducible grid-point
  counts read directly from the HDF5 files on 2026-09-21; they agree to every printed digit
  with the A8 stage-1 table in `payload/records/CAMPAIGN_RESUME.md` §9, which is the primary
  record for this campaign:

  | $q$-mesh | irreducible grid points | $\kappa_{xx}$ (W/mK) | $\kappa_{zz}$ (W/mK) | source dataset |
  | :--- | ---: | ---: | ---: | :--- |
  | $11\times 11\times 6$ | 64 | 230.110 | 209.366 | `kappa-m11116.hdf5` → `kappa` |
  | $15\times 15\times 8$ | 135 | 240.572 | 222.997 | `kappa-m15158.hdf5` → `kappa` |
  | $19\times 19\times 10$ | 240 | 250.827 | 224.175 | `kappa-m191910.hdf5` → `kappa` |
  | $20\times 20\times 11$ | 264 | 250.544 | 221.690 | `kappa-m202011.hdf5` → `kappa` |
  | $20\times 20\times 14$ | 352 | 250.233 | 227.943 | `kappa-m202014.hdf5` → **`kappa_RTA`** (see note) |
  | $23\times 23\times 12$ | 392 | 251.125 | 226.456 | `kappa-m232312.hdf5` → `kappa` |
  | $27\times 27\times 15$ | 600 | 250.398 | 228.314 | `kappa-m272715.hdf5` → `kappa` |

  > **Note on `kappa-m202014.hdf5`.** This file was overwritten by a later direct-solution
  > (LBTE) run at the same mesh and filename. Its top-level `kappa` dataset therefore holds
  > the **LBTE** result (277.727 / 236.688 W/mK), not RTA. The RTA value quoted in the table
  > above is the `kappa_RTA` dataset inside the same file. Reading `kappa` from this one file
  > and comparing it against `kappa` from the others silently mixes two different solvers.

- **The two components do not converge together.** $\kappa_{xx}$ is settled by
  $19\times 19\times 10$ (every denser mesh sits within $\pm 0.18\%$ of 250.6).
  $\kappa_{zz}$ is not monotone in total grid density: it sorts by the $c$-axis divisor $n_3$
  and by its parity. Taking only even $n_3$: 209.37 (6), 223.00 (8), 224.18 (10), 226.46 (12),
  227.94 (14) — monotone toward $\approx 228$. The odd $n_3 = 11$ point breaks the trend
  downward (221.69 where interpolation wants $\approx 225$) because the $A$, $L$ and $H$ points
  lie on the grid only when $n_3$ is even. **Keep $n_3$ even.** Quoting the raw sequence without
  this rule makes the convergence look erratic when it is not.

- **Convergence metric**: relative difference between $20\times 20\times 14$ and
  $27\times 27\times 15$ is $+0.07\%$ for $\kappa_{xx}$ and $+0.16\%$ for $\kappa_{zz}$
  (227.943 → 228.314). $23\times 23\times 12$ lands *further* out (0.81% on $\kappa_{zz}$)
  despite being denser in-plane, for the $n_3$ reason above. $27\times 27\times 15$ is the
  densest mesh executed, **not a proven limit** — the tolerance is measured against it, not
  against infinity.

### 2.2 FC2 Supercell Convergence
- **Classification**: `PARTIAL`
- **Evidence**:
  - Harmonic forces were derived from a $3\times 3\times 2$ supercell (72 atoms).
  - Cross-check against DFPT (`A5_phonon` $6\times 6\times 4$ q-grid) showed agreement within $0.99\ \text{cm}^{-1}$ at $\Gamma$.
  - Recalculation using the independent `A11_fc2_443` displacement set yielded $\kappa_{xx} = 249.85\ \text{W/mK}$ (-0.22%) and $\kappa_{zz} = 229.46\ \text{W/mK}$ (+0.50%).
  - **Limitation**: While internally consistent across 72-atom configurations, supercell size convergence (testing $4\times 4\times 3$ or larger to verify real-space force cutoff decay) was not computed.

### 2.3 FC3 Supercell Convergence
- **Classification**: `NOT_DEMONSTRATED`
- **Evidence**:
  - Only one supercell geometry ($3\times 3\times 2$, 72 atoms, 98 displacement runs) was evaluated for three-phonon interactions (`campaign/A7_fc3/FORCES_FC3`).
  - No comparison to a $4\times 4\times 3$ or larger cell exists in the workspace.

### 2.4 FC3 Cutoff Convergence
- **Classification**: `NOT_DEMONSTRATED`
- **Evidence**:
  - Raw calculation used `--cutoff-pair 4.0` with `--qe`, which passed the value in bohr: $r_{\text{cut}} = 4.0\ \text{bohr} = 2.1167\ \text{Å}$.
  - The nearest-neighbor shell is at $1.904\ \text{Å}$; the second neighbor shell sits at $3.095\ \text{Å}$.
  - Therefore, third-order forces are truncated past the first shell. Only one cutoff radius was executed.
  - Frobenius norm analysis of the force tensor indicates that this 1st-shell truncation captures 67.0% of the total anharmonic interaction magnitude.
  - Extending the cutoff to $4.0\ \text{Å}$ (incorporating 2nd and 3rd shells) requires 466 supercells (368 new runs, ~86 h wall time on 1 GPU, ~43 h on Dual RTX 4090) as designed in `prepare_a10_fc3.py`, but has NOT been executed.
  - A prepared calculation is not convergence evidence. FC3 cutoff convergence is therefore unverified.

---

## 3. Publication Designation Guidelines

To ensure scientific integrity:
1. All thermal conductivity results from the $27\times 27\times 15$ grid must be reported as:
   $$\mathbf{\kappa}_{\text{RTA}} = 250.40\ \text{W/(m}\cdot\text{K)}\ (\perp c),\quad 228.31\ \text{W/(m}\cdot\text{K)}\ (\| c)$$
   with the explicit qualification:
   `QMESH_CONVERGED_FOR_CURRENT_TRUNCATED_FC3 (72-atom, 1st-neighbor FC3 shell)`
2. The dataset must **NOT** be claimed as `FULLY_CONVERGED_INTRINSIC_KAPPA` without the completed $4.0\ \text{Å}$ FC3 cutoff and supercell scaling studies.
