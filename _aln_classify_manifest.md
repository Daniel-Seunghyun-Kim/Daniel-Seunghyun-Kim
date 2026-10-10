=== AlN 멀티스케일 정리 분석 (2026-08-30) ===

# 근거 (physically grounded)
D:\AlN ≈ 700,000개 엔트리. 대부분 = 2026-05 AAO 학술-발표 캠페인 + 자기-강화 과대평가 루프(동일 프레이밍 반복)로 인한 파생물.
가장 큰 단일 항목: "Research_Topic_3_Etching_AI" ≈ 153,847 엔트리(CNN/회귀 추론 + images).

A) ML 회귀 파이프라인 — 물리 모순으로 REORG-EXCLUDE (지시 준거)
- aln_analysis_data_integrator.py (line 94-97):
    process_columns = power_density, temperature, pressure, deposition_time, dc_bias
    property_columns = thermal_conductivity, surface_roughness, deposition_rate, film_quality
  → 물리적 모순: AlN 열전도도는 단결정 본질 속성(~300 W/mK). sputter 전력을 대상화해서는 도출할 수 없음.
    thermal_conductivity를 "본질"이 아니라 전극자-편향이 예측하는 값으로 취급 = AI 과대평가 신호.
- Target/Prop: thermal_conductivity / surface_roughness / deposition_rate / film_quality는 "score"-형 합성 목표.
- aln_ml_results/01_predictions.csv 행의 Actual=Predicted 동일 → 검증-단언 자동 통과(auto-pass 위험).
- aln_research/08_Regression_Training/{setup,train_data,analysis_results} 디렉토리 비어둠/빈 -> 파생물 생성 대기.
- AlN_Sputtering_ML (01_Research) = 동일 ML 회귀/이미지 추론 파이프라인:
    Scripts(14 py), Data(250730 AlN data xlsx), Environment(autosklearn_env.yml),
    Model_Outputs(Auto_Summary_Table, autosklearn_models), Presentations(250810/250811 SH pptx).

B) 후속 연구 가능한 폴더 (REORG-RESCHEDULE)
1) Research_Topic_1_Thermal_Management
    • 03_dft/REAL_RESEARCH: REAL_RESEARCH/Relax_70/80.{in,out}, run.log, run_qe.sh, wrap_launch.sh (pw.x 실제 이력)
    • 05_lammps/in.aln_thermal: LAMMPS 실제 입력파
    • 04_phonon, 06_comsol: 단계 스캐폴드 (빈). 제안: 이 단계만 REORG-EVALUATE.
    • 소제출: Figures/Fig2_K_vs_Thickness, Fig3_Temperature_Profile (열 설계)
    → 유제본 첫 원칙 단계 이력 + 유제를 근거로 한 유제 설계.
2) Research_Topic_2_Ferroelectric_AlN
    • 03_dft ~ 06_comsol: 단계 스캐폴드.
    • Figures/Fig2_NEB_Barrier, Fig3_Coercive_Field (NEB 장벽, 강제장).
    • pc1_aln_0002_master_pipeline, pc1_aln_bulk, pc1_ferroelectric_analysis_agent.
    → 유제 AlN NEB + 강제장 유제 설계 (본질 계산, 첫 원칙).
3) Papers (4797 엔트리): 260315_SH_TM__Figure_Table_Review_Pack (실제 논문 표/도형) → 유제 문헌 수집 증거.

C) AI-발표/마케팅 파생물 — 무거운 파생물 → REORG-CLEANUP
- AAO, Core_shell, Crystalline, AlN2, Simulation_Data_Lake, TBR, Future plans, Anode_Aluminum_Oxide 등
  = 동일 AAO+Cu 하이브리드 본딩/열 설계 프레이밍 반복.

D) AI-오케스트레이션 도구/상태 파일 (루프 신호)
- Iteration_* (12+), Doctoral_*, multi_agent_collaboration_loop.py, PC_지속, HALLUCINATION_GUIDELINE,
  AGENT_Dependency_Map, alertmanager/prometheus/grafana, scientific_paper_thermal_chart 등.

E) 실제 유제본/첫 원칙 유제 데이터 (검증)
- AlN_Cu_interface.cif / .in, aln_etch_tcad.in, in.lammps → 유제 이력.
- Papers/260315_SH_TM__Figure_Table_Review_Pack → 유제 문헌.
