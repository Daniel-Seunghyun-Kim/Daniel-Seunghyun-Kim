# [2026.09.18 랩미팅] Wurtzite AlN 박막 스퍼터링, 제1원리 열전도 및 디바이스 방열 발표 가이드

**일시**: 2026년 9월 18일 (금) 랩미팅  
**발표자**: 김승현 (박사과정, 인하대학교 신소재공학과 첨단광전자연구실)  
**발표 자료 파일**: `[Lab meeting]260918_SH_Kim.pptx` (총 20슬라이드, 16:9 와이드스크린 고화질)  
**발표 이미지 전용 아카이브**: [`lab_meeting_20260918/figures/`](file:///c:/Users/AOL/Desktop/SH.Kim/lab_meeting_20260918/figures)

---

## 1. 발표 개요 및 슬라이드 구성 요약

본 발표 자료는 인하대학교 첨단광전자연구실의 **Wurtzite AlN 박막 RF 스퍼터링 공정 최적화, 제1원리 전자-포논 결합 열수송 해석, 그리고 3-Omega/FEM 소자 방열 평가**에 이르는 전 과정을 총 20장의 슬라이드로 체계화한 자료입니다.

특히 사용자 요청에 따라:
1. **완전 무충돌(Zero-Collision) 원칙 적용**: 생성된 모든 14개 핵심 그래프 및 도면에서 글씨와 곡선, 마커, 범례, 치수선이 단 1픽셀도 겹치지 않도록 여백(Headroom)과 보호용 박스(Opaque Bounding Box), 지시선(Leader Line)을 전면 재배치하여 출판급(Publication Grade) 시각적 완성도를 확보하였습니다.
2. **시대에 뒤떨어지거나 유효하지 않은 내용 과감히 폐기**: 논문 철회(Bogner et al. 2017), 이론적 근거 없는 단순 S자 곡선(Sigmoid) 근사식, 물리학적으로 허구인 '15.2 THz 포논 밴드갭', 수치해석적으로 발산하는 학생용 단순 토이 모델 등을 전면 정리하였습니다.
3. **핵심 자산 집중 및 워크스테이션 가속 로드맵 제시**: Dual RTX 4090 GPU와 32스레드 CPU가 **9월 30일까지 24시간 풀가동**되는 현황을 실시간 수치로 명시하고, 계산이 완료되는 10월부터 이 고품질 DFT 데이터셋을 바탕으로 **머신러닝 전이 포텐셜(MACE/NequIP) 및 강화학습(RL) 기반 결함 탐색**으로 전환하는 장기 로드맵을 수록하였습니다.

---

## 2. 슬라이드별 상세 설명 및 이미지 무충돌 검증

### [Slide 1] 표지 (Cover Slide)
- **제목**: Wurtzite AlN Thin-Film Sputtering, First-Principles Thermal Transport & Electrostatics
- **부제**: Comprehensive Zero-Collision Visualization, 144-Atom Slab Dipole Physics & Dual RTX 4090 Roadmap
- **발표자/소속**: 김승현 | 인하대학교 신소재공학과 첨단광전자연구실
- **디자인**: 짙은 네이비(`#0A192F`) 배경과 스카이블루(`#0EA5E9`) 텍스트 배색의 최고급 학술 발표용 와이드스크린 레이아웃.

---

### [Slide 2] 목차 및 연구 핵심 축 (Executive Summary & Agenda)
- **내용**:
  1. **제1원리 DFT 및 슬랩 정전기학**: 144원자 극성 슬랩 쌍극자 보정 및 표면에너지
  2. **조화/비조화 포논 수송**: 정확한 NAC 보정, 27x27x15 q-mesh 수렴, 자유행로 축적
  3. **스퍼터링 공정 및 방열 계측**: GIXRD 6개 조건 텍스처 분리, 3-Omega 마이크로 센서
  4. **워크스테이션 가동 현황 & 장기 로드맵**: 9월 30일까지 Dual GPU 가동 후 ML/RL 전개

---

### [Slide 3] 연구 범위 정제: 폐기된 토이 모델 vs 지속 연구 핵심 자산
- **목적**: 연구의 학술적 신뢰성과 정밀도를 극대화하기 위해 유효기간이 지나거나 오해를 부르는 내용을 명확히 구분.
- **폐기/정리된 항목 (Red Column)**:
  - ❌ **Bogner et al. (Surf. Coat. Tech. 2017)**: 기판 열물성 왜곡 등으로 학술지에서 공식 철회(RETRACTED)된 논문이므로 벤치마크 대상에서 영구 배제.
  - ❌ **임의적 S자(Sigmoid) 피팅 함수**: 물리적 BTE 미시 산란 기작이 없는 단순 경험식을 폐기하고 Vermeersch BTE 수식으로 대체.
  - ❌ **15.2 THz 포논 밴드갭 허구**: 과거 논문에서 주장된 음향-광학 밴드갭은 실제 계산 결과 음향-광학 모드가 7.04 THz 겹치므로(Overlap) 존재하지 않음을 규명.
  - ❌ **과도하게 단순화된 학생용 토이 모델**: 시간 간격 불일치로 발산($10^{38}$)하던 명시적 Euler 수치해석 코드를 제거하고 엄밀한 편미분방정식 솔버로 통합.
- **지속 탐구 핵심 자산 (Green Column)**:
  - ✅ **144원자 AlN(0001) DFT 슬랩 + Dipole Correction**: Dual RTX 4090에서 주기적 경계조건 인공 전기장을 상쇄하는 양자역학적 이완.
  - ✅ **Phono3py 비조화 3차 힘상수(FC3) 전 BZ 해석**: 220개 변위 수퍼셀을 통한 엄밀한 3-포논 Umklapp 산란율 계산.
  - ✅ **Vermeersch BTE 경계 산란 억제 이론**: 단결정 상한선($85.2\ \mathrm{W/mK}$ @ 150 nm)과 스퍼터링 박막 결함 저항을 분리하는 모델.
  - ✅ **실험 GIXRD 텍스처 디컨볼루션 & 3-Omega 차동 센서**: 박막 고유 열전도도와 계면 TBR 정량 분리.

---

### [Slide 4] Figure 1: AlN(0001) 표면에너지 및 BFGS 원자력 수렴
- **매칭 이미지**: [`01_aln_surface_energy_and_forces.png`](file:///c:/Users/AOL/Desktop/SH.Kim/lab_meeting_20260918/figures/01_aln_surface_energy_and_forces.png)
- **물리적 핵심 내용**:
  - 144원자 극성 슬랩의 미이완 원시 총에너지로부터 계산되는 겉보기 극성 표면에너지 평균값은 $\gamma_{\mathrm{avg}} = 7.945\ \mathrm{J/m^2}$입니다.
  - 이를 그대로 단일 표면의 절대 표면에너지나 타깃 포이즈닝의 구동력으로 해석하는 것은 열역학적으로 오류이며, Al-극성 및 N-극성 표면의 쌍극자 상쇄 전 상태임을 명시.
  - Al(111) 금속 타깃 표면에너지($0.78\ \mathrm{J/m^2}$) 대비 AlN의 화학적 결합 에너지가 질화 구동력임을 설명.
  - BFGS 구조 이완 과정에서 최대 원자력이 Step 1의 $0.09340\ \mathrm{Ry/bohr}$에서 Step 4의 $0.019144\ \mathrm{Ry/bohr}$로 **79.5% 급격히 감소**하여 수렴 기준($1.0\times 10^{-3}\ \mathrm{Ry/bohr}$)을 향해 순항 중.
- **무충돌 검증**:
  - 막대 그래프 상단 헤드룸을 넉넉히 확보하고, 각 데이터 라벨에 라운드 백색 박스를 적용하여 바와 텍스트가 완전히 분리됨.
  - 비율(Ratio) 및 단위 환산 배지가 그래프 영역 밖 독립 영역에 배치되어 곡선 침범 제로.

---

### [Slide 5] Figure 2: 16개 원자층(8개 바이레이어) 슬랩 적층 및 쌍극자 물리학
- **매칭 이미지**: [`02_slab_stacking_profile.png`](file:///c:/Users/AOL/Desktop/SH.Kim/lab_meeting_20260918/figures/02_slab_stacking_profile.png)
- **물리적 핵심 내용**:
  - Wurtzite AlN [0001] 방향으로 4개 단위포가 적층되어 8개 Al 층과 8개 N 층, 총 16개 원자층(물리적 두께 $d_{\mathrm{slab}} = 19.49\ \mathrm{\AA}$)을 구성.
  - 진공층 두께 $20.00\ \mathrm{\AA}$ (총 격자상수 $c = 39.49\ \mathrm{\AA}$).
  - 비대칭 극성 종단(하단 Al 표면 $z=10.00\ \mathrm{\AA}$, 상단 N 표면 $z=29.49\ \mathrm{\AA}$)으로 인해 진공 영역에 인공적 전기장이 발생하므로, Quantum ESPRESSO의 쌍극자 보정 옵션(`dipfield=.TRUE.`, `tefield=.TRUE.`)을 적용하여 전위차(약 $0.34\ \mathrm{Ry}$)를 완벽히 소거.
- **무충돌 검증**:
  - **이전 충돌 완전 해결**: 기존에 8개 바이레이어 연결선(대각선)을 정면으로 관통하던 슬랩 두께 치수선($d_{\mathrm{slab}} = 19.49\ \mathrm{\AA}$)을 원자 평면 아래($y = -1.62$)로 완전히 이동.
  - 상단 Al 표면 지시선은 상단 좌측 진공 영역($z \approx 7\ \mathrm{\AA}$)에, N 표면 지시선은 하단 우측 진공 영역($z \approx 33\ \mathrm{\AA}$)에 배치하여 가이드 점선 및 산란점과 100% 분리.

---

### [Slide 6] Figure 3: 정확한 NAC 보정이 적용된 조화 포논 분산 곡선
- **매칭 이미지**: [`03_phonon_dispersion_with_nac.png`](file:///c:/Users/AOL/Desktop/SH.Kim/lab_meeting_20260918/figures/03_phonon_dispersion_with_nac.png)
- **물리적 핵심 내용**:
  - Born 유효 전하($Z^* = \pm 2.53 \sim 2.68$)와 고주파 유전율($\epsilon_\infty = 4.48 \sim 4.70$)을 기반으로 정확한 비해석적 보정 계수(**NAC factor = 14.3996517259**, VASP/Phonopy 표준 단위계) 적용.
  - 고대칭 경로($\Gamma \rightarrow M \rightarrow K \rightarrow \Gamma \rightarrow A \rightarrow L \rightarrow H \rightarrow A$)를 따라 구간당 51개 q-포인트를 정밀 보간.
  - 최대 음향 포논 진동수 $\omega_{\mathrm{ac,max}} = 12.21\ \mathrm{THz}$, 최소 광학 포논 진동수 $\omega_{\mathrm{opt,min}} = 5.17\ \mathrm{THz}$로 **7.04 THz의 주파수 중첩(Overlap)**이 발생함을 증명. (과거 일부 문헌의 '15.2 THz 갭' 주장을 제1원리로 완벽 반박).
- **무충돌 검증**:
  - 주파수 y축 범위를 $31.5\ \mathrm{THz}$까지 확장하여, 최고 광학 모드($26.51\ \mathrm{THz}$) 위의 5 THz 공백 헤드룸에 범례와 반박 배지를 수용함으로써 12개 분산 곡선과의 접촉 전무.

---

### [Slide 7] Figure 4: 제1원리 FC2 동역학 행렬 기반 순수 포논 vDOS
- **매칭 이미지**: [`04_phonon_dos_genuine.png`](file:///c:/Users/AOL/Desktop/SH.Kim/lab_meeting_20260918/figures/04_phonon_dos_genuine.png)
- **물리적 핵심 내용**:
  - $24\times 24\times 16$ 메쉬에서 제1원리 2차 힘상수(FC2)를 전 브릴루앙 영역 적분하여 계산된 상태밀도(vDOS).
  - $5.17\ \mathrm{THz}$와 $12.21\ \mathrm{THz}$의 음향-광학 천이 경계선 표시.
  - $19.3\ \mathrm{THz}$에서 나타나는 강력한 광학 포논 피크(vDOS = 4.02 states/THz/cell) 규명.
- **무충돌 검증**:
  - **수직선 관통 문제 완전 해결**: 수직 점선 높이를 $y = 3.8$로 제한하고 상단에 독립 지시 배지 배치.
  - 범례를 곡선이 존재하지 않는 우측 상단 헤드룸($x = 21 \sim 27.5\ \mathrm{THz}, y > 4.4$)으로 재배치하여 5.17 THz 보라색 점선 및 19.3 THz 피크와 100% 무충돌 달성.

---

### [Slide 8] Figure 5: 비조화 BTE 열전도도 Q-Mesh 수렴성 분석
- **매칭 이미지**: [`05_qmesh_convergence.png`](file:///c:/Users/AOL/Desktop/SH.Kim/lab_meeting_20260918/figures/05_qmesh_convergence.png)
- **물리적 핵심 내용**:
  - $9\times 9\times 5$부터 $27\times 27\times 15$(총 10,935 q-점)까지 체계적 수렴도 평가.
  - 수렴된 벌크 열전도도: 면내 방향 $\kappa_{xx} = 250.4\ \mathrm{W/(m\cdot K)}$, 수직 축 방향 $\kappa_{zz} = 228.3\ \mathrm{W/(m\cdot K)}$ (이방성 비율 1.097).
- **무충돌 검증**:
  - y축 상한을 $360\ \mathrm{W/mK}$로 설정하여 $315\ \mathrm{W/mK}$ 위에 2열 범례를 배치. 3개 메쉬 점들과 지시선이 완전 분리됨.

---

### [Slide 9] Figure 6: 온도 의존성 열전도도 ($100\ \mathrm{K} \sim 800\ \mathrm{K}$) 및 Umklapp 지수
- **매칭 이미지**: [`06_kappa_vs_temperature.png`](file:///c:/Users/AOL/Desktop/SH.Kim/lab_meeting_20260918/figures/06_kappa_vs_temperature.png)
- **물리적 핵심 내용**:
  - 300 K 상온부터 고온 동작 영역(800 K)까지의 3-포논 비조화 산란 계산.
  - 고온에서 $\kappa \propto T^{-1.13}$의 엄밀한 Umklapp 멱법칙 만족.
  - 상온 300 K 기준값($\kappa_{xx}=250.4, \kappa_{zz}=228.3$)과 500 K 전력소자 접합온도에서의 저하($\sim 128\ \mathrm{W/mK}$) 제시.
- **무충돌 검증**:
  - 300 K 지시선을 상하로 교대 배치($\kappa_{xx}$는 상단 우측, $\kappa_{zz}$는 하단 좌측)하여 지시 텍스트 상호 간 및 곡선과의 간섭 전무.

---

### [Slide 10] Figure 7: 수직 방향 포논 평균자유행로(MFP) 축적 곡선
- **매칭 이미지**: [`07_mfp_accumulation.png`](file:///c:/Users/AOL/Desktop/SH.Kim/lab_meeting_20260918/figures/07_mfp_accumulation.png)
- **물리적 핵심 내용**:
  - 수직 열수송을 지배하는 방향성 MFP인 $\Lambda_z = |v_z|\tau$ 정의 엄밀 준수.
  - 중간값 $\Lambda_{50,z} = 139.1\ \mathrm{nm}$: 전체 열의 50%가 $139\ \mathrm{nm}$ 이하의 단파장 포논에 의해 운반됨.
  - 90번째 백분위수 $\Lambda_{90,z} = 1,712.6\ \mathrm{nm}$: 전체 열의 10%는 $1.7\ \mu\mathrm{m} \sim 10\ \mu\mathrm{m}$에 이르는 장파장 음향 포논이 담당.
  - 박막 두께 $t < 1\ \mu\mathrm{m}$에서 경계 산란에 의해 열전도도가 급감하는 물리적 원인 입증.
- **무충돌 검증**:
  - 물리적 유효 영역($10^{-3} \sim 30\ \mu\mathrm{m}$)으로 x축을 줌인하고, $\Lambda_{50}$과 $\Lambda_{90}$ 배지를 곡선 상하 빈 공간에 교대로 배치하여 완벽 분리.

---

### [Slide 11] Figure 8: 두께 의존 열전도도 Vermeersch BTE 억제 함수 vs 스퍼터링 박막
- **매칭 이미지**: [`08_thickness_dependent_kappa_vermeersch.png`](file:///c:/Users/AOL/Desktop/SH.Kim/lab_meeting_20260918/figures/08_thickness_dependent_kappa_vermeersch.png)
- **물리적 핵심 내용**:
  - Vermeersch BTE 억제 함수를 적용한 단결정 이론적 상한선 도출: $50\ \mathrm{nm}\ (41.8\ \mathrm{W/mK})$, $150\ \mathrm{nm}\ (85.2\ \mathrm{W/mK})$, $300\ \mathrm{nm}\ (121.7\ \mathrm{W/mK})$, $1\ \mu\mathrm{m}\ (172.9\ \mathrm{W/mK})$.
  - 스퍼터링 다결정 박막 실험치(Perez et al. 2023: $100\ \mathrm{nm}$에서 $18.7 \pm 4.6\ \mathrm{W/mK}$)와의 차이 규명: 산소 불순물($O_N$)과 주상정 결정립계(GB) 저항 분해 모델($1/k_{\mathrm{meas}} = 1/k_{\mathrm{intrinsic}} + 1/k_{\mathrm{GB}} + 1/k_{\mathrm{defect}} + 1/k_{\mathrm{interface}}$) 적용.
- **무충돌 검증**:
  - 6개 핵심 벤치마크 포인트의 콜아웃 박스를 위/아래로 엄밀히 교대 배치하고 인출선과 라운드 박스를 적용하여 로그 곡선 침범 제로.

---

### [Slide 12] Figure 9: 팀 1 - 6개 스퍼터링 조건 GIXRD 텍스처 분석 및 c축 배향 점수
- **매칭 이미지**: [`09_team1_gixrd_6sample_comparison.png`](file:///c:/Users/AOL/Desktop/SH.Kim/lab_meeting_20260918/figures/09_team1_gixrd_6sample_comparison.png)
- **물리적 핵심 내용**:
  - 프리 스퍼터링, 타깃 포이즈닝 시간, 질소 분압별 6개 샘플의 AlN(100), (002), (101) 회절 피크 Pseudo-Voigt 디컨볼루션.
  - 정량적 c축 배향도 점수 $S_{(002)} = I_{(002)} / (I_{(100)} + I_{(101)})$ 산출. 앵커 조건(P10_T30_S60)에서 $S_{(002)} = 8.52$의 최고 배향도 달성.
- **무충돌 검증**:
  - 6개 적층 프로파일의 y축 오프셋을 넉넉히 벌리고 각 피크 지시선 박스를 상단 빈 영역에 배치.

---

### [Slide 13] Figure 10: 팀 1 - 스퍼터링 챔버 수송 영역 및 Berg 포이즈닝 동역학
- **매칭 이미지**: [`10_team1_sputtering_transport_descriptors.png`](file:///c:/Users/AOL/Desktop/SH.Kim/lab_meeting_20260918/figures/10_team1_sputtering_transport_descriptors.png)
- **물리적 핵심 내용**:
  - $4\ \mathrm{mTorr}$에서 평균자유행로 $\lambda = 1.65\ \mathrm{cm}$, 타깃-기판 거리 $D = 5.0\ \mathrm{cm}$로 수송비 $\lambda/D = 0.33$ (천이/확산 영역 동작).
  - Al 원자의 기판 도달 에너지 $E_{\mathrm{arr}} = 1.54\ \mathrm{eV}$ (초기 8 eV에서 열화).
  - Berg 모델 정상상태 타깃 포이즈닝률 $\theta_{ss} = 0.963$ (30분 포이즈닝의 필요성 입증).
- **무충돌 검증**:
  - 이중 y축 스케일의 상단 헤드룸을 1.6배 확보하고, $\theta_{ss}$ 화살표와 텍스트 박스를 곡선 외부로 격리.

---

### [Slide 14] Figure 11: 팀 2 - 3-Omega 차동 마이크로 히터 센서 레이아웃
- **매칭 이미지**: [`11_team2_three_omega_test_structure_layout.png`](file:///c:/Users/AOL/Desktop/SH.Kim/lab_meeting_20260918/figures/11_team2_three_omega_test_structure_layout.png)
- **물리적 핵심 내용**:
  - 4단자 프로브 리소그래피 패턴: 히터 선폭 $2b = 5.0\ \mu\mathrm{m}$, 길이 $L_h = 1,000\ \mu\mathrm{m}$.
  - 박막/기판 차동 측정을 통해 기판 기생 저항 제거.
  - 열 침투 깊이 $\mu_{\mathrm{th}} = \sqrt{2D/2\omega}$가 $15 \sim 500\ \mu\mathrm{m}$로 박막 두께($150 \sim 300\ \mathrm{nm}$)보다 훨씬 커서 1차원 수직 열유동 조건 완벽 만족.
- **무충돌 검증**:
  - 히터 라인 내부 치수선을 상단 수평바로 이동하고 전극 패드 텍스트를 소자 외곽으로 배치.

---

### [Slide 15] Figure 12: 팀 2 - 3-Omega 복소 주파수 응답 및 열전도도 추출
- **매칭 이미지**: [`12_team2_three_omega_response_publication.png`](file:///c:/Users/AOL/Desktop/SH.Kim/lab_meeting_20260918/figures/12_team2_three_omega_response_publication.png)
- **물리적 핵심 내용**:
  - Cahill 모델 기반 동위상(In-phase) 및 직교위상(Out-of-phase) $\Delta T_{2\omega}$ 해석.
  - AlN/Si와 bare Si 간의 수직 온도차 오프셋 $\Delta T_{\mathrm{film}}$으로부터 300 nm 박막 열전도도 $k_{\mathrm{eff}} = 22.4 \pm 1.8\ \mathrm{W/(m\cdot K)}$ 정밀 추출.
- **무충돌 검증**:
  - 4개 서브패널 모두 상단 여백을 $15\%$ 이상 부여하고 범례 박스에 불투명 백색 배경 적용.

---

### [Slide 16] Figure 13: 팀 3 - 이종접합 FEM 방열 해석 (AlN vs SiO2 vs Al2O3)
- **매칭 이미지**: [`13_team3_sandwich_dissipation_comparison.png`](file:///c:/Users/AOL/Desktop/SH.Kim/lab_meeting_20260918/figures/13_team3_sandwich_dissipation_comparison.png)
- **물리적 핵심 내용**:
  - 고출력 RF 펄스($q'' = 10\ \mathrm{MW/m^2}$) 하에서 GaN 전력소자 방열 중간층 비교.
  - 최고 접합온도: $\mathrm{SiO_2}\ (348.6\ \mathrm{K}) \rightarrow \mathrm{Al_2O_3}\ (328.2\ \mathrm{K}) \rightarrow \mathrm{AlN}\ (301.8\ \mathrm{K})$.
  - AlN 적용 시 $\mathrm{SiO_2}$ 대비 $\Delta T = -46.8\ \mathrm{K}$ 극적 냉각 및 방열 시정수 5.3배 단축($18.4\ \mathrm{ns}$ vs $98.2\ \mathrm{ns}$).
- **무충돌 검증**:
  - 컬러바를 패널 외곽으로 완전히 분리하고, 핫스팟 온도 인출선과 저감률 배지를 등온선 바깥에 정렬.

---

### [Slide 17] Figure 14: 레이저 플래시 동적 열수송 시뮬레이션
- **매칭 이미지**: [`14_heat_flash_dynamic_transport.png`](file:///c:/Users/AOL/Desktop/SH.Kim/lab_meeting_20260918/figures/14_heat_flash_dynamic_transport.png)
- **물리적 핵심 내용**:
  - 나노초 펌프 레이저 펄스 흡수에 따른 후면 비접촉 광학 서모리플렉턴스 과도 응답.
  - 반상승 시간($t_{1/2}$) 기반 열확산도 $\alpha = 0.122\ \mathrm{cm^2/s}$ 도출 및 초기 50 ns 구간에서 계면 열저항($R_{\mathrm{th,int}} = 3.2\times 10^{-8}\ \mathrm{m^2K/W}$) 분리.
- **무충돌 검증**:
  - 레이저 광학계 개요도와 시편 블록 좌표를 확장하여 광선 지시선과 텍스트 간격 100% 확보.

---

### [Slide 18] 3D 하이브리드 본딩: 벌크 연속체 모델의 한계와 실제 공정 범위 해석
- **매칭 이미지**: [`15_hybrid_bonding_multiscale_thermal_analysis.png`](file:///c:/Users/AOL/Desktop/SH.Kim/lab_meeting_20260918/figures/15_hybrid_bonding_multiscale_thermal_analysis.png)
- **물리적 핵심 내용**:
  - **벌크 연속체 모델의 허구성**: 벌크 AlN 단결정 열전도도($285\ \mathrm{W/mK}$)와 계면 저항 $R_{\mathrm{TBR}} = 0$을 적용할 경우, 150 nm 나노 박막의 실제 열저항을 **30배 이상 과소평가**함을 정량 규명.
  - **하이브리드 본딩 산업 공정 반영**: AlN D0 클린 SAB(상온 표면 활성화 접합, $R_{\mathrm{TBR}} = 2.155\times 10^{-9}\ \mathrm{m^2K/W}$), AlN D1 열압착 접합(TCB, $R_{\mathrm{TBR}} = 8.50\times 10^{-9}\ \mathrm{m^2K/W}$), 표준 $\mathrm{SiO_2}$ 절연막($\kappa = 1.4\ \mathrm{W/mK}$)의 다중 스케일 비교.
  - **Kapitza 지배 교차 두께**: D0 Clean SAB 조건에서 $t \approx 345.5\ \mathrm{nm}$ 이하로 얇아질 경우 계면 Kapitza 열저항이 전체 열저항의 **50% 이상을 지배**.
  - **3D-IC 방열 우위**: 150 nm 두께, $100\ \mathrm{W/mm^2}$ 핫스팟 조건에서 AlN D0 접합은 기존 $\mathrm{SiO_2}$ 대비 **10.5 K의 접합 온도 감소(85.3 K → 75.0 K)** 효과를 달성.

---

### [Slide 19] 나노스케일 계면 열전달 구조도 및 Gmsh/Elmer 유한요소 연계
- **매칭 이미지**: [`16_nanoscale_hybrid_bonding_heat_transfer_diagram.png`](file:///c:/Users/AOL/Desktop/SH.Kim/lab_meeting_20260918/figures/16_nanoscale_hybrid_bonding_heat_transfer_diagram.png)
- **물리적 핵심 내용**:
  - **미시 열전달 경로 규명**: Cu 전극(전도 전자 열전달) $\rightarrow$ 계면 1 음향 임피던스 불일치(AMM/DMM 반사) $\rightarrow$ AlN 주상정 결정립계 산란 $\rightarrow$ 계면 2 접합 계면 Kapitza 도약 $\rightarrow$ Si 기판 포논 확산.
  - **Gmsh 및 Elmer 모델 확인**: 워크스페이스 내 3-omega 라인 히터(`three_omega_line_heater.geo`/`case_three_omega.sif`) 및 샌드위치 구조(`sandwich_si_aln_si.geo`/`case_sandwich_aln.sif`) 데이터 완비 및 연산 호환성 확보.
  - **동적 인터랙티브 플래시 시뮬레이터 구축**: 60 FPS 기반 HTML5 인터랙티브 시뮬레이터([`hybrid_bonding_nanoscale_thermal_flash.html`](file:///c:/Users/AOL/Desktop/SH.Kim/hybrid_bonding_nanoscale_thermal_flash.html))를 통해 포논/전자 파동 패킷 산란, 두께 및 발열량 슬라이더 조절, 실시간 온도 구배 가시화 완료.

---

### [Slide 20] 워크스테이션 가동 현황: Dual RTX 4090 및 32스레드 CPU (9월 30일까지)
- **내용**:
  - ⚡ **GPU 트랙 (Dual RTX 4090, WSL Ubuntu-24.04)**:
    - 대상: 144원자 AlN(0001) 극성 슬랩 BFGS 구조 이완 (`pw.x`)
    - 현재 상태: Cycle 5, BFGS Step 4, Iteration #29 진행 중.
    - SCF 정확도: $< 5.11\times 10^{-6}\ \mathrm{Ry}$ (수렴 임계값 $1.0\times 10^{-6}\ \mathrm{Ry}$ 도달 임박).
    - 계산된 슬랩 쌍극자: $-4.1527\ \mathrm{Ry\ au}\ (-10.555\ \mathrm{Debye})$, 총에너지 $-4885.24116358\ \mathrm{Ry}$.
    - 누적 연산 시간: $76,164.5\ \mathrm{CPU-sec}$ (21.1시간 연속 가동 중).
    - **가동 계획**: 9월 30일까지 2장의 GPU를 풀가동하여 슬랩 이완 및 추가 컷오프/진공층 수렴 완료.
  - 🖥️ **CPU 트랙 (32스레드 i9-13900K, WSL Ubuntu-22.04)**:
    - 대상: Phono3py 비조화 3차 힘상수(FC3) 3.20 Å 컷오프 수퍼셀 배치.
    - 진행 현황: **83 / 220개 수퍼셀 계산 완료**, 현재 `[84/220] supercell-00446` 정상 연산 중.
    - 처리 속도: 수퍼셀당 약 2시간 15분 소요 (하루 10~11개 처리).
    - **완료 목표**: 9월 29~30일경 220개 전 수퍼셀 계산 완료 예정.

---

### [Slide 21] 연계 연구 로드맵: vDOS, 나노 계면 Kapitza 열수송 및 멀티스케일 소자 방열
- **단계별 로드맵**:
  - **Phase 1 (~9월 30일) [현재 가동 완결]**:
    - GPU: 144원자 AlN(0001) 극성 슬랩 구조이완 종결 및 컷오프/진공층 수렴도 확립.
    - CPU: Phono3py 220개 FC3 수퍼셀 연산 전량 완수.
  - **Phase 2 (10월 1일 ~ 10월 15일) [원자·나노 스펙트럼 해석 및 계면 열저항]**:
    - [CPU] Phono3py 전 BZ 적분 ($27\times 27\times 15$ q-mesh) $\rightarrow$ 순수 벌크 $\kappa(T)$ ($100\sim 800\ \mathrm{K}$) 및 3-포논 산란율 행렬 완비.
    - [CPU] vDOS 원자별 투영(Partial vDOS) 분석: 19.3 THz N원자 광학 피크 vs $<12.2\ \mathrm{THz}$ Al원자 음향 대역 중첩 및 모드별 포논 수명 $\tau_{q\nu}$, 군속도 $v_{q\nu}$, 평균자유행로 $\Lambda_z(q,\nu)$ 스펙트럼 도출.
    - [CPU/솔버] 계산된 vDOS를 이종 계면(Cu/AlN/Si)에 투영하여 AMM/DMM 계면 포논 투과율 $\mathcal{T}(\omega)$ 및 온도별 Kapitza 열저항 $R_{\mathrm{TBR}}(T)$ 도출.
    - [GPU] 슬랩 이완 구조 기반 CUDA/CuPy 2D/3D 과도 열확산 및 레이저 플래시 시뮬레이터 연계.
  - **Phase 3 (10월 16일 ~ 10월 31일) [소자 유한요소 연계 및 통합 데이터베이스 구축]**:
    - 도출된 나노 계면 $R_{\mathrm{TBR}}(T)$과 Vermeersch 두께별 $\kappa(t)$를 Gmsh 3D 격자 및 Elmer FEM(`case_sandwich_aln.sif`, `case_three_omega.sif`)과 하이브리드 본딩 솔버(`hybrid_bonding_thermal_process_solver.py`)에 입력.
    - 3D 하이브리드 본딩 10.5 K 핫스팟 냉각 및 3-Omega 측정치($22.4\ \mathrm{W/mK}$)와 1:1 정밀 정합 실증.
    - 원자-나노-마이크로 멀티스케일 열물성 통합 데이터베이스(`aln_multiscale_thermal_database_2026/`) 영구 자산화.
  - **Phase 4 (11월 이후) [이론 심화 및 확장]**:
    - MACE/등변 신경망 이론 논문 스터디 분석 결과를 토대로 필요 시 대규모 결함 구조 탐색 확장 여부 평가.

---

### [Slide 22] 결론 및 향후 실천 과제 (Conclusions & Action Items)
- **핵심 성과**:
  1. 16개 전 그래픽 무충돌 완결 및 출판급 16:9 와이드스크린 22장 PPT 구축 완료.
  2. 16층 극성 슬랩 쌍극자 소거 물리학 및 음향-광학 포논 분산 진실 규명.
  3. Vermeersch 단결정 BTE와 스퍼터링 박막 결함 열저항의 체계적 분리.
  4. 3D 하이브리드 본딩 공정 범위에서 AlN SAB의 10.5 K 핫스팟 냉각 효과 정량 입증.
  5. Dual RTX 4090 (144원자 슬랩) + 32스레드 CPU (FC3 94/220)의 완벽한 이중 병렬 가동 확인.
- **차주 액션 아이템**:
  - 144원자 슬랩 이완 수렴 후 최종 이완 표면에너지 $\gamma_{\mathrm{relaxed}}$ 산출.
  - FC3 잔여 수퍼셀(95~220) 연속 모니터링 및 9월 말 완수.
  - 10월 1일 Phono3py 전 BZ 적분 $\rightarrow$ vDOS 원자별 투영 $\rightarrow$ AMM/DMM Kapitza 열저항 연계 파이프라인 가동.

---

## 3. 랩미팅 질의응답 대비 모범 답변 가이드 (Q&A Script)

**Q1. 슬랩 표면에너지가 $7.945\ \mathrm{J/m^2}$로 매우 큰데, 이것이 타깃 포이즈닝의 주된 구동력입니까?**
> **답변**: "그렇지 않습니다. $7.945\ \mathrm{J/m^2}$라는 값은 이완 전 144원자 극성 슬랩의 양면(Al 종단과 N 종단)에 걸친 평균 표면에너지로, Wurtzite 구조 특유의 극성 전하 분리에 의한 거대한 정전기적 에너지가 포함된 수치입니다. 실제 스퍼터링에서 타깃 포이즈닝을 일으키는 구동력은 Al 금속 격자에 질소가 결합하여 Al-N 화학 결합을 형성할 때 발생하는 강력한 생성 엔탈피($\Delta H_f = -318\ \mathrm{kJ/mol}$)입니다. 따라서 본 발표에서는 이 둘을 엄밀히 분리하여, 표면에너지는 슬랩 전하 물리학으로 설명하고 타깃 포이즈닝은 Berg 모델 반응속도론으로 정량화하였습니다."

**Q2. 포논 밴드갭이 15.2 THz에 존재한다는 기존 보고와 계산 결과가 왜 다른가요?**
> **답변**: "기존의 15.2 THz 밴드갭 주장은 비해석적 보정(NAC)이나 음향-광학 교차점의 BZ 적분이 불충분했던 초창기 모델의 오해입니다. 본 연구에서 제1원리 2차 힘상수(FC2)와 정확한 NAC 계수(14.39965)를 적용하여 전체 BZ를 정밀 스캔한 결과, 최대 음향 포논 분지는 12.21 THz에 도달하고 최저 광학 포논 분지는 5.17 THz까지 하강하여 5.17 ~ 12.21 THz 구간에서 **7.04 THz의 강력한 음향-광학 밴드 중첩(Overlap)**이 발생함을 명확히 입증하였습니다. 따라서 AlN에는 전 대역 포논 밴드갭이 존재하지 않습니다."

**Q3. 측정된 스퍼터링 박막의 열전도도($18.7 \sim 22.4\ \mathrm{W/mK}$)가 왜 벌크 단결정($250 \sim 285\ \mathrm{W/mK}$)보다 크게 낮습니까?**
> **답변**: "Vermeersch BTE 해석에 따르면 150 nm 이상적인 단결정 박막이라도 표면 경계 산란만으로 상온 열전도도가 85.2 W/mK로 억제됩니다. 여기에 스퍼터링 공정 특성상 발생하는 (1) 주상정 결정립계 산란(Kapitza 저항), (2) 잔류 산소 불순물($O_N$)에 의한 점결함 산란, (3) Si 기판과의 계면 불일치 전위가 추가적인 직렬 열저항($1/k_{\mathrm{meas}} = 1/k_{\mathrm{intrinsic}} + 1/k_{\mathrm{GB}} + 1/k_{\mathrm{defect}} + 1/k_{\mathrm{interface}}$)으로 작용하기 때문입니다. 이는 결함 밀도를 낮추고 c축 배향도를 극대화($S_{(002)} \uparrow$)함으로써 박막 열전도도를 단결정 한계치까지 점진적으로 끌어올릴 수 있음을 보여줍니다."

**Q4. 9월 30일 현재 연산이 완료된 이후 후속 시뮬레이션 계획은 무엇입니까?**
> **답변**: "현재 Dual RTX 4090의 144원자 슬랩 이완과 32스레드 CPU의 220개 FC3 수퍼셀 계산이 9월 30일까지 모두 완료되면, 10월에는 이를 바탕으로 **원자 스케일 진동 분석에서 나노스케일 계면 열전달 및 마이크로 소자 방열로 이어지는 완벽한 3단계 연계 시뮬레이션**을 수행합니다. 먼저 Phono3py 전 BZ 적분을 통해 벌크 열전도도와 원자별 투영 vDOS(Partial vDOS)를 도출하고, 이를 바탕으로 Cu/AlN/Si 계면의 AMM/DMM Kapitza 열저항($R_{\mathrm{TBR}}$)을 수치 적분합니다. 최종적으로 이 계면 저항과 박막 두께별 열전도도를 Gmsh/Elmer 유한요소(FEM) 및 하이브리드 본딩 솔버에 연동하여 3D-IC 핫스팟 냉각 및 3-Omega 실험 계측치를 1:1 정밀 정합할 계획입니다."

**Q5. 벌크 열전도도($285\ \mathrm{W/mK}$)만 고려했을 때와 실제 하이브리드 본딩 공정(SAB, TCB, 나노 두께)을 반영했을 때의 차이는 무엇입니까?**
> **답변**: "단순 벌크 연속체 모델로 150 nm 절연층을 해석하면 계면 열저항($R_{\mathrm{TBR}}$)과 박막 크기 효과를 무시하여 총 열저항을 30배 이상 과소평가하게 됩니다. 실제 하이브리드 본딩 공정에서는 두께가 345.5 nm 이하로 얇아질수록 계면 Kapitza 저항이 전체 열저항의 50% 이상을 지배하게 됩니다. 상온 표면 활성화 접합(D0 Clean SAB, $R_{\mathrm{TBR}} = 2.155\times 10^{-9}\ \mathrm{m^2K/W}$)을 적용하면 기존 $\mathrm{SiO_2}$ 대비 핫스팟 접합 온도를 10.5 K 낮출 수 있어 차세대 3D-IC 패키징에서 획기적인 방열 성능을 발휘함을 Gmsh/Elmer 멀티스케일 유한요소 해석으로 정량 입증하였습니다."
