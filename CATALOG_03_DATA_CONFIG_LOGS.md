# Obsidian Knowledge Vault: Data, Config, and Log Files Catalog

**Generated**: 2026-10-08 | **Platform**: PC2 Dual RTX 4090 Workstation
**Target Path**: `c:\Users\AOL\Desktop\SH.Kim`

---

## 1. Overview
This catalog documents all non-code structured data files (JSON, CSV, Quantum ESPRESSO decks, crystallographic POSCAR/CIF structures, checksums, and runtime logs) in the root directory.

| File Name | Format | Size | Description & Record Count |
| :--- | :---: | :---: | :--- |
| `[[BUNDLE.sha256]]` | `.sha256` | 0.1 KB | 1 lines / records |
| `[[GATE_A_ALL_396_CONTINUOUS_ITERATIONS.csv]]` | `.csv` | 18.6 KB | 397 lines / records |
| `[[GATE_A_ALL_396_CONTINUOUS_ITERATIONS.json]]` | `.json` | 71.9 KB | 3566 lines / records |
| `[[GATE_A_ALL_ITERATIONS.json]]` | `.json` | 47.7 KB | 2774 lines / records |
| `[[GATE_A_VERIFIED_STEP_HISTORY.csv]]` | `.csv` | 0.6 KB | 11 lines / records |
| `[[MANIFEST.json]]` | `.json` | 10.6 KB | 243 lines / records |
| `[[_aside_write_test.txt]]` | `.txt` | 0.0 KB | 1 lines / records |
| `[[aln_0001_slab_64atom.cif]]` | `.cif` | 6.2 KB | 89 lines / records |
| `[[aln_144at_slab.cif]]` | `.cif` | 8.1 KB | 162 lines / records |
| `[[aln_144at_slab.vasp]]` | `.vasp` | 8.6 KB | 153 lines / records |
| `[[claude_perplexity_audit_prompt.txt]]` | `.txt` | 4.2 KB | 35 lines / records |
| `[[hybrid_bonding_simulation_results.json]]` | `.json` | 0.3 KB | 9 lines / records |
| `[[input_tmp.in]]` | `.in` | 0.0 KB | 0 lines / records |
| `[[pc2_watchdog.log]]` | `.log` | 0.9 KB | 10 lines / records |

## 2. Detailed Data Profiles

### `BUNDLE.sha256`
- **Path**: `c:\Users\AOL\Desktop\SH.Kim\BUNDLE.sha256`
- **Format**: `.sha256` | **Lines**: 1 | **Size**: 0.1 KB
- **Content Preview**:
```
008816feec13066cdfd0794988da7b9b0eaa26953df1cd0a8b32780281e6021b  aln_migration.tar.gz 
```
---

### `GATE_A_ALL_396_CONTINUOUS_ITERATIONS.csv`
- **Path**: `c:\Users\AOL\Desktop\SH.Kim\GATE_A_ALL_396_CONTINUOUS_ITERATIONS.csv`
- **Format**: `.csv` | **Lines**: 397 | **Size**: 18.6 KB
- **Content Preview**:
```
global_iter,bfgs_step,step_iter,energy,accuracy,dipole_debye,line 1,0,1,-4890.66778131,123.39335454,-1.3071,315 2,0,2,-4885.27274567,41.96017663,-1.90
```
---

### `GATE_A_ALL_396_CONTINUOUS_ITERATIONS.json`
- **Path**: `c:\Users\AOL\Desktop\SH.Kim\GATE_A_ALL_396_CONTINUOUS_ITERATIONS.json`
- **Format**: `.json` | **Lines**: 3566 | **Size**: 71.9 KB
- **Content Preview**:
```
[   {     "global_iter": 1,     "bfgs_step": 0,     "step_iter": 1, 
```
---

### `GATE_A_ALL_ITERATIONS.json`
- **Path**: `c:\Users\AOL\Desktop\SH.Kim\GATE_A_ALL_ITERATIONS.json`
- **Format**: `.json` | **Lines**: 2774 | **Size**: 47.7 KB
- **Content Preview**:
```
[   {     "line": 315,     "restart": 1,     "iter": 1, 
```
---

### `GATE_A_VERIFIED_STEP_HISTORY.csv`
- **Path**: `c:\Users\AOL\Desktop\SH.Kim\GATE_A_VERIFIED_STEP_HISTORY.csv`
- **Format**: `.csv` | **Lines**: 11 | **Size**: 0.6 KB
- **Content Preview**:
```
step,force_Ry_au,scf_corr_Ry_au,energy_Ry,status,date_approx 0,0.093456,0.000149,-4885.23218417,Completed,2026-09-08 1,0.041163,0.000183,-4885.2383404
```
---

### `MANIFEST.json`
- **Path**: `c:\Users\AOL\Desktop\SH.Kim\MANIFEST.json`
- **Format**: `.json` | **Lines**: 243 | **Size**: 10.6 KB
- **Content Preview**:
```
{   "project": "AlN_Simulation",   "target": "ALN_WZ_002_CPLANE",   "orientation": {     "xrd": "(002)", 
```
---

### `_aside_write_test.txt`
- **Path**: `c:\Users\AOL\Desktop\SH.Kim\_aside_write_test.txt`
- **Format**: `.txt` | **Lines**: 1 | **Size**: 0.0 KB
- **Content Preview**:
```
write test
```
---

### `aln_0001_slab_64atom.cif`
- **Path**: `c:\Users\AOL\Desktop\SH.Kim\aln_0001_slab_64atom.cif`
- **Format**: `.cif` | **Lines**: 89 | **Size**: 6.2 KB
- **Content Preview**:
```
data_image0 _chemical_formula_structural       Al2N2Al2N2Al2N2Al2N2Al2N2Al2N2Al2N2Al2N2Al2N2Al2N2Al2N2Al2N2Al2N2Al2N2Al2N2Al2N2 _chemical_formula_sum 
```
---

### `aln_144at_slab.cif`
- **Path**: `c:\Users\AOL\Desktop\SH.Kim\aln_144at_slab.cif`
- **Format**: `.cif` | **Lines**: 162 | **Size**: 8.1 KB
- **Content Preview**:
```
data_AlN_144at_slab _chemical_name_systematic 'Aluminum Nitride (0001) 144-atom Slab' _symmetry_cell_setting hexagonal _symmetry_space_group_name_H-M 
```
---

### `aln_144at_slab.vasp`
- **Path**: `c:\Users\AOL\Desktop\SH.Kim\aln_144at_slab.vasp`
- **Format**: `.vasp` | **Lines**: 153 | **Size**: 8.6 KB
- **Content Preview**:
```
AlN (0001) 144-atom slab 3x3 supercell (8 Al-N bilayers + 20A vacuum) 1.0       9.3978456030      0.0000000000      0.0000000000      -4.6989228015   
```
---

### `claude_perplexity_audit_prompt.txt`
- **Path**: `c:\Users\AOL\Desktop\SH.Kim\claude_perplexity_audit_prompt.txt`
- **Format**: `.txt` | **Lines**: 35 | **Size**: 4.2 KB
- **Content Preview**:
```
[클로드(Claude) 및 퍼플렉시티(Perplexity) 교차 검증용 맞춤 프롬프트] ================================================================================ 아래 프롬프트를 그대로 복사하여 Cl
```
---

### `hybrid_bonding_simulation_results.json`
- **Path**: `c:\Users\AOL\Desktop\SH.Kim\hybrid_bonding_simulation_results.json`
- **Format**: `.json` | **Lines**: 9 | **Size**: 0.3 KB
- **Content Preview**:
```
{   "crossover_thickness_d0_nm": 345.5107294592218,   "crossover_thickness_d1_nm": 1000.0,   "dt_hotspot_150nm_sio2_K": 85.26742113602451,   "dt_hotsp
```
---

### `input_tmp.in`
- **Path**: `c:\Users\AOL\Desktop\SH.Kim\input_tmp.in`
- **Format**: `.in` | **Lines**: 0 | **Size**: 0.0 KB
- **Content Preview**:
```

```
---

### `pc2_watchdog.log`
- **Path**: `c:\Users\AOL\Desktop\SH.Kim\pc2_watchdog.log`
- **Format**: `.log` | **Lines**: 10 | **Size**: 0.9 KB
- **Content Preview**:
```
[2026-09-11 06:17:49] [WATCHDOG] Starting PC2 Simulation Auto-Resume Watchdog... [2026-09-11 06:17:52] [WATCHDOG] live_checkpoint_daemon.py is NOT run
```
---
