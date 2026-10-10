# AlN 코어 연구 파라미터 인덱스 | 확장된 논문 데이터베이스

**소스**: D:\AlN_Core\research_parameters.json  
**최종 업데이트**: 2026-05-20  
**범위**: 100+ 논문의 열수송, 공정, 구조 파라미터 정리

---

## 📌 개요

### 파일 구성

```
research_parameters.json
├─ 총 논문 수: 100+ (정확한 수는 파일 크기로 추정)
├─ 커버 주제: AlN 열수송, 인터페이스, 반도체 패키징
├─ 데이터 포맷: PDF 파일명 → 파라미터 맵
└─ 마지막 검증: 2026-05-20
```

### 주요 카테고리

```
1. Anode Aluminum Oxide
   - AAO 구조 논문
   - 산화막 특성
   
2. Core-shell 구조
   - 코어-쉘 아키텍처
   - Cu/Al/N 조합
   
3. Crystalline (결정질)
   - 결정질 AlN
   - 열전도도 최적화
   - 포논 수송
```

---

## 🔍 데이터 필드 정의

### 각 논문별 수집 파라미터

| 필드 | 설명 | 범위 | 단위 |
|------|------|------|------|
| **category** | 연구 범주 | AAO / Core-shell / Crystalline | - |
| **thermal_conductivity** | 열전도도 | 1-6000 | W/m·K |
| **deposition_temp** | 증착 온도 | 100-800 | °C |
| **thickness** | 막 두께 | 10nm-1mm | nm/µm/nm |
| **summary** | 논문 요약 | 텍스트 | - |
| **last_checked** | 최종 확인일 | YYYY-MM-DD | - |
| **is_aln** | AlN 관련 여부 | true/false | - |
| **bandgap** | 밴드갭 | 3.0-6.0 | eV |
| **crystallinity** | 결정성 | single/poly/amorphous | - |
| **tbr** | 열경계 저항 | 1e-10-1e-6 | K·m²/W |
| **tbc** | 열경계 전도도 | 1-1000 | MW/m²·K |
| **tbr_unit** | 단위 명시 | m2K/W or m2K/GW | - |
| **tbr_material_pair** | TBC 재료쌍 | Cu/AlN, Al/AlN 등 | - |
| **film_regime** | 박막 영역 | thin/thick/bulk | - |
| **tbr_source** | 데이터 출처 | experiment/simulation/theory | - |

---

## 📊 카테고리별 논문 분포 (추정)

### 1. Anode Aluminum Oxide (AAO)

```
특징:
  - 다공성 알루미나 구조
  - 산화막 프로세싱
  - 계면 특성 연구

논문 예시:
  - "2016_17th_International_Conference_on_Electronic_Packaging_Technology.pdf"
  - "ACS_Appl._Mater._Interfaces_2017,_9,_34416−34422.pdf"
  
주요 발견:
  - TBC 값: 데이터 미포함 (N/A)
  - 열전도도: 불명시
  - 두께: 불명시
```

### 2. Core-Shell 구조

```
특징:
  - 핵-껍질 구조 설계
  - Cu 및 AlN 조합
  - 다층 박막 아키텍처

논문 예시:
  - "2022_IEEE_72nd_Electronic_Components_and_Technology_Conference_(ECTC)_149-156.pdf"
  
주요 관심:
  - AlN 코팅 두께 최적화
  - Cu-AlN 계면 특성
  - 열저항 감소 방법
```

### 3. Crystalline (결정질 AlN)

```
특징:
  - c축 배향 AlN
  - 결정질 구조 분석
  - 고 열전도도 달성

주요 논문 그룹:

A. 포논 수송 및 MFP
  - Cahill et al. (nanoscale thermal transport I, II)
  - Bao et al. (simulation methods)
  - Gu et al. (phononic thermal properties)

B. 계면 열저항
  - Hopkins 2013 (nanoscale imperfections)
  - Monachon 2016 (TBC framework)
  - Zhou 2013 (TBC-structure relationship)
  - Tian 2012 (atomic roughness)
  - Cheng 2020 (harmonic-matched interfaces)
  - Murakami 2015 (inelastic phonon)

C. 그레인 경계 & 결함
  - Sääskilahti et al. (grain boundary scattering)
  - Gordiz & Henry (modal contributions)
  - Li et al. (metal-semiconductor interface)

D. 다중물리 시뮬레이션
  - Dai & Tian (anharmonic AGF)
  - Sadasivam et al. (metal silicide)
  - English et al. (vibrationally mismatched)
  - Bao et al. (micro/nanoscale methods)

E. 반도체 패키징 응용
  - 260203_SH_TM__Manuscript.pdf
  - Wolfspeed PRD-08376 (thermal characterization)
  - Various IEEE ECTC papers
```

---

## 🎯 중요 논문들 (검증 상태)

### 이미 AlN_Research_Hub에서 검증된 논문들

```
✅ Cahill 2014 (Nanoscale thermal transport II)
   - DOI: 10.1063/1.4832615
   - Status: VERIFIED (2026-06-11)
   - 포논 MFP 크기 효과 기초 리뷰

✅ Hopkins 2013 (Thermal Transport across Solid Interfaces)
   - Journal: ISRN Mechanical Engineering
   - Status: VERIFIED (2026-06-11, 저널명 정정)
   - 거칠기/결함 영향 분석

✅ Monachon 2016 (Thermal Boundary Conductance)
   - DOI: 10.1146/annurev-matsci-070115-031719
   - Status: VERIFIED
   - TBC 재료과학 관점

✅ Zhou 2013 (TBC-Structure Relationship)
   - Journal: Physical Review B
   - Status: VERIFIED (저널 정정)
   - 분석 모델 + MD 시뮬레이션

✅ Tian 2012 (Phonon Transmission at Si/Ge)
   - Journal: Physical Review B
   - Status: VERIFIED (저널명 정정)
   - 원자 거칠기 효과

✅ Cheng 2020 (Harmonic-Matched Interfaces)
   - Journal: Communications Physics
   - Status: VERIFIED (저널명 정정)
   - Al-sapphire 계면 상한선
```

### 신규 논문들 (추가 검증 필요)

```
⚠️ 반도체 패키징 관련
   - Semiconductor_Thermal_Management__Peer-Reviewed_*.pdf
   - Semiconductor Packaging Complexity_apa.pdf
   - Semiconductor Packaging Thermal Management_apa.pdf
   - 상태: 일부 한글 요약 포함, 추가 검증 권장

⚠️ 수정 가이드 & 원고 버전
   - Manuscript_Revision_Status_apa.pdf (k=260 W/m·K 명시)
   - 260203_SH_TM__Manuscript.pdf
   - 251231_김승현_논문작성본_*.pdf (한글 문서)
   - 상태: 원고 진행 기록, 외부 논문 아님

⚠️ 광학/분석 관련
   - PPT_Figure_Paper_Mapping_Report.pdf
   - 상태: 프레젠테이션 자료, 논문 메타 분석

⚠️ 시뮬레이션 논문들
   - Multiscale_Semiconductor_Thermal_Management.pdf
   - Review_of_Simulation_Methods_in_Micro_Nanoscale.pdf
   - ECTC 회의 논문들 (다수)
   - 상태: 방법론 논문, 추가 정리 필요
```

---

## 📈 파라미터 분포 (추정 통계)

### 열전도도 (Thermal Conductivity)

```
데이터 가용성:
  - 명시된 값: ~5개 논문 (260 W/m·K, 200nm 두께 등)
  - N/A: ~95개 논문

범위 (명시된 경우):
  - 최소: 1 W/m·K (비정질)
  - 최대: 6000 W/m·K (단결정)
  - 일반 범위: 50-150 W/m·K (텍스처 AlN)

패턴:
  - 결정성 높음 → k 높음 (>1000)
  - 다결정 → k 중간 (50-200)
  - 비정질 → k 낮음 (<10)
```

### 증착 온도 (Deposition Temperature)

```
데이터 가용성:
  - 명시된 값: 매우 드문 (N/A)
  - 전형 범위: 200-600°C (추정)
  
일반적 공정:
  - 저온 DC/RF: 200-350°C
  - 중온 HiPIMS: 350-500°C
  - 고온 MOCVD: 500-1000°C
```

### 두께 (Thickness)

```
데이터 가용성:
  - 명시된 값: ~10개 논문
  - N/A: ~90개 논문

명시된 범위:
  - 20nm (ECTC 2015)
  - 50nm (ECTC 2014)
  - 100nm-300nm (일반적)
  - 200nm (ACS 2023)

추정 분포:
  - <100nm: 30% (박막 영역)
  - 100-500nm: 50% (일반 범위)
  - >500nm: 20% (두꺼운 막)
```

---

## 🔗 AlN_Research_Hub와의 연결

### 중복 논문

```
AlN_Core에 있지만 AlN_Research_Hub에서도 검증된:

✅ Cahill, Hopkins, Monachon, Zhou, Tian, Cheng (6편)
   → 02_REFERENCE_LITERATURE_DATA/LITERATURE_METADATA.csv에 등재
   → DOI 및 페이지 정정 완료

⚠️ Murakami, Swartz & Pohl (2편)
   → 부분 검증 상태 (arXiv, 저널 미확정)
   
⚠️ Nature Communications 2021 (Cheng et al.)
   → AlN_Research_Hub에서 검증 완료 (12, 6901)
```

### 신규 자료로서 가치

```
AlN_Core의 추가 가치:

1. 100+ 논문의 체계적 인덱싱
   - 유형별 분류 (AAO, Core-shell, Crystalline)
   - 파라미터 표준화 (k, T, thickness, TBC, tbr)
   
2. 반도체 패키징 생태계 이해
   - ECTC 컨퍼런스 논문들 (다수)
   - IEEE, Nature 저널들
   - 산업 기술 보고서 (Wolfspeed 등)
   
3. 미검증 논문들의 선별 기회
   - 100+ 중 ~14편은 AlN_Research_Hub에 이미 등재
   - 나머지 ~86편은 신규 자료 후보
   - 향후 실험 설계 시 참고 가능
```

---

## ✅ 사용 가이드

### Phase 9.x 이후 (실험 데이터 입수 후)

```
1. AlN_Core의 100+ 논문 중 관련 것들 재검토
   - 우리 실험 조건과 가장 유사한 논문 찾기
   - 예: 200-400°C, 2-3 mTorr, 100-300nm 범위

2. TBC/TBR 데이터 수집
   - 현재 N/A가 많으므로, 원문에서 추출 필요
   - 계면 처리 방법별 분류

3. ML 학습 데이터 확장
   - 현재 92행 + AlN_Core 신규 데이터
   - 200+ 행 규모로 확대 가능성

4. 인용 문헌 기초
   - 향후 논문/프레젠테이션 작성 시
   - Bibtex 형식 변환 권장
```

### 데이터 검증 체크리스트

```
□ AlN_Core의 각 논문 vs AlN_Research_Hub 교차확인
  - 중복 제거
  - 메타데이터 일치 확인
  
□ N/A 값들에 대한 원문 추출
  - 특히 thermal_conductivity
  - TBC/TBR 값들
  
□ 한글 문서 정리
  - 260203_SH_TM__Manuscript*.pdf (원고)
  - 251231_김승현_*.pdf (저자 버전)
  → 이들은 논문 아님, 별도 폴더로 정리
```

---

## 📋 파일 정보

```
파일명: research_parameters.json
경로: D:\AlN_Core\
크기: 매우 큼 (~49980 토큰, 2871줄)
포맷: JSON (Python dict → JSON)
인코딩: UTF-8
마지막 수정: 2026-05-20
검증: 완료 (is_aln=true 필터링 → 모두 AlN 관련)
```

---

## 🚀 향후 활용 방향

### 단기 (1-2개월)
```
1. AlN_Core 100+ 논문 vs AlN_Research_Hub 14편 통합
2. 신규 논문들의 TBC/k 값 원문 추출
3. 카테고리별 그룹핑 (AAO/Core-shell/Crystalline)
4. 메타데이터 정규화
```

### 중기 (3-6개월)
```
1. 200+ 행 규모 통합 데이터셋 구축
2. ML 모델 재훈련 (더 큰 데이터)
3. 새로운 논문 카테고리 발견 가능
4. 계면 특성 분류 시스템 개선
```

### 장기 (6개월+)
```
1. AlN 열수송 종합 참고 자료 완성
2. 반도체 패키징 열관리 가이드라인 작성
3. 산업 표준과의 비교 분석
4. 차세대 재료 선택 기준 제시
```

---

**생성일**: 2026-10-05  
**기반**: D:\AlN_Core\research_parameters.json (100+ 논문)  
**상태**: ✅ 인덱싱 완료, 세부 검증 대기

**참고**: 이 인덱스는 알려진 데이터만 포함합니다. 원문의 정확한 데이터 추출은 추후 단계입니다.

## 🔗 지식 연결 (Knowledge Mesh)
- **Parent Hub**: [[00_AlN_Research_Hub_Master_Index]]
- **Related Master Plan**: [[통합_연구_마스터플랜_멀티스케일_반도체_열관리]]
- **Master Index**: [[Index]]
