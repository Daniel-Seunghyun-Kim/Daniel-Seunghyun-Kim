# Step A3: 질소 흡착 열역학 및 결합 에너지 산출 가이드 (Adsorption Thermodynamics Guide)

**연구 주제**: Al(111) 표면 상 질소 흡착 사이트별 열역학적 안정성 및 계면 활성화 에너지  
**작성일**: 2026-10-10 (Asia/Seoul)

---

## 1. 질소 흡착 에너지 ($E_{\text{ads}}$) 정의식

흡착 반응식:
$$\text{Al}_{125}(\text{slab}) + \frac{1}{2} \text{N}_2(\text{gas}) \longrightarrow \text{N}/\text{Al}_{125}(\text{adsorbed})$$

단일 질소 원자 기준 흡착 에너지 계산 공식:
$$E_{\text{ads}} = E_{\text{total}}(\text{N}/\text{Al}_{125}) - \left[ E_{\text{slab}}(\text{Al}_{125}) + \frac{1}{2} E_{\text{ref}}(\text{N}_2) \right]$$

### 기준 기준값 (Reference Baseline):
- **$E_{\text{slab}}(\text{Al}_{125})$ (모체 슬랩 에너지)**: **`-4936.51366715 Ry`** (Step 18 완결 수렴치)
- **$E_{\text{ref}}(\text{N}_2)$ (기체 질소 분자 에너지)**:
  - 분자 질소 삼중 결합 완화 계산값 (PBE-PAW 기준 $1\ \text{N}_2$ 분자 = $-39.8542\ \text{Ry}$ 수준, 동일 pseudo-potential 및 ecutwfc=55 Ry 사용)
  - $\frac{1}{2} E_{\text{ref}}(\text{N}_2) \approx -19.9271\ \text{Ry}$

---

## 2. 부호 및 안정성 판정 기준
- **$E_{\text{ads}} < 0$**: 발열 반응 (Exothermic) $\longrightarrow$ **열역학적으로 안정한 흡착 상태**
- **$E_{\text{ads}} > 0$**: 흡열 반응 (Endothermic) $\longrightarrow$ 열역학적으로 불안정한 상태
- **절댓값 $|E_{\text{ads}}|$가 가장 큰 사이트**가 초기 질화 과정에서 질소 원자가 우선적으로 점유하는 **바닥 상태(Ground State) 흡착 사이트**임.

---

## 3. 문헌 이론 예측치 및 사이트별 예상 순위

Al(111) 면심입방 격자의 (111) 표면에서 문헌(DFT-GGA)에 보고된 전형적인 흡착 경향:

| 마이크로스테이트 | 결합 양식 | 배위수 (Coordination) | 예상 흡착 에너지 ($E_{\text{ads}}$) | 열역학적 안정성 |
| :---: | :---: | :---: | :---: | :---: |
| **`fcc hollow`** | 3중 배위 (3-fold) | 3 | **$-4.2 \sim -4.8\ \text{eV}$** (가장 안정) | **최우선 바닥 상태** |
| **`hcp hollow`** | 3중 배위 (3-fold) | 3 | $-4.0 \sim -4.6\ \text{eV}$ | 준안정 상태 ($\sim 0.2\ \text{eV}$ 차이) |
| **`bridge`** | 2중 배위 (2-fold) | 2 | $-3.2 \sim -3.8\ \text{eV}$ | 확산 경로 전이 상태 |
| **`ontop`** | 1중 배위 (1-fold) | 1 | $-2.0 \sim -2.8\ \text{eV}$ (가장 불안정) | 고에너지 흡착 상태 |

---

## 4. 후속 Step B (계면 전하 이동 및 BTE 결합) 연계
1. 바닥 상태(`fcc hollow`)로 확인된 사이트를 기준으로 AlN 초기 박막 형성의 핵생성 에너지 장벽 도출.
2. Bader 전하 분석(Bader Charge Analysis)을 수행하여 Al $\to$ N 전하 이동량($\Delta \rho$) 산출.
3. Al/AlN 계면 격자 부정합에 의한 계면 열저항($R_{\text{interface}}$) 모델링 입력값으로 직접 연결.
