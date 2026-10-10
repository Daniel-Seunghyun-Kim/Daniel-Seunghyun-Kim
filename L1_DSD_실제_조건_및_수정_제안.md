# L1 DSD 실제 공정 조건 vs PREREG 재검토

조사일: 2026-09-25  
기반: ATS-Sputter 현장 확인 + 사용자 실제 운용 데이터

---

## 1. 현재 고정 조건 (실제 운영)

| 항목 | 설정값 | PREREG 원본 범위 | 상태 |
|---|---|---|---|
| **N₂ fraction** | 80% | 25–75% | 범위 초과 |
| **전체 유량** | 20 sccm | 명시 안 됨 | 낮은 편 |
| **Target 재료** | Al metal | 명시 안 됨 | reactive N₂ sputtering |
| **분할 증착** | 중간중간 정지 | 명시 안 됨 | 과열 방지 SOP |
| **RF duty cycle** | ~100% (연속) | 명시 안 됨 | 미시도, 열 누적 최대 |

---

## 2. PREREG 원본 L1 DSD vs 현실

### PREREG 명시 5인자
- RF power: 2–6 W/cm²
- N₂ fraction: 25–75%
- pressure: 2–8 mTorr
- substrate T: 50–350°C
- RF bias: 0–30 W

### 실제 운영 결과
1. RF bias: 사용 안 함 → 제거
2. N₂ fraction: 80% 고정 (범위 초과) → 범위 재검토 필요
3. RF power: 범위 내 가능
4. pressure: 범위 내 가능
5. substrate T: 범위 내 가능
6. RF duty: 미시도 → 새로운 가능 인자

---

## 3. 응력 측정 문제 (L1 GO 병목)

### PREREG L1 GO 기준
- |σ·t| ≤ 80 N/m (Stoney method, wafer curvature)
- |Δσ| ≤ 50 MPa (thermal cycle)

### 대안 4가지

#### (1) Alpha-step 국부 곡률 (가장 실용적)
- 30 mm scan을 4–5개 위치에서 수행
- 각 위치에서 곡률반경 R = (L²/8h + h/2) 계산
- Stoney 환산: σ = E·t·κ / (6(1-ν))
- 오차: ±20–30%
- 비용: 무료

#### (2) XRD sin²ψ residual stress (더 정확)
- AlN (0002), (10-14) 회절선 이용
- 표준분석연구원 Pro MRD
- 소요시간: 1–2 h/sample
- 장점: 격자 변형 직접 측정
- 단점: Stoney 방법과 다름 → Change Log 필수

#### (3) Raman E2(high) 피크 이동 (보조)
- AlN E2 mode ~3–4 cm⁻¹/GPa
- LabRAM 현재 보유
- 빠르고 비용 없음, 상대 변화만 신뢰

#### (4) 외부 wafer-curvature 기관 의뢰
- KAIST, 서울대, 고려대
- 비용: 시편당 5–10만 원
- 소요시간: 1–2주
- PREREG 정합성: 100%

---

## 4. RF duty cycle 인자 검토

### 현재: 거의 100% (연속)
- 열 누적 극대
- 과열로 인한 분할 증착 강제

### 도입 시 예상 변화
| 조건 | 기대 효과 |
|---|---|
| 50% duty | 기판 온도 저감, 결정성 개선 |
| 25% duty | 온도 제어 용이 |
| 100% (현재) | 최대 이온 흐름, 높은 compressive stress |

---

## 5. 수정된 L1 DSD 제안

### 옵션 A: 4인자 DSD (bias 제거, RF duty 추가)
- RF power density (2 / 4 / 6 W/cm²)
- pressure (2 / 5 / 8 mTorr)
- substrate temperature (50 / 200 / 350°C)
- RF duty cycle (25% / 50% / 100%)
- 런 수: 3×3×3×3 = 81 run

### 옵션 B: 3인자 + 고정 조건 (보수적)
- RF power density (2 / 4 / 6 W/cm²)
- pressure (2 / 5 / 8 mTorr)
- substrate temperature (50 / 200 / 350°C)
- 런 수: 3×3×3 = 27 run
- 고정: N₂ 80%, RF duty 100%, 분할증착 SOP

### 옵션 C: 초기 3인자 + RF duty spin-off
- 1차: 3인자 DSD 완료
- 2차: RF duty 영향도 평가

---

## 6. 응력 측정 로드맵

### Phase 1 (현재 ~ 1주)
1. Alpha-step 국부 곡률 시범 (5–10 sample, 4 방위)
2. XRD sin²ψ 가능성 조회 (표준분석연구원)

### Phase 2 (DSD 병렬)
- Raman E2(high) shift 기록 (모든 sample)

### Phase 3 (필요시)
- 외부 curvature profiler 의뢰 (5–10 sample)

---

## 7. PREREG Change Log 초안

### 수정 배경
인하대 ATS-Sputter 실제 운영 조건 확인 결과, RF bias는 사용하지 않으므로 제거하고, 현장 기반 3–4인자 DSD로 재설계. 응력 측정은 Alpha-step 국부 곡률 및 XRD sin²ψ 병렬 추진.

### 수정 내용
1. **DSD 인자 변경**
   - 삭제: substrate RF bias (0/15/30 W)
   - 추가: RF duty cycle (대기 또는 고정)
   - 유지: RF power density, pressure, substrate temperature
   - 주의: N₂ fraction 현재값 80%는 범위 초과 → 재검토 필요

2. **응력 측정 방법**
   - 주 방법: Alpha-step D-500 국부 곡률 (4 방위 radial scan)
   - 보조: XRD sin²ψ (표준분석연구원)
   - 추적: Raman E2(high) shift

3. **분할 증착 SOP**
   - 0.5 µm: 100 nm × 5 pass, 각 pass 후 10 min cooling
   - 2 µm: 3ω 시편으로 별도 (L1 DOE 제외)

4. **L1 GO 기준**
   - XRD sin²ψ 또는 Alpha-step 곡률 조합 허용
   - 열이력: |Δσ| ≤ 50 MPa (400°C, 10 min RTP 또는 furnace)

---

## 8. 남은 확인사항

| 항목 | 현황 | 우선도 |
|---|---|---|
| RF duty 효과 | 미시도 | 중 |
| N₂ fraction 80% 정당성 | PREREG 범위 초과 | 높음 |
| wafer curvature 방법 | Alpha-step/XRD/Raman 평가 | 높음 |
| 외부 기관 협력 | UT Dallas TDTR 가능성 | 중 |
