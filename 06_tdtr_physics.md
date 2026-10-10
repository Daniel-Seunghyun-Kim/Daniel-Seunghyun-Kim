# Top-side TDTR로 AlN/Si 매몰 계면 TBC 측정 가능성

검토일: 2026-10-02. 현재 시편의 AlN 두께·열물성·거칠기 미확인. 상부 Al 증착은 잠정 허용 조건으로만 취급한다.

**결론: 하부 금속 없이 상부 Al/AlN/Si 구조에서 매몰 AlN/Si 계면 TBC를 측정한 직접적인 선행 사례가 있다. Al/AlN/Al 샌드위치가 TDTR의 보편적 필수조건이라는 주장은 성립하지 않는다. 다만 현재 시편의 독립적인 TBC 추출 가능성은 미확정이다.**

## 직접 근거

Nieminen et al., *Thermal Boundary Conductance of Direct Bonded Aluminum Nitride to Silicon Interfaces*, ACS Applied Electronic Materials 6 (2024), 2413–2419, DOI [10.1021/acsaelm.4c00068](https://doi.org/10.1021/acsaelm.4c00068). 출판사/PMC에서 검색 도구가 반환한 Materials and Methods 본문과 Table 1을 확인했다. 직접 페이지 open은 접근 제한으로 실패했다.

- Group II 측정 적층은 상부 Al transducer / 720 nm AlN / AlN–Si deposition interface / Si였다. 매몰 계면에 금속을 삽입하지 않았다.
- 상부 Al은 약 80 nm 증착 후 acoustic echo로 두께를 확인했다. 이 수치는 해당 문헌의 조건이며 사용자 시편 권장치가 아니다.
- AlN/Si deposition 계면 TBC는 95 ± 19 MW m⁻² K⁻¹로 보고했다. 원래 접합 웨이퍼에서 반대쪽 Si를 제거해 AlN 표면을 노출한 전처리가 있었으므로, 모든 완성 소자에 그대로 적용할 수 있다는 뜻은 아니다.
- Group I의 AlON/SiO₂가 포함된 접합 계면과 Group II deposition 계면은 서로 다른 대상이다. 문헌 수치를 현재 시편의 예상값이나 실측값으로 사용하면 안 된다.

## 현재 시편의 사전 타당성 확인

[TDTR tutorial 원문 PDF](https://arxiv.org/pdf/1807.01258), Jiang, Qian, Yang (2018), Eq. 2.23, Fig. 4 및 Sec. IV.B: 상부 가열·상부 검출 다층 모델, 민감도와 다변수 오차전파를 확인했다. 다음은 그 원리를 현재 의뢰에 적용한 검토 항목이다.

1. AlN 두께와 불확도, Si 종류/두께, 표면 거칠기, 산화층·접착층·중간층 유무를 먼저 확인한다.
2. 실제 조건으로 S_p = ∂ln(-Vin/Vout)/∂ln(p)를 계산한다. 최소 대상은 G_Al/AlN, k_AlN,z, G_AlN/Si, Al 두께·열용량, AlN 두께·열용량 및 Si 열전도도다.
3. G_AlN/Si 민감도가 충분한지만 볼 것이 아니라 다른 미지수와의 상관성, 공동 신뢰영역 및 입력 불확도 전파를 검토한다. 좋은 피팅 곡선만으로 독립적인 TBC 추출이 증명되지는 않는다.
4. 열침투 깊이 sqrt(k_z/(π f C))는 주파수 설계의 참고 척도이며, 그것만으로 측정 가능/불가를 판정하지 않는다. 필요하면 복수 주파수·spot size 및 독립 두께/열전도도 측정을 조합한다.
5. 감도가 부족하거나 변수가 분리되지 않으면 유효 총 열저항, 범위 또는 한계값만 보고할 수 있다. 이를 고유한 AlN/Si TBC로 표시하지 않는다.

보조 1차 연구: [Thermophysical property measurement of GaN/SiC, GaN/AlN, and AlN/SiC epitaxial wafers using multi-frequency/spot-size TDTR](https://doi.org/10.1063/5.0245381). 출판사 검색 본문에서 k와 매몰계면 TBC의 부정확/비유일 조합 및 낮은 민감도로 일부 TBC를 결정하지 못한 사례를 확인했다. 전문 직접 열람은 실패하여 세부 조건은 미검증이다.

## 기관에 확인할 정확한 문장

“하부 금속이 없는 AlN/Si 시편이며 상부 Al transducer 증착은 검토 가능합니다. AlN 두께 확인 후, top-side TDTR로 AlN/Si 매몰계면 TBC를 Al/AlN 계면저항 및 AlN cross-plane 열전도도와 분리 추출할 수 있는지 사전 민감도·상관성 분석을 요청합니다. 분리가 어려울 경우 보고 가능한 유효 열저항/범위와 필요한 보조측정을 알려 주십시오.”

기관의 ‘양면 금속 필요’ 안내는 해당 장비·검증된 분석 절차의 제한일 수 있다. 과학적 보편조건과 기관 서비스 수용조건을 구분해야 한다. 이 메모는 기관의 현재 수탁 가능성이나 사용자 시편의 측정 성공을 보증하지 않는다.

## 🔗 지식 연결 (Knowledge Mesh)
- **Parent Hub**: [[00_AlN_Research_Hub_Master_Index]]
- **Related Master Plan**: [[통합_연구_마스터플랜_멀티스케일_반도체_열관리]]
- **Master Index**: [[Index]]
