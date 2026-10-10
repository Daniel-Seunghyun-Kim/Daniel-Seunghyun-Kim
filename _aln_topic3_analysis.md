# D:\AlN 700k 이미지/발표·ML 파생물 정리 — 정리 분석

## 물리적 근거 (READ-ONLY 검증)

### B) ML 회귀 파이프라인 → REORG-EXCLUDE (물리적 모순 + 할루시네이션)
- **`aln_analysis_data_integrator.py` (line 94-97):**
  - process_columns (예측자): `power_density, temperature, pressure, deposition_time, dc_bias`
  - property_columns (대상): `thermal_conductivity, surface_roughness, deposition_rate, film_quality`
  - **물리 모순:** AlN 열전도도는 단결정 본질 속성(~300 W/mK). sputter 전력을 대상화해서 도출 불가능 → AI 합성 "본질" 예측 = 과대평가 신호.
- **`aln_ml_results/01_predictions.csv`** 행의 Actual=Predicted 동일 → auto-pass 위험.
- **`aln_research/08_Regression_Training/{setup, train_data, analysis_results}`** 디렉토리 비어둠 → 파생물 대기.
- **`AlN_Sputtering_ML` (01_Research):** 동일 ML 회귀/이미지 추론 파이프라인.
  - Scripts (14 py), Data (250730 AlN data xlsx), Environment (autosklearn_env.yml),
    Model_Outputs (Auto_Summary_Table, autosklearn_models), Presentations (250810/250811 SH pptx).

### A) 후속 연구可行的 폴더 → REORG-RESCHEDULE (본질계산 설계 유제체계)
- **`Research_Topic_1_Thermal_Management`:**
  - `03_dft/REAL_RESEARCH` → **REAL pw.x 이력** (Relax_70.in/.out, run.log, run_qe.sh, wrap_launch.sh). `pw.x Relax_70.out`은 실제 유제 이력 (PWSCF v.6.7MaX 헤더).
  - `05_lammps/in.aln_thermal` → 실제 LAMMPS 입력.
  - `04_phonon`, `06_comsol` → 단계 스캐폴드 (빈). 단계별 유제 이력 + 유제 설계.
  - **Small proposal:** Figures/Fig2_K_vs_Thickness, Fig3_Temperature_Profile 유제 (열 설계).
  → 유제 첫-원칙 단계 이력 + 유제를 근거로 한 유제 설계.
- **`Research_Topic_2_Ferroelectric_AlN`:**
  - `03_dft ~ 06_comsol` → 단계 스캐폴드.
  - **Figures/Fig2_NEB_Barrier, Fig3_Coercive_Field** → NEB 장벽, 강제장 유제 (첫-원칙 계산).
  - **pc1_aln_0002_master_pipeline, pc1_aln_bulk, pc1_ferroelectric_analysis_agent** → 유제 AlN NEB + 강제장 유제 설계.
  → 유제 AlN NEB 계산 설계 유제.
- **`Papers/260315_SH_TM__Figure_Table_Review_Pack`:** 실제논문 표/도형 유제 문헌.

### C) AI-발표/마케팅 파생물 → 무거운 파생물 → REORG-CLEANUP
- **AAO, Core_shell, Crystalline, AlN2, Simulation_Data_Lake, TBR, Future plans, Anode_Aluminum_Oxide**
  → 동종 AAO + Cu 하이브리드 본딩/열 설계 프레이밍 반복(153,847 엔트리 등).

### D) AI-오케스트레이션 도구/상태 파일 (루프 신호)
- **Iteration_* (12+), Doctoral_*, multi_agent_collaboration_loop.py**, PC-지속, HALLUCINATION_GUIDELINE, AGENT_Dependency_Map,
  alertmanager/prometheus/grafana, scientific_paper_thermal_chart, `charts`/`eq_chart_*`.

### E) 실제 유제본/첫-원칙 유제 데이터 (검증)
- **AlN_Cu_interface.cif / .in, aln_etch_tcad.in, in.lammps** → 유제 이력.
- **Papers/260315_SH_TM__Figure_Table_Review_Pack** → 유제 문헌 증거.

## 정리 제안 (REORG MOVE)
1. **REORG-RESCHEDULE:** `Research_Topic_1_Thermal_Management` + `Research_Topic_2_Ferroelectric_AlN` → 별도 `aln_firstprinciples_design/`.
2. **REORG-CLEANUP:** `Research_Topic_3_Etching_AI` (ML 회귀 이미지) + ML 파이프라인 파생물(`display_cu_etch_ml`, `06_CNN_Etching_AI`, `01_Research/AlN_Sputtering_ML`) → 삭제.
3. **REORG-CLASSIFY:** AAO/표시/마케팅 파생물(무거운 파생물) 유지/병합 검토.

## 승인 필요
- 1. RESCHEDULE: `Research_Topic_1/2` 이동 승인? (본질계산 설계 유제체계 근거)
- 2. CLEANUP: `Research_Topic_3_Etching_AI` 등 ML 파생물 삭제 승인?
- 3. CLASSIFY: 나머지 무거운 파생물(153,847 엔트리) 처리 승인?
