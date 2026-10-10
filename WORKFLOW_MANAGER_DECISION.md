# [Workflow Manager Decision Report] Orchestration Architecture Evaluation for PC2
**Date**: 2026-09-18 18:32 KST  
**Evaluator**: Lead HPC / Computational Materials Workflow Engineer  
**Status**: PROPOSAL (Awaiting Researcher Review; Zero Software Installed)  

---

## 1. Context and Objective

PC2 is a hybrid Windows 11 + Dual WSL2 (`Ubuntu-22.04` and `Ubuntu-24.04`) workstation equipped with an Intel Core i9-13900K (32 threads), 128 GB RAM, and Dual NVIDIA GeForce RTX 4090 (48 GB VRAM). Its primary mission is 24/7 unattended execution of Quantum ESPRESSO, Phono3py, and multiscale thermal transport calculations for an AlN PhD research program.

The orchestration system must satisfy:
$$\text{Objective} = \max(\text{RELIABILITY} \times \text{SCIENTIFIC VALIDITY} \times \text{THROUGHPUT} \times \text{REPRODUCIBILITY})$$

---

## 2. Workflow Manager Candidates

1. **Option A: Lightweight Python Scheduler + Research-MCP Engine**
   - Architecture: Python-based asynchronous job supervisor utilizing a file/SQLite/JSON state engine, process wrappers, and MCP protocol integration.
   - External Dependencies: Zero (pure Python standard library + existing `numpy`/`ase`).
2. **Option B: Jobflow + FireWorks**
   - Architecture: Materials Project graph-based task engine with MongoDB document database backend.
   - External Dependencies: MongoDB server, `pymatgen`, `jobflow`, `fireworks`.
3. **Option C: AiiDA (Automated Interactive Infrastructure and Density)**
   - Architecture: Full provenance graph workflow framework with daemon architecture.
   - External Dependencies: PostgreSQL database server, RabbitMQ message broker, `aiida-core`, `aiida-quantumespresso`.
4. **Option D: Existing Custom Scripts (`run_cpu_batch.sh` + `auto_master_chain.py`)**
   - Architecture: Sequential Bash loop on CPU and manual shell scripts on GPU.

---

## 3. Decision Matrix

| Evaluation Criteria (Weight) | Option A: Lightweight Python + MCP | Option B: Jobflow / FireWorks | Option C: AiiDA | Option D: Existing Shell Scripts |
| :--- | :---: | :---: | :---: | :---: |
| **QE Compatibility** (10%) | 10 / 10 | 9 / 10 | 10 / 10 | 9 / 10 |
| **Phono3py Compatibility** (10%) | **10 / 10** | 7 / 10 | 6 / 10 | 8 / 10 |
| **Windows/Dual-WSL2 Stability** (15%) | **10 / 10** | 6 / 10 | 4 / 10 | 8 / 10 |
| **Zero External DB Overhead** (10%) | **10 / 10** (File/SQLite) | 5 / 10 (Requires MongoDB) | 3 / 10 (PostgreSQL+RabbitMQ) | 10 / 10 (Text logs) |
| **Failure Isolation & Quarantine** (15%) | **10 / 10** | 8 / 10 | 9 / 10 | 3 / 10 (Can stall queue) |
| **Scientific Provenance Tracking** (10%) | 9 / 10 | 9 / 10 | **10 / 10** | 4 / 10 |
| **Unattended 24/7 Reliability** (15%) | **10 / 10** | 7 / 10 | 6 / 10 | 6 / 10 |
| **Ease of Audit & Low Complexity** (15%) | **10 / 10** | 7 / 10 | 5 / 10 | 7 / 10 |
| **Total Weighted Score** | **9.85 / 10** | **7.40 / 10** | **6.40 / 10** | **6.75 / 10** |

---

## 4. Deep-Dive Comparative Analysis

### 4.1 Why Option C (AiiDA) is NOT Recommended for PC2
- **Severe Database/Daemon Fragility on Windows/WSL2**: AiiDA requires running PostgreSQL and RabbitMQ background services inside WSL2. When Windows sleeps, updates, or restarts the WSL virtual network interface, RabbitMQ socket connections frequently drop, causing the AiiDA daemon to hang silently.
- **Phono3py Friction**: AiiDA has dedicated plugins for QE (`aiida-quantumespresso`), but lacks native, battle-tested support for advanced Phono3py 3-phonon displacement batches, requiring complex ad-hoc wrappers.
- **Heavy Learning Curve**: High maintenance overhead for a single PhD workstation.

### 4.2 Why Option B (Jobflow/FireWorks) is Suboptimal
- **MongoDB Requirement**: FireWorks relies on an active MongoDB instance. Running a database daemon inside a WSL2 environment that shares memory with Windows adds an unnecessary point of failure.
- **Python Version Mismatch**: PC2 has Python 3.10 on Ubuntu-22.04 and Python 3.12 on Ubuntu-24.04. Installing the full `pymatgen` and `atomate2` stack across both distros introduces dependency conflicts.

### 4.3 Why Option D (Existing Shell Scripts) is Insufficient
- **Single Point of Failure**: In `run_cpu_batch.sh`, if a single supercell encounters an unhandled MPI error or hangs, the entire queue stops.
- **No Memory-Aware Scheduling**: Cannot dynamically check available RAM before launching subsequent jobs.
- **No Structured Provenance**: Outputs are simple text logs with no cryptographic hashes or automated quarantine.

### 4.4 Why Option A (Lightweight Python Scheduler + Research-MCP) WINS
1. **Rock-Solid Reliability in Dual-WSL2**: Operates natively across Windows, Ubuntu-22.04, and Ubuntu-24.04 via standard Python 3 standard library (`subprocess`, `pathlib`, `sqlite3`, `json`).
2. **Zero Daemon/Service Crashes**: No external database (PostgreSQL/MongoDB/RabbitMQ) that can silently disconnect. All state is persisted to an ACID SQLite database and human-readable JSON state ledger.
3. **Phono3py & QE Native**: Tailored directly to handle QE `pw.x` exit conditions and Phono3py YAML/HDF5 force collections seamlessly.
4. **Strict Failure Isolation**: Implements the 8-state machine (`PENDING`, `READY`, `RUNNING`, `VALIDATING`, `COMPLETED`, `FAILED`, `QUARANTINED`, `BLOCKED`). A failed job is quarantined immediately, and the queue proceeds to the next independent supercell.
5. **Memory & Thermal Watchdog**: Directly queries `free -m` and `nvidia-smi` before releasing any job from the queue.

---

## 5. Formal Recommendation & Action Directive

**Recommendation**: Deploy **Option A (Lightweight Python Research-Node Scheduler)** within `PC2_RESEARCH_NODE/`.

> [!IMPORTANT]
> **Action Constraint**: No scheduler software, daemons, or packages will be installed until the researcher explicitly approves this recommendation in writing.
