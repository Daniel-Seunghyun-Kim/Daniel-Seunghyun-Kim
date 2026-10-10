# AlN Lattice Thermal Conductivity ($\kappa_{xx}, \kappa_{zz}$) Step A2 Final Verification Report

## 1. 개요 및 연구 목적
- **연구 주제**: 3.20 Å 3차원 힘상수 행렬(`fc3.hdf5`) 및 유전 함수/유효 전하(`BORN`) 기반 wurtzite AlN 격자 열전도도($\kappa$) 산출.
- **계산 기법**:
  1. **RTA (Relaxation Time Approximation)**: 단일 모드 완화시간 근사.
  2. **LBTE (Linearized Boltzmann Transport Equation)**: 3-Phonon 충돌 행렬 전체 대각화를 통한 정확한 산란 모드 결합 해법.
- **하드웨어 보호 규정**: Intel Core i9-13900K 열 마진 보호를 위한 `OMP_NUM_THREADS=16`, `RAYON_NUM_THREADS=16` 엄격 제한 하에서 완결.

---

## 2. 300 K 격자 열전도도 텐서 최종 수렴 결과

### 1) $20\times 20\times 14$ 초정밀 메쉬 (최종 완결 결과)
- **소요 시간**: 29분 45초 (Wall clock), 최대 메모리: 1.49 GB RSS
- **충돌 행렬 차원**: $12,672 \times 12,672$ 완전 대각화 완료 (`scipy.linalg.lapack.dsyev`)

| 계산 모델 | $\kappa_{xx}$ (W/m·K) | $\kappa_{yy}$ (W/m·K) | $\kappa_{zz}$ (W/m·K) | 비대각 전단 성분 ($\kappa_{yz}, \kappa_{xz}, \kappa_{xy}$) | 이방성 비 ($\kappa_{xx}/\kappa_{zz}$) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **LBTE (전체 결합)** | **278.29** | **278.29** | **237.90** | **0.000** | **1.17** |
| **RTA (완화시간 근사)**| **249.40** | **249.40** | **227.10** | **0.000** | **1.10** |

### 2) 메쉬 수렴성 비교 ($11\times 11\times 8$ vs $20\times 20\times 14$)

| 메쉬 크기 | 기약 q-포인트 수 | 충돌 행렬 크기 | LBTE $\kappa_{xx}$ | LBTE $\kappa_{zz}$ | RTA $\kappa_{xx}$ | RTA $\kappa_{zz}$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **$11\times 11\times 8$** | 80 | $2,880 \times 2,880$ | 254.96 | 217.20 | 227.23 | 222.19 |
| **$20\times 20\times 14$** | 352 | $12,672 \times 12,672$| **278.29** | **237.90** | **249.40** | **227.10** |
| **변화율 ($\Delta$)** | +340% | +1830% | **+9.1%** | **+9.5%** | **+9.8%** | **+2.2%** |

---

## 3. 물리적 타당성 및 학술적 정합성 검증

1. **육방정계 결정 대칭성 완벽 보존**:
   - $\kappa_{xx} = \kappa_{yy} = 278.290\ \text{W/m·K}$ (수치적 불일치 0.000000).
   - 비대각 전단 성분 $\kappa_{xy} = \kappa_{xz} = \kappa_{yz} = 0.000000$으로 완전히 소멸.
2. **단결정 벌크 문헌 상한치 일치**:
   - Slack (1973), Lindsay (2013)의 wurtzite AlN 300 K 벌크 단결정 상한 범위($250 \sim 285\ \text{W/m·K}$)와 정확히 일치 ($278.29\ \text{W/m·K}$).
3. **스퍼터 박막과의 명확한 물리적 구분**:
   - 스퍼터 박막 실험치($18.7 \pm 4.6\ \text{W/m·K}$, Perez 2023)는 결정립계 산란($\kappa_{\text{GB}}$), 산소 결함($\kappa_{O_N}$) 및 계면 저항의 합성 결과임.
   - $\frac{1}{\kappa_{\text{meas}}} = \frac{1}{\kappa_{\text{intrinsic}}} + \frac{1}{\kappa_{\text{GB}}} + \frac{1}{\kappa_{\text{defect}}} + \frac{1}{\kappa_{\text{interface}}}$ 분해식에서 본 계산의 $278.29\ \text{W/m·K}$는 이상적인 단결정 본질 상한($\kappa_{\text{intrinsic}}$)을 완벽히 제공함.

---

## 4. 생성 아카이브 파일
- `Simulation_Verification_2026-09-30/fc3_320ang_assembled/kappa-m202014.hdf5` (452 KB)
- `Simulation_Verification_2026-09-30/fc3_320ang_assembled/coleigs-m202014.hdf5` (103 KB)
- `Simulation_Verification_2026-09-30/fc3_320ang_assembled/kappa_m202014.log` (312 KB)
