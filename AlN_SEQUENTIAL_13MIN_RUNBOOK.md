# AlN 시뮬레이션용 순차 13분 제어 주기

## 이 문서의 시간 기준

13분은 AlN 물리 시뮬레이션이 끝나는 시간 약속이 아니다. 현재 로컬 상태에서 13분은 다음 작업을 시작해도 되는지를 검증하고, 다음 모델·다음 PC가 그대로 이어갈 수 있는 상태를 남기는 순차 제어 주기다.

특히 QE 기준 SCF가 이미 약 19분, relax가 수 시간 이상이 될 수 있는 상태이므로 QE, DFPT, NEMD, FEM의 완료를 13분 안에 기대하면 안 된다. 이 주기에서는 긴 solver를 시작하기 전의 입력·근거·자원·중단 조건을 결정한다.

## 현재 확인된 두 AlN 가지

이 둘은 같은 run ID로 병합하거나 한쪽의 결과를 다른 쪽의 직접 근거로 쓰면 안 된다.

| 가지 | 현재 기준 경로 | 현재 상태 | 13분 주기의 역할 |
|---|---|---|---|
| T: texture-to-thermal | D:\AlN_Research_Hub\04_SIMULATION_RESULTS\EXPERIMENT_VALIDATED\20260717_evidence_gated_aln_v1 | XRD screening과 orientation geometry만 안전 단계 완료 | XRD–방향성–열수송 가설을 분리하고, 다음 unblocker를 확정 |
| N: Gate 2c QE/MD nitridation | C:\Users\effec\Downloads\AlN_Simulation\GATE2C_CHECKPOINT.md | Hollow/Bridge 입력은 준비, QE relax는 아직 장기 실행 전 | input/pseudopotential/WSL/실행 PC를 확인하고 장기 job 준비만 수행 |

T 가지의 thermal transport gate는 다음을 명시한다.

- XRD는 measured input screening이며 absolute film k를 만들지 않는다.
- harmonic phonon DOS는 pilot이며 더 조밀한 q-grid 검증이 필요하다.
- FC2, FC3, ShengBTE CONTROL이 없어 intrinsic bulk lattice k는 BLOCKED다.
- Cu/AlN interface model, 측정 k/TBC/TBR, heater geometry, solver license가 없어 Cu-line FEM은 BLOCKED다.

따라서 첫 순차 주기에서는 T 가지를 기본으로 선택한다. N 가지는 독립적인 장기 atomistic 캠페인으로만 다룬다.

## 전역 중단 계약

시간 예산과 모델 토큰 예산은 서로 다르다.

- wall-clock budget: 13분
- model budget: 사전 선언한 normalized credit

0분 전에 13분 전체 단계와 중단 기록에 필요한 token credit을 모두 선예약한다. 잔여량을 확인할 수 없거나 예약량보다 작으면 즉시 STOP_TOKEN_BUDGET 또는 BUDGET_UNVERIFIABLE로 끝낸다. 일부 단계만 수행해 예산을 맞추지 않는다.

각 단계가 13분 시간창을 넘기면 TIMEBOX_EXCEEDED로 멈춘다. 완료되지 않은 staging 결과는 연구 결론이나 다음 solver 입력으로 승격하지 않는다.

## T 가지: 기본 순차 13분 주기

| 시간 | 순차 단계 | 수행 내용 | 허용되는 산출물 | 다음 단계 차단 조건 |
|---|---|---|---|---|
| 0:00–0:45 | C0 예산·재개 확인 | token 선예약, state revision, immutable snapshot hash, 이전 stop reason 확인 | PREFLIGHT_OK 또는 stop 상태 | 예산 미확인·부족 |
| 0:45–2:00 | C1 질문 하나 고정 | 이번 주기의 질문을 하나만 선택: XRD texture screening, ideal bulk phonon convergence, interface, 또는 device thermal model | run_id, branch_id, single question | 두 질문 이상을 한 run에 혼합 |
| 2:00–3:30 | C2 입력·근거 gate | raw XRD, source notation, config, 현재 thermal gate, 이전 output freshness를 읽기 전용으로 확인 | input hash 목록, DIRECT_EVIDENCE/INFERENCE/NOT_VERIFIED 분리 | XRD에서 film k를 직접 추정하려는 경우 |
| 3:30–5:30 | C3 실행 가능성 probe | 프로그램 경로, 라이선스, output directory, timeout, stale-output 방지 조건을 비파괴적으로 점검 | SAFE_PROBE_OK, NEEDS_LICENSE, BLOCKED, RECHECK_REQUIRED 중 하나 | 임의 solver 실행, 이전 output 재사용 |
| 5:30–7:30 | C4 최소 screen 또는 준비 | 검증된 경량 Python screening이 있고 입력이 완비된 경우에만 단일 후보를 새 run folder에서 실행한다. 그렇지 않으면 input package와 실행 계획만 남긴다. | SCREENING_ONLY 또는 BLOCKED_INPUT | 절대 k, TBC, 논문급 물성값 주장 |
| 7:30–9:30 | C5 출력·물리 QC | 이번 run의 fresh log, exit status, input hash, 단위, 방향성, 비교 기준을 점검한다. 계산 완료와 물리 검증 완료를 구분한다. | FRESH_OUTPUT 또는 REVIEW_REQUIRED | stale output, 누락 log, 가정이 결과로 섞인 경우 |
| 9:30–11:00 | C6 실현성·PC route | 후보를 NOW, CONFIRM_NEXT, BLOCKED로 분류하고 PC route를 하나만 선택한다. | idea card와 단일 next route | license, geometry, measured k/G가 없는 FEM 자동 시작 |
| 11:00–13:00 | C7 commit·handoff | 상태, 입력 hash, gate, 금지된 주장, 다음 단 하나의 행동을 기록한다. | COMMITTED checkpoint 또는 halt record | 미완료 staging의 공개 |

## T 가지에서의 첫 연구 후보

### 후보 T-01: texture와 열수송의 연결을 분리해 검증하기

질문: Si(100) 위 AlN의 XRD/GI-XRD texture screening 결과가, 방향성 열수송을 다루는 어떤 후속 검증 가지를 우선시해야 하는가?

- DIRECT_EVIDENCE: raw XRD screening, texture index, orientation geometry의 완료 log
- INFERENCE: (0002)/(103) 계열과 두께·grain boundary·interface 조건이 열수송 후보를 달리 만들 수 있다는 연구 가설
- NOT_VERIFIED: film k, k tensor, Cu/AlN TBC, Cu heater temperature rise
- 최소 다음 검증: 측정 thermal metrology 또는 문헌에서 고정한 입력을 가진 sensitivity case
- 차단 조건: XRD peak area를 texture volume fraction 또는 absolute k로 자동 변환하려는 시도

### 후보 T-02: device model은 측정값 도착 후에만 활성화하기

질문: Cu line temperature rise 비교가 가능한 최소 입력 묶음은 무엇인가?

필수 입력은 measured thickness, k_perp 또는 등가 열전달 입력, interface G 또는 TBR/TBC, heater geometry/Joule load, 경계조건, solver license다. 하나라도 없으면 COMSOL/ANSYS microheater는 BLOCKED_MISSING_INPUT으로 남긴다.

현재 thermal gate가 가리키는 우선 unblocker는 PS15-ST5, PS90-ST30, PS90-ST0 300-nm raw scan 및 thermal-metrology 입력 확보이다. 이 자료가 없을 때는 T-01의 screening/geometry 범위를 넘지 않는다.

## N 가지: Gate 2c의 순차 주기

N 가지는 thermal 가지의 보조 증거가 아니다. L21 표면에서 N Hollow/Bridge adsorption과 그 후 potential validation·MD로 이어지는 별도 campaign이다.

13분에는 다음만 수행한다.

1. Gate2c input, L21 source XML, N pseudopotential, WSL target path의 존재·hash·권한을 확인한다.
2. Hollow/Bridge 좌표와 pseudopotential 이름을 checkpoint와 대조한다.
3. 지정 실행 PC를 하나로 고정한다.
4. stdout/stderr, restart, output freshness, 예상 wall time을 가진 장기 QE job package만 준비한다.
5. QE 실행은 별도 승인된 long job으로 큐에 넣는다.

주의: 현재 computation plan은 PC1 중심의 Gate 2c 경로를, simulation campaign config는 DFT/DFPT에 PC3을 제안한다. 이 충돌을 해소하지 않은 상태에서는 job을 launch하지 않는다. 새 run의 state에 PC owner와 WSL/QE executable version을 명시해 먼저 정합시킨다.

## PC별 다음 route

| 환경 | 이 13분 주기에서 허용할 일 | 이후 장기 route |
|---|---|---|
| 문서·저사양 PC | path/hash, XRD screen, geometry, handoff | solver는 시작하지 않음 |
| PC1 | controller, XRD, 경량 Python/FDM proof screen | 작은 bounded sensitivity case |
| PC3 CPU/MPI | QE/DFPT input과 q-grid convergence 계획 검토 | 승인 후 SCF, vc-relax, DFPT |
| PC2 dual GPU | GPU build와 potential·protocol 검증 | 승인 후 독립 LAMMPS/MD queue |
| 상용 FEM PC | license 및 측정 입력의 존재 확인 | 모든 device input이 갖춰진 뒤 작은 2D case |

CPU/GPU 수가 많아도 license, memory, disk, executable version, potential/force-constant QC가 확인되기 전에는 concurrency를 올리지 않는다.

## 13분 후 상태 형식

~~~json
{
  "run_id": "ALN-T-YYYYMMDD-001",
  "branch": "T_TEXTURE_THERMAL",
  "status": "COMMITTED | BLOCKED_MISSING_INPUT | REVIEW_REQUIRED | STOP_TOKEN_BUDGET | TIMEBOX_EXCEEDED",
  "direct_evidence": [],
  "inference": [],
  "not_verified": [],
  "current_gate": "MEASURED_INPUT_SCREENING_ONLY",
  "next_one_action": null,
  "long_job_authorized": false
}
~~~

새 모델은 이 상태와 input hashes, log paths, current gate만 신뢰한다. 대화 내용이나 다른 모델의 아이디어를 직접 물성 근거로 재사용하지 않는다.
