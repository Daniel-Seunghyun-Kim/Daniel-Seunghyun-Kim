# Obsidian Knowledge Vault: Shell & PowerShell Scripts Catalog

**Generated**: 2026-10-08 | **Platform**: PC2 Dual RTX 4090 Workstation
**Target Path**: `c:\Users\AOL\Desktop\SH.Kim`

---

## 1. Overview
This catalog documents all background daemons, watchdogs, launcher scripts, and GPU/CPU monitors implemented in PowerShell, Bash, and Windows Batch.

| Script Name | Type | Size | Role & Execution Target |
| :--- | :---: | :---: | :--- |
| `[[OPEN_IN_VESTA.bat]]` | `.bat` | 0.3 KB | @echo off cho ============================================================= |
| `[[TAIL_CPU_LOG.ps1]]` | `.ps1` | 0.6 KB | Intel Core i9-13900K 220-Supercell FC3 Batch Real-Time Streamer Write-Host  |
| `[[TAIL_GPU_LOG.ps1]]` | `.ps1` | 0.5 KB | Dual RTX 4090 GPU 144-Atom Slab QE Output Real-Time Streamer Write-Host "== |
| `[[WATCH_PROGRESS.ps1]]` | `.ps1` | 8.2 KB | PC2 Dual RTX 4090 & Intel i9-13900K DFT Real-Time Monitor param( [int]$Inte |
| `[[pc2_autoresume_watchdog.ps1]]` | `.ps1` | 4.3 KB | =========================================================================== |
| `[[pc2_autoresume_watchdog.ps1.bak_20260921]]` | `.bak_20260921` | 4.5 KB | =========================================================================== |
| `[[run_gpu_parallel_bench.sh]]` | `.sh` | 6.2 KB | !/usr/bin/env bash Dual RTX 4090 parallelisation benchmark for the 144-atom |
| `[[smart_resume_dual_gpu.sh]]` | `.sh` | 3.0 KB | !/usr/bin/env bash set -euo pipefail xport NVHPC_ROOT=/opt/nvidia/hpc_sdk/L |

## 2. Detailed Automation Script Profiles

### `OPEN_IN_VESTA.bat`
- **Path**: `c:\Users\AOL\Desktop\SH.Kim\OPEN_IN_VESTA.bat`
- **Type**: `.bat` (5 lines)
- **Description**: @echo off cho ================================================================ cho  Launching 144-Atom AlN(0002) Polar Slab Supercell in VESTA... cho ==================================================
- **Usage Example**:
```powershell
powershell -ExecutionPolicy Bypass -File .\OPEN_IN_VESTA.bat
```
---

### `TAIL_CPU_LOG.ps1`
- **Path**: `c:\Users\AOL\Desktop\SH.Kim\TAIL_CPU_LOG.ps1`
- **Type**: `.ps1` (7 lines)
- **Description**: Intel Core i9-13900K 220-Supercell FC3 Batch Real-Time Streamer Write-Host "======================================================================" -ForegroundColor Cyan Write-Host " [PC2 CPU Batch] S
- **Usage Example**:
```powershell
powershell -ExecutionPolicy Bypass -File .\TAIL_CPU_LOG.ps1
```
---

### `TAIL_GPU_LOG.ps1`
- **Path**: `c:\Users\AOL\Desktop\SH.Kim\TAIL_GPU_LOG.ps1`
- **Type**: `.ps1` (7 lines)
- **Description**: Dual RTX 4090 GPU 144-Atom Slab QE Output Real-Time Streamer Write-Host "======================================================================" -ForegroundColor Cyan Write-Host " [PC2 Dual RTX 4090] 
- **Usage Example**:
```powershell
powershell -ExecutionPolicy Bypass -File .\TAIL_GPU_LOG.ps1
```
---

### `WATCH_PROGRESS.ps1`
- **Path**: `c:\Users\AOL\Desktop\SH.Kim\WATCH_PROGRESS.ps1`
- **Type**: `.ps1` (154 lines)
- **Description**: PC2 Dual RTX 4090 & Intel i9-13900K DFT Real-Time Monitor param( [int]$Interval = 3, [switch]$Once ) function Show-Dashboard { Clear-Host $now = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
- **Usage Example**:
```powershell
powershell -ExecutionPolicy Bypass -File .\WATCH_PROGRESS.ps1
```
---

### `pc2_autoresume_watchdog.ps1`
- **Path**: `c:\Users\AOL\Desktop\SH.Kim\pc2_autoresume_watchdog.ps1`
- **Type**: `.ps1` (89 lines)
- **Description**: ============================================================================== PC2 Simulation Auto-Resume & Health Watchdog  (rewritten 2026-09-21)  Job: make sure each WSL distro is up and its detach
- **Usage Example**:
```powershell
powershell -ExecutionPolicy Bypass -File .\pc2_autoresume_watchdog.ps1
```
---

### `pc2_autoresume_watchdog.ps1.bak_20260921`
- **Path**: `c:\Users\AOL\Desktop\SH.Kim\pc2_autoresume_watchdog.ps1.bak_20260921`
- **Type**: `.bak_20260921` (110 lines)
- **Description**: ============================================================================== PC2 Simulation Auto-Resume & Health Watchdog Ensures Quantum ESPRESSO Dual RTX 4090 & CPU FC3 runs remain active and resi
- **Usage Example**:
```powershell
powershell -ExecutionPolicy Bypass -File .\pc2_autoresume_watchdog.ps1.bak_20260921
```
---

### `run_gpu_parallel_bench.sh`
- **Path**: `c:\Users\AOL\Desktop\SH.Kim\run_gpu_parallel_bench.sh`
- **Type**: `.sh` (138 lines)
- **Description**: !/usr/bin/env bash Dual RTX 4090 parallelisation benchmark for the 144-atom AlN(0001) slab. Design: GPU_PARALLEL_BENCHMARK_PLAN.md  Tests whether the current `-nk 2` layout is starved by VRAM (28.17 G
- **Usage Example**:
```powershell
powershell -ExecutionPolicy Bypass -File .\run_gpu_parallel_bench.sh
```
---

### `smart_resume_dual_gpu.sh`
- **Path**: `c:\Users\AOL\Desktop\SH.Kim\smart_resume_dual_gpu.sh`
- **Type**: `.sh` (67 lines)
- **Description**: !/usr/bin/env bash set -euo pipefail xport NVHPC_ROOT=/opt/nvidia/hpc_sdk/Linux_x86_64/25.3 xport PATH="$NVHPC_ROOT/compilers/bin:$NVHPC_ROOT/comm_libs/openmpi4/bin:$NVHPC_ROOT/cuda/12.8/bin:$PATH" xp
- **Usage Example**:
```powershell
powershell -ExecutionPolicy Bypass -File .\smart_resume_dual_gpu.sh
```
---
