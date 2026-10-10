<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# TDTR 탭 기준으로 내가 열전도도 분석을 위해 시료 구조부터 어떤 부분까지 철저하게 준비해야하는지를 알려줘.

TDTR로 **AlN/Si 박막의 cross-plane 열전도도와 AlN/Si 계면 열저항**을 분석하려면, 단순히 “AlN 증착 후 금속막 코팅”에서 끝나면 안 됩니다. **시료 구조, 두께·계면·표면의 독립 측정값, transducer 기준시편, 그리고 fitting 목적의 사전 정의**까지 한 세트로 준비해야 결과의 신뢰도가 확보됩니다. TDTR 신호는 막 두께, 각 층의 열용량, transducer 열물성, laser spot size 등에 모두 영향을 받습니다.[^1_1]

## 먼저 목표를 분리하세요

현재 네 연구 목적에서는 아래 두 값을 **동시에 한 번에 완벽히 분리하려 하기보다**, 우선순위를 정해야 합니다.


| 우선 목표 | TDTR 시료 구조 | 핵심 fitting 결과 | 비고 |
| :-- | :-- | :-- | :-- |
| AlN의 cross-plane $k_\perp$ | Mo/AlN/Si | $k_{\mathrm{AlN},\perp}$, 필요 시 유효 계면 저항 | 가장 기본 구조 |
| 직접 AlN/Si 계면 TBR | Mo/AlN/Si + 두께 series | $G_{\mathrm{AlN/Si}}$ 또는 $R_{\mathrm{AlN/Si}}$ | AlN 두께 series와 sensitivity 검증이 중요 |
| Mo/AlN 계면 특성 | Mo/AlN/Mo/DSP-Si 또는 별도 구조 | $G_{\mathrm{Mo/AlN}}$ | AlN/Si 계면은 사라짐 |
| 금속막 자체 기준값 | Mo/Si 또는 Mo/SiO2/Si | Mo의 $k$, $C$, 두께·계면 기준 | 실제 transducer 증착 조건과 동일해야 함 |

AlN/Si 직접 계면이 핵심이라면, 현재 가장 안전한 기본 구조는 다음입니다.

$$
\boxed{\mathrm{Mo}(100\text{–}120\,nm)/\mathrm{AlN}(t)/\mathrm{Si}(100)}
$$

이 구조에는 Mo/AlN 및 AlN/Si 두 계면이 모두 존재합니다. 따라서 피팅 모델에서 두 계면을 무조건 자유변수로 두기보다, 측정 sensitivity와 기준시료 결과에 따라 하나를 고정·제약해야 합니다. 실제 AlN/Si TDTR 연구에서도 Al transducer/AlN/Si 구조를 이용해 AlN 열전도도와 AlN/Si thermal boundary conductance를 추출했습니다.[^1_2]

## 권장 시료 구성

### 필수 분석 시편

동일한 Si wafer lot 및 동일 AlN deposition run을 바탕으로, 최소한 다음과 같이 준비하는 것을 권합니다.


| 시료 ID | 구조 | 목적 |
| :-- | :-- | :-- |
| A1 | Mo/AlN 75 nm/Si | 두께 의존성, 얇은 막 영역 |
| A2 | Mo/AlN 150 nm/Si | 중간 두께 |
| A3 | Mo/AlN 300 nm/Si | 우선 측정 권장 기준 시료 |
| Ref-Mo | Mo/Si | transducer 및 Mo/Si 기준 응답 |
| Ref-Si | Bare Si | 기판 물성·광학 상태 확인, 필요 시 background/reference |
| Witness | AlN/Si, Mo 미증착 | XRR/XRD/AFM/XPS/ellipsometry/단면 분석용 |

네가 75/150/300 nm series를 생각한 방향은 타당합니다. 특히 단일 시료에서는 $k_{\mathrm{AlN}}$, $G_{\mathrm{Mo/AlN}}$, $G_{\mathrm{AlN/Si}}$가 상관되어 분리가 어려울 수 있으므로, **동일 공정의 두께 series를 global fitting 또는 상호 제약 조건에 활용**하는 편이 훨씬 낫습니다. 고열전도 박막은 단일 주파수 TDTR에서 막 열전도도에 대한 sensitivity가 낮아질 수 있어, dual-frequency TDTR가 정확도를 개선하는 방법으로 제시되어 있습니다.[^1_3][^1_4]

### 1장만 먼저 맡긴다면

의뢰 전 feasibility 확인이 목적이라면, 아래를 1순위로 권합니다.

$$
\boxed{\mathrm{Mo}(100\text{–}120\,nm)/\mathrm{AlN}(300\,nm)/\mathrm{Si}(100)}
$$

- 300 nm는 75 nm보다 AlN 막 자체의 열저항 기여가 커서 $k_{\mathrm{AlN}}$ sensitivity를 확보하기 상대적으로 유리합니다.
- 동시에 별도 **Mo/Si 기준시편**은 같은 Mo 증착 run에서 반드시 확보하세요.
- 단, “시료 1장”의 TDTR 결과만으로 $k_{\mathrm{AlN}}$, $G_{\mathrm{Mo/AlN}}$, $G_{\mathrm{AlN/Si}}$를 모두 독립적으로 신뢰성 있게 추출하겠다는 목표는 과도합니다.


## 증착 구조에서 관리할 것

### Si 기판

- **기판 종류:** Si(100), dopant type, resistivity, 두께, DSP 여부를 기록하세요.
- **동일 wafer lot:** 두께 series와 Mo reference는 가능한 한 같은 wafer lot에서 제작하세요.
- **세정 이력:** solvent clean, DI rinse, N2 dry, dehydration bake, Ar plasma 또는 HF-last 여부와 시간을 기록하세요.
- **native oxide:** AlN을 Si native oxide 위에 증착하면 실제로는 “AlN/Si”가 아니라 **AlN/SiO$_x$/Si 계면**일 수 있습니다. 이 얇은 산화막이 계면 열저항에 크게 기여할 수 있으므로, native oxide를 유지할지 제거할지부터 연구 조건으로 정의해야 합니다.

특히 네 연구 주제가 BEOL 절연막 및 hybrid bonding 맥락이라면, “실제 공정에서 형성되는 interfacial oxide를 포함한 유효 열저항”을 볼 것인지, “가능한 oxide-free AlN/Si 직접 계면”을 볼 것인지 논문 수준에서 분명히 나눠야 합니다.

### AlN 막

각 AlN 시료에 대해 아래 항목을 TDTR fitting 입력값 또는 결과 해석 변수로 확보하세요.

- **실제 두께 $t_{\mathrm{AlN}}$:** nominal deposition time이 아니라 ellipsometry, XRR, profilometry, cross-sectional SEM/TEM 중 최소 하나로 측정
- **두께 균일도:** wafer 중앙 및 최소 4–5개 위치에서 측정
- **밀도 $\rho$:** 가능하면 XRR, 어려우면 조성·공극 여부를 별도 확인
- **비열 $C_p$:** 문헌값 사용 가능하지만, film density를 반영해 volumetric heat capacity $C=\rho C_p$로 입력
- **결정성:** XRD $\theta$-2$\theta$, rocking curve, 가능하면 pole figure
- **(0002) 배향성:** AlN에서는 c-axis texture가 cross-plane phonon transport 해석에 직접적으로 중요
- **조성:** XPS, RBS, ERDA, EDS 등 가능한 방법으로 Al:N ratio와 O incorporation 확인
- **응력:** wafer curvature, XRD peak shift 등으로 tensile/compressive stress 확인
- **표면 조도:** AFM RMS roughness 측정

TDTR은 반사 probe를 이용하므로 표면이 광학적으로 충분히 평탄해야 합니다. 일반적인 지침은 RMS roughness를 약 15 nm 이하로 관리하는 것이며, 거칠기가 크면 diffuse scattering과 열팽창 유래 신호가 thermoreflectance 해석을 오염시킬 수 있습니다.[^1_5][^1_1]

## 계면을 철저히 관리하세요

AlN/Si TBR을 주장하려면 가장 중요한 것은 **AlN/Si 계면이 정말 무엇으로 구성되어 있는지**입니다.

### 반드시 확인할 항목

- Si 표면 native oxide 유무 및 예상 두께
- 증착 전 Ar plasma가 Si 표면에 만든 손상 또는 재증착층
- 초기 nucleation layer의 조성 변화
- Al-rich 또는 N-rich interlayer 형성 가능성
- 산소·탄소 오염
- AlN/Si 계면 반응층 또는 저밀도층
- substrate temperature 및 pre-sputter 중 기판 노출 조건
- base pressure, working pressure, $N_2/(Ar+N_2)$, RF power, deposition rate

실제 TDTR 기반 AlN/Si 연구에서는 AlN/Si deposition interface layer 두께를 TEM으로 확인하고, Al transducer·AlN·계면층의 두께를 각각 acoustic echo, ellipsometry, TEM 등으로 확보해 모델에 반영했습니다.[^1_2]

따라서 네 경우도 가능하다면 **대표 시료 1개는 단면 TEM/STEM-EDS 또는 최소 FESEM 단면**으로 계면을 확인하는 것이 좋습니다. 계면층을 보지 않은 채 $R_{\mathrm{AlN/Si}}$라고 부르면, 실제로는 “AlN/비정질 산화층/Si를 포함한 유효 계면 저항”일 가능성이 있습니다.

## Mo transducer 준비

Mo를 사용할 수는 있지만, Al 대비 광학·열물성 및 film stress가 다르므로 **동일 run 기준시편**이 더 중요합니다. TDTR에서는 transducer 두께와 열전도도가 결과에 큰 영향을 주므로, transducer 자체의 물성을 정확히 아는 것이 필수입니다.[^1_6][^1_1]

### Mo 막 권장 조건

- **두께:** 우선 100–120 nm 범위
- **형태:** 패턴 없이 blanket film으로 충분
- **증착:** 분석 시료와 Ref-Mo를 반드시 같은 run에서 동시 증착
- **두께 측정:** TDTR acoustic echo 가능 여부와 별개로 profilometry, XRR 또는 cross-sectional SEM으로 외부 검증
- **sheet resistance:** 4-point probe 측정 후 resistivity 산출
- **표면 상태:** AFM 또는 optical microscopy로 pinhole, cracking, particle 확인
- **접착층:** Ti/Cr adhesion layer는 가능하면 피하세요. 넣으면 Mo/AlN 외에 Ti/AlN 또는 Cr/AlN 계면이 생겨 모델이 복잡해집니다.
- **산화·오염 방지:** Mo 증착 전 AlN 표면을 과도하게 plasma clean하면 AlN 표면 손상이나 조성 변화가 생길 수 있으므로 조건을 최소화하고 기록하세요.

Transducer는 일반적으로 약 100 nm 수준의 Al이 많이 사용되지만, 핵심은 금속 종류 자체보다 **정확한 두께, 열용량, 열전도도, 열반사 특성 및 계면 상태를 모델에 반영하는 것**입니다.[^1_4][^1_1]

## TDTR fitting 입력값

의뢰처에 전달하거나 네가 fitting할 때, 아래 표를 빈칸 없이 채우는 것을 목표로 하세요.


| 층/파라미터 | 필요한 값 | 확보 방법 |
| :-- | :-- | :-- |
| Mo | 두께, $k$, $\rho$, $C_p$, sheet resistance | profilometer/XRR, 4-point probe, 문헌·보정 |
| AlN | 두께, $\rho$, $C_p$, 초기 $k_\perp$ 범위 | ellipsometry/XRR/SEM, XRR, 문헌 |
| Si | orientation, thickness, doping/resistivity, $k$, $C_p$ | wafer spec, 문헌 또는 calibration |
| Mo/AlN | $G_{\mathrm{Mo/AlN}}$ 또는 $R_{\mathrm{Mo/AlN}}$ | fitting 또는 reference·문헌 제약 |
| AlN/Si | $G_{\mathrm{AlN/Si}}$ 또는 $R_{\mathrm{AlN/Si}}$ | fitting target |
| Laser | pump/probe spot radius, modulation frequency, power | 장비 측정값 |
| Optical | Mo reflectance, probe wavelength, signal quality | 장비/센터 확인 |

열저항은 다음처럼 모델에 들어갑니다.

$$
R_{\mathrm{stack}}
=
R_{\mathrm{Mo/AlN}}
+
\frac{t_{\mathrm{AlN}}}{k_{\mathrm{AlN},\perp}}
+
R_{\mathrm{AlN/Si}}
$$

여기서 TDTR은 보통 이 전체 열전달 응답을 fitting합니다. 즉, 단일 시료에서 측정되는 값은 기본적으로 위 성분들이 섞인 응답이며, 단순히 $R_{\mathrm{stack}}=R_{\mathrm{AlN/Si}}$로 둘 수 없습니다.

## 측정 전 품질 확인

TDTR 금속 증착 전에 AlN/Si 상태를 먼저 확인하고, 금속 증착 후에는 transducer 품질을 다시 확인하세요.

### AlN 증착 후, Mo 전

- XRD: (0002) peak 위치, FWHM, texture
- AFM: RMS roughness 및 scan area 명시
- Ellipsometry/XRR/profilometry: 두께와 균일도
- Optical microscope: particle, crack, delamination
- 필요 시 XPS: surface contamination 및 산소
- 대표 시료 단면 SEM 또는 TEM: film thickness·계면


### Mo 증착 후, TDTR 전

- Mo thickness 재확인
- 4-point probe로 sheet resistance mapping
- microscope로 continuity, crack, pinhole 확인
- AFM 또는 roughness 확인
- sample size, flatness, wafer bow 확인
- 측정할 지점을 5–10개 이상 표시하거나 map 계획 수립

TDTR은 매우 작은 반사율 변화를 다루므로 높은 SNR과 정밀 lock-in detection이 중요하며, 시료 위치에 따른 두께·조도·막질 불균일은 곧 데이터 산포로 나타납니다.[^1_7]

## 분석 의뢰 전 질문

센터에 아래를 명확히 확인해야 합니다.

1. **Mo/AlN/Si 3층 구조에 대해 multilayer heat-diffusion fitting이 가능한가?**
2. **추출 가능 파라미터가 $k_{\mathrm{AlN},\perp}$만인지, $G_{\mathrm{AlN/Si}}$까지 포함 가능한지?**
3. **Mo/AlN 및 AlN/Si 두 계면을 동시에 free parameter로 둘 수 있는지, 아니면 하나를 고정해야 하는지?**
4. **권장 AlN 두께와 modulation frequency는 무엇인지?**
5. **dual-frequency TDTR 또는 다중 modulation frequency fitting이 가능한지?**
6. **Mo transducer 허용 여부와 권장 두께, 필요한 reflectivity 조건은 무엇인지?**
7. **센터가 직접 수행하는 sensitivity analysis 및 uncertainty propagation 범위는 무엇인지?**
8. **Mo/Si reference를 반드시 함께 제출해야 하는지, 제출한다면 어떤 기판·두께 조건이 필요한지?**
9. **시료 1장당 측정 위치 수와 spatial mapping 가능 여부는 무엇인지?**
10. **각 층의 두께, density, heat capacity, substrate 정보 중 사용자가 제출해야 하는 항목은 무엇인지?**

## 네 상황의 실무 권장안

현재 조건이라면 아래 순서가 가장 깔끔합니다.

1. 동일 lot의 Si(100) wafer에 AlN을 75, 150, 300 nm로 증착합니다.
2. AlN 막 두께와 RMS roughness를 각 시료에서 정량화합니다.
3. 대표 시료에서 XRD와 단면 분석으로 (0002) texture 및 AlN/Si 계면 상태를 확보합니다.
4. 동일 Mo deposition run에서 모든 AlN 시료와 **Mo/Si reference**를 함께 제작합니다.
5. 1차 의뢰는 **Mo/AlN(300 nm)/Si + Mo/Si reference**로 feasibility와 sensitivity를 확인합니다.
6. 장비가 $k_{\mathrm{AlN}}$와 $G_{\mathrm{AlN/Si}}$를 분리할 수 있다고 확인되면, 75/150 nm까지 확장하여 thickness-dependent fitting을 수행합니다.
7. 결과는 단일 $k$ 값만 제시하지 말고, $k_\perp$, $G_{\mathrm{AlN/Si}}$, $G_{\mathrm{Mo/AlN}}$의 가정값, thickness uncertainty, roughness, film density, modulation frequency, sensitivity curve를 함께 보고합니다.

이 구조라면 네 AlN sputtering 조건, 결정성·밀도·계면 품질 변화와 TDTR 열전도도 변화를 제대로 연결할 수 있습니다.
<span style="display:none">[^1_10][^1_11][^1_12][^1_13][^1_14][^1_15][^1_16][^1_8][^1_9]</span>

<div align="center">⁂</div>

[^1_1]: https://pubs.aip.org/aip/jap/article/124/16/161103/1030095/Tutorial-Time-domain-thermoreflectance-TDTR-for

[^1_2]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11044587/

[^1_3]: https://pubs.aip.org/aip/rsi/article/87/7/075101/358226/Accurate-measurements-of-cross-plane-thermal

[^1_4]: https://arxiv.org/pdf/1511.04852.pdf

[^1_5]: https://www.linseis.com/en/methods/time-domain-thermoreflectance-tdtr/

[^1_6]: https://s-space.snu.ac.kr/bitstream/10371/210086/1/000000183259.pdf

[^1_7]: https://www.zhinst.com/en/applications/optics-photonics/time-domain-thermoreflectance-tdtr/

[^1_8]: chrome://newtab/

[^1_9]: https://pubs.acs.org/ancac3/article/15/6/9588/1399139/High-In-Plane-Thermal-Conductivity-of-Aluminum

[^1_10]: https://pubs.acs.org/doi/10.1021/acsami.3c13418

[^1_11]: https://nanoheat.stanford.edu/wp-content/uploads/2022/01/Thermal-Characterization-of-Metal−Oxide-Interfaces-Using-TimeDomain-Thermoreflectance-with-Nanograting-Transducers.pdf

[^1_12]: https://patrickehopkins.com/wp-content/uploads/2021/08/hoque2021ab.pdf

[^1_13]: http://www.eyoungindustry.com/uploadfile/file/20201026/20201026212825_21404.pdf

[^1_14]: https://pmc.ncbi.nlm.nih.gov/articles/PMC12261518/

[^1_15]: https://www.ifp.tuwien.ac.at/fileadmin/pers_homepages/buehler_paschen_silke/papers/Pub178.pdf

[^1_16]: https://www.tandfonline.com/doi/full/10.1080/14686996.2025.2523240


---

# TDTR의 기준으로 아래와 같이 시료를 준비해야한다면 내가 실질적으로 준비해야하는 내용들이 어떤 내용들일까?

-. Substrate - 하부 Mo - Si - AlN - 상부 Mo 구조로 서로 다른 두께의 3개 샘플 준비
-. 여기서 (하부 Mo - Si)를 1개의 layer라고 가정한다면 기존 RF mode 권장 샘플 구조와 동일하게 가능
-. 다만 (하부 Mo - Si) 상태에서의 열확산계수, 밀도, 비열이 필요한 상황
: Substrate - 하부 Mo - Si - AlN - 상부 Mo 구조에서 적용한 (하부 Mo - Si) 물질의 두께는 nm or um 수준일 겁니다. 해당 두께에서 열확산계수, 밀도, 비열 측정은 어려울 듯 합니다......
: 대신 Si 두께를 1mm 수준으로 제작 후 하부 Mo 100nm를 올려서 LFA(열확산계수), DSC(비열), 아르키메데스법(밀도)으로 정보를 구할 수 있으나, 이는 실제 샘플과는 다른 두께를 가진다는 문제 발생합니다.

핵심은 **하부 Mo/Si를 하나의 “등가 물질”로 묶어서 $\alpha$, $\rho$, $C_p$를 따로 측정하는 방향은 TDTR에는 적절하지 않다**는 점입니다. 이 구조는 각 층을 분리한 다층 열전달 모델로 다뤄야 하며, 특히 1 mm Si를 넣고 LFA·DSC·아르키메데스법으로 얻은 값을 RF-TDTR의 얇은 적층부에 그대로 적용하는 것은 물리적으로도 측정 감도 측면에서도 맞지 않을 가능성이 큽니다. TDTR은 각 층의 두께·체적비열·transducer 물성에 민감하므로, 층별 입력값을 정확히 정의하는 것이 기본입니다.[^2_1]

## 제안 구조의 의미

네가 말한 구조를 아래처럼 해석하겠습니다.

$$
\boxed{
\text{DSP-Si support}
/
\text{rear Mo}
/
\text{thin Si}
/
\text{AlN}
/
\text{top Mo}
}
$$

- **DSP-Si support:** rear-side pump가 통과하는 광학 지지기판
- **rear Mo:** pump를 흡수해 열을 발생시키는 buried heater
- **thin Si:** AlN/Si 직접 계면을 유지하기 위한 Si layer
- **AlN:** 열전도도 또는 AlN/Si 계면 특성을 보고 싶은 층
- **top Mo:** probe 반사율 변화로 온도를 읽는 transducer

즉, 목표는 단순한 “AlN 단층 열전도도”가 아니라 다음과 같은 다층 열저항·계면저항을 포함한 구조입니다.

$$
R_{\mathrm{eff}}
=
R_{\mathrm{Mo_{rear}/Si}}
+
\frac{t_{\mathrm{Si}}}{k_{\mathrm{Si}}}
+
R_{\mathrm{Si/AlN}}
+
\frac{t_{\mathrm{AlN}}}{k_{\mathrm{AlN},\perp}}
+
R_{\mathrm{AlN/Mo_{top}}}
$$

따라서 하부 Mo/Si를 하나의 layer로 바꾸어

$$
\alpha_{\mathrm{Mo/Si}},\quad
\rho_{\mathrm{Mo/Si}},\quad
C_{p,\mathrm{Mo/Si}}
$$

를 실측해서 넣는 모델이 아니라, **Mo와 Si를 별도의 층으로 입력**하고 각 계면의 thermal boundary conductance $G$ 또는 TBR을 넣는 방식이 맞습니다.

Mo/Si처럼 수 nm~수십 nm 단위의 multilayer는 bulk 성질의 단순 평균으로 충분하지 않을 수 있으며, 실제 cross-plane 열전달에는 각 층 두께와 계면 conductance가 함께 영향을 줍니다.[^2_2][^2_3]

## 1 mm Si 방식의 문제

Si를 약 1 mm로 두고 rear Mo를 100 nm 형성한 뒤, LFA·DSC·아르키메데스법으로 Mo/Si의 열물성을 얻자는 접근은 **TDTR 시료 설계와 목적이 다릅니다.**

### LFA로는 실제 적층부를 대표하기 어렵습니다

LFA는 일반적으로 시편 전체 두께와 rear-to-front 열확산 시간을 이용합니다. 즉, 1 mm Si의 결과는 거의 전적으로 **bulk Si의 열확산도**를 반영합니다. 100 nm Mo와 Mo/Si 계면의 기여는 1 mm Si에 비해 지나치게 작아 분리하기 어렵습니다. LFA에서 산출되는 열확산도도 시편 두께 $d$의 제곱에 비례하므로, 두께 정의와 bulk specimen 조건이 결과를 지배합니다.[^2_4][^2_5]

### RF-TDTR의 열 침투 길이와 맞지 않습니다

TDTR의 modulation frequency가 MHz 수준이면, Si에서 열이 유효하게 탐침되는 깊이는 대략 수 µm 수준입니다.

$$
d_p \approx \sqrt{\frac{\alpha}{\pi f}}
$$

예를 들어 Si의 $\alpha\approx 9\times10^{-5}\,\mathrm{m^2/s}$를 가정하면:


| Modulation frequency | Si thermal penetration depth, 대략 |
| --: | --: |
| 1 MHz | 약 5 µm |
| 5 MHz | 약 2.4 µm |
| 10 MHz | 약 1.7 µm |

따라서 rear Mo에서 가열된 열이 **1 mm Si를 지나 AlN/top Mo까지 도달하여 유의미한 RF-TDTR 신호를 만들기는 사실상 어렵습니다.** 1 mm Si 구조는 “얇은 Si layer가 AlN/Si 계면을 유지하는 RF multilayer”가 아니라, rear heater와 top probe가 열적으로 분리된 두꺼운 Si wafer 구조가 됩니다.

### DSC·아르키메데스법도 불필요합니다

- **DSC:** 100 nm Mo와 수백 nm~수 µm Si 적층부의 비열을 독립 측정하기 어렵습니다. 측정 질량이 너무 작고, support substrate의 신호가 지배적입니다.
- **아르키메데스법:** 이 방법은 bulk specimen density 측정용입니다. 수 nm Mo + 박막 Si 적층의 밀도를 분리해서 줄 수 없습니다.
- **결론:** 이 세 방법은 “두꺼운 bulk composite의 유효 열물성”에는 의미가 있을 수 있지만, 네 TDTR 다층 fitting의 입력값 확보 방법으로는 맞지 않습니다.


## 실제로 준비할 것

### 1. 구조와 두께를 먼저 확정

우선 Si layer의 두께가 핵심입니다. 네 구조에서 Si는 1 mm가 아니라 **열 침투 깊이 및 fitting sensitivity를 고려한 thin Si layer**여야 합니다.

현 단계에서는 장비센터에 아래 두 가지를 반드시 확인해야 합니다.

- RF fitting에서 지원 가능한 **Si layer의 두께 범위**
- $R_{\mathrm{Si/AlN}}$를 independent fitting parameter로 둘 수 있는지
- Si와 AlN의 합산 두께 또는 각 층 두께에 대한 장비의 권장 범위
- standard RF-ITR model이 아니라 **5-layer custom fitting**을 지원하는지

실무적으로는 다음처럼 설계하는 것이 더 현실적입니다.

$$
\text{DSP-Si support}
/
\text{Mo}_{\mathrm{rear}}(100\text{–}120\,\mathrm{nm})
/
\text{Si}(t_{\mathrm{Si}})
/
\text{AlN}(t_{\mathrm{AlN}})
/
\text{Mo}_{\mathrm{top}}(100\text{–}120\,\mathrm{nm})
$$

단, $t_{\mathrm{Si}}$는 임의로 정하면 안 됩니다. **RF modulation frequency, Si thermal penetration depth, 총 열저항, 그리고 AlN/Si interface sensitivity**를 바탕으로 센터와 정해야 합니다.

### 2. Si layer 형성 방법 결정

가장 큰 공정적 질문은 “rear Mo 위에 Si를 어떻게 형성할 것인가”입니다.

RF sputtering 장비로 단결정 Si와 동일한 열물성을 갖는 Si layer를 만들기는 어렵습니다. 단순 sputtered Si는 보통 amorphous 또는 미세결정 상태가 될 가능성이 높고, 단결정 Si와 열전도도·밀도·계면 품질이 다릅니다.

가능한 방식은 다음과 같습니다.


| 방법 | 장점 | 주의점 |
| :-- | :-- | :-- |
| SOI device layer transfer | 두께가 알려진 단결정 Si layer 확보 가능 | bonding/transfer 공정 필요 |
| Thin Si membrane bonding | 실제 Si/AlN 계면 구현 가능 | handling과 void 관리가 어려움 |
| Si-on-insulator 활용 후 BOX 제거·bonding | thin crystalline Si 제어 가능 | 공정 복잡도 높음 |
| Sputtered Si | 장비 접근성은 좋음 | 단결정 Si가 아니며 $k$, $C$, 계면을 별도 검증해야 함 |

만약 네가 의도한 “Si”가 실제 Si(100) wafer의 단결정 Si 성질을 의미한다면, **SOI 기반 thin Si layer 또는 thin-Si transfer/bonding** 쪽이 논리적으로 더 맞습니다.

### 3. 층별로 필요한 입력값 확보

다층 TDTR 모델에 실제로 필요한 내용은 아래입니다.


| 구성 | 필요한 값 | 권장 확보법 |
| :-- | :-- | :-- |
| Top Mo | 두께, 전기저항, $k$, 체적비열 $C_v$ | profilometry/XRR/TDTR acoustic echo, 4-point probe, 문헌·보정 |
| AlN | 두께, $C_v$, $\rho$, $k_\perp$ 범위 | ellipsometry/XRR/단면 SEM, XRR, 문헌·피팅 |
| Thin Si | 실제 두께, 결정성, doping, $k$, $C_v$ | SOI spec, ellipsometry/XRR, Raman/XRD, 문헌·보정 |
| Rear Mo | 두께, $k$, $C_v$, sheet resistance | top Mo와 동일 |
| DSP-Si support | 기판 재질, 두께, resistivity, optical transparency | wafer spec |
| Mo/Si | $G_{\mathrm{Mo/Si}}$ | 문헌 범위·reference sample·fitting constraint |
| Si/AlN | $G_{\mathrm{Si/AlN}}$ | 핵심 fitting target |
| AlN/Mo | $G_{\mathrm{AlN/Mo}}$ | reference 또는 문헌 제약 |

여기서 $\rho$와 $C_p$를 분리해 직접 재는 것보다 TDTR 관점에서는 다음 값이 더 직접적입니다.

$$
\boxed{C_v = \rho C_p}
$$

즉, **체적비열 $C_v$** 입니다. TDTR 신호는 특히 transducer와 각 층의 두께×체적비열 $hC_v$에 민감합니다.[^2_1]

### 4. Mo/Si를 “등가층”으로 보지 말 것

하부 Mo/Si가 매우 얇더라도 다음처럼 분리 모델링하는 것이 원칙입니다.

$$
\mathrm{DSP\text{-}Si}
/
\mathrm{Mo}_{rear}
/
G_{\mathrm{Mo/Si}}
/
\mathrm{Si}
/
G_{\mathrm{Si/AlN}}
/
\mathrm{AlN}
/
G_{\mathrm{AlN/Mo}}
/
\mathrm{Mo}_{top}
$$

다만 실제 fitting에서는 모든 변수를 동시에 자유롭게 두면 ill-conditioned해질 가능성이 큽니다. 따라서 아래처럼 역할을 분리해야 합니다.

- $t_{\mathrm{Mo}}, t_{\mathrm{Si}}, t_{\mathrm{AlN}}$: 독립 측정 후 고정 또는 작은 uncertainty 부여
- $C_{v,\mathrm{Mo}}, C_{v,\mathrm{Si}}, C_{v,\mathrm{AlN}}$: 문헌값 또는 별도 검증값으로 제약
- $k_{\mathrm{Si}}$: Si layer가 단결정 SOI이면 wafer spec/문헌값으로 우선 고정
- $G_{\mathrm{Mo/Si}}$: 별도 reference sample 또는 literature prior로 제약
- fitting target: $k_{\mathrm{AlN},\perp}$, $G_{\mathrm{Si/AlN}}$ 중 하나 또는 제한된 두 개

TDTR에서는 transducer 두께 오차가 관심 열전도도 fitting 오차를 크게 키울 수 있으므로, Mo 100–120 nm라는 nominal 값만 쓰지 말고 **실측 두께와 불확실도**를 확보해야 합니다.[^2_6][^2_7]

## 필요한 시료 세트

3개 두께 sample만 제출하는 것은 최소 구성이고, 실제 분석 가능성을 높이려면 reference도 함께 있어야 합니다.


| 시료 | 구조 | 용도 |
| :-- | :-- | :-- |
| Sample-1 | DSP-Si / Mo / Si / AlN(얇음) / Mo | AlN 두께 의존성 |
| Sample-2 | DSP-Si / Mo / Si / AlN(중간) / Mo | AlN 두께 의존성 |
| Sample-3 | DSP-Si / Mo / Si / AlN(두꺼움) / Mo | AlN 두께 의존성 및 우선 분석 |
| Ref-1 | DSP-Si / Mo / Si / Mo | Si layer와 Mo/Si·Si/Mo 기준 응답 |
| Ref-2 | DSP-Si / Mo / Si / AlN / Mo, 가능한 AlN 기준 두께 | 공정 재현성 확인 또는 반복 측정 |
| Witness | Si / AlN, top Mo 없음 | XRD, AFM, XRR, XPS, 단면 TEM/SEM |

특히 Ref-1은 중요합니다. 이 기준시료가 있어야 Si layer 자체, rear Mo/Si 계면, top-side Mo/Si 계면의 응답을 어느 정도 제약한 뒤, AlN을 넣었을 때 추가되는 응답을 $k_{\mathrm{AlN}}$ 및 $G_{\mathrm{Si/AlN}}$와 연결할 수 있습니다.

## 제작·분석 체크리스트

### 공정 전

- DSP-Si support의 1550 nm 파장 투과성, 두께, doping/resistivity 확인
- rear Mo가 pump 파장에서 충분히 흡수하는지 확인
- Si layer의 형성 방법 결정: SOI transfer인지, membrane bonding인지, sputtered Si인지
- Si layer의 목표 두께를 RF modulation frequency와 sensitivity calculation을 기반으로 확정
- AlN/Si 계면을 만들기 전 native oxide를 유지할지, HF-last로 제거할지 결정
- rear Mo/Si bonding interface의 void와 오염을 최소화할 공정 정의


### 각 시료에서 측정할 것

- 각 층 두께: XRR, ellipsometry, profilometry, 단면 SEM/TEM 중 복수 방법
- Mo thickness 및 sheet resistance: 4-point probe 포함
- Si layer thickness·결정성: SOI spec, Raman, XRD, TEM
- AlN thickness·(0002) texture·FWHM: XRD
- AlN 표면 roughness: AFM
- AlN/Si 계면: 대표 시료 단면 TEM/STEM-EDS 또는 최소 단면 SEM
- top Mo surface roughness 및 continuous film 여부: AFM/optical microscopy
- sample bow, crack, particle, delamination, bonding void 여부

TDTR 표면은 probe를 정반사로 검출할 수 있을 만큼 평탄해야 하며, 통상 RMS roughness는 약 15 nm 이하가 권장됩니다.[^2_1]

## 결론

네가 만들려는 5층 RF 구조는 **custom multilayer fitting이 가능하다는 전제에서만** AlN/Si 계면을 보존한 RF 분석 후보가 될 수 있습니다. 그러나 다음 두 가지는 피해야 합니다.

- **하부 Mo/Si를 하나의 등가층으로 놓고 $\alpha,\rho,C_p$를 LFA·DSC·아르키메데스법으로 구하는 것**
- **Si를 1 mm로 두고 RF-TDTR에서 AlN/Si 계면까지 열적으로 연결될 것이라 기대하는 것**

대신, Mo·Si·AlN을 개별 층으로 모델링하고, 얇은 Si layer의 실제 두께·결정성·계면 품질을 확보해야 합니다. 그리고 제작을 시작하기 전 분석기관에 반드시 “DSP-Si/Mo/Si/AlN/Mo 5층 구조에 대한 custom thermal model과 $G_{\mathrm{Si/AlN}}$ 독립 fitting이 가능한지”를 확인해야 합니다. 이 답이 “불가”라면, 이 RF 구조를 만들어도 목표한 direct AlN/Si TBR을 얻을 수 없습니다.
<span style="display:none">[^2_10][^2_11][^2_12][^2_13][^2_14][^2_15][^2_8][^2_9]</span>

<div align="center">⁂</div>

[^2_1]: https://pubs.aip.org/aip/jap/article/124/16/161103/1030095/Tutorial-Time-domain-thermoreflectance-TDTR-for

[^2_2]: https://ris.utwente.nl/ws/files/234394935/Medvedev2015anisotropy.pdf

[^2_3]: https://nanoheat.stanford.edu/wp-content/uploads/2012/09/Bozorg-Grayeli-EUV.pdf

[^2_4]: http://kjmm.org/upload/pdf/kjmm-138.pdf

[^2_5]: https://blog.naver.com/sj-lab/221640779929

[^2_6]: https://s-space.snu.ac.kr/bitstream/10371/210086/1/000000183259.pdf

[^2_7]: https://conservancy.umn.edu/server/api/core/bitstreams/e81be3bf-2cbc-4c2a-aa41-5ce4d19be951/content

[^2_8]: https://www.kriss.re.kr/main/download/club_guide23.pdf

[^2_9]: https://www.tandfonline.com/doi/pdf/10.1080/15567265.2016.1154630

[^2_10]: https://bib-pubdb1.desy.de/record/329134/files/PhysRevB.95.184305.pdf?subformat=pdfa

[^2_11]: https://www.jksmer.or.kr/articles/xml/LDrj/

[^2_12]: https://users.mrl.illinois.edu/cahill/tongji_tdtr_advanced.pdf

[^2_13]: https://www.scribd.com/document/517816603/1-5046944

[^2_14]: https://cahill.matse.illinois.edu/files/2019/03/leshouches_lecture2_mar19.pdf

[^2_15]: https://nanoheat.stanford.edu/wp-content/uploads/2022/01/Thermal-Characterization-of-Metal−Oxide-Interfaces-Using-TimeDomain-Thermoreflectance-with-Nanograting-Transducers.pdf


---

# 그러면 AlN/Si 에서의 ITR에 맞는 시료 구조는 어떤건데? NanoTR 장비에 맞는 내용을 알려줘

AlN/Si의 **직접 ITR**이 목표라면, NanoTR에서 가장 물리적으로 맞는 기본 구조는 다음입니다.

$$
\boxed{
\mathrm{Mo}(100\text{–}120\,\mathrm{nm})
/
\mathrm{AlN}(t)
/
\mathrm{Si}(100)
}
$$

즉, **상부 Mo / AlN / Si 기판** 구조입니다. AlN과 Si를 직접 맞닿게 유지해야 $G_{\mathrm{AlN/Si}}$ 또는 $R_{\mathrm{AlN/Si}}$를 모델의 관심 계면으로 설정할 수 있습니다. rear Mo를 넣는 표준 RF sandwich 구조는 AlN/Si 계면을 Mo/AlN 계면으로 바꾸므로, 원래 목표인 AlN/Si ITR을 직접적으로 주지 않습니다.

## 먼저 결론

| 목표 | 권장 NanoTR 구조 | 측정 모드 | AlN/Si ITR 직접 추출 |
| :-- | :-- | :-- | :-- |
| AlN 자체 열확산도·Mo/AlN ITR | DSP-Si / Mo(rear) / AlN / Mo(top) | 표준 RF | 불가 |
| **Direct AlN/Si ITR** | **Mo(top) / AlN / Si** | **FF** | 가능성 있음 |
| AlN/Si ITR을 RF로 시도 | DSP-Si / Mo(rear) / thin-Si / AlN / Mo(top) | Custom RF | 센터 custom fitting 가능 시에만 가능 |

따라서 네 질문에 대한 실무적 답은 아래입니다.

> **NanoTR의 표준 RF ITR 프로토콜만 가능하다면, AlN/Si direct ITR 측정에 맞는 표준 시료 구조는 없다.**
> AlN/Si ITR을 보려면 **FF 모드에서 Mo/AlN/Si 구조를 custom multilayer fitting** 하는 것이 우선이다.

NanoTR은 시간영역 열반사율 방식으로 얇은 film과 계면 열특성을 측정하는 장비이지만, 실제로 어떤 구조를 해석할 수 있는지는 장비 자체보다 **센터가 적용하는 fitting model과 RF/FF 프로토콜**이 결정합니다.[^3_1]

## AlN/Si용 기본 구조

### 권장 시료

$$
\boxed{
\mathrm{Mo}_{top}
/
\mathrm{AlN}
/
\mathrm{Si(100)}
}
$$

권장 세부 조건은 다음과 같습니다.


| 층 | 권장 사양 | 역할 |
| :-- | --: | :-- |
| Top Mo | 100–120 nm | Pump 흡수, probe 반사율 검출, transducer |
| AlN | 우선 300 nm, 이후 75/150/300 nm series | 관심 박막 |
| Si(100) | 단결정 Si wafer, DSP이면 더 좋음 | AlN의 실제 기판 및 관심 계면 형성층 |
| Rear Mo | 넣지 않음 | 넣으면 AlN/Si direct interface 목적과 충돌 |

열 흐름 및 계면은 아래와 같습니다.

$$
\mathrm{Mo}
\rightarrow
\mathrm{AlN}
\rightarrow
\boxed{\mathrm{AlN/Si}}
\rightarrow
\mathrm{Si}
$$

피팅 모델에는 최소한 다음 항목이 들어갑니다.

$$
R_{\mathrm{eff}}
=
R_{\mathrm{Mo/AlN}}
+
\frac{t_{\mathrm{AlN}}}{k_{\mathrm{AlN},\perp}}
+
\boxed{R_{\mathrm{AlN/Si}}}
$$

여기서 네가 궁극적으로 얻고 싶은 값은

$$
G_{\mathrm{AlN/Si}}
=
\frac{1}{R_{\mathrm{AlN/Si}}}
$$

입니다.

실제로 sputtered AlN/Si TDTR 연구에서도 **Al transducer / AlN / Si**의 3층 구조를 사용하고, multilayer heat-diffusion fitting으로 AlN의 cross-plane 열전도도와 AlN/Si thermal boundary conductance를 함께 평가했습니다. 특히 약 100 nm AlN에서는 top metal/AlN 및 AlN/Si 계면이 모두 열응답에 크게 기여하므로, 계면 분석의 sensitivity가 확보될 수 있습니다.[^3_2]

## NanoTR 모드별 판단

### FF: AlN/Si ITR을 위한 모드

FF는 위쪽 Mo에서 pump를 흡수하고, 같은 상부 Mo에서 probe로 온도를 검출합니다.

$$
\text{Pump/Probe}
\downarrow
\mathrm{Mo}
/
\mathrm{AlN}
/
\boxed{\mathrm{Si}}
$$

이 방식의 장점은 다음과 같습니다.

- AlN/Si 실제 접촉 계면이 보존됩니다.
- Si 기판이 불투명해도 됩니다.
- rear metal과 DSP support가 필요 없습니다.
- 네가 만든 **AlN/Si 박막 자체**를 그대로 평가할 수 있습니다.
- 계면 구조가 단순하여 $R_{\mathrm{AlN/Si}}$의 물리적 의미가 명확합니다.

단, FF에서 $k_{\mathrm{AlN}}$, $G_{\mathrm{Mo/AlN}}$, $G_{\mathrm{AlN/Si}}$를 모두 자유변수로 놓으면 fitting 상관성이 커질 수 있습니다. 그래서 Mo/AlN 계면 또는 AlN 열용량·두께는 reference나 독립 측정으로 제약해야 합니다.

### 표준 RF: AlN/Si ITR에는 부적합

NanoTR의 전형적인 RF sandwich 구조는 아래와 같습니다.

$$
\mathrm{DSP\text{-}Si}
/
\mathrm{Mo}_{rear}
/
\mathrm{AlN}
/
\mathrm{Mo}_{top}
$$

이 구조에서 열은 rear Mo에서 발생해 AlN을 지나 top Mo로 이동합니다.

$$
\mathrm{Mo}_{rear}
\rightarrow
\mathrm{AlN}
\rightarrow
\mathrm{Mo}_{top}
$$

따라서 분석 대상 계면은

$$
\mathrm{Mo/AlN}
\quad \text{및} \quad
\mathrm{AlN/Mo}
$$

입니다. **AlN/Si 계면은 아예 존재하지 않습니다.** 그러므로 RF 측정값을 아무리 수식으로 재배열해도 $R_{\mathrm{AlN/Si}}$를 산출할 수는 없습니다.

## 왜 custom RF도 권장하지 않는가

네가 검토한 구조는 다음과 같았습니다.

$$
\mathrm{DSP\text{-}Si}
/
\mathrm{Mo}_{rear}
/
\mathrm{Si}
/
\mathrm{AlN}
/
\mathrm{Mo}_{top}
$$

이론적으로는 AlN/Si 계면을 포함합니다. 하지만 NanoTR 표준 RF-ITR 구조가 아니라 **5층 custom multilayer 구조**가 됩니다.

이때 fitting해야 할 변수는 적어도 다음입니다.

$$
G_{\mathrm{Mo_{rear}/Si}},
\quad
k_{\mathrm{Si}},
\quad
G_{\mathrm{Si/AlN}},
\quad
k_{\mathrm{AlN}},
\quad
G_{\mathrm{AlN/Mo_{top}}}
$$

이 중 $G_{\mathrm{Si/AlN}}$만 독립적으로 추출하려면 다른 변수들을 높은 정확도로 고정하거나 별도 기준시편으로 제약해야 합니다. 특히 thin-Si layer가 단결정 Si인지, sputtered amorphous Si인지, bonding interface가 존재하는지에 따라 열전달 경로가 완전히 달라집니다.

그리고 NanoTR의 표준 RF protocol이 이 구조의 **5층 transfer-matrix fitting**과 independent $G_{\mathrm{AlN/Si}}$ fitting을 지원하지 않는다면, 시료를 만들더라도 “AlN/Si ITR”이라는 결과는 신뢰성 있게 나올 수 없습니다.

## 네 시료의 권장 구성

### 최소 의뢰 세트

AlN/Si ITR의 가능성을 가장 적은 시료로 확인하려면 다음 2장을 권합니다.


| 시료 | 구조 | 목적 |
| :-- | :-- | :-- |
| Main | Mo 100–120 nm / AlN 300 nm / Si(100) | $k_{\mathrm{AlN},\perp}$ 및 $G_{\mathrm{AlN/Si}}$ feasibility |
| Reference | Mo 100–120 nm / Si(100) | Mo film 및 Mo/Si 기준 응답 확인 |

300 nm를 첫 시료로 권하는 이유는 75 nm보다 AlN 막의 열저항 기여가 커서 $k_{\mathrm{AlN}}$ sensitivity를 얻기 쉽고, 동시에 AlN/Si 계면도 열응답에 반영될 여지가 있기 때문입니다. 다만 최종적으로 계면값을 분리하려면 thickness series가 더 유리합니다. AlN/Si TDTR 연구에서는 약 100 nm AlN에서 AlN/Si 계면 sensitivity가 특히 크고, 막이 약 1.7 µm로 두꺼워지면 해당 계면은 열적으로 둔감해진다고 보고했습니다.[^3_2]

### 권장 확장 세트

$$
\begin{aligned}
&\mathrm{Mo}/\mathrm{AlN}(75\,\mathrm{nm})/\mathrm{Si}\\
&\mathrm{Mo}/\mathrm{AlN}(150\,\mathrm{nm})/\mathrm{Si}\\
&\mathrm{Mo}/\mathrm{AlN}(300\,\mathrm{nm})/\mathrm{Si}\\
&\mathrm{Mo}/\mathrm{Si}\quad\text{reference}
\end{aligned}
$$

여기서 중요한 점은 모든 시료의 조건을 최대한 통제하는 것입니다.

- 동일 Si wafer lot
- 동일 Si pre-clean 또는 HF-last 조건
- 동일 AlN deposition recipe
- AlN 두께만 변경
- 동일 Mo target, power, pressure, deposition rate
- 가능하면 같은 Mo deposition run에서 top Mo 동시 증착
- Mo 두께 실측 및 4-point probe sheet resistance 측정
- AlN 두께와 roughness를 독립 측정
- 대표 시료의 AlN/Si 계면은 단면 TEM 또는 최소 단면 SEM으로 확인


## 센터에 확인할 문장

NanoTR 분석 담당자에게는 다음처럼 문의하는 것이 정확합니다.

> 목표는 Si(100) 위 sputtered AlN의 direct AlN/Si interfacial thermal resistance 또는 thermal boundary conductance 추출입니다.
> 시료는 Mo(100–120 nm)/AlN(75, 150, 300 nm)/Si(100) 구조로 준비할 예정입니다.
>
> 1. FF mode에서 위 3층 구조의 multilayer thermal model fitting이 가능한지,
> 2. $k_{\mathrm{AlN},\perp}$와 $G_{\mathrm{AlN/Si}}$를 fitting parameter로 설정 가능한지,
> 3. Mo/AlN 계면 conductance는 reference 또는 문헌값으로 고정·제약해야 하는지,
> 4. 권장 AlN 두께 및 최소 시료 수가 몇 개인지,
> 5. Mo/Si reference 시료가 필요한지
> 확인 부탁드립니다.

센터가 “**FF multilayer fitting 가능**”이라고 답하면, 네 시료 구조는 확정입니다.

$$
\boxed{\mathrm{Mo}/\mathrm{AlN}/\mathrm{Si}}
$$

반대로 “**RF standard ITR 구조만 가능**”이라고 답하면, NanoTR의 해당 서비스로는 direct AlN/Si ITR을 맡기지 않는 것이 맞습니다. 그 경우 RF용 Mo/AlN/Mo/DSP-Si 시료를 만들면 얻을 수 있는 것은 $G_{\mathrm{Mo/AlN}}$ 중심의 정보이지, 네가 원하는 $G_{\mathrm{AlN/Si}}$가 아닙니다.
<span style="display:none">[^3_10][^3_11][^3_12][^3_13][^3_14][^3_3][^3_4][^3_5][^3_6][^3_7][^3_8][^3_9]</span>

<div align="center">⁂</div>

[^3_1]: https://analyzing-testing.netzsch.com/ko/jepum/time-domain-thermoreflectance-analyzer-tdtr/nanotr

[^3_2]: https://poplab.stanford.edu/pdfs/Perez-SputteredAlNhighThermalK-nano23.pdf

[^3_3]: https://pubs.acs.org/doi/10.1021/acsami.3c16905

[^3_4]: https://dr.ntu.edu.sg/handle/10356/166521

[^3_5]: https://www.osti.gov/biblio/2997110

[^3_6]: https://repositories.lib.utexas.edu/server/api/core/bitstreams/510da89a-977f-4c9f-9762-db470efc997c/content

[^3_7]: https://www.sciencedirect.com/science/article/abs/pii/S0169433223000958

[^3_8]: https://eureka.ewha.ac.kr/eureka/my/cmmFileDownController.do?bizFileId=20260729T5GCFGHFHCE9\&fileId=1

[^3_9]: https://www.changwon.ac.kr/upload/electric/na/bbs_2079/ntt_1340183/doc_60957252-6b7c-4021-907b-022fd9aeb3d21720402584473.hwp

[^3_10]: https://poplab.stanford.edu/pdfs/Vaziri-AlNthermalMaterial3DICs-afm25.pdf

[^3_11]: https://jtu.ac.kr/cmsware/bbs_download.php?mv_data=aWR4PTMyNDExJnN0YXJ0UGFnZT0wJmxpc3RObz0yNzUmdGFibGU9Y3NfYmJzX2RhdGEmbmF2X2NvZGU9anR1MTcyODg4MjA5MCZjb2RlPW5vdGljZTAwNCZzZWFyY2hfaXRlbT0mc2VhcmNoX29yZGVyPSZvcmRlcl9saXN0PSZsaXN0X3NjYWxlPSZ2aWV3X2xldmVsPSZ2aWV3X2NhdGU9JnZpZXdfY2F0ZTI9%7C%7C\&download=h\&seq=1

[^3_12]: https://www.linkedin.com/posts/kyungjun-lim-702483128_highresolution-microtimedomain-thermoreflectance-activity-7450538706521718785-jyE5

[^3_13]: https://sciencetech.tistory.com/entry/박막의-열전도율과-계면-열저항-측정법

[^3_14]: https://chem.kaist.ac.kr/_res/pdfjs/web/viewer.html?url=/_files/board/20240516//8201d54335a7a0e3207bf11497adb0f8.pdf


---

# 아래의 내용들에 대한 추가 설명이 필요할거야 FF mode에서 위 3층 구조의 multilayer thermal model fitting이 가능한 경우면 역산 등의 다른 방법으로 ITR을 유도할 수 있는지의 내용이 필요하거든...

FF mode에서 위 3층 구조의 multilayer thermal model fitting이 가능한지,
kAlN,⊥k_{\mathrm{AlN},\perp}kAlN,⊥​와 GAlN/SiG_{\mathrm{AlN/Si}}GAlN/Si​를 fitting parameter로 설정 가능한지,
Mo/AlN 계면 conductance는 reference 또는 문헌값으로 고정·제약해야 하는지,
권장 AlN 두께 및 최소 시료 수가 몇 개인지,
Mo/Si reference 시료가 필요한지
확인 부탁드립니다.

가능합니다. 다만 **FF 3층 구조에서 ITR을 “역산”으로 구할 수 있는지**는 NanoTR이 단순한 열확산도 출력이 아니라, **Mo/AlN/Si 다층 모델에서 계면 conductance를 fitting parameter로 허용하는지**에 달려 있습니다.

그리고 중요한 정정이 있습니다. NETZSCH의 NanoTR 공식 사양은 FF mode의 적용 film thickness를 **1 µm 초과**로 제시합니다. 따라서 네 AlN 75/150/300 nm 시료는 FF의 표준 권장 범위 밖입니다. NanoTR이 FF와 RF 모두에서 계면 열저항 및 multilayer 분석 기능을 제공한다고 안내하지만, 75–300 nm AlN/Si를 FF로 custom fitting 해줄지는 담당 센터의 실제 모델·검증 범위 확인이 필수입니다.[^4_1][^4_2]

## ITR을 얻는 원리

FF 구조를 다음으로 둡니다.

$$
\mathrm{Mo}_{top}/\mathrm{AlN}(t_{\mathrm{AlN}})/\mathrm{Si}
$$

열저항 관점에서는 대략 다음과 같습니다.

$$
R_{\mathrm{eff}}
=
R_{\mathrm{Mo/AlN}}
+
\frac{t_{\mathrm{AlN}}}{k_{\mathrm{AlN},\perp}}
+
R_{\mathrm{AlN/Si}}
$$

여기서 관심값은

$$
R_{\mathrm{AlN/Si}}=\frac{1}{G_{\mathrm{AlN/Si}}}
$$

입니다.

TDTR/NanoTR은 열반사율 시간응답을 다층 열확산 모델과 비교해 fitting합니다. 일반적으로 cross-plane 열전도도 $k_\perp$와 계면 conductance $G$는 TDTR 신호에 서로 다른 방식으로 영향을 주므로, 조건이 좋으면 한 측정 세트에서도 동시에 fitting할 수 있습니다. 다만 실제 신뢰도는 sensitivity와 parameter correlation에 좌우됩니다.[^4_3]

### 직접 fitting

가장 좋은 방식은 NanoTR fitting model에서 아래를 직접 넣는 것입니다.

$$
\begin{aligned}
&k_{\mathrm{AlN},\perp} &&\text{: free 또는 제한된 fitting parameter}\\
&G_{\mathrm{AlN/Si}} &&\text{: 핵심 fitting parameter}\\
&G_{\mathrm{Mo/AlN}} &&\text{: reference/문헌값으로 고정 또는 제한}
\end{aligned}
$$

이 경우 “역산”은 필요 없습니다. 모델이 시간영역 데이터 전체를 이용하여 $k_{\mathrm{AlN},\perp}$와 $G_{\mathrm{AlN/Si}}$를 직접 최적화합니다.

### 단순 역산

만약 센터가 다층 fitting 결과로 유효 열저항 $R_{\mathrm{eff}}$만 제공한다면, 원리적으로는 다음처럼 계산할 수 있습니다.

$$
\boxed{
R_{\mathrm{AlN/Si}}
=
R_{\mathrm{eff}}
-
R_{\mathrm{Mo/AlN}}
-
\frac{t_{\mathrm{AlN}}}{k_{\mathrm{AlN},\perp}}
}
$$

하지만 이것은 **보조 검산용**으로만 쓰는 편이 좋습니다.

- $R_{\mathrm{eff}}$, $R_{\mathrm{Mo/AlN}}$, $t/k$의 오차가 모두 마지막 값에 누적됩니다.
- AlN이 얇을수록 $\frac{t_{\mathrm{AlN}}}{k_{\mathrm{AlN}}}$가 작아져 두 계면 저항을 분리하기 어려워집니다.
- 결과적으로 큰 두 값의 차이로 작은 $R_{\mathrm{AlN/Si}}$를 구하는 상황이 생길 수 있습니다.
- 따라서 문헌 수준의 ITR 주장은 단순 차감보다 **global multilayer fitting + sensitivity/uncertainty analysis**가 훨씬 강합니다.


## 두께 series의 역할

두께가 다른 $n$개 시료가 있고, AlN 공정과 두 계면 상태가 충분히 동일하다고 가정하면,

$$
R_{\mathrm{eff},i}
=
R_{\mathrm{Mo/AlN}}
+
R_{\mathrm{AlN/Si}}
+
\frac{t_{\mathrm{AlN},i}}{k_{\mathrm{AlN},\perp}}
$$

로 쓸 수 있습니다.

이를 두께 $t_{\mathrm{AlN}}$에 대해 선형적으로 보면:

$$
R_{\mathrm{eff}}
=
\left(
R_{\mathrm{Mo/AlN}}
+
R_{\mathrm{AlN/Si}}
\right)
+
\frac{1}{k_{\mathrm{AlN},\perp}}t_{\mathrm{AlN}}
$$

- **기울기** $=1/k_{\mathrm{AlN},\perp}$
- **절편** $=R_{\mathrm{Mo/AlN}}+R_{\mathrm{AlN/Si}}$

즉, 75/150/300 nm 두께 series는 $k_{\mathrm{AlN},\perp}$와 **두 계면 저항의 합**을 구하는 데 유리합니다.

하지만 이것만으로는 절편을 아래처럼 분리할 수 없습니다.

$$
R_{\mathrm{Mo/AlN}}+R_{\mathrm{AlN/Si}}
\;\not\Rightarrow\;
R_{\mathrm{AlN/Si}}
$$

따라서 $R_{\mathrm{AlN/Si}}$만 얻으려면 다음 중 적어도 하나가 필요합니다.

- $R_{\mathrm{Mo/AlN}}$를 독립 기준시료나 신뢰할 수 있는 문헌값으로 제약
- NanoTR 다층 fitting에서 $G_{\mathrm{Mo/AlN}}$와 $G_{\mathrm{AlN/Si}}$에 대한 sensitivity가 충분히 다르도록 조건 설정
- 서로 다른 modulation frequency 또는 다중 측정 조건에서 global fitting
- Mo/AlN 계면은 같은 상태로 유지하고, AlN/Si 계면만 의도적으로 달리 만든 control sample 비교

여러 modulation frequency를 활용한 TDTR은 열전도도와 계면 열저항 추출의 불확실성을 낮추는 데 유효한 방법으로 보고되어 있습니다.[^4_4][^4_3]

## Reference 시료의 정확한 역할

### Mo/Si reference는 필요하지만 충분하지는 않음

$$
\mathrm{Mo}/\mathrm{Si}
$$

이 시료는 다음에 유용합니다.

- 실제 증착된 Mo의 두께·열확산 응답 확인
- Mo film의 실측 열물성 또는 모델 입력값 보정
- Mo/Si 계면 conductance 평가 또는 reference response 확보
- Si 기판과 Mo transducer 조합의 baseline 확인

그러나 **Mo/Si reference만으로 $G_{\mathrm{Mo/AlN}}$를 알 수는 없습니다.**

$$
G_{\mathrm{Mo/Si}}
\neq
G_{\mathrm{Mo/AlN}}
$$

따라서 Mo/Si는 필요한 보조 기준시편이지만, AlN/Si ITR의 분리 문제를 혼자 해결하지는 못합니다.

### Mo/AlN 계면 제약용 시료

Mo/AlN 계면을 따로 제약하려면, main sample과 **동일한 AlN surface 및 동일 Mo deposition 조건**을 가져야 합니다. 후보는 아래와 같습니다.


| 시료 | 얻는 정보 | 한계 |
| :-- | :-- | :-- |
| Mo/Si | Mo 물성, Mo/Si baseline | Mo/AlN 계면값은 못 구함 |
| Mo/AlN/Si, 두께 series | $k_{\mathrm{AlN}}$ 및 두 계면 합의 제약 | 두 계면을 자동 분리하지는 못함 |
| Mo/AlN/known substrate | Mo/AlN 계면 제약 가능성 | substrate/하부 계면의 값이 충분히 알려져야 함 |
| 동일 AlN 위 Mo만 바꾼 control | top-interface 변화 비교 | 시료 수·공정 관리 증가 |

실무적으로는 **두께 series 3개 + Mo/Si reference 1개**를 먼저 준비하고, 센터가 $G_{\mathrm{Mo/AlN}}$를 어떤 방식으로 취급하는지 답한 뒤에 추가 control을 결정하는 편이 낫습니다.

## NanoTR에 꼭 확인할 질문

메일에는 아래처럼 “가능 여부”와 “가능할 경우 어떤 fitting strategy를 쓰는지”를 분리해 물어보는 것이 좋습니다.

> 목표는 Mo/AlN/Si 구조에서 direct AlN/Si interfacial thermal resistance $R_{\mathrm{AlN/Si}}$, 또는 thermal boundary conductance $G_{\mathrm{AlN/Si}}$를 정량화하는 것입니다.
>
> 현재 계획 구조는 Mo(100–120 nm)/AlN(75, 150, 300 nm)/Si(100)이며, AlN/Si 계면을 실제 관심 계면으로 유지하고자 합니다.
>
> 1. NanoTR의 FF mode에서 위 3층 구조에 대해 **multilayer thermal-diffusion fitting**이 가능한지 문의드립니다.
>
> 2. FF mode에서 AlN 두께가 75–300 nm인 경우에도 분석이 가능한지, 또는 공식 FF 권장 두께인 1 µm 이상 조건이 필수인지 확인 부탁드립니다.
>
> 3. fitting 시 $k_{\mathrm{AlN},\perp}$와 $G_{\mathrm{AlN/Si}}$를 동시에 fitting parameter로 둘 수 있는지 문의드립니다. 가능하다면, 두 parameter의 sensitivity 및 correlation analysis도 제공 가능한지 확인 부탁드립니다.
>
> 4. 상부 Mo/AlN 계면 conductance $G_{\mathrm{Mo/AlN}}$는 fitting에서 고정값으로 두어야 하는지, 문헌값 또는 reference sample을 통해 제약하는 방식이 필요한지 문의드립니다.
>
> 5. 단일 주파수 또는 단일 시료 분석만으로 $G_{\mathrm{AlN/Si}}$를 분리할 수 있는지, 아니면 다중 modulation condition 및 두께 series global fitting이 필요한지 확인 부탁드립니다.
>
> 6. Mo/Si reference 시료가 필요한지, 필요하다면 Mo/Si reference가 Mo film 물성 보정용인지 또는 Mo/Si 계면 conductance 추출용인지 확인 부탁드립니다.
>
> 7. AlN 75/150/300 nm series와 Mo/Si reference를 제출할 경우, $k_{\mathrm{AlN},\perp}$, $G_{\mathrm{Mo/AlN}}$, $G_{\mathrm{AlN/Si}}$ 중 각각 어떤 값을 독립적으로 추출할 수 있는지 문의드립니다.

## 현실적인 판단 기준

센터의 답변이 아래와 같으면 진행할 수 있습니다.

- “FF에서 75–300 nm AlN도 custom multilayer model로 가능”
- “$k_{\mathrm{AlN},\perp}$와 $G_{\mathrm{AlN/Si}}$ fitting 가능”
- “$G_{\mathrm{Mo/AlN}}$는 reference 또는 literature prior로 제약 가능”
- “sensitivity 및 fitting uncertainty 제공 가능”

반대로 아래와 같다면 NanoTR FF로는 지금의 75–300 nm AlN/Si ITR 목표가 어렵습니다.

- “FF는 1 µm 이상 film만 가능”
- “standard output은 thermal diffusivity만 제공”
- “interface resistance는 RF sandwich 구조에서만 가능”
- “3층 이상의 custom fitting 불가”
- “$G_{\mathrm{Mo/AlN}}$와 $G_{\mathrm{AlN/Si}}$ 분리 불가”

이 경우 75–300 nm AlN/Si의 direct ITR을 NanoTR 표준 의뢰만으로 얻으려는 계획은 멈추고, custom TDTR fitting이 가능한 기관이나 기법을 찾는 것이 맞습니다.
<span style="display:none">[^4_10][^4_11][^4_12][^4_13][^4_14][^4_15][^4_5][^4_6][^4_7][^4_8][^4_9]</span>

<div align="center">⁂</div>

[^4_1]: https://analyzing-testing.netzsch.com/en/products/time-domain-thermoreflectance-analyzer-tdtr/nanotr

[^4_2]: https://analyzing-testing.netzsch.com/ko/beulrogeu/2023/nanotr-yalbeun-ceungyi-yeol-teugseonghwareul-wihan-seupaen-seupaen-seupaen-gyeceuggi-rain-picotr-nbsp-span-span-instrument-line-for-the-thermal-characterization-of-thin-layers

[^4_3]: https://pubs.aip.org/aip/jap/article/124/16/161103/1030095/Tutorial-Time-domain-thermoreflectance-TDTR-for

[^4_4]: https://dr.ntu.edu.sg/handle/10356/166521

[^4_5]: https://pubs.aip.org/aip/jap/article/124/14/144301/155489/Measurement-and-multilayer-model-of-cooling-of

[^4_6]: https://arxiv.org/abs/2404.02707v3

[^4_7]: https://scienceon.kisti.re.kr/srch/selectPORSrchArticle.do?cn=NART74634330

[^4_8]: https://www.sciencedirect.com/science/article/am/pii/S0017931015300624

[^4_9]: https://arxiv.org/abs/1708.03809

[^4_10]: https://www.arxiv.org/abs/2411.15767

[^4_11]: https://www.science.gov/topicpages/t/time-domain+thermoreflectance+tdtr

[^4_12]: https://irel.jp/pdf/NCCG43Poster.pdf

[^4_13]: https://scispace.com/pdf/impedance-spectroscopy-of-al-aln-n-si-metal-insulator-25g5w8t873.pdf

[^4_14]: https://irel.jp/pdf/Nanoepi2015_Poster.pdf

[^4_15]: https://www.linkedin.com/posts/kyungjun-lim-702483128_highresolution-microtimedomain-thermoreflectance-activity-7450538706521718785-jyE5


---

# 아래의 두 개 제목에 대한 논문을 확인하면 좋을듯 해

1. Thermal characterization of buried interfaces in multilayer heterostructures via TDTR with periodic waveform analysis
2. Thermal Transport at the AlN−SiC Interface and Grain Boundary of AlN

네. 두 논문은 지금 고민 중인 **“매립된 AlN/Si 계면을 TDTR로 분리할 수 있는가”**와 **“AlN 막질·결함이 열전도도 및 계면 TBR에 어떻게 반영되는가”**를 각각 다른 층위에서 보완해 줍니다. 다만 네 NanoTR 의뢰 설계에 가장 직접적인 근거는 1번이고, 2번은 공정·계면 품질을 해석하는 물리적 근거로 쓰는 것이 맞습니다.

## 논문별 핵심

| 논문 | 성격 | 네 연구에 주는 핵심 |
| :-- | :-- | :-- |
| *Thermal Characterization of Buried Interfaces in Multilayer Heterostructures via TDTR with Periodic Waveform Analysis* | 실험 TDTR 방법론 | 다층 구조에서 주파수별 sensitivity를 다르게 만들어 buried interface의 $G$, 각 층 $k$, 체적비열 $C_v$를 joint fitting으로 분리 |
| *Thermal Transport at the AlN–SiC Interface and Grain Boundary of AlN* | DFT/NEGF 기반 이론 연구 | AlN 계면과 AlN grain boundary의 TBR은 vacancy·O impurity·원자 혼입·질량 불일치에 민감하며, 공정 중 O 제어가 중요 |

## 1번: 네 구조 논의에 가장 중요

첫 논문은 2026년 4월 공개된 Zhang, Jiang, Yang의 PWA-TDTR 연구입니다. 핵심은 기존 TDTR처럼 단일 또는 제한된 고주파 조건만 사용하는 대신, **넓은 modulation-frequency 범위에서 측정하고, 각 주파수의 sensitivity를 이용해 공동 fitting**을 수행한 것입니다. 이를 통해 $\epsilon$-Ga$_2$O$_3$/SiC, GaN/Si, bonded GaN/diamond 같은 다층 구조의 buried interface를 비파괴적으로 분석했습니다.[^5_1]

### 왜 네 AlN/Si 구조와 연결되는가

네 기본 구조는 다음입니다.

$$
\mathrm{Mo}/\mathrm{AlN}/\mathrm{Si}
$$

여기서 TDTR 신호는 다음 항의 결합으로 나타납니다.

$$
R_{\mathrm{eff}}
=
R_{\mathrm{Mo/AlN}}
+
\frac{t_{\mathrm{AlN}}}{k_{\mathrm{AlN},\perp}}
+
R_{\mathrm{AlN/Si}}
$$

문제는 한 조건만 측정하면 $k_{\mathrm{AlN},\perp}$, $G_{\mathrm{Mo/AlN}}$, $G_{\mathrm{AlN/Si}}$가 서로 상관되어, 하나의 결과로 깔끔히 분리하기 어렵다는 것입니다.

1번 논문이 제시하는 해법은 다음입니다.

$$
\boxed{
\text{다중 주파수 데이터}
+
\text{sensitivity-guided joint fitting}
+
\text{두께 series}
}
$$

즉, 각 주파수에서 열 침투 깊이가 달라진다는 점을 이용합니다.

$$
\delta(f)
\approx
\sqrt{\frac{k}{\pi C_vf}}
$$

- 높은 주파수: 표면 Mo/AlN, AlN 막 자체에 상대적으로 민감
- 낮은 주파수: 열 침투 깊이가 커져 AlN/Si buried interface와 Si substrate 영향이 증가
- 여러 주파수 데이터: $k_{\mathrm{AlN},\perp}$와 $G_{\mathrm{AlN/Si}}$의 sensitivity를 분리할 가능성 증가

이 논문은 GaN/Si 전이층을 단일 유효층으로 모델링하고, 94.0 및 250.0 kHz 데이터의 joint fitting으로 transition layer와 Si substrate의 열물성을 분리했습니다. 또한 23.5 kHz의 저주파 PWA-TDTR로 약 24 µm 깊이에 위치한 GaN/diamond 계면의 conductance를 추출했습니다.[^5_1]

### 네가 이 논문에서 가져와야 할 논리

NanoTR 센터에 단순히 “AlN/Si ITR 측정 가능한가요?”라고만 묻기보다, 아래의 조건을 확인해야 합니다.

> Mo/AlN/Si 구조에서 AlN/Si buried interface의 thermal boundary conductance를 추출하고자 합니다.
> 단일 조건 fitting이 아니라, 여러 측정 조건 또는 복수 주파수 기반 sensitivity analysis 및 joint fitting이 가능한지 문의드립니다.
>
> 특히 $k_{\mathrm{AlN},\perp}$, $G_{\mathrm{Mo/AlN}}$, $G_{\mathrm{AlN/Si}}$의 parameter correlation을 평가하고, AlN/Si 계면에 대한 sensitivity가 확보되는 주파수 범위를 설정할 수 있는지 확인 부탁드립니다.

다만 중요한 한계가 있습니다. 이 논문의 PWA-TDTR은 **50 Hz 수준까지 접근 가능한 frequency-tunable waveform 분석**을 핵심으로 합니다. 일반 NanoTR의 표준 RF/FF 운용이 같은 주파수 가변 범위, 파형 취득 방식, joint fitting 기능을 제공한다고 볼 수는 없습니다. 즉, 논문은 “원리적으로 가능하다”는 강한 근거이지만, NanoTR 표준 서비스가 그대로 구현할 수 있다는 보증은 아닙니다.[^5_1]

## 2번: 공정 해석용으로 중요

두 번째 논문은 AlN/SiC 계면과 AlN inversion domain boundary의 열저항을 **NEGF와 first-principles 계산**으로 분석한 이론 연구입니다. 따라서 Mo/AlN/Si의 NanoTR fitting 절차를 직접 제안하는 실험 논문은 아닙니다. 그러나 네 RF sputtered AlN의 결과를 해석하는 데는 매우 유용합니다.[^5_2]

논문의 핵심은 다음입니다.

- AlN/SiC 계면 및 AlN grain boundary의 열저항은, 같은 두께의 bulk AlN·SiC 자체 열저항보다 클 수 있습니다.
- 계면 원자 혼입, vacancy, 산소 관련 결함이 열전달을 크게 떨어뜨릴 수 있습니다.
- 특히 $V_{\mathrm{Al}}+3O_{\mathrm{N}}$ 형태의 charge-balanced defect가 열저항 증가와 관련되며, 산소 농도가 높아지면 Al vacancy 형성을 촉진할 수 있다고 분석했습니다.[^5_2]


### 네 AlN/Si에 대한 해석

AlN/SiC와 AlN/Si는 서로 다른 계면이므로, 이 논문의 TBR 절대값을 네 결과에 그대로 적용하면 안 됩니다. 그러나 아래의 해석 틀은 직접 가져올 수 있습니다.

$$
\text{높은 }R_{\mathrm{AlN/Si}}
\quad\Longleftrightarrow\quad
\text{계면 산화층, O/C 오염, vacancy, 저밀도 초기 nucleation layer, roughness}
$$

즉, 네가 AlN/Si에서 낮은 $G_{\mathrm{AlN/Si}}$ 또는 높은 $R_{\mathrm{AlN/Si}}$를 얻는다면, 단순히 “AlN과 Si의 고유 phonon mismatch”만으로 설명하면 부족합니다. 아래를 함께 확인해야 합니다.

- Si native oxide의 존재와 두께
- HF-last 후 AlN 증착까지의 air exposure 시간
- pre-sputtering 중 기판이 plasma에 노출된 조건
- AlN 초기 nucleation 조건
- Ar ion bombardment에 따른 Si surface damage
- Al:N 비율 및 O contamination
- AlN/Si 계면의 비정질 interlayer
- AlN (0002) texture, grain size, mosaicity
- RMS roughness와 interfacial roughness


## Perez 논문도 함께 봐야 함

네 경우에는 위 두 논문에 더해, Perez et al.의 **“High Thermal Conductivity of Submicrometer Aluminum Nitride Thin Films Sputter-Deposited at Low Temperature”**가 가장 직접적인 실험 선행연구입니다.

이 논문은 Al transducer/AlN/Si(111) 구조의 TDTR 모델에서 Al/AlN 계면 $G_1$, AlN/Si 계면 $G_2$, AlN cross-plane thermal conductivity를 함께 다뤘습니다. 특히 100 nm AlN에서는 top Al/AlN 및 buried AlN/Si 두 계면이 모두 열응답에 크게 기여하지만, 1.7 µm AlN에서는 AlN/Si 계면 sensitivity가 낮아진다고 명시합니다.[^5_3]

즉, 네가 준비하려는 75/150/300 nm AlN은 “AlN/Si 계면 sensitivity” 확보 측면에서는 오히려 의미가 있습니다.


| AlN 두께 | AlN/Si ITR sensitivity | $k_{\mathrm{AlN}}$ 안정 추출 | 역할 |
| --: | :-- | :-- | :-- |
| 75 nm | 높을 가능성 | 낮거나 parameter correlation 큼 | 계면 민감 시료 |
| 150 nm | 높음 | 중간 | 계면 중심 시료 |
| 300 nm | 중간 | 상대적으로 좋음 | 첫 feasibility 시료 |
| 600 nm 이상 | 감소 가능성 | 좋음 | $k_{\mathrm{AlN}}$ 중심 시료 |
| 1 µm 이상 | 낮음 | 좋음 | AlN 막 자체 물성 중심 시료 |

Perez 논문은 100, 300, 647, 800, 1156, 1735 nm AlN/Si series를 실제로 분석했고, 100 nm와 300 nm 시료에서 각각 $18.7\pm4.6$, $25.5\pm4.7$ W m$^{-1}$ K$^{-1}$의 cross-plane 열전도도를 보고했습니다. 그 연구는 10 MHz TDTR, 다층 3D 열확산 모델 및 sensitivity analysis를 사용했습니다.[^5_3]

## 네 시료 전략에 적용

따라서 현재 네가 준비해야 할 최적의 논문 기반 전략은 아래에 가깝습니다.

$$
\boxed{
\mathrm{Mo}(100\text{–}120\,\mathrm{nm})
/
\mathrm{AlN}(75,150,300\,\mathrm{nm})
/
\mathrm{Si(100)}
}
$$

그리고 반드시 다음을 병행합니다.

- 동일 AlN 공정에서 두께만 바꾼 75/150/300 nm series
- 동일 Mo deposition run에서 제작한 Mo/Si reference
- AlN 두께의 독립 측정: ellipsometry, XRR 또는 단면 SEM
- Mo 두께의 독립 측정 및 sheet resistance 확인
- AlN surface roughness: AFM
- AlN (0002) orientation과 FWHM: XRD
- 가능하면 대표 시료의 단면 TEM/STEM-EDS
- Si native oxide 및 AlN/Si interlayer 상태 확인
- TDTR fitting 전 sensitivity analysis
- 가능한 범위에서 다중 frequency 또는 다중 measurement condition fitting

다만 NanoTR 표준 FF의 공식 두께 권장조건과 네 75–300 nm 시료 사이에는 여전히 간극이 있습니다. 따라서 이 논문들은 **Mo/AlN/Si 구조 및 ITR 분리의 과학적 타당성**을 분명히 뒷받침하지만, NanoTR의 표준 FF 서비스에서 동일 수준의 fitting이 가능한지는 별도 확인이 필요합니다. NanoTR 센터가 multi-condition fitting, sensitivity analysis, 그리고 $G_{\mathrm{AlN/Si}}$ 독립 parameter fitting을 제공하는지가 실제 진행 여부를 결정합니다.
<span style="display:none">[^5_10][^5_11][^5_12][^5_13][^5_14][^5_15][^5_4][^5_5][^5_6][^5_7][^5_8][^5_9]</span>

<div align="center">⁂</div>

[^5_1]: https://arxiv.org/abs/2604.12539

[^5_2]: https://pubs.acs.org/doi/10.1021/acsami.4c07327

[^5_3]: https://kummelgroup.ucsd.edu/pubs/papers_2023/Perex%20Mcleod%20AlN%20Thermal%20Conductivity%20ACS%20Nano%202023.pdf

[^5_4]: https://pmc.ncbi.nlm.nih.gov/articles/PMC13258771/

[^5_5]: https://pubs.acs.org/doi/abs/10.1021/acsami.2c17661

[^5_6]: https://pmc.ncbi.nlm.nih.gov/articles/PMC12808098/figure/Fig3/

[^5_7]: https://arxiv.org/list/cond-mat.mtrl-sci/recent?skip=91\&show=250

[^5_8]: https://www.sciencedirect.com/science/article/pii/S2542529325003438

[^5_9]: https://arxiv.org/pdf/2103.08084.pdf

[^5_10]: https://www.sciencedirect.com/science/article/pii/S2542529326000489

[^5_11]: https://arxiv.org/abs/2510.11936

[^5_12]: https://www.themoonlight.io/ko/review/thermal-characterization-of-buried-interfaces-in-multilayer-heterostructures-via-tdtr-with-periodic-waveform-analysis

[^5_13]: https://www.themoonlight.io/en/review/thermal-characterization-of-buried-interfaces-in-multilayer-heterostructures-via-tdtr-with-periodic-waveform-analysis

[^5_14]: https://patrickehopkins.com/wp-content/uploads/2024/08/li2024aa.pdf

[^5_15]: https://scispace.com/pdf/using-mosaicity-to-tune-thermal-transport-in-polycrystalline-vbtmeipjku.pdf


---

# 이를 통해 내가 분석을 위해 전체 준비해야하는 시료의 개수와 시료 구조들에 대해 설명을 얻고 싶은데??

네 목표가 **AlN/Si direct ITR**이라면, “3개 두께 시료만”으로 끝내기보다 **최소 5개, 권장은 6개 열분석 시료**로 계획하는 것이 맞습니다. 단, 이것은 NanoTR 센터가 **FF mode에서 Mo/AlN/Si의 custom multilayer fitting과 sub-µm AlN 분석**을 지원한다고 확인한 경우의 구성입니다.

중요하게도 NanoTR의 공개 사양은 FF 방식의 권장 film thickness를 **1 µm 이상**으로 제시하고, RF 방식은 ceramic layer에 대해 약 300 nm 이상을 제시합니다. 하지만 RF 표준 구조에서는 AlN/Si 계면이 rear Mo/AlN 계면으로 대체되므로, 현재의 75–300 nm AlN/Si direct ITR 목표에는 맞지 않습니다.[^6_1][^6_2]

## 최종 권장 시료 수

### 최소: 열분석용 5개

| ID | 구조 | AlN 두께 | 핵심 역할 |
| :-- | :-- | --: | :-- |
| S-75 | Mo / AlN / Si(100) | 75 nm | AlN/Si 계면 sensitivity가 가장 큰 시료 |
| S-150 | Mo / AlN / Si(100) | 150 nm | 계면과 AlN 막 저항의 중간 조건 |
| S-300 | Mo / AlN / Si(100) | 300 nm | $k_{\mathrm{AlN},\perp}$ 추출 안정성 향상 |
| S-1000 | Mo / AlN / Si(100) | 1.0–1.5 µm | AlN bulk-like $k_\perp$ 및 Mo/AlN 상부 계면 제약용 |
| Ref-Mo/Si | Mo / Si(100) | — | Mo transducer 및 Mo/Si baseline 확인 |

모든 Mo는 가능하면 동일 조건과 동일 run에서 증착합니다.

$$
t_{\mathrm{Mo}}
=
100\text{–}120\,\mathrm{nm}
$$

이 5개가 “직접 AlN/Si ITR을 분리하려는” 최소한의 분석 세트입니다.

### 권장: 열분석용 6개

| ID | 구조 | 목적 |
| :-- | :-- | :-- |
| S-75 | Mo / AlN(75 nm) / Si | 얇은 AlN, buried AlN/Si 계면 sensitivity |
| S-150 | Mo / AlN(150 nm) / Si | 계면–막 저항 분리용 |
| S-300 | Mo / AlN(300 nm) / Si | $k_{\mathrm{AlN},\perp}$ 및 ITR 균형 조건 |
| S-1000 | Mo / AlN(1.0–1.5 µm) / Si | $k_{\mathrm{AlN},\perp}$, Mo/AlN 계면 제약 |
| Ref-Mo/Si | Mo / Si | Mo film 및 Mo/Si baseline |
| Repeat-300 | Mo / AlN(300 nm) / Si | 재현성·공정 산포·uncertainty 평가 |

여기서 **Repeat-300**은 단순 여분이 아닙니다. TDTR/NanoTR 결과는 laser spot, Mo thickness, roughness, AlN 두께, 위치별 grain structure에 영향을 받으므로, 대표 두께 조건에서 독립 증착 또는 독립 wafer 위치의 반복 시료가 있어야 논문 수준의 재현성을 확보할 수 있습니다.

실제 AlN/Si TDTR 연구에서도 복수 시료와 다수 위치에서 측정했고, 각 그룹당 3개 시료 및 총 9개 지점을 사용해 통계적 신뢰도를 확보했습니다. 또한 AlN 두께는 ellipsometry, Al transducer는 acoustic measurement, buried interface는 TEM으로 독립 확인했습니다.[^6_3]

## 각 시료가 필요한 이유

### S-75, S-150, S-300: 핵심 ITR 시료

세 시료의 기본 구조는 동일합니다.

$$
\boxed{
\mathrm{Mo}(100\text{–}120\,\mathrm{nm})
/
\mathrm{AlN}(75,150,300\,\mathrm{nm})
/
\mathrm{Si}(100)
}
$$

이들은 다음 관계를 분석하는 데 사용됩니다.

$$
R_{\mathrm{eff},i}
=
R_{\mathrm{Mo/AlN}}
+
\frac{t_{\mathrm{AlN},i}}{k_{\mathrm{AlN},\perp}}
+
R_{\mathrm{AlN/Si}}
$$

- 75 nm: AlN/Si 계면의 열적 기여가 상대적으로 크므로 $G_{\mathrm{AlN/Si}}$ sensitivity가 높아질 가능성이 큽니다.
- 150 nm: 계면저항과 AlN 막 저항이 함께 반영되는 중간 조건입니다.
- 300 nm: AlN 자체 열저항이 커져 $k_{\mathrm{AlN},\perp}$ 추출이 상대적으로 안정적입니다.

선행 AlN/Si TDTR 연구에서도 약 100 nm AlN에서는 Al/AlN 및 AlN/Si 계면이 모두 thermal response에 크게 기여했으며, 막이 약 1.7 µm까지 두꺼워지면 AlN/Si 계면 sensitivity가 매우 낮아졌습니다.[^6_4]

### S-1000: 상부 계면·AlN 열전도도 제약용

$$
\mathrm{Mo}/\mathrm{AlN}(1.0\text{–}1.5\,\mu\mathrm{m})/\mathrm{Si}
$$

이 시료는 AlN/Si ITR을 직접 뽑기 위한 주력 시료는 아닙니다. 오히려 다음 목적입니다.

- NanoTR FF 공식 권장 두께인 1 µm 이상 조건에서 분석 가능성 검증
- AlN film 자체의 $k_{\mathrm{AlN},\perp}$ 추정 정확도 향상
- $G_{\mathrm{Mo/AlN}}$을 fitting에서 제약할 보조 데이터 확보
- 75–300 nm 시료 fitting에서 $k_{\mathrm{AlN},\perp}$와 $G_{\mathrm{AlN/Si}}$의 상관성을 낮춤

단, 두꺼운 AlN은 얇은 AlN과 grain size, stress, density, texture가 달라질 수 있습니다. 그러므로 S-1000에서 얻은 $k_{\mathrm{AlN}}$을 75 nm 시료에 무조건 고정하면 안 됩니다. **초기값 또는 합리적 범위**로 사용하고, XRD·AFM·density 차이를 함께 확인해야 합니다.

### Ref-Mo/Si: 꼭 필요하지만 ITR 답은 아님

$$
\mathrm{Mo}(100\text{–}120\,\mathrm{nm})/\mathrm{Si}(100)
$$

이 기준시료는 다음을 확인합니다.

- 실제 증착된 Mo film의 열응답
- Mo 두께 및 transducer model 정확성
- Mo/Si 계면 conductance
- bare Si 위 Mo의 baseline signal
- main sample에서 Mo 관련 parameter uncertainty 제약

하지만 아래는 성립하지 않습니다.

$$
G_{\mathrm{Mo/Si}}
\neq
G_{\mathrm{Mo/AlN}}
$$

따라서 Ref-Mo/Si 하나만으로 $G_{\mathrm{Mo/AlN}}$를 결정할 수는 없습니다. 이 시료는 **Mo transducer의 기준값을 잡기 위한 필수 reference**이지, AlN/Si ITR을 역산해 주는 직접 reference는 아닙니다.

### Repeat-300: 신뢰도 확보용

$$
\mathrm{Mo}/\mathrm{AlN}(300\,\mathrm{nm})/\mathrm{Si}
$$

S-300과 같은 구조를 하나 더 만드는 이유는 다음과 같습니다.

- AlN deposition run 간 재현성 확인
- Mo thickness variation 영향 평가
- sample-to-sample error bar 확보
- TDTR/NanoTR 위치별 산포와 시료 간 산포 구분
- 향후 논문에서 “한 시료의 한 지점 결과”라는 약점을 피함


## 시료 외 필수 witness

열분석용 test structure 외에, 별도 witness coupon도 준비해야 합니다. 이들은 NanoTR에 반드시 제출하지 않아도 되지만, fitting 입력값과 결과 해석을 위해 필요합니다.


| Witness | 구조 | 필요한 분석 |
| :-- | :-- | :-- |
| W-75 | AlN(75 nm)/Si | 두께, AFM, XRD, XPS |
| W-150 | AlN(150 nm)/Si | 두께, AFM, XRD |
| W-300 | AlN(300 nm)/Si | 두께, AFM, XRD, 단면 SEM |
| W-1000 | AlN(1–1.5 µm)/Si | XRD, AFM, 단면 SEM |
| W-Mo | Mo/Si 또는 glass/Si | Mo deposition rate, thickness, sheet resistance |

대표적으로 W-300 또는 W-1000 중 하나는 가능하면 단면 TEM/STEM-EDS까지 수행하는 것이 좋습니다. 특히 네 핵심 결과가 $G_{\mathrm{AlN/Si}}$라면, 실제 계면에 native oxide, O-rich layer, 저밀도 nucleation layer가 존재하는지를 확인해야 하기 때문입니다. TDTR 기반 AlN-Si 연구에서는 AlN/Si 계면층의 두께를 TEM으로 확인한 뒤 그 값을 thermal model에 반영했습니다.[^6_3]

## 실제 제작 장수

웨이퍼 조각 기준으로 정리하면 다음입니다.


| 구분 | 최소 장수 | 권장 장수 |
| :-- | --: | --: |
| NanoTR 열분석용 Mo-coated sample | 5장 | 6장 |
| Mo 없는 AlN/Si witness coupon | 4장 | 4장 |
| Mo deposition calibration coupon | 1장 | 1장 |
| 총 제작 coupon | **10장** | **11장** |

다만 여러 coupon을 한 장의 동일 wafer에서 함께 만들 수 있으므로, 반드시 wafer 10장을 쓴다는 뜻은 아닙니다. 예를 들어 각 AlN 두께별 wafer에서 중앙부는 NanoTR용, 가장자리 또는 별도 diced coupon은 XRD/AFM/ellipsometry용으로 활용할 수 있습니다.

## NanoTR 기준 최종 분기

이 시료 세트는 아래 조건에서만 진행하세요.

$$
\boxed{
\text{FF custom multilayer fitting 가능}
\land
\text{sub-}\mu\mathrm{m}\;\mathrm{AlN}\text{ 분석 가능}
\land
G_{\mathrm{AlN/Si}}\text{ sensitivity 확인 가능}
}
$$

센터가 이 세 조건을 충족한다고 답하면, **권장 세트는 NanoTR 6장 + witness 5개**입니다.

반대로 센터가 “FF는 1 µm 이상만 가능” 또는 “RF standard ITR만 가능”이라고 답하면, 75/150/300 nm AlN/Si direct ITR을 위한 NanoTR 시료를 지금 만들면 안 됩니다. 그때는 RF용으로 별도 구조를 만들더라도 얻는 계면값은 AlN/Si가 아니라 Mo/AlN이 되므로, 네 연구 목표와 달라집니다.
<span style="display:none">[^6_10][^6_11][^6_12][^6_13][^6_14][^6_15][^6_5][^6_6][^6_7][^6_8][^6_9]</span>

<div align="center">⁂</div>

[^6_1]: https://analyzing-testing.netzsch.com/ko/products/sigan-domein-deomobansayul-bunseoggi-tdtr/nanotr

[^6_2]: https://analyzing-testing.netzsch.com/ko/beulrogeu/2023/nanotr-yalbeun-ceungyi-yeol-teugseonghwareul-wihan-seupaen-seupaen-seupaen-gyeceuggi-rain-picotr-nbsp-span-span-instrument-line-for-the-thermal-characterization-of-thin-layers

[^6_3]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11044587/

[^6_4]: https://kummelgroup.ucsd.edu/pubs/papers_2023/Perex%20Mcleod%20AlN%20Thermal%20Conductivity%20ACS%20Nano%202023.pdf

[^6_5]: https://pubs.aip.org/aip/jap/article-pdf/doi/10.1063/5.0245381/20429173/095105_1_5.0245381.pdf

[^6_6]: https://koreascience.kr/article/JAKO202521832402107.pdf

[^6_7]: https://scienceon.kisti.re.kr/srch/selectPORSrchArticle.do?cn=NART126387656

[^6_8]: https://scienceon.kisti.re.kr/aiq/issue/selectIssueReportView.do?searchIssueRptNo=958\&searchDataSectionId=tab_analysis_information

[^6_9]: https://oxfamilibrary.openrepository.com/bitstream/handle/10546/621419/rr-cri-2022-111022-summ-ko.pdf?sequence=32\&isAllowed=y

[^6_10]: https://patrickehopkins.com/wp-content/uploads/2016/08/2016-sthc_tdtrnometal.pdf

[^6_11]: https://patrickehopkins.com/wp-content/uploads/2021/08/hoque2021aa.pdf

[^6_12]: https://dr.ntu.edu.sg/handle/10356/166521

[^6_13]: https://www.tandfonline.com/doi/pdf/10.1080/15567265.2016.1154630

[^6_14]: https://analyzing-testing.netzsch.com/ko/jepum/time-domain-thermoreflectance-analyzer-tdtr/nanotr

[^6_15]: https://poplab.stanford.edu/pdfs/Vaziri-AlNthermalMaterial3DICs-afm25.pdf

