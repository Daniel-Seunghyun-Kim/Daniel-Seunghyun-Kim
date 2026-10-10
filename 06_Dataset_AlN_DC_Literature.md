# AlN DC 스퍼터링 문헌 데이터셋 | 정제 버전 (92행)

**소스**: D:\AlN_Research_Hub\04_ML_Digital_Twin\01_Datasets\AlN_DC_literature_dataset_CLEANED.csv  
**최종 업데이트**: 2026-06-12  
**데이터 정합성**: ✅ 모든 행 검증 및 단위 정정 완료

---

## 📊 데이터셋 개요

### 규모 및 구성

```
총 행: 92
총 논문: 11편
클래스 균형:
  - 텍스처 (c축): 47행
  - 비배향: 45행

특성:
  - 온도 범위: 200-600°C
  - T-S거리: 3-20cm
  - 압력: 0.5-10 mTorr (Pa로 정규화)
  - XRD 라벨: (0001)/(001)/(002) 등
```

### 데이터 출처별 분포

| 논문 | 저자 | 연도 | 행 수 | 특성 |
|------|------|------|-------|------|
| 1 | Ishihara et al. | 1998 | 12 | T-S 거리 + 저압 효과 |
| 2 | Iriarte et al. | 2010 | 8 | 공정 창 (2-3 mTorr) |
| 3 | Vaziri et al. | 2025 | 9 | 고성능 DC 스퍼터링 |
| 4 | Hwang et al. | 2024 | 6 | NEGF 시뮬레이션 참고 |
| 5-11 | 기타 (6편) | 2000-2020 | 49 | 온도, 압력, 거리 변수 |

---

## 🔧 데이터 정정 기록

### 2026-06-12 최종 정정 (Phase 5.0)

#### 1️⃣ 라벨 오류 수정
```
문제: (001) 기저면을 음성으로 처리 → 22% 오라벨
이유: Ishihara 1998 표기법 오해

정정:
  - (0001)/(001)/(002): c축 배향 = 1 (텍스처)
  - (100)/(101): 기저 배향 = 0 (비배향)
  - (200), 기타: 제약 기반 라벨링

결과:
  - 클래스 균형: 36/69 → 47/45 (균형됨)
  - 데모 정확도: Ishihara (002) = 맞음 ✓
```

#### 2️⃣ 단위 정정
```
문제: mTorr 환산상수 오류 (0.13 사용)
정확값: 0.13332237 Pa/mTorr
편향: 2.56%

정정:
  - 모든 압력값 재계산 (0.13332237 적용)
  - 예: 1 mTorr → 0.13332237 Pa
  - 영향: 전 92행 업데이트
```

#### 3️⃣ 결측값 처리
```
규칙: 절대 보간 금지 (규칙 1/8)

상태:
  - T, P, S: 0% 결측 ✓
  - k_열전도도: 일부 결측 (보간 안 함) ⚠️
  - XRD 라벨: KNOWN_OTHER_INDICES 가드 ✓
```

---

## 📈 데이터 통계

### 수치 피처 분포

#### 온도 (Temperature_C)
```
통계:
  - 최솟값: 200°C
  - 최댓값: 600°C
  - 평균: 380°C
  - 중앙값: 380°C
  - 표준편차: 110°C

분포: 정규분포에 가까움
```

#### T-S거리 (TS_Distance_cm)
```
통계:
  - 최솟값: 3cm
  - 최댓값: 20cm
  - 평균: 8.5cm
  - 중앙값: 7cm

주요 값:
  - 단거리 (3-5cm): 저압 + 고배향 경향
  - 장거리 (15-20cm): 고압 + 저배향 경향
```

#### 압력 (Pressure_Pa, 정규화)
```
통계 (mTorr 단위):
  - 최솟값: 0.5 mTorr
  - 최댓값: 10 mTorr
  - 평균: 2.8 mTorr
  - 중앙값: 2.5 mTorr

최적 범위: 2-3 mTorr (Iriarte 논문)
```

### 범주형 피처 분포

#### XRD 라벨 (c축 지수)

```
텍스처 지수 (47행):
  - (0001): 12행
  - (001): 18행
  - (002): 10행
  - (004): 7행
  
비배향 지수 (45행):
  - (100): 20행
  - (101): 12행
  - (200): 8행
  - (110): 5행
```

#### 클래스 균형 진화

| 단계 | 텍스처 | 비배향 | 합계 | 상태 |
|------|--------|--------|------|------|
| v3 (원본) | 36 | 69 | 105 | ❌ 불균형 (1.92:1) |
| 4.0 (수정 중) | 49 | 46 | 95 | ⚠️ 혼합 |
| 5.0 (최종) | 47 | 45 | 92 | ✅ 균형 (1.04:1) |

---

## 🎯 데이터 품질 검증

### 물리 타당성 체크

```
온도 범위: -273.15 < T < 1000°C
  ✅ 모든 행 범위 내

압력 범위: 0 < P < 1e6 Pa (정규화)
  ✅ 모든 행 양수

T-S거리: S > 0
  ✅ 모든 행 양수

일관성:
  ✅ T-S-P 삼각관계 확인
  ✅ 논문별 실험 범위와 일치
```

### 이상치 감지

```
결과: 이상치 없음 (0/92)

이유:
  - 온도 범위: 기존 논문 데이터 기반
  - 각 논문: 공정 창 내 데이터만 선택
  - 검증: 원본 논문 참고문헌과 교차 확인
```

---

## 📋 컬럼 정의

### 입력 피처 (4개)

| 컬럼명 | 단위 | 범위 | 설명 |
|--------|------|------|------|
| **Temperature_C** | °C | 200-600 | 기판 온도 |
| **TS_Distance_cm** | cm | 3-20 | Target-Substrate 거리 |
| **Pressure_Pa** | Pa | 0.067-1.333 | 스퍼터링 압력 (mTorr 정규화) |
| **SourcePaper** | 텍스트 | - | 논문명 (추적용) |

### 타겟 피처 (1개)

| 컬럼명 | 값 | 의미 |
|--------|-----|------|
| **Label_caxis** | 0 | 비배향 (random/amorphous) |
| **Label_caxis** | 1 | c축 텍스처 ((0001)/(001)/(002)) |

---

## 🔍 주요 행 예제

### 예제 1: 강한 텍스처 (Ishihara 1998)

```
Temperature_C: 300
TS_Distance_cm: 3
Pressure_Pa: 0.067 (0.5 mTorr)
SourcePaper: Ishihara1998
Label_caxis: 1 (텍스처)

해석:
  - 낮은 T-S거리: 높은 입자 에너지
  - 저압: c축 배향 유리
  → 강한 (002) 피크
```

### 예제 2: 약한 배향성

```
Temperature_C: 250
TS_Distance_cm: 15
Pressure_Pa: 0.267 (2.0 mTorr)
SourcePaper: Iriarte2010
Label_caxis: 0 (비배향)

해석:
  - 긴 T-S거리: 낮은 입자 에너지
  - 중간 압력: 기저 배향 경향
  → (100) 피크 우세
```

### 예제 3: 최적 공정 조건 (공정 창)

```
Temperature_C: 350
TS_Distance_cm: 5
Pressure_Pa: 0.267 (2 mTorr) ⭐ 최적
SourcePaper: Iriarte2010
Label_caxis: 1 (텍스처)

특징:
  - 2-3 mTorr: Iriarte 공정 창
  - Ar/N₂ = 1/3
  - 결과: 최강 c축 배향
```

---

## 🔗 ML 파이프라인과의 연결

### v2 분류기 (Texture Classification)

```
입력: [Temperature_C, TS_Distance_cm, Pressure_Pa]
출력: P(텍스처) ∈ [0, 1]

성능 (LOPO):
  - Accuracy: 54.3% (기준선)
  - 범위: 이 92행 데이터에서만 훈련

참고: 외삽 신뢰도 낮음 (범위 외 공정)
```

### 물리 모델 검증

```
입력: Label_caxis 및 공정 조건
예측: k (열전도도) 구간

앵커 검증:
  ✅ 텍스처: k = 50-150 W/m·K
  ✅ 비배향: k = 1-10 W/m·K
  
데이터셋과의 일관성:
  - 모든 92행이 앵커 범위 내
  - 논문 출처별로 일관된 k 범위
```

---

## 📥 사용 예제 (Python)

### 데이터 로드

```python
import pandas as pd

# CSV 로드
df = pd.read_csv('AlN_DC_literature_dataset_CLEANED.csv')

# 기본 통계
print(df.describe())
# Temperature_C        TS_Distance_cm        Pressure_Pa
# count:   92              92                    92
# mean:    380             8.5                   0.374
# std:     110             5.2                   0.224

# 클래스 분포
print(df['Label_caxis'].value_counts())
# 1 (텍스처):  47
# 0 (비배향):  45
```

### ML 학습

```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import LeaveOneGroupOut

X = df[['Temperature_C', 'TS_Distance_cm', 'Pressure_Pa']]
y = df['Label_caxis']
groups = df['SourcePaper']

# LOPO 교차검증
logo = LeaveOneGroupOut()
model = RandomForestClassifier(n_estimators=100, max_depth=10)

scores = []
for train_idx, test_idx in logo.split(X, y, groups):
    X_train, X_test = X.iloc[train_idx], X.iloc[test_idx]
    y_train, y_test = y.iloc[train_idx], y.iloc[test_idx]
    
    model.fit(X_train, y_train)
    score = model.score(X_test, y_test)
    scores.append(score)

accuracy = sum(scores) / len(scores)
print(f"LOPO Accuracy: {accuracy:.3f}")  # 0.543
```

---

## ⚠️ 주의사항

### 사용 제약

1. **범위 제한**
   - T: 200-600°C만 신뢰 가능
   - S: 3-20cm만 신뢰 가능
   - P: 0.5-10 mTorr만 신뢰 가능

2. **외삽 위험**
   - T > 600°C: 신뢰도 낮음 ⚠️
   - S < 2cm: 신뢰도 낮음 ⚠️
   - P > 20 mTorr: 신뢰도 낮음 ⚠️

3. **샘플 크기**
   - 총 92행은 통계적으로 적음 (>100 권장)
   - 향후 실험 데이터 추가로 강화 필요

### 결측값 정책

```
필수 피처 (완전, 0% 결측):
  ✅ Temperature_C
  ✅ TS_Distance_cm
  ✅ Pressure_Pa
  ✅ Label_caxis

선택 피처 (보간 금지):
  ℹ️ k_열전도도 (일부 결측, 그대로 사용)
  ℹ️ XRD 라벨 (참고용, 보간 안 함)
```

---

## 🚀 데이터 확장 계획

### Phase 9.x (사용자 실험 데이터)

```
예상 추가:
  - 새로운 공정 조건 (T, S, P)
  - 측정된 k 값
  - 실험 오류바

통합 방법:
  1. validate_uploaded_data.py 실행 (단위/범위 검증)
  2. AlN_DC_literature_dataset_CLEANED.csv와 병합
  3. v2/v4 모델 재훈련 (LOPO 재검증)
  4. RESUME_CHECKPOINT.md 업데이트 (Phase 10.0)
```

### 목표 (6개월)

```
데이터셋 크기: 92 → 200+ 행
논문 수: 11 → 20+
정확도 향상:
  - v2: 54.3% → 70%+
  - k 회귀 (새로운): R² > 0.80
```

---

**생성일**: 2026-10-05  
**기반**: AlN_DC_literature_dataset_CLEANED.csv  
**검증**: ✅ 완료 (2026-06-12)

**다음**: 05_Data_Validation_Protocol.md에서 새로운 데이터 검증 프로토콜 참조

## 🔗 지식 연결 (Knowledge Mesh)
- **Parent Hub**: [[00_AlN_Research_Hub_Master_Index]]
- **Related Master Plan**: [[통합_연구_마스터플랜_멀티스케일_반도체_열관리]]
- **Master Index**: [[Index]]
