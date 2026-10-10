# Aside 재개용 통합 자료

이 파일에는 핵심 문서 4개와 인계 README, 추가 연구 후보 문서의 전문이 들어 있다. 폴더 접근이 차단되면 이 첨부파일의 본문을 읽으면 된다. 원본 파일별 구분은 SOURCE 표제를 참조한다. 동결 기준의 원본은 PREREG.md v0.10이다.

## 이번 재개 요청

기존 연구를 처음부터 다시 시작하지 말고, 아래 자료를 읽어 맥락을 복원해줘. 핵심 파일은 누락된 것이 아니라 algorithm_v0.10_claude_final/AlN_HybridBonding_Algorithm_v0.10/00_core/ 아래에 있다.

우선 기존에 제안했던 (b)의 후보 2, AlN-mediated GaN/diamond topside integration에 대한 문헌 검증과 kill-search를 진행해줘. 제시된 논문 제목 자체도 미검증 단서로 취급하고, 출판사 원문에서 저자·학술지·연도·DOI 및 실제 AlN의 역할을 확인해줘. 이어서 bonding energy/strength, TBR, reliability를 체계적으로 함께 다룬 선행 논문·특허가 있는지 조사해줘. 검색 결과가 없다는 이유만으로 BLUE를 확정하지 마.

출력은 한국어로: 확인된 서지정보와 직접 출처 링크, 선행연구 비교표, KEEP/VERIFY/REJECT 판정 및 근거, 남은 검증 항목. 후보 1의 RED 판정도 근거 서지정보가 미검증이라는 점을 유지해줘. AI 답변 자체를 증거로 쓰지 마.

새 실험·계산이나 동결 임계값 변경은 하지 말고, 검증 결과는 별도 보고서로 정리해줘. HANDOFF의 8개 입력은 문서 작성 당시의 미결 항목이며 현재 환경에서 해결되었다고 추정하지 마. 이번 문헌 검증만으로 PREREG를 자동 수정하지 마.

---

# SOURCE: research_working_set/reports/FINAL_TRANSFER_README.md


# Final Transfer Package README

## Decision status
This project is now in "ALGORITHM DECIDED" state, per user instruction (2026-09-24 evening).
No new experiments or calculations should be started until the open decisions below are resolved
by the user, on any computer this package is moved to.

## Authoritative source of truth
`algorithm_v0.10_claude_final/AlN_HybridBonding_Algorithm_v0.10/00_core/PREREG.md` (v0.10) is the single source of truth for all
kill/go criteria. Everything else (STATUS.md, ALGORITHM_FINAL.md, HANDOFF.md) is a summary of it.

Read in this order when resuming on any machine:
1. `algorithm_v0.10_claude_final/AlN_HybridBonding_Algorithm_v0.10/00_core/ALGORITHM_FINAL.md` - declares the algorithm as decided,
   full S0-S5 structure, which RT-1..RT-12 red-team findings map to which stage.
2. `algorithm_v0.10_claude_final/AlN_HybridBonding_Algorithm_v0.10/00_core/HANDOFF.md` - what's confirmed / what folder to start
   execution in / the 8 required inputs before any further step can run.
3. `algorithm_v0.10_claude_final/AlN_HybridBonding_Algorithm_v0.10/00_core/STATUS.md` - one-page dashboard with the flowchart filled
   with actual computed results.
4. `algorithm_v0.10_claude_final/AlN_HybridBonding_Algorithm_v0.10/00_core/PREREG.md` - full frozen criteria, change log, references.
5. `algorithm_v0.10_claude_final/AlN_HybridBonding_Algorithm_v0.10/00_core/MANIFEST_sha256.txt` - integrity check for all 47 files.

## What is DECIDED (safe to reuse without re-deriving)
- S0/S0b materiality gate: CONDITIONAL-GO, HB-era 16-Hi ΔTj P50 = 2.06-2.78K depending on version;
  bonding-layer resistance is NOT the dominant lever - "removing SiO2" itself is most of the gain.
- S4.4: interface TBR does not control the go/no-go decision (gain retained >=80% even at
  R_int <= 1e-7 m2K/W); this reframes #6's original "TBR Pareto front" narrative as scientifically
  weak, and Claude proposed swapping #6 to a polarity/interface-structure narrative instead -
  **this swap is NOT yet decided by the user.**
- S4.7: AlN vs SiO2 capacitance ratio is fixed at 2.18-2.31x (independent of pitch/thickness in the
  parallel-plate approximation) - use directly, do not recompute.
- S5 pipeline: manuscript number-linter, DOI checker, synthetic-data scanner, reviewer-attack table
  generator all built and self-tested (found and fixed one real DOI typo during self-test).
- 3 self-corrections logged (stress-criteria contradiction, Model-B FEM validation gap, DOI typo) -
  keep these in any future methods-section writeup as evidence of rigor.

## What is NOT decided (do not proceed past these without the user)
See `HANDOFF.md` section 3 for the full 8-item table. Highlights:
1. Whether to keep #6 as "TBR Pareto front" (6-A) or switch to "polarity/interface structure and
   phonon transmission" (6-B), per Claude's S4.4 finding.
2. Target channel RC budget / crosstalk tolerance for judging whether the 2.18-2.31x capacitance
   ratio is acceptable.
3. Engineering justification for the 3K ΔTj GO threshold (DRAM retention/refresh margin literature).
4. Actual sputtering equipment specs (RF power/pressure/temperature/bias range, substrate size) -
   needed to finalize the L1 DOE factor levels.
5. Direct confirmation of the Phonon Olympics (JAP 2025, DOI 10.1063/5.0289819) paper's own
   recommended settings - Claude could not access the full text.
6. Lattice-constant citation confirmation (a=3.112, c=4.982 A currently flagged [LIT-verify]).

## Hard rule for whichever computer/session continues this
Per G-1 in the frozen rules: do not adjust any frozen kill/go threshold after seeing new data.
Any change must go through PREREG's Change Log with justification, before new data collection.

## Other files in this working set (supporting context, not authoritative)
- `reports/MASTER_Algorithm_v1.md` + `MASTER_Algorithm_v1_1_Claude_Update.md`: the multi-model
  (Gemini/Perplexity/ChatGPT/Liner/NotebookLM/Claude) design process that led to this final
  algorithm - useful for understanding *why* each rule exists, but PREREG.md v0.10 supersedes it
  for actual criteria values.
- `automation/`: the original provenance/synthetic-data-blocking scaffold (provenance.py,
  scan_for_synthetic.py, RESULTS_INDEX.md template) - now superseded in detail by
  `algorithm_v0.10_claude_final/AlN_HybridBonding_Algorithm_v0.10/S5_manuscript_pipeline/s5_tools.py`, but kept for reference.
- `network/`: Tailscale bootstrap checklist and sync scripts for moving this package to the
  simulation PC once network bootstrap/smoke tests pass (see network/HANDOFF_TO_SIM_PC.md).
- `raw_chat_evidence/`: merged Claude chat corpus used earlier for NotebookLM evidence-ledger work.

## Transfer instructions (for a human moving this to another computer)
1. Copy `research_working_set.zip` (or this whole folder) to the target machine by any available
   method (USB, cloud folder, or Tailscale sync once bootstrapped per network/HANDOFF_TO_SIM_PC.md).
2. On the target machine, open a fresh Claude web chat (not Code/Cowork) and say:
   "PREREG.md 기준으로 이어서 진행해줘" after uploading or pasting
   `algorithm_v0.10_claude_final/AlN_HybridBonding_Algorithm_v0.10/00_core/PREREG.md`.
3. Do not let the new session re-derive or silently change any frozen threshold. If it wants to
   change one, it must log the change in PREREG's Change Log first, per G-1.


# SOURCE: research_working_set/algorithm_v0.10_claude_final/AlN_HybridBonding_Algorithm_v0.10/00_core/ALGORITHM_FINAL.md


# 최종 알고리즘 선언 — AlN Hybrid Bonding Dielectric 연구
### 상태: **결정됨 (DECIDED)** — PREREG.md v0.10 기준 동결 완료

이 문서는 실행 문서가 아니라 **선언 문서**다. "무엇을 어떤 기준으로 판정할 것인가"는 전부 데이터 취득 전에 확정되었다. 남은 것은 실행뿐이며, 실행 결과가 어떻게 나오든 이 문서의 기준 자체는 (G-1 규칙에 따라) 근거 없이 바뀌지 않는다.

---

## 1. 전체 구조 (S0 → S5)

```
S0  물질성 게이트        [완료·CONDITIONAL-GO]  "AlN이 열적으로 유의미한가?"
S0b 3D 검증              [완료·KEEP]            "Cu pad 병렬경로가 판정을 뒤집는가?"
S1  공정→소자 스크리닝     [완료]                 hard-constraint 표로 후보 소자 필터링
S2  레드/블루오션 판정     [완료·재검토 신호 있음]  #6/#8/#12 포트폴리오, RT-11 블루오션 검정
─────────────────────── 실험 루프 (기준 동결, 미실행) ───────────────────────
L1  증착(응력/저응력)      [기준 동결·미실행]      DSD 15-run, 막힘 기준
L2  CMP/본딩              [기준 동결·미실행]      결합에너지, void, Plan B 분기
G*  TDTR 게이트           [기준 동결·미실행]      블라인드, 두께시리즈, 상한판정
L3  신뢰성 (#8)           [기준 동결·미실행]      비열등성, uHAST 우선, kinetics 선행
─────────────────────── 시뮬레이션 (기준 동결, 부분 실행) ───────────────────────
S4.1 DFT bulk            [워크플로 완료·미실행]   κ_bulk 벤치마크 (316 W/mK ±15%)
S4.2 계면 DFT             [초기구조 완료·미실행]   극성반전계면(RT-12) 후보 (HH-A/B)
S4.3 MLIP                [기준 동결·미실행]      held-out 3계열 고정
S4.4 계면 TBR             [계산 완료]            → TBR은 go/no-go 비결정 요인
S4.5 Nano-κ 블라인드       [기준 동결·미실행]      p=0 고정, 예측 선등록 후 측정
S4.6 regime map (#12)     [기준 동결·미실행]      명칭규칙(RT-10), 레드오션 인용 의무
S4.7 capacitance (RT-8)   [계산 완료]            비율 2.18-2.31배 확정, 허용판정 OPEN
─────────────────────── 출판 ───────────────────────
S5  논문 파이프라인        [완료·자체검증됨]       lint/gate/doi 도구, 리뷰어 공격표
```

## 2. 핵심 판정 (동결, 데이터로 뒤집히기 전까지 유효)

| 게이트 | 판정 | 근거 수치 | 이 판정이 바꾼 것 |
|---|---|---|---|
| S0 | **CONDITIONAL-GO** | ΔTj P50 = 2.71 K (HB-era, 16-Hi) | L1 목표를 "k 극대화"에서 "면당 AlN ≥0.5μm의 저응력 달성"으로 전환 |
| S0b | **KEEP** (모델 교정 후) | Model B 원본 오차 최대 +37% → FEM surrogate로 교정 | Model B 원본을 그대로 썼다면 결론이 부정확했을 것 |
| S4.4 | **TBR은 비결정적 요인** | R_int=1e-7 m²K/W에서도 이득 80% 유지 | #6 원래 서사(TBR Pareto front)의 근거 약화 → RT-12(극성계면) 대안 부상 |
| S4.7 | **capacitance 비율 확정, 허용여부 OPEN** | C_AlN/C_SiO2 = 2.18–2.31배 (기하무관) | #12 regime map에 정량 caveat 의무화 |
| S5 | **파이프라인 동작 확인** | fixture 14건 검출, 실제 DOI 오류 1건 자체 발견 | 투고 게이트의 실효성 입증 |

## 3. Red-team 발견 (RT-1 ~ RT-12) — 전부 알고리즘에 반영됨

| ID | 요지 | 반영 위치 |
|---|---|---|
| RT-1 | TDTR은 매립 계면을 단일 측정으로 분리 못함 | G* 두께시리즈+민감도 프로토콜 |
| RT-2 | "AlN-AlN 본딩"이 실은 산화 계면일 가능성 | L2-3 STEM-EELS, framing 분기 규칙 |
| RT-3 | 물질성(열 이득이 실재하는가) 미검증 | S0 신설 |
| RT-4 | #6/#8/#12가 G* 단일 실패점에 의존 | S2 G*-비의존 논문 40% 규칙 |
| RT-5 | 시뮬레이션-실험 순환검증 | 블라인드 프로토콜(S4.5), 후보선정-TBR 분리(S4.2) |
| RT-6 | 무한루프·기준이동 | G-1~G-5 전역규칙, N_max, time box |
| RT-7 | 불공정 비교(SiO2 대조 없음) | paired control 전 실험 단계 의무화 |
| RT-8 | 전기·기계적 비용 누락 | S4.7 capacitance, L1 막힘 기준 |
| RT-9 | 신뢰성 과대주장·습도 취약성 | L3 비열등성 설계, uHAST 최우선 |
| RT-10 | "디지털트윈" 용어 남용 | S4.6 명칭규칙(test vehicle 실측 조건부) |
| RT-11 | 블루오션 착시·공개순서 | S2 "왜 비어있는가" 3분기, G-6 특허우선 |
| RT-12 | 본딩계면은 반드시 극성반전 경계 (신규 발견) | S4.2 IDB 기반 후보 재설계, #6 서사 재검토 신호 |

## 4. 자기 정정 이력 (신뢰성의 증거)

| 항목 | 문제 | 정정 | 발견 계기 |
|---|---|---|---|
| S1 초기 응력 기준 | \|σ\|≤300MPa와 bow≤50μm이 0.5μm 막에서 물리적으로 모순 (Stoney 계산 시 93μm) | 막 힘(film force) 기준으로 교체 | L1 설계 중 자체 계산 |
| Model B (Cu pad 병렬경로) | 검증 없이 쓰면 AlN 전 구간 오차 최대 +37% | 3D FEM(S0b)으로 검증 후 보정 surrogate로 교체 | S0b 계획된 검증 단계 |
| Nano-κ 서지 인용 | DOI 10.1016/j.cpc.2023.10**8959** 오기입 (실제로는 무관한 논문) | Crossref 대조로 발견, 10.1016/j.cpc.2023.10**8954**로 정정 | S5 doi 검증 도구 실행 |

이 세 건 모두 **데이터 취득 전, G-1 규칙에 따라 정당하게 정정되었고 Change Log(PREREG §9)에 기록되어 있다.**

## 5. 결정되지 않은 것 (의도적으로 열어둠)

아래는 "설계 미비"가 아니라 **실제 실험/장비/문헌 확인 없이는 원칙적으로 결정할 수 없는 항목**이다. HANDOFF.md §3에 구체 입력 요건을 정리했다.

1. #6 논문 서사 (TBR축 유지 vs 극성계면축 전환)
2. #12-4 capacitance 허용 기준 (설계 RC/crosstalk 예산 필요)
3. S0 GO 임계값(3K)의 공학적 근거 문헌
4. Phonon Olympics(JAP 2025) 원문 대조
5. L1 DSD 인자 수준의 장비 사양 확정
6. 실험 격자상수 인용문헌 확정

## 6. 선언

**PREREG.md v0.10에 동결된 기준은 지금 이 시점에서 "연구팀이 무엇을 봐도 판정 방법을 바꾸지 않겠다"고 약속한 상태다.** 이 알고리즘은 즉시 실행 가능한 상태로 패키징되어 있으며, 실험이나 계산이 재개되는 시점에 PREREG.md를 열어 해당 섹션의 동결 기준대로 진행하면 된다. 새로운 데이터는 Change Log에 추가될 뿐, 이미 동결된 기준 자체는 근거 문서 없이 수정되지 않는다.



# SOURCE: research_working_set/algorithm_v0.10_claude_final/AlN_HybridBonding_Algorithm_v0.10/00_core/HANDOFF.md


# 인수인계 문서 — 다른 컴퓨터/다른 세션에서 이어가기 위한 안내

작성 시점: 대화 종료 시점 (PREREG.md v0.10)
대상 독자: 미래의 본인, 또는 이 프로젝트를 넘겨받는 사람, 또는 새 세션의 Claude

## 0. 먼저 읽을 순서

1. `00_core/ALGORITHM_FINAL.md` — 무엇이 결정되었는지 5분 요약
2. `00_core/STATUS.md` — 어느 단계가 완료/미실행인지 플로우차트
3. `00_core/PREREG.md` — **모든 기준의 원본(source of truth)**. 다른 요약본과 충돌하면 이 파일이 우선.
4. 이 문서(HANDOFF.md) §2 폴더 안내를 보고 필요한 하위 폴더로 이동

## 1. 지금 확정된 것 (재논의 불필요, 바로 사용 가능)

- **S0/S0b 판정**: HB-era 16-Hi 조건에서 ΔTj P50 2.71 K, CONDITIONAL-GO. 재계산 불필요.
- **L1/L2/L3/G* 의 kill/go 기준**: PREREG §3A/3B/3C/3(G*)에 전부 수치로 동결됨. 실험만 하면 됨.
- **S4.1~4.7 계산 설정과 판정 기준**: PREREG §4.1~4.7에 동결됨. 계산만 하면 됨.
- **S5 도구 체인**: `S5_manuscript_pipeline/s5_tools.py`가 동작 확인됨 (index/lint/render/doi/rules/gate).
- **전역 규칙 G-1~G-6**: PREREG §전역규칙. 무한루프 방지, 기준 동결 원칙 — 앞으로도 그대로 적용.

## 2. 폴더 안내 (실행 순서대로)

| 폴더 | 내용 | 다음 행동 |
|---|---|---|
| `00_core/` | PREREG.md(원본), STATUS.md, ALGORITHM_FINAL.md, 이 문서 | 항상 먼저 참조 |
| `S0_materiality/` | S0 v0.1~v0.4 계산 스크립트·결과 (재현 가능, seed 고정) | 참조용, 재실행 불필요 |
| `S0b_FEM/` | 3D unit-cell FEM 솔버 + 결과 | 참조용, t_b≠1μm 외삽 시에만 재실행 |
| `L1_deposition/` | DSD 15-run 실험설계, film force 계산기, 런시트 CSV | **여기부터 실행 시작 지점** — 런시트에 실측값 채우기 |
| `L3_reliability/` | uHAST/HTS 가속계수, success-run 표본수 계산 | L1 GO 이후 참조 |
| `S4.1_DFT_bulk/` | QE+phono3py 워크플로 (`s41_workflow.py`) | conv 단계부터 실행 (아래 §4 참조) |
| `S4.2-4.3_interface_MLIP/` | 계면/변형/결함 초기구조 생성기 (ASE), MLIP 데이터 매니페스트 스키마 | 구조는 모두 **비이완 초기 추정** |
| `S4.4_TBR_budget/` | 계면저항 민감도 계산 (완료, 결론: TBR 비결정적) | 참조용 |
| `S4.7_capacitance/` | capacitance 비율 계산 (완료, 결론: 2.18-2.31배) | 참조용 |
| `S5_manuscript_pipeline/` | 원고 lint/gate 도구, 리뷰어 공격표, results_index.csv 시작본 | 원고 작성 시작하면 바로 사용 |

## 3. 다음에 반드시 필요한 입력 (실행 전 확보할 것)

이 항목들이 없으면 해당 단계를 시작할 수 없거나, 시작해도 판정이 완결되지 않는다.

| # | 필요한 입력 | 없으면 막히는 단계 | 비고 |
|---|---|---|---|
| 1 | 스퍼터 장비 실제 사양 (RF power 범위, 압력, 온도, bias 가능 여부, 기판 크기) | L1 DSD 인자 수준 확정 | `L1_deposition/l1_doe.py`의 `factors`를 장비값으로 교체 후 CSV 재생성 |
| 2 | #6 논문 서사 결정 (TBR축 유지 / 극성계면축 전환) | S4.2 계산 우선순위, S2 포트폴리오 표 | ALGORITHM_FINAL.md §5-1 참조 |
| 3 | 목표 채널 RC 지연 예산 또는 crosstalk 허용치 | S4.7 capacitance 최종 판정, #12 regime map 완결 | 없으면 "OPEN, caveat만 기재" 상태 유지 |
| 4 | S0 GO 임계값(3K)의 공학적 근거 문헌 (DRAM retention/refresh 마진) | S0 판정의 정당화 서술 (판정 자체는 이미 유효) | 값 자체는 변경하지 않음 (G-1) |
| 5 | Phonon Olympics (JAP 2025) 원문 | S4.1 벤치마크 비교표 | Claude가 원문을 확인하지 못한 상태로 동결됨 |
| 6 | 실험 wurtzite AlN 격자상수의 정확한 인용문헌 | S4.1 설정 각주 | 현재 a=3.112Å, c=4.982Å는 [LIT-verify] 상태 |
| 7 | QE 7.2 소스 빌드 환경 (WSL2) | S4.1 실제 실행 | Ubuntu 24.04 apt 패키지 QE 6.7은 크래시함 (검증됨, PREREG 4.1.5) |
| 8 | PseudoDojo pseudo-H (Z=0.75) 생성 (ld1.x) | S4.2 계면 구조 표면 종결 | PseudoDojo 라이브러리에 기성품 없음 |

## 4. 재개 시 실행 순서 (권장)

```
1. L1_deposition/L1_DSD_runsheet.csv 를 장비 사양에 맞게 조정 → 15-run 증착·측정
2. (병행 가능) S4.1_DFT_bulk/s41_workflow.py conv  ← QE 7.2 환경에서
   결과를 가져와 다음 세션에 "S4.1 conv 결과: {...}" 형태로 제공하면 판정 가능
3. L1 GO 판정 나오면 → L2_CMP/본딩 (PREREG §3B) 착수
4. L2 GO 판정 나오면 → G* TDTR (PREREG §3, G*) + S4.2 계면 DFT 병행
5. 모든 실험 게이트 통과 후 → S5_manuscript_pipeline/s5_tools.py 로 원고 lint
```

## 5. 새 세션(Claude 등)에게 주는 지침

이 패키지를 새 대화에 올리고 "PREREG.md 기준으로 이어서 진행해줘"라고 요청하면 된다.
- **하지 말아야 할 것**: 이미 동결된 kill/go 임계값을 결과를 보고 조정하는 것 (G-1 위반). 재계산 시 기존 스크립트의 seed(20260924)를 그대로 사용해 재현성을 유지할 것.
- **해야 할 것**: 새 데이터가 들어오면 PREREG.md의 해당 섹션에 결과를 채우고 Change Log(§9)에 기록. 판정이 바뀌면(GO↔KILL) STATUS.md도 갱신.
- 이 대화에서 발견된 자기 정정 3건(ALGORITHM_FINAL.md §4)은 "이 알고리즘이 스스로 오류를 잡아낸 사례"로, 방법론 논의나 리뷰어 대응에 재사용 가능.

## 6. 무결성 확인

패키지의 모든 스크립트와 JSON 결과 파일의 sha256은 PREREG.md 본문에 각 섹션별로 기록되어 있다. 파일을 다른 컴퓨터로 옮긴 뒤,

```bash
sha256sum <file> 
```

로 PREREG.md에 기록된 해시와 대조하면 전송 중 손상 여부를 확인할 수 있다.



# SOURCE: research_working_set/algorithm_v0.10_claude_final/AlN_HybridBonding_Algorithm_v0.10/00_core/PREREG.md


# PREREG.md — AlN Hybrid Bonding Dielectric 연구 사전등록

> 규칙 G-1: 이 문서의 kill/go 기준은 해당 데이터 취득 **전에** commit 한다.
> 변경은 새 데이터 취득 전 + 사유 기록 시에만 허용하며, 변경 이력은 논문 SI에 공개한다.
> 태그: `[GIVEN]` 연구자 지정 / `[ASSUMED]` 미검증 가정 / `[MEASURED]` 실측 / `[LIT]` 문헌(DOI 필수) / `[MODEL]` 모델링 선택

---

## 0. 메타데이터

| 항목 | 값 |
|---|---|
| 문서 버전 | v0.10 (#12-4 capacitance penalty 계산 완료, #6 서사 결정 대기) |
| 동결 commit hash | `<git rev-parse HEAD 기입>` |
| 동결 일시 | `<YYYY-MM-DD>` |
| 책임자 | `<이름>` |
| 관련 논문 | #6 (TBR/bonding), #8 (reliability), #12 (HBM regime map) |

---

## 1. S0 물질성 게이트

### 1.1 가설
H0-S0: HBM hybrid bonding 스택에서 bonding dielectric을 SiO₂에서 sputtered AlN(0002)로 바꿔도 base-die Tj 감소(ΔTj)는 실용적으로 무의미하다.

### 1.2 판정 지표 (동결)
- ΔTj 분포: P5(worst) / P50(expected) / P95(best), 16-Hi 기준
- 본딩층 저항 비율: n·R''_layer,SiO₂ / (n·(R''_layer,SiO₂ + R''_die)) 의 P50 (내부 스택 기준)

### 1.3 Kill / Go 기준 (동결, S0 계산 이전에 정의됨)

| 판정 | 조건 |
|---|---|
| KILL | ΔTj P95 < 1 K **또는** 본딩층 비율 P50 < 5 % |
| GO | ΔTj P50 ≥ 3 K |
| CONDITIONAL-GO | 위 둘 다 아님 → regime 한정 서사로만 진행, S0b(3D 모델) 필수 |

- 판정은 **Model A와 Model B 중 보수적인 쪽(Model B)** 을 기준으로 한다.
- `[TODO]` 3 K 임계값의 공학적 근거(DRAM retention/refresh 마진 등)를 `[LIT]`로 보강한다. **근거 보강 시 값은 바꾸지 않는다** (값 변경 = goalpost moving).

### 1.4 모델 정의 `[MODEL]`
- 1D 직렬 저항망, 16-Hi(보조: 12-Hi), 열은 f_up 비율만큼 상부 방열 경로로 이동.
- 계면 j의 열유속: q_j = f_up·(P_base + (j−1)·P_core)/A
- ΔTj = Σ_j q_j·(R''_layer,SiO₂ − R''_layer,AlN)
- Model A: dielectric only (Cu pad 무시, dielectric 중요도의 상한)
- Model B: Cu pad 병렬 경로 + dense-array constriction ψ=(1−ε)^1.5, pad array 면적비 f_array
- Monte Carlo N = 200,000, seed = 20260924
- 코드: `s0_materiality.py` sha256 `f3146e751062a7263ddb2880930d3070f9278f550f0d5934120ea621ab0c129c`
- 후속: `s0_followup.py` sha256 `54b9ce4baa4d863608cdd37a0ba8f82b4324b3294a6996c2ebc74b6b3e395f28`

### 1.5 입력 분포

| 변수 | 분포 | 범위 | 태그 |
|---|---|---|---|
| k_AlN (cross-plane) | log-uniform | 20–150 W/mK | [GIVEN] |
| TBR_bond,AlN | log-uniform | 1e-9 – 5e-8 m²K/W | [GIVEN] |
| k_SiO₂ | uniform | 1.3–1.4 W/mK | [GIVEN] |
| TBR_side,AlN (×2) | log-uniform | 1e-9 – 1e-8 | [ASSUMED] |
| TBR_bond,SiO₂ | log-uniform | 1e-9 – 5e-9 | [ASSUMED] |
| t_b (계면당 dielectric 총두께) | uniform | 0.4–2.0 μm | [ASSUMED] |
| P_total (stack) | uniform | 30–60 W | [ASSUMED] |
| f_base | uniform | 0.30–0.50 | [ASSUMED] |
| f_up | uniform | 0.60–0.90 | [ASSUMED] |
| A (die 면적) | uniform | 100–130 mm² | [ASSUMED] |
| t_die / k_Si | uniform | 30–50 μm / 100–130 W/mK | [ASSUMED] |
| t_BEOL / k_BEOL | uniform / log-uniform | 2–6 μm / 2–10 W/mK | [ASSUMED] |
| R_pkg (TIM+lid+sink) | uniform | 1e-5 – 4e-5 m²K/W | [ASSUMED] |
| pitch | uniform | 3–10 μm | [ASSUMED] |
| pad 반경/pitch | uniform | 0.20–0.30 | [ASSUMED] |
| k_spread | log-uniform | 5–120 W/mK | [ASSUMED] |
| f_array | uniform | 0.2–1.0 | [ASSUMED] |
| k_Cu / R_CuCu | uniform / log-uniform | 300–400 W/mK / 1e-9 – 1e-8 | [ASSUMED] |

### 1.6 S0 결과 (v0.1, 입력이 대부분 [ASSUMED] → **증거가 아니라 방향 설정용**)

| ID | 항목 | 16-Hi Model A | 16-Hi Model B |
|---|---|---|---|
| S0-001 | ΔTj P5 / P50 / P95 [K] | 0.95 / 2.56 / 5.09 | 0.18 / 0.76 / 2.31 |
| S0-002 | P(ΔTj ≥ 3 K) | 38 % | 1.5 % |
| S0-003 | 본딩층 비율 P50 (내부 / 패키지 포함) | 40 % / 23 % | 19 % / 9 % |
| S0-004 | 판정 | CONDITIONAL-GO | CONDITIONAL-GO |

- 12-Hi Model B: ΔTj P50 0.57 K, P95 1.72 K → CONDITIONAL-GO (KILL 경계에 근접)
- 민감도(PRCC) Model A: t_b 0.98 > P_total 0.91 > f_up 0.78 > A −0.63 … k_AlN 0.18, TBR_bond −0.16
- 민감도(PRCC) Model B: k_spread −0.93 > f_array −0.80 > P_total 0.67 > pitch 0.66 > t_b 0.66

### 1.7 S0 판정: **CONDITIONAL-GO** (동결 기준 적용 결과, 해석 변경 금지)

---

## 2. S0b — 3D unit-cell 검증 (완료)

### 2.1 목적
Model B의 constriction 근사(가장 큰 모델 불확도)를 3D 유한체적 unit cell로 검증한다.

### 2.2 동결 기준 (v0.1에서 동결, 변경 없음)
| 판정 | 조건 |
|---|---|
| 모델 검증 | unit cell vs Model B의 R''_layer 차이 ≤ 20 % |
| KILL(HBM 평균 Tj 서사) | 검증된 모델로 16-Hi ΔTj P50 < 1 K |
| 유지 | ΔTj P50 ≥ 1 K인 regime이 존재 → #12 regime map 축으로 채택 |

### 2.3 솔버 `[FEM]`
- quarter-cell 3D 정상상태 유한체적, 측벽 단열(대칭), 상하 고정온도, TBR은 2–4 nm 등가 시트로 삽입
- 검증: 균질 매질에서 R''_eff = t/k 일치 (오차 < 1e-10 %); 격자 수렴 nx 20→28→36에서 변화 < 1 %
- 코드: `s0b_unitcell.py` sha256 `f0a98e39abb0dfe6a8e6cb99e1ebaf7be6e032225d52e2cacf7730e18efee32c`, runner `s0b_run.py` sha256 `f61acb3e48f8cc2ebc547ee02746c1ae38c87b8cd7edbea0a754420f6e846f1e`
- 결과: `s0b_results.jsonl` sha256 `52f8f0b6124cd1c167d8899c87dea099667642678e22a41726b402550a63b09e`

### 2.4 결과
| ID | 항목 | 결과 |
|---|---|---|
| S0b-001 | Model B 오차 (SiO₂, k_spread 25/120) | −4.5 ~ +8.5 % → 통과 |
| S0b-002 | Model B 오차 (SiO₂ k_spread 5, AlN 전 구간) | +7 ~ +37 % → **불통과** |
| S0b-003 | dummy pad 영역(via 비연결, pitch 12–30 μm) R''_eff / R''_diel | SiO₂ 0.86–0.98, AlN 0.94–0.99 → 사실상 dielectric-only |
| S0b-004 | 조치 | Model B를 FEM 보정계수 R_FEM/R_B (pitch × log k_spread 격자 보간)로 교정한 surrogate로 대체 |

- 보정 적용 범위 제한: t_b = 1 μm, w/p = 0.4에서만 보정됨 → 다른 t_b·w/p에서의 외삽은 `[MODEL]` 불확도로 남음

### 2.5 [ASSUMED] → 문헌 대체 현황
| 변수 | v0.1 | v0.2 | 태그 / 근거 |
|---|---|---|---|
| t_b (계면당 총두께) | 0.4–2.0 μm | 0.3–1.6 μm | [LIT] 면당 pad/dielectric 0.15–0.8 μm (US 12266622; imec Cu/SiCN W2W pad height ~550 nm, Microelectron. Reliab. 2022; FEM study 0.15–0.45 μm) |
| active pad pitch / width | 3–10 μm / 0.4–0.6 p | 6–9 μm / 2.5–3.5 μm | [LIT] US 11769724 (일부 실시예, HBM 전용 아님) |
| dummy pad pitch | (단일 f_array) | 12–30 μm, via 비연결 | [LIT] US 11769724 (11–30 μm), US 11257805 (dummy pad 하부 via 없음) |
| P_total | 30–60 W | 40–100 W (HB-era) | [LIT-2nd] HBM4E ≤80 W, HBM5 ~100 W 로드맵 전망(2차 보도) — 전망치 |
| f_act (active pad 영역 면적비) | f_array 0.2–1.0 | 0.05–0.40 | **[ASSUMED] 문헌 미확보 — 잔여 1순위 미지수** |
| k_spread | 5–120 | 5–120 | [ASSUMED] |
| f_up, f_base, A, die/BEOL, R_pkg | — | 변경 없음 | [ASSUMED] |

- 배제한 출처: 자동생성형 특허분석 리포트(HBM4 12–15 W/stack 등) — 근거 불명확으로 사용하지 않음

### 2.6 S0 v0.2 결과 (`s0_v02.py` sha256 `11349ed72a7bf5ed51b0f5703cd616d0ab4914fb7028eaf59745f898dc31fe55`, 결과 `s0_v02_results.json` sha256 `35f0065b3cad2e02c88069ac1f14779a432327299449b481f58f3cc61db9dbf7`)

| ID | 시나리오 | ΔTj P5/P50/P95 [K] | P(≥3 K) | 본딩층 비율 P50 (내부/전체) | S0 판정 | S0b 판정 |
|---|---|---|---|---|---|---|
| S0-101 | HB-era 16-Hi | 0.70 / 1.84 / 4.31 | 19 % | 25 % / 13 % | CONDITIONAL-GO | KEEP |
| S0-102 | HB-era 12-Hi | 0.52 / 1.37 / 3.21 | 7 % | 25 % / 11 % | CONDITIONAL-GO | KEEP |
| S0-103 | HBM4-level 16-Hi | 0.48 / 1.20 / 2.69 | 3 % | 25 % / 13 % | CONDITIONAL-GO | KEEP |
| S0-104 | HBM4-level 12-Hi | 0.35 / 0.89 / 2.00 | 0.2 % | 25 % / 11 % | CONDITIONAL-GO | KILL(평균 Tj 서사) |

- 민감도(PRCC, HB-era 16-Hi): t_b 0.88 > P_total 0.81 > k_spread −0.74 > f_act −0.62 > f_up 0.52 > pitch_act 0.48
- Regime (HB-era 16-Hi 조건부 P50): t_b > 1.0 μm → 2.53 K; t_b > 1.0 μm & P > 70 W → **3.21 K (GO 기준 충족)**; f_act < 0.15 → 2.27 K

### 2.7 판정
- 주 판정(HB-era 16-Hi): **CONDITIONAL-GO + S0b KEEP**
- #12 regime map 1차 축: t_b, P_total, f_act(또는 k_spread), die 수
- 12-Hi / HBM4-level 전력에서는 평균 Tj 서사를 쓰지 않는다


### 2.8 S0 v0.3 — f_act 문헌 경계 반영 (`s0_v03.py` sha256 `de111bb20a84ec6594116758d2abf1ed9b94e873e87d67696fb904776ba44232`, 결과 `s0_v03_results.json` sha256 `fc45ddd9dafac0a19975a7e238fb56cc7875358cc510282c6763be6e7a137d8a`)
- f_act: 0.05–0.40 → **0.05–0.25**. 상한 근거 [LIT]: DRAM에서 TSV가 들어가는 주변회로(periphery)가 칩 면적의 20–30 % (SK hynix, EE Times 2024), TSV 어레이는 die 면적의 작은 비율 (US 8344493). 하한 0.05는 [ASSUMED].

| ID | 시나리오 | ΔTj P5/P50/P95 [K] | P(≥3 K) | 본딩층 비율 P50 (내부/전체) | S0 | S0b |
|---|---|---|---|---|---|---|
| S0-201 | HB-era 16-Hi | 0.80 / 2.06 / 4.63 | 25 % | 27 % / 14 % | CONDITIONAL-GO | KEEP |
| S0-202 | HB-era 12-Hi | 0.59 / 1.53 / 3.44 | 9 % | 27 % / 12 % | CONDITIONAL-GO | KEEP |
| S0-203 | HBM4-level 16-Hi | 0.55 / 1.35 / 2.88 | 4 % | 27 % / 14 % | CONDITIONAL-GO | KEEP |
| S0-204 | HBM4-level 12-Hi | 0.40 / 1.00 / 2.13 | 0 % | 27 % / 12 % | CONDITIONAL-GO | KEEP (경계, P50 = 1.00 K) |

- Regime (HB-era 16-Hi, 조건부 P50): t_b > 1.0 μm & P > 70 W → **3.60 K**; t_b > 1.0 μm → 2.86 K; t_b ≤ 0.6 μm → 1.16 K; t_b ≤ 0.6 μm & P > 70 W → 1.44 K
- PRCC: t_b 0.91 > P_total 0.84 > k_spread −0.70 > f_up 0.57 > f_act −0.51
- 판정: S0 CONDITIONAL-GO 유지. **#12 핵심 regime = 16-Hi, HB-era 전력(>70 W), t_b > 1 μm (면당 AlN > 0.5 μm)**
- S0-204는 판정 경계값이므로 12-Hi/HBM4급 전력 regime을 논문에서 "benefit 있음"으로 서술하지 않는다.



### 2.9 S0 v0.4 — f_up·f_base 문헌 반영 + Plan B(oxide cap) (`s0_v04.py` sha256 `39eea794edda554cf7021125c6912e819dfdfd2bea8fe12c79698c38d5853fe8`, 결과 `s0_v04_results.json` sha256 `f476e9cba9467a8943f3f15350561d2b4c433e5eaf5b1d15ec2282aa3f65002e`)
- f_up: 0.60–0.90 → **0.85–1.00** [LIT-anchor]: 칩 발열의 약 95 %가 패키지 상부로 제거 (imec, IEEE Spectrum 2026); Micron 특허 해석은 기판 측 방열 0 가정 (US 9269646). HBM 전용 측정값 아님.
- f_base: 0.30–0.50 → **0.30–0.65** [LIT-anchor + ASSUMED]: 상한 앵커 = HMC 해석 예시 logic 11.2 W / DRAM 1.6 W×4 → 0.64 (US 9269646, HMC이며 HBM 아님)
- Plan B: AlN 코어 + 면당 20–50 nm SiO₂/SiCN bonding cap [ASSUMED], cap 계면 TBR 1e-9–1e-8

| ID | 시나리오 | ΔTj P5/P50/P95 [K] | P(≥3 K) | S0 | S0b |
|---|---|---|---|---|---|
| S0-301 | HB-era 16-Hi | 1.06 / 2.71 / 5.98 | 43 % | CONDITIONAL-GO | KEEP |
| S0-302 | HB-era 12-Hi | 0.79 / 2.02 / 4.45 | 23 % | CONDITIONAL-GO | KEEP |
| S0-303 | HBM4-level 16-Hi | 0.72 / 1.77 / 3.71 | 14 % | CONDITIONAL-GO | KEEP |
| S0-304 | HBM4-level 12-Hi | 0.54 / 1.32 / 2.77 | 3 % | CONDITIONAL-GO | KEEP |
| S0-305 | HB-era 16-Hi, **Plan B cap** | 0.85 / 2.43 / 5.64 | 36 % | CONDITIONAL-GO | KEEP |
| S0-306 | HB-era 12-Hi, Plan B cap | 0.63 / 1.81 / 4.19 | 18 % | CONDITIONAL-GO | KEEP |

- Regime (HB-era 16-Hi 조건부 P50): t_b > 1.0 μm → **3.75 K (GO)**; t_b > 1.0 μm & P > 70 W → 4.72 K; t_b ≤ 0.6 μm → 1.52 K
- Plan B는 uncapped 대비 P50 약 90 % 유지 (2.43 / 2.71). 단 cap 적용 시 FEM 보정계수는 uncapped AlN 값을 그대로 사용 [MODEL 근사]
- 판정: CONDITIONAL-GO 유지. GO regime이 "HB-era 전력 & t_b > 1 μm"에서 "t_b > 1 μm"로 확장

## 3A. L1 — 후막 AlN 저응력 증착 루프 (기준 동결, 데이터 취득 전)

### 3A.1 목적
S0 GO regime(면당 AlN ≥ 0.5 μm)을 공정적으로 달성 가능한지 판정한다.

### 3A.2 기준 정정 (자기 정정 기록)
- 초기 S1 제안값 "|σ| ≤ 300 MPa **그리고** 300 mm bow ≤ 50 μm"는 0.5 μm 막에서 **서로 모순** (Stoney: 300 MPa × 0.5 μm → bow 93 μm). 초기 제안 오류이며 L1 데이터 취득 전 정정한다.
- 대체 지표: **막 힘(film force) |σ·t|** — 웨이퍼 크기와 무관하게 이전 가능. 300 mm/775 μm에서 bow ≤ 50 μm ⇔ |σ·t| ≤ 80 N/m (`l1_doe.py` sha256 `1b576b21a2fc12b0ecabccd23c73a4cf6fddd47fe82cdb526c04340e19052498`). bow 50 μm 자체는 [ASSUMED].

### 3A.3 동결 기준 (면당 t = 0.5 μm 기준)
| 항목 | GO 조건 | 측정 |
|---|---|---|
| 막 힘 | \|σ·t\| ≤ 80 N/m (⇔ \|σ\| ≤ 160 MPa @ 0.5 μm) **그리고** ≤ 동일 장비·동일 lab의 PECVD SiO₂ baseline 막 힘 × 1.2 | wafer curvature (Stoney) |
| 열 이력 | RT→400 °C→RT 후 응력 변화 \|Δσ\| ≤ 50 MPa, 크랙/박리 없음 | in-situ 또는 전후 curvature, 광학현미경 |
| 결정성 | (0002) rocking FWHM ≤ 3° | XRD |
| 표면(증착 직후) | RMS ≤ 2 nm (5×5 μm) — CMP 목표 0.5 nm는 L2에서 판정 | AFM |
| 산소 | ≤ 2 at% | XPS depth / SIMS |
| 열전도 하한 | k_cross ≥ 20 W/mK (GO 후보 레시피 1–2개만) | TDTR |
| 재현성 | 주요 지표 CV ≤ 10 % (wafer ≥ 2장) | — |

### 3A.4 실험 설계
- Round 1: Definitive Screening Design, 5 인자 + fake 인자 1 (오차 추정), 12 + center 3 = **15 run**, t = 0.5 μm, run 순서 무작위(seed 20260924). 인자 수준은 [ASSUMED] → 장비 사양으로 조정 후 동결: RF power density 2/4/6 W/cm², N₂ 25/50/75 %, 압력 2/5/8 mTorr, 기판온도 50/200/350 °C, RF bias 0/15/30 W. 런시트 `L1_DSD_runsheet.csv` sha256 `3887bc5980bac494e1c0c6faf7c7d28b55a93b90b9067523a95349341ff1890d`
- Round 2: 상위 2 레시피로 두께 시리즈 0.25 / 0.5 / 0.8 μm → σ(t) 곡선, 열 이력 시험
- Round 3 (필요 시): 응력 보상(압력 grading 이층막 등) 1회

### 3A.5 Kill / 루프 제한
- N_max = 3 라운드, time box 3개월, G-3 정체 판정 적용
- **KILL(두꺼운 t_b regime)**: 3라운드 후 0.5 μm에서 막 힘 기준 불통과 → #12 regime을 t_b ≤ 0.6 μm로 축소 (S0-201 기준 ΔTj P50 1.16 K → 평균 Tj 서사 폐기, 비열적 가치(CTE·Cu barrier) 서사로 전환 검토)
- **D2W 주의 [MODEL]**: 40 μm 박막화 die(11 mm)에서 단일면 150 MPa × 0.5 μm → die bow 약 24 μm (균형 막 무시). L2에서 die 수준 warpage를 별도 판정 항목으로 추가할 것


## 3B. L2 — CMP / 본딩 루프 (기준 동결, 데이터 취득 전)

### 3B.1 범위 선언 (리뷰어 공격 사전 대응)
- 1차 범위: **blanket AlN–AlN 유전체 본딩** (Cu 없음). G* TDTR 시편도 여기서 제작.
- 패턴 Cu/AlN hybrid bonding은 fab 접근이 확보될 때만 L2-4로 수행. 미확보 시 논문 claim은 "hybrid bonding용 bonding dielectric"으로 한정하고 이를 본문에 명시.

### 3B.2 단계 및 동결 기준
| 단계 | 내용 | GO | KILL / 분기 |
|---|---|---|---|
| L2-1 CMP | blanket AlN 0.5–0.8 μm. 인자: slurry pH 3수준 × down pressure 2수준 | RMS ≤ 0.5 nm (AFM 5×5 μm, 3점 이상); DI water 24 h soak 후 두께 변화 < 1 %, 표면 O 증가 기록 | 3라운드 후 RMS > 0.5 nm → **Plan B** |
| L2-2 활성화·어닐 | O₂ vs N₂ plasma × 어닐 200 / 250 / 300 °C (2 h), 조건당 3쌍 = 18쌍 + SiO₂ paired control 250·300 °C × 3쌍 | 결합에너지 ≥ 1.5 J/m² (≤ 300 °C) **그리고** ≥ 동일 조건 SiO₂ control의 0.7배; C-SAM void ≤ 1 % | 최선 조건 < 1.0 J/m² 또는 void > 5 % → **Plan B** |
| L2-3 계면 | 최선·최악 조건 HAADF-STEM + EELS | d_int 측정·기록 (합불 아님) | d_int ≥ 2 nm → claim을 "AlN/AlOx interlayer/AlN"으로 변경 (S3 규칙) |
| L2-4 (선택) | 패턴 Cu/AlN, daisy chain | Cu recess < 5 nm, 체인 저항 수율 기록 | fab 미확보 → 범위 한정 |
| L2-5 (D2W) | 40 μm 박막 die warpage (shadow moiré) | die bow ≤ 10 μm [ASSUMED] | 측정 불가 → 계산값만 보고, claim을 W2W로 한정 |

- 결합에너지 측정: 이중외팔보(DCB/razor blade)를 **건조 N₂ 분위기**에서 수행 (습기에 의한 응력부식으로 과소평가 방지). 동일 방법으로 SiO₂ control 측정.
- N_max = 3 (각 단계), time box 3개월, G-3/G-4 적용.

### 3B.3 Plan B — AlN 코어 + oxide/SiCN bonding cap (사전 등록 분기)
- 트리거: L2-1 또는 L2-2 KILL
- 구조: AlN(면당 ≥ 0.5 μm) + SiO₂ 또는 SiCN 20–50 nm cap, 접합은 기존 oxide/SiCN 공정
- GO: 결합에너지 ≥ SiO₂ control의 0.8배, void ≤ 1 %
- 열적 기대치: S0-305 (uncapped 대비 P50 약 90 %)
- 논문 framing 변경: "AlN–AlN bonding" → "AlN thermal core with bonding cap". **분기 조건과 framing을 지금 등록하므로 사후 변경이 아님.**


## 3C. L3 — 신뢰성 루프 (#8, 기준 동결, 데이터 취득 전)

### 3C.1 핵심 판단
- 계산 (`l3_calc.py` sha256 `bde70e74737bdb32402c8045ed734e9380ce436edacb0820fe7db8c8956a4434`): uHAST 130 °C/85 %RH 96 h의 현장(30 °C/60 %RH [ASSUMED]) 등가 수명은 Peck 모델(m=3)에서 **Ea 0.5 eV → 3.6년, 0.7 eV → 24년, 0.9 eV → 160년**. AlN 가수분해의 Ea를 모르면 uHAST 통과는 수명에 대해 아무것도 말해주지 않는다. → **L3-0(가수분해 kinetics)이 선행 필수.**
- 표본수: 무고장 success-run, 신뢰도 90 % 기준 n=3 → R ≥ 0.46, n=5 → 0.63, n=22 → 0.90. 학술 규모로 절대 신뢰도 주장은 불가 → **#8의 claim은 "SiO₂ 대조 대비 비열등성(non-inferiority)"으로 설계**한다.
- 가수분해는 pH와 온도가 높을수록 가속, pH≈1에서는 사실상 억제 [LIT: PMC5707611 인용 문헌]. 반응: AlN + 2H₂O → 비정질 AlOOH + NH₃ → Al(OH)₃, 초기 속도는 계면 반응 지배(unreacted-core) [LIT: J. Eur. Ceram. Soc. 2011, 분말 기준]. → L2-1 CMP의 알칼리 slurry도 같은 위험 (교차 확인).

### 3C.2 단계 및 동결 기준
| 단계 | 내용 | 측정 | GO | KILL / 분기 |
|---|---|---|---|---|
| L3-0 kinetics | blanket AlN (± cap) 쿠폰, 85/110/130 °C × 85 %RH, 0/24/96/250 h | 두께 손실(엘립소), O(XPS), Al–OH(FTIR), RMS | Arrhenius 적합 R² ≥ 0.9로 Ea 추출 (3온도, 1/T 폭 3.1×10⁻⁴ K⁻¹) | 적합 실패 → 시간점 1회 추가, 이후 Ea 범위(0.5–0.9 eV) 최악값으로 보수 판정 |
| L3-1 uHAST (최우선) | 본딩 쌍, JESD22-A118 130 °C/85 %RH 96 h | C-SAM 가장자리 침투 거리 x, void 증가, TDTR | 추출 Ea로 환산한 10년 침투 거리 ≤ keep-out 50 μm [ASSUMED] **그리고** SiO₂ 대조 대비 비열등 | 침투 > keep-out → 조건부: edge seal/Plan B 필요로 #12 regime에 반영; 박리 → NO-GO(습윤 환경) |
| L3-2 HTS | JESD22-A103 150 °C 1000 h | TDTR R''_AlN층, C-SAM | R''_AlN층 변화 ≤ 20 % 그리고 ≤ 1e-7 m²K/W 유지 | 초과 → 원인(계면층 성장) STEM 1회 후 판정 |
| L3-3 TC | JESD22-A104 −55/125 °C 1000 cycles (중간 250/500 점검) | C-SAM 박리 면적, TDTR | 박리 증가 ≤ 1 % 면적, R'' 변화 ≤ 20 % | 초과 → CTE 불일치 가설 확인(FEM 응력) 후 NO-GO 또는 regime 한정 |
| L3-4 결합에너지 유지 | 각 시험 후 파괴 시편 (DCB, 건조 N₂) | γ | 초기 대비 ≥ 80 % | < 60 % → NO-GO |
| L3-5 전기 (가능 시) | AlN MIM 커패시터 | 누설전류, 파괴전계 | 시험 전후 누설 증가 ≤ 1 decade | 초과 → 전기적 사용 조건 제외 |

### 3C.3 표본 설계
- 조건당 AlN 5쌍 + SiO₂ 대조 5쌍 (동일 lot, paired). Plan B 발동 시 cap 5쌍 추가.
- 비열등성 판정: 지표 차이(AlN − SiO₂)의 90 % 신뢰구간 상한 ≤ 사전 허용 마진 (R'' 변화: +10 %p, 박리 면적: +1 %p, γ 유지율: −10 %p) [ASSUMED 마진, 지금 동결].
- 순서: L3-0 → L3-1 → (L3-2 ∥ L3-3) → L3-4. uHAST가 가장 유력한 kill이므로 먼저.

### 3C.4 #8 결론 분기 (모두 출판 가능한 결과로 사전 정의)
| 결과 | #8 결론 문장 형식 |
|---|---|
| 전부 GO | "스크리닝 수준에서 SiO₂ 대비 비열등, Ea = X eV 기반 수명 추정" |
| uHAST만 실패 | "건조/밀봉 조건 한정 적용 가능, edge seal 요구 조건 정량화" |
| HTS/TC 실패 | "열화 메커니즘 규명(계면층 성장/CTE) 및 적용 불가 경계" (NO-GO 논문) |

- 금지 표현: "JEDEC qualification 통과", "신뢰성 확보". 허용: "JEDEC 조건에 준한 screening".

## 3. G* TDTR 게이트 (S0 결과 반영 제안 — **데이터 취득 전이므로 변경 허용 구간**)

| 항목 | 기존 | 제안 | 사유 |
|---|---|---|---|
| 판정 지표 | R_bond 정밀 추출 | R''_AlN-layer(계면 포함) 상한 ≤ 1e-7 m²K/W 입증 | S0에서 AlN 측 저항은 SiO₂ 대비 이미 1/20 수준 → 상한 입증으로 충분 |
| UNID 처리 | 교정 1회 후 상한 보고 | 상한 ≤ 1e-7이면 GO로 간주 | RT-1 식별불가 리스크 완화 |
| k 하한 | 미정 | k_cross ≥ 20 W/mK @ t≈1 μm | ΔR 손실 ≤ 10 % 조건 (계산: k_floor ≈ 18.5 W/mK, TBR 합 2e-8 가정) |

- [ ] 연구책임자 승인 후 동결: `<commit hash>`

---


## 4.1 S4.1 — AlN bulk DFT 벤치마크 (기준 동결, 계산 전)

### 4.1.1 목적과 원칙
- bulk wurtzite AlN의 조화·비조화 IFC와 κ_bulk를 **실험값에 맞추지 않고** 독립 계산해 이후 MLIP·MC·FEM의 기준으로 쓴다 (RT-5).
- 모든 수치는 QE/phono3py 출력에서 파싱한다. 워크플로우: `s41_workflow.py` sha256 `bd37ad38663e01ffc725cf9b1c306db62e8137d84c95bb3bd4edfcc56681ba11`

### 4.1.2 계산 설정 (동결)
| 항목 | 값 |
|---|---|
| 코드 | QE 7.2 (연구자 소스 빌드), phono3py ≥ 4.x |
| 범함수 / PP | PBEsol / PseudoDojo NC SR v0.4 standard (`nc-sr-04_pbesol_standard_upf.tgz`), Al.upf sha256 `acf6bb98e0ccdd937c0b48d8339848b07d5cffaec802e4d301b93d2eaad23b90`, N.upf sha256 `9d173b6ca975d23fd3e9db8b00e894541d377ddd78d8675c0073fea98c192a1f` |
| 초기 구조 | a = 3.112 Å, c = 4.982 Å, u = 0.382 **[LIT-verify: 인용 문헌 확정 필요]** |
| FC3 | 3×3×2 (72 atoms), cutoff-pair 4.0 Å = **7.56 bohr** → 466 변위; 수렴 확인 5.0 Å = 9.45 bohr → 790 변위 |
| FC2 | 4×4×3 (192 atoms), 6 변위 |
| NAC | ph.x (epsil) → `phonopy-qe-born` → BORN |
| κ | RTA + isotope, mesh 16×16×10 → 20×20×12 → 24×24×14; 수렴 mesh에서 LBTE 1회 |

### 4.1.3 동결 기준
| 단계 | 기준 |
|---|---|
| ecut / k 수렴 (N 원자 z 변위 구조) | 최고 설정 대비 ΔE ≤ 0.5 meV/atom, ΔF ≤ 5×10⁻⁵ Ry/bohr, ΔP ≤ 0.5 kbar를 처음 만족하는 값 |
| 격자상수 (vc-relax 2회) | a, c 모두 실험 대비 ±1 % |
| Γ 진동수 | A1(TO) 613.4, E2(high) 658.1, E1(TO) 670.1, A1(LO) 889.3 cm⁻¹ 대비 ±3 % [LIT: MOCVD 후막 AlN Raman, Xu et al., arXiv:1911.01595 — THz 값을 cm⁻¹로 환산] |
| cutoff 수렴 | 4.0 Å vs 5.0 Å에서 κ_avg 변화 ≤ 5 % → 4.0 Å 채택, 아니면 5.0 Å |
| mesh 수렴 | 연속 mesh 간 κ_avg 변화 ≤ 3 % |
| **벤치마크** | κ_avg = (2κ_xx + κ_zz)/3 @300 K (isotope 포함)이 316 W/mK의 ±15 % (269–363) [LIT: PVT 단결정 최대 316 W/mK, Inyushkin et al., J. Appl. Phys. 127, 205109 (2020), doi:10.1063/5.0008919 — Crossref 검증] |
| 참고 (판정 아님) | 결함 포함 결정 3ω 측정 237 ± 6 W/mK (OSTI 1604926) — intrinsic DFT의 목표값 아님 |
| Phonon Olympics (JAP 2025) | 권장 설정과의 차이 표를 작성 **[연구자가 원문 확인 후 기입 — Claude는 원문 미확인]** |

### 4.1.4 불일치 시 진단 (G-5: 최대 2회)
1. BORN/NAC 적용 여부 (kappa 로그) 2. FC2 supercell 5×5×3 확대 3. 4-phonon 산란 미포함을 한계로 명시
- **금지**: κ를 실험에 맞추기 위한 파라미터 조정. 2회 진단 후에도 벗어나면 불일치를 그대로 보고하고 S4.2 이후는 "DFT 기준값" 대신 실험 κ_bulk를 앵커로 사용함을 명시.

### 4.1.5 환경 주의 (검증됨)
- phono3py QE 모드의 `--cutoff-pair` 단위는 **bohr**: 4.0 입력 시 98 변위(= 2.1 Å, 최근접만), 7.56 → 466, 9.45 → 790 (Claude 환경에서 phono3py 4.5.0으로 확인)
- Ubuntu 24.04 apt 패키지 QE 6.7은 pw.x 실행 즉시 `__chk_fail` abort (연구자가 과거 겪은 glibc 문제와 동일) → 소스 빌드 7.2 사용
- 계산 비용: 72-atom SCF 1회 시간을 `fc3run --limit 1`로 측정 후 × 472 (cutoff 수렴 확인 시 × 796)로 산정해 기록

### 4.1.6 RESULTS_INDEX 예약 ID
S4-001 수렴 ecut/k, S4-002 격자상수, S4-003 Γ 진동수, S4-004 κ(RTA, isotope, 수렴 mesh), S4-005 κ(LBTE), S4-006 cutoff 수렴 차이


## 4.2 S4.2 — 본딩 계면 DFT (기준 동결, 계산 전)

### 4.2.1 핵심 가설 (신규 red-team 항목 RT-12)
- 같은 레시피로 증착한 두 AlN(0002) 막을 **마주 보게(face-to-face) 접합하면 계면은 반드시 극성 반전 경계**가 된다 (Al-polar 막 → head-to-head, N-polar 막 → tail-to-tail).
- AlN 세라믹의 평면 반전 도메인 경계(IDB)는 산소로 배위된 팔면체 Al 기저면 층 모델로 기술되고 [LIT: Westwood et al., J. Mater. Res. 10 (1995), Harris 모델 정밀화], EELS로 **산소 1.5 monolayer**가 측정됨 [LIT: Bruley/Westwood, MRS Proc.]. 전하 보상(Pauling 규칙) 때문에 산소량이 이 값으로 제한된다는 해석이 있음 [LIT: Sci. Rep. 2018, polarity conversion by O].
- → "AlN–AlN 본딩 계면"의 물리적 후보는 (i) IDB형 얇은 Al–O 층, (ii) 비정질 AlOx 층이며, 산소 없는 이상 계면은 기준(reference)일 뿐 물리적 후보가 아니다.

### 4.2.2 후보 구조 (전자 계수법으로 선정 — **Claude 유도, DFT 밴드갭으로 검증 대상**)
- 2×2 HH 계면당: 양쪽 Al 면의 dangling bond가 6 e 공급, 계면 Al 1개당 3 e, O 1개당 2 e 필요 → n_O = 3 + 1.5·n_Al
| ID | 계면층 | O 피복 | 원자 수 (면당 8 / 12 bilayer) | 상태 |
|---|---|---|---|---|
| HH-A | O 3개 (Al 없음) | 0.75 ML | 139 / 203 | 생성됨 |
| HH-B | O 6 + Al 2 | **1.5 ML** (EELS 문헌값과 일치) | 144 / 208 | 생성됨 |
| HH-C | O 9 + Al 4 | 2.25 ML | 4×4 셀 필요 | 보류 |
| TT-x | 양이온 계면층 | — | — | L1 극성 측정에서 N-polar 확인 시 생성 |
| AM-1/2/3 | 비정질 AlOx 1/2/3 nm | — | S4.3 MLIP melt-quench 후 | S4.3 이후 |
- 생성기 `build_structures.py` sha256 `ab9023986f592860a6b113a6716f79bc096cb1fdf6d761c0a452739383e4c331`, 구조 `interfaces_HH.extxyz` sha256 `0d99e107589cd7f245524aeff49cb49aa830cf091a2ccca8f637b221c78e1af7` — **모두 비이완 초기 추정**, 최소 비-H 원자간 거리 1.79 Å, 외곽면 N/N
- 외곽 N 면: pseudo-H (Z = 0.75) 부동태화 → **ld1.x로 생성 필요** (PseudoDojo에 없음). O.upf sha256 `d91e3e76b237bb20c22fd32187fa3ed08250014cd11e74d0e13f305ccd73996f`

### 4.2.3 동결 기준
| 항목 | 기준 |
|---|---|
| 설정 | S4.1과 동일 (PBEsol, PseudoDojo). O 포함 계로 ecut 수렴 재확인 (S4.1 기준 동일) |
| 표면 검증 | 진공 영역 정전 퍼텐셜 평탄 (구조 대칭이므로 dipole 보정 없이 차이 < 0.05 eV), 외곽면 gap state 없음 |
| 두께 수렴 | 면당 8 vs 12 bilayer: W_sep 변화 ≤ 0.05 J/m², 계면층 두께 변화 ≤ 0.05 Å → 8 채택 |
| 전자구조 | 층분해 PDOS에서 계면 gap ≥ 동일 설정 bulk gap의 50 %. 미달 → "불안정 후보"로 제외 |
| 출력 | W_sep, 계면층 두께 d_int, O 면밀도, 계면 IFC(S4.4용) |
| **실험 대조 (선택 규칙)** | L2-3 STEM-EELS의 d_int ± 0.3 nm 및 O 면밀도 ± 0.5 ML에 맞는 후보만 S4.4 TBR 계산에 사용. **TBR 값으로 후보를 고르지 않는다** (RT-5) |
| 결합에너지 | W_sep는 실측 결합에너지와 **순위만** 비교 |
| 제한 | DFT 완전 이완 후보 최대 6개 |

### 4.2.4 L1 추가 요구 (지금 등록)
- 막 극성(Al-polar / N-polar / 혼합) 측정: KOH 습식 식각 또는 STEM ABF/iDPC. 혼합 극성이면 계면이 HH/TT 패치 구조가 되므로 S4.2 후보 체계를 재검토.

## 4.3 S4.3 — MLIP 학습·검증 (기준 동결, 학습 전)

### 4.3.1 데이터 계열 (라벨은 모두 DFT, S4.1과 동일 설정)
| 계열 | 내용 | 예상 프레임 |
|---|---|---|
| D1 | S4.1 phono3py 변위 supercell (추가 비용 없음) | ~472 |
| D2 | 3×3×2 변형 격자 ±3 % (`bulk_strain.extxyz`, 15개 생성됨) | 15 |
| D3 | 4×4×3 점결함 O_N, V_Al, V_Al+3O_N (`defects.extxyz`) + 이완·AIMD 샘플 | ~60 |
| D4 | bulk AIMD 300/600/900/1200 K | ~80 |
| D5 | S4.2 계면 이완 궤적 + AIMD 300/600 K | ~300 |
| D6 | 비정질 AlOx/AlON melt-quench (밀도 범위 [ASSUMED]) | ~200 |
| 합계 | | ~1,100–1,300 |

### 4.3.2 절차
- 모델: 등변(equivariant) MLIP (MACE 등). 버전·하이퍼파라미터를 학습 전 기록. foundation 모델 미세조정 허용, 단 판정은 아래 held-out 기준으로만.
- Active learning: 4-모델 committee, 힘 표준편차 0.10–1.0 eV/Å 프레임을 DFT 라벨링. **최대 5라운드**, 1 ns MD에서 초과 프레임 < 2 %면 종료.
- **Held-out 계열 (지금 고정, 학습에 절대 포함 금지)**: HH-B 12 bilayer 계, AIMD 1200 K, V_Al+3O_N
- 매니페스트: `dataset_manifest_schema.json` sha256 `6e540e193ec94f9a9acaeb95353d0a94a3bf1f8dfc4bf214e9a1b2a327652a4b` — pw.out sha256 없는 프레임은 폐기

### 4.3.3 동결 합격 기준 (held-out 기준)
| 항목 | 기준 |
|---|---|
| 에너지 RMSE | ≤ 3 meV/atom |
| 힘 RMSE | bulk·결함 ≤ 50 meV/Å, 계면·비정질 ≤ 80 meV/Å |
| 포논 | DFT FC2 대비 진동수 RMS 오차 ≤ 0.3 THz |
| κ_bulk | MLIP 힘으로 동일 supercell·mesh phono3py → **S4.1 DFT κ 대비 ±10 %** (실험값이 아닌 DFT가 기준) |
| 안정성 | 계면 모델 900 K NVT 1 ns에서 계면층 밖 결합 파괴 없음 (배위수 분석) |
| 계면 순위 | S4.2 후보의 W_sep 순위가 DFT와 동일 |

### 4.3.4 Kill
- 5라운드 후 계면·비정질 기준 불합격 → MLIP는 bulk·결함에만 사용, 계면 TBR은 DFT 조화 IFC 기반 AGF로 축소 (비조화 효과는 한계로 명시)


## 4.4 S4.4 — 본딩 계면 TBR (기준 동결, 계산 전)

### 4.4.1 TBR 예산 (계산 완료, `s44_tbr_budget.py` sha256 `fc99be6622acccba29e22efc73ecb17f7cc522773568c5696e39f950d434c20f`, 결과 sha256 `b62a05053f7f165f86771b09afcf14e2b585b878b99b1227f1d4b38d967e4359`)
- 동결된 S0 v0.4 모델(HB-era 16-Hi)에서 R_int만 고정해 ΔTj P50 유지율 계산:
| R_int [m²K/W] | 1e-9 | 1e-8 | 3e-8 | 1e-7 | 2e-7 | 5e-7 | 1e-6 |
|---|---|---|---|---|---|---|---|
| ΔTj P50 [K] | 2.78 | 2.72 | 2.61 | 2.23 | 1.74 | 0.61 | −0.69 |
| 유지율 | 100 % | 98 % | 94 % | 80 % | 63 % | 22 % | 역전 |
- 비정질 AlOx 계면층 추정 R_int (k = 1.5 W/mK, 경계 2×2e-9 [ASSUMED]): 1 nm → 4.7e-9, 3 nm → 6.0e-9, 10 nm → 1.1e-8 → **현실적 계면층은 이득의 2 % 미만만 잠식**
- G* 기준(R'' ≤ 1e-7)은 이득 80 % 유지에 해당 — 기준 정합성 확인
- **결론: 계면 TBR은 적용 가능성 판정(go/no-go)을 좌우하지 않는다.** 판정을 바꿀 수 있는 계면 요인은 (a) 미접합·void, (b) L3 가수분해로 성장한 수산화물층(k ≈ 1 W/mK로 가정 시 약 100 nm에서 1e-7 도달)뿐 → S4.4의 판정용 역할은 L3 이후 **열화 계면** 해석으로 이동
- S4.4의 주 가치는 논문(#6)의 물리: 극성 반전 계면(RT-12)의 phonon 투과

### 4.4.2 방법
| 방법 | 대상 | 특성 |
|---|---|---|
| AGF | HH-A, HH-B (+ 선택된 비정질 모델) | DFT 또는 MLIP 조화 IFC, 탄성 산란, 양자 점유 |
| NEMD | 동일 | S4.3 MLIP, 비조화·비탄성 포함, 고전 점유 |
| 비교 | NEMD − AGF | 비탄성 기여 추정 (고전 점유 한계 명시) |

### 4.4.3 동결 기준
- NEMD: 길이 3수준 이상 → 1/L 외삽, 정상상태 판정(열유속 5 % 이내 안정), 독립 seed 5개로 불확도
- AGF: 계면 양쪽 lead 두께 수렴(투과 스펙트럼 변화 ≤ 2 %)
- 내부 일관성: AGF와 NEMD의 후보 간 **순위 일치**, 절대값은 2배 이내면 "일치"로 보고
- 실험 대조: G* TDTR은 상한만 제공하므로 계산 TBR과 **상한 비교만** 수행 (정밀 일치 주장 금지)
- Time box 2개월. S4.3 계면 기준 불합격 시 AGF만 수행

## 4.5 S4.5 — Nano-κ 박막 κ 블라인드 예측 (기준 동결, 계산 전)

### 4.5.1 도구
- Nano-κ: 제일원리 phonon 데이터로 phonon BTE를 Monte Carlo로 푸는 Python 코드 [LIT: Silva, Lacroix, Isaiev, Chaput, Comput. Phys. Commun. 294, 108954 (2024), doi:10.1016/j.cpc.2023.108954 — Crossref 검증]. **입력 형식과 phono3py 연동 방식은 매뉴얼로 확인 후 기입** [Claude 미확인]

### 4.5.2 블라인드 프로토콜 (RT-5)
1. 입력은 **독립 측정값만**: 두께 = L1 Round 2 시리즈 (0.25/0.5/0.8 μm), 기둥형 grain 직경 분포 = TEM plan-view, 산소 함량 = XPS/SIMS, phonon 특성 = S4.1
2. 경계 specularity p = 0 (완전 확산)을 **기본값으로 고정**. 산소 산란은 질량 분산 모델(과소평가 가능성 명시)
3. 예측값 k_cross(t)와 불확도(MC 통계 + 입력 분포 전파)를 JSON으로 저장 → sha256과 git commit 시각을 RESULTS_INDEX에 기록 → **그 다음에** TDTR 두께 시리즈 측정
4. 판정: 3개 두께 중 2개 이상에서 |k_exp − k_MC| / σ_comb ≤ 2, 그리고 두께 의존 기울기가 2배 이내
5. 불합격 시 진단 (G-5, 최대 2회): grain 분포 재측정 → 결함 산란 모델 상향(DFT 기반) → 최후로 p를 **단일 선언 피팅 파라미터**로 사용. 이 경우 모델을 "calibrated"로 표기하고 예측력 주장 철회

## 4.6 S4.6 — Regime map / 디지털트윈 (#12, 기준 동결)

### 4.6.1 구성
- 코어: S0 v0.4 compact 모델 + S0b FEM 보정. 데이터가 들어오는 대로 [ASSUMED] 입력을 측정 분포로 교체 (G* → R''_AlN층, S4.5 → k(t), L1 → t_b 달성 범위)
- 출력: t_b × 전력 × 적층 수 × f_act 축의 ΔTj 지도 + 불확도 띠

### 4.6.2 명칭 규칙 (RT-10)
- 2-die 본딩 test vehicle (Pt heater + RTD) 실측 ΔT가 모델 **사전 예측** 대비 ±15 % 이내 → "digital twin" 명칭 허용
- 미실측 또는 불일치 → "physics-based regime map"으로만 표기

### 4.6.3 선행연구 차별화 (S2 레드오션 점검, 필수 인용)
- HBM 내부 온도 분포에 대한 비-Fourier 열전달 효과 연구가 이미 있음 [LIT: Zhou et al., IEEE Trans. Electron Devices, 2025, doi 10.1109/TED.2025.3628342 — 원문 확인 후 차별점 1줄 작성]

### 4.6.4 시뮬레이션 전체 time box (포트폴리오 보호)
- S4.2–4.6 합계 계산 인력 투입은 실험 L1–L3 진행을 지연시키지 않는 범위로 제한. 실험 게이트(L1 GO) 전에는 S4.1, S4.3 D1–D4, S4.5 예측까지만 수행


## 5. S5 — 논문 작성·검증 파이프라인 (동결)

### 5.1 도구 (`s5_tools.py` sha256 `da81054bd94a4150e64101542594b7a30c095360712bb1577d49388c013ded37`)
| 명령 | 역할 |
|---|---|
| `index` | results_index.csv 필수 필드, EXP/SIM 원시파일 sha256 대조, LIT는 실제 doi:10.xxxx 필수 |
| `lint` | 원고의 모든 숫자는 `\res{ID}` / `\cond{...}` / whitelist 중 하나. frozen이 아닌 ID, **ASSUMED-dominant ID 인용 차단** |
| `render` | `\res{ID}` → 값 ± 불확도 단위로 치환한 빌드본 생성 |
| `doi` | .bib의 DOI를 Crossref로 조회: 존재·제목 유사도 ≥ 0.8·철회 표시 |
| `rules` | PREREG 금지 표현: "JEDEC qualification", "신뢰성 확보", 조건부 "digital twin"(TV_VALIDATED), "predict"(MC_BLIND_PASSED), "AlN–AlN bond"(DINT_LT_2NM) |
| `gate` | 위 전부 + 연구자의 scan_for_synthetic.py + 특허 출원 확인 → 문제 0개일 때만 투고 |

- 기존 provenance.py / RESULTS_INDEX.md와의 관계: results_index.csv를 기계 판독용 원본으로 두고, RESULTS_INDEX.md는 생성물로 취급 (연구자 기존 스크립트 형식에 맞춰 어댑터 1회 작성)
- 시작 인덱스 `results_index.csv`: S0-301, S0-305 (ASSUMED-dominant → 본문 인용 차단 확인), S44-001, LIT-001

### 5.2 파이프라인 자체 검증 (실행 결과)
- 테스트 fixture에서 게이트가 14건 검출: ASSUMED-dominant 인용 2, draft ID 1, 맨숫자 3, 금지 표현 4, DOI 누락, 특허 미확인 등 → **DO NOT SUBMIT** 판정 정상 작동
- **DOI 검증이 실제 오류를 잡음**: 이 대화에서 Claude가 기입한 Nano-κ 서지(CPC 294, **108959**)가 틀렸음. Crossref 조회 결과 해당 DOI는 다른 논문("Bit-twiddling hacks for gamma matrices")이었고, 정답은 **108954, doi:10.1016/j.cpc.2023.108954**. 4.5.1절 정정 완료
- PREREG 문헌 앵커 6건 DOI 검증 통과 (`prereg_refs.bib`): Inyushkin 2020, Silva 2024 (Nano-κ), Zhou 2025, Westwood 1995 Part I, Sci. Rep. 2018, Electronics 2025 리뷰

### 5.3 투고 게이트 (동결)
1. `s5_tools.py gate` 문제 0건
2. 리뷰어 공격표(`reviewer_attack_tables.md`)에서 등급 F 항목이 모두 CLOSED
3. Claim–Evidence Matrix 전 행 채움
4. 특허 출원 완료 (G-6), 그 후 학회 초록 → preprint → 투고 순
5. 적대적 mock review 1회 (다른 모델 또는 동료), 신규 F 항목 발생 시 S3/S4로 1회 복귀 후 claim 축소

### 5.4 공격표에서 새로 드러난 미계획 F 항목
- #12-4: AlN ε_r 증가에 따른 pad 간 capacitance 불이익 — **계획 없음 → 다음 작업으로 등록**
- #6-A-2: TBR Pareto 서사가 S44-001에 의해 약화 → #6 서사 결정 필요 (6-A 유지 / 6-B 전환)


## 4.7 S4.7 (#12-4, RT-8) — 측면 pad-pad 결합 커패시턴스 페널티 (계산 완료)

### 4.7.1 모델과 결과 (`s47_capacitance.py` sha256 `972abca823d51cdcf84ec265ff5bdb30f4e4edad8e33900ebf25c1fdd8bfb32d`, 결과 sha256 `28c59e24c0a0c1200d989c79e939c9aef0b23c3a285b13fff8aada6f1d5b56f9`)
- 모델 [MODEL, 근사]: 인접 pad를 마주보는 평행판으로 근사, C_pp = ε₀·ε_r·w·t_b/g (fringing 무시, 상한 성격)
- **기하 무관 결과**: w = 0.4·pitch 고정 조건에서 비율 C_AlN/C_SiO₂ = ε_r,AlN/ε_r,SiO₂만으로 결정되고 pitch·t_b에 무관 → **2.18–2.31배**
- 절대값 (pitch 6–9 μm, t_b 0.5–1.0 μm): C_SiO₂ = 0.012–0.023 fF/pair, C_AlN = 0.025–0.053 fF/pair — pad 1쌍 기준으로는 작음
- 총 노드 커패시턴스(인접 pad 수 × 배선 기생 포함)와 타이밍 여유는 **설계 데이터 없이는 판정 불가**

### 4.7.2 판정 기준 (조건부 동결 — 설계 마진 입력 대기)
| 항목 | 상태 |
|---|---|
| 비율 자체 | 확정: 2.18–2.31배 (물성비이므로 재계산 불필요) |
| 허용 여부 | **OPEN**: 목표 채널의 RC 지연 예산 또는 crosstalk 허용치가 있어야 kill/go 결정 가능 |
| 임시 기준 | 데이터 없는 동안 #12 규제지도에 "AlN 채택 시 pad 간 결합 커패시턴스 약 2.2–2.3배 증가"를 **정량 caveat로 필수 기재**, 강도 주장 금지 |
| 전기 시험 (L3-5) | AlN MIM 커패시터 실측 ε_r로 위 값 교체 |

### 4.7.3 다음 필요 입력
- 목표 신호 speed/BW, 채널 RC 예산 또는 crosstalk 허용치 (설계팀·논문 목표 스펙 보유 시 제공)
- 없으면 이 항목은 "OPEN, 정량 caveat로만 존속"

## 9. 변경 이력 (Change Log)

| 날짜 | 섹션 | 변경 전 | 변경 후 | 사유 | 데이터 취득 전? |
|---|---|---|---|---|---|
| `<YYYY-MM-DD>` | 3 | TBR 정밀 추출 | 상한 입증 | S0 민감도 결과 | 예 |
| `<YYYY-MM-DD>` | 1.5 → 2.5 | [ASSUMED] 입력 | [LIT] 대체 (기준값 변경 없음) | 문헌 확보 | 예 (시뮬레이션 입력) |
| `<YYYY-MM-DD>` | 1.4 | Model B | FEM 보정 surrogate | S0b-002 불통과 | 예 |
| `<YYYY-MM-DD>` | 2.8 | f_act 0.05–0.40 | 0.05–0.25 | 문헌 상한 확보 | 예 |
| `<YYYY-MM-DD>` | 2.9 | f_up 0.60–0.90, f_base 0.30–0.50 | 0.85–1.00, 0.30–0.65 | 문헌 앵커 확보 | 예 |
| `<YYYY-MM-DD>` | 3B | — | L2 기준·Plan B 신규 등록 | L2 착수 전 | 예 |
| `<YYYY-MM-DD>` | 3C | — | L3 기준·비열등성 마진 신규 등록 | L3 착수 전 | 예 |
| `<YYYY-MM-DD>` | 4.1 | — | S4.1 설정·기준 신규 등록 | 계산 전 | 예 |
| `<YYYY-MM-DD>` | 4.5.1 | Nano-κ CPC 294, 108959 (오류) | 108954, doi:10.1016/j.cpc.2023.108954 | S5 DOI 검증으로 발견한 Claude 인용 오류 | 예 |
| `<YYYY-MM-DD>` | 5 | — | S5 파이프라인·투고 게이트 등록 | 원고 작성 전 | 예 |
| `<YYYY-MM-DD>` | 4.7 | — | capacitance ratio 계산·조건부 기준 등록 | 계산 전 | 예 |
| `<YYYY-MM-DD>` | 4.4–4.6 | — | TBR 예산 계산, 블라인드 프로토콜, 명칭 규칙 등록 | 계산 전 | 예 |
| `<YYYY-MM-DD>` | 4.2–4.3 | — | 계면 후보·MLIP 기준·held-out 계열 등록, L1 극성 측정 추가 | 계산·학습 전 | 예 |
| `<YYYY-MM-DD>` | 3A.2 | \|σ\| ≤ 300 MPa & bow ≤ 50 μm (모순) | \|σ·t\| ≤ 80 N/m + SiO₂ baseline 대비 | 초기 제안 오류 정정 | 예 (L1 데이터 없음) |

---

## 10. RESULTS_INDEX 등록 규칙
- S0-101 ~ S0-104, S0b-001 ~ S0b-004: 출처유형 `SIM`, 입력 상태 `LIT+ASSUMED 혼합`, 해시는 2.3/2.6절 참조
- S0-001 ~ S0-004: 출처유형 `SIM`, 입력 상태 `ASSUMED-dominant`, 원시파일 `s0_results.json` sha256 `b53f116e82747cb8770f96bfb00aaf54468df1a63773f3d5146a5904eb705ee8`
- 후속 분석: `s0_followup.json` sha256 `bc06c0a11a616cf7be6e435f32afa3d542b734a1a3f3802dab98d635acab4b4a`
- **논문 본문 인용 금지**: [ASSUMED] 입력이 [LIT]/[MEASURED]로 교체되기 전까지 S0 수치는 motivation 서술에도 사용하지 않는다.


# SOURCE: research_working_set/algorithm_v0.10_claude_final/AlN_HybridBonding_Algorithm_v0.10/00_core/STATUS.md


# 프로젝트 상태 대시보드 (PREREG.md v0.10 기준)

> 이 문서는 PREREG의 요약·내비게이션이며 그 자체로 기준을 동결하지 않는다. 기준의 원본은 항상 PREREG.md.

## 1. 마스터 플로우차트 (실측 반영)

```
[S0 물질성 게이트] ── ΔTj P50=2.71K(HB-era) ──► CONDITIONAL-GO ✅
[S0b 3D 검증]     ── Model B 오차 최대+37% → FEM 보정 surrogate ──► KEEP ✅
[S1 스크리닝]      ── HBM hard-constraint 표 ──► 후보 확정, margin 최소=응력 ✅
[S2 레드/블루오션]  ── #6 서사 재검토 필요 신호 ──► 🟡 결정 대기 (사용자)
        │
        ├─[L1 증착]──○ 미실행 (DSD 15-run 설계 완료, 장비수준 조정 필요)
        ├─[L2 CMP/본딩]──○ 미실행 (기준 동결, 범위 선언 완료)
        ├─[G* TDTR]──○ 미실행 (블라인드 프로토콜 동결)
        └─[L3 신뢰성]──○ 미실행 (L3-0 kinetics 선행 필수로 순서 변경)
        │
[S4.1 DFT bulk]   ── 워크플로 작성 완료, 실행 미착수 (연구자 QE 7.2 필요) ──► ○
[S4.2 계면 DFT]    ── 초기 구조 생성 완료 (HH-A/B) ──► ○
[S4.3 MLIP]        ── 데이터 계열·held-out 동결 ──► ○
[S4.4 계면 TBR]    ── ✅ 계산 완료: TBR은 go/no-go를 좌우하지 않음 (이득 잠식 <20%, R_int≤1e-7에서)
[S4.5 Nano-κ]      ── 블라인드 프로토콜 동결 ──► ○
[S4.6 regime map]  ── 명칭 규칙·차별화 문헌 등록 ──► ○
[S4.7 capacitance] ── ✅ 계산 완료: 비율 2.18–2.31배 확정, 허용 여부는 🟡 설계마진 대기
        │
[S5 논문 파이프라인] ── ✅ 도구 작성·자체검증·DOI 6건 검증 완료
        │
[투고 게이트] ── 미충족 (F등급 다수 PLANNED, #6 서사 미정, 특허 미출원)
```

## 2. 판정 요약표

| 게이트 | 판정 | 근거 | PREREG §|
|---|---|---|---|
| S0 (물질성) | **CONDITIONAL-GO** | ΔTj P50 2.71 K (HB-era 16-Hi) | 2.9 |
| S0b (3D 검증) | **KEEP** | FEM 보정 후 모델 유효 | 2.4 |
| S4.4 (계면 TBR) | **비결정적 요인으로 강등** | R_int=1e-7에서도 이득 80% 유지 | 4.4.1 |
| S4.7 (capacitance) | **비율 확정, 판정 OPEN** | 2.18–2.31배, 설계 마진 없음 | 4.7.2 |
| S5 (파이프라인) | **동작 확인** | fixture 14건 검출, DOI 오류 1건 자체 발견·정정 | 5.2 |

## 3. 미해결 항목 (사용자 결정/입력 필요)

| # | 항목 | 필요한 것 | 영향 |
|---|---|---|---|
| 1 | #6 서사 (6-A TBR축 유지 vs 6-B 극성계면축 전환) | 연구자 결정 | 논문 포트폴리오, S4.2 우선순위 |
| 2 | #12-4 capacitance 허용 기준 | 목표 채널 RC 예산 / crosstalk 허용치 | S4.6 regime map 완결성 |
| 3 | 3 K 임계값(S0 GO 기준)의 공학적 근거 | DRAM retention/refresh 마진 문헌 | S0 판정 정당화 (값 자체는 불변) |
| 4 | Phonon Olympics(JAP 2025) 권장 설정 비교 | 원문 확인 (Claude 미확인) | S4.1 벤치마크 표 |
| 5 | L1 장비 실제 사양 (RF power, 압력, 온도, bias 범위) | 장비 스펙 | DSD 인자 수준 확정 |
| 6 | 실험 격자상수 인용문헌 확정 | 문헌 확인 | S4.1 설정 인용 |

## 4. 지금까지 나온 자기 정정 (신뢰성 기록용)

| 항목 | 문제 | 정정 |
|---|---|---|
| S1 초기 응력 기준 | \|σ\|≤300MPa와 bow≤50μm이 0.5μm 막에서 물리적으로 모순 | 막 힘(film force) 기준으로 대체 (3A.2) |
| Nano-κ 서지 | DOI 108959 오기입 (실제로는 다른 논문) | S5 doi 검증으로 발견, 108954로 정정 (4.5.1) |
| Model B (Cu pad 병렬경로) | 검증 없이 사용 시 AlN 전 구간 오차 최대 +37% | S0b FEM 보정 surrogate로 교체 |

## 5. 다음 권장 행동 (택1, 서로 배타적이지 않음)

- **(a) 계산 계속**: S4.2 밴드갭 검증용 설정 확정, 또는 RESULTS_INDEX에 남은 예약 ID 채우기
- **(b) 실행 전환**: `s41_workflow.py conv` 결과를 가져와 S4.1 실제 판정 시작
- **(c) 결정 사항 해소**: 위 3절의 1·2번 답변 제공
- **(d) 문서 정리**: PREREG.md 번호 체계 정리(현재 §3, §4.7이 뒤에 삽입되어 순서 어긋남) — 내용은 불변, 목차만 재배열



# SOURCE: research_working_set/reports/AlN_Additional_Paper_Opportunities.md


# Additional AlN Thin-Film Paper Opportunities Beyond HBM Hybrid Bonding (first pass, 2026-09-24)

Scope: broadened literature check for whether AlN thin films, used to solve device heat
dissipation problems, offer additional red/blue-ocean paper opportunities beyond the locked
#6/#8/#12 HBM hybrid-bonding program. This is a first pass via WebSearch; each candidate below
still needs the same Liner/Gemini/Perplexity kill-search discipline used for the HBM program
before being trusted as genuinely blue.

## Candidate 1: BSPDN nano-TSV AlN vs oxide dielectric (status: RED, already directly contested)

A conference paper already exists doing almost exactly this comparison: "Thermal Management of
Nano-TSVs in Advanced BS-PDN: A Comparative Study of AlN and Oxide Dielectrics for Heat
Dissipation Efficiency" (cited by a ResearchGate-indexed package-level BSPDN thermal analysis
paper). Status: RED for a direct "AlN vs oxide in BSPDN nano-TSV" claim - this exact comparison
has already been published. [UNVERIFIED: full bibliographic details not yet confirmed; DOI not
found in this pass, needs Liner/Google Scholar follow-up before citing or ruling out.]

Supporting industry signal (real, found this pass): semiengineering.com (2026-02-23) reports that
companies are actively evaluating AlN and other films for permanent fusion bonding in backside
power delivery contexts, explicitly because "the dielectric used for bonding adds to the thermal
resistance for evacuating heat, so the material needs to be carefully chosen." This is a second,
independent industry signal (after the Micron 2026 IITC finding) that AlN-as-bonding-dielectric is
a live industry question, this time in the BSPDN context rather than HBM.

Where the possible remaining gap is: not "AlN vs oxide in BSPDN" (already contested), but
specifically whether AlN's known narrow-regime behavior (found in this program's own S0/S0b
calculations - benefit concentrated in low-metal-coverage, thick-dielectric regions) also holds
for BSPDN nano-TSV geometry, which has very different metal density and TSV aspect ratios than HBM
Cu-Cu hybrid bonding pads. This would reuse the #12 regime-map methodology on a different geometry
- a plausible extension paper, not a from-scratch topic.

## Candidate 2: AlN-mediated GaN/diamond topside thermal integration (status: potentially BLUE, needs deeper check)

Found: "Low thermal boundary resistance and reduced junction temperature in GaN HEMTs via
AlN-mediated top-side diamond integration" - demonstrates a GaN/AlN/diamond heterostructure,
using AlN as a bonding/interlayer material between GaN and a diamond heat spreader (rather than as
the primary heat-spreading dielectric itself). [Author/journal/DOI not yet confirmed in this pass
- flag as UNVERIFIED until confirmed via Liner or direct fetch.]

Why this might be genuinely different from the locked #6/#8/#12 program: this uses AlN's role as
a low-TBR bonding interlayer between two different high-k/high-cost materials (GaN and diamond),
not as a bulk dielectric replacement. This is conceptually adjacent to but structurally distinct
from Cu/AlN/Cu hybrid bonding - it is GaN/AlN/diamond, no copper hybrid-bonding pads involved. If
the existing paper is a single demonstration without a systematic bonding-strength/TBR/reliability
Pareto study (the same gap structure already identified for #6 in the HBM context), a parallel
"AlN-mediated bonding interlayer for wide-bandgap device thermal management: bonding energy/TBR
Pareto front, generalized across GaN/diamond and other heterostructure pairs" paper could reuse
almost the entire #6 methodology (TDTR protocol, TEM/EELS interface characterization, blind MD/MC
prediction discipline) on a different device class. This would count as one of the ">=40%
gate-independent portfolio papers" Claude's red-team pass (RT-4) recommended building.

## Candidate 3: AlN passivation in AlGaN/GaN HEMTs (status: RED, mature field, not a new paper)

Multiple existing papers (2018 Mater. Des., 2026 MDPI Micromachines) already study AlN passivation
in AlGaN/GaN HEMTs for RF thermal performance, including detailed simulation studies of air-gap
gate + AlN passivation combinations. This is a mature, well-populated field. Do not pursue as a
standalone paper; useful only as background citation for #8's dielectric-reliability literature
review (AlN passivation reliability data may be reusable as supporting evidence, similar to how
PMUT/FBAR literature was used earlier in this program).

## Recommendation

- Candidate 1 (BSPDN nano-TSV): treat as RED for the core comparison, but flag the regime-map
  extension (reusing #12 methodology on BSPDN geometry) as a possible low-effort portfolio paper
  once the primary #12 work is validated. Do not start new experiments for this; it is a
  computational-only extension of already-planned work.
- Candidate 2 (AlN-mediated GaN/diamond bonding): the most promising genuinely new direction found
  this pass. Recommend a dedicated Liner + Gemini kill-search pass (same discipline as the HBM
  program) before deciding whether to add this as a formal 4th or 5th paper in the portfolio.
- Candidate 3 (GaN HEMT AlN passivation): confirmed red ocean, use only as citation background.

## Explicit non-recommendation

Do not treat any of these as confirmed blue ocean yet. This document is a first-pass WebSearch scan,
not a verified literature review. Before committing research time, run the same process already
used for #6/#8/#12: Liner paper-level verification, Gemini/Perplexity kill-search, and an honest
"why is this empty" test (RT-11 from the Claude red-team pass) to rule out physical impossibility
or undisclosed industry/patent activity.
