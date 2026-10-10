# [Data Protection Report] AlN PhD Research Data Inventory & Provenance Safeguards
**Inspection Date**: 2026-09-18 18:28 KST  
**Classification**: READ_ONLY (Zero modification to source research files)  
**Target Node**: PC2 (Dual RTX 4090 + Core i9-13900K)  

---

## 1. Executive Summary

This report establishes the **immutable baseline inventory** of all existing AlN research calculations, raw outputs, force constants, structural coordinates, and validated publication datasets on PC2. 

**Mandatory Protection Directives**:
1. All files listed herein are designated as **IMMUTABLE INPUTS**.
2. **Zero In-Place Normalization**: No active or historical input/output file will be modified, renamed, or formatted in-place.
3. **Quarantine Isolation**: Any post-processing, derived parsing, or benchmark copying must be directed to a separate, isolated workspace.

---

## 2. Comprehensive Research Data Inventory

### 2.1 Polar Slab Structures & Relaxation Calculations
| Dataset / File Description | Exact Verified Path | Size | State / Provenance |
| :--- | :--- | :--- | :--- |
| **144-atom AlN(0001) Active Run** | WSL2 Ubuntu-24.04: `/home/aol2/campaign_144at_gpu/pw.out` | ~760 KB (growing) | **ACTIVE RUNNING**: Step 4/Cycle 5, accuracy $6.0\times 10^{-8}\ \mathrm{Ry}$, dipole $-10.54\ \mathrm{Debye}$ |
| **144-atom Slab Input Deck** | WSL2 Ubuntu-24.04: `/home/aol2/campaign_144at_gpu/pw.in` | ~11 KB | 144 atoms, 16 layers, `dipfield=.TRUE.`, `tefield=.TRUE.` |
| **144-atom Iterations 1-25 Log** | WSL2 Ubuntu-24.04: `/home/aol2/campaign_144at_gpu/pw.out.iter1_25` | ~450 KB | Historical checkpoint logs from initial SCF cycles |
| **144-atom Wavefunctions** | WSL2 Ubuntu-24.04: `/home/aol2/campaign_144at_gpu/AlN_144at_slab.wfc*` | ~3.8 GB | Binary GPU wavefunction checkpoints |
| **144-atom Reference CIF** | Windows: `c:\Users\AOL\Desktop\SH.Kim\aln_144at_slab.cif` | 8,291 B | Space group P1, $a=b=9.398\ \mathrm{\AA}, c=39.494\ \mathrm{\AA}$ |
| **144-atom Reference VASP POSCAR** | Windows: `c:\Users\AOL\Desktop\SH.Kim\aln_144at_slab.vasp` | 8,784 B | Fractional coordinate format for VESTA inspection |
| **64-atom Slab Reference CIF** | Windows: `c:\Users\AOL\Desktop\SH.Kim\aln_0001_slab_64atom.cif` | 6,324 B | Historical benchmark slab (audit backup preserved) |
| **72-atom Al(111) Substrate CIF** | Windows: `PC2_Nitridation_Campaign_Package\03_AL111_72ATOMS_SLAB\Al111_3x3_L8_72atoms.cif` | 5,553 B | 8-layer Al metallic substrate slab |
| **AlN/Si(100) Interface Deck** | `AlN_Simulation\structures\interfaces\IF_ALN0001_SI100_001` | ~12 KB | Heteroepitaxial interface geometry |

### 2.2 Anharmonic 3-Phonon Suite (Phono3py FC3 Campaign)
- **Root Directory**: WSL2 Ubuntu-22.04: `/home/aol/campaign_fc3_320ang/`
- **Metadata & Manifests**:
  - `phono3py_disp.yaml`: 126,886 B (Phono3py displacement dictionary, 220 displacement pairs)
  - `DISPLACEMENT_FORCE_MANIFEST.csv`: 83,511 B (Full force mapping ledger)
  - `EXPECTED_FORCE_ORDER.txt`: 1,908 B (Atom order indexing verification)
  - `batch.log`: Real-time execution log (Records exact launch and completion timestamps)
- **Job Directories**:
  - 220 dedicated directories: `jobs/supercell-00013/` to `jobs/supercell-00516/`
  - Current completion: **95 / 220 supercells completed (43.2%)**
  - Per-job structure: `pw.in` (5,311 B), `pw.out` (~40–47 KB per converged job)

### 2.3 Validated Harmonic FC2, Dielectric & NAC Physics
- **Location**: `c:\Users\AOL\Desktop\SH.Kim\verification_exa_20260907\tables\`
- **Born Effective Charges & High-Frequency Dielectric**:
  - File: `born_and_dielectric.json`
  - $Z^*_{\text{Al}} = +2.53 \sim 2.68$, $Z^*_{\text{N}} = -2.53 \sim -2.68$, $\epsilon_\infty = 4.48 \sim 4.70$
  - **NAC Factor**: Strictly verified as **`14.3996517259`** $\mathrm{eV/\AA^2}$ (Rejecting arbitrary 2.0).
- **Phonon Dispersion & Frequencies**:
  - `phonon_frequencies_gamma.csv`: Exact $\Gamma$-point optical/acoustic frequencies
  - Acoustic-optical frequency overlap: **7.04 THz** (Acoustic max 12.21 THz, Optical min 5.17 THz; disproving phantom 15.2 THz bandgap)
- **Genuine Vibrational DOS**:
  - `phonon_total_dos.csv`: $24\times 24\times 16$ mesh FC2 integrated 상태밀도 (19.3 THz optical peak verified)
- **Q-Mesh Convergence Suite**:
  - `qmesh_convergence.csv`: Convergence from $9\times 9\times 5$ to $27\times 27\times 15$ ($\kappa_{xx}=250.4, \kappa_{zz}=228.3\ \mathrm{W/mK}$)

### 2.4 Scientific Audits & Banned Literature Ledger
- **Retracted Literature Quarantine**:
  - **Bogner et al. (Surf. Coat. Tech. 2017)**: Formally retracted. Prohibited from being used as calibration or reference baseline.
- **Formal Audit Reports**:
  - `AlN_Simulation\docs\SCIENTIFIC_AUDIT_20260909.md`: Comprehensive audit of energy units, NAC factor, and memory envelopes.
  - `AlN_Simulation\docs\ALN_LITERATURE_AUDIT_20260909.md`: Audit of Perez 2023 experimental BTE vs Bogner.
  - `verification_exa_20260907\VALIDATION_REPORT.md` & `CLAIM_LEDGER.md`: 1:1 ledger of physics claims.

---

## 3. Active Process Protection Safeguards

1. **WSL2 Ubuntu-24.04 Dual GPU Job (PID 208189, 208190)**:
   - Command: `pw.x -nk 2 -in pw.in`
   - Protection Rule: **NEVER kill, suspend, or signal SIGTERM/SIGKILL**. The job has accumulated >155,000 CPU-seconds. It must run to natural BFGS termination.
2. **WSL2 Ubuntu-22.04 CPU Batch Loop (PID 652, 5975)**:
   - Command: `run_cpu_batch.sh`
   - Protection Rule: **NEVER terminate `batch.log` or interrupt active `pw.x`**. It sequentially processes the remaining 126 supercells without human intervention.

---

## 4. Derived Workspace Isolation Strategy

All new operational tools, scheduler state files, benchmarking copies, and provenance trackers must reside exclusively inside a dedicated directory:
$$\text{Workspace: } \mathbf{C:\backslash Users\backslash AOL\backslash Desktop\backslash SH.Kim\backslash PC2\_RESEARCH\_NODE\backslash}$$
Raw data in `/home/aol/`, `/home/aol2/`, `master_simulation_archive/`, and `verification_exa_20260907/` remain read-only references.
