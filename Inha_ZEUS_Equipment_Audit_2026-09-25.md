# 인하대학교 3D나노융합소자연구센터 ZEUS 장비 전수조사

조사일: 2026-09-25  
조사범위: 센터 공식 장비목록 및 연결된 ZEUS 등록 페이지. ZEUS가 명시하지 않은 사양은 추정하지 않고 `미확인`으로 기록.

## 1. AlN L1 DOE 관련 핵심 판정

### 결론 (2026-09-25 사용자 실장비 확인 반영)
기존 `L1_DSD_runsheet.csv`의 5인자 중 N₂, pressure, target은 확보됐다. 그러나 substrate bias 인자는 실제 사용하지 않았고, 0.5–2 µm 증착은 과열 때문에 분할 증착이 필요하므로 기존 런시트는 그대로 실행하지 말고 데이터 취득 전에 Change Log와 런시트를 수정해야 한다.

| DOE 인자 | 기존 요구 범위 | 확인 결과 | 판정 |
|---|---:|---|---|
| RF power density | 2/4/6 W cm⁻² | ATS-Sputter RF 600 W, 3-inch target | 가능. 3-inch 면적 환산 약 91/182/274 W |
| N₂ fraction | 25/50/75% | N₂ MFC 최대 50 sccm | 가능성 높음. 정확한 fraction 설정에는 Ar MFC 최대유량 및 total-flow 운용값 필요 |
| pressure | 2/5/8 mTorr | 사용자 확인: 2–8 mTorr 가능 | 가능 |
| substrate T | 50/200/350°C | ZEUS: 최대 600°C | 가능 |
| RF substrate bias | 0/15/30 W | 사용자: bias power를 사용하지 않음 | DOE 인자에서 제거 권고. 장착 여부와 독립제어 가능 여부는 별도 확인 |
| deposition duty cycle | 기존에 없음 | 0.5–2 µm 연속 증착 시 과열, 중간 정지 필요 | 고정 SOP 또는 대체 DOE 인자로 사전등록 필요 |

Al 또는 AlN 3-inch target 보유는 사용자 확인 완료. 다만 Al metal reactive sputter인지 AlN ceramic target RF sputter인지에 따라 N₂ fraction의 물리적 의미가 달라지므로 사용 target 종류를 런시트에 명시해야 한다.

## 2. 증착·열처리·식각 장비

| 장비 / ZEUS | 제작사·모델 | ZEUS 핵심 사양 | AlN 연구 판정 |
|---|---|---|---|
| [DCRF 스퍼터링 시스템](https://www.zeus.go.kr/cloud/resvEq/read/Z-202207140944?cloudId=201903260802) | 아텍시스템 ATS-Sputter | max 4-inch, 3-inch target, substrate max 600°C, rotation 5–25 rpm, target distance 50–100 mm, DC 1 kW ×3, RF 600 W 13.56 MHz, 4 target, loadlock | L1의 유력 장비. N₂, pressure, substrate bias와 Al/AlN target 확인 필수 |
| [RF 스퍼터(2025)](https://www.zeus.go.kr/cloud/resvEq/read/Z-202504231009?cloudId=201903260802) | 더블루텍 Sputtering System | 4-inch, 3-inch target ×2, RF, ion-gun pretreatment, Ar/O₂, TMP | 기재 gas만 보면 AlN reactive sputter 불가. AlN ceramic target 탑재 여부 확인 |
| [(DC) 마그네트론 스퍼터](https://www.zeus.go.kr/cloud/resvEq/read/Z-202207140942?cloudId=201903260802) | Sntek MSS5000 | base <1×10⁻⁶ Torr, 5–100 mTorr, gun ×3, DC 1 kW | 금속 Al/전극용. RF 절연 AlN target 불가 |
| [DC 스퍼터-2](https://www.zeus.go.kr/cloud/resvEq/read/Z-202504231008?cloudId=201903260802) | 대기하이텍 Sputtering System | base <1×10⁻⁶ Torr, 5–100 mTorr, gun ×6, DC 1 kW | 금속·반응성 DC 후보. 기판크기, N₂, 온도 미확인 |
| [(DC) 스퍼터](https://www.zeus.go.kr/cloud/resvEq/read/Z-202207140945?cloudId=201903260802) | 대기하이텍 DKSPT-4-6 | base <1×10⁻⁶ Torr, 5–100 mTorr, gun ×6, DC 1 kW | 위와 동일 |
| [ALD](https://www.zeus.go.kr/cloud/resvEq/read/Z-202207140947?cloudId=201903260802) | 씨엔원 Atomic classic | piece–6-inch, thermal ALD, stage 400°C, source 4, Ar/N₂ carrier, H₂O, O₃ line | Al₂O₃ cap 가능. AlN PEALD 장비 아님 |
| [PECVD](https://www.zeus.go.kr/cloud/resvEq/read/Z-202401092123?cloudId=201903260802) | 엘에이티 PECVD System | piece–4-inch, heater 500°C, RF 300 W 13.56 MHz, N₂/O₂/SF₆/SiH₄/N₂O/NH₃ | PREREG Plan B의 SiO₂/SiN/SiON bonding cap 가능 |
| [LPCVD](https://www.zeus.go.kr/cloud/resvEq/read/Z-202207140940?cloudId=201903260802) | 대기하이텍 | 4-inch single wafer, heater 900°C, N₂-diluted SiH₄/O₂, 400°C SiO₂ | dense SiO₂ cap/control 가능. 열예산 주의 |
| [ICP etcher](https://www.zeus.go.kr/cloud/resvEq/read/Z-202207140948?cloudId=201903260802) | 엘에이티 | 4-inch, ICP 1 kW 13.56 MHz, chuck bias 600 W 12.56 MHz, −150–400°C, N₂/O₂/Ar/C₂F₆/SF₆/Cl₂, base ≤1×10⁻⁶ Torr | O₂/N₂/Ar 표면 활성화 가능. 최소 source/bias power와 damage 확인 필요 |
| [RTP](https://www.zeus.go.kr/cloud/resvEq/read/Z-202207140941?cloudId=201903260802) | Sntek RTP5000 | max 6-inch, 250–950°C, max 1000°C, 0–50°C/s, 최대 공정시간 10 min, N₂/O₂/Ar, 1×10⁻² Torr | 400°C 단시간 열이력 가능. PREREG의 2 h 어닐에는 부적합 |
| [Wet station](https://www.zeus.go.kr/cloud/resvEq/read/Z-202207140950?cloudId=201903260802) | 젠시스 IDW-001-1/2 | BOE, SC-1, DI bath/generator | 세정 가능. AlN hydrolysis 때문에 DI 노출시간 관리 필요 |
| [고진공 열증착기](https://www.zeus.go.kr/cloud/resvEq/read/Z-202207140946?cloudId=201903260802) | 대기하이텍 DKOLTH-8-2 | base/working <1×10⁻⁶ Torr, uniformity ±3% at Φ100 mm, 25 mm die ×9, metal source ×3 | 3ω heater/전극 증착 후보. 재료 및 최대 두께 확인 |

## 3. 계측·리소그래피 장비

| 장비 / ZEUS | 제작사·모델 | 사양 | 판정 |
|---|---|---|---|
| [AFM](https://www.zeus.go.kr/cloud/resvEq/read/Z-202303156182?cloudId=201903260802) | Park Systems Park NX10 | XY 50×50 µm closed-loop, Z 30 µm, SmartScan, AFM/EFM/KPFM/CFM/PFM | PREREG RMS 5×5 µm 측정 가능 |
| [Alpha-step](https://www.zeus.go.kr/cloud/resvEq/read/Z-202207140931?cloudId=201903260802) | KLA-Tencor AlphaStep D-500 | sample ≤140 mm, stage 80×20 mm, scan length max 30 mm, vertical resolution 0.38 Å | 두께·국부 profile 가능. **30 mm scan이라 4-inch 전체 wafer-curvature/Stoney stress 장비로 보기 어려움** |
| [Ellipsometer](https://www.zeus.go.kr/cloud/resvEq/read/Z-202209232161?cloudId=201903260802) | Nano-view SE MG-1000 | variable angle 5° step, 350–840 nm, 2048 CCD, 6 s/site | 두께·n/k. 곡률/응력 기능 없음 |
| [4-point probe](https://www.zeus.go.kr/cloud/resvEq/read/Z-202207140936?cloudId=201903260802) | AIT CMT-SR1000N | 1 mΩ/sq–2 MΩ/sq, center 1-point, 10 nA–100 mA | heater/전극 면저항 측정 가능. 균일도 mapping 불가 |
| [Mask aligner](https://www.zeus.go.kr/cloud/resvEq/read/Z-202207140943?cloudId=201903260802) | SUSS MicroTec MA6 NFH | piece–4-inch chuck, mask ≤5×5 inch, 350 W Hg 350–450 nm, contact/proximity modes | 3ω 패턴 가능. ZEUS에는 해상도·backside alignment가 명시되지 않음 |
| [Spin coater](https://www.zeus.go.kr/cloud/resvEq/read/Z-202404044205?cloudId=201903260802) | MIDAS SPIN-3000D | 100–8000 rpm, 50 step/20 recipe, piece–6-inch | PR/sol-gel 공정 가능 |
| [Optical microscope](https://www.zeus.go.kr/cloud/resvEq/read/Z-202207140935?cloudId=201903260802) | Olympus BX51 | objective ×5/10/50/100, CCD | crack/delamination screening |

## 4. 본딩·패키징 장비

| 장비 / ZEUS | 제작사·모델 | ZEUS 사양 | 판정 |
|---|---|---|---|
| [정밀 플립칩 본더](https://www.zeus.go.kr/cloud/resvEq/read/Z-202404044206?cloudId=201903260802) | Finetech FINEPLACER lambda2 | die 30×30 µm–20×20 mm, ±0.5 µm alignment, programmable force/temperature profile, adhesive/AuSn/Sn eutectic | D2W 위치맞춤 및 가압·가열 가능. ZEUS는 dielectric fusion/direct bonding, 진공/N₂ 분위기, force/temperature 범위를 보증하지 않음 |
| [패키징 다이본더](https://www.zeus.go.kr/cloud/resvEq/read/Z-202207140933?cloudId=201903260802) | Neotech NT-MPP1000 | XY ±35 µm, θ ±2°, 2–4-inch wafer/piece ≤20 mm, load 0.8–1.5 N, epoxy dispenser | epoxy die attach용. 직접 AlN–AlN 본딩에는 부적합 |

ZEUS에서 별도 **wafer bonder, die-shear/bond tester, C-SAM/IR void 검사, thermal-cycle/uHAST** 장비는 확인하지 못함.

## 5. 표준분석연구원 장비

- XRD: PANalytical Pro MRD ZEUS 등록 확인. omega rocking curve와 sin²ψ 가능 여부는 ZEUS 사양에 없음.
- 고온 XRD: 센터 공식 안내로 존재 확인, ZEUS 상세 미확인.
- TEM/STEM: 80–200 kV, TEM point resolution 0.244 nm, STEM resolution 1 nm, EDS 확인. EELS는 공식 사양에서 미확인.
- XPS: monochromated Al Kα, spot 10–400 µm, depth profile/ARXPS 확인. AlN O at% 측정은 원리상 가능하지만 검출한계·정량 프로토콜은 담당자 확인 필요.

## 6. PREREG 영향

1. **L1 증착 DOE**: N₂ 50 sccm, pressure 2–8 mTorr, 3-inch target 보유가 확인됐다. Bias를 실제 사용하지 않으므로 5인자 DSD를 4인자로 바꾸거나, 과열과 막질에 직접 영향을 주는 분할증착 duty cycle을 대체 인자로 넣는 Change Log가 필요.
2. **L1 stress gate**: 현재 장비로 wafer curvature가 확인되지 않음. AlphaStep 30 mm scan은 전체 4-inch bow 측정 대체로 불충분. 외부 curvature tool 또는 검증된 부분곡률 프로토콜 필요.
3. **L1 thermal history**: RTP는 10 min 제한. PREREG가 2 h를 요구하는 것은 L2 anneal이며, 해당 처리는 furnace/LPCVD tube 또는 별도 장비가 필요.
4. **L2 direct bonding**: ICP activation + lambda2 접촉은 물리적으로 시도 가능하지만, 본더가 plasma-activated dielectric direct bonding을 공식 지원한다는 근거는 없음. Atmosphere/force/temperature/chuck flatness를 확인해야 함.
5. **L2 Plan B**: PECVD SiO₂/SiN/SiON 또는 ALD Al₂O₃ cap은 인하대 장비로 실행 가능.
6. **검증 병목**: die shear, void inspection, wafer curvature, TDTR/3ω, STEM-EELS 및 uHAST는 여전히 별도 확보가 필요.

## 7. 담당자에게 물어볼 최소 질문

### ATS-Sputter (남은 확인사항)
1. Ar MFC 최대유량과 통상 total flow는? (N₂ fraction 계산에 필요)
2. 실제 사용할 target은 Al metal인가, AlN ceramic인가?
3. substrate bias supply가 물리적으로 없는가, 아니면 있으나 기존 공정에서 사용하지 않았는가?
4. RF power별 최대 연속 증착시간, 의무 냉각시간과 냉각 중 진공/가스 유지 방법은?
5. 냉각 후 재점화 시 target pre-sputter를 매번 수행하는가? wafer를 shutter로 보호할 수 있는가?
6. 0.5 µm와 2 µm에서 총 증착시간, run당 증착두께 및 온도 drift 기록이 가능한가?

### FINEPLACER lambda2
1. 실제 장착 module의 force 범위와 최대 chuck/tool 온도는?
2. 진공 또는 N₂ 분위기 모듈이 있는가?
3. adhesive/eutectic 외에 oxide/dielectric direct bonding 운용 사례가 있는가?
4. 10–20 mm die의 coplanarity·parallelism 사양은?

### 분석 장비
1. Pro MRD에서 AlN(0002) omega rocking curve가 가능한가?
2. wafer curvature 또는 film-stress 측정 장비가 교내 다른 센터에 있는가?
3. TEM에 EELS detector가 장착되어 있는가?
4. 별도 bond tester/die shear tester와 C-SAM이 있는가?
