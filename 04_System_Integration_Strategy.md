# 시스템 통합 전략 | AlN 연구 허브 자동화

**최종 업데이트**: 2026-06-12  
**범위**: 도구 연동, 데이터 파이프라인, 디지털 트윈 아키텍처  
**목표**: 엔드-투-엔드 자동화 (Phase 9.x 이후)

---

## 📌 전략 개요

### 3단계 로드맵

```
Phase 1 (현재 - 2주): 도구 검증 & 기본 파이프라인
  └─ 목표: 각 도구 독립 작동 확인
  
Phase 2 (2-4주): 중앙 통합 파이프라인
  └─ 목표: COMSOL ↔ Python ↔ VASP 데이터 흐름
  
Phase 3 (1개월+): 완전 자동화 & 디지털 트윈 v1.0
  └─ 목표: 공정 매개변수 입력 → 열특성 예측
```

---

## 🔧 도구 연동 (현황)

### 통합 모듈: tool_connectors.py

```python
# 위치: 03_SIMULATION_WORKFLOWS/Integration_Pipeline/

# 1. COMSOL 연동
class COmsolConnector:
    def __init__(self, mph_path):
        self.mph_path = mph_path
    
    def export_to_csv(self):
        # .mph → Python으로 후처리
        # T, Q_flux 분포 추출
        # CSV 저장
        pass
    
    def cli_batch_run(self, param_dict):
        # COMSOL CLI로 배치 실행
        # 매개변수 스윕 자동화
        pass

# 2. LSDYNA 연동
class LSDynaConnector:
    def __init__(self, lsdyna_path, input_deck):
        self.solver = lsdyna_path
        self.deck = input_deck
    
    def generate_cards(self, thickness, k_tensor):
        # 재료 특성 → 입력 카드 생성
        # 메시, 경계조건, 출력 설정
        return card_file
    
    def run_solver(self):
        # subprocess로 lsdyna 실행
        # 결과: DYNOUT, D3PLOT
        pass

# 3. VASP 연동
class VASPConnector:
    def load_poscar(self):
        # 구조 로드
        pass
    
    def setup_kpoints(self, grid=[8,8,8]):
        # k점 격자 생성
        pass
    
    def run_convergence(self):
        # 수렴 테스트 자동화
        pass

# 4. Python 데이터 처리
class DataPipeline:
    def collect_results(self):
        # 모든 도구 출력 수집
        results = {
            'comsol': self.comsol_export(),
            'lsdyna': self.lsdyna_results(),
            'vasp': self.vasp_output(),
        }
        return results
    
    def integrate_dataset(self):
        # 통합 CSV 생성
        # [T, S, P, k, ΔT, stress, ...] 행렬
        pass
    
    def train_ml_model(self, data):
        # v2/v4 재훈련
        # LOPO 검증
        pass
```

### 도구별 상태

#### COMSOL

```
현황:
  ✅ .mph 파일 3개 (inspect, inspect_out, output_Model)
  ✅ CLI 인터페이스 응답 확인
  ⚠️ 라이선스: 학생/학교 (2026년 유효)
  
연동 방법:
  1. COMSOL CLI로 .mph 실행
     $ comsol -inputfile model.mph -outputfile result.mph
  
  2. 결과 CSV 내보내기
     - T 분포: domain, evaluated values
     - Q_flux: 계면별 열플럭스
  
  3. Python 후처리
     - ΔT 통계 (min, max, mean)
     - 열경로 분석
     
검증:
  ✅ 모델 형상 (geometry) 로드 가능
  ✅ 메시 생성 확인
  ⚠️ 실제 솔버 실행은 라이선스 필요
```

#### LS-DYNA

```
현황:
  ✅ 카드 파일 3개 (계면, 식각, 벌크 테스트)
  ✅ 솔버 설치됨 (Suite R16.1 Student, 260MB)
  ⚠️ 매개변수 스윕 자동화 미완
  
파일 위치:
  D:\lsdyna\ls-dyna_smp_d_R16.1_180-*_studentversion.exe (SMP, double precision)
  D:\lspp\lsprepost4.12.exe (전/후처리)

연동 전략:
  1. 기본 카드 템플릿 수정
     ```
     *KEYWORD
     *MATERIAL_99_ELASTIC
     RHO, E1, E2, E3, G12, G23, G13, (AlN 재료 특성)
     
     *PART_COMPOSITE_...
     (메시 ID, 재료 ID, 방향)
     ```
  
  2. 매개변수 → 카드 자동 생성
     def generate_lsdyna_deck(T, S, P):
         k = predict_k(T, S, P)  # v2 분류기 사용
         E_tensor = k_to_elastic(k)  # 등방성 가정
         return card_template.format(E_tensor)
  
  3. 배치 실행
     for param in param_sweep:
         deck = generate_lsdyna_deck(*param)
         run_lsdyna(deck)
         extract_stress_strain()
```

#### VASP

```
현황:
  ✅ POSCAR, INCAR, KPOINTS 완성
  ✅ 구조 검증 (격자상수 ±0.5%)
  ⚠️ 라이선스 체크 (학교 기간 확인)
  
실행 방법:
  Option 1: Docker (권장)
    $ docker build -f Dockerfile .
    $ docker run -v $(pwd):/workdir image_name vasp
  
  Option 2: HPC 클러스터
    $ sbatch vasp_job.sh (SLURM)
  
  Option 3: 로컬 (slow)
    $ mpirun -n 16 vasp
    (여러 시간 소요)
  
결과 처리:
  OUTCAR → 총 에너지, 응력 텐서
  CONTCAR → 이완 후 원자 좌표
  
Python 통합:
    from ase.io import read
    atoms = read('CONTCAR')
    stress_tensor = parse_outcar()
    save_to_csv()
```

---

## 📊 데이터 파이프라인

### 단계별 데이터 흐름

```
┌─────────────────┐
│ 공정 매개변수   │  (T, S, P)
│ 입력            │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ v2 분류기      │  → 텍스처 확률 P(texture)
│ (ML 모델)       │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ 물리 모델      │  → k 구간 예측
│ (v1 재현)       │  → XRD 기하학
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ 1D 열 모델     │  → ΔT 계산
│ (해석 및 1D)    │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ 2D COMSOL      │  → 온도 분포
│ (유한요소)      │  → 스프레딩 효과
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ LSDYNA         │  → 응력 분포
│ (열-구조 연동)  │  → 계면 파괴 지수
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ 결과 통합      │  → CSV/JSON
│ (데이터베이스)  │  → 대시보드
└─────────────────┘
```

### CSV 구조 (통합 데이터셋)

```
integrated_dataset.csv

컬럼:
  # 입력 (공정)
  temperature_C
  ts_distance_cm
  pressure_mtorr
  
  # 예측 (ML)
  texture_probability
  k_min_w_mk
  k_max_w_mk
  
  # 계산 (열)
  delta_t_1d
  delta_t_2d
  heat_flux
  
  # 구조 (응력)
  max_stress_pa
  interface_traction
  
  # 검증
  source_paper
  confidence_score
  
행 수: 초기 92 (문헌) → 최대 1000 (확장 시나리오)
```

---

## 🤖 디지털 트윈 아키텍처 (v1.0)

### 컴포넌트 설계

```
┌─────────────────────────────────────────────┐
│  Digital Twin v1.0 - AlN 열수송 특성화     │
└─────────────────────────────────────────────┘

1️⃣ 데이터 계층 (Data Layer)
   ├─ 입력 데이터베이스
   │  └─ 공정 매개변수 (T, S, P)
   │  └─ 재료 속성 (k, ρ, c_p)
   │  └─ 구조 정보 (두께, 기하)
   │
   ├─ 결과 캐시
   │  └─ ML 예측값
   │  └─ FEA 시뮬레이션 결과
   │  └─ 성능 지표 (ΔT, 응력)
   │
   └─ 실시간 데이터
      └─ 온도 센서 (실제 실험)
      └─ 성능 피드백

2️⃣ 모델 계층 (Model Layer)
   ├─ 머신러닝
   │  ├─ v2 분류기 (텍스처 예측)
   │  ├─ v4 물리 기반 분류
   │  └─ 회귀 모델 (k 예측, 향후)
   │
   ├─ 물리 시뮬레이션
   │  ├─ 1D 열 해석
   │  ├─ 2D COMSOL 유한요소법
   │  └─ 응력 예측 (LSDYNA)
   │
   └─ 통계 모델
      └─ 불확실성 정량화 (Bayesian)

3️⃣ 최적화 계층 (Optimization Layer)
   ├─ 공정 설계
   │  └─ 공정 창 탐색 (T, S, P 그리드)
   │  └─ 제약 조건 (k > 50 W/m·K 등)
   │
   ├─ 활동 학습 (Active Learning)
   │  └─ 불확실성 높은 영역 식별
   │  └─ 실험 제안 생성
   │
   └─ 다목적 최적화 (Pareto)
      └─ k 최대화 vs 비용 최소화

4️⃣ 인터페이스 계층 (Interface Layer)
   ├─ 웹 API
   │  └─ REST 엔드포인트
   │     POST /predict → {"T": 300, "S": 5, "P": 1}
   │     GET /results → {"k": 80, "ΔT": 14.3, ...}
   │
   ├─ 대시보드
   │  └─ 공정 조건 입력 UI
   │  └─ 실시간 성능 모니터링
   │  └─ 예측 불확실성 시각화
   │
   └─ 데이터 내보내기
      └─ CSV/JSON
      └─ 보고서 생성
```

### 구현 스택

```
백엔드:
  - Python 3.10+
  - Flask/FastAPI (API)
  - scikit-learn, XGBoost (ML)
  - FEniCS (유한요소)
  - Pandas, NumPy

데이터베이스:
  - SQLite (로컬) 또는 PostgreSQL (클라우드)
  - 스키마: processes, simulations, results, experiments

프론트엔드:
  - React / Vue (웹 UI)
  - Plotly / D3.js (시각화)
  - Jupyter Notebook (분석)

배포:
  - Docker (컨테이너화)
  - Kubernetes (확장)
  - 클라우드: AWS / Google Cloud
```

---

## 📈 성능 벤치마크

### 실행 시간 예상

| 단계 | 도구 | 시간 | 병렬화 |
|------|------|------|--------|
| **1D 열 해석** | Python | 1초 | ✅ 병렬화 가능 |
| **2D COMSOL** | FEA | 10-60초 | ⚠️ 라이선스 제한 |
| **응력 계산** | LSDYNA | 30-180초 | ✅ MPI 병렬화 |
| **ML 예측** | scikit-learn | 0.1초 | ✅ GPU 가속 가능 |
| **포논 계산** | VASP | 1-4시간 | ✅ HPC 클러스터 |

### 정확도 목표

```
LOPO 교차검증 (92행 데이터셋):
  ├─ 텍스처 분류: Accuracy ≥ 0.70 (현재 0.565-0.543)
  ├─ k 예측: R² ≥ 0.80 (미개발, 향후)
  └─ ΔT 시뮬레이션: 상대오차 < 10% (현재 1D/2D 일치)

실험 데이터 추가 후:
  ├─ 내삽 (interpolation): MAE < 5% k
  ├─ 외삽 (extrapolation): 신뢰도 <50%
  └─ 재현성: 동일 공정 반복 시 σ < 10%
```

---

## 🎯 다음 단계 (로드맵)

### 즉시 (2주)
- [ ] tool_connectors.py 완성
  - [ ] COMSOL CLI 배치 실행 테스트
  - [ ] LSDYNA 카드 자동 생성
  - [ ] 결과 CSV 통합

- [ ] 데이터 파이프라인 프로토타입
  - [ ] 공정 입력 → 예측 → CSV 저장
  - [ ] 오류 처리 & 로깅

### 단기 (4주)
- [ ] 웹 API 프로토타입 (Flask)
  - [ ] POST /predict 엔드포인트
  - [ ] GET /results 조회

- [ ] 대시보드 초판 (Jupyter + Plotly)
  - [ ] 공정 매개변수 입력 위젯
  - [ ] 예측 결과 시각화

### 중기 (2개월)
- [ ] 실험 데이터 통합
  - [ ] validate_uploaded_data.py 실행
  - [ ] ML 모델 재훈련

- [ ] 불확실성 정량화
  - [ ] Bayesian Neural Network
  - [ ] 신뢰도 구간 계산

### 장기 (6개월)
- [ ] 디지털 트윈 v1.0 완성
- [ ] 클라우드 배포 (AWS/GCP)
- [ ] 활동 학습 루프 운영

---

## ⚠️ 주의사항 & 제약

### 기술적 제약

1. **라이선스 의존성**
   - COMSOL, VASP: 학교 라이선스 필요
   - 대안: Docker, HPC 클러스터 활용

2. **계산 비용**
   - LSDYNA + COMSOL 동시 실행: 수시간
   - 해결: 작은 메시, 병렬화

3. **데이터 부족**
   - 현재: 11논문 데이터만 (문헌 기반)
   - 필요: 실제 실험 30+ 샘플

### 물리적 한계

1. **외삽 신뢰도**
   - 학습 범위 밖 공정 조건 위험
   - 예: T > 600°C 또는 P < 0.1 mTorr

2. **계면 모델링**
   - 현재: TBC 단순 상수값
   - 개선: 구조 기반 TBC 계산 (NEGF)

3. **복합 효과**
   - 현재: 개별 매개변수 독립 처리
   - 고도화: 비선형 상호작용 포함

---

## ✅ 체크리스트 (통합 준비)

### 도구 점검
- [ ] COMSOL .mph 파일 로드 가능
- [ ] LSDYNA 솔버 경로 확인
- [ ] VASP/QE 라이선스 상태 점검
- [ ] Python 패키지 설치 (scikit-learn, pandas, ase 등)

### 데이터 검증
- [ ] AlN_DC_literature_dataset_CLEANED.csv 검증
- [ ] LITERATURE_METADATA.csv 14편 확인
- [ ] aln_common.py 단일 진실 모듈 테스트

### 파이프라인 테스트
- [ ] tool_connectors.py 기본 기능 실행
- [ ] 공정 입력 → ML 예측 → CSV 저장 확인
- [ ] 오류 처리 (결측값, 범위 초과 등)

### 문서화
- [ ] 각 도구 사용 매뉴얼 작성
- [ ] API 문서 (Swagger/OpenAPI)
- [ ] 문제 해결 가이드

---

**생성일**: 2026-10-05  
**기반**: 05_Integration_Hub/ + tool_connectors.py  
**상태**: ✅ 전략 확정 (구현 준비 단계)

---

**다음 세션에서**: 
- tool_connectors.py 완전 구현
- 첫 번째 자동 파이프라인 테스트
- 웹 API 프로토타입

## 🔗 지식 연결 (Knowledge Mesh)
- **Parent Hub**: [[00_AlN_Research_Hub_Master_Index]]
- **Related Master Plan**: [[통합_연구_마스터플랜_멀티스케일_반도체_열관리]]
- **Master Index**: [[Index]]
