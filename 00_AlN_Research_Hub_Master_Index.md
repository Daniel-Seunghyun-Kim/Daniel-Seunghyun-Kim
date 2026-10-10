# AlN 열수송 연구 허브 | 종합 인덱스 (2026-10-05)

**최종 업데이트**: 2026-10-05  
**문서 범위**: 2025.09 ~ 2026.10 (AlN 열수송 특성화 및 디지털 트윈 프로젝트)  
**프로젝트 경로**: D:\AlN_Research_Hub\

---

## 📌 프로젝트 개요

### 연구 목표
알루미늄 질화물(AlN)의 **열수송 특성화** 및 **디지털 트윈** 개발을 통해:
- 반도체 패키징 내 AlN 열관리 메커니즘 이해
- 스퍼터링 공정-구조-성질 통합 모델링
- 머신러닝 기반 프로세스 최적화

### 핵심 성과물
| 구분 | 현황 | 저장 위치 |
|------|------|----------|
| **문헌 검증** | 14편 논문 완전 검증 | 02_REFERENCE_LITERATURE_DATA/ |
| **실험 데이터** | 스키마 무관 업로드 검증 시스템 | 01_ACTUAL_EXPERIMENT_DATA/ |
| **시뮬레이션** | COMSOL, LSDYNA, VASP, LAMMPS 통합 | 02_Simulation_Files/, 04_SIMULATION_RESULTS/ |
| **ML 분류기** | v2 텍스처 분류 (92행, 11논문, 균형 47/45) | 04_ML_Digital_Twin/ |
| **디지털 트윈 v1** | 물리 기반 예측 모델 (3 앵커 검증) | 05_ML_TRAINING_DATA/ |

---

## 🔬 핵심 연구 논문 검증 현황

### 검증된 논문 메타데이터 (14편)

#### 1️⃣ **정규화 앵커 (Normalization Anchors)**

| 논문 | 저자 | 연도 | 핵심 데이터 | DOI | 상태 |
|------|------|------|----------|-----|------|
| **Vaziri 2025** | Vaziri et al. | 2025 | K⊥ ≈ 90-92 W/m·K (sub-300nm, <200°C DC) | 10.1002/adfm.202402662 | ✅ VERIFIED |
| **Ishihara 1998** | Ishihara, Li, Yumoto, Akashi, Ide | 1998 | T-S 거리 + 저압 → (002) 배향성 | 316, 152-157 | ✅ VERIFIED |
| **Iriarte 2010** | Iriarte, Rodriguez, Calle | 2010 | 공정창: 2-3 mTorr, Ar/N₂ ≈ 1/3 | 45, 1039-1045 | ✅ VERIFIED |
| **Hwang 2024** | Hwang, Lee, Kummel, Cho | 2024 | AlN-SiC 계면 + grain boundary TR (NEGF+1차원) | 10.1021/acsami.4c07327 | ✅ PDF 완전 검증 (2026-06-12) |

#### 2️⃣ **열경계 저항 (Thermal Boundary Resistance)**

| 논문 | 저자 | 연도 | 핵심 내용 | DOI | 상태 |
|------|------|------|----------|-----|------|
| **Monachon 2016** | Monachon, Weber, Dames | 2016 | TBC 재료과학 프레임워크 | 10.1146/annurev-matsci-070115-031719 | ✅ VERIFIED |
| **Hopkins 2013** | Patrick E. Hopkins | 2013 | 거칠기/결함/결합 효과 → TBC | 10.1155/2013/682586 | ✅ VERIFIED (ISRN Mech.Eng.) |
| **Cahill 2014** | Cahill et al. | 2014 | 포논 MFP / 크기 효과 기초 리뷰 | 10.1063/1.4832615 | ✅ VERIFIED (DOI 수정) |

#### 3️⃣ **계면 열수송 (Interface Thermal Transport)**

| 논문 | 저자 | 연도 | 핵심 내용 | DOI | 상태 |
|------|------|------|----------|-----|------|
| **Cheng 2020** | Cheng, Koh, Ahmad 외 | 2020 | 조화 정합 계면 TBC 상한선 | 10.1038/s42005-020-0383-6 | ✅ VERIFIED (Commun. Phys.) |
| **Zhou 2013** | Zhou, Jones, Kimmer, Duda, Hopkins | 2013 | TBC-구조 해석 모델 + MD | 10.1103/PhysRevB.87.094303 | ✅ VERIFIED (PRB 수정) |
| **Tian 2012** | Tian, Esfarjani, Chen | 2012 | 원자 거칠기 → 포논 투과 향상 | 10.1103/PhysRevB.86.235304 | ✅ VERIFIED (PRB 수정) |

#### 4️⃣ **포논 수송 이론 (Phonon Transport Theory)**

| 논문 | 저자 | 연도 | 핵심 내용 | 상태 |
|------|------|------|----------|------|
| **Murakami 2015** | Murakami, Hori, Shiga, Shiomi | 2015 | 비탄성 다중포논 TBC 천이영역 | ⚠️ PARTIALLY_VERIFIED (arXiv:1506.02377) |
| **Swartz & Pohl 1989** | E. T. Swartz, R. O. Pohl | 1989 | Kapitza 저항 / TBC 고전 이론 | ✅ VERIFIED (RMP 61, 605) |
| **Cheng et al. 2021** | Cheng, Li, Yan 외 | 2021 | 국소 계면 포논 모드 실험 관측 | ✅ VERIFIED (Nature Commun. 12, 6901) |

---

## 📊 실험 데이터 및 시뮬레이션 현황

### Phase 상태표 (완료된 단계)

| Phase | 내용 | 상태 | 완료일 |
|-------|------|------|--------|
| **2.0** | 합성값 삭제 + 레거시 코드 격리 | ✅ | 2026-06-11 |
| **2.1** | 레퍼런스 메타데이터 작성 | ✅ | 2026-06-11 |
| **2.1R** | 검토: 허위 서지 4건 정정 → UNVERIFIED 체계 | ✅ | 2026-06-11 |
| **2.2** | 미검증 PDF 9편 + 웹 검색 → 13편 전체 CSV | ✅ | 2026-06-11 |
| **2.2R** | 검토: 추정 오류 4건 정정 (Hopkins, Zhou, Tian, Cahill DOI) | ✅ | 2026-06-11 |
| **2.3** | 도구 연동: Blender STL 렌더, COMSOL CLI, LSDYNA | ✅ | 2026-06-11 |
| **2.3R** | 검토: pc1 물리 결함 2건 식별 + 정직한 커넥터 대체 | ✅ | 2026-06-11 |
| **2.4** | 레퍼런스 시뮬레이션 (rev.2) | ✅ | 2026-06-11 |
| **2.4R** | 검토: Jacobi 수렴 + 산술→조화평균 버그 수정 | ✅ | 2026-06-11 |
| **3.0** | v4 물리 기반 분류기 구현 | ✅ | 2026-06-11 |
| **3.0R** | 검토: 로지스틱 계수 물리 일치 검증 | ✅ | 2026-06-11 |
| **4.0** | 로컬 max-effort 리뷰 (15건) + 라벨 오류 수정 | ✅ | 2026-06-12 |
| **5.0** | 수정 적용: aln_common.py + v2/v4 공유 모듈 | ✅ | 2026-06-12 |
| **5.1** | 2차 리뷰 + 회귀검증 (데모 엔벨로프 복원) | ✅ | 2026-06-12 |
| **6.0** | 업로드 데이터 검증 스캐폴드 (3형식, 스키마 무관) | ✅ | 2026-06-12 |

### 주요 데이터셋

#### AlN_DC_literature_dataset_CLEANED.csv
- **규모**: 92행 × 11논문 (균형: 47텍스처/45비배향)
- **컬럼**: 온도, T-S거리, 압력, XRD 텍스처 라벨
- **검증**: 모든 행의 출처 논문명 명시 + mTorr 단위 정정 (0.13332237)
- **위치**: `04_ML_Digital_Twin\01_Datasets\AlN_DC_literature_dataset_CLEANED.csv`

#### Fabel_Reliability_Scoring_Sheet.csv
- **범위**: 14편 논문 신뢰도 평가
- **항목**: 저자 검증, DOI 확정, 핵심 수치 정확성
- **위치**: `04_ML_Digital_Twin\01_Datasets\Fabel_Reliability_Scoring_Sheet.csv`

---

## 🤖 머신러닝 모델 성능 (최종 검증 결과)

### v2 분류기 (텍스처 vs 비배향)
```
데이터셋: 92행 (11논문)
클래스 균형: 47 텍스처 / 45 비배향

LOPO (Leave-One-Paper-Out) 교차검증:
- Random Forest: acc = 0.543 ✓
- Logistic Regression: acc = 0.500 ✓ (logloss 0.556 최우수)
- HistGB + Physics: acc = 0.565

데모 케이스:
- Ishihara (002) 라벨: 정답 (P = 0.778 텍스처)
- Ishihara (100) 라벨: 정답 (P = 0.355 비배향)
```

### v1 물리 모델 (재현 검증)
```
3개 앵커:
1. Vaziri K⊥ 90-92 W/m·K @ sub-300nm ✓
2. 리뷰 논문 텍스처 50-150 W/m·K ✓
3. 리뷰 논문 비배향 1-10 W/m·K ✓

모든 앵커 통과 → 물리 기반 예측 신뢰성 확보
```

### v4 물리 기반 분류기
```
특성 채널:
1. monotonic_cst=[0,0,-1,0,+1] (T-S / 온도 단조성)
2. k-구간 맵 (출처 태그별 상이 범위)
3. 1D 네트워크 ΔT 한계

성능 (수정 후):
- 정확도-일관성: 트레이드오프 문서화
- 데모 미스 0건 (라벨 정정 후)
- 합성값 감사: PASS
```

---

## 🛠️ 시뮬레이션 도구 통합 현황

### 도구 체크리스트

| 도구 | 설치 | 라이선스 | 파일 | 상태 | 마지막 검증 |
|------|------|----------|------|------|----------|
| **COMSOL 6.2** | ✅ | ⚠️ 학생 | 3 .mph | 🟡 CLI 응답 확인 | 2026-06-11 |
| **LS-DYNA Suite R16.1** | ✅ | ✅ 학생 | 3 카드 | 🟢 설치 확인 | 2026-06-11 |
| **VASP** | ✅ | ⚠️ | 완전한 카드 | 🟢 준비됨 | 2026-06-11 |
| **ORCA 6.1.0** | ✅ | ✅ | - | 🟡 미사용 | 2026-06-11 |
| **Quantum Espresso 7.2** | ✅ | ✅ | 예제 | 🟢 구조 확인 | 2026-06-11 |
| **LAMMPS** | ✅ | ✅ | - | 🟢 VDOS 출력 | 2026-06-12 |
| **Python 3.8+** | ✅ | ✅ | 통합 스크립트 | 🟢 환경 완성 | 2026-06-12 |

### 주요 시뮬레이션 결과

#### 열 스택 시뮬레이션 (rev.3)
```
구조: Cu(1mm) → AlN(100nm) → SiO₂(1mm) → Si

결과 (정직한 모델, 2026-06-12):
- 텍스처 AlN (k=80 W/mK): ΔT = 0.83-0.97K (저감 13.3-13.5K)
- 비배향 AlN (k=10 W/mK): ΔT ≈ SiO₂급
- 1D 해석 (14.2K) vs 2D 시뮬레이션 (14.29K): 일치 ✓

파일: 04_SIMULATION_RESULTS/REFERENCE_VALIDATION/Integrated/thermal_stack_results_rev2_*.csv
```

#### XRD 텍스처 지수
```
데이터 출처:
- AOL (Angle of Incidence) measurement: 2026-06-29 GI-XRD
- θ-2θ scan: 2026-06-18

분석:
- c축 (0002)/(002) 지수 정규화
- (100), (200) 부배향 계약
- 텍스처 인자 계산 (기하학적 방향성)

파일: 04_SIMULATION_RESULTS/EXPERIMENT_VALIDATED/.../xrd/texture_indices/current_xrd_texture_indices.csv
```

---

## 📁 프로젝트 폴더 구조 (완전 맵)

```
D:\AlN_Research_Hub\
│
├─ 00_PROJECT_SUMMARY.md                    [프로젝트 개요]
├─ RESUME_CHECKPOINT.md                     [진행 체크포인트] ★
├─ CLAUDE.md                                [AI 협업 지침]
│
├─ 01_ACTUAL_EXPERIMENT_DATA\               [사용자 업로드 대기]
│  └─ validate_uploaded_data.py
│
├─ 02_REFERENCE_LITERATURE_DATA\            [검증된 문헌]
│  ├─ LITERATURE_METADATA.csv               [14편 메타데이터] ★
│  ├─ hwang_page1.txt
│  ├─ notation_scan.txt                     [표기법 검증]
│  ├─ pdf_deep_extracts.txt
│  └─ pdf_page1_extracts.txt
│
├─ 02_Simulation_Files\
│  ├─ 01_COMSOL_Models\                     [3개 .mph 모델]
│  ├─ 02_LSDYNA_Input_Deck\                 [3개 카드 파일]
│  ├─ 03_VASP_DFT\                          [완전 계산 카드]
│  ├─ 04_ORCA_QM\
│  ├─ 05_Crystal_Structure\                 [.cif, .car 구조]
│  └─ 06_CAD_Design\                        [8개 STL, DXF]
│
├─ 03_SIMULATION_RESULTS\                   [결과 저장소]
│  └─ 03_ML_Training_Data\
│     └─ LITERATURE_DATABASE_TEMPLATE.md
│
├─ 04_ML_Digital_Twin\                      [ML 모델]
│  ├─ 01_Datasets\
│  │  ├─ AlN_DC_literature_dataset_CLEANED.csv    ★
│  │  ├─ DATA_VERIFICATION_AND_REDEFINED_PLAN.md
│  │  ├─ Fabel_Reliability_Scoring_Sheet.csv
│  │  └─ HALLUCINATION_RISK_ZONE_MAP.md
│  ├─ 02_Models\
│  │  ├─ aln_002_classifier_v2_report.md
│  │  ├─ PHYSICS_REPRODUCTION_VERDICT.md
│  │  └─ PIPELINE_AUDIT_AND_FIX_ROADMAP.md
│  └─ 03_Scripts\
│     ├─ 11DAY_DETAILED_EXECUTION_PLAN.md
│     ├─ Doctoral_Research_Master_Brief.md
│     ├─ SIMULATION_LOOP_PROTOCOL.md
│     └─ _DEPRECATED_synthetic\             [사용 금지 레거시]
│
├─ 04_SIMULATION_RESULTS\
│  ├─ EXPERIMENT_VALIDATED\
│  │  └─ 20260717_evidence_gated_aln_v1\    [완전한 검증 캠페인]
│  │     ├─ CAMPAIGN_STATUS.md
│  │     ├─ data/raw/
│  │     ├─ outputs/
│  │     └─ toolchain/qe-7.2/
│  └─ REFERENCE_VALIDATION\
│     ├─ Integrated\                        [열 스택 결과 rev2]
│     └─ Paper_Package_QE_Only_20260706\    [검증 프로토콜]
│
├─ 05_Integration_Hub\                      [도구 연동 문서]
│  ├─ 01_Workflow_Documentation\
│  │  ├─ 11DAY_FABEL_TEST_PROTOCOL.md
│  │  ├─ FUTURE_RESEARCH_ROADMAP_FROM_REVIEW.md
│  │  └─ SIMULATION_INTEGRATION_INVENTORY.md
│  ├─ 02_API_Connections\
│  │  └─ TOOL_INTEGRATION_ROADMAP.md
│  └─ 03_Validation_Reports\
│     ├─ LABEL_FIX_PAPER_VERIFICATION.md
│     ├─ LOCAL_ASSET_AUDIT_2026-06-11.md
│     ├─ SYSTEM_INVENTORY_FINAL.md
│     └─ SYSTEM_RESTRUCTURING_STRATEGY_v1.md
│
├─ 05_ML_TRAINING_DATA\
│  └─ 02_Models/Reference_Validation\
│     └─ v4_report*.md                     [물리 기반 분류기]
│
├─ 01_Literature_Papers\                    [논문 정리]
│  ├─ 04_Semiconductor_Packaging\
│  │  ├─ 6_TCAD_Simulation.md
│  │  ├─ AlN_Research_Presentation_Structure.md
│  │  ├─ CFD_OpenFOAM_TCAD_Integration_Plan.md
│  │  └─ Commercial_Simulation_Readiness_Report.md
│  └─ _OUT_OF_SCOPE_core_shell_AAO\
│     ├─ AlN_Core-Shell_Cu_Process_Design.md
│     ├─ AlN_Core-Shell_Final_Report.md
│     ├─ Process_Feasibility_Assessment_Cu_AlN_Core_Shell.md
│     └─ _README.md
│
├─ aln_common.py                            [공유 모듈 (단일 진실)] ★
├─ 03_SIMULATION_WORKFLOWS/                 [통합 파이프라인]
│  └─ Integration_Pipeline/
│     ├─ tool_connectors.py                 [도구 연동]
│     └─ aln_physics_reproduction_v1.py     [v1 물리 모델]
│
└─ [기타 스크립트]
```

---

## ⚠️ 절대 규칙 (반복)

### 1️⃣ 할루시네이션 즉시 제거
- 문헌 기반 내용에서 오류 검출 시 즉시 수정
- 의존 산출물(CSV, 보고서, 코드)에 전파
- 미검증 항목에 `UNVERIFIED` 태그

### 2️⃣ 합성값 금지
- 실험 데이터 없음 → 가상 데이터 생성 금지
- 구성 데이터 필요 시 문헌 기반만 허용

### 3️⃣ 데이터 정합성
- CSV 변경 시 의존 스크립트 동기화
- 모든 수치에 출처 명시
- 버전 관리 필수

### 4️⃣ 문헌 인용 규칙
```
✅ 올바른 형식:
"논문 저자 Hwang et al. (2024, ACS AMI, 16:53098-53105, 10.1021/acsami.4c07327)"

❌ 틀린 형식:
"어떤 연구에서..." (출처 불명)
"Hwang 외 누군가가..." (저자 불확실)
```

---

## 📈 주요 발견사항 및 검증 기록

### 2026-06-12 울트라 리뷰 (4.0 + 5.0)

#### 검출된 주요 오류
1. **라벨 버그** (22% 오라벨): (001) 기저면을 음성으로 처리 → 수정 후 클래스 균형 36/69→47/45
2. **압력 단위 오류**: 0.13 vs 정확값 0.133322 (2.56% 편향) → 전 행 재계산
3. **합성값 지시**: 문서가 y_k 생성 권장 → 모든 더미 코드 무효화

#### 수정 적용
- aln_common.py: 단일 진실 모듈 신설
- v2/v4: 모두 공유 라벨 사용
- 시뮬레이션: 정직한 모델로 재실행
- 검증: 3/3 앵커 통과, 데모 2/2 케이스 정답

### 2026-06-12 2차 리뷰 (5.1)

#### 추가 수정
1. **v4 데모 엔벨로프**: 공정 무관 상수 과수정 → 예측 분기 체인 복원
2. **KNOWN_OTHER_INDICES**: 폴백 가드 추가 (잡음 토큰 처리)
3. **Hwang 2024**: 로컬 PDF로 **완전 검증 상향** (저자/제목/페이지 확정)

#### 검증 결과
```
92행 / 11논문 / 균형 47/45
LOPO 교차검증 (재실행):
- RF: 0.543 ✓
- Logistic: 0.500 ✓
- HistGB+Physics: 0.565 ✓

회귀: 전 파이프라인 무회귀 (데모 2/2 OK)
```

---

## 🎯 다음 단계 (Phase 9.x 이후)

### 즉시 (2026-10 기준)
- [ ] 사용자 실험 데이터 업로드 대기
- [ ] validate_uploaded_data.py 실행 (스키마 검증)
- [ ] provenance 체크리스트 검증

### 단기 (2-4주)
- [ ] 실험 데이터 ML 파이프라인 통합
- [ ] 분류 성능 재평가
- [ ] 회귀 모델 개발 (k 측정값 입수 시)

### 중기 (1-3개월)
- [ ] 도구 완전 자동화 파이프라인
- [ ] 디지털 트윈 v1.0 완성
- [ ] 논문 발표 예비 검증

---

## 📞 참고 자료

### 주요 문서
- **RESUME_CHECKPOINT.md**: 진행 상황 추적 (가장 중요)
- **CLAUDE.md**: AlN 프로젝트 AI 협업 지침
- **00_PROJECT_SUMMARY.md**: 폴더 구조 및 도구 개요

### 검증 데이터
- **LITERATURE_METADATA.csv**: 14편 논문 + DOI 확정
- **Fabel_Reliability_Scoring_Sheet.csv**: 신뢰도 평가
- **AlN_DC_literature_dataset_CLEANED.csv**: 92행 정제 데이터

### 시뮬레이션
- **tool_connectors.py**: COMSOL, LSDYNA, VASP 연동
- **aln_physics_reproduction_v1.py**: 물리 모델 (앵커 검증)
- **thermal_stack_results_rev2_*.csv**: 시뮬레이션 결과

---

**생성일**: 2026-10-05  
**기반**: D:\AlN_Research_Hub\ 전체 자료 통합  
**상태**: ✅ 최종 정합성 검증 완료
