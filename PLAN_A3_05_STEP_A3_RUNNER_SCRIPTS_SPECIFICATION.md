# Step A3: 실행 래퍼 스크립트 명세 및 무중단 가동 지침 (Runner Scripts Specification)

**대상 환경**: PC2 WSL2 Ubuntu-24.04 (Dual RTX 4090)  
**작성일**: 2026-10-10 (Asia/Seoul)

---

## 1. 스크립트 아키텍처

```
Simulation_Verification_2026-09-30/
├── Step_A3_Dual4090_Execution_Plan/    # 본 마크다운 가이드 폴더
└── step_a3_adsorption_campaign/        # 실제 연산 작업 폴더
    ├── 01_ontop/                       # pw.in, pw.out, scratch/
    ├── 02_bridge/                      # pw.in, pw.out, scratch/
    ├── 03_fcc_hollow/                  # pw.in, pw.out, scratch/
    ├── 04_hcp_hollow/                  # pw.in, pw.out, scratch/
    ├── launch_step_a3_chain.sh         # 전체 4개 사이트 연속 자동 실행 래퍼
    └── a3_supervisor.py                # 사이트 전환 및 복구 자동화 관리자
```

---

## 2. 연속 실행 래퍼 스크립트 핵심 로직 (`launch_step_a3_chain.sh`)

```bash
#!/usr/bin/env bash
set -euo pipefail

BASE="/mnt/c/Users/AOL/Desktop/SH.Kim/Simulation_Verification_2026-09-30/step_a3_adsorption_campaign"
QE_BIN="/home/aol2/qe_gpu_builds/qe-7.2-dual4090-sm89/bin/pw.x"
WRAPPER="/mnt/c/Users/AOL/Downloads/AlN_QE_PC2/AlN_QE_PC2_Dual4090_20260728_172441/wsl/qe_rank_gpu_wrapper.sh"

export OMP_NUM_THREADS=8
export MKL_NUM_THREADS=8
export OPENBLAS_NUM_THREADS=8

SITES=("01_ontop" "02_bridge" "03_fcc_hollow" "04_hcp_hollow")

for site in "${SITES[@]}"; do
    echo "=========================================================="
    echo "  STARTING STEP A3 ADSORPTION SITE: $site"
    echo "  Time: $(date -Is)"
    echo "=========================================================="
    cd "$BASE/$site"
    
    # Dual RTX 4090 np=2, nk=1 실행
    mpirun -np 2 bash "$WRAPPER" "$QE_BIN" -nk 1 -in pw.in > pw.out 2> pw.err
    
    # 수렴 확인
    if grep -q "JOB DONE" pw.out; then
        echo "[SUCCESS] $site CONVERGED (JOB DONE)"
    else
        echo "[WARNING] $site did not reach JOB DONE, checking supervisor..."
    fi
done

echo "=== ALL 4 ADSORPTION MICROSTATES EXECUTED ==="
```

---

## 3. 원클릭 백그라운드 가동 명령어 (Windows PowerShell)

```powershell
# Windows PowerShell에서 WSL2 백그라운드 분리 실행
wsl.exe -d Ubuntu-24.04 -u aol2 -- nohup bash /mnt/c/Users/AOL/Desktop/SH.Kim/Simulation_Verification_2026-09-30/step_a3_adsorption_campaign/launch_step_a3_chain.sh > /mnt/c/Users/AOL/Desktop/SH.Kim/Simulation_Verification_2026-09-30/step_a3_adsorption_campaign/campaign.log 2>&1 &
```

---

## 4. 실시간 모니터링 명령어

```powershell
# 1. GPU 로드 및 온도 확인
wsl.exe -d Ubuntu-24.04 -u aol2 -- nvidia-smi

# 2. 실시간 BFGS 수렴 추적
wsl.exe -d Ubuntu-24.04 -u aol2 -- tail -f /mnt/c/Users/AOL/Desktop/SH.Kim/Simulation_Verification_2026-09-30/step_a3_adsorption_campaign/campaign.log
```
