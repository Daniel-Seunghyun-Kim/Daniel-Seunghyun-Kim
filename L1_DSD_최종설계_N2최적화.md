# L1 DSD 최종 설계 (N₂ 최적화 반영)

## 1. N₂ 농도 80% 재평가

### 사용자 실제 데이터
- N₂ 80% (= N₂ 16 sccm / Ar 4 sccm, 총 20 sccm)
- Wurtzite AlN (002) **우수한 결정화 확인**
- 기존 PREREG 범위 25–75% 초과 → **최적값으로 재해석**

### 의미
1. **N₂ incorporation efficiency 최고** (Al metal target + N₂ reactive)
2. **산소 오염 최소화** (Ar 유량 낮으면 chamber O₂ partial pressure 낮음)
3. **compressive stress 제어 용이** (높은 N₂ ⇒ 질화도 높음 ⇒ 응력 예측 가능)

### 결론
**N₂ 농도는 고정, 80%를 기준값으로 사용**

---

## 2. 수정된 L1 DSD (최종)

### DOE 인자 (3인자 설계)
```
인자 1: RF power density
  - 2 W/cm² (약 182 W for 3-inch target)
  - 4 W/cm² (약 364 W)
  - 6 W/cm² (약 546 W)

인자 2: pressure
  - 2 mTorr
  - 5 mTorr
  - 8 mTorr

인자 3: substrate temperature
  - 50°C
  - 200°C
  - 350°C
```

### 고정 조건
```
N₂ fraction: 80% (N₂ 16 sccm, Ar 4 sccm, 총 20 sccm)
Target: Al metal 3-inch
RF bias: 0 W (사용 안 함)
RF duty cycle: 100% (현재 SOP)
RF frequency: 13.56 MHz (표준)

분할증착 SOP:
  - 0.5 µm 목표: 100 nm × 5 pass
  - 각 pass 사이 10 min cooling, Ar flow 유지
  - 재점화 전 2 min pre-sputter (Ar 20 sccm, shutter closed)

Pre-sputtering:
  - Ar 20 sccm, 90 min (chamber 상태 안정화)

Target poisoning:
  - N₂ 16/Ar 4 sccm, 30 min (N-rich AlN surface 복원)
```

### 런 수
**3 × 3 × 3 = 27 run**

### 런시트 구조
| Run | RF power (W/cm²) | Pressure (mTorr) | T_sub (°C) | Target thickness (nm) | Remarks |
|---|---|---|---|---|---|
| 1–27 | {2,4,6} | {2,5,8} | {50,200,350} | 500 | Full factorial 3³ |

---

## 3. 응력 측정 병렬 계획 (L1 GO 경로)

### Phase 1: Alpha-step 국부 곡률 (우선)
**목표**: L1 기본 응력 경향 파악

실행:
1. 각 조건 중 대표 5개 sample 선택
   - Low power, low T (2 W/cm², 50°C)
   - Mid condition (4, 5, 200)
   - High power, high T (6, 8, 350)
2. 각 sample에서 4 방위 radial scan (0°/90°/180°/270°)
3. 곡률반경 R 계산, Stoney 환산

공식:
```
Stoney: σ·t = (E·t·κ) / (6(1-ν))
여기서 κ = 1/R = 8h / L² (L=30 mm, h=bow height)
```

소요시간: 5 sample × 4 방위 × 30 min = 10 h

### Phase 2: XRD sin²ψ 가능성 조회 (병렬)
**담당**: 표준분석연구원

확인 사항:
- AlN (0002) omega rocking curve 가능한가?
- AlN (10-14) ψ-tilt measurement 가능한가?
- Stress conversion factor 문헌값 vs 실험값 비교 가능한가?

### Phase 3: Raman E2(high) 추적 (모든 sample)
**목표**: 응력 상대 변화 추적

실행:
- 모든 27 run에서 e-beam damaged region 피해서 5 spot 측정
- E2(high) peak shift Δω 기록
- 대략 3–4 cm⁻¹/GPa 환산계수 적용 (보조 지표로만)

---

## 4. RF duty cycle 미시도 문제 (향후 spin-off)

### 현재 상태
- 100% 연속 sputtering (duty cycle 조절 경험 없음)
- 과열로 인한 분할증착 강제 필요

### 향후 평가 (Phase 2)
만약 L1 기본 DOE가 응력/결정성이 우수하면:
- **50% duty cycle** (10 ms on / 10 ms off) 시험
- 기판 온도 저감 효과 측정
- N₂ incorporation efficiency 비교

별도 DOE:
```
RF duty: {50%, 100%}
고정: RF power 4 W/cm², pressure 5 mTorr, T_sub 200°C
반복: 3회
총 6 run (신속 평가용)
```

---

## 5. L1 GO 기준 재정의

### PREREG 원본 기준
```
|σ·t| ≤ 80 N/m (wafer curvature, Stoney)
|Δσ| ≤ 50 MPa (thermal cycle)
(0002) FWHM ≤ 3°
RMS ≤ 2 nm
```

### 현실 기반 수정
```
응력 측정:
  - 주 지표: Alpha-step 국부 곡률 + Stoney (±30% 신뢰도)
  - 보조: XRD sin²ψ (가능하면)
  - 추적: Raman E2(high) shift
  
GO 조건:
  1) Alpha-step |σ·t| ≤ 100 N/m (국부 편차 고려)
     또는 XRD |σ| ≤ 500 MPa (compressive)
  2) (0002) ω-rocking FWHM ≤ 3° (기존 유지)
  3) AFM RMS (5×5 µm) ≤ 2 nm (기존 유지)
  4) 열이력: RTP 400°C, 10 min → |Δσ| ≤ 50 MPa
     (기존 950°C, 2 h 어닐은 L2로 분리)
```

---

## 6. 측정 및 분석 순서

### Timeline
```
주차 1–2:  Pre-sputtering 조건 확정, 분할증착 SOP 검증
           → 3–5개 condition test run

주차 3–6:  27-run DSD 실행 (병렬: Alpha-step 10 sample 측정)
           Raman E2(high) shift 기록

주차 7:    XRD sin²ψ 표준분석연구원 의뢰 (대표 sample 3–5개)

주차 8:    데이터 정리, GO 판정, 변수 correlation 분석

주차 9–10: 필요시 확정 sample 외부 curvature 의뢰
           또는 L2로 진행
```

---

## 7. Change Log (PREREG 최종 수정)

### 배경
인하대 ATS-Sputter 현장 확인 결과, RF bias는 사용하지 않고 N₂ 농도 80%에서 우수한 AlN (002) 결정화를 달성했으므로, 3인자 DSD로 최적화. 응력 측정은 Alpha-step 국부 곡률 + 보조 방법 병렬.

### 수정 내용
1. **DSD 인자 재정의**
   - 삭제: RF bias (0/15/30 W)
   - 유지: RF power, pressure, substrate T (3인자)
   - **고정 최적값**: N₂ 80%, Al target, 분할증착 SOP

2. **응력 측정 방법**
   - Alpha-step D-500 국부 곡률 (4 방위 radial scan)
   - XRD sin²ψ (표준분석연구원, 가능시)
   - Raman E2(high) 추적 지표

3. **L1 GO 기준**
   - Alpha-step: |σ·t| ≤ 100 N/m (국부, ±30% 신뢰도)
   - XRD: |σ| ≤ 500 MPa (compressive)
   - (0002) FWHM ≤ 3°, RMS ≤ 2 nm 유지
   - 열이력: RTP 400°C, 10 min (기존 950°C 제거)

---

## 8. 남은 확인사항

| 항목 | 담당 | 우선도 |
|---|---|---|
| Ar MFC 최대 유량 확인 | 클린룸 담당자 | 높음 |
| XRD sin²ψ 가능성 | 표준분석연구원 | 높음 |
| Pre-sputtering 90 min 필요성 | 사용자 경험상 검증 | 중 |
| RF duty cycle 가능 여부 | 클린룸 담당자 | 중 (Phase 2) |
| 열이력용 RTP vs furnace | 열처리 담당자 | 중 |
