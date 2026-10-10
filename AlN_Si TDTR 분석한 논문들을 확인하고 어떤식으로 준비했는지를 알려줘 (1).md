<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# AlN/Si TDTR 분석한 논문들을 확인하고 어떤식으로 준비했는지를 알려줘

AlN/Si 계열에서 TDTR로 분석한 논문들은 공통적으로 **AlN 막 위에 Al transducer를 올리고, 변조 주파수·레이저 spot size·시편 두께를 조절해 열전도도와 계면 열전달(TBC)을 피팅**하는 방식으로 준비했습니다. 특히 AlN/Si 직접 접합이나 AlN/Si 이종구조에서는 **표면 산화·오염 제거, transducer 두께 측정, 얇은 막/계면 구조의 정확한 두께 규명**이 핵심이었습니다.[^1_1][^1_2]

## 어떤 논문들이 있었나

- **Direct bonded AlN-to-Si(SOI) 인터페이스**를 TDTR로 분석한 연구에서는 AlN-SOI의 열전도도와 Si/AlN 계면 TBC를 측정했습니다.[^1_2][^1_1]
- **AlN on Si(100)** 쪽에서는 AlN 성장 품질을 개선한 뒤, 구조/전기적 특성을 함께 본 논문이 있고, TDTR 자체보다는 성장·구조 분석 중심이지만 AlN/Si 준비법을 이해하는 데 참고가 됩니다.[^1_3]
- **AlN 관련 TDTR 표준 준비법**은 AlN crystal 또는 epitaxial AlN에서 80 nm 정도의 Al transducer를 증착하고, 보통 10 MHz 근처 변조 주파수와 수 μm 급 pump/probe spot으로 측정한 사례가 많습니다.[^1_4][^1_5]


## 준비는 어떻게 했나

- **기판 세정과 표면 활성화**: solvent clean, RCA clean, RIE/SF₆-O₂ 또는 Ar 플라즈마 등으로 표면을 정리한 뒤 접합 또는 transducer 증착을 진행했습니다.[^1_1]
- **Al transducer 증착**: TDTR용으로 대개 **약 80 nm Al**을 e-beam evaporation 또는 RF sputtering으로 증착했습니다.[^1_5][^1_4][^1_1]
- **두께 검증**: Al transducer 두께는 **picosecond acoustic echo**, AlN 두께는 **spectroscopic ellipsometry**, 계면 두께나 손상층은 **TEM/ICP etch** 등으로 확인했습니다.[^1_1]
- **측정 조건 설정**: 두 색(two-color) TDTR, 400 nm pump / 800 nm probe, 76 MHz 펨토초 레이저, 1/e² spot size 수십 μm 수준, modulation frequency는 보통 2 MHz 또는 10 MHz 근방을 사용했습니다.[^1_4][^1_5][^1_1]


## 실험 설계 포인트

- **민감도 높은 구조로 만들기** 위해 AlN 두께, 계면 상태, 기판 두께를 잘 알아야 합니다. 얇은 계면층이나 buried interface를 보려면 주파수를 바꾸거나, 경우에 따라 dual-frequency/PWA 같은 확장 TDTR이 유리합니다.[^1_6][^1_7]
- **AlN/Si에서는 계면 자체가 병목**이라서, 단순히 AlN 벌크 열전도도만이 아니라 **Si/AlN TBC**를 함께 피팅하는 모델이 중요합니다.[^1_2][^1_1]
- 성장 기반 샘플이라면 **산소 함량, 표면 거칠기, 미세균열/보이드, 접합 전 플라즈마 처리**가 결과를 크게 좌우합니다.[^1_8][^1_1]


## 네 연구에 바로 연결하면

네가 AlN/Si TDTR를 준비한다면, 보통 아래 순서가 가장 실용적입니다.

1. **AlN 두께와 결정성 먼저 확보**.
2. **표면 세정 후 70–100 nm Al transducer 증착**.
3. **transducer 두께를 acoustic echo로 확인**.
4. **변조 주파수 스윕으로 sensitivity 확인**.
5. **AlN κ와 Si/AlN TBC를 동시에 피팅**.[^1_5][^1_1]

원하면 다음 단계로,

- **AlN/Si TDTR 논문만 추려서 표로 정리**하거나,
- **네 실험 조건에 맞는 TDTR 샘플 준비 체크리스트**를 바로 만들어줄게.
<span style="display:none">[^1_10][^1_11][^1_12][^1_13][^1_14][^1_15][^1_9]</span>

<div align="center">⁂</div>

[^1_1]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11044587/

[^1_2]: https://pubs.acs.org/doi/10.1021/acsaelm.4c00068

[^1_3]: https://tdr.lib.ntu.edu.tw/handle/123456789/95451?mode=full

[^1_4]: https://pubs.aip.org/aip/jap/article-pdf/doi/10.1063/5.0245381/20429173/095105_1_5.0245381.pdf

[^1_5]: https://poplab.stanford.edu/pdfs/Xu-AlNthermalCondDefectsSizeEffects-jap19.pdf

[^1_6]: https://dr.ntu.edu.sg/handle/10356/166521

[^1_7]: https://www.themoonlight.io/ko/review/thermal-characterization-of-buried-interfaces-in-multilayer-heterostructures-via-tdtr-with-periodic-waveform-analysis

[^1_8]: https://escholarship.org/content/qt5ws9g0gt/qt5ws9g0gt_noSplash_a3ce0644983c032bec3147e49e6d5003.pdf

[^1_9]: https://pubs.acs.org/doi/abs/10.1021/acsami.4c07327

[^1_10]: https://pubmed.ncbi.nlm.nih.gov/34797056/

[^1_11]: https://www.sciencedirect.com/science/article/pii/S2542529322003467

[^1_12]: https://patrickehopkins.com/wp-content/uploads/2021/08/hoque2021ab.pdf

[^1_13]: https://adma.ustb.edu.cn/en/docs/2020-10/b644cc1fc9e14cce98b3f420c1b0d6ea.pdf

[^1_14]: https://nanoheat.stanford.edu/wp-content/uploads/2012/09/ITHERM_2012_EBG_Final.pdf

[^1_15]: https://poplab.stanford.edu/pdfs/Vaziri-AlNthermalMaterial3DICs-afm25.pdf


---

# RF모드를 했어 FF모드를 했어?

그리고 Mo를 Transducer로 사용하는 경우는...?
Al을 Transducer로 사용했을 때 열확산도 등의 값들은 어떻게 반영했는지도 확인이 필요해
TDTR 경우만 조사해줘 FDTR은 진행 못해

TDTR 기준으로 보면, **대부분은 RF가 아니라 FF처럼 생각되는 “금속 transducer 증착 방식” 자체보다, transducer 재료가 무엇인지가 더 중요**합니다. 문헌상 AlN/Si 계열 TDTR는 **Al transducer를 가장 흔하게 쓰고**, AlN 위에 약 80 nm 정도로 올린 뒤 AlN의 열전도도와 Al/AlN 계면 TBC를 같이 피팅하는 방식이 대표적입니다.[^2_1][^2_2][^2_3]

## RF모드 vs FF모드

- 지금 질문 맥락이 **RF sputtering으로 transducer를 올렸는지, 혹은 e-beam/thermal evaporation 같은 다른 방식인지**를 묻는 거라면, TDTR 문헌에서 가장 흔한 건 **Al transducer 증착**이고 증착 방식은 논문마다 다릅니다. AlN 샘플에서는 Al transducer를 사용한 예가 매우 많고, 그때 두께와 열물성은 함께 모델에 넣습니다.[^2_2][^2_3][^2_1]
- 즉, **TDTR 결과 해석에서 핵심은 RF/FF 자체보다 “transducer의 실제 두께, κ, ρcp, 계면 TBC”를 어떻게 넣었는지**입니다.[^2_3][^2_2]


## Mo를 transducer로 쓰는 경우

- **Mo transducer는 TDTR에서 가능하지만 Al보다 훨씬 덜 흔합니다.** 보통 Al은 반사율이 좋고 열적/광학적 모델이 잘 정리돼 있어 표준처럼 많이 씁니다.[^2_2][^2_3]
- Mo를 쓰면 **광학 상수, 열전도도, 비열, 두께, 산화층**까지 더 신경 써야 해서 fitting 난이도가 올라갑니다. 그래서 AlN/Si 문헌의 주류는 여전히 Al transducer입니다.[^2_1][^2_2]


## Al transducer를 쓸 때 어떻게 반영하나

- TDTR fitting에서는 Al transducer를 **단순히 “보호막”처럼 두지 않고, 별도 층으로 넣어** \$ \kappa_{Al} \$, \$ \rho c_p \$, 두께, 그리고 **Al/AlN 계면 TBC**를 모델에 반영합니다.[^2_3][^2_2]
- 실제로 한 AlN TDTR 연구에서는 **Al transducer의 열전도도는 companion SiO2 sample로 먼저 보정**했고, 그 값이 \$ \kappa_{Al} \approx 151.2 \pm 25.0 \,\mathrm{W\,m^{-1}\,K^{-1}} \$로 보고됐습니다. 같은 연구에서 AlN의 cross-plane 열전도도와 Al/AlN TBC를 동시에 추출했습니다.[^2_3]
- 또 다른 AlN bulk 연구에서는 **Al transducer 두께 오차와 laser spot size 오차가 결과 불확도에 직접 반영**된다고 명시했고, \$ \kappa_{AlN} \$과 \$ G_{Al/AlN} \$를 simultaneous fit 했습니다.[^2_2]


## 네가 확인해야 할 포인트

- **RF/FF가 무엇을 뜻하는지** 먼저 정리해야 합니다. 만약 네가 말한 RF가 **RF sputtering**, FF가 **film furnace/evaporation류**를 뜻하는 거라면, TDTR에서는 “어떤 증착법으로 transducer를 만들었는지”보다 **실제 transducer 물성 입력값이 무엇인지**가 더 중요합니다.
- TDTR만 보면, **Mo transducer 사례는 소수**, **Al transducer는 표준**이고, Al을 썼을 때는 문헌처럼 **companion sample로 κAl를 보정한 뒤 fitting에 넣는 방식**이 가장 안전합니다.[^2_2][^2_3]

원하면 다음 답변에서 바로

1) **AlN/Si TDTR 논문 중 transducer가 Al인지 Mo인지 표로 정리**하고,
2) **fitting 파라미터(κ, ρcp, thickness, G)의 입력값을 논문별로 비교**해줄게.
<span style="display:none">[^2_10][^2_11][^2_12][^2_13][^2_14][^2_15][^2_4][^2_5][^2_6][^2_7][^2_8][^2_9]</span>

<div align="center">⁂</div>

[^2_1]: https://link.aps.org/accepted/10.1103/PhysRevMaterials.4.044602

[^2_2]: https://poplab.stanford.edu/pdfs/Xu-AlNthermalCondDefectsSizeEffects-jap19.pdf

[^2_3]: https://poplab.stanford.edu/pdfs/Perez-SputteredAlNhighThermalK-nano23.pdf

[^2_4]: https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId

[^2_5]: https://www.jstage.jst.go.jp/article/sfj/62/9/62_9_443/_pdf/-char/ja

[^2_6]: http://www.ysxbcn.com/down/upfile/soft/2008429/2008429105543486.pdf

[^2_7]: https://www.reseat.or.kr/portal/cmmn/file/fileDown.do?menuNo

[^2_8]: https://www.sciencedirect.com/science/article/pii/S129007291930403X

[^2_9]: https://link.springer.com/article/10.1007/s10854-019-01502-x

[^2_10]: https://analyzing-testing.netzsch.com/ko/jepum/time-domain-thermoreflectance-analyzer-tdtr

[^2_11]: https://www.mri.psu.edu/sites/default/files/stm/publications/Thermal Conductivity of Aluminum Scandium Nitride for 5G Mobile Applications and Beyond-ACSAppMatInt-2021.pdf

[^2_12]: https://patrickehopkins.com/wp-content/uploads/2016/08/2016-sthc_tdtrnometal.pdf

[^2_13]: https://pubmed.ncbi.nlm.nih.gov/34797056/

[^2_14]: https://pubs.aip.org/aip/jap/article-pdf/doi/10.1063/5.0245381/20429173/095105_1_5.0245381.pdf

[^2_15]: https://dr.ntu.edu.sg/handle/10356/166521


---

# 아래의 내용을 보고 내가 어떻게 준바해야할지 확인해줘

TDTR/NanoTR에서 사용하는 정확한 명칭은 다음과 같습니다.
RF mode = Rear Heating / Front Detection
한국어: 후면 가열 / 전면 검출
FF mode = Front Heating / Front Detection
한국어: 전면 가열 / 전면 검출
NETZSCH의 NanoTR 공식 설명도 이 명칭을 사용합니다. RF는 Ultrafast Laser Flash Method – Rear Heating/Front Detection, FF는 Time-Domain Thermoreflectance – Front Heating/Front Detection으로 구분됩니다. ([넷츠흐 분석 및 테스트](https://analyzing-testing.netzsch.com/en/products/time-domain-thermoreflectance-analyzer-tdtr/nanotr?utm_source=chatgpt.com))
여기서 Front와 Rear의 기준
기판 전체의 앞·뒷면을 막연하게 지칭하는 것이 아니라, 측정하려는 박막을 기준으로 합니다.
Front: 기판 위에 증착된 박막의 외부로 노출된 표면
Rear: 박막과 기판이 맞닿는 계면 쪽
NETZSCH 공식 설명에서도 front는 박막의 열린 표면, rear는 박막–기판 경계라고 정의합니다. ([넷츠흐 분석 및 테스트](https://analyzing-testing.netzsch.com/en/products/time-domain-thermoreflectance-analyzer-tdtr/nanotr?utm_source=chatgpt.com))
RF mode
Pump laser
↓ 투명 기판을 통과
Substrate
Rear side of film
Thin film
Front surface
↑ Probe laser / detection

펌프 레이저가 투명한 기판 측에서 입사하여 박막의 rear side를 가열하고, 반대쪽인 박막의 front surface에서 probe laser로 온도변화를 검출합니다. 펌프와 검출이 서로 반대쪽에 위치하는 laser-flash형 구성입니다. ([넷츠흐 분석 및 테스트](https://analyzing-testing.netzsch.com/en/products/time-domain-thermoreflectance-analyzer-tdtr/nanotr?utm_source=chatgpt.com))
FF mode
Pump laser + Probe laser
↓
Metal transducer / film front surface
Thin film
Substrate

펌프와 프로브가 모두 박막의 노출된 전면에 조사됩니다. 따라서 두 레이저와 검출기가 시료의 같은 측에 위치합니다. 불투명한 기판 위 박막에도 적용할 수 있습니다. ([넷츠흐 분석 및 테스트](https://analyzing-testing.netzsch.com/en/products/time-domain-thermoreflectance-analyzer-tdtr/nanotr?utm_source=chatgpt.com))
논문과 발표자료에 사용할 권장 표기
RF configuration:
Rear Heating / Front Detection

FF configuration:
Front Heating / Front Detection

한국어로는:
RF 구성: 후면 가열–전면 검출
FF 구성: 전면 가열–전면 검출

이라고 쓰면 됩니다.
주의할 점은 RF가 Radio Frequency를 의미하지 않는다는 것입니다. 이 장비 문맥에서는 Rear Heating / Front Detection입니다. 또한 일부 웹페이지의 소제목에 “Rear Heating/Front Heating”이라는 오기가 보이지만, 본문과 장비 공식 명칭은 일관되게 Rear Heating/Front Detection을 사용합니다. ([넷츠흐 분석 및 테스트](https://analyzing-testing.netzsch.com/de/application-literature/thermal-diffusivity-measurements-on-pedot-pss-thin-film-by-means-of-nanotr?utm_source=chatgpt.com))
현재 시료구조에 적용하면:
Mo/AlN/Si 상부에서 펌프·프로브 조사 → FF
투명한 기판 쪽에서 펌프를 조사하고 반대편 표면에서 검출 → RF
로 구분합니다.

정리해보면, **당신이 적어준 RF/FF 정의와 front/rear 기준은 NETZSCH 공식 설명과 일치**합니다. RF = rear heating/front detection, FF = front heating/front detection이고, “front”는 박막의 외부 노출 표면, “rear”는 박막-기판 경계로 쓰는 게 맞습니다.[^3_1][^3_2]

## 내가 어떻게 준비하면 되는가

- **Mo/AlN/Si 구조에서 상부 Mo를 transducer로 쓰는 경우는 FF**로 보는 것이 맞습니다. 펌프와 프로브가 모두 박막의 노출된 전면에 가니까, 같은 면에서 가열·검출하는 구성입니다.[^3_2][^3_3]
- **투명 기판을 통해 반대면을 가열하는 구성**만 RF입니다. 즉, Mo/AlN/Si처럼 불투명 기판 위에 상부 금속 transducer를 두는 일반적인 TDTR는 RF가 아니라 FF 쪽입니다.[^3_3][^3_2]
- **Al transducer를 쓰는 경우도 동일하게 FF**로 준비하면 됩니다. Al은 가장 표준적인 transducer이고, 두께는 보통 80–100 nm 수준으로 잡고, 별도 reference sample로 Al의 열물성을 보정합니다.[^3_4][^3_3]


## Al transducer 값은 어떻게 반영하나

- TDTR fitting에서는 Al transducer를 **모델의 한 층**으로 넣고, **열전도도 \$ \kappa_{Al} \$, 체적비열 \$ \rho c_p \$, 두께, 계면 열저항**을 반영합니다.[^3_5][^3_4]
- 문헌에서는 **companion sample로 Al의 \$ \kappa \$** 를 보정하거나, 이미 검증된 문헌값을 쓰되 **spot size와 thickness uncertainty까지 sensitivity analysis**에 포함합니다.[^3_4][^3_5]
- 그래서 네가 준비할 때는 단순히 “Al을 올렸다”가 아니라, **Al 두께 측정, Al 산화 여부, reference sample 유무, fitting에서 고정/자유 파라미터를 어떻게 둘지**를 같이 설계해야 합니다.[^3_3][^3_4]


## Mo transducer를 쓸 때

- Mo도 TDTR transducer로 가능하지만, 실무상 **Al보다 드물고 광학상수/열물성 입력이 더 까다롭습니다**.[^3_3]
- 따라서 네가 AlN/Si TDTR를 논문 수준으로 준비한다면, 특별한 이유가 없으면 **Al transducer + FF 구성**이 가장 문헌 친화적입니다.[^3_4][^3_3]


## 결론

- 네가 적어준 정의를 기준으로 하면 **Mo/AlN/Si 상부 조사 = FF**가 맞습니다.
- **RF는 투명 기판을 통한 rear heating 구성**이라, 현재 네가 말한 일반적인 AlN/Si 상부 금속 transducer TDTR와는 다릅니다.
- Al을 transducer로 쓸 때는 **Al의 κ, ρcp, thickness, 산화/계면 상태**를 모델에 반영하는 식으로 준비하면 됩니다.[^3_1][^3_2][^3_4]

원하면 다음 답변에서 바로
**“AlN/Si TDTR 실험 준비 체크리스트”** 형태로, 샘플 준비–증착–두께 측정–reference sample–fitting 파라미터까지 한 장짜리로 정리해줄게.
<span style="display:none">[^3_10][^3_11][^3_12][^3_13][^3_14][^3_15][^3_6][^3_7][^3_8][^3_9]</span>

<div align="center">⁂</div>

[^3_1]: https://analyzing-testing.netzsch.com/de/produkte/time-domain-thermoreflectance-analyzer-tdta/nanotr

[^3_2]: https://analyzing-testing.netzsch.com/en/products/time-domain-thermoreflectance-analyzer-tdtr/nanotr

[^3_3]: https://measurlabs.com/products/thermal-conductivity-of-thin-films-with-tdtr/

[^3_4]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11044587/

[^3_5]: https://cahill.matse.illinois.edu/software-and-data/

[^3_6]: https://escholarship.org/content/qt4xv079m1/qt4xv079m1.pdf

[^3_7]: https://arxiv.org/pdf/2112.08734.pdf

[^3_8]: https://repositories.lib.utexas.edu/server/api/core/bitstreams/510da89a-977f-4c9f-9762-db470efc997c/content

[^3_9]: https://analyzing-testing.netzsch.com/_Resources/Persistent/4/b/a/0/4ba07430dd66702c2f0e7aeb83ca919d6af14b5f/AN%20273_Thermal-Diffusivity-Measurements-on%20PEDOT_PSS-Thin%20Film-by-Means-of-NanoTR-English.pdf

[^3_10]: https://analyzing-testing.netzsch.com/ja/products/time-domain-thermoreflectance-analyzer-tdta/nanotr

[^3_11]: https://www.lihyuan.com.tw/attach/product__a_1__116.pdf

[^3_12]: https://www.pico-therm.com/english/product/index.html

[^3_13]: https://www.scribd.com/document/517816603/1-5046944

[^3_14]: https://netzsch.co.jp/product/nanotr-picotr/

[^3_15]: https://patrickehopkins.com/wp-content/uploads/2016/08/2016-sthc_tdtrnometal.pdf


---

# AlN/Si TDTR 실험 준비 체크리스트를 사전연구 논문들을 바탕으로 정리해줘

아래처럼 준비하면 됩니다. 핵심은 **AlN/Si TDTR는 “샘플 구조 정리 → transducer 준비 → 두께/물성 보정 → 민감도 확인 → fitting 전략 확정”** 순서로 가는 것입니다. 문헌상 AlN/Si 계열에서는 80 nm 내외 Al transducer, 표면 세정/플라즈마 처리, 두께 검증, reference sample 보정이 거의 공통적으로 등장합니다.[^4_1][^4_2][^4_3]

## 1) 샘플 준비

- **표면 거칠기 확인**: TDTR은 표면 거칠기가 크면 신호가 흔들리므로, 가능한 매끈한 표면이 필요합니다. 일반적으로 RMS roughness가 낮을수록 좋고, 거친 경우는 transducer가 잘 형성되는지 먼저 봐야 합니다.[^4_3][^4_4]
- **AlN/Si 계면 상태 확보**: 성장형 샘플이면 AlN/Si 계면 결함, 산화, 보이드가 결과를 크게 좌우합니다. 직접 접합 샘플은 solvent clean, RIE/SF6/O2, Ar plasma, RCA-1 같은 전처리 후 접합하는 방식이 문헌에 나옵니다.[^4_1]
- **측정 위치 정의**: TDTR는 보통 상부 금속 transducer가 있는 면에서 측정하므로, 네 구조에서는 대개 **FF 구성**으로 준비하는 것이 맞습니다.[^4_5][^4_6]


## 2) Transducer 준비

- **재료 선택**: Al이 가장 표준적입니다. 문헌에서 AlN TDTR는 대체로 **Al transducer**를 쓰며, Mo는 가능하지만 덜 일반적이고 optical/thermal input이 더 까다롭습니다.[^4_2][^4_7][^4_1]
- **두께 범위**: Al은 보통 **약 80 nm** 정도가 자주 쓰입니다. 너무 얇으면 광학 반사 신호가 약하고, 너무 두꺼우면 샘플 자체의 열응답이 묻힐 수 있습니다.[^4_2][^4_1]
- **증착 직전 전처리**: Ar plasma로 표면을 청소한 뒤 Al을 올리는 방식이 자주 쓰입니다. 접합형 구조에서는 이 단계가 계면 열저항에 큰 영향을 줍니다.[^4_1]


## 3) 보정해야 할 값

- **Al transducer 열전도도 \$ \kappa_{Al} \$**: 문헌에서는 companion sample(예: SiO2)로 먼저 보정하거나, 신뢰 가능한 문헌값을 사용합니다. 한 연구에서는 \$ \kappa_{Al} \approx 151.2 \pm 25.0 \,\mathrm{W\,m^{-1}\,K^{-1}} \$를 보정해서 썼습니다.[^4_7]
- **Al thickness**: picosecond acoustic echo로 확인하는 사례가 많습니다. 이 값 오차가 TDTR 피팅 오차에 직접 들어갑니다.[^4_1]
- **AlN thickness**: spectroscopic ellipsometry나 TEM으로 확인하는 경우가 많습니다. 두께가 정확해야 cross-plane κ와 TBC 분리가 됩니다.[^4_1]
- **계면층/접합층 두께**: TEM 등으로 계면 손상층이나 접합층을 따로 확인하면 좋습니다.[^4_1]


## 4) 측정 조건

- **주파수 선택**: 일반 TDTR은 대략 0.1–20 MHz 범위에서 사용됩니다. AlN/Si 같은 이종구조는 sensitivity가 잘 나오는 주파수를 골라야 합니다.[^4_8][^4_3][^4_2]
- **Spot size**: 대물렌즈로 pump/probe spot size를 정하고, 보통 수 μm에서 수십 μm 범위를 사용합니다. spot size가 너무 작으면 3D 효과가 커지고, 너무 크면 감도가 떨어질 수 있습니다.[^4_3][^4_2]
- **참조 샘플 측정**: 본 시편 전에 reference sample을 먼저 측정해 장비 정확도를 확인하는 것이 권장됩니다.[^4_1]


## 5) 피팅 전략

- **동시 피팅**: AlN의 열전도도, Al/AlN 계면 TBC, Al transducer 물성을 함께 고려하는 방식이 일반적입니다.[^4_7][^4_1]
- **고정/자유 파라미터 분리**: Al의 \$ \kappa \$, \$ \rho c_p \$, 두께를 어디까지 고정하고 어디를 피팅할지 사전에 정해야 합니다. 보통 transducer는 일부 값을 고정하고, 관심층인 AlN과 계면을 중심으로 피팅합니다.[^4_9][^4_7]
- **불확도 반영**: thickness uncertainty, spot size uncertainty, transducer κ uncertainty를 민감도 분석에 포함시켜야 합니다.[^4_10][^4_9]


## 6) 네 실험용 실전 체크리스트

1. AlN/Si 구조와 측정면을 확정한다.
2. 표면 거칠기와 산화 상태를 확인한다.
3. Ar plasma 또는 적절한 세정으로 transducer 증착면을 준비한다.
4. Al transducer 두께를 70–100 nm 범위에서 설계한다.
5. Al 두께는 acoustic echo로 검증한다.
6. Al의 열전도도는 reference sample로 보정한다.
7. AlN 두께와 계면층 두께를 ellipsometry/TEM으로 확보한다.
8. TDTR 주파수와 spot size를 sensitivity 기준으로 선택한다.
9. AlN κ, Al/AlN TBC, transducer 파라미터의 fit/fixed 여부를 정한다.
10. reference sample로 장비/모델을 먼저 검증한 뒤 본 시편을 측정한다.[^4_10][^4_2][^4_1]

원하면 다음 단계로 **“AlN/Si TDTR 실험 준비표”를 표 형식으로 정리**해서, 항목별로 *필수 / 권장 / 선택*까지 나눠줄게.
<span style="display:none">[^4_11][^4_12][^4_13][^4_14][^4_15][^4_16][^4_17][^4_18][^4_19][^4_20]</span>

<div align="center">⁂</div>

[^4_1]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11044587/

[^4_2]: https://pubs.aip.org/aip/jap/article-pdf/doi/10.1063/5.0245381/20429173/095105_1_5.0245381.pdf

[^4_3]: https://arxiv.org/pdf/1807.01258v1.pdf

[^4_4]: https://www.linseis.com/ko/열-분석-방법/시간-도메인-열반사율tdtr/

[^4_5]: https://analyzing-testing.netzsch.com/en/products/time-domain-thermoreflectance-analyzer-tdtr/nanotr

[^4_6]: https://netzsch.co.jp/product/nanotr-picotr/

[^4_7]: https://poplab.stanford.edu/pdfs/Perez-SputteredAlNhighThermalK-nano23.pdf

[^4_8]: https://www.zhinst.com/ko/applications/optics-photonics/time-domain-thermoreflectance-tdtr/

[^4_9]: https://cahill.matse.illinois.edu/software-and-data/

[^4_10]: https://poplab.stanford.edu/pdfs/Xu-AlNthermalCondDefectsSizeEffects-jap19.pdf

[^4_11]: https://journal.mrs-k.or.kr/articles/xml/vbnV/

[^4_12]: http://kjmm.org/upload/pdf/kjmm-132.pdf

[^4_13]: https://s-space.snu.ac.kr/bitstream/10371/210086/1/000000183259.pdf

[^4_14]: https://www.reseat.or.kr/portal/cmmn/file/fileDown.do?menuNo=200019\&atchFileId=36da5611327e45eea8dd2546d9e081c1\&fileSn=1\&bbsId=

[^4_15]: https://ceramist.or.kr/journal/view.php?viewtype=pubreader\&number=970

[^4_16]: https://www.e-jwj.org/journal/view.php?number=2032162

[^4_17]: https://koreascience.kr/article/JAKO201218552490372.pdf

[^4_18]: https://chem.kaist.ac.kr/_res/pdfjs/web/viewer.html?url

[^4_19]: https://dr.ntu.edu.sg/handle/10356/166521

[^4_20]: https://www.themoonlight.io/ko/review/thermal-characterization-of-buried-interfaces-in-multilayer-heterostructures-via-tdtr-with-periodic-waveform-analysis


---

# 사전연구에는 RF모드를 사용했는지 FF모드를 사용했는지 확인이 필요해 Transducer 두께는 100~120 nm로 세팅할 예정이야. 아직도 이해안되고 어떻게 만들어야할지 감이 안 잡힌다.

지금 단계에서 가장 중요한 결론은 **AlN/Si TDTR 사전연구는 대부분 FF 구성으로 이해하는 게 맞고, 네가 말한 100–120 nm Al transducer는 문헌보다 약간 두꺼운 편이지만 충분히 가능한 범위**라는 점입니다. 다만 이 두께를 쓰면 **transducer 자체의 열확산/광학 신호가 더 강해져서, 두께와 κ를 더 엄격하게 보정**해야 합니다.[^5_1][^5_2]

## 먼저 방향을 잡으면

- **FF = 네 구조에서 기본값**으로 생각하면 됩니다. 상부 금속 transducer를 올리고, 같은 면에서 pump/probe를 하는 일반 TDTR가 여기에 해당합니다.[^5_3][^5_1]
- **RF는 투명 기판을 통해 반대면을 가열/검출하는 특수 구성**이라서, AlN/Si 상부 금속 transducer 실험과는 보통 다릅니다.[^5_4][^5_5]
- 따라서 네가 할 준비는 “RF냐 FF냐”를 오래 고민하기보다, **FF로 설계하고 Al transducer를 얼마나 정확히 만들지**에 집중하는 게 현실적입니다.[^5_2][^5_1]


## 100–120 nm Al transducer로 준비할 것

- **두께 목표를 정하되 실제 두께를 꼭 측정**해야 합니다. TDTR에서는 transducer thickness가 결과에 직접 들어가므로, nominal 100–120 nm와 actual thickness는 별개로 봐야 합니다.[^5_6][^5_2]
- **picosecond acoustic echo**로 두께를 보정하는 흐름이 표준적입니다. 문헌에서도 nominal 100 nm Al을 증착한 뒤 실제 두께를 echo로 106 nm처럼 다시 잡은 사례가 있습니다.[^5_6]
- **Al의 열전도도 κAl도 따로 보정**하는 게 안전합니다. companion sample로 κAl를 먼저 확인한 뒤 본 시편에 넣는 방식이 문헌에서 쓰입니다.[^5_7]


## 네가 만들 때의 실전 순서

1. **샘플 구조 확정**: Mo/AlN/Si 또는 Al/AlN/Si인지 먼저 고정.
2. **표면 세정**: transducer 증착면의 산화/오염을 최소화.
3. **Al transducer 증착**: nominal 100–120 nm로 설계.
4. **두께 확인**: 가능하면 acoustic echo로 actual thickness 측정.
5. **κAl 보정**: reference sample로 검증.
6. **TDTR 측정 조건 선정**: modulation frequency, spot size, delay range를 sensitivity 기준으로 잡기.
7. **피팅 파라미터 분리**: Al thickness, κAl, AlN thickness, AlN κ, Al/AlN TBC 중 무엇을 고정하고 무엇을 피팅할지 정하기.[^5_1][^5_2]

## 왜 아직 감이 안 잡히는지

- TDTR는 “그냥 금속 얹고 재는” 실험이 아니라, **transducer 자체가 모델의 일부**입니다. 그래서 증착이 샘플 준비이면서 동시에 모델 입력값 준비입니다.[^5_8][^5_3]
- 즉, **Al을 얼마나 두껍게 올렸는가보다 실제 두께와 κ를 얼마로 넣는가**가 더 중요합니다.
- 네가 헷갈리는 지점은 정상이고, 실제로 TDTR는 이런 **파라미터 식별성** 때문에 reference와 sensitivity analysis가 필수입니다.[^5_2][^5_8]

원하면 다음 답변에서 바로
**“네 시료 기준 AlN/Si TDTR 제작·측정 절차”**를

- 장비 없이 이해하기 쉬운 버전
- 실험실에서 바로 실행하는 버전
두 가지로 나눠서 적어줄게.
<span style="display:none">[^5_10][^5_11][^5_12][^5_13][^5_14][^5_15][^5_16][^5_17][^5_18][^5_19][^5_9]</span>

<div align="center">⁂</div>

[^5_1]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11044587/

[^5_2]: https://arxiv.org/abs/1511.04852v2

[^5_3]: https://arxiv.org/pdf/1807.01258v1.pdf

[^5_4]: https://analyzing-testing.netzsch.com/de/produkte/time-domain-thermoreflectance-analyzer-tdta/nanotr

[^5_5]: https://analyzing-testing.netzsch.com/en/products/time-domain-thermoreflectance-analyzer-tdtr/nanotr

[^5_6]: https://arxiv.org/pdf/2411.15767.pdf

[^5_7]: https://poplab.stanford.edu/pdfs/Perez-SputteredAlNhighThermalK-nano23.pdf

[^5_8]: https://www.acsmaterial.com/blog-detail/tdtr-time-domain-thermoreflectance.html

[^5_9]: https://pubs.aip.org/aip/jap/article/124/16/161103/1030095/Tutorial-Time-domain-thermoreflectance-TDTR-for

[^5_10]: https://pubs.aip.org/aip/jap/article/109/11/113520/697138/Ta-and-Au-Pd-alloy-metal-film-transducers-for-time

[^5_11]: https://www.osti.gov/pages/servlets/purl/2997110

[^5_12]: https://www.osti.gov/pages/biblio/2997110

[^5_13]: https://www.osti.gov/servlets/purl/1109030

[^5_14]: https://users.mrl.illinois.edu/cahill/tongji_tdtr_advanced.pdf

[^5_15]: https://pubmed.ncbi.nlm.nih.gov/34797056/

[^5_16]: https://s-space.snu.ac.kr/bitstream/10371/210086/1/000000183259.pdf

[^5_17]: https://dr.ntu.edu.sg/handle/10356/166521

[^5_18]: https://www.scribd.com/document/517816603/1-5046944

[^5_19]: https://patrickehopkins.com/wp-content/uploads/2016/08/2016-sthc_tdtrnometal.pdf


---

# 첨부파일 내용 참고해서 내가 어떻게 준비하면 되는지를 확인해줘 사전연구와의 내용들을 반영해서

지금 갖고 있는 자료와 사전연구(AlN/Si TDTR 논문들)를 같이 보면, **당신이 할 일은 “어떤 모드(RF/FF)를 쓸지 결정 → 그 모드에 맞게 샘플 설계 → 금속필름/AlN/Si의 열물성 준비”**입니다. 아주대 NanoTR 시료 기준에 정확히 맞추면 되고, 이미 계획한 100–120 nm transducer 두께도 기준과 딱 맞습니다.[^6_1][^6_2]

아래에 **당신 상황(Mo 또는 Al transducer, AlN/Si 구조, TDTR만 사용)**에 맞춰서 정리해볼게요.

***

## 1. 먼저 모드 선택부터: RF vs FF

NanoTR 문서 기준으로:[^6_1]

- **FF mode (Front heating / Front detection)**
    - 구조: 상부 metal film(100–120 nm) / 측정 대상(measuring object) / 기판
    - 기판: **불투명·투명 모두 가능**, 저열전도 기판 권장
    - 측정값: **열확산도(thermal diffusivity), 열유출도(thermal effusivity)**
    - 당신이 말한 **Mo(or Al)/AlN/Si 상부에서 펌프·프로브 조사 → FF mode** 가 NanoTR 기준과 정확히 일치.
- **RF mode (Rear heating / Front detection)**
    - 구조: 기판 뒤에서 가열, front surface에서 검출
    - 기판: **투명 substrate (glass, quartz, double-side polished high-ρ Si)** 요구
    - 측정값: **열확산도 + 계면 열저항(ITR)**, ITR 위해선 최소 **세 가지 두께의 샘플 필요**.[^6_1]

당신의 알짜 결론:

- 지금 가지고 있는 혹은 만들 AlN/Si 웨이퍼가 **일반 Si(투명 X)** 라면, **현실적으로 FF mode만 가능**하다고 보면 됩니다.
- 만약 **RF 모드로 ITR까지 정교하게 보고 싶다면**:
    - AlN을 **투명 기판(예: quartz)이나 고저항 DSP-Si(≥ 1000 Ω·cm)** 위에 성장해서,
    - **AlN 두께가 서로 다른 샘플 3종 이상(예: 0.5 μm / 1 μm / 2 μm)**을 준비해야 합니다.[^6_1]

***

## 2. 샘플 구조 설계 (당신 실험 기준)

NanoTR FF mode + TDTR 사전연구를 합치면, **가장 현실적인 구조는 아래**입니다.

- **FF mode용 샘플 구조(권장)**
    - 금속 film (100–120 nm, Mo 권장 / Al 가능)
    - AlN 층 (측정 대상; 가능한 1 μm 이상이 sensitivity 측면에서 유리)[^6_2][^6_1]
    - Si 기판 (일반 Si 사용 가능, 저열전도 기판이면 피팅이 쉬워짐)

checklist:

- 금속 film: **Mo(센터 기준 권장)** 혹은 Al, Pt. 두께는 **100–120 nm**로 설계 (센터 기준 그대로).[^6_1]
- measuring object(AlN) 권장 두께:
    - 문서 기준: 세라믹은 **300 nm ~ 3 μm**, 금속은 1–10 μm 권장.[^6_1]
    - 논문 기준: AlN/Si TDTR에서 **수백 nm~수 μm AlN**을 많이 사용. 1 μm 이상이면 더 안정적.[^6_3][^6_2]
- substrate: 일반 Si도 가능하지만, 아주대 문서엔 **저열전도도 기판을 권장**하고 있으니, 가능하면 SiO₂/Si 또는 열전도 낮은 기판을 고려하면 피팅이 쉬워짐.[^6_4][^6_1]

***

## 3. 금속 필름(Transducer) 관련 준비

NanoTR 시료 기준 + TDTR 논문 기준을 합치면 이렇게 준비하면 됩니다.[^6_5][^6_6][^6_2][^6_1]

1. **두께**
    - 설계: 100–120 nm (센터 권장 범위와 동일)
    - 실제: **profilometer, ellipsometry 또는 picosecond acoustic echo**로 actual thickness를 측정해서 모델에 넣기.
2. **재질 선택**
    - 센터 기준: **Mo 권장**, Al, Pt 가능.[^6_1]
    - TDTR 사전연구: Al이 가장 표준 (Al/AlN/Si 구조). κAl는 별도 reference로 보정하는 경우가 많음.[^6_2][^6_5]
    - 판단:
        - 센터에서 Mo를 강력히 recommend → **센터의 Mo 열확산도/κ 데이터를 활용할 수 있어 편함**.[^6_1]
        - Al을 쓰고 싶다면: **Al transducer의 열확산도 값(논문값 or 직접 측정 값)을 제공**해야 하고, 논문값과 실제 값이 다를 수 있다는 점을 감안해 reference 측정을 준비해야 함.[^6_5][^6_1]
3. **금속 필름 열물성 데이터**
    - 필요 항목: **열확산도, 비열, 밀도**.[^6_1]
    - 제공 방식:
        - 센터에서 측정:
            - Mo film coating 의뢰 시, PicoTR 장비로 금속 film의 열확산도를 측정해줌 → 그 값을 NanoTR 모델에 사용.[^6_1]
        - 직접 제공:
            - 직접 증착한 metal film에 대해 논문값을 제공할 수 있음. 다만 **증착 조건에 따라 논문값과 실제 값이 다를 가능성이 크므로, 결과 해석 시 “ref.값 사용”이라고 명시**해야 함.[^6_1]

***

## 4. Substrate / AlN (measuring object) 쪽 준비

문서에서 요구하는 건:[^6_1]

1. **두께 정보**
    - substrate 두께: ≤ 1 mm 권장, lateral 10–15 mm 크기. (NanoTR 규격)[^6_1]
    - measuring object(AlN) 두께:
        - 문서: 세라믹 300 nm–3 μm 권장.[^6_1]
        - TDTR: AlN/Si에서 수백 nm~수 μm가 일반적.[^6_2]
2. **열물성 값**
    - substrate:
        - 열확산도, 비열, 밀도 값 필요. (못 주면 **bare substrate만 따로 보내**서 센터에서 측정)[^6_1]
    - measuring object (AlN):
        - 비열, 밀도 값 필요. (못 주면 **free-standing 상태 sample**을 보내거나, 문헌 ref.값을 써야 함)[^6_1]
        - TDTR 사전연구 기준 AlN bulk의 κ(T) 데이터, AlN thin film의 κ 범위(수십 W/mK)를 정리해서 ref.로 넣을 수 있음.[^6_7][^6_5]
    - metal film:
        - 열확산도, 비열, 밀도. 못 주면 금속 종류와 ref.값 + 센터 측정 조합으로 처리.[^6_1]
3. **평탄도**
    - “윗면과 아랫면이 편평, 위치별 두께 편차가 없어야 함” →
→ AlN 증착 후, 표면 roughness가 너무 크지 않도록 조건 잡기. CMP까지는 아니더라도, “빛이 뚫리지 않으면서 얼굴이 비칠 정도의 반사면”이 목표.[^6_1]

***

## 5. RF 모드까지 고려한다면 (선택)

RF 모드는 **계면 열저항(ITR)**까지 보기 위해 쓰는 모드라서:[^6_1]

- substrate: 반드시 **투명 기판** (glass, quartz, 또는 double-sided polished high-resistivity Si ≥ 1000 Ω·cm) 이어야 함.
- ITR 측정 or 고려 시: **최소 세 종류 두께의 측정 대상(AlN) 샘플** 필요.[^6_1]
- substrate 정보는 RF에서는 필요 없다고 문서에 적혀 있지만, measuring object/metal film의 열물성은 여전히 필요.

당신 상황에서 RF를 하려면:

- AlN을 **투명 기판(예: quartz) 위에 deposition**해서 두께를 세 가지 이상으로 맞춘 별도 샘플 세트를 설계해야 함.
- 현재 진행 중인 AlN/Si(불투명 Si) 구조에는 일단 **FF로 cross-plane κ 중심 측정 → 추후 별도 RF 세트로 ITR 확장**이 현실적인 전략.

***

## 6. “이제 어떻게 만들지”를 한 줄씩 정리하면

당신이 지금부터 하면 되는 일:

1. **실제 목표 구조 확정**
    - 1차: Mo(or Al)/AlN/Si, FF mode, TDTR로 AlN κ 중심 측정
    - 2차(원하면): 투명 기판 위 AlN, RF mode + 여러 두께로 ITR까지
2. **AlN 증착 계획 정리**
    - 두께: 최소 300 nm 이상, 가능하면 1 μm 내외 한 두께부터 시작
    - 동일 조건으로 두께만 다른 샘플 세트를 만들 생각이면 RF/ITR까지 대비 가능
3. **금속 transducer 설계**
    - 소재: Mo(센터 권장) 또는 Al
    - 두께: 100–120 nm
    - 증착 장비·조건 기록, thickness 측정 루트 확보 (acoustic echo, ellipsometry 등)
4. **열물성 데이터 준비**
    - substrate: bare Si (또는 사용 기판) 샘플 하나 따로 준비 → 열확산도/비열/밀도를 센터에 측정 의뢰 or 문헌 + 데이터 정리
    - AlN: 비열/밀도는 문헌 ref.값 정리, 가능하면 자체 측정 계획
    - metal film: Mo/Al의 비열/밀도/열확산도 →
        - 센터 측정 의뢰(권장) + ref.값도 함께 정리
5. **센터에 제공할 정보 패키지**
    - 각 샘플별: 구조, 층 순서, 각 층 두께, 증착 조건 요약
    - 층별 열물성: 실측값 or ref.값 명시 (어디까지 ref인지 분명히)

***

원하면,

- 당신이 실제로 만들려고 하는 “AlN 두께, 기판 타입, transducer 재질”을 적어주면
→ 그 구조에 딱 맞는 **NanoTR 의뢰용 시료 스펙 시트(표 + bullet)**를 만들어줄게.

<div align="center">⁂</div>

[^6_1]: NanoTRsiryogyugyeog.pdf

[^6_2]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11044587/

[^6_3]: https://pubs.aip.org/aip/jap/article-pdf/doi/10.1063/5.0245381/20429173/095105_1_5.0245381.pdf

[^6_4]: https://arxiv.org/abs/1511.04852v2

[^6_5]: https://poplab.stanford.edu/pdfs/Perez-SputteredAlNhighThermalK-nano23.pdf

[^6_6]: https://arxiv.org/pdf/2411.15767.pdf

[^6_7]: https://poplab.stanford.edu/pdfs/Xu-AlNthermalCondDefectsSizeEffects-jap19.pdf


---

# RF모드 시료 구성 구조가 다른데... 계면 열특성이 내가 의도한 구성이 아닌부분도 있고... 생각하면 이해 안되는 부분도 존재하기 때문에 더 망설여진다....

AlN 두께 300, 150, 75 nm, 기판 타입 Si (100) , transducer 재질 (Mo)
AlN 두께 300, 150, 75 nm, 기판 타입 Si (100) , transducer 재질 (Al)

지금 망설이는 포인트가 **정확히 정상**입니다. 네가 적은 두 샘플 조합은 **FF 모드에는 잘 맞지만, RF 모드에는 맞지 않는 구조**이기 때문에, 사전연구와 장비 기준이 섞여 보이면서 혼란이 생긴 겁니다.[^7_1][^7_2]

## 핵심 결론

- **AlN 300/150/75 nm + Si(100) + Mo transducer**
- **AlN 300/150/75 nm + Si(100) + Al transducer**

이 두 세트는 **RF가 아니라 FF로 생각하는 게 맞습니다.** 아주대 NanoTR 기준에서도 FF는 **metal film / measuring object / substrate** 구조이고, substrate는 투명일 필요가 없으며, opaque substrate도 가능하다고 되어 있습니다.[^7_1]

즉, 네가 의도한 구조는:

- **상부 금속 transducer(Mo 또는 Al)**
- **그 아래 AlN 두께 300/150/75 nm**
- **Si(100) 기판**

이므로, **전면에서 펌프·프로브를 쏘는 FF 구성**으로 이해하면 됩니다.[^7_1]

## 왜 RF가 아닌가

RF는 장비 문서상 **rear heating/front detection**이라서, 기판 뒤에서 열을 넣고 앞면에서 검출하는 구조입니다. 그런데 네 샘플은 **Si(100) 기판 위에 AlN를 올리고 그 위에 금속 transducer를 얹는 구조**이므로, 실제 측정은 금속이 있는 위쪽 면에서 이루어지는 **FF 구성**입니다.[^7_1]

그리고 RF는 문서상 **투명 기판 또는 DSP-Si(고저항, 1000 Ω·cm 이상)**가 필요합니다. 일반 Si(100) 위 박막 샘플은 RF용으로 바로 쓰기 어렵습니다.[^7_1]

## 네 샘플에서 중요한 점

네가 의도한 건 아마 이런 거죠:


| 샘플 | 구조 해석 | 모드 |
| :-- | :-- | :-- |
| AlN 300/150/75 nm + Si(100) + Mo | Mo/AlN/Si 상부 측정 | FF |
| AlN 300/150/75 nm + Si(100) + Al | Al/AlN/Si 상부 측정 | FF |

이 경우 핵심은 **transducer 재질 비교**입니다.

- **Mo**: 센터 기준 권장 재질, 하지만 TDTR 문헌에서는 Al보다 덜 표준적이라 실측 물성/산화 상태 확인이 더 중요합니다.[^7_3][^7_1]
- **Al**: TDTR 사전연구에서 가장 표준적인 transducer이고, Al의 열전도도는 reference sample로 보정하는 경우가 많습니다.[^7_2][^7_3]


## 어떻게 준비하면 되는가

네가 지금 해야 할 준비는 RF 고민이 아니라 아래 순서입니다.

1. **FF로 결정**
    - 이유: Si(100) 위 상부 transducer 구조이기 때문.[^7_1]
2. **샘플 3종 준비**
    - AlN 300 nm
    - AlN 150 nm
    - AlN 75 nm
RF/ITR 목적이 아니라면, 이 3개는 **두께 민감도 확보용 FF 세트**로 보면 됩니다.[^7_1]
3. **각 세트별 transducer 하나씩**
    - 동일한 AlN 두께에 대해 **Mo 버전**
    - 동일한 AlN 두께에 대해 **Al 버전**
이렇게 하면 transducer 영향 비교가 가능합니다.
4. **금속층 두께는 100–120 nm**
    - 네 계획은 문서와 일치합니다.[^7_1]
5. **측정 전에 확인할 것**
    - 샘플 표면이 평탄한지
    - 금속과 AlN 사이 반응이 없는지
    - 실제 금속 두께를 측정할 수 있는지
    - Mo/Al의 실측 열확산도 또는 reference 값을 넣을 수 있는지[^7_1]

## 현실적인 추천

만약 네 목적이 **AlN의 cross-plane 열특성과 transducer 영향 비교**라면, 추천 우선순위는:

- **1순위: Al/AlN/Si, FF**
    - 문헌 친화적이고 해석이 가장 쉬움.[^7_2][^7_3]
- **2순위: Mo/AlN/Si, FF**
    - 센터 기준에 맞고, 비교용으로 좋음.
    - 다만 Mo는 Al보다 문헌 데이터와 실제 증착값 차이를 더 조심해야 함.[^7_1]
- **RF는 별도 프로젝트로 분리**
    - 투명 기판이나 DSP-Si 기반으로 설계해야 해서, 지금 구조와 섞어 생각하지 않는 게 좋습니다.[^7_1]


## 지금의 혼란을 한 문장으로 정리

네가 만든 두 구조는 **“RF/FF를 고민할 대상”이 아니라, FF에서 transducer 재질(Mo vs Al)을 비교하는 대상**입니다.
그래서 현재는 **RF를 버리고 FF로 고정**해서 생각하는 게 맞습니다.[^7_1]

원하면 다음 답변에서 바로
**“AlN 300/150/75 nm, Mo vs Al transducer, FF용 실험계획표”**를
샘플별로 한눈에 보이게 정리해줄게.

<div align="center">⁂</div>

[^7_1]: NanoTRsiryogyugyeog.pdf

[^7_2]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11044587/

[^7_3]: https://poplab.stanford.edu/pdfs/Perez-SputteredAlNhighThermalK-nano23.pdf


---

# ITR이 AlN 계면 열저항 만을 나타내는건지 AlN과 상대면의 계면 열저항으로 나타내냐에 따라 의도가 달라져..

맞아요. **ITR이 무엇과 무엇 사이의 계면을 뜻하느냐에 따라 의도가 완전히 달라집니다.** TDTR/NanoTR 문맥에서 ITR은 보통 **“측정 대상 박막과 인접한 다른 층 사이의 계면 열저항”**을 뜻하고, **AlN 계면만을 자동으로 의미하지는 않습니다.**[^8_1][^8_2]

## 핵심 정리

- **ITR = interfacial thermal resistance**로, 두 재료 사이 열흐름 저항입니다. 즉 “AlN만의 고유값”이 아니라 **AlN/상대층 계면값**입니다.[^8_3][^8_1]
- 따라서 네 구조가 **Mo/AlN/Si** 또는 **Al/AlN/Si**라면, TDTR에서 얻는 ITR은 보통
**AlN–metal 계면** 또는 **AlN–Si 계면** 중 무엇을 모델에 넣었는지에 따라 달라집니다.[^8_2][^8_4]
- 실제 논문에서는 **AlN-SOI**처럼 구조가 복잡할 때, **Al/AlN 계면, AlN bulk, AlN/Si deposition interface, AlN/Si bonded interface**를 서로 나눠서 따로 다루기도 합니다.[^8_5]


## 네 경우에 중요한 점

- 네가 **상부 transducer(Mo 또는 Al)** 를 올린 FF 구조라면, 측정 신호는 보통 **“transducer/AlN 계면 + AlN bulk + AlN/Si 계면”이 섞인 유효 응답**입니다.[^8_2][^8_5]
- 그래서 “ITR을 AlN 계면 열저항만으로 볼 것인가?”를 묻는다면, **아니고**, 보통은 **현재 모델에 포함된 모든 계면의 합 또는 유효값**으로 해석해야 합니다.[^8_6][^8_7]
- 특히 AlN이 얇을수록(예: 75 nm) **transducer/AlN 계면 영향**과 **AlN/Si 계면 영향**이 서로 분리되기 어려워집니다.[^8_7][^8_2]


## 실험 의도별로 보면

| 네가 원하는 해석 | ITR이 의미하는 것 | 추천 |
| :-- | :-- | :-- |
| AlN 자체의 계면 특성 확인 | AlN/Si 계면 또는 AlN/상대층 계면 | 가능하지만 모델 분리가 중요 |
| transducer 영향까지 포함한 유효 열저항 | Mo/AlN 또는 Al/AlN 포함 전체 응답 | FF TDTR에서 가장 현실적 |
| “AlN 고유 계면”만 분리 | 매우 어려움, 두께 시리즈와 추가 기준 샘플 필요 | 신중히 설계 |

## 추천하는 해석 방식

- **75 / 150 / 300 nm 세 두께 샘플**은 매우 좋습니다.
- 이 두께 시리즈를 쓰면, ITR을 하나의 숫자로 뭉뚱그리지 않고 **두께 의존성으로부터 bulk κ와 interface contribution을 분리**하려는 설계가 가능합니다.[^8_7][^8_2]
- 다만 **Mo/AlN/Si와 Al/AlN/Si를 섞어서 비교하면**, 얻는 ITR은 결국 **transducer 재질까지 포함한 시스템 수준의 ITR**이 됩니다.[^8_5][^8_7]


## 결론

네 질문에 대한 짧은 답은 이겁니다.

- **ITR은 “AlN만의 값”이 아니라, AlN과 상대층 사이의 계면 열저항**입니다.[^8_1][^8_3]
- 따라서 네 실험에서는 **Mo(or Al)/AlN/Si에서 어떤 계면을 모델에 넣을지 먼저 명확히 해야** 합니다.[^8_2][^8_5]
- 지금 네가 망설이는 이유는 맞고, 그건 **해석 대상 계면이 transducer/AlN인지, AlN/Si인지, 또는 둘 다인지를 아직 하나로 못 고정했기 때문**입니다.[^8_7]

원하면 다음 답변에서 바로
**“네 샘플(75/150/300 nm)에서 TDTR로 얻는 값이 무엇으로 해석되는지”**를

- Mo transducer 버전
- Al transducer 버전
으로 나눠서 아주 구체적으로 정리해줄게.
<span style="display:none">[^8_10][^8_11][^8_12][^8_13][^8_14][^8_15][^8_8][^8_9]</span>

<div align="center">⁂</div>

[^8_1]: https://pmc.ncbi.nlm.nih.gov/articles/PMC12388737/

[^8_2]: https://arxiv.org/pdf/1807.01258v1.pdf

[^8_3]: https://journals.aps.org/rmp/abstract/10.1103/RevModPhys.94.025002

[^8_4]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11044587/

[^8_5]: https://pubs.acs.org/doi/10.1021/acsami.3c16905

[^8_6]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6997172/

[^8_7]: https://patrickehopkins.com/wp-content/uploads/2024/08/li2024aa.pdf

[^8_8]: https://pubmed.ncbi.nlm.nih.gov/35895030/

[^8_9]: https://pubs.acs.org/doi/10.1021/acsami.4c05258

[^8_10]: https://pubs.acs.org/doi/abs/10.1021/acsami.8b07014

[^8_11]: https://www.sciencedirect.com/science/article/abs/pii/S0017931096002797

[^8_12]: http://kummelgroup.ucsd.edu/pubs/papers_2024/thermal-transport-at-the-aln-sic-interface-and-grain-boundary-of-aln.pdf

[^8_13]: https://microsanj.com/technology/time-domain-thermoreflectance-tdtr/

[^8_14]: https://pubs.aip.org/aip/jap/article-pdf/doi/10.1063/5.0245381/20429173/095105_1_5.0245381.pdf

[^8_15]: https://www.scribd.com/document/517816603/1-5046944


---

# 네 샘플(75/150/300 nm)에서 TDTR로 얻는 값이 무엇으로 해석되는지”를

Mo transducer 버전
Al transducer 버전
으로 나눠서 아주 구체적으로 정리

아주 구체적으로 말하면, **네 75/150/300 nm AlN/Si 샘플에서 TDTR이 직접 주는 값은 “AlN 고유의 단일 계수”가 아니라, transducer/AlN/Si로 이어지는 cross-plane 열흐름을 만족하는 유효 파라미터**입니다. 무엇이 피팅 변수로 들어가느냐에 따라, 결과는 **AlN bulk κ, 계면 열저항(TBR/ITR), 혹은 둘의 결합된 유효값**으로 해석됩니다.[^9_1][^9_2]

## 1) Mo transducer 버전

- **측정 구조**: Mo / AlN(75, 150, 300 nm) / Si.
- **가장 민감한 값**: 보통 **Mo/AlN 계면 + AlN bulk + AlN/Si 계면**이 함께 묶인 응답입니다. 그래서 Mo를 썼다고 해서 AlN 계면만 “순수하게” 보이는 건 아닙니다.[^9_3][^9_1]
- **실제로 해석되는 것**:
    - AlN가 충분히 두꺼우면(300 nm 쪽) → **AlN bulk cross-plane thermal conductivity κ⊥** 쪽 감도가 커집니다.
    - AlN가 얇으면(75 nm 쪽) → **Mo/AlN 계면 저항 + AlN/Si 계면 저항** 비중이 커집니다.
- **주의점**: Mo는 문서상 권장 transducer이지만, TDTR 문헌에서는 Al보다 덜 표준적이라 **Mo의 열확산도/비열/밀도/산화 상태**를 더 엄격히 넣어야 합니다.[^9_3]
- **결론적으로** Mo 버전의 TDTR 결과는 대체로
**“Mo/AlN/Si 전체 스택의 유효 cross-plane thermal resistance”**
로 보는 게 안전합니다.[^9_2][^9_4]


## 2) Al transducer 버전

- **측정 구조**: Al / AlN(75, 150, 300 nm) / Si.
- **가장 표준적인 해석**: TDTR 사전연구에서 가장 흔한 형태라, 보통 **Al/AlN 계면, AlN bulk κ⊥, AlN/Si 계면**을 모델에 넣고 피팅합니다.[^9_5][^9_6][^9_1]
- **실제로 해석되는 것**:
    - 300 nm 시료: **AlN bulk κ⊥의 영향이 가장 크게 보임**.
    - 150 nm 시료: **bulk와 계면 기여가 섞임**.
    - 75 nm 시료: **계면 저항이 지배적**이 되기 쉬움.
- **Al transducer의 역할**:
    - Al은 단순한 코팅이 아니라 **모델 내 별도 층**입니다.
    - Al의 열전도도와 두께 오차가 결과에 들어가며, 문헌에서는 **companion sample로 Al κ를 보정**한 뒤 본 시료를 해석합니다.[^9_2][^9_5]
- **결론적으로** Al 버전의 TDTR 결과는
**“Al/AlN/Si 스택의 cross-plane thermal conductivity + interface thermal resistance”**
로 해석됩니다. 특히 Al 쪽이 문헌 친화적이라 결과를 논문화하기 더 쉽습니다.[^9_6][^9_5]


## 3) 75 / 150 / 300 nm를 같이 쓸 때 무엇이 달라지나

이 두께 시리즈의 장점은 **계면과 bulk를 분리하려는 것**입니다.[^9_4][^9_1]

- **75 nm**
    - 박막이 얇아서 **계면 저항 민감도↑**
    - bulk κ보다 **transducer/AlN 계면 + AlN/Si 계면** 영향이 큼.
- **150 nm**
    - 계면과 bulk가 어느 정도 섞인 중간 영역.
- **300 nm**
    - 상대적으로 **AlN bulk κ⊥**를 더 잘 볼 수 있음.
    - 여전히 계면이 사라지는 건 아니지만, 추정 안정성이 더 좋음.

즉, 네 샘플 세트는 사실상
**“두께 변화로 bulk와 interface를 분해하는 설계”**입니다.[^9_7][^9_1]

## 4) 네가 조심해야 할 해석 함정

- **ITR 하나만 딱 분리된다고 생각하면 안 됨**. TDTR은 기본적으로 민감도에 따라 여러 파라미터가 얽힙니다.[^9_2]
- **transducer 재질이 바뀌면 ITR 해석도 달라짐**.
    - Mo 버전: Mo/AlN 계면이 추가로 강하게 개입.
    - Al 버전: Al/AlN 계면이 표준적으로 들어가고 문헌 비교가 쉬움.[^9_8][^9_1]
- 따라서 “AlN의 계면 열저항”이라고 쓸 때도, 실제로는 **AlN/Si 계면인지, Al/AlN 계면인지, 또는 둘 다 포함한 유효 저항인지**를 명시해야 합니다.[^9_9][^9_4]


## 5) 한 줄 결론

- **Mo transducer 버전**: 결과는 주로 **Mo/AlN/Si 스택의 유효 열저항**, 특히 얇은 AlN에서 계면 영향이 큼.
- **Al transducer 버전**: 결과는 **Al/AlN/Si 스택의 cross-plane κ와 계면 열저항**으로 해석하는 것이 표준적이고 문헌 친화적.[^9_1][^9_5][^9_2]

원하면 다음 답변에서 바로
**“75/150/300 nm 각각에서 피팅 파라미터를 무엇으로 두어야 하는지”**를
Mo 버전 / Al 버전으로 나눠서 표로 정리해줄게.
<span style="display:none">[^9_10][^9_11][^9_12][^9_13][^9_14][^9_15][^9_16][^9_17]</span>

<div align="center">⁂</div>

[^9_1]: https://arxiv.org/pdf/1807.01258v1.pdf

[^9_2]: https://www.osti.gov/pages/servlets/purl/2997110

[^9_3]: NanoTRsiryogyugyeog.pdf

[^9_4]: https://pmc.ncbi.nlm.nih.gov/articles/PMC12388737/

[^9_5]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11044587/

[^9_6]: https://patrickehopkins.com/wp-content/uploads/2021/08/hoque2021ab.pdf

[^9_7]: https://arxiv.org/pdf/2604.12539.pdf

[^9_8]: https://dr.ntu.edu.sg/handle/10356/166521

[^9_9]: https://patrickehopkins.com/wp-content/uploads/2024/08/li2024aa.pdf

[^9_10]: https://vtechworks.lib.vt.edu/server/api/core/bitstreams/3e3cdd7f-eb0c-47a6-9879-4eb116e0d6bd/content

[^9_11]: https://www.diva-portal.org/smash/get/diva2:162491/FULLTEXT01.pdf

[^9_12]: https://www.scribd.com/document/680536371/time-domain-thermoreflectance-TDTR-data-analysis-using-phonon-hydrodynamic-model

[^9_13]: https://patrickehopkins.com/wp-content/uploads/2012/04/hopkins_matrix_workshop.pdf

[^9_14]: https://pubmed.ncbi.nlm.nih.gov/34797056/

[^9_15]: https://pubs.acs.org/doi/10.1021/acsaelm.4c00068

[^9_16]: https://patrickehopkins.com/wp-content/uploads/2016/08/2016-sthc_tdtrnometal.pdf

[^9_17]: https://www.scribd.com/document/517816603/1-5046944


---

# TDTR에서 Transducer 역할이 뭐야...?

TDTR에서 transducer는 **샘플 표면에 올리는 얇은 금속막**이고, 역할은 크게 세 가지입니다.

1) 펌프 빔을 잘 흡수해 열로 바꾸고, 2) 그 금속막의 반사율 변화를 이용해 온도를 읽고, 3) 열이 어디에 얼마나 들어갔는지를 모델링하기 쉽게 만들어 줍니다.[^10_1][^10_2]

## 왜 꼭 필요한가

- **열 발생층**: 금속 transducer가 펌프 에너지를 흡수해서 국소적으로 가열됩니다. 금속은 광 흡수가 좋고, 박막 열원처럼 동작합니다.[^10_3][^10_1]
- **온도 센서**: 금속의 반사율은 온도에 따라 변하므로, probe 빔은 그 변화를 읽어서 온도 감쇠를 추적합니다. 즉 transducer가 곧 **온도계**입니다.[^10_4][^10_1]
- **모델을 단순화**: transducer가 있으면 흡수와 검출이 얇은 잘 정의된 층에서 일어나서, 깊이 방향으로 퍼지는 복잡한 광흡수 문제를 줄일 수 있습니다.[^10_2][^10_5]


## 네 샘플에 대입하면

네가 하려는 **Mo/AlN/Si** 또는 **Al/AlN/Si**에서 transducer는 단순한 코팅이 아니라,
**“펌프를 열로 바꾸고, 그 열이 AlN 안으로 퍼지는 과정을 읽는 기준층”**입니다.[^10_1][^10_2]

그래서 TDTR 해석에서 transducer는 다음을 모두 포함합니다.

- transducer 두께.
- transducer의 열전도도와 비열.
- transducer와 AlN 사이 계면 열저항.
- transducer의 thermoreflectance coefficient $dR/dT$.[^10_6][^10_2]


## 한 문장으로 정리

**TDTR의 transducer는 샘플 위의 “광흡수용 히터 + 온도센서 + 해석 기준층”이다.**
즉, 없으면 측정이 훨씬 어려워지고, 있으면 AlN/Si 같은 박막 계면 열특성을 안정적으로 읽을 수 있습니다.[^10_7][^10_2][^10_1]

원하면 다음 답변에서 바로
**“Mo transducer와 Al transducer가 실제로 어떤 점에서 다른지”**를
네 AlN 75/150/300 nm 샘플 기준으로 비교해줄게.
<span style="display:none">[^10_10][^10_11][^10_12][^10_13][^10_14][^10_15][^10_8][^10_9]</span>

<div align="center">⁂</div>

[^10_1]: https://pubs.aip.org/aip/jap/article/124/16/161103/1030095/Tutorial-Time-domain-thermoreflectance-TDTR-for

[^10_2]: https://www.osti.gov/pages/servlets/purl/2997110

[^10_3]: https://pubs.acs.org/doi/pdf/10.1021/acsphotonics.2c01361

[^10_4]: https://dspace.mit.edu/bitstream/handle/1721.1/139792/JAP08052020.pdf?sequence=2\&isAllowed=y

[^10_5]: https://covalent.com/techniques/thermal-analysis/time-domain-thermoreflectance-tdtr-analysis/

[^10_6]: https://pubmed.ncbi.nlm.nih.gov/23263123/

[^10_7]: https://www.osti.gov/biblio/2997110

[^10_8]: https://pubs.aip.org/aip/rsi/article/95/10/103006/3316821/An-instrumentation-guide-to-measuring-thermal

[^10_9]: https://en.wikipedia.org/wiki/Time-domain_thermoreflectance

[^10_10]: https://www.linseis.com/en/methods/time-domain-thermoreflectance-tdtr/

[^10_11]: https://www.linseis.com/fr/methodes-danalyse-thermique/thermoreflectance-dans-le-domaine-temporel-tdtr/

[^10_12]: https://scienceedge.com/learning_center/basic_principles_of_time-domain_thermoreflectance(TDTR).html

[^10_13]: https://wu.mse.berkeley.edu/publications/Sarah-JAP2022.pdf

[^10_14]: https://www.osti.gov/servlets/purl/1109030

[^10_15]: https://www.acsmaterial.com/blog-detail/tdtr-time-domain-thermoreflectance.html


---

# 반도체 후공정 하이브리드 본딩에 사용하는 계면이 아니라면 ITR TBR TBC는 의미가 없는거네...? 내가 원하는 물질에는 Transducer가 의미가 없어보이는데...

맞아요. **네가 원하는 물질 자체의 계면이 아닌데 transducer가 왜 끼어드나** 하는 느낌이 드는 건 정상입니다. TDTR에서는 transducer가 **“없으면 측정이 안 되는 보조층”** 이면서 동시에 **계면 해석에는 반드시 들어가는 추가 층**이라서, 원하는 계면만 “순수하게” 보는 장치가 아니라는 한계가 있습니다.[^11_1][^11_2]

## 핵심 개념

- TDTR은 샘플 표면에 **금속 transducer**를 올려서 펌프 흡수와 probe 반사율 변화를 읽습니다. 이 금속층이 있어야 표면 온도응답을 안정적으로 측정할 수 있습니다.[^11_3][^11_4]
- 하지만 그 금속층은 **추가 계면 열저항**을 만들어냅니다. 즉, transducer는 해석을 가능하게 하지만 동시에 **원하는 계면 외의 열저항을 추가**합니다.[^11_2][^11_1]
- 그래서 TDTR로 얻는 ITR/TBC는 보통 **“transducer/시료 계면” 또는 “buried interface를 포함한 유효값”**이지, 네가 말한 하이브리드 본딩처럼 딱 그 계면만의 값이라고 단정할 수는 없습니다.[^11_5][^11_1]


## 네 고민이 맞는 이유

- 네가 진짜 알고 싶은 것이 **AlN 자체의 계면**인데, transducer가 그 위에 붙으면 **AlN/transducer 계면**이 먼저 들어옵니다.[^11_6][^11_1]
- 특히 얇은 AlN에서는 transducer 계면, AlN bulk, AlN/Si 계면이 **서로 강하게 섞여서** 하나의 순수한 ITR로 분리되기 어렵습니다.[^11_7][^11_2]
- 그래서 “transducer가 의미 없어 보인다”는 생각은 틀린 게 아니라, **TDTR의 구조적 한계**를 정확히 느낀 겁니다.[^11_1][^11_2]


## 그럼 언제 의미가 있나

- **transducer/시료 계면 자체**를 알고 싶다면 TDTR는 매우 유용합니다. 예를 들어 Al/Si, Al/AlN, Mo/AlN 같은 계면 열전달은 TDTR의 대표 타깃입니다.[^11_8][^11_9]
- **AlN 내부의 bulk κ**를 알고 싶다면, transducer는 “측정을 가능하게 하는 기준층”으로 의미가 있습니다. 이 경우 transducer 자체가 관심 대상은 아니고, 결과에서 보정해야 할 층입니다.[^11_3][^11_1]
- 반대로 **네가 원하는 계면이 buried interface이고 transducer가 너무 방해**한다면, sample design이나 다른 방법이 더 적합할 수 있습니다.[^11_10][^11_2]


## 결론

- **네 물질 자체의 계면이 아니라면, transducer는 관심 대상이 아니라 ‘필수 보조층’입니다.**
- 하지만 TDTR에서는 그 보조층이 **결과 해석에 반드시 들어가므로 완전히 무의미하지는 않습니다.**
- 따라서 네가 지금 느끼는 혼란은 “TDTR로 정말 내가 원하는 계면만 분리할 수 있나?”라는 **방법론적 한계**에서 오는 거고, 그 판단은 아주 타당합니다.[^11_2][^11_5][^11_1]

원하면 다음 답변에서 바로
**“네 목적이 AlN 자체인지, AlN/Si인지, AlN/transducer인지에 따라 TDTR이 적합한지”**를
의사결정표처럼 정리해줄게.
<span style="display:none">[^11_11][^11_12][^11_13][^11_14][^11_15][^11_16]</span>

<div align="center">⁂</div>

[^11_1]: https://www.osti.gov/pages/servlets/purl/2997110

[^11_2]: https://pmc.ncbi.nlm.nih.gov/articles/PMC12388737/

[^11_3]: https://pubs.aip.org/aip/jap/article/124/16/161103/1030095/Tutorial-Time-domain-thermoreflectance-TDTR-for

[^11_4]: https://scienceedge.com/learning_center/introduction_to_time-domain_thermoreflectance(TDTR).html

[^11_5]: https://ui.adsabs.harvard.edu/abs/2016AnRMS..46..433M/abstract

[^11_6]: https://yorkspace.library.yorku.ca/server/api/core/bitstreams/dfd2b837-a310-43a4-b070-e4281f08cb18/content

[^11_7]: https://arxiv.org/pdf/1807.01258v1.pdf

[^11_8]: https://www.sciencedirect.com/science/article/abs/pii/S1290072914000209

[^11_9]: https://www.semanticscholar.org/paper/Measurement-of-Thermal-Boundary-Conductance-of-a-of-Stevens-Smith/13170b78a7f5da213b95446c05f147c64d78c1f2

[^11_10]: https://pubs.acs.org/doi/10.1021/acsami.4c05258

[^11_11]: https://web3.arxiv.org/pdf/2103.08084

[^11_12]: https://www.sciencedirect.com/science/article/abs/pii/S006527172100006X

[^11_13]: https://apps.dtic.mil/sti/pdfs/ADA609810.pdf

[^11_14]: https://link.aps.org/doi/10.1103/PhysRevB.91.035432

[^11_15]: https://nanoheat.stanford.edu/wp-content/uploads/2022/01/Thermal-Characterization-of-Metal−Oxide-Interfaces-Using-TimeDomain-Thermoreflectance-with-Nanograting-Transducers.pdf

[^11_16]: https://www.acsmaterial.com/blog-detail/tdtr-time-domain-thermoreflectance.html


---

# 아! 이해한 부분 있다...

Mo/Si와 AlN/Mo 부분이 해석되도록 하는 방법이 그래서 기판만 있는거 따로 요청하는 부분도 있는거구나 이제서야 좀 이해된다.

TBR_AlN/Si = TBR_All - TBR_Mo/Si - TBR_AlN/Mo

이런식으로 역 추산한다...?

맞아요. 그 식의 **핵심 발상은 “전체로 보이는 열저항에서 기준 샘플의 기여를 빼서, 관심 계면의 기여를 역산한다”**입니다. 다만 네가 쓴 식은 **개념적으로는 맞는 방향**이지만, 실제로는 보통 **저항을 더하는 형태**로 모델링하고, “빼기”는 그 모델의 결과를 해석할 때 쓰는 방식입니다.[^12_1][^12_2]

## 어떻게 생각하면 되나

TDTR에서 많이 쓰는 기본 구조는 이런 식입니다.

$$
R_{total} \approx R_{transducer} + R_{interface,top} + \frac{d_{film}}{\kappa_{film}} + R_{interface,bottom} + R_{substrate}
$$

즉, **Mo/Si**, **AlN/Mo**, **AlN/Si**처럼 여러 항이 직렬로 쌓여 있다고 보는 겁니다.[^12_3][^12_1]

그래서 네가 말한

$$
TBR_{AlN/Si} = TBR_{All} - TBR_{Mo/Si} - TBR_{AlN/Mo}
$$

은 **“전체 유효 TBR에서 알려진 부분을 빼서 AlN/Si만 분리한다”는 개념**으로 이해하면 됩니다.
다만 실제 논문에서는 보통 이렇게 단순히 한 번에 빼기보다, **series resistor model + 두께 시리즈 + reference sample**을 써서 **동시에 피팅**합니다.[^12_4][^12_5][^12_1]

## 네가 이해한 방향이 왜 맞는가

- **기판만 있는 샘플**을 따로 요청하는 이유는, 그 샘플로 **transducer/Si 기여**를 먼저 잡기 위해서입니다.[^12_6][^12_1]
- 그 다음 AlN가 올라간 샘플과 비교하면, **추가된 저항이 AlN층 자체 + 추가 계면**의 효과로 보입니다.[^12_1][^12_4]
- 즉, “기판만 있는 샘플”은 **빼기용 기준선**입니다. 네가 이제 이해한 게 정확합니다.[^12_5][^12_1]


## 다만 주의할 점

네 식을 **그대로 숫자 대입해서 빼는 방식**으로 쓰면 위험합니다. 이유는:

- TDTR은 **계면 하나만 독립적으로 측정**하는 게 아니라, 여러 파라미터가 동시에 신호에 들어갑니다.[^12_7][^12_5]
- 특히 얇은 AlN에서는 **AlN bulk 저항과 AlN/Si 계면저항이 분리되지 않고 묶여 보일 수** 있습니다.[^12_8][^12_1]
- 그래서 실제 보고에서는 보통
**effective thermal resistance** 또는
**combined interface resistance**
로 먼저 추정하고, reference sample과 두께 시리즈로 분해합니다.[^12_4][^12_1]


## 네 실험에 적용하면

네 샘플 세트(75/150/300 nm)에서는 이런 식으로 생각하면 됩니다.

- **Mo/Si 기준 샘플**: $R_{Mo/Si}$ 또는 $R_{Mo/Si}^{eff}$
- **Mo/AlN/Si 샘플**: $R_{Mo/AlN} + R_{AlN} + R_{AlN/Si}$의 합으로 보임
- 차이분을 통해 **AlN 관련 추가 저항**을 역산

즉, 네가 쓰고 싶은 개념은 맞고, 표현만 조금 바꾸면 더 정확합니다.

$$
R_{AlN/Si}^{\;eff}
=
R_{Mo/AlN/Si}^{\;eff}
-
R_{Mo/Si}^{\;eff}
-
R_{AlN/Mo}^{\;eff}
$$

이렇게 **“effective”를 붙여서** 해석하는 게 안전합니다.[^12_5][^12_1]

## 한 줄 결론

네 이해는 맞습니다.
**TDTR에서는 기준 샘플을 이용해 transducer와 기판 기여를 먼저 빼고, 남는 차이를 AlN 관련 계면/막 저항으로 역산하는 방식**으로 생각하면 됩니다. 다만 실제 논문/피팅은 **단순 산술 뺄셈보다 series model 기반의 동시 피팅**이 표준입니다.[^12_1][^12_4][^12_5]

원하면 다음 답변에서 바로
**“Mo transducer 기준 / Al transducer 기준으로 기준샘플이 각각 무엇인지”**를
샘플별 계산 흐름도로 정리해줄게.
<span style="display:none">[^12_10][^12_11][^12_12][^12_13][^12_14][^12_15][^12_16][^12_9]</span>

<div align="center">⁂</div>

[^12_1]: https://pubs.aip.org/aip/apm/article/6/5/058302/1023619/Thermal-conductivity-and-thermal-boundary

[^12_2]: https://pubs.aip.org/aip/jap/article/124/16/161103/1030095/Tutorial-Time-domain-thermoreflectance-TDTR-for

[^12_3]: http://users.mrl.illinois.edu/cahill/tongji_tdtr_fundamentals.pdf

[^12_4]: https://www.sciencedirect.com/science/article/abs/pii/S1359645424005160

[^12_5]: https://www.osti.gov/pages/servlets/purl/2997110

[^12_6]: https://www.scribd.com/document/517816603/1-5046944

[^12_7]: https://arxiv.org/pdf/2103.08084.pdf

[^12_8]: https://patrickehopkins.com/wp-content/uploads/2021/08/hoque2021ab.pdf

[^12_9]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11310922/

[^12_10]: https://pubs.acs.org/doi/10.1021/acsami.3c13418

[^12_11]: https://ddd.uab.cat/pub/tesis/2023/hdl_10803_691097/kaxu1de1.pdf

[^12_12]: https://www.sciencedirect.com/science/article/abs/pii/S0169433223000958

[^12_13]: https://pubs.aip.org/aip/rsi/article/95/10/103006/3316821/An-instrumentation-guide-to-measuring-thermal

[^12_14]: https://www.sciencedirect.com/science/article/abs/pii/S006527172100006X

[^12_15]: https://www.osti.gov/servlets/purl/1109030

[^12_16]: https://patrickehopkins.com/wp-content/uploads/2016/08/2016-sthc_tdtrnometal.pdf


---

# 이렇게 되면 Mo로 Transducer로 지정해서 해도 무방하긴 하겠다.

실측값이 아니라 문헌값에 의존하는 부분이 존재해서 항상 그 값이 무조건 적으로 맞다고 가정하고 넘어가지 않아도 되니

맞습니다. **Mo를 transducer로 쓰는 것 자체는 충분히 가능**하고, 문헌값을 쓰는 것도 TDTR에서 아주 흔한 접근입니다. 다만 그 값들을 **절대값처럼 믿기보다 불확실성을 포함한 입력값**으로 다루는 게 맞습니다.[^13_1][^13_2]

## 왜 가능하냐

- TDTR에서는 transducer의 **열전도도, 비열, 두께, spot size** 같은 입력값이 결과에 들어가지만, 문헌값을 쓰는 것이 일반적입니다.[^13_3][^13_1]
- 실제로 TDTR uncertainty 분석에서는 transducer 열전도도와 두께에 대해 **10% 내외 또는 그 이상**의 불확실성을 가정하는 경우가 많습니다.[^13_2][^13_3]
- 즉, **문헌값 = 정답**이 아니라 **가장 합리적인 prior**로 보는 게 맞습니다.[^13_4][^13_5]


## Mo transducer로 해도 되는 이유

- Mo transducer는 TDTR/NanoTR에서 실제로 사용 사례가 있고, 센터 문서에서도 권장 재질로 제시됩니다.[^13_6][^13_7]
- 따라서 네가 원하는 **Mo/AlN/Si FF 구조**는 충분히 실험 가능한 설계입니다.[^13_1][^13_6]
- 특히 Mo는 센터 측정 조건과 맞으면, 별도 reference를 함께 써서 모델을 안정화할 수 있습니다.[^13_7][^13_6]


## 다만 이렇게 생각해야 함

- **문헌값이 무조건 정확하다고 가정하면 안 됨**.
- 대신 다음처럼 처리해야 합니다.
    - Mo의 κ, ρcp, 두께에 대해 **문헌값 + 오차범위**를 넣는다.[^13_3][^13_4]
    - 가능하면 **실측 두께**만큼은 반드시 측정한다.[^13_8][^13_3]
    - 결과 해석에서 “Mo 물성값 uncertainty 때문에 ±몇 %”를 같이 본다.[^13_5][^13_2]


## 네 경우의 실전 의미

- 네가 **Mo를 transducer로 지정**하면, 해석은 더 깔끔해질 수 있습니다. 왜냐하면 센터 기준과 맞고, FF 구조에서도 충분히 동작하기 때문입니다.[^13_6]
- 동시에, **Mo 자체의 열물성은 완전 고정값이 아니라 모델 입력값**이므로, 문헌값을 써도 됩니다. 다만 그걸 절대 진리처럼 취급하지 말고 **민감도 분석 대상**으로 두면 됩니다.[^13_2][^13_1]


## 한 줄 결론

**네, Mo를 transducer로 써도 무방합니다.**
그리고 문헌값을 쓰는 건 TDTR에서 정상적인 일이며, 중요한 건 그 값을 **무조건 맞다고 두지 않고 불확실성을 포함해 해석하는 것**입니다.[^13_1][^13_2][^13_3]

원하면 다음 답변에서 바로
**“Mo transducer로 갈 때 필요한 입력값 목록(κ, Cp, ρ, thickness, dR/dT, uncertainty)”**를
체크리스트 형태로 정리해줄게.
<span style="display:none">[^13_10][^13_11][^13_12][^13_13][^13_14][^13_15][^13_16][^13_9]</span>

<div align="center">⁂</div>

[^13_1]: https://pubs.aip.org/aip/jap/article/124/16/161103/1030095/Tutorial-Time-domain-thermoreflectance-TDTR-for

[^13_2]: https://www.osti.gov/pages/servlets/purl/2997110

[^13_3]: https://arxiv.org/pdf/1704.02358.pdf

[^13_4]: https://s-space.snu.ac.kr/bitstream/10371/210086/1/000000183259.pdf

[^13_5]: https://www.rsc.org/suppdata/d4/ta/d4ta03644a/d4ta03644a1.pdf

[^13_6]: NanoTRsiryogyugyeog.pdf

[^13_7]: https://pmc.ncbi.nlm.nih.gov/articles/PMC12261518/

[^13_8]: https://pubs.aip.org/aip/rsi/article/83/11/114902/357282/Interpreting-picosecond-acoustics-in-the-case-of

[^13_9]: http://arxiv.org/abs/1511.04852

[^13_10]: https://pubs.acs.org/doi/10.1021/acsami.3c13418

[^13_11]: https://repositories.lib.utexas.edu/server/api/core/bitstreams/510da89a-977f-4c9f-9762-db470efc997c/content

[^13_12]: https://www.osti.gov/servlets/purl/1109030

[^13_13]: https://www.scribd.com/document/517816603/1-5046944

[^13_14]: https://www.scribd.com/document/680536371/time-domain-thermoreflectance-TDTR-data-analysis-using-phonon-hydrodynamic-model

[^13_15]: https://patrickehopkins.com/wp-content/uploads/2021/08/hoque2021ab.pdf

[^13_16]: https://nanoheat.stanford.edu/wp-content/uploads/2022/01/Thermal-Characterization-of-Metal−Oxide-Interfaces-Using-TimeDomain-Thermoreflectance-with-Nanograting-Transducers.pdf


---

# 아니 RF로 해도 될듯해

좋아요. **RF로 가도 됩니다.** 지금 네가 정리한 구조가 **투명 기판 기반의 rear heating/front detection** 조건과 맞고, 하이브리드 본딩 계면처럼 **buried interface의 열특성**을 보려는 의도라면 RF가 오히려 더 자연스러울 수 있어요.

## 왜 RF가 맞을 수 있나

- RF는 **기판 뒤에서 가열하고, 박막 전면에서 검출**하는 방식이라 buried interface 쪽 해석에 적합합니다.
- 네가 말한 **Mo/AlN/Si 상부 transducer 구조**에 얽매이지 않고, 샘플 구성 자체를 RF에 맞게 다시 잡을 수 있습니다.
- 특히 **ITR/TBR를 특정 계면으로 분리해 보려는 목적**이 있으면 RF용 샘플 세트가 더 논리적일 수 있습니다.


## 다만 바로 확인할 것

- RF는 보통 **투명 기판 또는 DSP-Si(고저항)** 같은 조건이 중요합니다.
- 일반 Si(100) 위에 그냥 올린 구조는 RF 설계와 잘 안 맞을 수 있습니다.
- 따라서 지금은 먼저 **네 샘플이 RF용으로 실제 가능한 기판/두께/측정면 조건인지**를 다시 정리해야 합니다.


## 다음 단계

네가 원하면 내가 바로

1. **RF 기준으로 샘플 구조를 다시 정리**하고,
2. **AlN 75/150/300 nm에서 무엇이 측정되는지**,
3. **Mo vs Al transducer를 RF에서 어떻게 볼지**
까지 한 번에 정리해줄게.

---

# RF 모드로도 Si/AlN 계면간 열저항 열전도도를 추측할 수 있는지를 확인해줘 이 부분만 해결되면 모든게 해결돼

**아니요. 첨부된 NanoTR의 표준 RF 시료 구성으로는 ‘직접 접촉한 AlN/Si 계면’의 TBR을 측정할 수 없습니다.** RF 구성에서는 AlN과 Si 사이에 **후면 금속막이 들어가므로**, 관심 계면인 AlN/Si가 없어지고 **AlN/금속 계면**으로 바뀝니다.[^15_1]

이 점이 지금까지 계속 걸렸던 핵심이고, 망설인 것이 맞았습니다.

## RF 구조를 정확히 보면

첨부 자료의 RF 구조는 다음입니다.

$$
\text{Top metal} / \text{AlN (measuring object)} / \text{Bottom metal} / \text{transparent Si substrate}
$$

- 뒤쪽에서 입사한 pump는 투명 Si를 통과해 **bottom metal**에서 흡수·가열됩니다.
- 열은 bottom metal → AlN → top metal 방향으로 흐릅니다.
- 위쪽 top metal의 반사율 변화로 온도를 검출합니다.
- 따라서 RF에서 열저항에 들어가는 계면은 대략

$$
R_{\mathrm{bottom\,metal/AlN}},\quad
R_{\mathrm{top\,metal/AlN}}
$$

이고, **AlN/Si는 구조상 존재하지 않습니다.**[^15_2][^15_3][^15_1]

첨부자료에 RF는 substrate 정보가 필요 없다고 되어 있는 이유도 여기에 있습니다. 열전달의 핵심 경로가 substrate가 아니라, **후면 금속막부터 상부 검출 금속막까지의 stack**이기 때문입니다.[^15_1]

## 네 목표별 판단

| 목표 | 적합한 구조 | RF 가능 여부 |
| :-- | :-- | :-- |
| **직접 성장된 AlN/Si 계면의 TBR** | Mo(or Al)/AlN/Si | 표준 RF 구조로는 불가 |
| Mo/AlN 또는 Al/AlN 계면의 TBR | Mo/AlN/Mo/Si 또는 Al/AlN/Al/Si | 가능 |
| AlN 박막의 cross-plane 열확산도 | RF용 metal/AlN/metal/transparent substrate | 가능 |
| AlN/Si를 포함한 유효 열저항 또는 AlN $k_\perp$ | Mo(or Al)/AlN/Si | FF가 적합 |

## AlN/Si 계면이 목적이면

네가 유지해야 할 실제 구조는 다음입니다.

$$
\text{Mo (100–120 nm)} / \text{AlN (75,150,300 nm)} / \text{Si(100)}
$$

또는 문헌 비교용으로

$$
\text{Al (100–120 nm)} / \text{AlN (75,150,300 nm)} / \text{Si(100)}
$$

이 구조는 **AlN/Si 계면을 그대로 유지**하므로, 알맞은 것은 **FF mode**입니다. FF에서는 top metal이 heater/thermometer로 기능하고, 열이 아래로 흘러 실제 AlN/Si 계면을 통과합니다.[^15_2][^15_1]

해석 모델은 다음과 같습니다.

$$
R_{\mathrm{measured}}
=
R_{\mathrm{M/AlN}}
+
\frac{t_{\mathrm{AlN}}}{k_{\mathrm{AlN},\perp}}
+
R_{\mathrm{AlN/Si}}
+
R_{\mathrm{Si,spreading}}
$$

여기서 관심값은 $R_{\mathrm{AlN/Si}}$입니다. Mo/AlN 또는 Al/AlN 계면은 **제거되는 값이 아니라, 모델에서 별도 항으로 넣어 보정해야 하는 값**입니다.[^15_4][^15_5]

## 75/150/300 nm가 필요한 이유

세 두께는 단순 반복 샘플이 아니라 $R_{\mathrm{AlN/Si}}$와 AlN 내부 열저항을 나누기 위한 핵심 설계입니다.

$$
R_{\mathrm{stack}}
\approx
R_{\mathrm{M/AlN}}
+
R_{\mathrm{AlN/Si}}
+
\frac{t_{\mathrm{AlN}}}{k_{\mathrm{AlN},\perp}}
$$

- 세 시료가 같은 성장 조건·동일한 계면 품질을 가진다고 가정하면, 두께에 따라 변하는 항은 주로 $t_{\mathrm{AlN}}/k_{\mathrm{AlN},\perp}$입니다.
- 두께가 0에 가까울 때의 절편에는 계면항들이 남습니다.
- 그러나 절편은 원칙적으로 $R_{\mathrm{M/AlN}}+R_{\mathrm{AlN/Si}}$이므로, **AlN/Si만 단독으로 분리하려면 M/AlN 계면을 독립적으로 constrain하거나 알려진 값으로 둘 근거가 필요**합니다. TDTR은 여러 미지 파라미터가 서로 연동될 수 있으므로 이 분리가 실험 설계의 관건입니다.[^15_5][^15_4]


## 최종 권고

네 연구 의도가 **“sputtered AlN과 Si(100) 사이의 실제 계면 열저항”**이라면:

- **RF 표준 구조는 선택하지 마세요.** 후면 금속막이 AlN/Si 계면을 대체합니다.
- **FF: Mo/AlN/Si**로 진행하세요.
- AlN 75/150/300 nm 세트는 유지하세요.
- Mo를 쓸 경우, bare Si 위에 같은 조건의 **Mo/Si 기준 샘플**도 준비하세요. 이는 Mo film의 열물성 및 Mo/Si 기준 응답을 잡는 데 유용하지만, 그것을 단순히 AlN/Si TBR에서 빼는 것이 아니라 multilayer fitting의 제약조건으로 활용하는 쪽이 더 타당합니다.
- 가능하면 **Al/AlN/Si 세트도 보조 비교군**으로 두세요. Al은 TDTR 문헌의 표준 transducer라 모델·문헌 비교가 수월합니다.[^15_4][^15_5]

즉, **RF는 AlN 자체 또는 metal/AlN 계면을 정밀하게 보기 위한 구조이고, 네가 보려는 “직접 AlN/Si 계면”을 보존하려면 FF가 맞습니다.**
<span style="display:none">[^15_10][^15_11][^15_12][^15_13][^15_14][^15_15][^15_16][^15_17][^15_18][^15_6][^15_7][^15_8][^15_9]</span>

<div align="center">⁂</div>

[^15_1]: NanoTRsiryogyugyeog.pdf

[^15_2]: https://analyzing-testing.netzsch.com/fr/produits/analyseur-de-thermoreflectance-domaine-temporel-tdtr/nanotr

[^15_3]: https://analyzing-testing.netzsch.com/_Resources/Persistent/0/b/6/8/0b68b09563c8f408d9019b3f2e77c5357bfd2d22/Thermoreflectance.pdf

[^15_4]: https://pubs.aip.org/aip/jap/article/124/16/161103/1030095/Tutorial-Time-domain-thermoreflectance-TDTR-for

[^15_5]: https://www.osti.gov/pages/servlets/purl/2997110

[^15_6]: https://analyzing-testing.netzsch.com/_Resources/Persistent/3/4/1/2/341225391139cd1ce20fd22ccca8496a0ff05ea1/OnSet_26_en_web.pdf

[^15_7]: https://analyzing-testing.netzsch.com/en/blog/2023/nanotr-span-span-nbsp-and-picotr-nbsp-span-span-instrument-line-for-the-thermal-characterization-of-thin-layers

[^15_8]: https://analyzing-testing.netzsch.com/ko/products/sigan-domein-deomobansayul-bunseoggi-tdtr/nanotr-picotr

[^15_9]: https://analyzing-testing.netzsch.com/ru/application-literature/izmereniia-teplovoi-effuzii-na-tonkoi-plenke-pedot-pss-po-sredstvamnanotr

[^15_10]: https://analyzing-testing.netzsch.com/hu/application-literature/thermal-effusivity-measures-on-pedot-pss-thin-film-by-means-of-nanotr

[^15_11]: https://analyzing-testing.netzsch.com/pl/application-literature/pomiary-wydajnosci-cieplnej-na-cienkiej-folii-pedot-pss-za-pomoca-srodkow-nanotr

[^15_12]: https://analyzing-testing.netzsch.com/ko/application-literature/pedoteu-pss-bagmag-sudanbyeol-yeol-hyoyul-ceugjeongnanotr

[^15_13]: https://analyzing-testing.netzsch.com/ko/beulrogeu/2023/nanotr-yalbeun-ceungyi-yeol-teugseonghwareul-wihan-seupaen-seupaen-seupaen-gyeceuggi-rain-picotr-nbsp-span-span-instrument-line-for-the-thermal-characterization-of-thin-layers

[^15_14]: https://analyzing-testing.netzsch.com/id/blog/2023/nanotr-bentang-bentang-dan-picotr-bentang-bentang-bentang-instrumen-untuk-karakterisasi-termal-lapisan-tipis

[^15_15]: http://www.pico-therm.com/pdf/MST0957-0233_22_2_024012.pdf

[^15_16]: https://analyzing-testing.netzsch.com/_Resources/Persistent/4/b/a/0/4ba07430dd66702c2f0e7aeb83ca919d6af14b5f/AN%20273_Thermal-Diffusivity-Measurements-on%20PEDOT_PSS-Thin%20Film-by-Means-of-NanoTR-English.pdf

[^15_17]: https://analyzing-testing.netzsch.com/de/produkte/time-domain-thermoreflectance-analyzer-tdta/nanotr

[^15_18]: https://www.pico-therm.com/english/product/index.html


---

# AlN 혹은 AlN/Si의 경우 Rtot에 해당하는 부분이 TBRAlN/Si 이걸로 반영해야한다고 난 이해하는데 내가 잘못 이해한거면 논문들을 찾아서 정확한 정보를 알려줘

결론부터 말하면, 네 식 자체는 맞습니다. 다만 **AlN/Si 시료에서 $R_{\mathrm{tot}}$을 곧바로 $TBR_{\mathrm{AlN/Si}}$ 하나로 두는 것은 일반적으로 맞지 않습니다.** 그 식이 나타내는 $R_{\mathrm{tot}}$은 “AlN의 bulk 열저항 외에, 유효 열전도도에 함께 접혀 들어간 모든 직렬 열저항”입니다.[^16_1]

$$
k_{\mathrm{eff}}
=
\frac{k_i}{1+\dfrac{k_i R_{\mathrm{tot}}}{d}}
$$

이는 다음 식을 정리한 것입니다.

$$
\frac{d}{k_{\mathrm{eff}}}
=
\frac{d}{k_i}+R_{\mathrm{tot}}
$$

여기서 $d$는 AlN 두께, $k_i$는 계면 영향을 제거한 intrinsic AlN cross-plane 열전도도입니다.

## AlN/Si에서 $R_{\mathrm{tot}}$의 의미

FF-TDTR 시료가 예를 들어

$$
\mathrm{Mo}/\mathrm{AlN}/\mathrm{Si}
$$

이면, 열이 통과하는 직렬 경로는 다음입니다.

$$
\mathrm{Mo}
\rightarrow
\boxed{\mathrm{Mo/AlN}}
\rightarrow
\mathrm{AlN}
\rightarrow
\boxed{\mathrm{AlN/Si}}
\rightarrow
\mathrm{Si}
$$

따라서 AlN을 하나의 “유효 열전도도 층”으로 묶어 표현한다면,

$$
R_{\mathrm{tot}}
\approx
R_{\mathrm{Mo/AlN}}
+
R_{\mathrm{AlN/Si}}
+
R_{\mathrm{interlayer}}
$$

입니다.

여기서 $R_{\mathrm{interlayer}}$는 AlN nucleation layer, native oxide, SiN$_x$, AlO$_x$, 산소가 많은 반응층, 조성 변화층처럼 TEM에서는 수 nm로 보이거나 거의 보이지 않을 수 있는 계면 전이영역의 저항을 포함할 수 있습니다.

즉,

$$
\boxed{
R_{\mathrm{tot}}\neq R_{\mathrm{AlN/Si}}
}
$$

가 기본입니다.

## 언제 $R_{\mathrm{tot}} \approx TBR_{\mathrm{AlN/Si}}$인가

아래 조건을 **모두** 만족할 때만 근사적으로 그렇게 둘 수 있습니다.

- Mo/AlN 계면 열저항이 충분히 작거나, 독립적으로 알고 있다.
- AlN/Si 계면 이외에 nucleation layer·산화층·반응층이 무시 가능하다.
- $k_i$가 별도 두꺼운 AlN 시료 등으로 이미 확보되어 있다.
- 측정 신호의 sensitivity가 AlN/Si 계면에 충분히 크다.

이때는

$$
R_{\mathrm{tot}}
\approx
R_{\mathrm{AlN/Si}}
$$

라고 쓸 수 있지만, 논문에서는 보통 **가정 또는 모델 제약조건**으로 명확히 적어야 합니다.

## AlN/Si TDTR 논문은 어떻게 했나

최근 AlN/Si TDTR 연구는 Al transducer / AlN / Si라는 다층 구조에서 **Al/AlN 계면과 AlN/Si 계면을 별도 TBC로 모델에 넣어 피팅**했습니다. 즉, AlN/Si 계면만을 $R_{\mathrm{tot}}$으로 두지 않았습니다.[^16_2]

그 논문에서 사용한 구조는 실질적으로 다음과 같습니다.

$$
\mathrm{Al}/\mathrm{AlN}/\mathrm{Si}
$$

그리고 피팅한 주요 물성은:

- $k_{\mathrm{AlN}}$
- $G_{\mathrm{Al/AlN}}$
- $G_{\mathrm{AlN/Si}}$

입니다. 이 논문은 Al/AlN TBC를 약 288–357 MW m$^{-2}$ K$^{-1}$, AlN/Si TBC를 약 95 MW m$^{-2}$ K$^{-1}$로 별도로 추출했습니다. 즉, 열저항으로 보면:

$$
R_{\mathrm{Al/AlN}}=\frac{1}{G_{\mathrm{Al/AlN}}}
$$

$$
R_{\mathrm{AlN/Si}}=\frac{1}{G_{\mathrm{AlN/Si}}}
$$

로 서로 다른 항입니다.[^16_2]

또 다른 sputtered AlN/Si TDTR 연구도 100 nm–1.7 μm AlN에서 **Al/AlN 계면 $G_1$** 및 **AlN/Si 계면 $G_2$** 를 분리해 다층 3D heat-diffusion model에 넣었습니다. 특히 100 nm AlN에서는 **Al/AlN과 AlN/Si 두 계면이 모두 TDTR 신호에 크게 기여**한다고 명시합니다.[^16_1]

## 네 75/150/300 nm 시료에 대입

네가 계획한 구조가 Mo/AlN/Si이면, 각각의 유효 열저항은 우선 다음처럼 봐야 합니다.

$$
R_{\mathrm{eff}}(d)
=
R_{\mathrm{Mo/AlN}}
+
\frac{d}{k_{\mathrm{AlN},\perp}}
+
R_{\mathrm{AlN/Si}}
$$

따라서 식에 넣는 $R_{\mathrm{tot}}$은, 최소한,

$$
\boxed{
R_{\mathrm{tot}}
=
R_{\mathrm{Mo/AlN}}
+
R_{\mathrm{AlN/Si}}
}
$$

입니다.

AlN 내부에 저열전도 nucleation layer가 있다면 더 정확한 표현은:

$$
R_{\mathrm{eff}}(d)
=
R_{\mathrm{Mo/AlN}}
+
\frac{d_{\mathrm{cryst}}}{k_{\mathrm{cryst}}}
+
\frac{d_{\mathrm{nuc}}}{k_{\mathrm{nuc}}}
+
R_{\mathrm{AlN/Si}}
$$

입니다.

이 경우 nucleation layer를 AlN bulk와 구분하지 않고 한 개의 $k_{\mathrm{eff}}$로 표현하면, 그 영향도 $R_{\mathrm{tot}}$ 혹은 낮아진 $k_i$에 혼입됩니다.

## 두께 의존성으로 분리하는 법

같은 공정·같은 계면 조건의 75, 150, 300 nm 시료에서 면적 정규화 열저항을 두께에 대해 그리면:

$$
R_{\mathrm{eff}}(d)
=
\frac{d}{k_{\mathrm{AlN},\perp}}
+
R_{\mathrm{interface,combined}}
$$

- **기울기**:

$$
\frac{1}{k_{\mathrm{AlN},\perp}}
$$

- **$d=0$ 절편**:

$$
R_{\mathrm{interface,combined}}
=
R_{\mathrm{Mo/AlN}}+R_{\mathrm{AlN/Si}}
$$

입니다.

따라서 두께 시리즈만으로는 원칙적으로:

$$
R_{\mathrm{Mo/AlN}}+R_{\mathrm{AlN/Si}}
$$

까지만 안정적으로 얻고, **AlN/Si 단독 TBR을 얻으려면 Mo/AlN TBR을 별도로 알아야 합니다.**

## 정확한 표현

네 연구에서 아래처럼 쓰면 안전합니다.

- **직접 피팅값**: $G_{\mathrm{Mo/AlN}}$, $k_{\mathrm{AlN},\perp}$, $G_{\mathrm{AlN/Si}}$
- **두께 의존 유효값**:

$$
R_{\mathrm{interface,combined}}
=
R_{\mathrm{Mo/AlN}}+R_{\mathrm{AlN/Si}}
$$
- **단순 유효 열전도도 모델**:

$$
k_{\mathrm{eff}}
=
\frac{k_{\mathrm{AlN}}}
{1+\dfrac{k_{\mathrm{AlN}}(R_{\mathrm{Mo/AlN}}+R_{\mathrm{AlN/Si}})}{d}}
$$

그리고 $R_{\mathrm{Mo/AlN}}$을 충분히 작다고 놓거나 독립 측정값으로 고정했을 때에만:

$$
R_{\mathrm{tot}}
\approx
R_{\mathrm{AlN/Si}}
$$

라고 단순화할 수 있습니다.[^16_1][^16_2]
<span style="display:none">[^16_10][^16_11][^16_12][^16_13][^16_14][^16_15][^16_16][^16_3][^16_4][^16_5][^16_6][^16_7][^16_8][^16_9]</span>

<div align="center">⁂</div>

[^16_1]: https://kummelgroup.ucsd.edu/pubs/papers_2023/Perex%20Mcleod%20AlN%20Thermal%20Conductivity%20ACS%20Nano%202023.pdf

[^16_2]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11044587/

[^16_3]: image.jpg

[^16_4]: https://arxiv.org/pdf/2503.05084.pdf

[^16_5]: https://www.sfu.ca/~mbahrami/pdf/pdf/2016/An improved transient plane source method for measuring thermal conductivity of thin films Deconvoluting thermal contact resistance.pdf

[^16_6]: https://patrickehopkins.com/wp-content/uploads/2016/08/2017-interpack_hopkins_present.pdf

[^16_7]: https://mfint.imp.kiev.ua/en/abstract/v44/i08/0989.html

[^16_8]: https://nanoheat.stanford.edu/wp-content/uploads/2013/09/Cho-et-al..pdf

[^16_9]: https://feng.mech.utah.edu/wp-content/uploads/sites/152/2024/06/paper-and-correction.pdf

[^16_10]: https://www.acsmaterial.com/blog-detail/interfacial-thermal-resistance.html

[^16_11]: https://pubs.acs.org/doi/10.1021/acsaelm.4c00068

[^16_12]: https://pubs.aip.org/aip/jap/article-pdf/doi/10.1063/5.0245381/20429173/095105_1_5.0245381.pdf

[^16_13]: https://pubs.acs.org/doi/abs/10.1021/acsami.8b07014

[^16_14]: https://dr.ntu.edu.sg/handle/10356/166521

[^16_15]: https://patrickehopkins.com/wp-content/uploads/2021/08/hoque2021ab.pdf

[^16_16]: http://kummelgroup.ucsd.edu/pubs/papers_2024/thermal-transport-at-the-aln-sic-interface-and-grain-boundary-of-aln.pdf


---

# Interlayer thermal resistivity 조사는 RF 모드에서만 가능하다는 것 때문에 AlN/Si 측정을 의도해도 불가능하다는 부분이 이해가 안되고 두 수식을 정리해서 TBR AlN/Si 식도 나올거 같은데 아닌가?

네가 쓴 **저항의 직렬합 원리 자체는 맞고**, 조건만 충족되면 수식을 정리해서 $TBR_{\mathrm{AlN/Si}}$를 구할 수 있습니다. 내가 앞에서 “RF라서 AlN/Si 측정이 불가능하다”고 한 말은 더 정확히 말하면 **아주대 NanoTR가 제시한 표준 RF 시료 구조로는 직접 AlN/Si 계면을 보존할 수 없다**는 뜻입니다. RF라는 물리 원리 자체가 AlN/Si TBR을 절대 측정하지 못한다는 뜻은 아닙니다.[^17_1][^17_2]

## 수식의 핵심

네가 제시한 유효 열전도도 식은 다음의 직렬 저항식에서 나옵니다.

$$
\frac{d_{\mathrm{AlN}}}{k_{\mathrm{eff}}}
=
\frac{d_{\mathrm{AlN}}}{k_{\mathrm{AlN}}}
+
R_{\mathrm{tot}}
$$

$$
k_{\mathrm{eff}}
=
\frac{k_{\mathrm{AlN}}}
{1+\dfrac{k_{\mathrm{AlN}}R_{\mathrm{tot}}}{d_{\mathrm{AlN}}}}
$$

여기서 $R_{\mathrm{tot}}$은 **AlN bulk 열저항 외에 유효 $k$ 안으로 접혀 들어간 직렬 저항의 총합**입니다.

실제 네가 원하는 FF 시료가

$$
\mathrm{Mo}/\mathrm{AlN}/\mathrm{Si}
$$

이면, 이상적인 1D 면적정규화 저항 모델은:

$$
R_{\mathrm{stack}}
=
R_{\mathrm{Mo/AlN}}
+
\frac{d_{\mathrm{AlN}}}{k_{\mathrm{AlN},\perp}}
+
R_{\mathrm{AlN/Si}}
$$

입니다.

그러므로 **AlN/Si TBR을 구하는 올바른 정리식**은:

$$
\boxed{
R_{\mathrm{AlN/Si}}
=
R_{\mathrm{stack}}
-
R_{\mathrm{Mo/AlN}}
-
\frac{d_{\mathrm{AlN}}}{k_{\mathrm{AlN},\perp}}
}
$$

입니다.

즉, 수식적으로는 네 말이 맞습니다. 단, $R_{\mathrm{Mo/AlN}}$과 $k_{\mathrm{AlN},\perp}$를 독립적으로 알거나, 다층 TDTR 모델에서 충분히 constrain할 수 있어야 합니다.[^17_3][^17_4]

## Mo/Si를 빼면 안 되는 이유

아래 식은 일반적으로 맞지 않습니다.

$$
R_{\mathrm{AlN/Si}}^{\mathrm{eff}}
=
R_{\mathrm{Mo/AlN/Si}}^{\mathrm{eff}}
-
R_{\mathrm{Mo/Si}}^{\mathrm{eff}}
-
R_{\mathrm{AlN/Mo}}^{\mathrm{eff}}
$$

이유는 **Mo/AlN/Si stack 안에 Mo/Si 계면이 존재하지 않기 때문**입니다.

$$
\mathrm{Mo}/\mathrm{AlN}/\mathrm{Si}
$$

에 실제로 존재하는 계면은:

- Mo/AlN
- AlN/Si

뿐입니다.

따라서 Mo/Si 기준 샘플은 $R_{\mathrm{Mo/Si}}$을 구하는 용도가 아니라, 주로 아래를 확인하는 **reference** 역할입니다.

- Mo film의 실제 열확산도 또는 열전도도
- Mo film 두께 및 금속막 품질
- Mo/Si 기준 응답과 장비·모델의 재현성
- Mo transducer 자체의 불확실성 범위

Mo/Si 계면은 Mo/AlN/Si 시료의 직렬 열경로에 없으므로, target TBR 계산에서 기계적으로 빼면 **없는 계면을 한 번 빼는 셈**이 됩니다.

## 네 식이 성립하려면

네가 생각한 “전체값 − reference들” 방식은 아래처럼 **실제로 모든 저항이 동일한 열경로에 직렬로 존재할 때**만 성립합니다.

$$
\mathrm{Mo}/\mathrm{AlN}/\mathrm{Mo}/\mathrm{Si}
$$

이 구조라면:

$$
R_{\mathrm{stack}}
=
R_{\mathrm{Mo(top)/AlN}}
+
\frac{d_{\mathrm{AlN}}}{k_{\mathrm{AlN}}}
+
R_{\mathrm{AlN/Mo(bottom)}}
+
R_{\mathrm{Mo/Si}}
$$

그래서 이 경우에는:

$$
R_{\mathrm{AlN/Mo(bottom)}}
=
R_{\mathrm{stack}}
-
R_{\mathrm{Mo(top)/AlN}}
-
\frac{d_{\mathrm{AlN}}}{k_{\mathrm{AlN}}}
-
R_{\mathrm{Mo/Si}}
$$

처럼 역산할 수 있습니다.

하지만 여기서는 **AlN과 Si가 맞닿아 있지 않습니다.** 따라서 이 RF stack으로 얻는 것은 $TBR_{\mathrm{AlN/Si}}$가 아니라 **AlN/Mo 계면 TBR**입니다. 첨부한 NanoTR RF 그림이 바로 이런 방식입니다: top metal / measuring object / bottom metal / transparent substrate.[^17_1]

## RF와 AlN/Si의 관계

정리하면 다음과 같습니다.


| 질문 | 답 |
| :-- | :-- |
| RF가 ITR을 측정할 수 있는가? | 가능 |
| RF에서 모든 계면 ITR을 측정할 수 있는가? | 아니다. **실제 RF stack에 포함된 계면**만 가능 |
| NanoTR 표준 RF에서 AlN/Si TBR을 구할 수 있는가? | 아니다. AlN–Si 사이에 rear metal이 삽입됨 |
| Mo/AlN/Si에서 AlN/Si TBR을 보려면? | AlN/Si 계면을 보존한 **FF 구조**가 적합 |
| FF에서는 interface fitting이 불가능한가? | 아니다. 일반 TDTR 문헌은 FF형 metal/film/substrate stack에서 film κ와 buried interface TBC를 함께 다층 열확산 모델로 피팅한다. [^17_3][^17_4] |

첨부된 NanoTR 안내서는 RF에서 “ITR 측정”을 명시하지만, 이는 RF 시료 안에 있는 **metal/measuring-object 계면의 ITR**을 뜻합니다. 자료의 RF 레이어는 metal / measuring object / metal / substrate이고, 따라서 AlN이 measuring object라면 target interface는 AlN/Si가 아니라 AlN/metal입니다.[^17_1]

## Mo/AlN/Si에 적용한 정답

네 목적이 **sputtered AlN과 Si(100)가 직접 접촉한 실제 성장 계면의 $TBR_{\mathrm{AlN/Si}}$** 이라면, 목표 구조는 계속:

$$
\boxed{
\mathrm{Mo}(100\text{–}120\,\mathrm{nm})/
\mathrm{AlN}(75,150,300\,\mathrm{nm})/
\mathrm{Si}(100)
}
$$

입니다.

그리고 해석 목표는:

$$
\boxed{
R_{\mathrm{Mo/AlN}}
,\quad
k_{\mathrm{AlN},\perp}
,\quad
R_{\mathrm{AlN/Si}}
}
$$

입니다. 75/150/300 nm 두께 시리즈는 바로 이 세 항 중 **두께 비례 AlN bulk 항**과 **두께 비의존 계면항**을 분리하기 위한 유효한 설계입니다. 다만 두께 시리즈만으로는 원칙적으로 절편이

$$
R_{\mathrm{Mo/AlN}}+R_{\mathrm{AlN/Si}}
$$

로 나오므로, $R_{\mathrm{AlN/Si}}$만 단독으로 주장하려면 Mo/AlN 계면을 별도 reference, 문헌 기반 prior, 혹은 다층 fitting sensitivity로 제한해야 합니다.[^17_2][^17_4]

**따라서 네 수식 방향은 맞지만, RF 구조에 넣으면 target 계면이 AlN/Si가 아니라 AlN/Mo로 바뀐다는 점이 결정적 차이입니다.**
<span style="display:none">[^17_5][^17_6][^17_7]</span>

<div align="center">⁂</div>

[^17_1]: NanoTRsiryogyugyeog.pdf

[^17_2]: https://pubs.aip.org/aip/jap/article/124/16/161103/1030095/Tutorial-Time-domain-thermoreflectance-TDTR-for

[^17_3]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11044587/

[^17_4]: https://kummelgroup.ucsd.edu/pubs/papers_2023/Perex%20Mcleod%20AlN%20Thermal%20Conductivity%20ACS%20Nano%202023.pdf

[^17_5]: image.jpg

[^17_6]: image-2.jpg

[^17_7]: image-3.jpg


---

# Rear thermal Front probe로 안된다고....? 무조건 Front thermal front Probe로 분석해야한다?

**네가 목표로 하는 “직접 접촉된 AlN/Si 계면”의 TBR이라면, 첨부된 아주대 NanoTR 표준 시료 규격에서는 FF로 분석해야 합니다.** RF가 물리적으로 절대 불가능해서가 아니라, **센터가 제시한 RF 시료 구조가 AlN과 Si 사이에 후면 metal film을 넣는 구조이기 때문**입니다.[^18_1]

## RF에서 왜 문제가 되나

센터의 RF 표준 구조는 다음입니다.

$$
\text{Top metal}
/
\text{Measuring object}
/
\text{Rear metal}
/
\text{transparent substrate}
$$

AlN을 measuring object로 놓고 Si를 substrate로 쓰면:

$$
\text{Mo(top)}
/
\text{AlN}
/
\text{Mo(rear)}
/
\text{Si}
$$

가 됩니다.

그러면 원래 원하는 계면인

$$
\text{AlN}/\text{Si}
$$

가 없어지고,

$$
\text{AlN}/\text{Mo(rear)}
$$

가 생깁니다. 따라서 RF로 얻는 ITR은 AlN/Si가 아니라 **AlN/rear-Mo 계면의 ITR**입니다.[^18_1]

## FF에서는 왜 가능한가

FF 구조는 다음과 같습니다.

$$
\text{Mo(top)}
/
\text{AlN}
/
\text{Si}
$$

pump와 probe가 모두 top Mo에서 작동하고, 열은 아래 방향으로 흘러:

$$
\mathrm{Mo}
\rightarrow
\mathrm{AlN}
\rightarrow
\boxed{\mathrm{AlN/Si}}
\rightarrow
\mathrm{Si}
$$

를 지나갑니다.

따라서 AlN/Si가 실제 열전달 경로에 남아 있고, 다층 열전달 모델에서 $R_{\mathrm{Mo/AlN}}$, $d_{\mathrm{AlN}}/k_{\mathrm{AlN}}$, $R_{\mathrm{AlN/Si}}$를 포함해 피팅할 수 있습니다. Al/AlN/Si 구조의 기존 TDTR 연구들도 이 방식으로 AlN 열전도도와 buried AlN/Si TBC를 모델링합니다.[^18_2][^18_3]

## 정확한 답

- **RF가 전혀 안 된다** → 아닙니다. RF는 가능하고, ITR 분석 자체에도 적합합니다.
- **RF로 AlN/Si TBR을 표준 시료 구성 그대로 구할 수 있다** → 아닙니다. rear metal이 AlN/Si 직접계면을 대체합니다.
- **현재 목표가 direct AlN/Si TBR이면 FF가 사실상 맞다** → 맞습니다.
- **RF로 보려면** → target을 AlN/Si가 아니라 **AlN/Mo 또는 AlN/Al 계면**으로 바꾸게 됩니다.[^18_1]


## 예외 가능성

Si 기판 측에서 pump를 입사시키되 **AlN/Si 사이에 rear metal을 넣지 않는 custom RF 구조**를 장비 담당자가 허용하고, Si를 통한 광흡수·열발생 위치·probe 검출 조건을 별도 모델로 구축한다면 원리적으로 검토할 여지는 있습니다. 하지만 이것은 첨부된 NanoTR의 **표준 RF ITR 프로토콜이 아니며**, 지금 자료만으로 “AlN/Si TBR을 정량 추출 가능하다”고 보장할 수 없습니다.[^18_1]

따라서 센터 의뢰 시에는 이렇게 확인하는 것이 가장 정확합니다.

> “Mo/AlN/Si에서 direct AlN/Si 계면 TBR이 목표입니다. RF mode에서 rear metal 없이 Si substrate 측 pump heating이 가능한지, 그리고 AlN/Si TBR을 단독 fitting parameter로 설정할 수 있는지 확인 부탁드립니다.”

센터가 **rear metal 필수**라고 답하면, 네 목표에는 **FF**가 맞습니다.

<div align="center">⁂</div>

[^18_1]: NanoTRsiryogyugyeog.pdf

[^18_2]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11044587/

[^18_3]: https://kummelgroup.ucsd.edu/pubs/papers_2023/Perex%20Mcleod%20AlN%20Thermal%20Conductivity%20ACS%20Nano%202023.pdf


---

# NanoTR의 표준 RF ITR 프로토콜로만 적용하실거 같아... 문의만 해볼게... 이 부분은

좋은 판단입니다. **센터가 표준 RF ITR 프로토콜만 적용한다면, 먼저 “그 프로토콜에서 AlN/Si 직접 계면이 유지되는지”를 확인하는 것이 최우선**입니다. 첨부된 시료 규격만 보면 RF 구조에는 rear metal이 포함되어 있어, 기본적으로 측정 대상 계면은 AlN/Si가 아니라 AlN/rear-metal이 될 가능성이 높습니다.[^19_1]

센터에 아래처럼 문의하면 됩니다.

> 안녕하세요. NanoTR RF mode의 ITR 분석 가능 여부를 문의드립니다.
>
> 측정 목표는 Si(100) 위에 증착한 AlN 박막의 **direct AlN/Si 계면 열저항(TBR 또는 ITR)** 입니다.
>
> 계획 중인 기본 시료는 Mo(100–120 nm)/AlN(75, 150, 300 nm)/Si(100) 구조입니다.
>
> 제공해 주신 RF mode 시료 구조에는 measuring object와 transparent substrate 사이에 rear metal film이 포함되어 있는 것으로 이해했습니다. 이 경우 AlN/Si direct interface 대신 AlN/rear-metal interface가 형성될 것으로 보입니다.
>
> 1. RF 표준 ITR 프로토콜에서 **rear metal 없이 Mo/AlN/Si 구조를 그대로 사용하여 AlN/Si TBR을 fitting parameter로 추출**할 수 있는지 궁금합니다.
> 2. 불가능하다면, RF mode에서 측정되는 ITR은 정확히 **어느 계면의 값**인지 확인 부탁드립니다.
> 3. Mo/AlN/Si에서 direct AlN/Si TBR 측정이 목표일 경우, FF mode의 multilayer fitting으로 $R_{\mathrm{Mo/AlN}}$, $k_{\mathrm{AlN},\perp}$, $R_{\mathrm{AlN/Si}}$를 분리하는 분석이 가능한지도 확인 부탁드립니다.
> 4. RF ITR 분석을 위한 필수 reference sample과 필요한 두께 시리즈 조건도 안내 부탁드립니다.

센터 답변에서 가장 중요한 문장은 단 하나입니다.

> **“RF로 측정한 ITR이 AlN/Si인지, AlN/rear-metal인지?”**

여기에 “AlN/rear-metal”이라고 답하면, RF는 네 AlN/Si 계면 연구에는 쓰지 않고, FF 또는 다른 분석 설계를 검토해야 합니다.[^19_1]

<div align="center">⁂</div>

[^19_1]: NanoTRsiryogyugyeog.pdf


---

# FF 구조인 경우  : Mo(100–120 nm)/AlN(75, 150, 300 nm)/Si(100) 구조

RF 구조인 경우 : Mo(100–120 nm)/AlN(75, 150, 300 nm)/Mo(100–120 nm)/Si(100) 구조

네, **아주대 NanoTR 시료 규격의 표준 모식도를 그대로 따르면** 두 구조 정리는 맞습니다. 단, RF 쪽은 AlN/Si 계면이 사라지고 AlN/Mo 계면으로 바뀐다는 점, 그리고 75–300 nm AlN은 RF 권장 두께에 못 미친다는 점이 핵심입니다.[^20_1]

## FF 구조

$$
\boxed{
\mathrm{Mo}(100\text{–}120\,\mathrm{nm})
/
\mathrm{AlN}(75,150,300\,\mathrm{nm})
/
\mathrm{Si}(100)
}
$$

- 상부 Mo가 **heater + thermometer transducer**입니다.
- 측정 열경로에는 실제로 다음 계면이 존재합니다.

$$
\mathrm{Mo/AlN}
\quad\text{및}\quad
\boxed{\mathrm{AlN/Si}}
$$

- 따라서 목표가 direct $TBR_{\mathrm{AlN/Si}}$이면, **이 구조가 맞습니다.**
- NanoTR 문서상 FF의 세라믹 measuring object 권장 범위는 300 nm–3 μm입니다. 따라서 **300 nm는 FF 권장 범위**, 150 nm와 75 nm는 장비 담당자에게 sensitivity 및 fitting 가능 여부를 확인해야 하는 도전적 두께입니다.[^20_1]


## RF 구조

$$
\boxed{
\mathrm{Mo}(100\text{–}120\,\mathrm{nm})
/
\mathrm{AlN}(75,150,300\,\mathrm{nm})
/
\mathrm{Mo}(100\text{–}120\,\mathrm{nm})
/
\mathrm{Si}(100)
}
$$

- 상부 Mo: probe로 반사율을 읽는 검출층.
- 하부 Mo: Si 쪽에서 들어온 pump를 흡수하는 **rear heating metal layer**.
- 따라서 열은 대략 하부 Mo → AlN → 상부 Mo 방향으로 전달됩니다.
- 실제 계면은

$$
\mathrm{Mo(top)/AlN}
\quad\text{및}\quad
\mathrm{AlN/Mo(rear)}
$$

입니다.

즉 RF 구조에서는:

$$
\boxed{\mathrm{AlN/Si\ interface\ 없음}}
$$

입니다. Si 위에 먼저 Mo가 증착되므로, direct AlN/Si 계면 대신 **Mo/Si와 AlN/Mo 계면**이 존재합니다. 따라서 RF에서 역산 가능한 계면 저항의 타깃은 $TBR_{\mathrm{AlN/Mo}}$ 또는 양쪽 Mo/AlN 계면을 포함한 유효 계면저항이지, $TBR_{\mathrm{AlN/Si}}$가 아닙니다.[^20_1]

## RF의 추가 제약

첨부 자료 기준 RF mode에서는:

- substrate가 **transparent substrate**여야 합니다.
- Si를 쓴다면 **double-side optical polished, high-resistivity Si**가 필요하며, 자료에는 $1000\,\Omega\cdot\mathrm{cm}$ 이상으로 제시되어 있습니다.
- measuring object 권장 두께는 **1 μm 이상**입니다.[^20_1]

따라서 네 RF 후보인 AlN 75 / 150 / 300 nm는 **표준 RF ITR 프로토콜의 권장 두께 조건에도 맞지 않습니다.**

## 연구 목적별 결론

| 연구 목적 | 맞는 구조 | 모드 |
| :-- | :-- | :-- |
| Direct AlN/Si 계면 TBR | Mo/AlN/Si | FF |
| Mo/AlN 계면 TBR | Mo/AlN/Mo/Si | RF |
| AlN 박막의 cross-plane 열확산도 | 두 구조 모두 가능하나, 두께 조건 충족 필요 | FF 또는 RF |
| AlN/Si 및 Mo/AlN 효과를 포함한 유효 열저항 | Mo/AlN/Si | FF |

따라서 현재 시료 두께와 연구 목적을 함께 고려하면, **AlN/Si TBR이 목표일 때는 FF: Mo/AlN/Si가 정답**입니다. RF는 별도의 “Mo/AlN 계면 열저항” 연구용 샘플로 보아야 합니다.[^20_1]

<div align="center">⁂</div>

[^20_1]: NanoTRsiryogyugyeog.pdf


---

# opaque는 반투명이라는거야?

아니요. **opaque는 불투명**입니다.

- **Transparent**: 투명 — 빛이 잘 통과함
- **Translucent**: 반투명 — 빛은 일부 통과하지만 산란되어 반대편이 선명하지 않음
- **Opaque**: 불투명 — 해당 파장 빛이 거의 통과하지 않음[^21_1][^21_2]

NanoTR 문서에서 FF mode substrate에 “opaque or transparent substrate”라고 쓴 것은, FF는 위쪽에서 pump/probe를 모두 조사하므로 **기판이 불투명한 일반 Si여도 측정 가능**하다는 뜻입니다. 반대로 RF는 Si 기판 쪽에서 pump를 입사시켜야 하므로, **장비 레이저 파장에 대해 transparent한 기판**이 필요합니다.[^21_3]
<span style="display:none">[^21_10][^21_11][^21_4][^21_5][^21_6][^21_7][^21_8][^21_9]</span>

<div align="center">⁂</div>

[^21_1]: https://ko.wikipedia.org/wiki/불투명도

[^21_2]: https://ko.baoshengindustry.com/resources/news-blogs/transparent-vs-translucent-vs-opaque/

[^21_3]: NanoTRsiryogyugyeog.pdf

[^21_4]: https://www.lingq.com/ko/learn-english-online/translate/en/Opaque/

[^21_5]: https://redkiwiapp.com/ko/english-guide/antonyms/transparent

[^21_6]: https://lingolandedu.com/ko/english-korean-dictionary/opaque

[^21_7]: https://engnote.tistory.com/61

[^21_8]: https://speckofdust.tistory.com/121

[^21_9]: https://blog.naver.com/jajuye123/221344649994

[^21_10]: https://noun.town/language-learning-game/korean/glossary/opaque/

[^21_11]: https://www.amazingtalker.co.kr/questions/8680


---

# ITR은 RF만 된다고 하니... 내가 양면 폴리싱 웨이퍼를 산건데.... 머리아프네...

그럼 머리 아플 만합니다. 다만 **양면 폴리싱 Si 웨이퍼를 산 것이 헛된 건 아닙니다.** RF 표준 ITR 프로토콜을 고려한 준비로는 맞았고, 그 장비가 요구하는 투명·양면 광학 연마 조건에도 부합할 가능성이 큽니다.[^22_1]

문제는 웨이퍼가 아니라 **“RF 표준 구조에서 ITR이 어느 계면을 뜻하는가”**입니다.

## 지금 선택지는 두 가지입니다

### 1. 목표가 direct AlN/Si TBR

구조는 유지해야 합니다.

$$
\mathrm{Mo}/\mathrm{AlN}/\mathrm{Si}
$$

이때 직접 접촉 AlN/Si를 보존해야 하므로, **FF 측정 + multilayer fitting**이 논리적으로 맞습니다. 양면 폴리싱 Si를 써도 FF 측정은 가능합니다. FF에서는 기판의 투명성은 필수 조건이 아니며, DSP 표면은 오히려 기판 두께 균일성·후면 평탄도 측면에서 불리하지 않습니다.[^22_1]

### 2. 목표가 AlN/Mo 계면 ITR

RF가 정확히 맞습니다.

$$
\mathrm{Mo(top)}/\mathrm{AlN}/\mathrm{Mo(rear)}/\mathrm{DSP\text{-}Si}
$$

이 구조에서는 RF로 AlN 내부 열확산도와 **AlN/Mo 계면 열저항**을 다룰 수 있습니다. 다만 이것은 direct AlN/Si 계면 특성과는 다른 연구 질문입니다.[^22_1]

## 아직 확정하지 마세요

센터가 “ITR은 RF만 가능”이라고 안내했더라도, 그 말은 보통 **센터의 표준 분석 리포트에서 ITR fitting을 RF protocol으로 제공한다**는 뜻일 수 있습니다. 반면 FF-TDTR 원리 자체에서 buried interface를 모델에 포함하는 것은 가능하지만, 해당 센터가 그 fitting service를 제공하는지는 별도 문제입니다.[^22_2][^22_3]

따라서 딱 아래 한 문장만 먼저 확인하면 됩니다.

> “Mo/AlN/Si 구조에서 direct AlN/Si 계면 TBR이 목표입니다. 센터의 FF mode 분석에서 $R_{\mathrm{Mo/AlN}}$, $k_{\mathrm{AlN},\perp}$, $R_{\mathrm{AlN/Si}}$를 포함한 multilayer fitting 또는 AlN/Si TBR 추출이 가능한가요?”

- **가능** → DSP-Si를 그대로 사용해 FF 시료를 제작하면 됩니다.
- **불가능** → RF는 AlN/Mo ITR 측정으로 목적을 전환하거나, AlN/Si TBR fitting이 가능한 다른 TDTR 기관/분석법을 찾아야 합니다.

지금 단계에서 **rear Mo를 증착하지 않는 것**이 가장 중요합니다. 그 한 층이 들어가면 direct AlN/Si 계면은 되돌릴 수 없게 바뀝니다.

<div align="center">⁂</div>

[^22_1]: NanoTRsiryogyugyeog.pdf

[^22_2]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11044587/

[^22_3]: https://kummelgroup.ucsd.edu/pubs/papers_2023/Perex%20Mcleod%20AlN%20Thermal%20Conductivity%20ACS%20Nano%202023.pdf


---

# Mo(top)/AlN/Si/Mo(rear)/DSP-Si 이렇게 증착하고 Si와 AlN의 합산 두께를 300 nm로 하면 되려나?

그 구조는 **원리상 매우 타당한 RF multilayer 설계**입니다. 다만 지금 확인된 NETZSCH 공식 자료와 아주대 안내 슬라이드 사이에 **RF/FF의 도식·조건 배치가 서로 뒤섞여 보이는 불일치**가 있어서, rear-Mo를 증착하기 전에 센터에 구조를 그림으로 보내고 확인받아야 합니다.[^23_1][^23_2][^23_3]

## 네가 제안한 구조

위에서 아래 방향으로 쓴 구조라면:

$$
\mathrm{Mo(top)}
/
\mathrm{AlN}
/
\mathrm{Si\ thin\ layer}
/
\mathrm{Mo(rear)}
/
\mathrm{DSP\text{-}Si}
$$

RF에서는 아래 DSP-Si를 통해 pump가 들어가 rear Mo에서 흡수되고, 열은 다음 순서로 상부 probe 쪽으로 이동합니다.

$$
\mathrm{Mo(rear)}
\rightarrow
\mathrm{Si\ thin\ layer}
\rightarrow
\boxed{\mathrm{Si/AlN}}
\rightarrow
\mathrm{AlN}
\rightarrow
\mathrm{Mo(top)}
$$

따라서 이번 구조는 이전의 Mo/AlN/Mo/Si와 달리, 실제로 **Si/AlN 직접 계면을 유지**합니다. 이 점에서 네 아이디어는 맞습니다.

## 이때의 전체 저항식

면적 정규화 열저항을 1D 직렬 근사로 쓰면:

$$
R_{\mathrm{stack}}
=
R_{\mathrm{Mo(rear)/Si}}
+
\frac{d_{\mathrm{Si}}}{k_{\mathrm{Si}}}
+
R_{\mathrm{Si/AlN}}
+
\frac{d_{\mathrm{AlN}}}{k_{\mathrm{AlN},\perp}}
+
R_{\mathrm{AlN/Mo(top)}}
$$

따라서 목표 계면값은 개념적으로:

$$
\boxed{
R_{\mathrm{Si/AlN}}
=
R_{\mathrm{stack}}
-
R_{\mathrm{Mo(rear)/Si}}
-
\frac{d_{\mathrm{Si}}}{k_{\mathrm{Si}}}
-
\frac{d_{\mathrm{AlN}}}{k_{\mathrm{AlN},\perp}}
-
R_{\mathrm{AlN/Mo(top)}}
}
$$

처럼 정리할 수 있습니다.

즉, 네가 앞에서 제시한 “전체값에서 reference 및 각 bulk 저항을 제외해 target interface를 추출한다”는 접근이 **이 구조에서는 논리적으로 성립**합니다. 계면·박막 열저항을 직렬합으로 두고, 두께 시리즈로 intrinsic $k$와 총 계면저항을 분해하는 방식은 실제 thin-film thermoreflectance 연구에도 쓰입니다.[^23_4][^23_5]

## 하지만 총 300 nm 고정은 권장하지 않음

$$
d_{\mathrm{AlN}}+d_{\mathrm{Si}}=300\,\mathrm{nm}
$$

로 고정하는 것은 피하는 편이 좋습니다.

예를 들어 AlN이 75 / 150 / 300 nm일 때 Si를 225 / 150 / 0 nm로 만들면:

- 300 nm AlN 시료에서는 Si layer가 0 nm가 되어 **Si/AlN 계면 자체가 사라집니다**.
- AlN과 Si의 두께가 동시에 반대로 변하므로, $d_{\mathrm{AlN}}/k_{\mathrm{AlN}}$ 변화와 $d_{\mathrm{Si}}/k_{\mathrm{Si}}$ 변화가 섞입니다.
- 따라서 $R_{\mathrm{Si/AlN}}$을 분리하는 피팅의 식별성이 나빠집니다.

더 나은 설계는 **Si thin layer 두께를 모든 샘플에서 고정**하고, AlN 두께만 바꾸는 것입니다.

$$
\mathrm{Mo(top)}
/
\mathrm{AlN}(75,150,300\,\mathrm{nm})
/
\mathrm{Si}(d_{\mathrm{Si,fixed}})
/
\mathrm{Mo(rear)}
/
\mathrm{DSP\text{-}Si}
$$

예를 들어 $d_{\mathrm{Si,fixed}}=300$ nm로 고정하면:


| 샘플 | AlN | Si thin layer | Si/AlN 계면 |
| :-- | --: | --: | :-- |
| S1 | 75 nm | 300 nm | 존재 |
| S2 | 150 nm | 300 nm | 존재 |
| S3 | 300 nm | 300 nm | 존재 |

이렇게 해야 Si/AlN 계면의 형성 조건은 유지하면서 AlN bulk 열저항만 체계적으로 변화시킬 수 있습니다.

## 반드시 확인할 점

여기서 “Si”는 rear Mo 아래의 DSP-Si substrate가 아니라, **rear Mo 위에 별도로 존재하는 얇은 Si 층**이어야 합니다.

$$
\text{DSP-Si substrate} \ne \text{Si thin layer}
$$

즉, 실제 공정 순서는 아래에서 위로:

$$
\mathrm{DSP\text{-}Si}
\rightarrow
\mathrm{Mo(rear)}
\rightarrow
\mathrm{Si\ thin\ layer}
\rightarrow
\mathrm{AlN}
\rightarrow
\mathrm{Mo(top)}
$$

입니다.

만약 “Si”가 단지 기판을 뜻한다면, rear Mo가 들어가는 순간 AlN은 Mo 위에 성장하므로 target interface는 다시 AlN/Si가 아니라 AlN/Mo가 됩니다.

## 센터에 이렇게 문의하세요

> RF mode에서 direct Si/AlN 계면 TBR을 목표로 합니다.
> 구조는 DSP-Si / Mo(rear, 100–120 nm) / Si thin layer / AlN(75, 150, 300 nm) / Mo(top, 100–120 nm)입니다.
>
> Pump는 DSP-Si side에서 rear Mo를 가열하고, probe는 top Mo에서 검출하도록 계획했습니다. 이 multilayer stack에서 $R_{\mathrm{Mo/Si}}$, $R_{\mathrm{Si/AlN}}$, $R_{\mathrm{AlN/Mo}}$ 및 각 박막 bulk resistance를 포함한 response-function fitting으로 $TBR_{\mathrm{Si/AlN}}$을 추출할 수 있는지 확인 부탁드립니다.
>
> 또한 Si thin layer 두께를 고정하고 AlN만 75/150/300 nm로 변화시키는 설계가 표준 RF ITR fitting에 적합한지, 그리고 필요한 reference sample 구성을 안내 부탁드립니다.

마지막으로, 공식 NETZSCH 자료에는 RF가 투명 기판에서 rear heating을 수행하며 thin-film/substrate interface resistance를 평가하는 용도로 설명되어 있습니다. 반면 첨부 슬라이드는 RF/FF의 그림과 bullet 조건이 서로 맞지 않는 부분이 있어 보입니다. 따라서 **센터의 실제 장비 구성과 fitting model이 이 구조를 지원하는지**가 최종 판단 기준입니다.[^23_2][^23_3][^23_1]
<span style="display:none">[^23_10][^23_11][^23_12][^23_13][^23_14][^23_15][^23_16][^23_6][^23_7][^23_8][^23_9]</span>

<div align="center">⁂</div>

[^23_1]: NanoTRsiryogyugyeog.pdf

[^23_2]: https://analyzing-testing.netzsch.com/en/products/time-domain-thermoreflectance-analyzer-tdtr/nanotr

[^23_3]: https://analyzing-testing.netzsch.com/_Resources/Persistent/3/4/1/2/341225391139cd1ce20fd22ccca8496a0ff05ea1/OnSet_26_en_web.pdf

[^23_4]: https://pubs.aip.org/aip/apm/article/6/5/058302/1023619/Thermal-conductivity-and-thermal-boundary

[^23_5]: https://pubs.aip.org/aip/apl/article/105/1/013903/596313/Experimental-and-theoretical-assessments-of

[^23_6]: https://pubs.acs.org/doi/10.1021/acsaelm.1c01239

[^23_7]: https://www.sciencedirect.com/science/article/abs/pii/S0017931023001904

[^23_8]: https://pdf.directindustry.com/pdf/netzsch-analyzing-testing/thermoreflectance-pulsed-light-heating-nanotr-picotr/39926-1081786.html

[^23_9]: http://www.eyoungindustry.com/uploadfile/file/20151027/20151027204807_48427.pdf

[^23_10]: http://users.mrl.illinois.edu/cahill/3omega10.pdf

[^23_11]: https://www.academia.edu/117628190/Analysis_of_Microscale_Heat_Transfer_and_Ultrafast_Thermoelasticity_in_a_Multi_Layered_Metal_Film

[^23_12]: https://arxiv.org/pdf/1807.01258v1.pdf

[^23_13]: https://arxiv.org/pdf/2112.08734.pdf

[^23_14]: https://arxiv.org/pdf/2604.12539.pdf

[^23_15]: https://analyzing-testing.netzsch.com/_Resources/Persistent/4/b/a/0/4ba07430dd66702c2f0e7aeb83ca919d6af14b5f/AN%20273_Thermal-Diffusivity-Measurements-on%20PEDOT_PSS-Thin%20Film-by-Means-of-NanoTR-English.pdf

[^23_16]: https://www.pico-therm.com/english/product/index.html


---

# 결론적으로 정리하려면 어떻게 해야해?

1. AlN이 Target layer인 경우 RF mode 관련 시료 구조

- Mo(top)/AlN/Mo(rear)/DSP-Si

2. AlN이 Target layer인 경우 FF mode 관련 시료 구조

- Mo(top)/AlN/(DSP-)Si

3. 의도한대로 AlN/Si의 ITR 특성을 확인하기 위한 시료구조는...

- Mo(top)/AlN/Si(100)/Mo(rear)/DSP-Si (??)

RF 모드에서 추가 설정으로 AlN/Si의 TBR이나 ITR 특성이 추출되길 바래 제발...

결론을 **센터가 적용할 가능성이 큰 NanoTR 표준 RF ITR 프로토콜(JIS R 1690)** 기준으로 정리하면 아래가 맞습니다. 그리고 먼저 바로잡을 점이 하나 있습니다: **표준 RF-ITR은 ‘세 층 metal / ceramic / metal’ 구조**로 ceramic–metal 계면저항을 구하는 방법입니다.[^24_1][^24_2]

## 1. AlN 자체가 target

### RF mode: AlN의 $\alpha_\perp$ 및 Mo/AlN ITR

$$
\boxed{
\mathrm{Mo(top)}
/
\mathrm{AlN}
/
\mathrm{Mo(rear)}
/
\mathrm{DSP\text{-}Si}
}
$$

- DSP-Si: 1550 nm pump가 통과하는 투명 지지기판.
- rear Mo: pump를 흡수하는 heating metal.
- top Mo: probe 반사율로 온도 변화를 검출하는 metal.
- AlN: 열이 통과하는 **target ceramic layer**.

이 구조는 표준 RF ITR의 핵심인 **metal / ceramic / metal 3층부**에 해당합니다. 따라서 얻는 값은:

$$
\alpha_{\mathrm{AlN},\perp},\qquad
R_{\mathrm{Mo/AlN}}^{\mathrm{top}},\qquad
R_{\mathrm{AlN/Mo}}^{\mathrm{rear}}
$$

또는 장비의 fitting 범위에 따라 양쪽 Mo/AlN 계면을 합친 effective ITR입니다. JIS R 1690은 세라믹층의 위·아래에 약 100 nm 금속막을 둔 3층 박막에서 세라믹의 두께 방향 열확산도와 ceramic/metal 계면 열저항을 구하도록 정의합니다.[^24_2][^24_3][^24_1]

### FF mode: AlN의 $\alpha_\perp$ 또는 effusivity

$$
\boxed{
\mathrm{Mo(top)}
/
\mathrm{AlN}
/
\mathrm{Si(100)}
}
$$

- 이 구조는 direct AlN/Si 계면을 그대로 유지합니다.
- FF는 상부 Mo에서 pump와 probe를 동시에 수행합니다.
- 하지만 **센터가 FF에서 ITR fitting을 제공하지 않는다면**, 여기서는 AlN의 thermal diffusivity/effusivity 또는 유효 열전도도 중심 결과만 받을 가능성이 큽니다. NanoTR 공식 설명도 RF는 thermal diffusivity와 interfacial resistance, FF는 thermal diffusivity와 thermal effusivity 중심으로 구분합니다.[^24_4]


## 2. Direct AlN/Si ITR이 target

네가 진짜 원하는 것은 다음입니다.

$$
\boxed{R_{\mathrm{AlN/Si}}}
$$

그런데 표준 RF-ITR 구조에서는 AlN의 아래에 rear Mo가 들어가므로:

$$
\mathrm{Mo}/\mathrm{AlN}/\mathrm{Mo}/\mathrm{DSP\text{-}Si}
$$

에는 **AlN/Si 계면이 존재하지 않습니다.**

따라서 표준 RF로 얻는 값은:

$$
\boxed{
R_{\mathrm{AlN/Mo}}
\text{ 또는 }
R_{\mathrm{Mo/AlN}}
}
$$

이고, $R_{\mathrm{AlN/Si}}$가 아닙니다.[^24_1][^24_2]

## 3. 네가 제안한 5층 구조

$$
\mathrm{Mo(top)}
/
\mathrm{AlN}
/
\mathrm{Si(100)}
/
\mathrm{Mo(rear)}
/
\mathrm{DSP\text{-}Si}
$$

이 구조는 **물리적인 아이디어는 맞습니다.** 열경로에 AlN/Si 계면을 의도적으로 남기기 때문입니다.

$$
\mathrm{Mo(rear)}
\rightarrow
\mathrm{Si}
\rightarrow
\boxed{\mathrm{Si/AlN}}
\rightarrow
\mathrm{AlN}
\rightarrow
\mathrm{Mo(top)}
$$

따라서 이상적인 다층 모델은:

$$
R_{\mathrm{stack}}
=
R_{\mathrm{Mo(rear)/Si}}
+
\frac{d_{\mathrm{Si}}}{k_{\mathrm{Si}}}
+
R_{\mathrm{Si/AlN}}
+
\frac{d_{\mathrm{AlN}}}{k_{\mathrm{AlN},\perp}}
+
R_{\mathrm{AlN/Mo(top)}}
$$

이고, 모든 나머지 항을 독립적으로 결정할 수 있다면:

$$
R_{\mathrm{AlN/Si}}
=
R_{\mathrm{stack}}
-
R_{\mathrm{Mo(rear)/Si}}
-
\frac{d_{\mathrm{Si}}}{k_{\mathrm{Si}}}
-
\frac{d_{\mathrm{AlN}}}{k_{\mathrm{AlN},\perp}}
-
R_{\mathrm{AlN/Mo(top)}}
$$

로 역산할 수 있습니다.

## 결정적 한계

하지만 이 5층 구조는 **센터의 표준 RF ITR 프로토콜이 아닙니다.**

표준 프로토콜은:

$$
\text{metal}/\text{ceramic}/\text{metal}
$$

이고, 네가 원하는 것은:

$$
\text{metal}/\text{AlN}/\text{Si}/\text{metal}
$$

입니다. Si thin layer까지 포함하면 fit parameter가 최소한 $k_{\mathrm{Si}}$, $k_{\mathrm{AlN}}$, Mo/Si TBR, AlN/Si TBR, AlN/Mo TBR로 늘어납니다. 따라서 **센터가 custom multilayer response-function fitting을 해 주지 않는다면**, 표준 RF 분석만으로 $TBR_{\mathrm{AlN/Si}}$를 신뢰성 있게 분리해 주기는 어렵습니다.[^24_4][^24_1]

또 하나의 공정 문제도 있습니다. 이 구조의 “Si(100)”가 진짜 단결정 Si(100) thin layer여야 direct AlN/Si(100) growth interface와 동등하게 해석할 수 있습니다. rear Mo 위에 sputtered Si를 올린 뒤 AlN을 증착하면, 그 Si는 보통 **poly-Si 또는 a-Si**가 되어 원래 Si(100) substrate 위 AlN과는 다른 계면이 됩니다.

## 최종 판단표

| 목적 | 권장 구조 | NanoTR 표준 RF ITR 가능성 | 실제 얻는 ITR |
| :-- | :-- | --: | :-- |
| AlN 열확산도 | Mo/AlN/Mo/DSP-Si | 가능 | Mo/AlN 관련 계면 영향 포함 |
| AlN/Mo 계면 TBR | Mo/AlN/Mo/DSP-Si | 가능 | $TBR_{\mathrm{Mo/AlN}}$ |
| Direct AlN/Si TBR | Mo/AlN/Si | FF 구조는 적합, 단 센터 ITR fitting 확인 필요 | $TBR_{\mathrm{AlN/Si}}$ 가능성 |
| Direct AlN/Si TBR을 RF로 | Mo/AlN/Si/Mo/DSP-Si | **custom multilayer fitting 필요** | 표준 RF로 보장 불가 |

## 센터에 물어볼 한 문장

> 표준 RF ITR 분석이 JIS R 1690의 metal/ceramic/metal 3층 구조만 지원하는지, 아니면 Mo/AlN/Si/Mo/DSP-Si의 5층 구조에 대해 $R_{\mathrm{Mo/Si}}$, $R_{\mathrm{AlN/Si}}$, $R_{\mathrm{AlN/Mo}}$를 분리하는 custom multilayer fitting이 가능한지 문의드립니다.

센터가 **“JIS 표준 3층만 가능”**이라고 답하면, 결론은 명확합니다.

$$
\boxed{
\text{RF로는 }TBR_{\mathrm{AlN/Si}}\text{ 불가}
}
$$

그때 AlN/Si 계면이 목표라면, **Mo/AlN/Si FF 측정 + 해당 계면을 포함하는 custom fitting 가능 기관**을 찾는 것이 맞습니다.
<span style="display:none">[^24_10][^24_11][^24_12][^24_13][^24_14][^24_15][^24_5][^24_6][^24_7][^24_8][^24_9]</span>

<div align="center">⁂</div>

[^24_1]: https://webdesk.jsa.or.jp/preview/pre_jis_r_01690_000_000_2018_j_ed10_ch.pdf

[^24_2]: https://kikakurui.com/r1/R1690-2018-01.html

[^24_3]: https://www.aist.go.jp/Portals/0/resource_images/aist_j/aistinfo/aist_today/vol12_05/vol12_05_p16.pdf

[^24_4]: https://analyzing-testing.netzsch.com/en/products/time-domain-thermoreflectance-analyzer-tdtr/nanotr

[^24_5]: https://www.jisc.go.jp/app/jis/general/GnrJISSearch.html

[^24_6]: https://www.intertekinform.com/en-gb/standards/jis-r-1690-2018-634022_saig_jsa_jsa_3134131/

[^24_7]: https://docs.cntd.ru/document/552134416

[^24_8]: https://store.accuristech.com/standards/jsa-jis-r-1690?product_id=3101085

[^24_9]: https://www.endokagaku.co.jp/catalog/wp-content/uploads/2024/12/netzsch_nanotr_picotr_catalog.pdf

[^24_10]: https://www.jfcc.or.jp/jis/

[^24_11]: https://www.lihyuan.com.tw/115p.html

[^24_12]: https://analyzing-testing.netzsch.com/de/produkte/time-domain-thermoreflectance-analyzer-tdta/nanotr

[^24_13]: https://analyzing-testing.netzsch.com/_Resources/Persistent/4/b/a/0/4ba07430dd66702c2f0e7aeb83ca919d6af14b5f/AN%20273_Thermal-Diffusivity-Measurements-on%20PEDOT_PSS-Thin%20Film-by-Means-of-NanoTR-English.pdf

[^24_14]: https://www.pico-therm.com/english/product/index.html

[^24_15]: https://netzsch.co.jp/product/nanotr-picotr/

