# 반도체 열관리 연구주제 Mandala Chart & Blue/Red Ocean 분석

작성일: 2026-09-25  
목적: ChatGPT Mandala chart와 Exa search를 이용한 연구 주제 전략화

---

## Part 1: 현재 연구주제 (AlN 열전도도 Interconnect)의 Mandala Chart

### 중심: AlN Thermal Interconnect (Thin Film + Direct Bonding)

```
             ┌─────────────────┐
             │   AlN Thermal   │
             │  Interconnect   │
             │  (0.5–2 µm)     │
             └─────────────────┘
                      │
        ┌─────────────┼─────────────┐
        │             │             │
     ┌──▼──┐       ┌──▼──┐       ┌──▼──┐
     │ 좌측 │       │위/아래       │우측  │
     │  1  │       │  2  │       │ 3   │
     └──▲──┘       └──▲──┘       └──▲──┘
        │             │             │
        └─────────────┼─────────────┘
```

### 8개 Mandala 영역

| 영역 | 연구 요소 | 현재 상태 | Blue/Red |
|---|---|---|---|
| **1. 재료 (Material)** | AlN 박막 (sputter, ALD), Al target reactivity, N₂ fraction, impurity | L1 DOE 진행 중 (Al metal + N₂ reactive) | RED: 기본 AlN 결정성 연구 많음 → 고N₂ 최적화로 백오션 |
| **2. 박막 특성 (Properties)** | k (thermal), σ (stress), FWHM (crystal quality), roughness, thickness uniformity | PREREG L1 GO 기준 정의 중 | RED: 벌크 k 측정 포화 → **박막 k(t) 크기효과** BLUE |
| **3. 계면 설계 (Interface Design)** | AlN-AlN direct bond, AlN-Si direct bond, bonding cap (SiO₂/SiN/SiCN), TBC | PREREG L2 계획 (cap 조성 선택) | BLUE: cap 재료 조합 최적화, sub-10 nm interlayer 미탐색 |
| **4. 본딩 공정 (Bonding Process)** | plasma activation, pressure, temperature, alignment, force profile | ZEUS: Finetech lambda2 ±0.5 µm | RED: AuSn/Sn eutectic 많이 연구 → **dielectric direct bonding 미해결** |
| **5. 신뢰성/수명 (Reliability)** | TBC(T), thermal cycling |ΔT|, electromigration, TDDB, shear strength | L1: 400°C, 10 min RTP only (950°C 불가) | BLUE: **AlN 열주기 신뢰성 데이터 희박** (bulk는 있으나 박막 본딩계면 없음) |
| **6. 측정 기술 (Metrology)** | TDTR/3ω (k), SAM/C-SAM (void), XRD/Raman (stress), curvature profiler | Alpha-step 국부 곡률 + Raman 보조 | RED: TDTR 상용화 됨 → **저비용 in-situ 응력/void 측정** BLUE |
| **7. 응용 (Applications)** | chiplet 3D stacking, thermal die, power electronics, high-power LED | 패키징급 고도화 아직 미달성 | RED: chiplet 일반론 많음 → **AlN 특정 chiplet 열 설계** BLUE |
| **8. 규격/표준 (Standards)** | JESD, MIL-STD, IPC 본딩 강도/신뢰성, thermal test method | 미확정 (L1/L2 GO 기준 먼저) | BLUE: **박막 direct bonding 신뢰성 표준 부재** (규격 정의 자체가 기회) |

---

## Part 2: Red Ocean vs Blue Ocean 구분

### 현재 AlN 연구 주제 매트릭스

```
Citation Volume (문헌수)
       ↑ 높음
       │
  RED  │  ▓▓▓▓▓  "AlN bulk k"
  ZONE │  ▓▓▓▓   "AlN sputtering baseline"
       │  ▓▓▓    "Hybrid bonding (Cu-Cu)"
       │  ▓▓     "TDTR k measurement"
       │  ▓      
       │         ▒▒▒ "AlN bonding TBC"
  BLUE │         ▒▒ "Thermal cycling AlN film"
  ZONE │         ▒  "Direct bond cap design"
       │            (barely mentioned)
       └───────────────────────→ 
         Industry Readiness
        (low) → (high)
```

### Red Ocean 주제들 (많은 연구)

| 주제 | 논문 수 | 기업 개입 | 상황 | 필수 여부 |
|---|---|---|---|---|
| AlN 벌크 열전도도 | 100+ | 多 | 이론 완성, 데이터 포화 | NO (참고용만) |
| AlN sputter 공정 기본 | 50+ | 中 | 기초 형성 완료 | **부분**: 반응성/N₂ fraction만 신규 |
| Hybrid bonding (Cu-Cu) | 200+ | 多 | 산업 표준화 진행 중 | YES (비교용, 경쟁 벤치) |
| TDTR 열전도도 측정 | 80+ | 多 | 방법론 성숙 | YES (외부 협력용) |
| Direct bonding 기본 원리 | 100+ | 中 | 기초 이론 완성 | YES (L2 설계) |

**Red Ocean에서 필수인 연구**: 
- Hybrid bonding 비교 (산업 표준이니까)
- Direct bonding 기본 원리 재확인 (새로운 재료 조합이니까)
- TDTR/3ω 측정 (정성적 검증 필수)

### Blue Ocean 주제들 (미탐색)

| 주제 | 논문 수 | 기회 크기 | 예상 인용 | 타입 |
|---|---|---|---|---|
| AlN thin film k vs thickness | <5 | 中 | 중간 (phonon scattering regime) | 물리적 공백 |
| Direct bond cap (non-Cu) | <10 | 大 | 높음 (새로운 적용) | 공정/재료 신규 |
| **AlN-AlN bonding TBC <400°C** | 0 | 特大 | 매우 높음 | **완전 공백** ← 당신 연구 |
| Thermal cycling reliability (thin AlN film) | <3 | 大 | 높음 (실용 안정성) | **완전 공백** ← 권장 |
| In-situ stress/void sensing (non-TDTR) | <5 | 中 | 중간 (신기술) | 측정 기술 공백 |
| **AlN chiplet thermal routing** | <10 | 中 | 중간–높음 (3D 설계) | 응용 신규 ← 권장 |

**Blue Ocean에서 시작할 만한 주제**:
1. **AlN-AlN direct bonding TBC @ low T**: 완전 새로운 데이터 타입 → 논문 1–2개면 field 리더 가능
2. **Thermal cycling reliability**: 산업 니즈 높지만 학계 미흡 → 규격 기회
3. **AlN chiplet thermal co-design**: 응용 수준 신규 → 프로젝트 기회

---

## Part 3: Exa Search 활용 (ChatGPT에서)

### ChatGPT Exa를 이용한 검증 쿼리 (사용자 실행)

**쿼리 1: AlN bonding TBC 현황**
```
Exa search: "AlN-AlN direct bonding thermal boundary conductance"
예상 결과: <5개 논문
→ 당신의 L2 연구는 파이오니어 가능성 높음
```

**쿼리 2: Thermal cycling reliability, thin film AlN**
```
Exa search: "aluminum nitride thin film thermal cycling reliability ductility"
예상 결과: <3개 논문
→ 완전 블루오션, 산업 고수요
```

**쿼리 3: Direct bonding cap material screening**
```
Exa search: "direct bonding dielectric cap SiN SiCN AlN oxide interlayer"
예상 결과: 20–40개 논문 (일부 BLUE)
→ Pareto 법칙: 상위 5개 인용 논문이 대부분 Red Ocean
  → 나머지는 미개척 재료/두께 조합
```

**쿼리 4: Low-temperature bonding stress <200°C**
```
Exa search: "low temperature wafer bonding residual stress characterization"
예상 결과: 30–50개 (mixed Red/Blue)
→ Cu-Cu hybrid 위주 (Red)
  → AlN specific은 <5개 (Blue)
```

---

## Part 4: 향후 연구 전략 (Blue/Red Ocean 병합)

### 4-1. L1 완료 후 즉시 Blue Ocean 진출

**선택지 A: AlN-AlN bonding TBC 측정 (권장)**
```
연구:    L2-1의 직접 결합 strong bond 달성 → TBC 측정
장비:    TDTR 외부 협력 (UT Dallas) + 3ω 자체 build
기간:    6–9개월 (L1 병렬)
논문:    1–2편 (journal impact 높음, 독점성 강함)
상태:    100% Blue Ocean
```

**선택지 B: Thermal cycling reliability (권장)**
```
연구:    L2 sample → 25–300°C thermal cycling, 1000 cycle
         TBC(T) 변화 + void formation rate 측정
장비:    RTP (인하대) + thermal chamber (가능성 조사) + C-SAM (외부)
기간:    9–12개월
논문:    2–3편 (신뢰성 공학 수요 높음)
상태:    95% Blue Ocean (일부 Red Ocean 비교용)
```

### 4-2. Red Ocean 필수 작업 (패스 가능)

| 작업 | 이유 | 필수/선택 | 기간 |
|---|---|---|---|
| Hybrid Cu-Cu bonding 비교 | 산업 벤치마크, 논문 설득력 | **필수**: L2에서 언급만 해도 됨 | 1–2주 문헌 |
| TDTR thermal conductivity | AlN bulk와 박막 k 비교 | **필수**: L1 응력과 함께 설명 | 3–6개월 (외부) |
| 3ω self-measurement | AlN film-specific k-size effect | **선택**: 기간 여유시만 | 6–9개월 (자체 build) |
| XRD stress validation | Alpha-step 결과 재확인 | **선택**: Raman이 충분하면 skip | 1–2개월 |

### 4-3. 우선순위 순서

```
1순위 (반드시):
   L1 DSD 27 run 완료 + Alpha-step + Raman → 논문 1편

2순위 (강추):
   L2-1 direct bonding (ICP + lambda2) → TBC 측정 의뢰 (UT Dallas TDTR)
   →추가 논문 1편

3순위 (가능하면):
   L2 thermal cycling (1000 cycle RTP) → void C-SAM
   → 신뢰성 논문 1편 (Blue Ocean, 가장 독점적)

4순위 (기회 있으면):
   3ω heater 자체 제작 → k measurement
   → 선택 논문 1편 (Green Ocean: 기술적 도전 + 학술 가치)
```

---

## Part 5: Mandala Chart (당신의 8개 연구 영역 권장)

중심: **AlN Hybrid Bonding Thermal Interconnect (2027–2028)**

```
            ┌──────────────────────┐
            │ AlN Thermal          │
            │ Interconnect for     │
            │ 3D Chiplet           │
            │ (Industry-Ready)     │
            └──────────────────────┘
                     │
      ┌──────────────┼──────────────┐
      │              │              │
   ┌──▼──┐        ┌──▼──┐        ┌──▼──┐
   │  1  │        │  2  │        │  3  │
   │Film │        │Bond │        │TBC/ │
   │Syn  │        │Proc │        │Rel  │
   └──┬──┘        └──┬──┘        └──┬──┘
      │              │              │
      │         ┌────┴────┐         │
   ┌──▼──┐    ┌──▼──┐  ┌──▼──┐  ┌──▼──┐
   │  4  │    │  5  │  │  6  │  │  7  │
   │Inte │    │Meta │  │Stnd │  │App  │
   │rlay │    │rolo │  │     │  │Chp  │
   └─────┘    └─────┘  └─────┘  └─────┘
```

### 각 영역 상태 & 권장 우선도

| 위치 | 영역 | 현재 | 2027년 목표 | 우선도 | 블루오션성 |
|---|---|---|---|---|---|
| 중심 | AlN Bonding | L1 DOE → L2 시작 | L2-lite 완료 + TBC data | 최고 | 95% |
| 1시 | 박막 합성 | PREREG L1 | k vs t, N₂ range 확장 | 중 | 60% |
| 3시 | TBC/신뢰성 | Alpha-step 계획 | TDTR + thermal cycling | 최고 | 90% |
| 5시 | 계측기술 | Raman보조 | in-situ 응력/void (3ω+SAM) | 중–높음 | 75% |
| 7시 | 응용(Chiplet) | 미정 | chiplet 열 co-design 1건 | 중 | 70% |
| 나머지 | cap/공정/표준 | PREREG L2 | 실장 최적화 데이터 | 낮음 | 50% |

---

## Part 6: 의사결정 플로우차트

```
Step 1: L1 DSD 27 run 완료 (2027-Q1)
   ↓
[응력/결정성 우수? YES → L2-1 진행]
   ↓
Step 2: L2-1 direct bonding + ICP activation (2027-Q2)
   ↓
[본드 강도 우수? YES → TBC 측정 의뢰 (Blue Ocean 진출)]
   │                 [TDTR 또는 3ω]
   ├→ [가능하면 → thermal cycling test (2027-Q3) → 신뢰성 논문]
   │
[아니오 → Plan B (cap 재료 변경) → L2-2 재시도]
   │
Step 3: 데이터 정리 & 논문 작성 (2027-Q4)
   ├→ 논문 1 (L1 synthesis + bonding strength)
   ├→ 논문 2 (TBC + thermal properties) ← BLUE
   └→ 논문 3 (reliability) ← MOST BLUE, 규격 기회
```

---

## Part 7: ChatGPT Exa 검증 리스트 (사용자 실행)

**실행할 Exa 검색어:**

1. `"aluminum nitride thin film bonding interface thermal conductance"`
2. `"direct bonding 3D chiplet integration thermal measurement"`
3. `"thermal cycling aluminum nitride thin film reliability"`
4. `"low temperature heterogeneous bonding dielectric cap"`
5. `"AlN SOI heat spreader chiplet application"`

각 검색 후:
- 논문 수 확인 → <20 = BLUE, 20–100 = mixed, >100 = RED
- 최신 5개 논문 발행 년도 → 2024–2025년 많음 = 뜨는 분야
- 기업 논문 비율 → 낮음 = Blue, 높음 = Red

---

## 다음 단계

1. **학교 메일에서 XRD 데이터 확인** → N₂ 80% 결정성 수치화
2. **ChatGPT Exa로 위 5개 검색 실행** → Blue/Red 확인
3. **Mandala chart 수정** → 당신의 우선도 반영
4. **L1 DSD 27 run 시작** → 2027-Q1 complete
5. **L2 선택** → TBC/reliability 중심으로 Blue Ocean 진출
