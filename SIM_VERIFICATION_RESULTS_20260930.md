# AlN 시뮬레이션·문헌 대조 및 결과 수집

감사일: 2026-09-30, Asia/Seoul. 범위: Antigravity의 SH.Kim AlN 계산 이력, Aside의 AlN hybrid-bonding 대화 및 로컬 인계 자료, 현재 PC2 FC3 큐와 선택한 벌크·박막 열수송 데이터. 다른 연구 폴더 전체나 모든 앱 대화에 대한 전수 감사는 아니다.

**현재 결과는 조건을 명시하면 설명·발표할 수 있지만, 최종 박막 물성 또는 전체 연구 검증 완료라고 발표할 수는 없다.** Exa는 근거 문헌을 찾는 수단이다. 문헌과 수치가 비슷하다는 사실과 원자료·수렴성·실험 검증은 별개다.

## 직접 검사한 결과

| 대상 | 이번 검사 | 판정 / 발표 범위 |
|---|---|---|
| FC3 3.20 Å 새 SCF 큐 | 220개 입력·출력 조회. 215개 종료·SCF 정확도·72개 유한 힘·phonopy 실제 QE parser 확인 | 215개 force 자료의 수치·파싱 검사 통과, 5개 미완료. FC3 최종 수렴 인증 아님 |
| 변위 YAML ↔ 실제 QE 입력 | 220개 전체의 원자 순서·셀·좌표 비교. QE native Bohr→Å 변환을 공식 calculator 단위로 적용 | 모두 일치. 셀 최대 오차 1.78e-15 Å, 좌표 4.86e-13 Å |
| 과거 HDF5 9개 | 9월 9일 감사 해시와 비교 | 9개 모두 동일. 파일 동일성이 물리적 정확성을 증명하지는 않음 |
| 현재 열전도도 HDF5 | 10개, 독립 SI 단위 재구성과 저장 모드 합계 대조 | 전부 통과. 기존 9개와 추가 온도 sweep 1개. IFC 수렴은 별도 |
| 온도 sweep | 100–800 K, 29개 온도에서 SI 재구성·CSV 일치 확인 | CSV–HDF5 최대 차이 4.89e-5 W/(m·K), 출력 반올림 범위 |
| 두께 모델 | 저장 모드에서 수명·Λz·억제함수를 다시 계산 | 원 CSV 최대 차이 3.83e-4 W/(m·K). 조건부 reservoir RTA 근사이며 MC·full film LBTE·실측 시료 예측이 아님 |
| 144원자 slab 완료본 | 최종 144개 힘과 입력 고정 원자 mask, 전자·이온 종료 조건 검사 | 움직이는 성분 최대 4.956e-5 < 1e-4 Ry/Bohr. 수치상 이완 완료. 마지막 SCF 힘 보정 경고 때문에 tighter-SCF 확인 권장 |
| 과거 archive의 144원자 출력 | 별도 원본 조회 | BFGS 종료·최종 좌표 없음. 완료본 대신 사용 금지 |
| 180원자 slab | 지정 입력과 대응 출력 조회 | 입력만 확인, 해당 output 없음. 완료 계산으로 분류하지 않음 |
| AlN/Si DMM 표 | 투과율 범위·공식·G↔R 역수·PDOS 합계 검사 | 표 내부 기본 산술은 일치. binned isotropic spectrum 재적분은 원 G와 최대 0.304% 차이. 실제 계면 검증은 미완료 |
| 과거 Gate C 요약 | 34개 행에 supercell-00876 중복 | 33개 고유 job. 이중 집계 제거. 마지막 job 종료는 9월 27일로, 9월 24–26 완료 범위에 포함하면 안 됨 |
| 과거 NEMD/PMC/second-sound 그림 | 생성 코드와 9월 9일 감사 기록 대조 | 실제 NEMD/MC/second-sound 증거에서 제외 |

원자료는 수정·이동하지 않았다. 날짜는 QE termination / phono3py 종료 로그에서 가져왔으며 복사일·mtime으로 대체하지 않았다. 원 완료일을 확인하지 못한 기존 IFC 기반 두께 자료는 `completion_date_unverified`에 남겼다.

### 144원자 판정 정정

QE 공식 `forc_conv_thr`는 각 힘 성분 기준이다. `Total force=0.000253`을 `1e-4`와 직접 비교해 실패로 판정하는 방식은 맞지 않는다. 고정 원자에는 큰 잔여 힘이 존재할 수 있으며, 이 계산은 움직이는 성분이 기준을 충족했다. 최종 Gradient error도 약 5e-5 Ry/Bohr다. 다만 마지막 SCF correction 약 4.1e-5와 경고가 남아 있어 최종 좌표에서 `conv_thr`를 더 엄격히 한 force single-point, 필요시 짧은 continuation relax가 다음 순서다. 이 감사는 새 전자구조 계산을 시작하지 않았다.

## Exa 원문 대조: 설명 가능한 것과 제한

| 연구 주장 | 확인한 1차 자료 | 이번 해석 |
|---|---|---|
| DFT→IFC2/IFC3→RTA/LBTE 방법은 타당한가 | [Phonon Olympics, JAP 138, 135108 (2025)](https://doi.org/10.1063/5.0289819), [원문](https://www.osti.gov/servlets/purl/3002310) | 방법 자체는 타당. 초격자·절단거리·변위·대칭·q-grid를 따로 검증해야 함 |
| 현재 κ≈250.40(xx), 228.31(zz)가 문헌상 설명 가능한가 | 위 원문 PDF p.18, Table XIII 직접 렌더 확인 | phono3py RTA 253/232와 가까운 잠정값. 다른 코드 결과나 실험값과 동일한 검증 수준을 의미하지 않음 |
| 316 W/mK는 모든 DFT 결과의 목표인가 | 위 Table XIII 및 로컬 PREREG §4.1.2 | 표의 316은 실험 cross-plane 값. 현재 PREREG는 κavg=(2κxx+κzz)/3의 316±15%를 동결 기준으로 둠. 방향·시료·solver 비교의 차이를 설명해야 하며 기준은 변경하지 않음 |
| 두께 감소에 따른 열수송 억제 | [Vermeersch et al., APL (2016)](https://doi.org/10.1063/1.4948968) | 명시한 reservoir RTA 모델의 조건부 계산으로 설명 가능. 실제 결함·입계·계면 보정은 아직 없음 |
| 실제 MC 계산을 수행했는가 | [Nano-κ 원 논문](https://doi.org/10.1016/j.cpc.2023.108954), [개발자 코드](https://github.com/brunohs1993/Nanokappa) | 현재 경험식 그림은 Nano-κ 실행 증거가 아님. 입자·시간·geometry·convergence 기록이 필요 |
| GaN/AlN/diamond는 새로운 무선행 분야인가 | [Deng et al., SST 41, 045013 (2026)](https://doi.org/10.1088/1361-6641/ae5ccc) | Aside에서 미검증이던 논문 제목·DOI·서지 확인. AlN interlayer의 top-side 연구가 이미 존재하므로 단순 구조 재현만으로 신규성 주장 불가 |
| AlN/diamond NEMD 자체가 새로운가 | [Qi et al., Applied Surface Science 615, 156419 (2023)](https://doi.org/10.1016/j.apsusc.2023.156419), [저자 원문](https://cronfa.swan.ac.uk/Record/cronfa62330/Download/62330__26297__b74a009da7f64c4b882a714dd56aceea.pdf) | 계면 nanostructure NEMD가 이미 존재. bonding strength·공정 손상·신뢰성과 연결되는 별도 질문을 먼저 검증해야 함 |
| AlN interlayer가 항상 유리한가 | [Low Thermal Boundary Resistance Interfaces for GaN-on-Diamond Devices (2018)](https://doi.org/10.1021/acsami.8b07014) | 성장 손상과 보호층 조건이 결과를 바꿀 수 있음. 최저 TBR 한 값만 이식하면 안 됨 |
| BSPDN AlN vs oxide 비교가 새 주제인가 | [IEEE ECTC 2025 record 11038190](https://ieeexplore.ieee.org/document/11038190), [공저자 ORCID](https://orcid.org/0000-0002-2047-2406) | 제목·저자 등록·학회 확인. IEEE 직접 fetch는 미확보하여 DOI·세부 조건은 확인 대기. 단순 비교의 신규성 확정은 보류 |

Table XIII의 실제 방향별 RTA 값은 ALAMODE 282/263, phono3py 253/232, ShengBTE 271/251 W/(m·K)이다. 검색 본문에 나온 방향별 범위와 표가 일치하지 않는 부분이 있어 원문 표를 우선했다. 실험 316을 phono3py RTA 목표값으로 오인하지 않는다. 방법 차이는 Table XII: harmonic/cubic 원자수 192/192, 300/72, DFPT/300 및 각기 다른 neighbor cutoff와 q-grid이다.

현재 κavg≈243.04 W/(m·K)는 동결된 316±15% 기준 하한 268.6보다 낮다. 즉 **저장 배열의 산술 검사는 PASS, 현재 PREREG bulk 벤치마크는 미충족**이다. 수치를 맞추기 위한 보정이나 임계값 변경은 하지 않았다.

## 추가로 필요한 계산

실행 순서와 입력·검증 게이트는 `additional_simulations.csv`에 정리했다. A는 현재 결과를 과학적으로 사용할 때 필요한 계산, B는 Aside/HBM 핵심 연구의 추가 계산, C는 선택적 확장이다.

1. **A — 현재 batch 이후:** 재사용 98개 원본 force provenance를 확보하고 318개 변위의 순서·설정·pseudo hash·ASR/drift를 검증한 뒤 3.20 Å IFC를 재구성한다. 220개 새 계산의 완료는 이 단계의 대체 증거가 아니다.
2. **A — FC3 cutoff/supercell:** 같은 기준으로 3.20→4.0→5.0 Å, 필요시 no-cutoff를 단계적으로 비교한다. 수렴하면 다음 불필요한 단계를 생략한다. FC2와 FC3 초격자, q-grid, MFP tail, NAC 및 RTA/LBTE를 따로 시험한다. 새 grid는 c축 even n3를 포함해 비교한다.
3. **A — slab:** tighter-SCF 힘, cutoff·k-grid·진공·두께·극성 termination/dipole 검사. 이후 matched clean parent·N/N2 references·흡착 site가 있어야 adsorption energy와 NEB를 계산할 수 있다. historical nonpolar branch는 현 AlN_Simulation 지침상 유보되어 필수 큐에 넣지 않는다.
4. **B — Aside S4.2:** HH-A/HH-B 극성반전·산화 계면 DFT, pseudo-H(Z=0.75) 또는 대칭종결 검증, 후보구조 이완·전자구조·에너지. #6 서사 선택과 실제 계면 확인이 먼저다.
5. **B — S4.3/MD:** 승인된 계면을 위한 MLIP/DFT dataset과 동결된 held-out 계열 평가, 실제 bonded interface NEMD/Green–Kubo. 문헌 vdW AlN/Cu를 실제 Cu hybrid-bonding 계면 대신 사용하지 않는다. 정상 열유속·에너지 보존·길이·시간·seed 수렴과 반복 오차가 필요하다.
6. **B — MC:** Nano-κ의 Si/Ge 기준 문제부터 검증한 후 AlN 및 다층 geometry로 확장. DFT/MD 중첩 길이에서 대조하고 packet 수·시간·에너지 보존·수렴을 검사한다. Cu 전자 열수송을 phonon-only MC로 대체하지 않는다.
7. **B — blind nano-κ 및 소자 map:** 실험 비교 전에 예측을 등록하고, FEM 공간·시간 수렴·열수지·계면 sensitivity와 RC/crosstalk 비용을 같이 검사한다. 실측 TDTR/3ω가 없으면 실험 검증 완료로 선언하지 않는다.
8. **C — GaN/diamond·BSPDN:** 문헌·특허 대비 구체적 차별 질문을 먼저 확정. simple AlN/oxide 비교나 기존 nanopillar TBR 최적화를 무조건 추가하지 않는다. 조건부 공정손상/접착/열-기계 신뢰성 공동 검증 또는 다른 geometry의 regime-map 검증으로 제한한다.

## 완료 시점

현재 batch 관측 기준(14:57 KST): 215/220, 최근 10개 평균 1.9567 h/job. 남은 5개 전체 시간을 포함한 단순 계산은 **9월 30일 22:37–10월 1일 01:47**, 평균 **10월 1일 00:44 KST**다. 이미 진행 중인 job의 경과시간을 빼지 않은 보수적 처리이며 신뢰구간·보장 시간이 아니다. 중단·재검사·재계산은 포함하지 않았다.

**모든 추가 연구를 포함한 최종 완료일은 지금 확정할 수 없다.** 192원자/계면/MD/MC의 실제 처리시간과 승인 구조, 실험 자료가 없기 때문이다. `schedule_scenarios.csv`는 다음의 계산량을 설명하는 조건부 계획이다.

- 72원자에서 318개를 모두 재사용 가능하다고 가정하면 4.0 Å의 총 466개까지 **추가 148개**다. 현재 CPU 처리속도면 순수 force 계산만 평균 약 **12.1일**, 관측 min/max 속도 적용 시 9.5–13.4일이다.
- 5.0 Å 총 790개까지는 추가 누적 472개, 평균 **38.5일**이다.
- 72원자 no-cutoff 총 1254개까지는 추가 누적 936개, 평균 **76.3일**이다. 10월 1일 시작 가정 시 12월 중순에 해당한다. 이것도 192원자 초격자·계면·MD·MC·실험을 포함한 전체 완료일은 아니다.
- 재사용 98개 provenance가 통과하지 못하거나 변위 집합이 대응하지 않으면 계산 수가 증가한다. displacement-count 문서와 실제 새 입력에서 중첩 구조를 확인하기 전에는 위 차감 계산을 실제 큐로 실행하지 않는다.
- Dual GPU는 현재 idle이지만 CPU 대비 force 동등성과 실제 job throughput을 검증하기 전에는 2배 속도를 가정하지 않는다. 과거의 43시간 예상은 현재 관측 CPU 속도에 적용할 수 없다.

## 결과 폴더와 자동화

`results/실제완료일/연구항목/`에 PNG와 CSV를 함께 모았다. 각 그림에 잠정 IFC·조건부 모델·SCF 경고 등 필요한 제한을 붙였다. `manifest.json`은 파일·원자료 해시 및 날짜 근거를 기록한다. DMM 원자료 linkage·mesh/bin 민감도와 실제 계면 검증이 해결되지 않아 해당 그림은 검증 완료 폴더에 넣지 않았다. 실패·합성 그림도 제외했다.

가장 빠른 자동화 개선은 기존 CPU 큐를 중복 실행하지 않고 완료 이벤트에서 이 감사 스크립트를 한 번 실행하는 것이다. 현재 CPU supervisor는 batch 완료시 종료하며, 문서의 “자동 BTE 연결” 설명만으로 실제 후처리 trigger가 있다고 판단하지 않았다. force provenance gate PASS 후 IFC→BTE→CSV→PNG→manifest로 연결해야 한다. 새 결과가 없을 때 모델 호출을 하지 않는다.

이번 채팅에 `AlN FC3 완료 후 검증·결과 수집` 자동화(id: `aln-fc3`)를 ACTIVE로 등록했다. 매시간 간단한 상태만 확인하며 정상 미완료 상태에서는 보고와 전체 검사를 생략한다. 220개 종료 후 세 감사 스크립트를 실행해 결과를 같은 폴더에 갱신하고 FINAL_FC3_COMPLETION.md로 완료·미검증 항목을 한 번 알린 뒤 자동화를 일시 중지하도록 설정했다. 아직 미래 실행 성공이 확인된 것은 아니며 PC2 및 앱의 실행 가능 상태가 필요하다. 새 계산을 자동 시작하는 설정은 아니다.

JEV는 TypeSafe 공식 API 문서와 인증 경로를 다시 확인했지만 Process/User/Machine 환경의 JEV_API_KEY·TYPESAFE_API_KEY가 없어 **이번 작업에 실제 적용되지 않았다**. 키 값은 출력하지 않았다. JEV를 연결하면 연구판단 routing을 묶어서 실행할 수 있으나 물리 검증 gate는 유지한다. 현재 세션 모델/추론 설정을 직접 바꾸지는 않았다.

재실행 명령: `wsl.exe -d Ubuntu-22.04 -u aol python3 /mnt/c/Users/AOL/Desktop/SH.Kim/Simulation_Verification_2026-09-30/audit_and_collect.py`

절약 프롬프트: “기존 감사 해시와 완료 ledger를 재사용하고 새로 종료한 job만 검증하라. 물리 수렴 gate와 문헌·실측 비교를 분리하고, 통과한 PNG/CSV만 실제 완료일 폴더에 수집하라. JEV 연결상태와 변경된 ETA·차단 사유만 보고하라.”
