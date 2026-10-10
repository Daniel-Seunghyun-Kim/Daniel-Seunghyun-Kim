# 선행연구 데이터베이스
## AlN Sputtering Deposition & Thermal Properties (2015~2024)

**목적**: Day 2에서 수집한 논문들을 표준화된 형식으로 기록
**업데이트**: Day 2, Day 5-6, Day 9-10

---

## 빠른 참조 테이블

| # | 저자 | 연도 | 저널 | Deposition | TC or Texture | k (W/m·K) | 특이사항 | 신뢰도⭐ | 검증상태 |
|---|------|------|------|-----------|---------|----------|---------|--------|---------|
| 1 | [저자명] | [연도] | [저널] | RF/DC | [값] | [범위] | [요약] | ⭐⭐⭐⭐⭐ | ✅ |
| 2 | | | | | | | | | |
| 3 | | | | | | | | | |
| ... | | | | | | | | | |

---

## 상세 기록 양식

**각 논문마다 다음 정보를 기록하세요:**

```markdown
### Paper #1: [저자 et al., 연도]

#### 기본 정보
- **Journal**: [저널명]
- **DOI/Link**: [링크]
- **다운로드**: [ ] 확보 / [ ] 미확보
- **Full text 읽음**: [ ] YES / [ ] Partial / [ ] NO

---

#### 1. 공정 조건 (우리와 비교 가능한가?)

**Deposition Method**:
- Type: [ ] RF / [ ] DC / [ ] RF+DC
- Power: __ W
- Frequency: __ MHz
- Target material: __ (purity: __%)
- Reactive gas: N₂ (flow: __ sccm 또는 %)
- Sputtering gas: Ar (flow: __)
- Pressure: __ mTorr (또는 Pa)
- Substrate: [ ] Si / [ ] SiO₂/Si / [ ] Cu/Si / [ ] Other
- Substrate temp: __ °C
- **N₂/(N₂+Ar) ratio**: [우리 데이터와 비교 가능? YES/NO]
- Deposition time: __ min
- Film thickness: __ nm

**공정 평가**:
- [ ] 우리 범위와 유사 (RF 150-250W, N2/Ar 0.4-0.7, T 300-400°C, P 1.5-2.5)
- [ ] 우리와 다른 범위 (이유: ____)

---

#### 2. XRD & 결정학 데이터

**측정 조건**:
- X-ray source: [ ] CuKα / [ ] MoKα / [ ] Other
- Wavelength: __ Å
- Scan range: __ ~ __ °

**결과**:
- (0002) peak intensity: __ cps (또는 상대값)
- (10-10) peak intensity: __ cps
- (10-11) peak intensity: __ cps
- **Texture coefficient (TC)**: 
  - 정의: TC = I(0002) / [I(0002)+I(10-10)+I(10-11)]
  - 값: __ (우리는 0~1 범위)
  - 또는 "c-axis 강도비": I(0002)/I(10-10) = __ (환산: TC = __)
- (0002) FWHM: __ ° (결정성)
- Grain size (from XRD): __ nm

**우리 데이터와 비교**:
우리 TC 범위: 0.45 ~ 0.92
이 논문 TC: __
- [ ] 유사함 (우리 범위 내)
- [ ] 약간 높음
- [ ] 약간 낮음
- [ ] 매우 다름 (why? ___)

---

#### 3. 열전도도 측정

**측정 방법**:
- [ ] TDTR (Time-Domain Thermoreflectance)
- [ ] FDTR (Frequency-Domain Thermoreflectance)
- [ ] 3-omega method
- [ ] Flash diffusivity
- [ ] Other: __

**측정 조건**:
- Temperature: __ K (또는 °C)
- Pump wavelength: __ nm (TDTR)
- Frequency range: __ MHz (FDTR)

**결과**:
- **Thermal conductivity**: __ W/m·K
- Uncertainty/Error: ± __ % (또는 ± __ W/m·K)
- Cross-plane vs in-plane: [ ] 명시 / [ ] 미명시
- TBC (Thermal boundary conductance): __ MW/m²·K (있으면)
- TBR (Thermal boundary resistance): __ m²·K/GW (있으면)

**우리 데이터와 비교**:
우리 k 범위: 35 ~ 65 W/m·K (조건 다양)
이 논문 k: __
- [ ] 유사함 (우리 범위 내)
- [ ] 약간 높음
- [ ] 약간 낮음
- [ ] 훨씬 다름

**신뢰도 평가**:
- 측정방법 명확: [ ] YES / [ ] PARTIAL / [ ] NO
- 불확실성 명시: [ ] YES / [ ] NO
- 반복 측정: [ ] YES (n=__) / [ ] 언급 없음
- 비교 reference: [ ] 있음 / [ ] 없음
- **신뢰도 점수**: ⭐⭐⭐⭐⭐ (5/5)

---

#### 4. 마이크로구조 분석

**SEM 관찰**:
- Columnar structure: [ ] 명확 / [ ] 약함 / [ ] 없음
- Cross-section 또는 top-view: [ ] 단면 / [ ] 표면
- 기둥폭 (column width): __ nm (있으면)
- 밀도/공공도: [ ] Dense / [ ] Some voids / [ ] High porosity

**TEM (있으면)**:
- 그레인 크기: __ nm
- 계면 특성: [ ] Clean / [ ] Diffuse / [ ] Amorphous layer

**AFM (있으면)**:
- RMS roughness: __ nm
- Peak-to-valley: __ nm

---

#### 5. 불순물 & 조성

**XPS 분석** (있으면):
- O concentration: __ at%
- N concentration: __ at%
- Al concentration: __ at%
- C contamination: __ at% (있으면)

**GDOES** (있으면):
- Depth profile: [설명]

**우리 기준과 비교**:
우리 기준: O < 5% (Tier 1), O = 8-10% (⚠️ 주의)
이 논문: O = __ at%
- [ ] Good (< 5%)
- [ ] Acceptable (5-8%)
- [ ] Caution (8-10%)
- [ ] Bad (> 10%)

---

#### 6. Cu/AlN 계면 (있으면)

**Cu deposition**:
- Method: [스퍼터링/증발/도금 등]
- Thickness: __ nm
- 계면 준비: [설명]

**TBC 측정** (있으면):
- TBC: __ MW/m²·K
- 측정방법: [TDTR/FDTR/다른]
- 주요 저항: [ ] 계면 / [ ] intrinsic AlN / [ ] 둘 다

---

#### 7. 주요 발견 & 결론

**저자의 주요 결론**:
1. [결론 1]
2. [결론 2]
3. [결론 3]

**우리 데이터와의 일치도**:
- 결론 1: [ ] 일치 / [ ] 부분 일치 / [ ] 모순
- 결론 2: [ ] 일치 / [ ] 부분 일치 / [ ] 모순
- 결론 3: [ ] 일치 / [ ] 부분 일치 / [ ] 모순

**메커니즘 제시**:
- N2 비율 효과: [ ] YES / [ ] NO → [설명]
- Temperature 효과: [ ] YES / [ ] NO → [설명]
- RF power 효과: [ ] YES / [ ] NO → [설명]
- Pressure 효과: [ ] YES / [ ] NO → [설명]

---

#### 8. 이 논문의 한계

**저자 명시**:
- [한계 1]
- [한계 2]

**우리의 평가**:
- 샘플 크기: [ ] Sufficient / [ ] Limited
- System detail: [ ] 자세함 / [ ] 부족
- 재현성: [ ] 높음 / [ ] 보통 / [ ] 낮음

---

#### 9. Fabel 테스트 (Day 5-6 사용)

**Day 5-6에서 Fabel이 이 논문을 인용하거나 언급했는가?**
- [ ] YES → 인용 부분: [찾기]
- [ ] NO → Fabel이 모르는 논문?

**일치도**:
- Fabel 주장 vs 이 논문: [ ] 일치 / [ ] 부분 / [ ] 불일치

---

#### 10. 최종 신뢰도 평가

**우리가 이 논문을 믿을 수 있는가?**

| 항목 | 점수 | 비고 |
|------|------|------|
| 측정 엄밀성 | ⭐⭐⭐⭐⭐ / 5 | 불확실성, 반복 측정 |
| 공정 조건 명확성 | ⭐⭐⭐⭐ / 5 | 우리와 비교 가능 정도 |
| 결과의 대표성 | ⭐⭐⭐ / 5 | 샘플 수, 범위 |
| 재현성 | ⭐⭐⭐ / 5 | 다른 그룹이 따라할 수 있나 |
| **종합** | ⭐⭐⭐⭐ / 5 | 참조 가치 |

**사용 권장**:
- [ ] HIGH (4-5점): 우리 Discussion에 직접 인용 가능
- [ ] MEDIUM (3-4점): 참고하되, 우리 데이터와 비교 후 언급
- [ ] LOW (<3점): 배경 정보만, 정량값은 주의

---

### 예시: Paper #1 완성된 기록

```markdown
### Paper #1: Park et al., 2022

#### 기본 정보
- **Journal**: Applied Surface Science
- **DOI**: 10.1016/j.apsusc.2022.xxxxx
- **다운로드**: ✅ 확보
- **Full text 읽음**: ✅ YES

---

#### 1. 공정 조건

**Deposition Method**:
- Type: ✅ RF (13.56 MHz)
- Power: 200 W
- Target: Al (99.99%, 2 inch)
- Reactive gas: N₂ (rate: 50%, 우리의 0.50 = match!)
- Sputtering gas: Ar
- Pressure: 2.0 mTorr ✅ (우리 범위 1.8-2.2)
- Substrate: ✅ Si (100)
- Substrate temp: 300°C ✅
- Film thickness: 500 nm ✅

**공정 평가**: ✅ 우리 범위와 정확히 일치!

---

#### 2. XRD 데이터

**측정**:
- X-ray: CuKα
- Scan: 20~60°

**결과**:
- I(0002): 8500 cps
- I(10-10): 1000 cps
- **TC**: 8500/(8500+1000+500) = 0.88 ✅ (우리 0.88과 일치!)
- (0002) FWHM: 1.8°

**우리와 비교**: ✅ 거의 동일 (우리 0.88)

---

#### 3. 열전도도

**측정**: TDTR (488 nm pump)
- **k = 45 ± 2 W/m·K** ✅ (우리 45.2와 거의 같음!)
- 온도: 300 K

**신뢰도**: ⭐⭐⭐⭐⭐ (TDTR 표준 방법, 반복 n=3)

---

[... 나머지 섹션 작성 ...]

#### 9. Fabel 테스트

**Fabel이 이 논문 언급?**: 아마도 NO (Park 2022는 최근)

**하지만**: Park의 N2=50% 조건 → TC=0.88 결과는
우리 Fabel 예측과 정확히 일치!
→ Fabel의 메커니즘 설명 검증됨 ✅

#### 10. 최종 평가

| 항목 | 점수 |
|------|------|
| 측정 엄밀성 | ⭐⭐⭐⭐⭐ |
| 공정 명확성 | ⭐⭐⭐⭐⭐ |
| 결과 대표성 | ⭐⭐⭐⭐ |
| 재현성 | ⭐⭐⭐⭐⭐ |
| **종합** | ⭐⭐⭐⭐⭐ |

**권장**: ✅ HIGH - 직접 인용 가능
```

---

## Day 2-11 진행 상황

### ✅ 수집 상태

```
목표: 10개 논문 수집
현재: __/10 논문

검색 데이터베이스:
- [ ] Google Scholar (keyword: AlN sputtering thermal)
- [ ] ScienceDirect
- [ ] Springer Link
- [ ] ResearchGate
- [ ] ArXiv
- [ ] 대학 라이브러리

진행중 논문:
1. [ ] [저자명, 연도]
2. [ ] 
...
```

### Day 9-10 검증 통계

```markdown
## 메타분석 결과

### N2/(N2+Ar) 비율 vs TC (c축 배향)

[수집한 모든 논문 플롯]

논문 1: N2=0.40 → TC=0.90
논문 2: N2=0.50 → TC=0.88
논문 3: N2=0.60 → TC=0.75
논문 4: N2=0.70 → TC=0.45
우리: [범위 표시]

**결론**: N2 ↑ → TC ↓ (모든 논문 일치)
**문헌과 우리 일관성**: ✅ 100% 일치

---

### RF Power vs TC

[유사 플롯]

**결론**: [합성]

---

### Temperature vs TC

[유사 플롯]

**결론**: [합성]

---

### 열전도도 비교

논문 k 범위: 30~70 W/m·K
우리 k 범위: 35~65 W/m·K
**일치도**: ✅ 높음

---

### 신뢰도 종합

| 메커니즘 | 논문 합의도 | 우리 데이터 검증 | 최종 판정 |
|---------|----------|------------|--------|
| N2 효과 | 10/10 ✅ | ✅ YES | 매우 확실 |
| T 효과 | 7/10 ⚠️ | ~ WEAK | 약함 |
| RF 효과 | 8/10 | ✅ YES | 확실 |
| Pressure 효과 | 3/10 | ~ 미확인 | 불명확 |

```

---

## 검색 팁 (Day 2)

```markdown
### Google Scholar 키워드

주요 검색:
"AlN sputtering" AND "thermal conductivity"
"AlN magnetron" AND "c-axis"
"aluminum nitride" AND "TDTR"
"AlN" AND "RF sputtering" AND "XRD"

필터:
- 연도: 2015-2024 (최신 우선)
- 언어: English
- Peer-reviewed (체크)

### 다운로드 팁

불가능하면:
1. ResearchGate에서 저자에게 요청 (3일 소요)
2. 대학 라이브러리 VPN 접근
3. ArXiv preprint 검색
4. PubMed 또는 오픈 액세스 버전

### 읽기 순서

1. Title, Abstract (2분) → 우리 관련도?
2. Figures (3분) → 데이터 형식 확인
3. Methods (5분) → 공정 조건, 측정 방법
4. Results & Discussion (10분) → 정량값
5. Conclusion (2분) → 주요 메시지
```

---

**모든 논문을 위 양식으로 기록한 후**  
**Day 5-6의 메커니즘 검증과 Day 9-10의 Fabel 신뢰도 평가에 사용하세요.**
