# Project Execution Rules - PC2 Dual RTX 4090 All-In-One Platform

## 1. Workstation & Standalone Execution Policy
- **PC2 Complete Computing & Rendering Hub**: All DFT calculations (Quantum ESPRESSO), convergence studies (`00_clean_convergence`), data organization, log analysis, 3D structure visualization (VESTA), and photorealistic 3D rendering (Blender with NVIDIA OptiX Dual RTX 4090 acceleration) MUST be executed directly on **PC2**.
- **No Transfer Requirement**: Zero data transfer to PC1 is required. PC2 handles the entire pipeline end-to-end from simulation to publication-grade 3D renders.

## 2. Quantum ESPRESSO Dual GPU Environment Setup
- **OS**: Windows 11 + WSL2 (`Ubuntu-24.04`)
- **GPUs**: 2 x NVIDIA GeForce RTX 4090 (24 GB VRAM each, total 48 GB VRAM)
- **NVIDIA HPC SDK Root**: `/opt/nvidia/hpc_sdk/Linux_x86_64/25.3`
- **QE GPU Binary**: `/home/aol2/qe_gpu_builds/qe-7.2-dual4090-sm89/bin/pw.x`
- **GPU Rank Binding Script**: `/mnt/c/Users/AOL/Downloads/AlN_QE_PC2/AlN_QE_PC2_Dual4090_20260728_172441/wsl/qe_rank_gpu_wrapper.sh`

## 3. High-End 3D Rendering & Visualization (Blender + VESTA on PC2)
- **VESTA**: Used for structure verification, POSCAR/CIF generation, and electron density isosurface extraction.
- **Blender + OptiX**: Uses Dual RTX 4090 OptiX Ray Tracing acceleration for sub-second, 8K publication-ready 3D rendering of nitridation microstates and charge transfers.

## 4. Convergence Suite Policy
- `00_clean_convergence` suite uses Cutoff (35, 45, 55 Ry), K-points (`kpoint_gamma`, `kpoint_3x3x1`, `kpoint_5x5x5`), Vacuum (24, 29.67, 36 Å), and Slab layer thickness (4-layer, 5-layer).
- `kpoint_2x2x1` is excluded in favor of `kpoint_5x5x5`.

## 5. Memory Envelope & MAX_SAFE_ATOMS (PC2 128 GB RAM / WSL 108 GiB)
- **Verified Hardware Memory Limit**: **128 GB Physical RAM** (WSL2 allocated **108 GiB** RAM + 32 GiB Swap, with >82 GiB available).
- **Safe Production Limit (`-nk 4`)**: **`MAX_SAFE_ATOMS = 192`** (RAM peak ~55-65 GB, leaving >40 GB safety margin).
- **Recommended Production Limit (`-nk <= 2`)**: **`MAX_SAFE_ATOMS = 144 ~ 192`** (RAM peak ~40-55 GB, leaving >50 GB safety margin).
- **Extreme Memory-Conserving Mode (`-nk = 1`)**: **`MAX_SAFE_ATOMS = 256`** (RAM peak ~75.0 GB).
- **Prohibited on Single Node**: Cells $\ge$ 384 atoms without external distributed memory.

## 6. Scientific Rigor, Unit Conventions & Audited Guidelines (Astra Audit 2026-09-09)
- **Phonon Lifetime Formula**: `gamma` in phono3py is ordinary frequency half-linewidth in THz. The physical lifetime is strictly:
  $$\tau_{\text{ps}} = \frac{1}{4\pi (\Gamma + \Gamma_{\text{iso}} + \Gamma_{\text{ext}})}$$
  (Never declare $\tau = 1/(2\Gamma)$ which is a $2\pi$ mathematical error).
- **Unit Cell Volume**: Wurtzite AlN primitive cell volume $\Omega = \frac{\sqrt{3}}{2} a^2 c = 42.6820689169\ \text{Å}^3$ ($a = 3.132615\ \text{Å}, c = 5.022278\ \text{Å}$).
- **Non-Analytical Correction (NAC) Factor**: For Å and eV/Å² units, the exact NAC factor is **`14.3996517259`** (never use 2.0).
- **Directional MFP Definition**: Use $\Lambda_z = |v_z| \tau$ for cross-plane transport along c-axis. Cumulative percentiles must use discrete weighted quantiles ($\Lambda_{50, z} = 139.56\ \text{nm}$, $\Lambda_{90, z} = 1894.89\ \text{nm}$).
- **Banned Literature**: **Bogner et al. (Surf. Coat. Tech. 2017)** is formally RETRACTED; never use as benchmark or calibration baseline.
- **Intrinsic BTE vs Sputtered Thin-Film Distinction**:
  - Always state that Vermeersch BTE values ($85.23\ \text{W/mK}$ for $150\ \text{nm}$) are ideal single-crystal upper bounds.
  - Sputtered experimental films have oxygen impurities ($O_N$), grain boundaries, and texture mismatch, yielding lower measured values ($18.7 \pm 4.6\ \text{W/mK}$ in Perez 2023 for 100 nm).
  - Decompose: $\frac{1}{k_{\text{meas}}} = \frac{1}{k_{\text{intrinsic}}} + \frac{1}{k_{\text{GB}}} + \frac{1}{k_{\text{defect}}} + \frac{1}{k_{\text{interface}}}$.
- **144-Atom Slab Definition**: 4-atom WZ unit cell in $3\times 3\times 4$ repetition = **144 atoms, 8 Al-N bilayers (16 atomic layers)**. Clearly distinguish (0002) Bragg plane ($d_{0002} = c/2$) from (0001) surface plane.
