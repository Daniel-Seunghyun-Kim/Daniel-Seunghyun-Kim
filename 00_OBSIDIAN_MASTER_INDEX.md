---
title: PC2 Research Knowledge Vault Master Index
created: 2026-10-08
tags:
  - obsidian
  - pc2
  - aln-research
  - dft-quantum-espresso
  - bte-thermal-conductivity
  - hybrid-bonding
  - literature-audit
aliases:
  - Master MOC
  - Research Knowledge Base
---

# 🏛️ PC2 Research Knowledge Vault: Master Map of Content (MOC)

> [!NOTE]
> **Vault Architecture Notice**
> 이 폴더(`Obsidian_Markdown_Vault`)는 옵시디언(Obsidian) 지식 그래프 및 의사결정 파이프라인 전용으로 구성된 **순수 마크다운 전용 보관소**입니다.
> 폴더 내의 모든 파일은 **`.md` 확장자만을 유일하게 유지**하며, 작업공간의 파이썬 스크립트, 실행 데몬, 구조/데이터 파일, 발표 자료 및 시뮬레이션 폴더 전체에 대한 메타데이터 카탈로그와 긴밀히 상호 연결(Wikilink `[[...]]`)되어 있습니다.

---

## 🧭 1. 전체 자산 메타 카탈로그 (Workplace Assets Catalogs)
작업공간 루트에 존재하는 모든 비-마크다운 파일의 상세 명세, 입출력 구조, 실행 명령어가 마크다운 문서로 체계화되어 있습니다:

- 🐍 **[[CATALOG_01_PYTHON_SCRIPTS]]**: 전체 23개 파이썬 계산·자동화·시각화 스크립트 분석 및 함수 명세
- ⚙️ **[[CATALOG_02_SHELL_POWERSHELL_SCRIPTS]]**: Dual RTX 4090 무중단 감시 데몬, 워치독, 실행 래퍼 스크립트 명세
- 📊 **[[CATALOG_03_DATA_CONFIG_LOGS]]**: JSON, CSV 수렴 이력, QE 입력 덱, 구조 CIF/VASP, 무결성 해시 명세
- 🖼️ **[[CATALOG_04_FIGURES_AND_SLIDES]]**: 논문급 고해상도 수렴 그래프, 열 해석 시각화, 발표 슬라이드 및 압축 아카이브 명세
- 📁 **[[CATALOG_05_SUBDIRECTORIES_AND_CAMPAIGNS]]**: Gate A 수렴, 3-Team 다중스케일 프로젝트, 가상환경 등 하위 폴더 명세

---

## 🔬 2. 핵심 연구 주제별 마크다운 문서 분류 (Thematic MOC)

### A. DFT 계산 및 하드웨어 실행 거버넌스 (DFT & PC2 Governance)
- [[00_MASTER_SUMMARY]]: PC2 워크스테이션 전체 연구 요약 및 현황
- [[AGENTS]]: 연구 작업 공통 기준 및 8대 실행 원칙
- [[AGENTS_PC2_EXECUTION_RULES]]: Dual RTX 4090 올인원 단독 실행 및 물리 법칙 엄격성 규칙
- [[PC2_RESEARCH_NODE_ARCHITECTURE]]: PC2 노드 컴퓨팅 및 렌더링 파이프라인 아키텍처
- [[PC2_DISCOVERY_REPORT]]: PC2 하드웨어 사양(128 GB RAM, Dual 4090) 및 자원 검증 보고서
- [[GPU_PARALLEL_BENCHMARK_PLAN]]: Dual GPU 병렬화 및 k-point/band 분할 벤치마크 계획
- [[QE_BENCHMARK_PLAN]]: Quantum ESPRESSO GPU 가속 벤치마크 플랜
- [[WORKFLOW_MANAGER_DECISION]]: 단독 노드 관리자 결정 및 자동 복구 구조

### B. AlN 격자 열전도도 및 3차원 힘상수 (Phonon BTE & FC3)
- [[SIM_A2_FC3_EXECUTION_GUIDE]]: **3.20 Å fc3 기반 AlN 300 K RTA / LBTE 격자 열전도도 실행 지침**
- [[FORCE_CONSTANT_CONVERGENCE_STATUS]]: 초격자 변위 힘상수 수렴도 및 ASR 보존 상태
- [[SIM_VERIFICATION_RESULTS_20260930]]: Gate A 및 FC3 검증 결과 종합 보고서
- [[SIM_FULL_PIPELINE_DIRECTIVE_20261001]]: FC3 조립 및 N-흡착 4개 마이크로스테이트 실행 지침
- [[SIM_GPU_RESTART_20261001]]: 125원자 Al(111) 모체 슬랩 체크포인트 복구 및 BFGS 실행 지침
- [[FINALIZATION_GATES]]: 시뮬레이션 완결 게이트 기준 및 검증 체크리스트
- [[GATE_A_VERIFIED_STEP_HISTORY]]: Gate A 396회 연속 완화 단계 검증 이력

### C. 나노스케일 열전도 & 하이브리드 본딩 (Multiscale Thermal Transport)
- [[GMSH_ELMER_AND_HYBRID_BONDING_THERMAL_REPORT]]: Gmsh-Elmer FEM 유한요소 및 과도 열 플래시 해석 보고서
- [[SEAMLESS_SIMULATION_CHAIN_PLAN]]: BTE 미시 열전도도와 거시 FEM 열해석 무결점 연계 계획
- [[Supplementary_Experiments_TDTR_3omega_Laser]]: TDTR 및 3-Omega 레이저 열 측정 실험 보완 계획
- [[Thermal_Fluid_BlueRedOcean_Detailed]]: 열유체 다중스케일 블루오션 전략 상세 분석

### D. 연구 로드맵, 전략 및 연구실 세미나 (Strategy & Presentations)
- [[Final_Master_Plan_2027-2028]]: 2027-2028 마스터 연구 계획서
- [[Simulation_Roadmap_Thermal_Fluid_2027-2028]]: 열유체 시뮬레이션 연구 로드맵
- [[Research_Mandala_BlueRedOcean_Analysis]]: 연구 만다라트 및 가치 사슬 분석
- [[lab_meeting_20260918_presentation_guide]]: 2026-09-18 랩미팅 발표 가이드
- [[Inha_ZEUS_Equipment_Audit_2026-09-25]]: 인하대 ZEUS 공동활용 장비 감사 및 TDTR/XRD 연계 방안
- [[L1_DSD_실제_조건_및_수정_제안]]: L1 DSD 실제 실험 조건 및 수정 제안
- [[L1_DSD_최종설계_N2최적화]]: L1 DSD 질소 분압 및 증착 최적화 설계

### E. 시스템 상태 및 AI 도구 인프라 (AI Stack & Security)
- [[DATA_PROTECTION_REPORT]]: 연구 데이터 보호 및 백업 보고서
- [[JEV_SETUP_STATUS]]: TypeSafe AI Jev System One 연동 상태 진단서
- [[AI_Performance_Ranking_and_Paper_Validation]]: AI 모델 성능 랭킹 및 논문 검증 분석
- [[AI_Ranking_Summary_Guide]]: AI 랭킹 요약 가이드
- [[02_Free_APIs_and_OpenSource_Tools]]: 무료 API 및 오픈소스 도구 목록
- [[03_Setup_and_Initialize]]: 환경 설정 및 초기화 가이드
- [[04_Investment_and_Revenue_Strategy]]: 연구 과제 및 투자 전략
- [[05_Multi-Institution_and_Startup_Path]]: 다기관 협력 및 스타트업 경로
- [[ASIDE_HANDOFF_PROMPT]]: 이전 세션 핸드오프 프롬프트
- [[ASIDE_RESUME_PACKET]]: 세션 복구 및 상태 패킷
- [[ACTIONS_REQUIRING_APPROVAL]]: 승인 필요 작업 목록
- [[Integrating Claude and ChatGPT Codex]]: 클로드 및 챗GPT 연계 코덱스

---

## 📋 3. 보관소 내 전체 마크다운 파일 목록 (52 Files)

- [[00_MASTER_SUMMARY]]
- [[02_Free_APIs_and_OpenSource_Tools]]
- [[03_Setup_and_Initialize]]
- [[04_Investment_and_Revenue_Strategy]]
- [[05_Multi-Institution_and_Startup_Path]]
- [[ACTIONS_REQUIRING_APPROVAL]]
- [[AGENTS]]
- [[AGENTS_PC2_EXECUTION_RULES]]
- [[AI_Performance_Ranking_and_Paper_Validation]]
- [[AI_Ranking_Summary_Guide]]
- [[ASIDE_HANDOFF_PROMPT]]
- [[ASIDE_RESUME_PACKET]]
- [[CATALOG_01_PYTHON_SCRIPTS]]
- [[CATALOG_02_SHELL_POWERSHELL_SCRIPTS]]
- [[CATALOG_03_DATA_CONFIG_LOGS]]
- [[CATALOG_04_FIGURES_AND_SLIDES]]
- [[CATALOG_05_SUBDIRECTORIES_AND_CAMPAIGNS]]
- [[DATA_PROTECTION_REPORT]]
- [[FINALIZATION_GATES]]
- [[FORCE_CONSTANT_CONVERGENCE_STATUS]]
- [[Final_Master_Plan_2027-2028]]
- [[GATE_A_VERIFIED_STEP_HISTORY]]
- [[GMSH_ELMER_AND_HYBRID_BONDING_THERMAL_REPORT]]
- [[GPU_PARALLEL_BENCHMARK_PLAN]]
- [[Inha_ZEUS_Equipment_Audit_2026-09-25]]
- [[Integrating Claude and ChatGPT Codex]]
- [[JEV_SETUP_STATUS]]
- [[L1_DSD_실제_조건_및_수정_제안]]
- [[L1_DSD_최종설계_N2최적화]]
- [[PC2_DISCOVERY_REPORT]]
- [[PC2_RESEARCH_NODE_ARCHITECTURE]]
- [[PLAN_A3_00_A3_MASTER_EXECUTION_OVERVIEW]]
- [[PLAN_A3_01_HARDWARE_CAPACITY_AND_ALLOCATION_MATRIX]]
- [[PLAN_A3_02_DFT_DECK_CONFIGURATION_GUIDE]]
- [[PLAN_A3_03_AUTONOMOUS_SUPERVISOR_RECOVERY_PROTOCOL]]
- [[PLAN_A3_04_ADSORPTION_THERMODYNAMICS_CALCULATION_GUIDE]]
- [[PLAN_A3_05_STEP_A3_RUNNER_SCRIPTS_SPECIFICATION]]
- [[QE_BENCHMARK_PLAN]]
- [[Research_Mandala_BlueRedOcean_Analysis]]
- [[SEAMLESS_SIMULATION_CHAIN_PLAN]]
- [[SIM_125ATOM_PARENT_SLAB_CONVERGENCE]]
- [[SIM_A2_FC3_EXECUTION_GUIDE]]
- [[SIM_FULL_PIPELINE_DIRECTIVE_20261001]]
- [[SIM_GPU_RESTART_20261001]]
- [[SIM_PC2_NEXT_EXECUTION_DIRECTIVE]]
- [[SIM_REPAIR_FINDINGS]]
- [[SIM_VERIFICATION_RESULTS_20260930]]
- [[Simulation_Roadmap_Thermal_Fluid_2027-2028]]
- [[Supplementary_Experiments_TDTR_3omega_Laser]]
- [[Thermal_Fluid_BlueRedOcean_Detailed]]
- [[WORKFLOW_MANAGER_DECISION]]
- [[lab_meeting_20260918_presentation_guide]]

---
*Generated by DeepMind Antigravity IDE on PC2 Workstation (c:\Users\AOL\Desktop\SH.Kim)*

## 🔗 지식 연결 (Knowledge Mesh)
- **Parent Hub**: [[00_AlN_Research_Hub_Master_Index]]
- **Related Master Plan**: [[통합_연구_마스터플랜_멀티스케일_반도체_열관리]]
- **Master Index**: [[Index]]
