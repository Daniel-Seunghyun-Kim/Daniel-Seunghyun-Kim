# 부가 실험 상세 계획 (TDTR / 3ω / Laser Etching)
## 2027–2028 논문 완성을 위한 측정 기반 구축

작성일: 2026-09-25  
기반: TDTR Al-Al bonding, 3ω heater pattern 제작, 레이저 식각 의뢰

---

## Part 1: TDTR 측정용 Al-Al Bonding 공정

### 1-1. TDTR 원리 & 필수 조건

**TDTR의 기본 구성:**
- Picosecond pump pulse → Al transducer on sample surface에서 가열
- Probe pulse → Al reflectivity 변화 감지 (T 변화와 선형)
- Lock-in 신호 → layered thermal model fitting으로 k, TBC 추출

**필수 요건:**
1. **Al transducer**: 50–100 nm 두께 (80 nm 표준)
   - 균일한 증착 필수 (±5 nm)
   - 표면 거칠기 <15 nm RMS (평면도 중요)

2. **하층 샘플 표면:**
   - RMS roughness <15 nm
   - Optical flatness 필수 (micron scale bow 불가)

3. **문제**: AlN + Si bonding 후 Al transducer를 어디에 증착?

### 1-2. 우리의 시나리오: Al-Al Bonding (새로운 접근)

**Background:** 기존 논문은 Al transducer를 direct-bonded AlN-Si 위에 직접 증착

**우리의 전략:** **Al-Al 동종 본딩을 통해 AlN-Si 샘플 위에 Al transducer 부착**

**Step-by-step:**

#### Step 1: AlN-Si Direct Bonding 수행 (L2-1 standard)
```
1a. ICP activation (O₂ + Ar plasma, 50-100 W bias 최소)
1b. AlN + Si wafer 또는 4-inch die 표면 활성화
1c. Contact bonding (25°C, 3 min light contact)
1d. Vacuum annealing 80°C, 3 h
1e. Thermocompression bonding 200°C, 1000 N, 4 h
    → 기존 PREREG L2-1과 동일
```

#### Step 2: Al-Al Bonding을 통한 Al transducer 부착
```
재료: 
  - 상부: Al foil (99.99%, 50 µm thick) 또는 sputter Al film (200 nm on carrier)
  - 하부: AlN-Si bonded sample의 clean surface

공정:
2a. AlN-Si 샘플 (bonded) 표면 세정
    - Solvent clean (acetone → IPA → DI water)
    - Dry N₂ blow
    
2b. 표면 활성화 (선택적, 강도 향상)
    - Option A: Ar FAB (Ar ion beam) 2 min
    - Option B: 그대로 진행 (물리 접촉만)
    
2c. Al foil or sputter Al film을 bonding head로 접촉
    - Contact pressure: 100–500 N
    - Temperature: 50–150°C (저온, Al 손상 최소화)
    - Duration: 3–10 min
    
2d. **결과**: Al-Al bonded joint
    - mechanical locking (Al-Al diffusion 최소, pure contact)
    - TDTR measurement에서 Al transducer 역할
```

**기술적 도전:**
- Al-Al bonding 강도가 약할 수 있음 (diffusion 없이)
- 해결: Epoxy 또는 Au/Au flash layer로 보강

#### Step 3: TDTR 측정
```
표준 설정 (Stanford 기준):
- Pump wavelength: 800 nm (Ti:Sapphire)
- Probe wavelength: 400 nm (SHG)
- Modulation frequency: 1–10 MHz
- Time delay range: 0.1 ns – 10 µs
- Sample configuration:
  ┌─────────────────┐
  │ Al transducer   │ ← TDTR transducer (80 nm)
  │ (Al-Al bonded)  │
  ├─────────────────┤
  │ AlN film (0.5-2 µm) ← 측정 대상
  ├─────────────────┤
  │ Si substrate    │
  └─────────────────┘
```

### 1-3. TDTR 샘플 준비 타임라인

| Phase | Task | Duration | 인하대 가능 | 외부 의뢰 |
|---|---|---|---|---|
| **L2-1** | AlN-Si direct bonding | 1–2주 | ✓ | — |
| **Pre-TDTR** | Bonded sample 표면 준비 | 1주 | ✓ | — |
| **Al deposition** | Al transducer (sputter or evap) | 1–2일 | ✓ (sputter 가능) | — |
| **Al-Al bonding** | Al foil or Al film 부착 | 1–2일 | ✓ (다이본더 활용) | — |
| **Polishing** (Optional) | Surface polish if needed | 1주 | ◐ (외부 | ✓ |
| **TDTR measurement** | — | 2–3주 | ✗ | **UT Dallas 또는 국내** |

**국내 TDTR 가능 기관:**
- 서울대 나노과학공학센터 (SNUCEM)
- KAIST 신소재공학과
- 고려대 신소재공학과
- 대구경북과학기술원 (DGIST)

**예상 비용:** 시편당 150–300만 원, 7–14일 소요

---

## Part 2: 3ω Heater Pattern 제작

### 2-1. 3ω 기본 구조

**3ω 측정 원리:**
```
AC current (frequency ω) → Metal heater에 흐름
                         ↓
Joule heating → Temperature oscillation (frequency 2ω)
                         ↓
Metal resistance 변화 → Voltage 3ω 성분 발생
                         ↓
Lock-in amplifier로 3ω signal 추출
                         ↓
Frequency sweep (ω = 10 Hz – 100 kHz) → ln(ω) plot
                         ↓
기울기에서 thermal conductivity k 계산
```

**필수 요소:**
1. **Line heater**: 금속 선, 길이 10–20 mm, 폭 1–10 µm, 두께 50–200 nm
2. **4-point probe contacts**: 
   - 2개 outer leads: AC current input
   - 2개 inner leads: voltage measurement
3. **Insulation layer** (optional): Al 위에 SiO₂ 또는 SiN (50 nm) → 전기 절연

### 2-2. 3ω Heater 설계 (AlN 박막용)

**우리의 구조:**
```
┌─────────────────────────────────┐
│ Au/Ti heater (100 nm Au + 5 nm Ti) │ ← 하단
├─────────────────────────────────┤
│ AlN film (0.5–2 µm, 우리 L1 sample) │ ← 측정 대상
├─────────────────────────────────┤
│ Si substrate (525 µm)           │
└─────────────────────────────────┘
```

**Heater 설계 파라미터:**
| 파라미터 | 값 | 이유 |
|---|---|---|
| Heater length (L) | 10–13 mm | 횡방향 열 확산 고려 |
| Heater width (W) | 2–4 µm | 해상도 & 제조 가능성 |
| Heater thickness | 100 nm (Au: 95nm + Ti: 5nm) | 표준 |
| Probe spacing | 2–4 mm apart | 전압 측정 안정성 |
| Frequency range | 10 Hz – 100 kHz | AlN k ~80 W/mK일 때 적절 |

**온도 계산 (예상):**
- 10 mW bias current 가정
- ΔT ~ 0.1–0.5 K (Joule heating)
- 3ω signal ~ mV level (lock-in으로 감지)

### 2-3. 3ω Heater 제작 로드맵

#### 방법 A: 인하대 클린룸 자체 제작 (권장)

**공정 흐름:**
```
Step 1: 기판 준비 (1일)
  - AlN 0.5 µm sample on Si substrate
  - 표면 RMS < 2 nm (AFM 확인)
  - 표면 세정 (solvent clean + O₂ plasma)

Step 2: Photo/E-beam lithography (1일)
  - Photoresist 코팅 (AZ1512 또는 유사)
  - Mask 또는 E-beam lithography로 pattern
  - 목표: 2–4 µm wide line heater, 13 mm length
  - Requirement: NNFC/KANC mask 또는 인하대 photolithography

Step 3: Metal deposition (1일)
  - Ti 5 nm 접착층 (e-beam evaporator)
  - Au 95 nm (e-beam evaporator 또는 sputter)
  - 인하대 고진공 열증착기 (DKOLTH-8-2) 가능!

Step 4: Lift-off (1일)
  - Acetone bath에서 resist 제거
  - 초음파 세정 (조심스럽게)
  - 결과: Au line heater on AlN/Si

Step 5: 검증 (2–3일)
  - Optical microscope: geometry 확인
  - SEM: edge profile & width 확인
  - 4-point probe: resistance 측정
  - 목표 저항: 100–1000 Ω (주파수별 impedance matching 고려)

Step 6: 테스트 실행 (2–3주)
  - Lock-in setup (기존 또는 신규 구성)
  - 주파수 sweep
  - 3ω signal 추출
```

**인하대 장비 활용:**
| 장비 | 설치 위치 | 용도 | 비용 |
|---|---|---|---|
| Spin coater | 클린룸 | Photoresist 코팅 | 무료 |
| Mask aligner (MA6) | 클린룸 | Lithography | 40K₩/시간 |
| E-beam evaporator | 클린룸 | Ti/Au deposition | 60–120K₩/시간 |
| Optical microscope | 클린룸 | 패턴 확인 | 무료 |
| 4-point probe | 클린룸 | 저항 측정 | 20K₩/시간 |

**총 소요 비용:** ~300–500만 원, 소요 기간 1–2개월

#### 방법 B: 외부 기관 의뢰 (빠른 옵션)

**후보:**
- KANC (한국나노기술원, 수원) - Lithography + metal deposition
- NNFC (나노종합기술원, 대전) - 유사 서비스
- 서울대 공동기기원 - 학생 우대 가능

**비용:** 시편당 100–200만 원, 3–4주 소요

### 2-4. 3ω 측정 시스템 (Lock-in 기반)

**필요 장비:**
1. **AC signal generator**: 10 Hz – 100 kHz, low distortion <0.1%
2. **Lock-in amplifier**: Zurich Instruments HF2LI 또는 SR830
3. **Temperature controller**: 샘플 T 제어 (RT – 400°C)
4. **Probe station**: 4-point contact on heater

**예상 비용:**
- Lock-in: 5–10만 달러 (공동 구매 가능)
- Temperature stage: 1–2만 달러
- 기타: ~2000달러

**인하대 현황:** 확인 필요 (기존 3ω setup 유무)

---

## Part 3: Laser Etching 기관 (한국 기준)

### 3-1. Micro-channel 제작 요구사항

**목표:** Direct-bonded AlN-Si 구조 내 1–2 mm × 10–50 µm 마이크로채널 형성

**기술 요건:**
- Resolution: <10 µm (채널 정확도)
- Aspect ratio: 5–20:1 (폭 대비 깊이)
- 재료: AlN (경도 높음, 식각 어려움) + SiO₂ cap (상대적 쉬움)
- 정확도: ±5 µm tolerance (sealing 신뢰성)

### 3-2. 한국 내 Laser Etching 가능 기관

#### 기관 1: NNFC (나노종합기술원, 대전)
- **정식명**: 나노종합기술원 (National NanoFab Center)
- **주소**: 대전시 유성구 버드나루로 373
- **연락처**: (042) 366-1600
- **가능 서비스**:
  - Excimer laser (KrF, ArF) ablation
  - Femtosecond laser (fs-laser) micromachining
  - Lithography + reactive ion etching (RIE) 조합
- **적합성**: 
  - AlN 식각 가능 (CF₄ RIE 등)
  - 마이크로채널 10–50 µm 가능
  - 정확도: ±3–5 µm
- **비용**: 샘플당 100–200만 원
- **소요 시간**: 2–3주
- **접근성**: **높음** (산학협력 기관 가능)

#### 기관 2: KANC (한국나노기술원, 수원)
- **정식명**: 한국나노기술원 (Korea Nanotech Center)
- **주소**: 경기도 수원시 영통구 이의동
- **연락처**: (031) 888-1000
- **가능 서비스**:
  - Picosecond laser ablation
  - Lithography + ICP etching
  - CNC micromachining (보조)
- **적합성**: 
  - AlN/SiO₂ 식각 가능
  - 마이크로채널 가능
  - 정확도: ±5–10 µm
- **비용**: 샘플당 150–250만 원
- **소요 시간**: 2–3주
- **접근성**: **중간** (산학협력팀 문의)

#### 기관 3: 서울대 공동기기원
- **정식명**: 서울대학교 공동기기원
- **주소**: 서울시 관악구 대학로 1 (신공학관 지하)
- **연락처**: (02) 880-1700
- **가능 서비스**:
  - Femtosecond laser micromachining (구성 중)
  - ICP etching (상세 가능)
  - E-beam lithography + RIE 조합
- **적합성**: 
  - AlN 식각: 중간 (주로 Si/SiO₂ 중심)
  - 학생 우대 (저가)
- **비용**: 샘플당 50–100만 원 (학생 할인)
- **소요 시간**: 3–4주
- **접근성**: **높음** (학생 협력 용이)

#### 기관 4: KAIST 미세가공센터
- **정식명**: KAIST 창의적 설계제작센터
- **가능 서비스**:
  - Laser ablation (Nd:YAG, CO₂)
  - Micro-precision machining
- **적합성**: 
  - 마이크로채널 가능
  - 정확도: ±10 µm (상대적 낮음)
- **접근성**: **중간** (외부 협력 제약)

#### 기관 5: 경북대 첨단공정센터
- **주소**: 대구시 북구 대학로 80
- **가능 서비스**: Excimer laser + RIE 조합
- **적합성**: 높음 (AlN 경험)
- **비용**: 150–200만 원
- **접근성**: **낮음** (지역 제약)

### 3-3. 권장 전략

**Tier 1 (1순위): NNFC**
- 가장 정확도 높음 (±3–5 µm)
- 산학협력 우호적
- 비용 합리적
- **선택 이유**: 마이크로채널 신뢰성 최우선

**Tier 2 (2순위): 서울대 공동기기원 + KANC**
- 비용 절감
- 빠른 주기 (ICP etching)
- 병렬 진행 가능 (이중 sample set)

**예상 타임라인:**
```
2027-06: 기관 문의 & 견적 (1주)
2027-06: Sample 준비 (2주)
2027-07: 1차 etching 의뢰 (2–3주)
2027-07~08: 결과 평가 & 재etching (필요시, +2주)
2027-08: 최종 sample 확보
```

---

## Part 4: 종합 부가 실험 타임라인

### 4-1. TDTR + 3ω + Laser 병렬 일정

```
2027-Q1 (Jan–Mar): L1 DSD 완료 + 측정
  ├─ L1 DSD 27 run 수행
  ├─ Alpha-step, Raman, XRD 측정
  ├─ 3ω heater 설계 & lithography 준비
  └─ Paper 1 draft

2027-Q2 (Apr–Jun): L2-1 direct bonding + 부가 실험 시작
  ├─ L2-1 AlN-Si direct bonding 10–20 samples
  ├─ Al-Al bonding (TDTR transducer 부착) 5 samples
  ├─ 3ω heater 제작 병렬 (5 samples)
  ├─ TDTR 의뢰 (5 samples → UT Dallas 또는 국내)
  ├─ Laser etching 기관 문의 & 1차 샘플 준비
  └─ Paper 2 draft (bonding + preliminary k data)

2027-Q3 (Jul–Sep): TDTR 결과 + Laser etching + 3ω 측정
  ├─ TDTR 결과 수신 (2–3주 후)
  ├─ 3ω 측정 시작 (lock-in 기반)
  ├─ Laser etching 1차 완료 & 평가
  ├─ Thermal cycling test 병렬 시작 (1000 cycle)
  ├─ OpenFOAM CFD simulation (마이크로채널)
  ├─ Paper 2 완성 (bonding + TBC + k data)
  └─ Paper 3 draft (reliability + simulation)

2027-Q4 (Oct–Dec): Micro-channel prototype + 최종 데이터
  ├─ Laser etching 2차 개선 (필요시)
  ├─ Thermal cycling 500–1000 cycle 완료
  ├─ CFD thermal-fluid-stress coupling 완성
  ├─ Paper 3 완성 (reliability + void analysis)
  ├─ Paper 4 draft (micro-channel design)
  └─ **Papers 2–3 제출 준비**
```

### 4-2. 비용 & 일정 요약

| 항목 | 비용 | 기간 | 담당 |
|---|---|---|---|
| **TDTR (Al-Al bonding + transducer)** | 500–800만 원 | 2주 의뢰 | UT Dallas or 국내 |
| **3ω heater (설계 + 제작)** | 300–500만 원 | 6–8주 | 인하대 클린룸 |
| **3ω 측정 (lock-in setup)** | 500만–1000만 원 (shared) | 2–3주 | 인하대 또는 협력 |
| **Laser etching** | 500–700만 원 | 3–4주 의뢰 | NNFC 또는 서울대 |
| **Thermal cycling test** | 200–300만 원 | 8–12주 | 인하대 또는 외부 |
| **CFD simulation** | 0 (오픈소스) | 2–3개월 | 인하대 HPC |
| **총 예상** | **3000–4000만 원** | **6–9개월** | 병렬 진행 |

---

## Part 5: 실행 체크리스트

### 즉시 (2026-09-26 ~ 2026-10-15)
- [ ] NNFC 담당자 연락 (laser etching 기술 상담)
- [ ] KANC 담당자 연락 (lithography + etching 견적)
- [ ] 서울대 공동기기원 문의 (femtosecond laser 현황)
- [ ] 인하대 고진공 열증착기 (DKOLTH-8-2) 사용 가능성 확인
- [ ] TDTR 의뢰 기관 선정 (UT Dallas vs 국내)

### 10월 (2026-10)
- [ ] 3ω heater 설계 완료 (mask 또는 e-beam lithography 준비)
- [ ] TDTR Al-Al bonding 공정 테스트 1–2 samples
- [ ] Al transducer 증착 공정 최적화

### 2027-Q1 (2027-01 ~ 2027-03)
- [ ] L1 DSD 27 run 완료
- [ ] 3ω heater 제작 5 samples (인하대)
- [ ] TDTR 의뢰 기관과 계약 (SOP 확정)

### 2027-Q2 (2027-04 ~ 2027-06)
- [ ] L2-1 bonding 15–20 samples (TDTR 용 + 3ω용 + laser etching용)
- [ ] Al-Al bonding 5 samples → TDTR 의뢰 (UT Dallas 또는 국내)
- [ ] Laser etching 1차 의뢰 (NNFC 또는 서울대)
- [ ] 3ω 측정 시작 (parallel)

### 2027-Q3 ~ Q4 (2027-07 ~ 2027-12)
- [ ] TDTR 결과 분석
- [ ] 3ω 완전 측정 완료
- [ ] Thermal cycling test 완료
- [ ] CFD simulation 최종화
- [ ] Papers 2–3–4 제출

---

## 최종 목표

**2027년 말 기준:**
- ✅ L1 complete (synthesis + characterization)
- ✅ L2-1 direct bonding + TBC measured (TDTR)
- ✅ Thermal conductivity k measured (3ω 또는 external TDTR)
- ✅ Reliability assessed (thermal cycling + void analysis)
- ✅ Micro-channel design & CFD validated

**논문 제출:**
- Paper 1 (L1): 2027-02
- Paper 2 (L2 + TBC): 2027-05
- Paper 3 (Reliability): 2027-09
- Paper 4 (Micro-channel): 2028-02

**산업 응용:** TSMC/Intel chiplet 개발과 parallel하게 실제 제품 검증 가능
