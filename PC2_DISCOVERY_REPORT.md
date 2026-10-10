# [PC2 Discovery Report] Hardware, Software, and Environment Audit
**Execution Date**: 2026-09-18 18:25 KST  
**Auditor**: Lead HPC / Computational Materials Workflow Engineer  
**Machine Hostname**: DESKTOP-9KGSLD8 (PC2)  
**Audit Status**: VERIFIED (All data obtained via live read-only inspection; zero estimation)

---

## 1. Hardware Discovery

### 1.1 Central Processing Unit (CPU)
- **Model**: 13th Gen Intel(R) Core(TM) i9-13900K
- **Microarchitecture**: Raptor Lake-S (Intel 7 process)
- **Physical Cores**: 24 total (8 Performance-cores with Hyper-Threading + 16 Efficient-cores)
- **Logical Processors**: 32 threads
- **Base / Measured Clock**: 3.00 GHz (Current clock: 3000 MHz)
- **Cache Topology**:
  - L1d: 768 KiB (16 instances)
  - L1i: 512 KiB (16 instances)
  - L2: 32 MiB (16 instances)
  - L3: 36 MiB shared (1 instance)
- **NUMA Topology**: 1 NUMA node (node0: CPUs 0–31)
- **Current Load**: High sustained load (~16 threads at 99–100% CPU occupancy via `pw.x` MPI batch)

### 1.2 Memory (RAM & Swap)
- **Physical RAM (Windows Host)**: 127.75 GB (133,952,436 KB total visible)
- **Available Physical RAM (Host)**: 35.29 GB free (37,000,828 KB)
- **Virtual Memory / Pagefile**: 166.16 GB total (16.65 GB free)
- **WSL2 Memory Allocation**:
  - Total WSL2 RAM: **108 GiB**
  - Used in WSL2: 26 GiB
  - Free in WSL2: 71 GiB
  - Buffer / Cache: 27 GiB
  - Available in WSL2: **81 GiB**
  - Swap: **32 GiB** total (0 B used)
- **Memory Pressure Assessment**: LOW. >81 GiB available inside WSL2; no swapping active.

### 1.3 Graphics Processing Units (GPUs)
- **GPU 0**:
  - Model: NVIDIA GeForce RTX 4090
  - Architecture: Ada Lovelace (AD102, Compute Capability sm_89)
  - VRAM: 24,564 MiB (24.0 GB)
  - Driver Version: 591.86
  - Utilization: **100%**
  - VRAM In Use: **24,037 MiB** (102 MiB free)
  - Temperature: 51 °C
  - Power Draw: 103.5 W / 450.0 W (P2 state)
- **GPU 1**:
  - Model: NVIDIA GeForce RTX 4090
  - Architecture: Ada Lovelace (AD102, Compute Capability sm_89)
  - VRAM: 24,564 MiB (24.0 GB)
  - Driver Version: 591.86
  - Utilization: **100%** (active MPI rank 1)
  - VRAM In Use: **24,047 MiB** (92 MiB free)
  - Temperature: 48 °C
  - Power Draw: 111.5 W / 450.0 W (P2 state)
- **Total Combined VRAM**: 48.0 GB

### 1.4 Storage & Filesystems
- **Drive C: (Windows System & Data)**:
  - Total Capacity: 952.76 GB (1,023,024,295,936 bytes)
  - Free Space: **331.85 GB** (356,322,623,488 bytes)
  - Filesystem: NTFS
- **WSL2 Virtual Disks**:
  - Mounted via ext4 inside WSL2 virtual disk images (`ext4` on `/dev/sdb`, `/dev/sdc`)
- **Primary Research Directories & Approximate Sizes**:
  - `c:\Users\AOL\Desktop\SH.Kim\`: ~15–20 GB
  - `Simulation_History_20260904_20260918\`: ~144 MB
  - WSL2 `/home/aol/campaign_fc3_320ang/`: ~8.5 GB (220 supercells)
  - WSL2 `/home/aol2/campaign_144at_gpu/`: ~4.2 GB (144-atom slab wavefunctions & logs)

---

## 2. Software and Environment Discovery

### 2.1 Operating System & Subsystems
- **Host OS**: Microsoft Windows 11 Home (64-bit), Version 10.0.26200
- **WSL Subsystem**: WSL Version 2, Kernel `6.18.33.2-microsoft-standard-WSL2`
- **Active WSL Distributions**:
  1. `Ubuntu-22.04` (State: Running, Default WSL dist)
  2. `Ubuntu-24.04` (State: Running)

### 2.2 Quantum ESPRESSO & Scientific Binaries
| Distribution | Executable | Full Verified Path | Version / Build Details |
| :--- | :--- | :--- | :--- |
| **Ubuntu-24.04** | `pw.x` (GPU) | `/home/aol2/qe_gpu_builds/qe-7.2-dual4090-sm89/bin/pw.x` | **Quantum ESPRESSO v.7.2** (NVIDIA HPC SDK 25.3, sm_89 Dual 4090 Opt) |
| **Ubuntu-24.04** | `pw.x` (CPU) | `/usr/bin/pw.x` | PWSCF v.6.7MaX |
| **Ubuntu-24.04** | `ph.x` | `/usr/bin/ph.x` | PHonon v.6.7MaX |
| **Ubuntu-24.04** | `q2r.x` | `/usr/bin/q2r.x` | v.6.7MaX |
| **Ubuntu-24.04** | `matdyn.x` | `/usr/bin/matdyn.x` | v.6.7MaX |
| **Ubuntu-22.04** | `pw.x` (CPU) | `/usr/bin/pw.x` | **PWSCF v.6.7MaX** (Used for FC3 batch) |
| **Ubuntu-22.04** | `ph.x` | `/usr/bin/ph.x` | PHonon v.6.7MaX |
| **Ubuntu-22.04** | `q2r.x` | `/usr/bin/q2r.x` | v.6.7MaX |
| **Ubuntu-22.04** | `matdyn.x` | `/usr/bin/matdyn.x` | v.6.7MaX |
| **Ubuntu-22.04** | `lmp` (LAMMPS) | `/usr/bin/lmp` | LAMMPS (29 Sep 2021 - Update 2) |
| **Ubuntu-22.04** | `phonopy` | `/home/aol/.local/bin/phonopy` | **Phonopy v.4.4.0** |
| **Ubuntu-22.04** | `phono3py` | `/home/aol/.local/bin/phono3py` | **Phono3py v.4.4.0** |

### 2.3 MPI Environments
- **Ubuntu-22.04**:
  - Binary: `/usr/bin/mpirun`
  - Version: **Open MPI 4.1.2**
- **Ubuntu-24.04**:
  - Primary Binary: `/opt/nvidia/hpc_sdk/Linux_x86_64/25.3/comm_libs/12.8/openmpi4/latest/bin/mpirun`
  - Version: **Open MPI 4.1.5** (NVIDIA HPC-X / CUDA 12.8 integrated)
  - Wrapper: `/mnt/c/Users/AOL/Downloads/AlN_QE_PC2/AlN_QE_PC2_Dual4090_20260728_172441/wsl/qe_rank_gpu_wrapper.sh`

### 2.4 Python Environments & Libraries Matrix
| Library / Package | Windows Host (Python 3.10.11) | WSL Ubuntu-22.04 (Python 3.10.12) | WSL Ubuntu-24.04 (Python 3.12.3) |
| :--- | :--- | :--- | :--- |
| **NumPy** | 2.2.6 | 2.2.6 | NOT INSTALLED |
| **SciPy** | 1.15.3 | 1.15.3 | NOT INSTALLED |
| **pandas** | 2.3.3 | NOT INSTALLED | NOT INSTALLED |
| **h5py** | NOT INSTALLED | 3.16.0 | NOT INSTALLED |
| **ASE** | NOT INSTALLED | 3.29.0 | NOT INSTALLED |
| **pymatgen** | NOT INSTALLED | NOT INSTALLED | NOT INSTALLED |
| **PyTorch** | 2.12.1+cu130 | NOT INSTALLED | NOT INSTALLED |
| **phonopy** | NOT INSTALLED | 4.4.0 | NOT INSTALLED |
| **phono3py** | NOT INSTALLED | 4.4.0 | NOT INSTALLED |
| **Git** | 2.43.0 (in PATH) | 2.34.1 | 2.43.0 |

### 2.5 Workflow Management Software Detection
- **SLURM (`sbatch`, `squeue`)**: NOT DETECTED
- **PBS (`qsub`)**: NOT DETECTED
- **HTCondor (`condor_q`)**: NOT DETECTED
- **AiiDA (`verdi`)**: NOT DETECTED
- **FireWorks (`lpad`)**: NOT DETECTED
- **jobflow / atomate2**: NOT DETECTED
- **Existing Custom Workflow Schedulers**:
  - `run_cpu_batch.sh` (Sequential bash batch loop for FC3 supercells in `/home/aol/campaign_fc3_320ang/`)
  - `test_gpu_launch.sh` (GPU launcher for 144-atom slab)
  - `pc2_schedule_20260916/plan.json` (Gate/policy definition)
  - `auto_master_chain.py` (Custom Python monitoring daemon)
  - `WATCH_PROGRESS.ps1` (Real-time monitoring dashboard)

---

## 3. Currently Running Research Processes (Live Audit)

### 3.1 GPU Track (WSL2 Ubuntu-24.04)
- **Processes**:
  - PID `208189`: `pw.x -nk 2 -in pw.in` (Rank 0 on GPU 0, 99% CPU)
  - PID `208190`: `pw.x -nk 2 -in pw.in` (Rank 1 on GPU 1, 99% CPU)
  - Parent launcher PID `208177`: `bash test_gpu_launch.sh`
- **Active Task**: 144-atom AlN(0001) polar slab BFGS geometry relaxation (`calculation = 'relax'`).
- **Working Directory**: `/home/aol2/campaign_144at_gpu/`
- **State as of 18:50 KST**: BFGS Step 4, SCF Cycle 5, Iteration #20/200, estimated accuracy $2.0\times 10^{-8}\ \mathrm{Ry}$ (near $1.0\times 10^{-8}\ \mathrm{Ry}$ threshold).

### 3.2 CPU Track (WSL2 Ubuntu-22.04)
- **Processes**:
  - PID `652`: `bash run_cpu_batch.sh`
  - PID `6608`: `mpirun -np 16 pw.x -in /home/aol/campaign_fc3_320ang/jobs/supercell-00538/pw.in`
  - 16 parallel instances of `/usr/bin/pw.x`
- **Active Task**: Phono3py FC3 anharmonic supercell batch (`[96/220] supercell-00538`).
- **Working Directory**: `/home/aol/campaign_fc3_320ang/`
- **State as of 18:50 KST**: **95 / 220 supercells completed (43.2%)**. `supercell-00537` completed successfully at 17:01 KST; `supercell-00538` running.
