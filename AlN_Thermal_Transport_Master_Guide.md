# AlN 열수송 프로젝트 마스터 가이드
## 공정 설계 → 샘플 선별 → 측정 → 데이터 통합 → ML 모델링 (완전 워크플로우)

**최종 목표**: 고c축 배향 wurtzite AlN 박막의 공정-구조-열수송 관계 정량화 및 디지털 트윈 개발

**프로젝트 범위**: AlN sputtering deposition, c-axis orientation, columnar microstructure, 열전도도, Cu/AlN 계면

---

# 📋 전체 단계 개요

| Phase | 단계 | 기간 | 산출물 |
|-------|------|------|--------|
| **Phase 1** | 공정 설계 & 위험 평가 | 1주 | 공정 파라미터 테이블, Target poisoning/Plasma 평가 |
| **Phase 2** | 샘플 선별 & 구조분석 계획 | 2주 | 샘플 로드맵, 측정 우선순위 |
| **Phase 3** | 구조 특성화 | 3~4주 | XRD, SEM, AFM, XPS, 선택 TEM |
| **Phase 4** | 열수송 측정 | 4~6주 | TDTR/FDTR 데이터, TBC/TBR 정량화 |
| **Phase 5** | 데이터 통합 & 정제 | 2주 | 통합 데이터셋, 메타데이터 |
| **Phase 6** | ML 모델링 | 3~4주 | 예측 모델, 디지털 트윈 v1 |

**총 기간**: 15~20주 (병렬 처리 가능)

---

---

# ⚠️ 프로젝트 제약 조건 (Keyword Exclusion Rule)

## Active Scope (필수)
```
✅ AlN sputtering deposition (RF/DC)
✅ c-axis-oriented wurtzite AlN
✅ Columnar microstructure
✅ XRD, FE-SEM cross-section, AFM
✅ XPS, TDTR, FDTR
✅ Thermal conductivity & boundary conductance
✅ Cu/AlN interface
✅ Machine-learning-based process optimization
✅ Digital twin
```

## Inactive Scope (제외)
```
❌ Ferroelectricity, AlScN 강유전성
❌ P-E loop, coercive field
❌ TFT device stack, memory device operation
❌ Piezoelectric device, SAW filter, MEMS
❌ AAO (Anodic Aluminum Nitride)
```

**필터링 규칙**: 모든 제안/분석/미래 방향은 Active Scope 내에서만 제시

---

---

# PHASE 1: 공정 설계 & 위험 평가

## 1.1 현재 실험 플랫폼 확인

### 증착 방법
- **RF Magnetron Sputtering** 또는 **DC Magnetron Sputtering** (또는 RF+DC 하이브리드)

### 타겟 & 반응 가스
- Target: Aluminum (Al) 또는 Al-합금
- Reactive gas: Nitrogen (N₂)
- Sputtering gas: Argon (Ar)

### 기판
- Si (bare)
- SiO₂/Si
- Cu-coated Si (Cu/AlN 계면 평가용)

### 주요 제어 파라미터
```
공정 입력:
  • N₂/(N₂+Ar) ratio → 질소 함량 제어
  • RF power (W)     → 이온 에너지, 증착율
  • DC power (W)     → 추가 이온 에너지
  • Chamber pressure (mTorr) → 산란, 스퍼터링 수율
  • Substrate temperature (°C) → adatom 이동성
  • Film thickness (nm)   → 구조 진화 추적
  • Deposition time (min) → 증착율 계산
```

---

## 1.2 공정 조건 평가 틀

**제안하는 공정 조건이 있으면, 다음 항목을 반드시 평가하십시오:**

### A. Target Poisoning 평가

**목표**: 금속 모드 vs 독성 영역 판정

**평가 항목**:
1. **N₂/(N₂+Ar) 비율** → 0.3 (금속) ~ 0.7 (독성) 범위 추정
2. **RF/DC power** → 높을수록 금속 모드 유지
3. **chamber pressure** → 낮을수록 타겟 전압 유지 (금속 모드)
4. **예상 증착율** → 독성 영역에서 50~70% 감소 가능

**판정**:
- ✅ **안정 금속 모드**: high power, low N₂/(N₂+Ar), low pressure → 빠른 증착율, 높은 crystallinity 기대
- ⚠️ **전이 영역**: 불안정성 위험 (plasma extinction, reflected power ↑)
- ❌ **완전 독성 영역**: 극히 낮은 증착율 (<0.1 nm/s), 공정 실패 가능성

---

### B. Plasma 안정성 평가

**평가 항목**:
1. **Plasma ignition**: 매우 높은 N₂ → 점화 어려움
2. **Plasma extinction**: 극저 pressure + 높은 N₂/(N₂+Ar) → 소화 위험
3. **Reflected power**: 타겟 임피던스 변화 → matching network 조정 필수
4. **Pressure 조정**: 불안정하면 +0.5 mTorr 증가

**판정**:
- ✅ **안정적**: Steady plasma, constant reflected power < 5%
- ⚠️ **주의**: Reflected power 10~20%, 압력 미세조정 필요
- ❌ **위험**: Reflected power > 30%, 빈번한 plasma extinction → 공정 불가능

---

### C. Arcing 위험도 평가

**평가 항목**:
1. **Charge accumulation**: N-rich compound layer 형성 → dielectric
2. **타겟 표면 상태**: 매끄러운 금속 vs 울퉁불퉁한 산화물
3. **Particle 생성**: Arc → microdroplet 방출 → 박막 결함

**판정**:
- ✅ **저위험**: Clean metallic target, smooth sputtering
- ⚠️ **중위험**: Occasional arc (1~3회/시간), 표면 청결 유지
- ❌ **고위험**: 빈번한 arc (> 5회/시간) → 박막 품질 저하, SEM에서 visible defect

---

## 1.3 공정 조건 설계 예시

**예: c축 AlN 형성을 위한 기본 공정 윈도우**

| 항목 | 권장값 | 근거 |
|------|--------|------|
| **Deposition method** | RF (13.56 MHz) | 안정적 plasma, 높은 c축 방향성 |
| **RF power** | 150~250 W | 금속 모드 유지, adatom energy 최적화 |
| **N₂/(N₂+Ar)** | 0.4~0.6 | 금속→독성 전이 피함, 최적 질소 함량 |
| **Chamber pressure** | 1.5~2.5 mTorr | Plasma stability, 적절한 산란 |
| **Substrate temp** | 300~400°C | Adatom mobility ↑, 결정화 개선 |
| **Deposition time** | 30~60 min | 500 nm 막 달성 |
| **Expected rate** | 10~15 nm/min | 금속 모드 지표 |

---

## 1.4 공정 파라미터 테이블 (Planning Sheet)

**아래 테이블을 작성하여 계획된 실험을 정리하세요:**

```
ID  | Depo | RF_W | N2_Ar | Pressure | Temp_C | Time_min | Target_k | Poisoning_Risk | Plasma_Stability | Notes
----|------|------|-------|----------|--------|----------|----------|-----------------|-----------------|-------
1   | RF   | 200  | 0.5   | 2.0      | 300    | 40       | > 40     | ✅ Low         | ✅ Stable       | Baseline
2   | RF   | 250  | 0.4   | 1.8      | 350    | 35       | > 45     | ✅ Low         | ✅ Stable       | Power↑
3   | RF   | 180  | 0.6   | 2.2      | 300    | 45       | 35~40    | ⚠️ Medium      | ⚠️ Monitor      | N2↑ risk
4   | RF   | 200  | 0.5   | 2.0      | 400    | 40       | > 45     | ✅ Low         | ✅ Stable       | Temp↑
...
```

---

---

# PHASE 2: 샘플 선별 & 구조분석 계획

## 2.1 샘플 선별 기준 (TDTR/FDTR 측정 가치)

### Tier 1: 반드시 측정할 샘플 (높은 정보 이득)

| 기준 | 이유 | 우선순위 |
|------|------|---------|
| **c-axis 방향성 강함** (XRD (0002)/(10-10) 강도비 > 5) | 열전도도 이방성 정량화 | ⭐⭐⭐ |
| **SEM에서 명확한 columnar 구조** (기둥폭 균일 ±20%) | 그레인 경계 산란 메커니즘 검증 | ⭐⭐⭐ |
| **두께 범위 다양** (100 nm, 300 nm, 500 nm, 1000 nm) | 임계/포화 두께 식별 | ⭐⭐⭐ |
| **N₂/(N₂+Ar) 극단값** (0.3, 0.5, 0.7) | 질소 함량이 열전도도에 미치는 영향 | ⭐⭐⭐ |
| **기판 다양** (Si vs Cu/Si) | Cu/AlN 계면 열저항 평가 | ⭐⭐⭐ |

**목표**: Tier 1 샘플 8~12개 선정 → TDTR/FDTR 측정 집중

---

### Tier 2: 조건부 측정

| 기준 | 측정 조건 |
|------|----------|
| 산소 오염이 의심되는 샘플 (XPS O 피크 > 5%) | XPS 정량화 후 측정 |
| 비정질 interlayer 형성된 샘플 (TEM 관찰 필요) | TEM 단면분석 완료 후 |
| AFM 거칠기 > 5 nm | 계면 열저항에 미치는 영향 분석 |

---

### Tier 3: 스킵 가능

❌ 비정질/다결정 AlN (c축 배향 없음)  
❌ SEM에서 연속성 불안정한 막  
❌ 중복된 공정 조건 (< 10% 파라미터 변화)

---

## 2.2 구조분석 순차 실행 계획 (정보 흐름 최적화)

```
Phase 2-A: 빠른 스크리닝 (1~2주) — 모든 샘플
├─ XRD (0002, 10-10, 10-11)
│  └─ 목표: c축 방향성 평가, Tier 1 필터링
├─ FE-SEM 단면 (columnar 형태, 두께, 공공)
│  └─ 목표: 미시구조 평가, 두께 측정
└─ AFM 표면 (거칠기, 습곡)
   └─ 목표: 표면 특성, 계면 거칠기 평가

    ↓ (XRD 기반 Tier 분류)

Phase 2-B: 심화 분석 (2~3주) — Tier 1만
├─ XPS (산소, 질소 함량 정량)
│  └─ 목표: 산소 오염 게이트 (> 5% 제외 가능)
├─ GDOES (깊이별 조성)
│  └─ 목표: 산소 깊이 분포
└─ SEM 대면적 매핑 (균일성)
   └─ 목표: 샘플 전체 특성 검증

    ↓ (산소 판정 후)

Phase 2-C: 미시구조 분석 (3~4주) — Tier 1 극단값만
├─ TEM 단면 (grain boundary, amorphous layer, 계면)
│  └─ 목표: 그레인 크기, 산소/불순물 분포
└─ EELS (국소 산소/질소 분포)
   └─ 목표: 계면 오염 확인

    ↓ (물리적 메커니즘 가설 수립)

Phase 2-D: 열수송 측정 준비
└─ Tier 1 샘플 확인, TDTR/FDTR 스케줄링
```

---

## 2.3 샘플 데이터시트 (추적 템플릿)

**각 샘플마다 다음 항목을 기록하세요:**

```markdown
## Sample: AlN_RF_N2-50_500nm_Si_001

### Phase 2-A: XRD Screening
- (0002) intensity: [값, cps] | (10-10) intensity: [값]
- c-axis orientation ratio: [> 5 ✓ / 미달 ✗]
- FWHM (0002): [도]
- **Tier 판정**: [1 / 2 / 3]

### Phase 2-A: SEM Analysis
- Columnar structure: ✓ 명확 / ~ 약함 / ✗ 없음
- Film thickness: [nm] ± 5% (평균값, 3점 측정)
- Continuity: ✓ 우수 / ~ 보통 / ✗ 불안정
- Thickness_quality_flag: ✓ Reliable / ⚠️ Uncertain

### Phase 2-A: AFM Surface
- Roughness (Ra): [nm]
- Peak-to-valley: [nm]

### Phase 2-B: XPS Analysis (Tier 1만)
- O concentration: [at%]
- N/Al ratio: [값]
- **Oxygen_concern_flag**: [True if > 5% / False]

### Phase 2-C: TEM (선택, 극단값만)
- Grain size: [nm]
- Amorphous interlayer: [있음 ~Xnm / 없음]
- Interface disorder: [관찰내용]

### Recommendation
- **TDTR Target**: [Go / No-Go]
- **Priority Tier**: [1-1 / 1-2 / 2 / Skip]
- **Expected k range**: [예상 W/m·K]
```

---

## 2.4 샘플 로드맵 (최종 선별 테이블)

```
ID   | Composition | Thickness | XRD c-axis | SEM Quality | O_% | TDTR_Priority
-----|-------------|-----------|------------|-------------|-----|---------------
S01  | RF_N2-50    | 500nm     | ⭐⭐⭐⭐⭐   | ⭐⭐⭐⭐    | 2.1 | Tier 1-1 (기준)
S02  | RF_N2-50    | 100nm     | ⭐⭐⭐⭐    | ⭐⭐⭐     | 1.8 | Tier 1-1 (두께)
S03  | RF_N2-50    | 1000nm    | ⭐⭐⭐⭐    | ⭐⭐⭐     | 2.3 | Tier 1-1 (두께)
S04  | RF_N2-30    | 500nm     | ⭐⭐⭐     | ⭐⭐⭐     | 1.5 | Tier 1-2 (N2 감)
S05  | RF_N2-70    | 500nm     | ⭐⭐      | ⭐⭐      | 8.5 | ⚠️ Tier 2 (산소)
S06  | DC_N2-50    | 500nm     | ⭐⭐⭐⭐⭐   | ⭐⭐⭐⭐    | 2.0 | Tier 1-2 (DC)
S07  | RF_N2-50    | 500nm     | ⭐        | ⭐         | - | ❌ Skip (비정질)
S08  | RF_N2-50(Cu) | 500nm    | ⭐⭐⭐⭐⭐   | ⭐⭐⭐⭐    | 2.2 | Tier 1-1 (Cu/AlN)
...
```

---

---

# PHASE 3: 구조 특성화 (측정 & 분석)

## 3.1 XRD 분석

### 측정 프로토콜
```
장비: X-ray diffractometer (CuKα, λ = 1.54 Å)
범위: 20° ~ 60° 2θ (AlN (0002), (10-10), (10-11), (10-13) 포함)
스캔 속도: 2°/min (고해상도)
스텝: 0.02°
적분 시간: 2초/스텝
```

### 분석 항목

**1. 피크 강도 (Peak Intensity)**
```
I_0002 = AlN (0002) 피크 적분 강도 (cps)
I_0010 = AlN (10-10) 피크
I_0011 = AlN (10-11) 피크

→ 강도 정규화 필수! (장비/조건 다름)
  normalized_I_0002 = measured_I_0002 / reference_I_0002 × 100
  (기준: 고품질 AlN 표준 샘플)
```

**2. c축 방향성 (Texture Coefficient)**
```
TC = I_0002 / (I_0002 + I_0010 + I_0011)
범위: 0 (random orientation) ~ 1 (perfect c-axis)

판정:
  TC > 0.85 → ✅ 우수한 c축 배향
  0.70 < TC < 0.85 → ~ 보통
  TC < 0.70 → ❌ 약한 배향 (Tier 1 제외)
```

**3. 결정성 (FWHM - Full Width Half Maximum)**
```
FWHM_0002 = AlN (0002) 피크의 반치전폭 (degrees)

판정:
  FWHM < 2.0° → ✅ 높은 결정성 (좁은 피크)
  2.0° < FWHM < 3.5° → ~ 중간 결정성
  FWHM > 3.5° → ⚠️ 낮은 결정성
```

### 해석 틀 (Alternative explanations)

**관찰**: TC > 0.85, FWHM = 1.5°
- **주요 원인**: RF power ↑, 낮은 N₂/(N₂+Ar), 높은 substrate temp
- **물리 메커니즘**: Adatom mobility ↑ → 자기 정렬 (self-alignment)
- **대안 설명**: Target poisoning 없음 (금속 모드 유지)
- **다음 실험**: TDTR로 열전도도 확인, 두께 변화 추적

**관찰**: TC = 0.45, FWHM = 4.2°
- **주요 원인**: N₂/(N₂+Ar) > 0.65 (과량 질소)
- **물리 메커니즘**: Target poisoning → 증착율 ↓, 비정질 성장 선호
- **대안 설명**: Substrate temperature 부족, plasma instability
- **다음 실험**: Power ↑ 또는 N₂ ↓, XPS로 산소 확인

---

## 3.2 FE-SEM 단면 분석

### 측정 프로토콜
```
샘플 준비: 
  - Cross-section 샘플 준비 (ion milling 또는 mechanical fracture)
  - 금 코팅 (5~10 nm)

측정 조건:
  - 가속 전압: 3~5 kV (고해상도)
  - 배율: 3000×, 10000× (미시구조 판별)
  - 측정점: 3점 이상 (thickness 균일성)
```

### 분석 항목

**1. Columnar 형태**
```
평가:
  ✅ 명확 columnar: 기둥 폭 균일 (±20%), 직선 경계
  ~ 약한 columnar: 기둥 구조 흐릿함, 포락 구조 있음
  ❌ 없음: 등축 입자, 방향성 없음

물리 의미:
  Columnar structure + c축 배향 → 열전도도 ↑ (기대값)
```

**2. 두께 (Film Thickness)**
```
측정: 3점 평균 ± 표준편차 (nm)
예: 510 ± 8 nm

두께 균일성:
  (Max - Min) / Mean × 100 < 5% → ✅ 우수
  5~10% → ~ 보통
  > 10% → ❌ 불균일 (공정 문제)
```

**3. 공공(Voids) & 균열(Cracks)**
```
void_fraction = [공공 면적] / [전체 막 면적] × 100%

판정:
  < 1% → ✅ 우수 (dense film)
  1~5% → ~ 보통 (tolerable)
  > 5% → ❌ 높은 공공도 (열전도도 ↓ 예상)
```

---

## 3.3 AFM (Atomic Force Microscopy)

### 측정 프로토콜
```
모드: Tapping mode (비접촉)
스캔 범위: 2 μm × 2 μm, 10 μm × 10 μm (다중 영역)
해상도: 256 × 256 pixels
```

### 분석 항목

**1. RMS 거칠기 (Roughness)**
```
Ra = 산술평균 거칠기 (nm)
Rq = 제곱평균 거칠기 (nm)

판정:
  Ra < 2 nm → ✅ 매우 부드러움 (계면 양호)
  2~5 nm → ~ 보통
  Ra > 5 nm → ⚠️ 거침 (계면 열저항 ↑ 우려)
```

**2. 표면 형태 (Morphology)**
```
관찰:
  - 평탄한 표면 (featureless) → c축 columnar 구조 강함
  - 언덕/골짜기 패턴 → 입자 크기, grain boundary 신호
  - 불규칙한 울퉁불퉁 → 산소 오염, 비정질 성장
```

---

## 3.4 XPS (X-ray Photoelectron Spectroscopy) — Tier 1만

### 측정 프로토콜
```
장비: XPS spectrometer
X-ray source: Al Kα (1486.6 eV)
Depth profiling: Ar ion sputtering (30~60 seconds, 여러 깊이)
```

### 분석 항목

**1. 원소 정량화**
```
O (1s): 산소 함량 (at%)
N (1s): 질소 함량 (at%)
Al (2p): 알루미늄 함량 (at%)

계산:
  O_concentration (at%) = [O peak area] / [total peak area] × 100%
  
  예상값:
    AlN 이론: Al 50%, N 50%
    실제 (좋은 샘플): Al 48~52%, N 48~52%, O < 5%
```

**2. 산소 게이트 (Oxygen Gate)**
```
O_at% < 3% → ✅ 우수 (매우 낮은 오염)
3% < O_at% < 5% → ~ 보통 (허용 범위)
O_at% > 5% → ⚠️ 주의 (공정 문제)
  → TDTR 측정 전 공정 재평가
  → 챔버 누수, 반응 가스 순도 검사
```

**3. 깊이 분포 (Depth Profiling)**
```
표면 (0~10 nm): 일반적으로 산소 높음 (Al₂O₃ 형성)
중간층 (10~50 nm): AlN 조성 (산소 낮음)
기저층 (> 50 nm): 기판 신호

해석:
  표면 산화층 ~ 2~5 nm → 정상 (자연 산화)
  두꺼운 산화층 > 10 nm → 공정 중 산화 문제
  벌크 내 산소 > 3% → 심각 (공정 불량)
```

---

## 3.5 TEM (Transmission Electron Microscopy) — 선택, 극단값만

### 측정 범위
- Tier 1의 극단값 샘플 (예: 가장 높은 k, 가장 낮은 k)
- 2~3개 샘플만 (비용 효율)

### 분석 항목

**1. 그레인 크기 (Grain Size)**
```
측정: 10개 이상 grain의 직경 평균 (nm)
예: 50 ± 15 nm

물리 의미:
  그레인이 작을수록 → 그레인 경계 산란 ↑ → k ↓
  columnar 구조와 함께 분석 필수
```

**2. 비정질 Interlayer**
```
관찰: 기판과 AlN 사이 비정질층 존재 여부
  없음 → ✅ (계면 깨끗함)
  있음 → 두께 측정 (예: 3~5 nm)
           → TBR (Thermal Boundary Resistance) ↑ 원인

물리 메커니즘:
  비정질층 → 포논 산란 ↑ → 계면 열저항 ↑
```

**3. 계면 품질 (Interface Quality)**
```
HRTEM 관찰:
  Clean & abrupt: ✅ 양호 (원자급 정확)
  Diffuse & rough: ⚠️ 산소 오염 의심
```

---

---

# PHASE 4: 열수송 측정 (TDTR/FDTR)

## 4.1 TDTR (Time-Domain Thermoreflectance) 측정

### 목표
- AlN 박막의 열전도도 (k) 정량화
- 계면 열전도도 (TBC) 또는 열저항 (TBR) 측정

### 측정 프로토콜

```
장비: TDTR 시스템 (Maryland TDTR 또는 동등)

레이저 설정:
  - Pump 파장: 488 nm (AlN 투과)
  - Pump 파워: 조정 (샘플 손상 주의)
  - 펌프-프로브 지연: 0.1 ~ 3000 ps

측정 조건:
  - 온도: 실온 (300 K)
  - 반복: 3회 이상 (재현성 확인)
  - 측정점: 샘플당 3~5 지점 (공간 균일성)
```

### 분석 항목

**1. 막 열전도도 (Film Thermal Conductivity)**
```
측정값: k_AlN (W/m·K)

출력 형식:
  k = 45.2 ± 2.1 W/m·K (95% CI)
  
기대값 (c축 columnar AlN):
  100~200 nm: 30~50 W/m·K
  300~500 nm: 40~70 W/m·K
  1000 nm: 60~150 W/m·K
  (bulk 이론값: ~200 W/m·K)

이상치 판정:
  k < 10 W/m·K → 측정 오류 또는 매우 열악한 품질
  k > 200 W/m·K (박막) → 측정 방법 재검토
```

**2. 계면 열전도도 (Thermal Boundary Conductance, TBC)**
```
정의: TBC = [열류] / [ΔT across interface]
단위: MW/(m²·K)

측정:
  Al/AlN interface (ref.) → TBC ≈ 50~100 MW/(m²·K)
  Cu/AlN interface → TBC ≈ 50~150 MW/(m²·K)

고품질 Cu/AlN:
  TBC ↑ (부드러운 계면, 산소 없음)
저품질:
  TBC ↓ (거친 계면, 산소 오염, amorphous layer)
```

**3. 계면 열저항 (Thermal Boundary Resistance, TBR)**
```
정의: TBR = 1 / TBC
단위: m²·K/GW

예시:
  TBC = 100 MW/(m²·K) → TBR = 0.01 m²·K/GW = 10 mm²·K/W
  
해석:
  낮은 TBR (< 10 mm²·K/W) → 양호한 계면
  높은 TBR (> 50 mm²·K/W) → 열전달 병목
```

---

### 측정 오류 회피

| 오류 | 원인 | 방지법 |
|------|------|--------|
| **k 과대평가** | 계면 TBR을 막 k에 포함 | Al/AlN 또는 Au 기준 샘플로 보정 |
| **계면 신호 약함** | S/N ratio 낮음 | 측정 시간 ↑, 여러 지점 평균 |
| **재현성 낮음** | 샘플 표면 오염 | 측정 전 표면 초음파 세척 |
| **TDTR만 시행** | 주파수 의존성 간과 | FDTR 병행 (아래 참고) |

---

## 4.2 FDTR (Frequency-Domain Thermoreflectance) 측정 — 선택

### 목표
- TDTR 결과 검증
- 주파수 의존성 확인 (계층별 영향 분리)
- Thermal penetration depth 평가

### 측정 프로토콜

```
장비: FDTR 시스템 (lock-in 증폭기 포함)

주파수 범위: 0.1 ~ 10 MHz (최소 3 decade)
스캔: 각 주파수에서 30~60초 적분

검출: 반사율 변조 신호 (phase & amplitude)
```

### 분석 항목

**1. 주파수 의존성 (Frequency Dependence)**
```
관찰:
  f ↑ → penetration depth ↓ (얕은 층만 감지)
  f ↓ → penetration depth ↑ (깊은 계면까지 감지)

해석:
  FDTR 곡선이 f에 따라 변하면 → 층별 특성 다름
  예: 표면 산화층, amorphous interlayer 신호
```

**2. 열확산도 (Thermal Diffusivity, α)**
```
정의: α = k / (ρ × c_p)
  k = 열전도도 (W/m·K)
  ρ = 밀도 (kg/m³)
  c_p = 비열 용량 (J/kg·K)

FDTR로 측정하면:
  → TDTR 결과의 k 검증
  → ρ × c_p 역으로 추정 가능
```

---

## 4.3 측정 우선순위 및 일정

```
Week 7-8:   TDTR 기준 샘플 (S01, S02, S03)
            → 기기 캘리브레이션, 프로토콜 최적화

Week 9-10:  TDTR Tier 1 샘플 (총 8~10개)
            → k, TBC 정량화
            → 물리 해석 시작

Week 11-12: FDTR 선택 샘플 (이상 또는 계층 분석 필요)
            → f 의존성 확인
            → 최종 열전도도 값 결정
```

---

---

# PHASE 5: 데이터 통합 & 정제

## 5.1 통합 데이터셋 컬럼 구조 (계층적)

### Layer 1: 공정 파라미터 (Raw Input Features)
원본 데이터에서 수정 없이 유지 (단위 통일만)

```
deposition_method          RF / DC
rf_power_W                 [숫자, W]
dc_power_W                 [숫자, W]
chamber_pressure_mTorr     [숫자, mTorr]
n2_flow_sccm               [숫자]
ar_flow_sccm               [숫자]
substrate_temperature_C    [숫자]
target_substrate_distance_cm [숫자]
deposition_time_min        [숫자]
substrate_type             Si / SiO2_Si / Cu_Si
base_pressure_mTorr        [숫자]
pre_sputtering_time_min    [숫자]
target_purity              [%]
substrate_cleaning         Standard / Ar_ion / RCA
data_source                Own_exp / Paper_XYZ
batch_id                   [식별자] (grouped CV용)
```

---

### Layer 2: 파생 공정 변수 (Derived Features)
Layer 1에서 계산 (데이터 누수 X)

```
n2_ar_ratio                = n2_flow_sccm / (n2_flow_sccm + ar_flow_sccm)
total_gas_flow_sccm        = n2_flow_sccm + ar_flow_sccm
rf_power_density_W_cm2     = rf_power_W / target_area_cm2
working_pressure_mTorr     = measured_pressure_during_deposition
deposition_energy_proxy    = (rf_power_W + dc_power_W) / total_gas_flow_sccm
```

---

### Layer 3A: 구조 특성화 (Characterization Outputs)

```
# XRD
xrd_0002_intensity_cps         [숫자, 정규화됨]
xrd_0010_intensity_cps         [숫자]
xrd_0002_fwhm_deg              [숫자]
texture_coefficient_tc         [0~1]
xrd_quality_flag               High / Medium / Low

# SEM
film_thickness_nm              [숫자]
thickness_uncertainty_percent  [±%]
columnar_morphology_score      [0~1]
void_fraction_percent          [%]
continuity_rating              Excellent / Good / Fair / Poor
sem_quality_flag               Good / Fair / Poor

# AFM
rms_roughness_nm               [숫자]
peak_to_valley_nm              [숫자]

# XPS
oxygen_concentration_at_percent [숫자]
nitrogen_concentration_at_percent [숫자]
oxygen_concern_flag            False / True (O > 5%)

# TEM (선택)
grain_size_nm                  [숫자] 또는 NaN
amorphous_interlayer_nm        [숫자] 또는 None
```

---

### Layer 3B: 열수송 특성 (Thermal Transport Outputs)

```
# TDTR 측정
thermal_conductivity_W_mK      [숫자] ← **핵심**
thermal_conductivity_std_W_mK  [측정 표준편차]
tdtr_available                 True / False

# FDTR (선택)
thermal_conductivity_fdtr_W_mK [숫자]
fdtr_available                 True / False

# 계면 열저항
tbc_cu_aln_MW_m2K              [숫자] (Cu 기판만)
tbr_cu_aln_m2K_GW              [계산값]
tbc_substrate_MW_m2K           [일반 기판]
```

---

## 5.2 데이터 정제 규칙

### ❌ 완전 제외 (Row 삭제)

| 조건 | 이유 |
|------|------|
| 기본 공정 정보 부재 (rf_power, pressure, n2_ar_ratio 중 2개 이상 없음) | 모델 학습 불가능 |
| 필수 구조 데이터 부재 (XRD, SEM thickness 둘 다 없음) | 물리 해석 불가능 |
| **XRD 0002 피크 검출 불가** (배경 노이즈 수준) | c축 방향성 평가 불가 |
| **Thickness 오류 > 20%** (명백한 측정 실수) | 데이터 품질 저하 |
| **k < 1 또는 k > 400 W/m·K** (물리적 불가능) | 측정 오류 |

---

### ⚠️ 조건부 재활용 (플래그 추가, Row 유지)

| 조건 | 처리 | 사용 조건 |
|------|------|---------|
| **O_at% 3~10%** | oxygen_concern_flag = True | k 모델 주의, 해석 명시 |
| **XRD 측정 안 됨** | texture_coefficient_tc = NaN | 구조 회귀만 (k 불가) |
| **Thickness 오류 5~20%** | thickness_quality_flag = "uncertain" | 두께 회귀 가중치 ↓ |
| **여러 배치 섞여있음** | batch_id 명시 | Grouped k-fold CV |
| **FDTR만 (TDTR 없음)** | tdtr_available = False | 부분 모델 |

---

### ✅ 안전하게 재활용 (최소 가공)

| 데이터 | 재활용 방식 |
|------|----------|
| **공정 파라미터** | 그대로 사용 (단위 통일) |
| **N2/Ar 비율** | 원본 흐름값에서 재계산 |
| **XRD 강도** | 기준 샘플로 정규화 |
| **두께 (SEM)** | 기준값 (3점 평균 사용) |
| **열전도도 k** | 측정 방법별 분리 (TDTR vs FDTR) |

---

## 5.3 데이터 누수(Leakage) 방지

### ❌ 절대 금지

```
Input Feature        →  Output Target    문제점
─────────────────────────────────────────────────────
thickness           →  deposition_rate  파생 관계 (누수!)
xrd_0002_fwhm       →  c_axis_score     계산으로 도출됨
oxygen_at_percent   →  thermal_cond     부분 인과, 혼동
```

### ⚠️ 조건부 허용

```
xrd_0002_intensity  →  c_axis_orientation  OK (독립 측정)
substrate_temp      →  crystallinity       OK (물리 인과)
n2_ar_ratio         →  deposition_rate     OK (물리기반)
```

---

## 5.4 단위 통일 체크리스트

| 파라미터 | 표준 단위 | 변환 |
|---------|---------|------|
| Pressure | mTorr | Torr ×760, Pa ÷133 |
| Gas flow | sccm | lpm ×1000 |
| Temperature | °C | 그대로 (K 필요시 +273.15) |
| Thickness | nm | μm ×1000 |
| Power | W | kW ×1000 |
| Thermal cond. | W/m·K | kcal/h·m·K ÷859 |
| TBC | MW/m²·K | (확인 필수) |

---

## 5.5 데이터 일관성 검증

```python
# 1. N2/Ar 비율 검증
expected_ratio = n2_flow / (n2_flow + ar_flow)
if abs(expected_ratio - reported_ratio) > 0.05:
    flag = "⚠️ Ratio mismatch"

# 2. 증착율 검증
expected_rate = thickness_nm / deposition_time_min
if abs(expected_rate - reported_rate) > 20%:
    flag = "❌ Thickness/time inconsistent - DELETE"

# 3. 압력 범위
if pressure < 0.5 or pressure > 10:
    flag = "⚠️ Unusual pressure"

# 4. 온도 범위
if temperature < 100 or temperature > 600:
    flag = "⚠️ Unrealistic temperature"
```

---

## 5.6 배치 효과 & 반복 샘플

```markdown
## Batch Grouping (grouped k-fold CV용)

batch_1: 자체 실험 2024 (12개, 1개 장비)
batch_2: 논문 A (18개, 다른 연구실)
batch_3: 논문 B - Si 기판 (15개)
batch_4: 논문 B - Cu 기판 (10개)  ← 분리!

## 중복 샘플 처리
같은 조건이면 batch_id로 추적
→ 교차검증 시 같은 배치는 같은 폴드에 배치
```

---

## 5.7 최종 데이터 품질 보고서

```markdown
### Cleaned Dataset Summary

**통계**:
- 전체 행: 42개
- ✅ 포함: 28개 (66.7%)
- ⚠️ 조건부: 10개 (23.8%)
- ❌ 제외: 4개 (9.5%)

**제외 사유**:
1. 기본 데이터 부재 (2개)
2. 물리적으로 불가능한 k (1개)
3. XRD 정보 없음 (1개)

**조건부 포함 (플래그)**:
- oxygen_concern = True (5개)
- thickness_quality = "uncertain" (3개)
- fdtr_only = True (2개)

**배치 구성**:
- batch_1 (own): 12개
- batch_2 (paper): 18개
- batch_3 (paper): 10개 (Cu 기판 분리)
```

---

---

# PHASE 6: ML 모델링 & 디지털 트윈

## 6.1 데이터셋 크기 평가

**현재**: n_samples = 28 (조건부 10개 포함) → **소규모 데이터셋**

### 권장 모델 선택

```
n < 50: Ridge / Lasso / Gaussian Process
        ↓
        사용금지: Deep neural networks, 복잡한 앙상블
        
n = 28: 단순 기준선 모델부터 시작
        → Overfitting 방지 필수
        → Leave-one-out CV 또는 k-fold (k=5)
        → 교차검증 점수 > train 점수 모니터링
```

---

## 6.2 Feature Engineering

### Layer 1: 기본 특성 (공정 파라미터)
```
rf_power_W
dc_power_W
n2_ar_ratio
chamber_pressure_mTorr
substrate_temperature_C
```

### Layer 2: 파생 특성 (물리 기반)
```
total_power_W = rf_power_W + dc_power_W
power_density_proxy = total_power_W / chamber_pressure_mTorr
deposition_energy = total_power_W / total_gas_flow_sccm
nitrogen_enrichment = n2_ar_ratio / (1 - n2_ar_ratio)  # 질소 상대 풍부도
```

### Layer 3: 구조 특성
```
texture_coefficient_tc           (c축 배향)
columnar_morphology_score        (미시구조)
rms_roughness_nm                 (표면)
oxygen_at_percent                (불순물)
```

---

## 6.3 모델 선택

### 기준선 모델 (Baseline)

**1. Ridge Regression**
```
규칙화: L2 penalty on weights
장점: 단순, 과적합 방지
예상 R²: 0.65~0.75
```

**2. Random Forest (n_estimators=50)**
```
트리 깊이: max_depth=4
장점: Non-linearity 포착, feature importance 제공
예상 R²: 0.72~0.82
```

### 고급 모델 (n > 30인 경우)

**3. XGBoost**
```
n_estimators: 100, max_depth: 3
learning_rate: 0.05
장점: Gradient boosting, 강력한 예측
예상 R²: 0.75~0.85
```

**4. Gaussian Process Regression**
```
커널: RBF (Radial Basis Function)
장점: 불확실성 정량화 가능
예상 R²: 0.70~0.80
```

---

## 6.4 교차검증 전략

```
Dataset size: n=28

추천: 5-fold cross-validation (grouped)
├─ Fold 1: test batch_1 (12개), train others (16개)
├─ Fold 2: test batch_2_part1 (9개), train others (19개)
├─ Fold 3: test batch_2_part2 (9개), train others (19개)
├─ Fold 4: test batch_3 (5개), train others (23개)
└─ Fold 5: test 무작위 (5개), train (23개)

보고:
  - MAE (Mean Absolute Error)
  - RMSE (Root Mean Squared Error)
  - R² (train / validation)
  - 교차검증 평균 점수
```

---

## 6.5 물리 일관성 검증

**모든 예측값이 다음을 만족하는지 확인하세요:**

```
1. Deposition rate should not increase 
   under fully poisoned conditions (N2/(N2+Ar) > 0.7)
   
2. Higher substrate temperature may improve adatom mobility
   → Crystallinity ↑, k ↑ (일반적)
   
3. Better c-axis orientation (TC ↑)
   → cross-plane k ↑ (가능, 보장 X)
   
4. Oxygen contamination (> 5%)
   → k ↓ (phonon scattering ↑)
   
5. Columnar structure + low oxygen
   → k ↑ (가능성 높음)
```

**위배 사항 발견 시**: 모델 재검토, 데이터 누수 확인

---

## 6.6 Feature Importance 분석

**Random Forest / XGBoost에서 자동 생성**

```python
# 예시
feature_importance = {
    'texture_coefficient_tc': 0.35,      ← 가장 중요
    'rms_roughness_nm': 0.18,
    'oxygen_at_percent': 0.15,
    'substrate_temperature_C': 0.12,
    'n2_ar_ratio': 0.10,
    'columnar_morphology_score': 0.08,
    'rf_power_W': 0.02,
}
```

### 해석
- TC > 0.35 → **c축 배향이 k의 주요 결정인자**
- Oxygen > 0.15 → **산소 오염이 중요한 열전달 병목**
- RF power < 0.05 → **공정 power보다 결과 구조가 더 중요** (물리적 타당)

---

## 6.7 Active Learning & 다음 실험 제안

### 모델 불확실성이 높은 영역

**Gaussian Process의 예측 분산 활용**:
```
high uncertainty region 1: N2/(N2+Ar) = 0.55, substrate_temp = 350°C
  → 이 영역의 몇 개 샘플 추가
  → 모델 성능 ↑

high uncertainty region 2: thickness transition (300~500 nm)
  → 두께 450 nm 샘플 추가
  → 임계 두께 식별
```

### 우선순위 실험 (다음 5개 샘플)

```
1. N2/(N2+Ar) = 0.55, T=350°C, 500nm  (uncertainty ↓)
2. Thickness = 450 nm (transition 영역)
3. RF power = 180 W (낮은 영역 탐색)
4. Cu/AlN TBC (특수 구조)
5. Oxygen content 제어 (산소 영향 정량화)
```

---

## 6.8 디지털 트윈 v1 아키텍처

```
┌─────────────────────────────────────────────┐
│         Process Inputs                      │
│  (RF power, N2/Ar, pressure, temp, time)   │
└────────────┬────────────────────────────────┘
             │
      ┌──────▼────────┐
      │  ML Model v1  │
      │  (trained on  │
      │  28 samples)  │
      └──────┬────────┘
             │
  ┌──────────┼──────────┐
  │          │          │
  ▼          ▼          ▼
Prediction: k (W/m·K)  [with ±uncertainty]
Expected XRD: TC (0~1)
Expected SEM: columnar_score (0~1)

┌─────────────────────────────────────────────┐
│      Validation Loop                        │
│  - New experiment vs prediction             │
│  - MAE, RMSE tracking                       │
│  - Residual analysis                        │
└─────────────────────────────────────────────┘

Next: Collect 10~15 new samples → v2 재학습
```

---

## 6.9 모델 성능 보고서 템플릿

```markdown
## ML Model Performance Report

### Dataset
- Total samples: 28
- Training: 22-24 (k-fold)
- Test: 4-6 per fold
- Features: 12 (공정 8 + 구조 4)

### Best Model: Random Forest
- n_estimators: 50
- max_depth: 4
- Hyperparameter tuning: Grid search (CV 기반)

### Cross-Validation Results
- MAE: 4.2 W/m·K
- RMSE: 5.8 W/m·K
- R² (mean): 0.78 ± 0.08
- R² (train): 0.85

### Feature Importance (Top 5)
1. texture_coefficient_tc: 35%
2. oxygen_at_percent: 18%
3. rms_roughness_nm: 15%
4. substrate_temperature_C: 12%
5. columnar_morphology_score: 8%

### Physical Consistency
✅ Higher TC → Higher k (as expected)
✅ Higher O → Lower k (as expected)
⚠️ RF power weak signal (post-hoc verified by 구조)

### Limitations
- Small dataset (n=28)
- Batch effects present (grouped CV mitigates)
- Cu/AlN TBC data sparse (n=3)

### Recommendations for v2
1. Collect 10~15 new samples (uncertain regions)
2. Expand Cu/AlN TBC data
3. Add frequency-dependent k (FDTR)
4. Re-train with n=40~50
```

---

---

# 📊 종합 실행 체크리스트

## Phase 1: 공정 설계
- [ ] 실험 계획 공정 파라미터 테이블 작성
- [ ] Target poisoning 평가 완료
- [ ] Plasma stability 확인
- [ ] Arcing 위험도 판정

## Phase 2: 샘플 선별
- [ ] 모든 샘플 XRD + SEM 스크리닝
- [ ] Tier 분류 완료 (Tier 1: 8~12개)
- [ ] 샘플 로드맵 작성
- [ ] 다음 측정 순서 결정

## Phase 3: 구조 특성화
- [ ] XRD 정규화 및 TC 계산
- [ ] SEM 두께 측정 (3점 평균)
- [ ] AFM 거칠기 측정
- [ ] XPS 산소 정량화 (Tier 1만)
- [ ] TEM 분석 (극단값만)

## Phase 4: 열수송 측정
- [ ] TDTR 캘리브레이션 완료
- [ ] Tier 1 샘플 TDTR 측정 (3회 반복)
- [ ] k 및 TBC 값 정리
- [ ] FDTR 보충 측정 (필요시)

## Phase 5: 데이터 통합
- [ ] 모든 원본 데이터 수집
- [ ] 단위 통일 완료
- [ ] 일관성 검증 (ratio, rate, pressure)
- [ ] XRD 강도 정규화
- [ ] 산소 게이트 적용
- [ ] 최종 데이터셋 (n=28~40)

## Phase 6: ML 모델링
- [ ] Feature engineering 완료
- [ ] Ridge / Random Forest / XGBoost 학습
- [ ] 5-fold grouped CV 평가
- [ ] Feature importance 분석
- [ ] 물리 일관성 검증
- [ ] 다음 실험 우선순위 제안

---

# 🎯 Success Criteria

| 지표 | 목표 | 판정 |
|------|------|------|
| **Tier 1 샘플** | 8개 이상 | ✅ 달성 시 Phase 4 진행 |
| **XRD TC** | > 0.85 (최소 5개) | ✅ 우수한 c축 배향 확보 |
| **SEM 공공도** | < 3% (Tier 1) | ✅ 조밀한 막 구조 |
| **산소 < 5%** | Tier 1의 80% 이상 | ✅ 공정 안정성 입증 |
| **TDTR k 범위** | 30~100 W/m·K | ✅ 기대값 범위 |
| **ML R²** | > 0.75 (CV) | ✅ 예측 모델 신뢰도 |
| **물리 일관성** | 모든 trend 타당 | ✅ 메커니즘 이해도 |

---

# 참고: 제외 사항 (Active Scope 외)

❌ **이 프로젝트에서는 다루지 않습니다:**
- 강유전성, piezoelectric 특성
- TFT 소자 응용, 메모리 동작
- SAW 필터, MEMS 공명기
- AAO (음극산화)

⚠️ **만약 이런 주제가 제기되면:**
→ 별도의 미래 연구 방향으로 분류하고
→ 현재 프로젝트와 혼합하지 않음

---

**이 가이드를 따라 순차 진행하면, 15~20주 내에 AlN 열수송 프로젝트의 첫 번째 버전 완성이 가능합니다.**

**문제가 생기거나 단계별 세부 사항이 필요하면, Phase 번호와 함께 질문하세요.**
