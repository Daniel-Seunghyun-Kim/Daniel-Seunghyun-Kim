# [QE Benchmark Plan] Quantum ESPRESSO Scaling & Throughput Optimization Protocol for PC2
**Date**: 2026-09-18 18:35 KST  
**Author**: Lead HPC / Computational Materials Workflow Engineer  
**Target Node**: PC2 (Core i9-13900K 24-Core/32-Thread, 128 GB RAM)  
**Safety Status**: NON-DESTRUCTIVE PROTOCOL (Operates exclusively on isolated copies)  

---

## 1. Benchmark Objectives

1. **Quantify Parallel Scaling**: Measure wall-time, parallel speedup ($S_p$), and parallel efficiency ($E_p$) of Quantum ESPRESSO `pw.x` on the Core i9-13900K across thread counts: **4, 8, 16, 24, and 32 threads**.
2. **Resolve Asymmetric Core Architecture Impact**: The i9-13900K contains 8 Performance-cores (16 threads with Hyper-Threading) and 16 Efficient-cores. Benchmarking will determine whether spreading MPI across P-cores and E-cores causes thread synchronization stalls.
3. **Determine Optimal Throughput Topology**: Answer the critical HPC question:
   $$\text{Does PC2 achieve higher scientific throughput as } \mathbf{1 \times 32\text{-thread job}} \text{ or } \mathbf{2 \times 16\text{-thread concurrent jobs}} \text{ or } \mathbf{3 \times 8\text{-thread concurrent jobs}}?$$

---

## 2. Safety & Provenance Rules

> [!CAUTION]
> **Strict Non-Destructive Benchmark Policy**:
> - Benchmarks will NEVER run inside active production directories (`/home/aol2/campaign_144at_gpu/` or `/home/aol/campaign_fc3_320ang/`).
> - Benchmarks will NEVER run while GPU VRAM or host memory exceeds 75% utilization.
> - Benchmarks will run on an isolated copy inside:
>   $$\mathbf{c:\backslash Users\backslash AOL\backslash Desktop\backslash SH.Kim\backslash PC2\_RESEARCH\_NODE\backslash benchmarks\backslash qe\_scaling\backslash}$$

---

## 3. Representative Benchmark System

- **Selected Physical System**: Wurtzite AlN $2\times 2\times 2$ supercell (32 atoms) with PBE norm-conserving/PAW pseudopotentials.
- **Scientific Parameters (Strictly Constant Across All Runs)**:
  - `ecutwfc = 80.0 Ry`, `ecutrho = 320.0 Ry`
  - $k$-point mesh: $3\times 3\times 3$ Monkhorst-Pack grid (shifted)
  - Diagonalization: `david` (Davidson with overlap)
  - Mixing: `beta = 0.40`
  - Convergence threshold: `conv_thr = 1.0d-8 Ry`
  - Number of SCF cycles: Fixed to 10 iterations (to ensure identical mathematical workload)

---

## 4. Test Matrix & Execution Configurations

| Run ID | MPI Ranks (`-np`) | OpenMP Threads (`OMP_NUM_THREADS`) | Total Logical Threads | Target Core Mapping | Notes |
| :---: | :---: | :---: | :---: | :--- | :--- |
| **BM-04** | 4 | 1 | 4 | P-cores only (Cores 0, 2, 4, 6) | Baseline low-concurrency test |
| **BM-08** | 8 | 1 | 8 | P-cores only (All 8 physical P-cores) | Tests pure P-core execution |
| **BM-16** | 16 | 1 | 16 | 8 P-cores (HT) or mixed P+E | Current standard configuration in `run_cpu_batch.sh` |
| **BM-24** | 24 | 1 | 24 | 8 P-cores + 16 E-cores (1 thread/core) | Tests all physical cores without hyperthreads |
| **BM-32** | 32 | 1 | 32 | Full CPU saturation (All 32 logical threads) | Tests maximum thread saturation |
| **BM-2x16** | 2 concurrent jobs $\times$ 8 MPI | 1 | 16 total | Concurrent batch throughput test | Measures aggregated daily throughput |
| **BM-3x08** | 3 concurrent jobs $\times$ 8 MPI | 1 | 24 total | High-throughput concurrent queue | Reserves 8 threads for OS/GPU driver |

---

## 5. Measured Metrics & Output Deliverables

For each benchmark run, the following metrics will be automatically extracted:
1. **Wall Time ($T_{\text{wall}}$)**: Exact wall-clock seconds from `pw.x` output.
2. **CPU Time ($T_{\text{cpu}}$)**: Total aggregated CPU seconds.
3. **Peak Memory (RAM)**: Measured via `/usr/bin/time -v` (Maximum resident set size).
4. **Speedup ($S_p$)**:
   $$S_p = \frac{T_{\text{wall}}(p=4)}{T_{\text{wall}}(p)} \times 4$$
5. **Parallel Efficiency ($E_p$)**:
   $$E_p = \frac{S_p}{p} \times 100\%$$
6. **Convergence Verification**: Energy at iteration 10 must match across all runs within $10^{-6}\ \mathrm{Ry}$ to verify arithmetic equivalence.

### Output Files:
- `PC2_RESEARCH_NODE/benchmarks/QE_SCALING.csv`
- `PC2_RESEARCH_NODE/benchmarks/QE_SCALING_REPORT.md`

---

## 6. Execution Pre-conditions

> [!IMPORTANT]
> The benchmark suite will **NOT** be launched until:
> 1. The researcher reviews and approves this plan.
> 2. The active CPU FC3 batch or GPU slab calculation reaches a safe transition gate.
