# Al–Al / Mo–Mo Bonding Literature & Process-Condition Database v0.2

**Scope:** Al–Al 및 Mo–Mo 동종 접합을 중심으로, bonding 전처리 조건과 실제 bonding 조건을 분리해 정리한 문헌 기반 데이터베이스이다. 순수/박막 Al–Al 및 Mo–Mo를 핵심(`D0`)으로 두고, 동일 Al 합금의 homo-bonding은 보조 학습 데이터(`D0-AUX`), Pd/Ti/Cu 등의 계면층이 존재하는 경우는 `D1`, 표면처리만 검증된 자료는 `S`로 분리한다.

**현재 본체 bonding-condition records: 107개.** Supporting pretreatment-only records: 12개.

## 1. 데이터 무결성 규칙


1. 논문에서 실제로 수행된 것으로 확인되는 sample/condition만 개별 record로 기록한다.
2. 논문이 `200–300 °C`, `20–60 kN`처럼 범위만 제시한 경우 임의의 full-factorial 조합을 생성하지 않는다.
3. 동일 bonding recipe라도 frame width/corner geometry처럼 실제 독립 실험변수가 달라지면 별도 sample-condition으로 기록한다.
4. 값이 공개 초록/검색 가능한 원문에서 확인되지 않으면 `N/R` 또는 `Partial`로 남긴다.
5. 상충하는 캡션/표는 임의로 하나를 선택하지 않고 `Conflict-check`로 표시한다.
6. Wet-clean surface chemistry만 있고 실제 Al–Al/Mo–Mo 접합이 없는 경우 bonding record 수에 포함하지 않는다.
7. 압력은 가능하면 MPa로 기록하되, 원문이 총 force만 제시하면 force와 명목압력을 함께 보존한다.
8. 결과값의 시험방식(인장/전단/peel/IAE)이 다르므로 서로 직접 동일 척도로 비교하지 않는다.

## 2. Evidence / Problem code


### Evidence class

| Code | 의미 |
|---|---|
| `D0` | 동일금속 직접계면: Al/Al 또는 Mo/Mo |
| `D0-AUX` | 동일 Al계 합금 homo-bonding. 박막 Al 모델에는 보조 데이터로만 사용 |
| `D1` | 동일 기판이지만 Pd, Ti, Cu 등 passivation/interlayer 존재 |
| `S` | surface cleaning/oxide removal 등 supporting evidence; 실제 동종 bonding 미검증 |

### Problem code

| Code | 문제 |
|---|---|
| `OX` | native oxide / reoxidation |
| `RG` | roughness / pitting / swelling |
| `RES` | polymer, halogen, organic residue |
| `VD` | void / particle / incomplete contact |
| `HT` | high thermal budget |
| `HP` | high pressure / excessive deformation |
| `RC` | recrystallization / grain growth / embrittlement |
| `IL` | interlayer/passivation remains at interface |
| `TOP` | topography / wafer bow / nonuniform local pressure |
| `CR` | corrosion / over-etch |
| `DATA` | key quantitative value not reported or not yet extracted |

## 3. Record count summary

| 구분 | Records |
|---|---:|
| 1 Al–Al Dry/Mechanical | 82 |
| 2 Al–Al Wet/Mixed | 6 |
| 3 Mo–Mo Dry/Diffusion | 19 |
| **Bonding-condition total** | **107** |
| Supporting pretreatment-only | 12 |

## 4. 4개 카테고리별 문헌 목록

### 1. Al–Al Dry / Plasma / Vacuum / Mechanical

| First author/source | Year | Title / relevance | DOI / identifier |
|---|---:|---|---|
| Akatsu et al. | 1999 | Atomic structure of Al/Al interface formed by surface activated bonding | 10.1023/A:1004661610307 |
| Yun et al. | 2008 | Al to Al wafer bonding for MEMS encapsulation and 3-D interconnect | 10.1109/MEMSYS.2008.4443780 |
| Çakmak et al. | 2009 | Aluminum Thermo Compression Bonding Characterization | 10.1557/PROC-1222-DD04-02 |
| Frömel et al. | 2011 | Investigations of thermocompression bonding with thin metal layers | 10.1109/TRANSDUCERS.2011.5969495 |
| Malik et al. | 2014 | AlAl thermocompression bonding for wafer-level MEMS sealing | 10.1016/j.sna.2014.02.030 |
| Malik et al. | 2015 | Impact of SiO2 on Al–Al thermocompression wafer bonding | 10.1088/0960-1317/25/3/035025 |
| Malik et al. | 2016 | Interfacial characterization of Al-Al thermocompression bonds | 10.1063/1.4952709 |
| Rebhan et al. | 2016 | Low-Temperature Aluminum-Aluminum Wafer Bonding | 10.1149/07509.0015ECST |
| Hinterreiter et al. | 2018 | Surface pretreated low-temperature aluminum–aluminum wafer bonding | 10.1007/s00542-017-3520-8 |
| Schulze et al. | 2019 | Optimization of a BEOL Aluminum Deposition Process Enabling Wafer Level Al-Al TCB | 10.1109/ECTC.2019.00040 |
| Cheemalamarri et al. | 2020 | Effect of ultrathin palladium layer in low-T/P Al–Al bonding | 10.1088/2051-672X/abbb81 |
| Al Farisi et al. | 2022 | Electroplated Al press-marking approach for Al-Al bonding | 10.3390/mi13081221 |
| Hu et al. | 2022 | Two-Step Ar/N2 Plasma-Activated Al Surface for Al-Al Direct Bonding | 10.1109/ECTC51906.2022.00060 |
| Schulze et al. | 2022 | Influence of Process Parameters on Surface Activated Aluminum-to-Aluminum Wafer Bonding | 10.1109/TCPMT.2022.3152348 |
| Schulze et al. | 2023 | Al-Al Waferbonding Process Development for Heterogeneous Integration | 10.1149/11201.0025ECST |
| Schulze et al. | 2024 | Collective die-to-wafer bonding based on surface-activated Al-Al TCB | 10.1109/TCPMT.2024.3363236 |
| Wu et al. | 2025 | Low-temperature Al–Al bonding with Ti/Au passivation | 10.1109/LED.2025.3601663 |
| Song et al. | 2023 | Direct diffusion bonding of 1060Al with various Ar ion doses | 10.1016/j.surfin.2023.103285 |
| Venugopal et al. | 2018 | AA5083 homo diffusion bonding design-matrix study | 10.22214/ijraset.2018.2099 |
| AA6061 HIP study | 2022 | HIP bonding of AA6061/AA6061 plate interfaces | OSTI purl 1870635 |

### 2. Al–Al Wet / Wet-assisted / Mixed

| First author/source | Year | Title / relevance | DOI / identifier |
|---|---:|---|---|
| Chen et al. | 2013 | Low-temperature diffusion bonding of pure aluminum | 10.1007/s00339-013-7860-7 |
| Cheemalamarri et al. | 2023 | CMOS-compatible fine-pitch Al-Al bonding with wet residue clean + Ar activation | 10.1109/ECTC51909.2023.00294 |
| Al metallization surface-treatment patent | N/A | Hybrid wafer-to-wafer bonding and surface preparation for Al metallization | Patent; fluoride + low-water solvent chemistry |
| Samsung-related cleaning patent | 2016 | Cleaning solution using IPA/HF/NH4F/low water | US 9394509 |
| Ammonium bifluoride dicing-clean study | 2023 | A Study of Ammonium Bifluoride as an Agent for Cleaning Silicon Contamination | 10.3390/app13095294 |

### 3. Mo–Mo Dry / Vacuum / Diffusion / Interlayer

| First author/source | Year | Title / relevance | DOI / identifier |
|---|---:|---|---|
| Hashimoto & Tanuma | 1968 | Diffusion Bonding of Molybdenum | 10.2207/qjjws1943.37.1345 |
| Ohashi & Suga | 1992 | Mo single-crystal diffusion welding / orientation effects | 10.2207/qjjws.10.53 |
| Gnyusov et al. | 2004 | Low-temperature bonding of plastically deformed Mo | 10.1533/WINT.2004.3327 |
| Shimatsu & Uomoto | 2010 | Atomic diffusion bonding of wafers with nanocrystalline metal films | 10.1116/1.3437515 |
| Denisov et al. | 2017 | Mo/Ti/Mo diffusion welding under HIP | 10.1080/09507116.2017.1295562 |
| Al-Mashhadani | 2019 | Refractory metals low temperature diffusion bonding | TU Chemnitz dissertation, ISBN 978-3-96100-090-6 |
| Archival gas-pressure bonding study | N/A | The Bonding of Molybdenum-and Niobium-Clad Fuel Elements | UNT/DOE archival |
| Tarr | N/A | Solid State Diffusion Bonding of Refractory Metals and Alloys | 10.2172/4634983 |

### 4. Mo Wet / Wet-assisted surface preparation (supporting; direct Mo–Mo gap)

| First author/source | Year | Title / relevance | DOI / identifier |
|---|---:|---|---|
| Le et al. | 2022 | Wet Cleaning of Molybdenum for Nano Interconnects | ECS Meeting Abstract |
| Pacco/Nakano et al. | 2022 | Ozone-gas-bake + wet selective Mo oxide removal | ECS Meeting Abstract 10.1149/MA2022-01281261mtgabs |
| ASTM | 2003 | ASTM B629 preparation of molybdenum and alloys for electroplating | ASTM B629 |
| US Patent | 1979 | Electrochemical processing of molybdenum surface | US 4169027 |
| Hashimoto & Tanuma | 1968 | Electropolishing variants before Mo diffusion bonding | 10.2207/qjjws1943.37.1345 |

## 5. Master bonding-condition database — 107 records

| Record_ID | Source | Category | Material | Subtype | Pretreatment | Bond_T_C | Pressure_or_Force | Bond_Time | Ambient | Result | Problem_Code | Evidence | Verification | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| AL-D-001 | AL01 Malik et al. 2014, Sensors and Actuators A, DOI 10.1016/j.sna.2014.02.030 | 1 Al–Al Dry/Mechanical | Al–Al | Pure Al film / patterned MEMS frame | No bond-surface oxide strip; 1 µm sputtered Al; pre-deposition RCA/HF + back-sputter | 400 | 18 kN (~34.28 MPa nominal) | 60 min | <1×10^-3 mbar vacuum | Poor/incomplete; overall dicing yield <47% for low/medium-force 400°C cases | OX-3;VD-2;HT-2 | D0 | Verified | Geometry=F100: 100 µm square-corner frame; geometry changes local pressure. Exact geometry-specific yield not separately digitized. |
| AL-D-002 | AL01 Malik et al. 2014, Sensors and Actuators A, DOI 10.1016/j.sna.2014.02.030 | 1 Al–Al Dry/Mechanical | Al–Al | Pure Al film / patterned MEMS frame | No bond-surface oxide strip; 1 µm sputtered Al; pre-deposition RCA/HF + back-sputter | 400 | 18 kN (~34.28 MPa nominal) | 60 min | <1×10^-3 mbar vacuum | Poor/incomplete; overall dicing yield <47% for low/medium-force 400°C cases | OX-3;VD-2;HT-2 | D0 | Verified | Geometry=F200: 200 µm square-corner frame; geometry changes local pressure. Exact geometry-specific yield not separately digitized. |
| AL-D-003 | AL01 Malik et al. 2014, Sensors and Actuators A, DOI 10.1016/j.sna.2014.02.030 | 1 Al–Al Dry/Mechanical | Al–Al | Pure Al film / patterned MEMS frame | No bond-surface oxide strip; 1 µm sputtered Al; pre-deposition RCA/HF + back-sputter | 400 | 18 kN (~34.28 MPa nominal) | 60 min | <1×10^-3 mbar vacuum | Poor/incomplete; overall dicing yield <47% for low/medium-force 400°C cases | OX-3;VD-2;HT-2 | D0 | Verified | Geometry=F200R: 200 µm rounded-corner frame; geometry changes local pressure. Exact geometry-specific yield not separately digitized. |
| AL-D-004 | AL01 Malik et al. 2014, Sensors and Actuators A, DOI 10.1016/j.sna.2014.02.030 | 1 Al–Al Dry/Mechanical | Al–Al | Pure Al film / patterned MEMS frame | No bond-surface oxide strip; 1 µm sputtered Al; pre-deposition RCA/HF + back-sputter | 450 | 18 kN (~34.28 MPa nominal) | 60 min | <1×10^-3 mbar vacuum | Successful/strong; low-force dicing yield reported ~80–91% range across designs | HT-3;OX-1 | D0 | Verified | Geometry=F100: 100 µm square-corner frame; geometry changes local pressure. Exact geometry-specific yield not separately digitized. |
| AL-D-005 | AL01 Malik et al. 2014, Sensors and Actuators A, DOI 10.1016/j.sna.2014.02.030 | 1 Al–Al Dry/Mechanical | Al–Al | Pure Al film / patterned MEMS frame | No bond-surface oxide strip; 1 µm sputtered Al; pre-deposition RCA/HF + back-sputter | 450 | 18 kN (~34.28 MPa nominal) | 60 min | <1×10^-3 mbar vacuum | Successful/strong; low-force dicing yield reported ~80–91% range across designs | HT-3;OX-1 | D0 | Verified | Geometry=F200: 200 µm square-corner frame; geometry changes local pressure. Exact geometry-specific yield not separately digitized. |
| AL-D-006 | AL01 Malik et al. 2014, Sensors and Actuators A, DOI 10.1016/j.sna.2014.02.030 | 1 Al–Al Dry/Mechanical | Al–Al | Pure Al film / patterned MEMS frame | No bond-surface oxide strip; 1 µm sputtered Al; pre-deposition RCA/HF + back-sputter | 450 | 18 kN (~34.28 MPa nominal) | 60 min | <1×10^-3 mbar vacuum | Successful/strong; low-force dicing yield reported ~80–91% range across designs | HT-3;OX-1 | D0 | Verified | Geometry=F200R: 200 µm rounded-corner frame; geometry changes local pressure. Exact geometry-specific yield not separately digitized. |
| AL-D-007 | AL01 Malik et al. 2014, Sensors and Actuators A, DOI 10.1016/j.sna.2014.02.030 | 1 Al–Al Dry/Mechanical | Al–Al | Pure Al film / patterned MEMS frame | No bond-surface oxide strip; 1 µm sputtered Al; pre-deposition RCA/HF + back-sputter | 550 | 18 kN (~34.28 MPa nominal) | 60 min | <1×10^-3 mbar vacuum | Strong; near-100% dicing yield, CFN high | HT-3;RC-1 | D0 | Verified | Geometry=F100: 100 µm square-corner frame; geometry changes local pressure. Exact geometry-specific yield not separately digitized. |
| AL-D-008 | AL01 Malik et al. 2014, Sensors and Actuators A, DOI 10.1016/j.sna.2014.02.030 | 1 Al–Al Dry/Mechanical | Al–Al | Pure Al film / patterned MEMS frame | No bond-surface oxide strip; 1 µm sputtered Al; pre-deposition RCA/HF + back-sputter | 550 | 18 kN (~34.28 MPa nominal) | 60 min | <1×10^-3 mbar vacuum | Strong; near-100% dicing yield, CFN high | HT-3;RC-1 | D0 | Verified | Geometry=F200: 200 µm square-corner frame; geometry changes local pressure. Exact geometry-specific yield not separately digitized. |
| AL-D-009 | AL01 Malik et al. 2014, Sensors and Actuators A, DOI 10.1016/j.sna.2014.02.030 | 1 Al–Al Dry/Mechanical | Al–Al | Pure Al film / patterned MEMS frame | No bond-surface oxide strip; 1 µm sputtered Al; pre-deposition RCA/HF + back-sputter | 550 | 18 kN (~34.28 MPa nominal) | 60 min | <1×10^-3 mbar vacuum | Strong; near-100% dicing yield, CFN high | HT-3;RC-1 | D0 | Verified | Geometry=F200R: 200 µm rounded-corner frame; geometry changes local pressure. Exact geometry-specific yield not separately digitized. |
| AL-D-010 | AL01 Malik et al. 2014, Sensors and Actuators A, DOI 10.1016/j.sna.2014.02.030 | 1 Al–Al Dry/Mechanical | Al–Al | Pure Al film / patterned MEMS frame | No bond-surface oxide strip; 1 µm sputtered Al; pre-deposition RCA/HF + back-sputter | 400 | 36 kN (~68.57 MPa nominal) | 60 min | <1×10^-3 mbar vacuum | Poor/incomplete; all-frame dicing yield <40% | OX-3;VD-2;HP-2 | D0 | Verified | Geometry=F100: 100 µm square-corner frame; geometry changes local pressure. Exact geometry-specific yield not separately digitized. |
| AL-D-011 | AL01 Malik et al. 2014, Sensors and Actuators A, DOI 10.1016/j.sna.2014.02.030 | 1 Al–Al Dry/Mechanical | Al–Al | Pure Al film / patterned MEMS frame | No bond-surface oxide strip; 1 µm sputtered Al; pre-deposition RCA/HF + back-sputter | 400 | 36 kN (~68.57 MPa nominal) | 60 min | <1×10^-3 mbar vacuum | Poor/incomplete; all-frame dicing yield <40% | OX-3;VD-2;HP-2 | D0 | Verified | Geometry=F200: 200 µm square-corner frame; geometry changes local pressure. Exact geometry-specific yield not separately digitized. |
| AL-D-012 | AL01 Malik et al. 2014, Sensors and Actuators A, DOI 10.1016/j.sna.2014.02.030 | 1 Al–Al Dry/Mechanical | Al–Al | Pure Al film / patterned MEMS frame | No bond-surface oxide strip; 1 µm sputtered Al; pre-deposition RCA/HF + back-sputter | 400 | 36 kN (~68.57 MPa nominal) | 60 min | <1×10^-3 mbar vacuum | Poor/incomplete; all-frame dicing yield <40% | OX-3;VD-2;HP-2 | D0 | Verified | Geometry=F200R: 200 µm rounded-corner frame; geometry changes local pressure. Exact geometry-specific yield not separately digitized. |
| AL-D-013 | AL01 Malik et al. 2014, Sensors and Actuators A, DOI 10.1016/j.sna.2014.02.030 | 1 Al–Al Dry/Mechanical | Al–Al | Pure Al film / patterned MEMS frame | No bond-surface oxide strip; 1 µm sputtered Al; pre-deposition RCA/HF + back-sputter | 450 | 36 kN (~68.57 MPa nominal) | 60 min | <1×10^-3 mbar vacuum | Strong; almost 100% dicing yield | HT-3;HP-2 | D0 | Verified | Geometry=F100: 100 µm square-corner frame; geometry changes local pressure. Exact geometry-specific yield not separately digitized. |
| AL-D-014 | AL01 Malik et al. 2014, Sensors and Actuators A, DOI 10.1016/j.sna.2014.02.030 | 1 Al–Al Dry/Mechanical | Al–Al | Pure Al film / patterned MEMS frame | No bond-surface oxide strip; 1 µm sputtered Al; pre-deposition RCA/HF + back-sputter | 450 | 36 kN (~68.57 MPa nominal) | 60 min | <1×10^-3 mbar vacuum | Strong; almost 100% dicing yield | HT-3;HP-2 | D0 | Verified | Geometry=F200: 200 µm square-corner frame; geometry changes local pressure. Exact geometry-specific yield not separately digitized. |
| AL-D-015 | AL01 Malik et al. 2014, Sensors and Actuators A, DOI 10.1016/j.sna.2014.02.030 | 1 Al–Al Dry/Mechanical | Al–Al | Pure Al film / patterned MEMS frame | No bond-surface oxide strip; 1 µm sputtered Al; pre-deposition RCA/HF + back-sputter | 450 | 36 kN (~68.57 MPa nominal) | 60 min | <1×10^-3 mbar vacuum | Strong; almost 100% dicing yield | HT-3;HP-2 | D0 | Verified | Geometry=F200R: 200 µm rounded-corner frame; geometry changes local pressure. Exact geometry-specific yield not separately digitized. |
| AL-D-016 | AL01 Malik et al. 2014, Sensors and Actuators A, DOI 10.1016/j.sna.2014.02.030 | 1 Al–Al Dry/Mechanical | Al–Al | Pure Al film / patterned MEMS frame | No bond-surface oxide strip; 1 µm sputtered Al; pre-deposition RCA/HF + back-sputter | 550 | 36 kN (~68.57 MPa nominal) | 60 min | <1×10^-3 mbar vacuum | Strong; almost 100% dicing yield | HT-3;HP-2;RC-1 | D0 | Verified | Geometry=F100: 100 µm square-corner frame; geometry changes local pressure. Exact geometry-specific yield not separately digitized. |
| AL-D-017 | AL01 Malik et al. 2014, Sensors and Actuators A, DOI 10.1016/j.sna.2014.02.030 | 1 Al–Al Dry/Mechanical | Al–Al | Pure Al film / patterned MEMS frame | No bond-surface oxide strip; 1 µm sputtered Al; pre-deposition RCA/HF + back-sputter | 550 | 36 kN (~68.57 MPa nominal) | 60 min | <1×10^-3 mbar vacuum | Strong; almost 100% dicing yield | HT-3;HP-2;RC-1 | D0 | Verified | Geometry=F200: 200 µm square-corner frame; geometry changes local pressure. Exact geometry-specific yield not separately digitized. |
| AL-D-018 | AL01 Malik et al. 2014, Sensors and Actuators A, DOI 10.1016/j.sna.2014.02.030 | 1 Al–Al Dry/Mechanical | Al–Al | Pure Al film / patterned MEMS frame | No bond-surface oxide strip; 1 µm sputtered Al; pre-deposition RCA/HF + back-sputter | 550 | 36 kN (~68.57 MPa nominal) | 60 min | <1×10^-3 mbar vacuum | Strong; almost 100% dicing yield | HT-3;HP-2;RC-1 | D0 | Verified | Geometry=F200R: 200 µm rounded-corner frame; geometry changes local pressure. Exact geometry-specific yield not separately digitized. |
| AL-D-019 | AL01 Malik et al. 2014, Sensors and Actuators A, DOI 10.1016/j.sna.2014.02.030 | 1 Al–Al Dry/Mechanical | Al–Al | Pure Al film / patterned MEMS frame | No bond-surface oxide strip; 1 µm sputtered Al; pre-deposition RCA/HF + back-sputter | 400 | 60 kN (~114.3 MPa nominal) | 60 min | <1×10^-3 mbar vacuum | Bond improved; all-frame dicing yield >77%; strength >20 MPa reported for high-force condition | HP-3;OX-2 | D0 | Verified | Geometry=F100: 100 µm square-corner frame; geometry changes local pressure. Exact geometry-specific yield not separately digitized. |
| AL-D-020 | AL01 Malik et al. 2014, Sensors and Actuators A, DOI 10.1016/j.sna.2014.02.030 | 1 Al–Al Dry/Mechanical | Al–Al | Pure Al film / patterned MEMS frame | No bond-surface oxide strip; 1 µm sputtered Al; pre-deposition RCA/HF + back-sputter | 400 | 60 kN (~114.3 MPa nominal) | 60 min | <1×10^-3 mbar vacuum | Bond improved; all-frame dicing yield >77%; strength >20 MPa reported for high-force condition | HP-3;OX-2 | D0 | Verified | Geometry=F200: 200 µm square-corner frame; geometry changes local pressure. Exact geometry-specific yield not separately digitized. |
| AL-D-021 | AL01 Malik et al. 2014, Sensors and Actuators A, DOI 10.1016/j.sna.2014.02.030 | 1 Al–Al Dry/Mechanical | Al–Al | Pure Al film / patterned MEMS frame | No bond-surface oxide strip; 1 µm sputtered Al; pre-deposition RCA/HF + back-sputter | 400 | 60 kN (~114.3 MPa nominal) | 60 min | <1×10^-3 mbar vacuum | Bond improved; all-frame dicing yield >77%; strength >20 MPa reported for high-force condition | HP-3;OX-2 | D0 | Verified | Geometry=F200R: 200 µm rounded-corner frame; geometry changes local pressure. Exact geometry-specific yield not separately digitized. |
| AL-D-022 | AL02 Malik et al. 2015, J. Micromech. Microeng., DOI 10.1088/0960-1317/25/3/035025 | 1 Al–Al Dry/Mechanical | Al–Al | 1 µm Al, laminate Ox300; SiO2 below Al: 7500 Å patterned /1500 Å flat | Conventional Al TCB; no final oxide-removal activation | 300 | 36 kN (68.6 MPa nominal) | 60 min | <1×10^-3 mbar vacuum | Lower-quality than higher-T Ox cases; quantitative strength in paper | HT-2;OX-2 | D0 | Verified |  |
| AL-D-023 | AL02 Malik et al. 2015, J. Micromech. Microeng., DOI 10.1088/0960-1317/25/3/035025 | 1 Al–Al Dry/Mechanical | Al–Al | 1 µm Al, laminate Ox350; SiO2 below Al: 7500/1500 Å | Conventional Al TCB; no final oxide-removal activation | 350 | 36 kN (68.6 MPa nominal) | 60 min | <1×10^-3 mbar vacuum | Improved relative to 300°C | HT-2;OX-2 | D0 | Verified |  |
| AL-D-024 | AL02 Malik et al. 2015, J. Micromech. Microeng., DOI 10.1088/0960-1317/25/3/035025 | 1 Al–Al Dry/Mechanical | Al–Al | 1 µm Al, laminate Ox400; SiO2 below Al: 7500/1500 Å | Conventional Al TCB; no final oxide-removal activation | 400 | 36 kN (68.6 MPa nominal) | 60 min | <1×10^-3 mbar vacuum | Dicing yield 98%; inspected cross-sections: ~70% frames had local voids, avg void length 0.76 µm, height 0.024 µm | VD-2;HT-3 | D0 | Verified |  |
| AL-D-025 | AL02 Malik et al. 2015, J. Micromech. Microeng., DOI 10.1088/0960-1317/25/3/035025 | 1 Al–Al Dry/Mechanical | Al–Al | 1 µm Al, laminate Ox450; SiO2 below Al: 7500/1500 Å | Conventional Al TCB; no final oxide-removal activation | 450 | 36 kN (68.6 MPa nominal) | 60 min | <1×10^-3 mbar vacuum | High-quality; local void incidence lower (~40% inspected frames), avg 0.60 µm ×0.017 µm | VD-1;HT-3 | D0 | Verified |  |
| AL-D-026 | AL02 Malik et al. 2015, J. Micromech. Microeng., DOI 10.1088/0960-1317/25/3/035025 | 1 Al–Al Dry/Mechanical | Al–Al | 1 µm Al, laminate Ox400-15; SiO2 below Al: 2000/800 Å | Conventional Al TCB; no final oxide-removal activation | 400 | 60 kN (114.3 MPa nominal) | 15 min | <1×10^-3 mbar vacuum | Significantly weaker than 30/60 min; lower cohesive Si fracture | VD-2;HP-3 | D0 | Verified |  |
| AL-D-027 | AL02 Malik et al. 2015, J. Micromech. Microeng., DOI 10.1088/0960-1317/25/3/035025 | 1 Al–Al Dry/Mechanical | Al–Al | 1 µm Al, laminate Ox400-30; SiO2 below Al: 2000/800 Å | Conventional Al TCB; no final oxide-removal activation | 400 | 60 kN (114.3 MPa nominal) | 30 min | <1×10^-3 mbar vacuum | Strong; mean strength ~55 MPa reported, dicing ~98%; similar to 60 min | HP-3;HT-3 | D0 | Verified |  |
| AL-D-028 | AL02 Malik et al. 2015, J. Micromech. Microeng., DOI 10.1088/0960-1317/25/3/035025 | 1 Al–Al Dry/Mechanical | Al–Al | 1 µm Al, laminate Ox400-60; SiO2 below Al: 2000/800 Å | Conventional Al TCB; no final oxide-removal activation | 400 | 60 kN (114.3 MPa nominal) | 60 min | <1×10^-3 mbar vacuum | Strong; dicing near 100%; only ~10% inspected frames with voids | HP-3;HT-3 | D0 | Verified |  |
| AL-D-029 | AL02 Malik et al. 2015, J. Micromech. Microeng., DOI 10.1088/0960-1317/25/3/035025 | 1 Al–Al Dry/Mechanical | Al–Al | 1 µm Al, laminate Si400; Al directly on Si | Conventional Al TCB; no final oxide-removal activation | 400 | 36 kN (68.6 MPa nominal) | 60 min | <1×10^-3 mbar vacuum | Dicing yield ~33%; voids/pits prominent | VD-3;OX-3;HT-3 | D0 | Verified |  |
| AL-D-030 | AL02 Malik et al. 2015, J. Micromech. Microeng., DOI 10.1088/0960-1317/25/3/035025 | 1 Al–Al Dry/Mechanical | Al–Al | 1 µm Al, laminate Si450; Al directly on Si | Conventional Al TCB; no final oxide-removal activation | 450 | 36 kN (68.6 MPa nominal) | 60 min | <1×10^-3 mbar vacuum | Improved; inspected frames ~60% had local voids, avg 0.62 µm ×0.026 µm | VD-2;HT-3 | D0 | Verified |  |
| AL-D-031 | AL02 Malik et al. 2015, J. Micromech. Microeng., DOI 10.1088/0960-1317/25/3/035025 | 1 Al–Al Dry/Mechanical | Al–Al | 1 µm Al, laminate Si550; Al directly on Si | Conventional Al TCB; no final oxide-removal activation | 550 | 36 kN (68.6 MPa nominal) | 60 min | <1×10^-3 mbar vacuum | High-temperature strong-bond regime | HT-3;RC-1 | D0 | Verified |  |
| AL-D-032 | AL03 Al Farisi et al. 2022, Micromachines 13, 1221, DOI 10.3390/mi13081221 | 1 Al–Al Dry/Mechanical | Al–Al | ~8 µm electroplated Al; press-mark groove 3 µm | Mechanical press-marking/groove used to rupture native oxide | 150 | Local ~250 MPa | 40 min | Vacuum | No effective bond | HT-1;HP-3;OX-3 | D0 | Verified | Extreme local pressure improves oxide rupture but is device-stress-limited. |
| AL-D-033 | AL03 Al Farisi et al. 2022, Micromachines 13, 1221, DOI 10.3390/mi13081221 | 1 Al–Al Dry/Mechanical | Al–Al | ~8 µm electroplated Al; press-mark groove 4 µm | Mechanical press-marking/groove used to rupture native oxide | 150 | Local ~250 MPa | 40 min | Vacuum | No effective bond | HT-1;HP-3;OX-3 | D0 | Verified | Extreme local pressure improves oxide rupture but is device-stress-limited. |
| AL-D-034 | AL03 Al Farisi et al. 2022, Micromachines 13, 1221, DOI 10.3390/mi13081221 | 1 Al–Al Dry/Mechanical | Al–Al | ~8 µm electroplated Al; press-mark groove 3 µm | Mechanical press-marking/groove used to rupture native oxide | 250 | Local ~250 MPa | 40 min | Vacuum | Mean shear ~16 MPa | HP-3;HT-2 | D0 | Verified | Extreme local pressure improves oxide rupture but is device-stress-limited. |
| AL-D-035 | AL03 Al Farisi et al. 2022, Micromachines 13, 1221, DOI 10.3390/mi13081221 | 1 Al–Al Dry/Mechanical | Al–Al | ~8 µm electroplated Al; press-mark groove 4 µm | Mechanical press-marking/groove used to rupture native oxide | 250 | Local ~250 MPa | 40 min | Vacuum | Mean shear ~11 MPa | HP-3;HT-2 | D0 | Verified | Extreme local pressure improves oxide rupture but is device-stress-limited. |
| AL-D-036 | AL03 Al Farisi et al. 2022, Micromachines 13, 1221, DOI 10.3390/mi13081221 | 1 Al–Al Dry/Mechanical | Al–Al | ~8 µm electroplated Al; press-mark groove 3 µm | Mechanical press-marking/groove used to rupture native oxide | 350 | Local ~250 MPa | 40 min | Vacuum | Mean shear ~20 MPa | HP-3;HT-2 | D0 | Verified | Extreme local pressure improves oxide rupture but is device-stress-limited. |
| AL-D-037 | AL03 Al Farisi et al. 2022, Micromachines 13, 1221, DOI 10.3390/mi13081221 | 1 Al–Al Dry/Mechanical | Al–Al | ~8 µm electroplated Al; press-mark groove 4 µm | Mechanical press-marking/groove used to rupture native oxide | 350 | Local ~250 MPa | 40 min | Vacuum | Mean shear ~18 MPa | HP-3;HT-2 | D0 | Verified | Extreme local pressure improves oxide rupture but is device-stress-limited. |
| AL-D-038 | AL03 Al Farisi et al. 2022, Micromachines 13, 1221, DOI 10.3390/mi13081221 | 1 Al–Al Dry/Mechanical | Al–Al | ~8 µm electroplated Al; press-mark groove 3 µm | Mechanical press-marking/groove used to rupture native oxide | 450 | Local ~250 MPa | 40 min | Vacuum | Mean shear ~68 MPa | HP-3;HT-3 | D0 | Verified | Extreme local pressure improves oxide rupture but is device-stress-limited. |
| AL-D-039 | AL03 Al Farisi et al. 2022, Micromachines 13, 1221, DOI 10.3390/mi13081221 | 1 Al–Al Dry/Mechanical | Al–Al | ~8 µm electroplated Al; press-mark groove 4 µm | Mechanical press-marking/groove used to rupture native oxide | 450 | Local ~250 MPa | 40 min | Vacuum | Mean shear ~75 MPa | HP-3;HT-3 | D0 | Verified | Extreme local pressure improves oxide rupture but is device-stress-limited. |
| AL-W-000 | AL04 Chen et al. 2013, Applied Physics A, DOI 10.1007/s00339-013-7860-7 | 2 Al–Al Wet/Mixed | Al–Al | 99.9 wt% pure Al bulk | SiC #1000 polish → acetone → NaOH 8 g/L 2 min → HNO3 15 vol% 5 min → DI/acetone ultrasonic → Ar ion 1 keV, 340 mA, 0 min | 350 | 10 MPa | 180 min | High vacuum (paper reports <3×10^x Pa; exponent requires source-PDF recheck) | Conventional DB at 350°C: poor/infeasible; oxide remains | OX-3;VD-3 | D0 | Verified | Wet + dry activation. Final ion activation time is the swept variable. |
| AL-W-030 | AL04 Chen et al. 2013, Applied Physics A, DOI 10.1007/s00339-013-7860-7 | 2 Al–Al Wet/Mixed | Al–Al | 99.9 wt% pure Al bulk | SiC #1000 polish → acetone → NaOH 8 g/L 2 min → HNO3 15 vol% 5 min → DI/acetone ultrasonic → Ar ion 1 keV, 340 mA, 30 min | 350 | 10 MPa | 180 min | High vacuum (paper reports <3×10^x Pa; exponent requires source-PDF recheck) | Improved vs no ion clean; residual oxide still present | OX-2;VD-2 | D0 | Verified | Wet + dry activation. Final ion activation time is the swept variable. |
| AL-W-060 | AL04 Chen et al. 2013, Applied Physics A, DOI 10.1007/s00339-013-7860-7 | 2 Al–Al Wet/Mixed | Al–Al | 99.9 wt% pure Al bulk | SiC #1000 polish → acetone → NaOH 8 g/L 2 min → HNO3 15 vol% 5 min → DI/acetone ultrasonic → Ar ion 1 keV, 340 mA, 60 min | 350 | 10 MPa | 180 min | High vacuum (paper reports <3×10^x Pa; exponent requires source-PDF recheck) | Further improved; residual oxide ratio decreased | OX-1;VD-1 | D0 | Verified | Wet + dry activation. Final ion activation time is the swept variable. |
| AL-W-120 | AL04 Chen et al. 2013, Applied Physics A, DOI 10.1007/s00339-013-7860-7 | 2 Al–Al Wet/Mixed | Al–Al | 99.9 wt% pure Al bulk | SiC #1000 polish → acetone → NaOH 8 g/L 2 min → HNO3 15 vol% 5 min → DI/acetone ultrasonic → Ar ion 1 keV, 340 mA, 120 min | 350 | 10 MPa | 180 min | High vacuum (paper reports <3×10^x Pa; exponent requires source-PDF recheck) | Maximum tensile strength 62.3 MPa; elongation 14.1% | HT-2;DATA-0 | D0 | Verified | Wet + dry activation. Final ion activation time is the swept variable. |
| AL-D-040 | AL05 Rebhan et al. 2016, ECS Trans. 75, 15, DOI 10.1149/07509.0015ECST | 1 Al–Al Dry/Mechanical | Al–Al | Patterned-pure-Al-100; Patterned pure Al | ComBond proprietary dry oxide removal; no air break | 100 | 60 kN (~114.3 MPa nominal frame pressure) | 60 min | High-vacuum cluster / vacuum bonder | Dicing yield 100%; tensile ~23 MPa | VD-1 | D0 | Verified |  |
| AL-D-041 | AL05 Rebhan et al. 2016, ECS Trans. 75, 15, DOI 10.1149/07509.0015ECST | 1 Al–Al Dry/Mechanical | Al–Al | Patterned-pure-Al-150; Patterned pure Al | ComBond proprietary dry oxide removal; no air break | 150 | 60 kN (~114.3 MPa nominal frame pressure) | 60 min | High-vacuum cluster / vacuum bonder | Dicing yield 100%; tensile ~37 MPa | VD-1 | D0 | Verified |  |
| AL-D-042 | AL05 Rebhan et al. 2016, ECS Trans. 75, 15, DOI 10.1149/07509.0015ECST | 1 Al–Al Dry/Mechanical | Al–Al | Blank-ALPS-ComBond-150; 300 nm Al-0.5Cu /20 nm Ti, ALPS | ComBond mild dry oxide removal; no air break | 150 | 60 kN = 1.9 MPa full area | 90 min | High-vacuum cluster / vacuum bonder | High-quality low-T full-area bond; oxide-free atomic-contact regions | VD-1 | D0 | Verified |  |
| AL-D-043 | AL05 Rebhan et al. 2016, ECS Trans. 75, 15, DOI 10.1149/07509.0015ECST | 1 Al–Al Dry/Mechanical | Al–Al | Blank-ALPS-EVG520-550; 300 nm Al-0.5Cu /20 nm Ti, ALPS | Conventional TCB; no oxide removal | 550 | 60 kN = 1.9 MPa full area | 90 min | High-vacuum cluster / vacuum bonder | Weak/poor despite 550°C because oxide intact at low pressure | OX-3;HT-3 | D0 | Verified |  |
| AL-D-044 | AL06 Hinterreiter et al. 2018, Microsyst. Technol. 24, 773–777, DOI 10.1007/s00542-017-3520-8 | 1 Al–Al Dry/Mechanical | Al–Al | Unstructured 200 mm, 300 nm Al-0.5Cu /20 nm Ti | ComBond proprietary dry oxide removal; no air break | 150 | 60 kN = 1.9 MPa full area | 90 min | High vacuum | Minor interface defects; large defects mainly particle-related | VD-2 | D0 | Verified | Post-bond anneal=No post-anneal |
| AL-D-045 | AL06 Hinterreiter et al. 2018, Microsyst. Technol. 24, 773–777, DOI 10.1007/s00542-017-3520-8 | 1 Al–Al Dry/Mechanical | Al–Al | Unstructured 200 mm, 300 nm Al-0.5Cu /20 nm Ti | ComBond proprietary dry oxide removal; no air break | 150 | 60 kN = 1.9 MPa full area | 90 min | High vacuum | Small weakly bonded regions partially closed; weak-area fraction drops substantially | VD-1 | D0 | Verified | Post-bond anneal=250°C, 1 h |
| AL-D-046 | AL06 Hinterreiter et al. 2018, Microsyst. Technol. 24, 773–777, DOI 10.1007/s00542-017-3520-8 | 1 Al–Al Dry/Mechanical | Al–Al | Unstructured 200 mm, 300 nm Al-0.5Cu /20 nm Ti | ComBond proprietary dry oxide removal; no air break | 150 | 60 kN = 1.9 MPa full area | 90 min | High vacuum | Further void closure; particle-origin defects remain | VD-1;HT-2 | D0 | Verified | Post-bond anneal=350°C, 1 h |
| AL-D-047 | AL07 Cheemalamarri et al. 2020, Mater. Res. Express, DOI 10.1088/2051-672X/abbb81 | 1 Al–Al Dry/Mechanical | Al–Al | Al-2%Cu with ~2 nm Pd passivation | Ultrathin Pd deposited in situ to suppress Al oxidation | 230 | ~3 MPa | 40 min | Wafer bonder, controlled ambient | 250°C gives good-quality low-T interface; 230°C included in optimization series | IL-2;HT-1 | D1 | Verified | Not strict bare Al/Al because Pd remains/interdiffuses. |
| AL-D-048 | AL07 Cheemalamarri et al. 2020, Mater. Res. Express, DOI 10.1088/2051-672X/abbb81 | 1 Al–Al Dry/Mechanical | Al–Al | Al-2%Cu with ~2 nm Pd passivation | Ultrathin Pd deposited in situ to suppress Al oxidation | 250 | ~3 MPa | 40 min | Wafer bonder, controlled ambient | 250°C gives good-quality low-T interface; 230°C included in optimization series | IL-2;HT-1 | D1 | Verified | Not strict bare Al/Al because Pd remains/interdiffuses. |
| AL-D-049 | AL08 Hu et al. 2022, IEEE ECTC, DOI 10.1109/ECTC51906.2022.00060 | 1 Al–Al Dry/Mechanical | Al–Al | Plasma-activated Al die | Two-step Ar/N2 plasma, total ~10 s; thin AlN-like layer; contact angle ~8° | 300 | 50 N bonding force; anneal under 2000 mbar | Post-bond batch anneal (duration N/R in abstract) | Cleanroom ambient bonding | Bond strength ~32 MPa; good interface | IL-1;DATA-1 | D1 | Verified |  |
| AL-W-050 | AL09 Cheemalamarri et al. 2023, IEEE ECTC, DOI 10.1109/ECTC51909.2023.00294 | 2 Al–Al Wet/Mixed | Al–Al | Blanket Al with Ti passivation | Post-Cl-etch NE14 solvent clean performed promptly → 30 s Ar plasma; Ti passivation ~2–4 nm | ≤300 | <1 MPa | N/R | Controlled bonding environment | Low-T/low-P bonding demonstrated after wet residue clean + Ar activation | IL-2;RES-1 | D1 | Partial | Threshold/range condition as reported; not expanded into unreported factorial combinations. |
| AL-W-051 | AL09 Cheemalamarri et al. 2023, IEEE ECTC, DOI 10.1109/ECTC51909.2023.00294 | 2 Al–Al Wet/Mixed | Al–Al | 6 µm-pitch patterned Al, ~3 µm feature, ~16% metal density | Post-Cl-etch NE14 solvent clean performed promptly → 30 s Ar plasma; Ti passivation ~2–4 nm | ~350 | ≥1 MPa | N/R | Controlled bonding environment | Reliable fine-pitch bonding; immediate cleaning avoids Cl corrosion/pits | IL-2;CR-1;TOP-1 | D1 | Partial | Threshold/range condition as reported; not expanded into unreported factorial combinations. |
| AL-D-052 | AL10 Schulze et al. 2023, ECS Trans. 112, 25, DOI 10.1149/11201.0025ECST | 1 Al–Al Dry/Mechanical | Al–Al | Patterned 200 mm BEOL Al pads | Ar plasma activation 5 min; no vacuum break | 300 | 60 kN | 60 min | EVG ComBond high-vacuum cluster | >95% yield; mΩ-range contacts; paper reports high bond strength in optimized process family | HP-2;HT-2;TOP-1 | D0 | Verified | Exact optimum explicitly reported. |
| AL-D-053 | AL11 Schulze et al. 2024, IEEE TCPMT, DOI 10.1109/TCPMT.2024.3363236 | 1 Al–Al Dry/Mechanical | Al–Al | Collective die-to-wafer, surface-activated Al | Ar plasma surface activation | 300 | 52–60 MPa | 60 min | Controlled/high-vacuum bonding flow | >90% yield, >90 MPa bond strength, mΩ contacts reported | HP-2;HT-2;TOP-1 | D0 | Partial | Pressure reported as range for demonstrated process. |
| AL-D-054 | AL12 Akatsu et al. 1999, J. Mater. Sci., DOI 10.1023/A:1004661610307 | 1 Al–Al Dry/Mechanical | Al–Al | Single-crystal Al cube pair | Ultra-high-vacuum surface-activated bonding | RT | ~40 MPa | N/R | UHV | Atomic Al/Al interface formed at room temperature | HP-2;DATA-1 | D0 | Verified | Not wafer-scale. |
| AL-D-055 | AL13 Schulze et al. 2019, IEEE ECTC, DOI 10.1109/ECTC.2019.00040 | 1 Al–Al Dry/Mechanical | Al–Al | Patterned 200 mm; optimized Al roughness <2 nm | High-vacuum surface treatment followed by TCB without air break | 300–500 | 60 kN | 60 min | High-vacuum cluster | Reliable bonding; 20×20 µm² contacts <50 mΩ | DATA-1;HT-2 | D0 | Partial | Published range retained as one record; no artificial grid expansion. |
| AL-D-056 | AL14 Çakmak et al. 2009, MRS Proc., DOI 10.1557/PROC-1222-DD04-02 | 1 Al–Al Dry/Mechanical | Al–Al | 500 nm Al, full-area 150 mm class wafer | Conventional TCB; surface-treatment/ambient variables studied | 400–550 | 60 kN ≈3.4 MPa | N/R | Forming gas / inert gas conditions studied | IAE increases with T; ≥500°C needed for ~8–10 J/m² | HT-3;OX-2;DATA-1 | D0 | Partial | Temperature range retained as one non-factorial record. |
| AL-D-057 | AL15 Frömel et al. 2011, IEEE Transducers, DOI 10.1109/TRANSDUCERS.2011.5969495 | 1 Al–Al Dry/Mechanical | Al–Al | ~1 µm Al thin layers | Thermocompression with thin metal layers | 450 | ~4.5 MPa | N/R | Controlled bonder ambient | Successful Al–Al condition reported in literature comparison | HT-3;DATA-1 | D0 | Partial |  |
| AL-D-058 | AL16 Yun et al. 2008, IEEE MEMS, DOI 10.1109/MEMSYS.2008.4443780 | 1 Al–Al Dry/Mechanical | Al–Al | ~2 µm Al/Al-Cu MEMS sealing frame | Conventional Al TCB; no final oxide strip | 450 | Reported ~50–100 MPa effective pressure / 60 kN class | N/R | Controlled/vacuum process | Hermetic/electrical interconnection demonstrated; high pressure needed to rupture oxide | HT-3;HP-3;OX-2 | D0 | Partial |  |
| AL-D-059 | AL17 Wu et al. 2025, IEEE Electron Device Letters, DOI 10.1109/LED.2025.3601663 | 1 Al–Al Dry/Mechanical | Al–Al | Al with Ti/Au passivation | Ti/Au passivation suppresses native oxide | 160–250 | 2 MPa | N/R | Controlled bonding | Average shear up to ~40.85 MPa; contact resistivity ~0.93–2.0×10^-7 Ω·cm² reported for process family | IL-2;DATA-1 | D1 | Partial | Temperature range kept as one record. |
| AL-D-060 | AL18 Song et al. 2023, Surfaces and Interfaces, DOI 10.1016/j.surfin.2023.103285 | 1 Al–Al Dry/Mechanical | Al–Al | 1060 Al bulk | Ar ion bombardment 1 keV, dose 2×10^18 ions/cm²; oxide removed; Rms ~0.61 nm in related dataset | 450 | 5 MPa | 90 min | Vacuum/ion-activated diffusion-bonding setup | Bonding ratio ~97.7%; shear strength ~45.9 MPa | HT-2 | D0 | Verified | Too-low dose leaves oxide; too-high dose causes swelling/porous surface and cracking. |
| AL-AUX-001 | AL19 Venugopal et al. 2018 AA5083 homo-diffusion-bonding design matrix (reported table); DOI 10.22214/ijraset.2018.2099 | 1 Al–Al Dry/Mechanical | Al-base homo-bond | AA5083–AA5083, 5 mm rolled plate | Bond faces ground with SiC 200/400/600 grit; acetone clean | 496 | 7 MPa | 21 min | Vacuum chamber (~29 inHg reported) | Bonding strength 19.14 MPa | HT-3 | D0-AUX | Verified | Auxiliary Al-alloy homo-bond record; retain Material_Subtype filter when training thin-film Al model. |
| AL-AUX-002 | AL19 Venugopal et al. 2018 AA5083 homo-diffusion-bonding design matrix (reported table); DOI 10.22214/ijraset.2018.2099 | 1 Al–Al Dry/Mechanical | Al-base homo-bond | AA5083–AA5083, 5 mm rolled plate | Bond faces ground with SiC 200/400/600 grit; acetone clean | 514 | 7 MPa | 21 min | Vacuum chamber (~29 inHg reported) | Bonding strength 27.94 MPa | HT-3 | D0-AUX | Verified | Auxiliary Al-alloy homo-bond record; retain Material_Subtype filter when training thin-film Al model. |
| AL-AUX-003 | AL19 Venugopal et al. 2018 AA5083 homo-diffusion-bonding design matrix (reported table); DOI 10.22214/ijraset.2018.2099 | 1 Al–Al Dry/Mechanical | Al-base homo-bond | AA5083–AA5083, 5 mm rolled plate | Bond faces ground with SiC 200/400/600 grit; acetone clean | 496 | 13 MPa | 21 min | Vacuum chamber (~29 inHg reported) | Bonding strength 21.14 MPa | HT-3;HP-2 | D0-AUX | Verified | Auxiliary Al-alloy homo-bond record; retain Material_Subtype filter when training thin-film Al model. |
| AL-AUX-004 | AL19 Venugopal et al. 2018 AA5083 homo-diffusion-bonding design matrix (reported table); DOI 10.22214/ijraset.2018.2099 | 1 Al–Al Dry/Mechanical | Al-base homo-bond | AA5083–AA5083, 5 mm rolled plate | Bond faces ground with SiC 200/400/600 grit; acetone clean | 514 | 13 MPa | 21 min | Vacuum chamber (~29 inHg reported) | Bonding strength 25.24 MPa | HT-3;HP-2 | D0-AUX | Verified | Auxiliary Al-alloy homo-bond record; retain Material_Subtype filter when training thin-film Al model. |
| AL-AUX-005 | AL19 Venugopal et al. 2018 AA5083 homo-diffusion-bonding design matrix (reported table); DOI 10.22214/ijraset.2018.2099 | 1 Al–Al Dry/Mechanical | Al-base homo-bond | AA5083–AA5083, 5 mm rolled plate | Bond faces ground with SiC 200/400/600 grit; acetone clean | 496 | 7 MPa | 39 min | Vacuum chamber (~29 inHg reported) | Bonding strength 18.14 MPa | HT-3 | D0-AUX | Verified | Auxiliary Al-alloy homo-bond record; retain Material_Subtype filter when training thin-film Al model. |
| AL-AUX-006 | AL19 Venugopal et al. 2018 AA5083 homo-diffusion-bonding design matrix (reported table); DOI 10.22214/ijraset.2018.2099 | 1 Al–Al Dry/Mechanical | Al-base homo-bond | AA5083–AA5083, 5 mm rolled plate | Bond faces ground with SiC 200/400/600 grit; acetone clean | 514 | 7 MPa | 39 min | Vacuum chamber (~29 inHg reported) | Bonding strength 26.54 MPa | HT-3 | D0-AUX | Verified | Auxiliary Al-alloy homo-bond record; retain Material_Subtype filter when training thin-film Al model. |
| AL-AUX-007 | AL19 Venugopal et al. 2018 AA5083 homo-diffusion-bonding design matrix (reported table); DOI 10.22214/ijraset.2018.2099 | 1 Al–Al Dry/Mechanical | Al-base homo-bond | AA5083–AA5083, 5 mm rolled plate | Bond faces ground with SiC 200/400/600 grit; acetone clean | 496 | 13 MPa | 39 min | Vacuum chamber (~29 inHg reported) | Bonding strength 24.54 MPa | HT-3;HP-2 | D0-AUX | Verified | Auxiliary Al-alloy homo-bond record; retain Material_Subtype filter when training thin-film Al model. |
| AL-AUX-008 | AL19 Venugopal et al. 2018 AA5083 homo-diffusion-bonding design matrix (reported table); DOI 10.22214/ijraset.2018.2099 | 1 Al–Al Dry/Mechanical | Al-base homo-bond | AA5083–AA5083, 5 mm rolled plate | Bond faces ground with SiC 200/400/600 grit; acetone clean | 514 | 13 MPa | 39 min | Vacuum chamber (~29 inHg reported) | Bonding strength 29.71 MPa | HT-3;HP-2 | D0-AUX | Verified | Auxiliary Al-alloy homo-bond record; retain Material_Subtype filter when training thin-film Al model. |
| AL-AUX-009 | AL19 Venugopal et al. 2018 AA5083 homo-diffusion-bonding design matrix (reported table); DOI 10.22214/ijraset.2018.2099 | 1 Al–Al Dry/Mechanical | Al-base homo-bond | AA5083–AA5083, 5 mm rolled plate | Bond faces ground with SiC 200/400/600 grit; acetone clean | 490 | 10 MPa | 30 min | Vacuum chamber (~29 inHg reported) | Bonding strength 19.64 MPa | HT-3 | D0-AUX | Verified | Auxiliary Al-alloy homo-bond record; retain Material_Subtype filter when training thin-film Al model. |
| AL-AUX-010 | AL19 Venugopal et al. 2018 AA5083 homo-diffusion-bonding design matrix (reported table); DOI 10.22214/ijraset.2018.2099 | 1 Al–Al Dry/Mechanical | Al-base homo-bond | AA5083–AA5083, 5 mm rolled plate | Bond faces ground with SiC 200/400/600 grit; acetone clean | 520 | 10 MPa | 30 min | Vacuum chamber (~29 inHg reported) | Bonding strength 30.94 MPa | HT-3 | D0-AUX | Verified | Auxiliary Al-alloy homo-bond record; retain Material_Subtype filter when training thin-film Al model. |
| AL-AUX-011 | AL19 Venugopal et al. 2018 AA5083 homo-diffusion-bonding design matrix (reported table); DOI 10.22214/ijraset.2018.2099 | 1 Al–Al Dry/Mechanical | Al-base homo-bond | AA5083–AA5083, 5 mm rolled plate | Bond faces ground with SiC 200/400/600 grit; acetone clean | 505 | 5 MPa | 30 min | Vacuum chamber (~29 inHg reported) | Bonding strength 18.44 MPa | HT-3 | D0-AUX | Verified | Auxiliary Al-alloy homo-bond record; retain Material_Subtype filter when training thin-film Al model. |
| AL-AUX-012 | AL19 Venugopal et al. 2018 AA5083 homo-diffusion-bonding design matrix (reported table); DOI 10.22214/ijraset.2018.2099 | 1 Al–Al Dry/Mechanical | Al-base homo-bond | AA5083–AA5083, 5 mm rolled plate | Bond faces ground with SiC 200/400/600 grit; acetone clean | 505 | 15 MPa | 30 min | Vacuum chamber (~29 inHg reported) | Bonding strength 23.74 MPa | HT-3;HP-2 | D0-AUX | Verified | Auxiliary Al-alloy homo-bond record; retain Material_Subtype filter when training thin-film Al model. |
| AL-AUX-013 | AL19 Venugopal et al. 2018 AA5083 homo-diffusion-bonding design matrix (reported table); DOI 10.22214/ijraset.2018.2099 | 1 Al–Al Dry/Mechanical | Al-base homo-bond | AA5083–AA5083, 5 mm rolled plate | Bond faces ground with SiC 200/400/600 grit; acetone clean | 505 | 10 MPa | 15 min | Vacuum chamber (~29 inHg reported) | Bonding strength 20.44 MPa | HT-3 | D0-AUX | Verified | Auxiliary Al-alloy homo-bond record; retain Material_Subtype filter when training thin-film Al model. |
| AL-AUX-014 | AL19 Venugopal et al. 2018 AA5083 homo-diffusion-bonding design matrix (reported table); DOI 10.22214/ijraset.2018.2099 | 1 Al–Al Dry/Mechanical | Al-base homo-bond | AA5083–AA5083, 5 mm rolled plate | Bond faces ground with SiC 200/400/600 grit; acetone clean | 505 | 10 MPa | 45 min | Vacuum chamber (~29 inHg reported) | Bonding strength 23.94 MPa | HT-3 | D0-AUX | Verified | Auxiliary Al-alloy homo-bond record; retain Material_Subtype filter when training thin-film Al model. |
| AL-AUX-015 | AL19 Venugopal et al. 2018 AA5083 homo-diffusion-bonding design matrix (reported table); DOI 10.22214/ijraset.2018.2099 | 1 Al–Al Dry/Mechanical | Al-base homo-bond | AA5083–AA5083, 5 mm rolled plate | Bond faces ground with SiC 200/400/600 grit; acetone clean | 505 | 10 MPa | 30 min | Vacuum chamber (~29 inHg reported) | Bonding strength 22.14 MPa | HT-3 | D0-AUX | Verified | Auxiliary Al-alloy homo-bond record; retain Material_Subtype filter when training thin-film Al model. |
| AL-AUX-016 | AL19 Venugopal et al. 2018 AA5083 homo-diffusion-bonding design matrix (reported table); DOI 10.22214/ijraset.2018.2099 | 1 Al–Al Dry/Mechanical | Al-base homo-bond | AA5083–AA5083, 5 mm rolled plate | Bond faces ground with SiC 200/400/600 grit; acetone clean | 505 | 10 MPa | 30 min | Vacuum chamber (~29 inHg reported) | Bonding strength 21.14 MPa | HT-3 | D0-AUX | Verified | Auxiliary Al-alloy homo-bond record; retain Material_Subtype filter when training thin-film Al model. |
| AL-AUX-017 | AL19 Venugopal et al. 2018 AA5083 homo-diffusion-bonding design matrix (reported table); DOI 10.22214/ijraset.2018.2099 | 1 Al–Al Dry/Mechanical | Al-base homo-bond | AA5083–AA5083, 5 mm rolled plate | Bond faces ground with SiC 200/400/600 grit; acetone clean | 505 | 10 MPa | 30 min | Vacuum chamber (~29 inHg reported) | Bonding strength 20.14 MPa | HT-3 | D0-AUX | Verified | Auxiliary Al-alloy homo-bond record; retain Material_Subtype filter when training thin-film Al model. |
| AL-AUX-018 | AL19 Venugopal et al. 2018 AA5083 homo-diffusion-bonding design matrix (reported table); DOI 10.22214/ijraset.2018.2099 | 1 Al–Al Dry/Mechanical | Al-base homo-bond | AA5083–AA5083, 5 mm rolled plate | Bond faces ground with SiC 200/400/600 grit; acetone clean | 505 | 10 MPa | 30 min | Vacuum chamber (~29 inHg reported) | Bonding strength 20.14 MPa | HT-3 | D0-AUX | Verified | Auxiliary Al-alloy homo-bond record; retain Material_Subtype filter when training thin-film Al model. |
| AL-AUX-019 | AL19 Venugopal et al. 2018 AA5083 homo-diffusion-bonding design matrix (reported table); DOI 10.22214/ijraset.2018.2099 | 1 Al–Al Dry/Mechanical | Al-base homo-bond | AA5083–AA5083, 5 mm rolled plate | Bond faces ground with SiC 200/400/600 grit; acetone clean | 505 | 10 MPa | 30 min | Vacuum chamber (~29 inHg reported) | Bonding strength 20.14 MPa | HT-3 | D0-AUX | Verified | Auxiliary Al-alloy homo-bond record; retain Material_Subtype filter when training thin-film Al model. |
| AL-AUX-020 | AL19 Venugopal et al. 2018 AA5083 homo-diffusion-bonding design matrix (reported table); DOI 10.22214/ijraset.2018.2099 | 1 Al–Al Dry/Mechanical | Al-base homo-bond | AA5083–AA5083, 5 mm rolled plate | Bond faces ground with SiC 200/400/600 grit; acetone clean | 505 | 10 MPa | 30 min | Vacuum chamber (~29 inHg reported) | Bonding strength 20.14 MPa | HT-3 | D0-AUX | Verified | Auxiliary Al-alloy homo-bond record; retain Material_Subtype filter when training thin-film Al model. |
| AL-AUX-HIP-01 | AL20 AA6061/AA6061 HIP interface study, OSTI report purl 1870635 | 1 Al–Al Dry/Mechanical | Al-base homo-bond | AA6061-T6–AA6061-T6 plates | HIP canning/assembly; native interfacial oxide participates in Mg2Al2O5 reaction | 350 | 207.0 MPa HIP | 25.0 h | HIP | Low strength; voids and amorphous oxide remain; average peel bond strength 1.3 N/mm | VD-3;HP-3;HT-2 | D0-AUX | Verified |  |
| AL-AUX-HIP-02 | AL20 AA6061/AA6061 HIP interface study, OSTI report purl 1870635 | 1 Al–Al Dry/Mechanical | Al-base homo-bond | AA6061-T6–AA6061-T6 plates | HIP canning/assembly; native interfacial oxide participates in Mg2Al2O5 reaction | 400 | 155.1 MPa HIP | 5.0 h | HIP | Moderate peel bond strength; average peel bond strength 7.0 N/mm | HP-3;HT-3 | D0-AUX | Verified |  |
| AL-AUX-HIP-03 | AL20 AA6061/AA6061 HIP interface study, OSTI report purl 1870635 | 1 Al–Al Dry/Mechanical | Al-base homo-bond | AA6061-T6–AA6061-T6 plates | HIP canning/assembly; native interfacial oxide participates in Mg2Al2O5 reaction | 450 | 103.4 MPa HIP | 1.0 h | HIP | Highest reported peel bond strength; thinner/more uniform Mg2Al2O5; average peel bond strength 9.4 N/mm | HP-3;HT-3 | D0-AUX | Verified |  |
| AL-AUX-HIP-04 | AL20 AA6061/AA6061 HIP interface study, OSTI report purl 1870635 | 1 Al–Al Dry/Mechanical | Al-base homo-bond | AA6061-T6–AA6061-T6 plates | HIP canning/assembly; native interfacial oxide participates in Mg2Al2O5 reaction | 560 | 103.4 MPa HIP | 1.5 h | HIP | Strength lower than 450°C; thicker oxide/coarser Mg2Si; average peel bond strength 7.3 N/mm | HP-3;HT-3;RC-1 | D0-AUX | Verified |  |
| MO-D-001 | MO01 Hashimoto & Tanuma 1968, Journal of Japan Welding Society, DOI 10.2207/qjjws1943.37.1345 | 3 Mo–Mo Dry/Diffusion | Mo–Mo | Pure Mo direct | Emery-polished / cleaned; direct bond without interlayer | ~900 | 5–10% deformation; pressure N/R | N/R | High vacuum | Local bonding begins; insufficient for robust low-deformation direct bond | HT-3;VD-3 | D0 | Partial |  |
| MO-D-002 | MO01 Hashimoto & Tanuma 1968, Journal of Japan Welding Society, DOI 10.2207/qjjws1943.37.1345 | 3 Mo–Mo Dry/Diffusion | Mo–Mo | Pure Mo direct | Emery-polished / cleaned; direct bond without interlayer | ~1100 | 5–10% deformation; pressure N/R | N/R | High vacuum | Joint strength rises sharply as diffusion/contact improve | HT-3;RC-2 | D0 | Partial |  |
| MO-D-003 | MO01 Hashimoto & Tanuma 1968, Journal of Japan Welding Society, DOI 10.2207/qjjws1943.37.1345 | 3 Mo–Mo Dry/Diffusion | Mo–Mo | Pure Mo direct | Emery-polished / cleaned; direct bond without interlayer | 1250 | 5–10% deformation; pressure N/R | 5 min | High vacuum | Grains cross original interface; complete recrystallization but embrittlement/strength loss | HT-3;RC-3 | D0 | Partial |  |
| MO-D-004 | MO01 Hashimoto & Tanuma 1968, Journal of Japan Welding Society, DOI 10.2207/qjjws1943.37.1345 | 3 Mo–Mo Dry/Diffusion | Mo–Mo | Pure Mo / Cd 2.5 µm / Mo | Mechanical/electropolish variants + benzine clean; plated insert metal | 1100 | 500 kg/joint (Table-3 series) | 15 min | Vacuum | Survived rapid remelt test to 2000°C | IL-3 | D1 | Verified | D1: same Mo substrates but non-Mo insert remains/participates. |
| MO-D-005 | MO01 Hashimoto & Tanuma 1968, Journal of Japan Welding Society, DOI 10.2207/qjjws1943.37.1345 | 3 Mo–Mo Dry/Diffusion | Mo–Mo | Pure Mo / Ag 2.5 µm / Mo | Mechanical/electropolish variants + benzine clean; plated insert metal | 1100 | 500 kg/joint (Table-3 series) | 15 min | Vacuum | Survived rapid remelt test to 2000°C | IL-2 | D1 | Verified | D1: same Mo substrates but non-Mo insert remains/participates. |
| MO-D-006 | MO01 Hashimoto & Tanuma 1968, Journal of Japan Welding Society, DOI 10.2207/qjjws1943.37.1345 | 3 Mo–Mo Dry/Diffusion | Mo–Mo | Pure Mo / Cu 2.5 µm / Mo | Mechanical/electropolish variants + benzine clean; plated insert metal | 1100 | 500 kg/joint (Table-3 series) | 15 min | Vacuum | Survived rapid remelt test to 2000°C | IL-2 | D1 | Verified | D1: same Mo substrates but non-Mo insert remains/participates. |
| MO-D-007 | MO01 Hashimoto & Tanuma 1968, Journal of Japan Welding Society, DOI 10.2207/qjjws1943.37.1345 | 3 Mo–Mo Dry/Diffusion | Mo–Mo | Pure Mo / Ni 2.5 µm / Mo | Mechanical/electropolish variants + benzine clean; plated insert metal | 1100 | 500 kg/joint (Table-3 series) | 15 min | Vacuum | Survived rapid remelt test to 2000°C; strong low-T joining but Mo-Ni intermetallic concerns | IL-2 | D1 | Verified | D1: same Mo substrates but non-Mo insert remains/participates. |
| MO-D-008 | MO01 Hashimoto & Tanuma 1968, Journal of Japan Welding Society, DOI 10.2207/qjjws1943.37.1345 | 3 Mo–Mo Dry/Diffusion | Mo–Mo | Pure Mo / Fe 2.5 µm / Mo | Mechanical/electropolish variants + benzine clean; plated insert metal | 1100 | 500 kg/joint (Table-3 series) | 15 min | Vacuum | Survived rapid remelt test to 2000°C; intermetallic concerns | IL-2 | D1 | Verified | D1: same Mo substrates but non-Mo insert remains/participates. |
| MO-D-009 | MO01 Hashimoto & Tanuma 1968, Journal of Japan Welding Society, DOI 10.2207/qjjws1943.37.1345 | 3 Mo–Mo Dry/Diffusion | Mo–Mo | Pure Mo / Cu 2.5 µm / Mo | Mechanical/electropolish variants + benzine clean; plated insert metal | 900 | 500 kg/joint (Table-3 series) | 15 min | Vacuum | Survived rapid remelt test to 2000°C; partial Mo-Mo direct contact inferred | IL-2;HT-3 | D1 | Partial | D1: same Mo substrates but non-Mo insert remains/participates. |
| MO-D-010 | MO01 Hashimoto & Tanuma 1968, Journal of Japan Welding Society, DOI 10.2207/qjjws1943.37.1345 | 3 Mo–Mo Dry/Diffusion | Mo–Mo | Pure Mo / Cu 5.0 µm / Mo | Mechanical/electropolish variants + benzine clean; plated insert metal | 1000 | 500 kg/joint (Table-3 series) | 15 min | Vacuum | Survived rapid remelt test to 2000°C | IL-2;HT-3 | D1 | Partial | D1: same Mo substrates but non-Mo insert remains/participates. |
| MO-D-011 | MO01 Hashimoto & Tanuma 1968, Journal of Japan Welding Society, DOI 10.2207/qjjws1943.37.1345 | 3 Mo–Mo Dry/Diffusion | Mo–Mo | Pure Mo / Cu 30.0 µm / Mo | Mechanical/electropolish variants + benzine clean; plated insert metal | 1000 | 500 kg/joint (Table-3 series) | 15 min | Vacuum | Remelt/failure near ~1100°C; thick interlayer behaves as Cu-dominated joint | IL-3;HT-3 | D1 | Partial | D1: same Mo substrates but non-Mo insert remains/participates. |
| MO-D-012 | MO02 Historical gas-pressure Mo self-bonding (reported in Hashimoto 1968) | 3 Mo–Mo Dry/Diffusion | Mo–Mo | Bulk pure Mo direct | Surface preparation varies by archival study | 1260–1440 | 4.5 ton/in² | 3 h | Gas-pressure / protective environment | Grain migration across interface reported | HT-3;HP-3;RC-3 | D0 | Partial |  |
| MO-D-013 | MO03 Kohler et al., cited/compiled in Al-Mashhadani 2019 | 3 Mo–Mo Dry/Diffusion | Mo–Mo | Bulk pure Mo direct | Surface preparation varies by archival study | 1200 | 40 MPa | 20 min | Inert/vacuum diffusion bonding | Pure Mo–Mo joining reported NOT possible under this condition | HT-3;VD-3 | D0 | Secondary-verified |  |
| MO-D-014 | MO04 Charles et al., cited/compiled in Al-Mashhadani 2019 | 3 Mo–Mo Dry/Diffusion | Mo–Mo | Bulk pure Mo direct | Surface preparation varies by archival study | 1650 | 34.47 kPa | 60 min | Vacuum ~13×10^-5 kPa (~0.13 Pa) | Successful; original interface line not distinguishable optically | HT-3;RC-3 | D0 | Secondary-verified |  |
| MO-D-015 | MO05 Gas-pressure clad-fuel study, archival | 3 Mo–Mo Dry/Diffusion | Mo–Mo | Bulk pure Mo direct | Surface preparation varies by archival study | 2300–2600°F (~1260–1427°C) | 10,000 psi (~68.95 MPa) | 3 h | Gas-pressure bonding | Mo self-bonding readily achieved; directional ductility issue; cross-rolling improved ductility | HT-3;HP-3;RC-3 | D0 | Verified |  |
| MO-D-016 | MO06 Al-Mashhadani 2019, Refractory metals low temperature diffusion bonding, TU Chemnitz dissertation | 3 Mo–Mo Dry/Diffusion | Mo–Mo | Pure Mo direct, thesis Exp1 | Surface=As-received; grain orientations L/T/R investigated | N/R in retrieved excerpt | 80 MPa | 360 min | Vacuum diffusion-bonding furnace | Microstructure, hardness, shear/tensile behavior compared across surface state/orientation | DATA-2;HT-3 | D0 | Partial | Retained because actual experiment ID/time/pressure are documented; bonding temperature must be re-extracted from Table III-5 before modeling. |
| MO-D-017 | MO06 Al-Mashhadani 2019, Refractory metals low temperature diffusion bonding, TU Chemnitz dissertation | 3 Mo–Mo Dry/Diffusion | Mo–Mo | Pure Mo direct, thesis Exp2 | Surface=As-received; grain orientations L/T/R investigated | N/R in retrieved excerpt | 80 MPa | 60 min | Vacuum diffusion-bonding furnace | Microstructure, hardness, shear/tensile behavior compared across surface state/orientation | DATA-2;HT-3 | D0 | Partial | Retained because actual experiment ID/time/pressure are documented; bonding temperature must be re-extracted from Table III-5 before modeling. |
| MO-D-018 | MO06 Al-Mashhadani 2019, Refractory metals low temperature diffusion bonding, TU Chemnitz dissertation | 3 Mo–Mo Dry/Diffusion | Mo–Mo | Pure Mo direct, thesis Exp4 | Surface=As-received; grain orientations L/T/R investigated | N/R in retrieved excerpt | 40 MPa | 60 min | Vacuum diffusion-bonding furnace | Microstructure, hardness, shear/tensile behavior compared across surface state/orientation | DATA-2;HT-3 | D0 | Partial | Retained because actual experiment ID/time/pressure are documented; bonding temperature must be re-extracted from Table III-5 before modeling. |
| MO-D-019 | MO06 Al-Mashhadani 2019, Refractory metals low temperature diffusion bonding, TU Chemnitz dissertation | 3 Mo–Mo Dry/Diffusion | Mo–Mo | Pure Mo direct, thesis Exp5.2 | Surface=Polished; grain orientations L/T/R investigated | N/R in retrieved excerpt | 80 MPa | caption conflict: 60 vs 360 min | Vacuum diffusion-bonding furnace | Microstructure, hardness, shear/tensile behavior compared across surface state/orientation | DATA-2;HT-3 | D0 | Conflict-check | Retained because actual experiment ID/time/pressure are documented; bonding temperature must be re-extracted from Table III-5 before modeling. |

## 6. Supporting pretreatment-only database — bonding record 수에서 제외

| ID | Source | Category | Pretreatment condition | Surface result | Problem | Evidence |
|---|---|---|---|---|---|---|
| MO-S-01 | Mo Wet Cleaning for Nano Interconnects (ECS 2022) | 4 Mo–Mo Wet/Supporting | 0.05% HF, 1 min | Mo-compatible but little change in surface oxidation | OX-2 | S |
| MO-S-02 | Mo Wet Cleaning for Nano Interconnects (ECS 2022) | 4 Mo–Mo Wet/Supporting | SC1 | Significant Mo etching due to H2O2; not preferred for pristine bonding surface | CR-3;RG-3 | S |
| MO-S-03 | Mo Wet Cleaning for Nano Interconnects (ECS 2022) | 4 Mo–Mo Wet/Supporting | FOTOPUR R-2403 semi-aqueous | Removes post-etch residue and much of Mo oxide; ex-situ reoxidation still a risk | OX-1;RES-1 | S |
| MO-S-04 | O3-bake + wet Mo oxide removal (ECS 2022) | 4 Mo–Mo Wet/Supporting | O3 180–290°C, 100 g/m³, 18 L/min → NH4OH | Controlled oxidation/dissolution; roughness depends strongly on bake T | RG-2 | S |
| MO-S-05 | O3-bake + hot NH4OH optimized | 4 Mo–Mo Wet/Supporting | O3 290°C + 29% NH4OH diluted 1:8 at 70°C | Residual crystalline MoOx removed; Rq ~0.38 nm reported | OX-1;RG-1 | S |
| MO-S-06 | ASTM B629 Mo preparation | 4 Mo–Mo Wet/Supporting | Cathodic alkaline clean 60–75 g/L, 60–75°C, ~6V, 30–60s | Standardized preclean before plating | DATA-1 | S |
| MO-S-07 | ASTM B629 Mo preparation | 4 Mo–Mo Wet/Supporting | 80 mass% H2SO4, 20–30°C, 1100–2200 A/m², 30s | Electropolishing option | CR-1;RG-1 | S |
| MO-S-08 | ASTM B629 Mo preparation | 4 Mo–Mo Wet/Supporting | 50/50 vol% H2SO4/H3PO4, 50–55°C, 2500 A/m², 180s | Electropolishing option | CR-1;RG-1 | S |
| MO-S-09 | US Patent 4169027 Mo electropolish | 4 Mo–Mo Wet/Supporting | 87.5 vol% IPA +12.5 vol% conc H2SO4; example ~5 A/cm² at 22°C | Smooth Mo surface with slight roughness | CR-1;RG-1 | S |
| AL-S-01 | Al wet-clean chemistry supporting patents/literature | 2 Al–Al Wet/Mixed | NH4F/NH4HF2 in low-water alcohol/acetate chemistry | Can remove/transform alumina while suppressing Al/SiO2 attack; bonding must follow before reoxidation | CR-1;OX-1 | S |
| AL-S-02 | Al cleaning composition, US 9394509 | 2 Al–Al Wet/Mixed | 98.7–99.6% IPA + 0.002–0.01% HF +0.02–0.05% NH4F +0.4–1.25% H2O | Metal etch amount reported ≤5 Å in disclosed conditions; oxide/polymer removal | CR-1 | S |
| AL-S-03 | Al dicing-clean study, Appl. Sci. 2023 | 2 Al–Al Wet/Mixed | 10% H2SO4 +4% NH4F-HF +86% H2O | Al protected in test but UBM undercut observed | CR-2 | S |

## 7. 조건별 주요 문제 해석

### 7.1 Al–Al

Al–Al에서 가장 반복적으로 나타나는 지배 문제는 `Al2O3 native oxide`이다. Conventional TCB에서는 oxide를 기계적으로 깨고 실제 금속 접촉면적을 늘리기 위해 대체로 높은 온도와 높은 local pressure가 필요하다. Malik 계열 데이터에서는 400 °C에서 18–36 kN 조건이 불완전 접합으로 남는 반면, 450–550 °C 또는 400 °C/60 kN으로 이동하면 dicing yield와 bond strength가 급격히 개선된다.

반대로 in-situ dry oxide removal 또는 Ar/Ar–N2 activation을 사용하면 bonding temperature는 100–300 °C 영역으로 내려간다. 이 영역에서는 지배적인 실패 원인이 oxide 자체에서 `particle`, `roughness`, `etch residue`, `wafer bow/topography`, `air-break/reoxidation`으로 이동한다.

Al wet chemistry는 단독 bonding solution이라기보다 `residue removal → dry activation → bonding`의 mixed route가 현재 근거가 더 강하다. 과도한 wet clean은 pitting/Rz 증가와 passivation 손실을 만들 수 있으므로 단순히 “더 오래 세정 = 더 좋은 접합”으로 처리하면 안 된다.

### 7.2 Mo–Mo

Bulk Mo–Mo direct diffusion bonding은 Al보다 훨씬 높은 열예산을 요구한다. 고전 연구에서는 약 900 °C에서 국부 접합이 시작되지만 5–10% 정도의 낮은 변형률에서는 충분한 강도를 얻기 어렵고, 약 1100 °C 이후 bonding이 급격히 진행된다. 그러나 1200–1250 °C 이상에서는 recrystallization과 grain growth가 강해져 Mo의 취화와 강도 저하가 발생한다.

따라서 Mo의 공정창은 단순한 `T↑ → bond quality↑`가 아니다.

`low T → diffusion/contact insufficient`  
`intermediate T → bonding improves`  
`high T → recrystallization/embrittlement penalty`

의 비단조(non-monotonic) 구조로 모델링해야 한다.

Interlayer는 bonding temperature를 낮추지만 strict direct Mo/Mo interface가 아니며, Cu/Ni/Fe/Ag 등은 각각 diffusion, IMC, remelting, thermal stability 문제를 추가한다.

### 7.3 Mo wet pretreatment — 핵심 research gap

Mo에 wet chemistry를 사용하면 반드시 표면이 나빠진다는 결론은 맞지 않는다. 0.05% HF는 Mo 자체와 비교적 compatible하지만 oxide 제거 효과가 제한적이고, SC1/H2O2는 Mo를 강하게 etch하여 roughness 문제를 만들 수 있다. 반면 semi-aqueous formulation 또는 controlled MoOx formation + hot NH4OH dissolution은 oxide/residue 제거와 sub-nm 수준 roughness 회복 가능성을 보여준다.

그러나 현재 확보한 문헌에서 다음 연결이 정량적으로 충분히 검증되어 있지 않다.

`Mo wet oxide removal → sub-nm surface → controlled/no-air-break transfer → Mo/Mo direct bond → strength/electrical/TBR`

따라서 이 구간이 직접적인 논문 주제가 될 수 있다.


## 8. 연구용 데이터 모델 권장

실제 ML/DT/PINN 입력용으로는 위 master table을 그대로 쓰지 말고 아래 계층을 분리한다.

### Input features

- Material: pure Al / Al-Cu / 1060 / AA5083 / AA6061 / pure Mo / TZM
- Film_or_bulk
- Film thickness
- Grain orientation / texture
- Initial Ra / Rq / Rz
- Oxide thickness
- Wet chemistry / concentration / temperature / time
- Plasma gas / power / ion energy / dose / duration
- Air-break 여부
- Pretreat-to-bond delay
- Bond temperature
- Pressure / force / estimated local pressure
- Holding time
- Atmosphere / vacuum
- Post-anneal temperature/time
- Geometry / contact-area ratio / frame width

### Outputs

- Bonded / unbonded
- Dicing yield
- Void fraction
- Tensile strength
- Shear strength
- Peel strength
- Interfacial adhesion energy
- Contact resistance / contact resistivity
- Interface oxide thickness
- Grain-boundary migration
- Recrystallized fraction
- Residual stress
- Thermal boundary resistance (향후 직접 측정 권장)

### Mandatory provenance flags

`literature_measured`, `literature_reported_range`, `digitized_from_figure`, `derived`, `experimental`, `simulation`, `missing`.

특히 `reported_range`를 개별 숫자 sample로 복제해서는 안 된다.


## 9. 바로 실험으로 연결하기 위한 권장 DOE

### 9.1 Al control experiment

| Group | Wet | Dry activation | Bond T | 목적 |
|---|---|---|---|---|
| A0 | None | None | 300/400/450 °C | conventional baseline |
| A1 | None | Ar | 200/250/300 °C | dry SAB baseline |
| A2 | residue-clean only | None | 250/300 °C | wet-only contribution |
| A3 | residue-clean | Ar | 200/250/300 °C | mixed route |
| A4 | optimized passivation | mild Ar | 200/250/300 °C | oxidation-delay route |

### 9.2 Mo research experiment

| Group | Wet | Dry activation | Suggested initial T sweep | 핵심 질문 |
|---|---|---|---|---|
| M0 | None | None | 600→1000 °C | untreated baseline |
| M1 | None | mild Ar | 500→900 °C | dry activation only |
| M2 | 0.05% HF | None | 500→900 °C | HF compatibility vs oxide removal |
| M3 | semi-aqueous Mo-oxide clean | None | 500→900 °C | wet-only feasibility |
| M4 | 0.05% HF | Ar | 400→800 °C | wet+dry synergy |
| M5 | semi-aqueous clean | Ar | 400→800 °C | strongest candidate |
| M6 | controlled O3/NH4OH smoothing | Ar | 400→800 °C | sub-nm surface + activation |

> 위 온도 범위는 **문헌 재현조건이 아니라 향후 DOE 후보 범위**이다. 실제 장비/막 두께/잔류응력/재결정 거동을 고려해 pilot test에서 축소해야 한다.

### 9.3 Characterization minimum set

1. AFM: Ra/Rq/Rz
2. XPS: metallic fraction, O/metal ratio, oxide thickness proxy
3. C-SAM/SAT: void map
4. Cross-sectional SEM/TEM
5. Four-point / Kelvin / CBKR contact resistance
6. Shear or tensile bond strength
7. XRD/EBSD: texture and recrystallization
8. TDTR/FDTR: thermal boundary resistance — Mo/AlN 연구와 연결할 경우 특히 중요


## 10. 현재 DB의 제한점

- 107개 record는 모두 “문헌에서 실제 condition/sample이 확인되었거나, 논문이 명시한 단일 demonstrated range를 한 record로 보존한 것”이다.
- `Partial` record는 DOI/초록/검색 가능한 본문만으로 일부 수치가 확인된 경우다.
- Al-Mashhadani thesis의 Exp5.2는 검색 가능한 캡션 사이에 60 min과 360 min이 모두 나타나므로 `Conflict-check`로 남겼다.
- Malik 2014의 21개 record는 7개의 wafer-level bonding recipe를 3개의 실제 frame geometry로 분해한 sample-condition records이다. geometry별 exact yield가 별도로 공개되지 않은 경우 결과는 aggregate trend로 기록했다.
- AA5083/AA6061 records는 순수/박막 Al–Al과 물리적으로 동일하지 않으므로 `D0-AUX`로 분리했다. thin-film Al direct-bonding 모델 학습 시 별도 domain flag가 필수다.
- Mo Wet category는 의도적으로 direct bonding records를 만들지 않았다. 현재 근거는 주로 surface-cleaning/oxide-removal이므로 `S`로 유지해야 한다.

## 11. Machine-readable schema 제안

```yaml
record_id:
source_id:
doi:
material_family:
material_subtype:
evidence_class:
film_or_bulk:
film_thickness_nm:
grain_orientation:
pretreatment:
  mechanical:
  wet_chemistry:
  concentration:
  temperature_C:
  time_s:
  plasma_gas:
  plasma_power_W:
  ion_energy_eV:
  ion_dose_cm2:
  activation_time_s:
  air_break:
  delay_to_bond_min:
surface:
  Ra_nm:
  Rq_nm:
  Rz_nm:
  oxide_thickness_nm:
bond:
  temperature_C:
  force_kN:
  pressure_MPa:
  time_min:
  ambient:
post_anneal:
  temperature_C:
  time_min:
results:
  success:
  dicing_yield_pct:
  void_fraction_pct:
  tensile_strength_MPa:
  shear_strength_MPa:
  peel_strength_N_per_mm:
  adhesion_energy_J_m2:
  contact_resistance_ohm:
  contact_resistivity_ohm_cm2:
  thermal_boundary_resistance_m2K_W:
problem_codes: []
verification:
provenance:
notes:
```