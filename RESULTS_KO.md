# 대한민국 AlN/Si 계면 열분석 의뢰처 조사

> 후속 확장·정정: **RESULTS_NANOMETER_V2.md를 우선 읽으십시오.** 서울대 김태용·충남대 김윤영 등 추가 후보, KAIST FDTR 연구, 성균관대 sub-micron AlN FDTR 근거를 보강했다. KETI는 2023 TDTR 미보유 공식 답변이 추가 발견되어 우선순위를 낮췄다. 아래는 이전 조사 시점 기록을 보존한다.

조사일: 2026-10-02. 공개 기관·연구실·논문·장비 자료 기준. 실제 연락·예약·견적 요청은 하지 않았다. 전국을 대상으로 검색했지만 모든 연구실의 비공개 장비나 수탁 여부까지 조사 완료했다는 의미는 아니다.

## 결론

**하부 트랜스듀서가 없다는 이유만으로 AlN/Si 계면 TDTR 측정이 불가능한 것은 아니다.** 상부 Al/AlN/Si 구조로 진행한 선행 사례가 있다. 다만 사용자의 막 두께와 상부 금속 허용 여부가 아직 확인되지 않았으므로 현재 시료의 측정 성공을 보장할 수 없다.

우선 문의는 GIST 이종석 연구실·서울대 장혜진 연구실·IBS CINAP으로 진행할 가치가 있다. AlN 재료 적합성 및 FDTR 대안은 성균관대 조정완 MHeat 연구실, 상용 수탁은 NETZSCH 한국 창구를 병행한다. 3ω는 조선대 오동욱 및 KAIST 이봉재 연구실에 계면저항 분리 가능성을 먼저 문의한다. **현재 어느 기관도 이 정확한 시료의 외부 분석 수락까지 확인된 것은 아니다.**

## 요청 구조와 판단 기준

측정 예정 구조의 잠정안: 상부 Al / AlN / Si(100), 매몰 AlN/Si 계면과 Si 뒷면에 금속 없음. 상부 Al은 추가 공정의 검토안이며 이미 증착되었다고 확인된 상태가 아니다. 3ω는 별도 시료의 상부 패턴 히터. 상부 금속도 금지라면 아래 적합성 판단을 다시 해야 한다. 자연산화막 등 중간층이 있다면 측정된 유효 계면값을 원자적으로 깨끗한 AlN/Si 고유값으로 해석하지 않는다.

- TBC G의 단위는 W m⁻² K⁻¹. 면적 정규화 TBR R''=1/G의 단위는 m² K W⁻¹. 두 개의 독립 측정값이 아니다.
- TDTR 보유, 계면 역해석 역량, 외부 접수, 현재 시료 식별성은 별도 항목이다.
- 3ω의 유효 막/계면 저항을 AlN/Si 고유 계면저항으로 자동 해석하지 않는다.
- FDTR은 보조 대안이다. LFA·TPS·SThM·온도 영상은 TDTR/3ω 계면 분석 실적으로 대체하지 않는다.

## 우선 문의 후보

|기관·지역|공개 근거|연락처/경로|판정 및 미확인 사항|
|---|---|---|---|
|GIST 이종석, 광주|[상부 Al TDTR·계면 phonon 연구](https://phys.gist.ac.kr/optogist/sub01_01_04.do), [장비](https://phys.gist.ac.kr/optogist/sub01_02_00.do)|jsl@gist.ac.kr / 062-715-2222|기술 협의 우선. 외부 수탁·AlN/Si G 분리 미확인|
|서울대 장혜진, 서울|TDTR 연구 실적은 01_capital.md; [공식 교수 연락처](https://mse.snu.ac.kr/jang-hyejin/)|hjang@snu.ac.kr / 02-880-7096|계면 열수송 협업 후보. 외부 유료 분석·현재 시료 수락 미확인|
|IBS CINAP, 수원|[TDTR 장비 및 예약](https://centers.ibs.re.kr/_prog/equipments/index.php?GotoPage=2&menu_dvs_cd=050105&mng_no=1356&mode=V&site_dvs_cd=cinap_en)|장비 페이지 Kyung-Hun Ko / dmdhdhdn@naver.com / 010-5334-8658|기관 공개 담당 연락처. 현재 담당자·외부 자격·G 모델 확인 필요|
|성균관대 조정완 MHeat, 수원|[2026년 sputtered AlN FDTR 발표](https://mheat.skku.edu/), [연락처](https://mechskku.wixsite.com/mheat/people)|jungwan.cho@skku.edu|AlN 재료 직접 관련성 높음. 확인된 AlN 발표는 FDTR이며 TDTR 의뢰 수락과 별개|
|KIMM 한국기계연구원, 대전|DEPS 시간영역 열반사 Transometer 목록; 상세는 03_public.md|042-868-7880|장비/부서 연결 문의용. 외부 이용·담당자·현 가동상태 미확인|
|NETZSCH 한국, 경기|[계약 TDTR·interfacial resistance 및 한국 분석실](https://analyzing-testing.netzsch.com/en-US/services/contract-testing)|[한국 법인](https://analyzing-testing.netzsch.com/ko/meta-nav/imprint): nks@NETZSCH.com / +82 31 931 2300|글로벌 수탁 확인. 한국 직접 수행인지 해외 이관인지 확인 필요. 서비스 페이지 고양/법인 페이지 파주 표기 차이 있음|
|KETI 신뢰성연구센터, 성남|[Si 위 ≤1 µm 유전체 TDTR 문의 답변](https://www.keti.re.kr/reliability/sub/qna.php?at=view&idx=147304)|이규석 031-789-7293 / gslee@keti.re.kr|유사 문의 검토 창구 확인만 됨. 장비·분석 수행을 확인한 자료는 아님|
|조선대 오동욱, 광주|[열전달 연구실](https://sites.google.com/site/chosunheat/); 3ω 계면/접촉저항 논문 검토는 07_3omega.md|dwoh@chosun.ac.kr / 062-230-7944|3ω 방법 협의 후보. PDMS 접촉저항 실적을 AlN/Si 매몰계면 실적으로 오인하지 않음|
|KAIST 이봉재 TRAD, 대전|[3ω 및 박막 열측정 연구](https://trad.kaist.ac.kr/topics/polariton-mediated-thermal-conductivity-enhancement/)|bongjae.lee@kaist.ac.kr / 042-350-3239|확인 주제는 주로 면방향 열수송. 수직 계면 G·외부 수탁 미확인|

## 보조 후보와 제외/보류

|후보|확인된 범위|보류 이유|
|---|---|---|
|KRISS 대전|[TF-LFA 외부 의뢰 장비](https://deps.dips.or.kr/eps/equipMgr/view/6272), NFEC-2015-04-200924 / 042-868-5538|외부 분석 경로는 있으나 TDTR/3ω 및 계면 G 분리는 미확인|
|KBSI|2020년 공식 자료의 3ω 기술 개발; 03_public.md|현재 장비·수탁 확인 필요. 온도 영상 장비와 혼동 금지|
|POSTECH 안지환|[YSZ TDTR/FDTR 공동연구](https://ceramics.onlinelibrary.wiley.com/doi/10.1111/jace.19186), jihwanan@postech.ac.kr|공동저자 소속이 곧 장비 소재지는 아님|
|KAIST 강준상|2026 AB-SSTR 연구; 02_regional.md|TDTR 또는 AlN/Si TBC 의뢰 역량으로 확정하지 않음|
|부산대 양호순|역사적 박막 열측정 논문|해외 TDTR 시설 지원 사례여서 부산대 현 장비 증거로 사용하지 않음|
|LINSEIS/NI 서울|[국내 계약 열분석 안내](https://www.linseis.com/en/service-lab/material-testing-lab-south-korea/)|한국 메뉴 THB는 TDTR/3ω 매몰계면 분석 증거가 아님|
|Roientec|TDTR 제품 판매 자료; 04_commercial.md|판매와 시료 분석 수탁은 다름|

그 밖에 수도권·지역 대학과 KIST/KIMS/ETRI/KRICT/KERI/NNFC/KANC 등은 각 조사 파일의 확인 범위와 미확인 사유를 보존했다. 검색으로 근거를 찾지 못한 기관을 ‘불가능’으로 판정하지 않았다. 가격·납기·샘플 최소수량은 전부 견적 필요이며 임의 추정하지 않았다.

## 하부 금속 없는 구조의 문헌 근거

Nieminen et al., *Thermal Boundary Conductance of Direct Bonded Aluminum Nitride to Silicon Interfaces*, ACS Applied Electronic Materials (2024), [DOI 10.1021/acsaelm.4c00068](https://doi.org/10.1021/acsaelm.4c00068). Group II는 상부 Al/AlN/Si deposition interface 구조를 분석했다. 해당 시편은 접합 웨이퍼의 반대쪽 Si 제거 전처리를 거쳤으므로 사용자의 원래 시료와 동일한 제조 이력이라고 말할 수 없다. 자세한 검증 메모는 06_tdtr_physics.md. 이 문헌은 한국 수탁처 증거가 아니라 측정 구조의 가능성 근거다.

## 측정 의뢰 전 반드시 필요한 결정

1. 상부 Al 증착 또는 상부 3ω 히터는 허용되는가?
2. AlN 두께/오차, Si 두께, 거칠기, 시료 크기, 측정 온도를 확인한다.
3. AlN κ와 Al/AlN G 및 AlN/Si G의 민감도·상관성을 사전 검토한다.
4. 기관이 독립 G를 산출하지 못하면 유효 저항·범위만 가능한지 구분한다.
5. 필요한 비교 시료·막 두께 시리즈·히터/트랜스듀서 공정, 비용을 합의한 뒤 시료를 만든다.

현재 권고: **Al–Al 접합을 필수 선행 공정으로 확정하기 전에, 기존 AlN/Si에 상부 트랜스듀서를 추가하는 방식의 사전 타당성 검토부터 요청한다.** 기존 장비 담당자의 요구는 해당 장비/해석 절차의 조건일 수 있으므로 다른 기관의 검증된 방식과 비교한다.

문의 초안은 INQUIRY_DRAFT_KO.md. 실제 연락은 하지 않았다. 기관 회신이 있어야 ‘이 시료 분석 가능 확정’으로 상태를 올릴 수 있다.
