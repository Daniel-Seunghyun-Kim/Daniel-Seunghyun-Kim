# Publication Finalization Gates

This document establishes the mandatory quality and physical-validity gates required before any dataset in this project may be promoted to **`FINAL`**. 

**Policy**: No claim of completion is permitted while any gate is in `RUNNING`, `PARTIAL`, or `NOT_DEMONSTRATED` status. Promotion of `FINAL_PUBLICATION_DATASET.md` is strictly blocked until all relevant gates satisfy explicit passing criteria.

---

## 1. Finalization Gate Matrix

| Gate Identifier | Description | Current Status | Passing Criteria | Blocking Reason / Notes |
| :--- | :--- | :---: | :--- | :--- |
| **`GATE_A_144_SLAB_SCF`** | 144-atom AlN (0001) polar slab SCF convergence on Dual RTX 4090 GPUs. | **`RUNNING`** | `convergence has been achieved`, `JOB DONE.`, $\Delta E < 10^{-8}\ \text{Ry}$. | Task `task-683` is actively running Davidson diagonalization. |
| **`GATE_B_144_SLAB_ELECTROSTATICS`** | Planar-average potential $\bar{V}(z)$, macroscopic average, charge density $\bar{\rho}(z)$, and dipole correction verification. | **`NOT_DEMONSTRATED`** | 1. Sawtooth discontinuity located strictly in vacuum ($z = 0.95$, $z \in [0.80, 1.00]$); 2. Negligible electron density $\bar{\rho}(z) \approx 0$ at discontinuity; 3. Flat vacuum electrostatic potential away from the jump; 4. Residual internal slab field quantitatively extracted ($E_{\text{int}} = -\Delta\bar{V} / d_{\text{slab}}$) and interpreted physically (uncompensated polar slab vs compensated reference); 5. Extraction of `FINAL_CELL_DIPOLE` upon `JOB DONE.`. | Depends on `GATE_A_144_SLAB_SCF` completion. |
| **`GATE_C_FC3_CUTOFF_CONVERGENCE`** | Cutoff convergence of third-order anharmonic force constants within 72-atom supercell beyond 1st neighbor shell ($2.1167\ \text{Å}$). | **`NOT_DEMONSTRATED`** | Systematic comparison of $\kappa_{xx}, \kappa_{zz}$, lifetimes, and $\text{MFP}_{50,z}$ at cutoff $\ge 3.2\ \text{Å}$ (2nd shell) and $4.0\ \text{Å}$ (3rd shell) at fixed moderate $q$-mesh with $|\Delta \kappa / \kappa| < 3\text{--}5\%$. | Current dataset truncated at 4.0 bohr (1st shell). Prior norm-capture percentages retracted (`FC3_TRUE_MAGNITUDE_CAPTURE = UNKNOWN`). Dry-run displacement sets generated; 98 SCFs confirmed 100% reusable. |
| **`GATE_D_CROSS_PLANE_SUPPRESSION_MODEL`** | Physically valid cross-plane Boltzmann transport suppression function replacing ad-hoc Matthiessen formulas. | **`VERIFIED_FORMULATION`** | Adoption of documented anisotropic modal BTE cross-plane suppression approximation: $S_\lambda(L) = 1 / (1 + 2\Lambda_{z,\lambda}/L)$ (Vermeersch, Carrete, Mingo, APL 108, 193104 (2016)) with rigorous limits ($S \to 1$ as $\text{Kn}_z \to 0$, $S \to L/(2\Lambda_z)$ as $\text{Kn}_z \to \infty$) and decoupled series interface resistance $R_{\text{total}} = R_{\text{int, top}} + L/\kappa_{\text{film, eff}} + R_{\text{int, bottom}}$. | Faulty in-plane integral formula removed; Vermeersch et al. anisotropic modal model implemented and tabulated. |
| **`GATE_E_FC3_SUPERCELL_CONVERGENCE`** | Supercell size scaling for third-order anharmonic force constants ($4\times 4\times 3$ vs $3\times 3\times 2$). | **`NOT_DEMONSTRATED`** | Verification that real-space FC3 elements decay sufficiently within the supercell boundary. | Only one 72-atom supercell calculated for FC3 (`A7_fc3`). Subordinated to Gate C completion. |

---

## 2. Gate Verification Details

### Gate A: 144-Atom Polar Slab SCF
- **Platform**: WSL2 `Ubuntu-24.04`, Dual NVIDIA RTX 4090 (24 GB VRAM each).
- **Binary**: `/home/aol2/qe_gpu_builds/qe-7.2-dual4090-sm89/bin/pw.x`.
- **Status**: Currently at Iteration 2. `LATEST_ITERATIVE_CELL_DIPOLE = -1.3071 Debye`.
- **Action upon completion**: Confirm final energy and SCF accuracy, then proceed to Gate B.

### Gate B: Electrostatic Potential & Density Validation
- **Tools**: `pp.x` (plot_num = 11 for $V$, plot_num = 0 for $\rho$) and `average.x`.
- **Requirements**:
  1. Plot $\bar{V}(z)$ across the $c$-axis unit cell length ($67.17\ \text{bohr} \approx 35.54\ \text{Å}$).
  2. Prove that the potential jump at `emaxpos = 0.95` falls entirely within the vacuum region ($z \in [0.80, 1.00]$).
  3. Ensure electron density $\rho(z)$ is zero at the discontinuity.

### Gate C: FC3 Cutoff Convergence
- **Current State**: Truncated at $r_{\text{cut}} = 4.0\ \text{bohr} = 2.1167\ \text{Å}$ (captures 1st neighbor shell only, 67.0% of Frobenius norm).
- **Test Matrix Planned**:
  - Test 1: $r_{\text{cut}} = 2.1167\ \text{Å}$ (current baseline, 98 supercells, 0 h new).
  - Test 2: $r_{\text{cut}} = 3.20\ \text{Å}$ (captures 2nd neighbor shell at $3.095\ \text{Å}$, $81.4\%$ of $\|fc3\|$).
  - Test 3: $r_{\text{cut}} = 4.00\ \text{Å}$ (captures 1st, 2nd, 3rd shells, $86.2\%$ of $\|fc3\|$, 466 supercells, 368 new SCFs, $\sim 43\ \text{h}$ on Dual GPU).
- **Evaluation**: Compare on $15\times 15\times 8$ mesh before re-running 27x27x15.

### Gate D: Cross-Plane Suppression Model
- **Physical Criterion**: Steady-state cross-plane heat transfer across a film of thickness $L$ bounded by thermalizing reservoirs cannot be modeled by free specular reflecting surfaces.
- **Suppression Function**:
  $$\kappa_{zz}(L) = \sum_{\lambda} \kappa_{\lambda, zz} \cdot S(\text{Kn}_\lambda), \quad \text{Kn}_\lambda = \frac{\Lambda_z(\lambda)}{L}$$
  where $S(\text{Kn})$ is the documented 1D cross-plane BTE solution between thermalizing boundaries (e.g. Chen 2005 / Hua-Minnich 2014):
  $$S(\text{Kn}) = \frac{1}{1 + \alpha \cdot \text{Kn}} \quad \text{or} \quad S(\text{Kn}) = 1 - 3 \int_0^1 \mu(1-\mu^2)\left[1 - \exp\left(-\frac{1}{\text{Kn}\cdot\mu}\right)\right] d\mu$$
- **Interface Resistance**:
  $$R_{\text{total}} = R_{\text{interface, top}} + \frac{L}{\kappa_{\text{film, eff}}(L)} + R_{\text{interface, bottom}}$$

---

## 3. Publication Promotion Protocol

A dataset may only be promoted to `FINAL` when:
1. **Gate A** and **Gate B** pass (`PASS`).
2. **Gate D** is adopted with documented BTE suppression formulas.
3. If **Gate C** and **Gate E** are not run, the publication claim must explicitly state that thermal conductivity is:
   `QMESH_CONVERGED_FOR_CURRENT_TRUNCATED_FC3`
   and is not claimed as `FULLY_CONVERGED_INTRINSIC_KAPPA`.
