# 3D 반도체 패키징 및 AlN 열 관리 기술 참고문헌 및 핵심 요약

## 1. 개요 (Overview)
본 문서는 `Review_Manuscript_final_main part_additionally_revised.docx` 및 `Supporting_information_final_additionally_revised.docx` 두 소스 파일에서 인용된 참고문헌(References) 목록 및 핵심 연구 주제를 정리한 마크다운(.md) 문서입니다.

---

## 2. 참고문헌 핵심 주제 요약 (Key Themes)

### 1) 3D 반도체 패키징 및 하이브리드 본딩 기술의 진화와 한계
- **주요 내용:** AI 및 HPC 발전으로 인한 고대역폭 메모리(HBM) 다층 적층 및 sub-2 µm Cu-Cu 하이브리드 본딩 기술 동향.
- **핵심 이슈:** 적층 구조에 따른 칩 내부 '열 벽(Thermal Wall)' 형성 및 기존 외부 냉각 방식의 한계.

### 2) 나노스케일 미세 구조에서의 열 전달 물리 (푸리에 법칙의 붕괴)
- **주요 내용:** 10 µm 이하 미세 층에서의 볼츠만 수송 방정식(BTE) 및 포논 열전달 특성.
- **핵심 이슈:** 포논 평균 자유 경로(MFP), 경계 산란(Boundary Scattering)에 의한 유효 열전도도($k_{eff}$) 저하 및 열 경계 저항(TBR/Kapitza 저항).

### 3) 열교(Thermal Bridge)로서의 질화알루미늄(AlN) 및 유전체 소재 특성
- **주요 내용:** $SiO_2$ 대안으로서의 AlN, SiC, 다이아몬드 등 차세대 유전체 재료 평가.
- **핵심 이슈:** AlN의 수직 방향 열전도도 유지 특성, Cu와의 포논 진동 상태 밀도(vDOS) 일치성, 전기 절연성 및 열팽창계수(CTE) 정합성.

### 4) 나노 박막의 열 측정 기술(Metrology) 및 공정 결함 제어
- **주요 내용:** 매몰 박막 열전도도 측정을 위한 고주파 FDTR(주파수 영역 열반사율 측정) 및 TDTR 기술.
- **핵심 이슈:** Cu 산화물($CuO_x$), CMP 공정 손상층, Cu 펌핑(돌출) 등 공정 유발 결함 억제 방법론.

### 5) 다중 스케일 시뮬레이션 및 AI 기반 열 설계 자동화 (TDA)
- **주요 내용:** DFT(밀도범함수이론) 및 NEMD(비평형 분자동역학) 기반 원자 단위 해석과 AI/ML 융합.
- **핵심 이슈:** 가우시안 프로세스 회귀 및 베이지안 최적화를 활용한 공정 변수 예측 및 열 설계 자동화.

---

## 3. 핵심 추출 참고문헌 목록 (Extracted Core References)

### Category 1: 3D Packaging & Hybrid Bonding
1. **H. Y. Hsiao, C. M. Liu, H. W. Lin, et al.**, "Cu-Cu hybrid bonding mechanism," *Science*, **2012**, 336, 1007.
2. **S.-H. Lee, S.-J. Kim, J.-S. Lee, S.-H. Rhi**, "Effective thermal conductivity along the stacking direction for chip-to-wafer Cu hybrid bonding," *Electronics*, **2025**, 14, 2682.
3. **J. H. Lau**, "3D Integration & Hybrid Bonding," *IEEE Trans. Compon. Packag. Manuf. Technol.*, **2024**, 14, 376.
4. **S. H. Zandavi, A. Schmidt, X. Brun**, "Joint resistance in hybrid Cu bonding," *J. Appl. Phys.*, **2024**, 136, 155303.
5. **H. Park, H. Seo, S. E. Kim**, "Low temperature Cu-Cu bonding," *Sci. Rep.*, **2020**, 10, 21720.

### Category 2: Nanoscale Heat Transport Physics & BTE
6. **D. G. Cahill, W. K. Ford, K. E. Goodson, et al.**, "Nanoscale thermal transport review," *J. Appl. Phys.*, **2003**, 93, 793.
7. **R. B. Wilson, D. G. Cahill**, "Anisotropic heat transport," *Nat. Commun.*, **2014**, 5, 5075.
8. **A. J. Minnich, J. A. Johnson, A. J. Schmidt, et al.**, "Thermal conductivity spectroscopy," *Phys. Rev. Lett.*, **2011**, 107, 095901.
9. **Y. C. Hua, B. Y. Cao**, "Phonon boundary scattering in thin films," *Int. J. Therm. Sci.*, **2016**, 101, 126.
10. **E. T. Swartz, R. O. Pohl**, "Thermal boundary resistance," *Rev. Mod. Phys.*, **1989**, 61, 605.

### Category 3: AlN Dielectric & Low-Temp Deposition
11. **G. A. Slack, R. A. Tanzilli, R. O. Pohl, J. W. Vandersande**, "The intrinsic thermal conductivity of AlN," *J. Phys. Chem. Solids*, **1987**, 48, 641.
12. **M. E. Chen, S. Yi, S. Vaziri, et al.**, "Ultrathin sputtered AlN thermal properties," *ACS Nano*, **2023**, 17, 21240.
13. **S. Vaziri, C. Perez, I. M. Datye, et al.**, "Thermal anisotropy in reactively sputtered AlN," *Adv. Funct. Mater.*, **2025**, 35, 2402662.
14. **R. L. Xu, M. Muñoz Rojo, S. M. Islam, et al.**, "Anisotropic thermal conductivity of AlN," *J. Appl. Phys.*, **2019**, 126, 185105.
15. **C. Perez, A. J. McLeod, M. E. Chen, et al.**, "Low-temperature deposition of c-axis AlN," *ACS Nano*, **2023**, 17, 21240.

### Category 4: High-Frequency Thermal Metrology (FDTR/TDTR)
16. **D. G. Cahill**, "Analysis of thermal conductivity of thin films by 3-omega method," *Rev. Sci. Instrum.*, **2004**, 75, 5119.
17. **Y. K. Koh, D. G. Cahill**, "Frequency-dependent thermal conductivity," *Phys. Rev. B*, **2007**, 76, 075207.
18. **D. J. Kirsch, J. Martin, R. Warzoha, et al.**, "Frequency domain thermoreflectance sensitivity," *Rev. Sci. Instrum.*, **2024**, 95, 103006.
19. **R. J. Warzoha, A. A. Wilson, B. F. Donovan, et al.**, "Buried film thermal characterization," *ACS Appl. Mater. Interfaces*, **2024**, 16, 41633.

### Category 5: Multi-scale Modeling (DFT, MD) & AI-guided TDA
20. **B. Cao**, "Machine learning thermal design," *J. Appl. Phys.*, **2025**, 138, 180901.
21. **P. Giannozzi, S. Baroni, N. Bonini, et al.**, "Quantum ESPRESSO for DFT calculations," *J. Phys. Condens. Matter*, **2009**, 21, 395502.
22. **A. P. Thompson, H. M. Aktulga, R. Berger, et al.**, "LAMMPS - a flexible simulation tool for particle-based materials modeling," *Comput. Phys. Commun.*, **2022**, 271, 108171.
23. **A. Seko, A. Togo, H. Hayashi, et al.**, "Gaussian process regression for materials science," *Phys. Rev. Lett.*, **2015**, 115, 205901.
