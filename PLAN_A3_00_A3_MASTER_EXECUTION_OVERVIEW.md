# Step A3: 4대 질소 흡착 마이크로스테이트 무중단 실행 계획서 (Master Execution Overview)

**연구 과제**: AlN 초기 질화 기구 규명 및 계면 열전도도 최적화  
**대상 노드**: PC2 Dual RTX 4090 All-In-One 워크스테이션  
**기반 모델**: 로컬 `@local` (Ollama `gemma4:e4b`) 아키텍처 가이드 기반 수립  
**일자**: 2026-10-10 (Asia/Seoul)

---

## 1. 연구 맥락 및 선행 완료 단계
본 계획은 다음의 두 가지 핵심 선행 계산이 100% 검증 완료됨에 따라 즉시 착수되는 후속 파이프라인입니다:

1. **125원자 Al(111) 모체 슬랩 수렴 완결 (`JOB DONE`)**:
   - 최종 잔류 힘: $0.000051\ \text{Ry/Bohr}$ (기준치 $1.0\times 10^{-4}\ \text{Ry/Bohr}$ 충족)
   - 최종 바닥 상태 에너지: $E_{\text{slab}} = -4936.51366715\ \text{Ry}$
   - 보존 좌표: `Simulation_Verification_2026-09-30/gpu_parent_ABC_20261001/scratch/`
2. **3.20 Å FC3 기반 AlN 격자 열전도도 완결**:
   - 300 K LBTE 결과: $\kappa_{xx} = \kappa_{yy} = 278.29\ \text{W/m·K}$, $\kappa_{zz} = 237.90\ \text{W/m·K}$ (벌크 단결정 상한선 확립)

---

## 2. Step A3 핵심 목표
- 수렴된 125원자 Al(111) 표면의 최상층에 단일 질소 원자(N)가 흡착되는 4대 대칭 사이트의 구조 최적화 및 흡착 에너지($E_{\text{ads}}$) 산출:
  1. **Site 1: `ontop`** (최상층 Al 원자 바로 위 수직 흡착)
  2. **Site 2: `bridge`** (인접한 두 Al 원자 사이의 이중 결합 자리)
  3. **Site 3: `fcc hollow`** (3개 Al 원자 사이의 정삼각형 중공 자리, 아래 2층에 원자가 없는 자리)
  4. **Site 4: `hcp hollow`** (3개 Al 원자 사이의 중공 자리 중, 바로 아래 2층 Al 원자가 존재하는 자리)

---

## 3. PC2 성능 맞춤형 문서 체계 목차
본 폴더(`Step_A3_Dual4090_Execution_Plan`)에 수록된 6대 운영 문서는 PC2의 구체적인 하드웨어 한계와 성능을 100% 활용하도록 구성되었습니다:

- **[[00_A3_MASTER_EXECUTION_OVERVIEW.md]]**: 전체 연구 목표, 선행 성과, 4대 사이트 개요
- **[[01_HARDWARE_CAPACITY_AND_ALLOCATION_MATRIX.md]]**: Dual RTX 4090 VRAM 48GB, 128GB RAM, OMP 16스레드 제한, MPI GPU 바인딩 최적화
- **[[02_DFT_DECK_CONFIGURATION_GUIDE.md]]**: `conv_thr=1.0E-6 Ry`, `mixing_beta=0.05` 전하 진동 방지 덱 파라미터 표준
- **[[03_AUTONOMOUS_SUPERVISOR_RECOVERY_PROTOCOL.md]]**: `adaptive_recovery_supervisor` 연계 무중단 자동 복구 및 상태 전이도
- **[[04_ADSORPTION_THERMODYNAMICS_CALCULATION_GUIDE.md]]**: 흡착 에너지($E_{\text{ads}}$) 수식 및 열역학적 안정성 판정 기준
- **[[05_STEP_A3_RUNNER_SCRIPTS_SPECIFICATION.md]]**: 백그라운드 무중단 배치 스크립트 및 모니터링 명령어
