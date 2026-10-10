# 125-Atom Al(111) Parent Slab BFGS Relaxation: Final Convergence Report

## 1. 개요 및 하드웨어 사양
- **계산 대상**: 125원자 Al(111) 모체 슬랩 (5개 층, $5\times 5$ 초격자 구조)
- **실행 환경**: PC2 Dual NVIDIA GeForce RTX 4090 (24 GB $\times 2$, 총 48 GB VRAM)
- **QE GPU 빌드**: `/home/aol2/qe_gpu_builds/qe-7.2-dual4090-sm89/bin/pw.x`
- **실행 설정**: `np=2, nk=1` (Dual GPU Rank 바인딩), `conv_thr = 1.0E-6 Ry`
- **복구 관리자**: `adaptive_recovery_supervisor.py` (무중단 자율 복구 데몬)

---

## 2. 수렴 지표 및 BFGS 최종 완결 결과

```
     Total force =     0.000051     Total SCF correction =     0.000061
     Energy error            =      5.1E-07 Ry
     Gradient error          =      8.2E-06 Ry/Bohr

     bfgs converged in  18 scf cycles and  17 bfgs steps
     (criteria: energy <  1.0E-05 Ry, force <  1.0E-04 Ry/Bohr)

     End of BFGS Geometry Optimization

     Final energy             =   -4936.5136671520 Ry
```

### 핵심 수렴 감사 결과:
1. **잔류 힘 수렴**: **$0.000051\ \text{Ry/Bohr}$** (엄격한 기준치인 $1.0\times 10^{-4}\ \text{Ry/Bohr}$의 절반 수준으로 완벽 수렴).
2. **에너지 오차**: **$5.1\times 10^{-7}\ \text{Ry}$** (기준치 $1.0\times 10^{-5}\ \text{Ry}$ 대비 20배 고정밀 수렴).
3. **최종 바닥 상태 에너지**: **$-4936.5136671520\ \text{Ry}$**.
4. **소요 스텝**: 12차 체크포인트 재개 이후 18회 SCF 사이클 및 17회 BFGS 스텝으로 완결.

---

## 3. 자율 복구 관리자 (`adaptive_recovery_supervisor.py`)의 기여 분석

1. **전하 진동(Charge Sloshing) 실시간 감지**:
   - 125원자 대형 금속 슬랩의 Fermi 면 복잡성으로 인해 초기 SCF 정확도가 $0.325 \to 0.420 \to 0.542 \to 0.562\ \text{Ry}$로 발산하는 이상 징후 포착.
2. **동적 파라미터 적응형 보정**:
   - 관리자가 솔버를 안전하게 인터럽트한 후, 혼합 인자(`mixing_beta`)를 $0.20 \to 0.10 \to 0.05$로 즉각 감쇠.
3. **무중단 재개 및 완결 도달**:
   - `mixing_beta = 0.05` 적용 후 1차 SCF가 안정적으로 수렴 궤도에 진입, 18개 SCF 사이클 만에 `JOB DONE` 및 `COMPLETED_VALIDATED` 달성.

---

## 4. 후속 연구 단계 연계 (Step A3 준비 완료)
- 수렴된 125원자 Al(111) 표면 좌표(`/mnt/c/Users/AOL/Desktop/SH.Kim/Simulation_Verification_2026-09-30/gpu_parent_ABC_20261001/scratch/Al125_parent_ABC_20261001.save/`)가 완벽하게 저장되었습니다.
- **Step A3 착수 가능**: 질소 단원자 흡착 4대 마이크로스테이트(`ontop`, `bridge`, `fcc hollow`, `hcp hollow`)의 DFT 계산을 신뢰성 있는 기준 좌표 상에서 즉시 전개할 수 있습니다.
