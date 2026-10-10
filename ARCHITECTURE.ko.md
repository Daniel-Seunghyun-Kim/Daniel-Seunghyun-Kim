# 아키텍처와 권한 경계

## 목표

이 시스템은 질문 → 근거 → 시뮬레이션/실험 → 그림 → 원고 → 결정의 연결을 로컬 작업 패킷으로 축적합니다. AI는 초안·검토·검색 보조자이고, 연구 데이터와 최종 판단의 소유자는 사용자입니다.

    Discord (선택적 요청 창구) / Local CLI / MCP client
                        │
                        ▼
          Research OS Router + Job manifest + Audit log
           ├─ Literature   : PDF 목록, 인용 근거, gap 질문
           ├─ Simulation   : 입력 초안, 파라미터 점검, handoff package
           ├─ Experiment   : 원시 데이터 manifest, 체크리스트, 사람 검토
           ├─ Writing      : 초안, caption, reviewer-response staging
           ├─ Project      : 할 일, 결정, 실패 원인, 다음 실험
           └─ Model layer  : local / manual import / approved official API

## 다섯 모듈

| 모듈 | 지금 가능한 로컬 기능 | 자동 실행 금지 경계 |
| --- | --- | --- |
| Literature | PDF/파일 manifest, 증거 노트와 연구 질문 패킷 | 원문을 임의의 클라우드 모델에 전송 |
| Simulation | Silvaco·COMSOL·VASP 입력 초안 요청과 검증 패킷 | 외부 실행, VASP 실행·재시작 |
| Experiment | DOE/체크리스트/원시 데이터 해시 manifest | 결측치 보정, 합성값 생성, 자동 PASS |
| Writing | 초안·caption·reviewer response를 writing/drafts에 저장 | 원고 원본 덮어쓰기, 인용 사실 자동 확정 |
| Project | 아이디어·결정·실패 원인·작업 상태 기록 | 사람 승인 없는 파일 이동/외부 알림 |

## 공통 ID 체계

연구 연결을 쉽게 하려면 다음과 같은 ID를 작업 패킷에 기록합니다.

    RQ-012 (연구 질문)
      └─ EVD-041 (근거)
          └─ SIM-018 (시뮬레이션 입력/결과)
              └─ EXP-007 (시편/측정)
                  └─ FIG-003 (그림)
                      └─ WRT-006 (원고 단락)
                          └─ DEC-010 (결정)

state/jobs/JOB-.../request.json에 이 ID를 넣어 연결합니다. 지금의 CLI는 작업 ID와 audit 로그를 만들고, 후속 UI/MCP/Discord가 같은 정보를 읽도록 설계했습니다.

## 모델 계층

1. local_ollama: 이 PC의 Ollama 서비스와 설치된 모델이 확인됐을 때만 사용합니다. 외부 API 비용이 없습니다.
2. manual_import: ChatGPT/Claude/Gemini 웹·공식 CLI에서 사용자가 결과를 검토하고 작업 패킷으로 가져옵니다.
3. official_api: API 키, 예산 한도, 전송 가능 데이터 등급을 사용자가 승인한 뒤에만 추가합니다.

구독형 웹 세션/쿠키를 Discord 봇이 제어하는 연결은 이 프로젝트의 범위가 아닙니다. 소비자 구독의 남은 사용량은 신뢰성 있게 읽거나 자동 failover의 신호로 쓰지 않습니다.

## 프로그램 상태

config/tool-registry.local.json은 경로 존재와 실행 승인을 분리합니다.

- path_verified_runtime_not_approved: 파일은 있지만, 라이선스·환경·실행 성공을 보증하지 않습니다.
- stage_only / probe_only: 입력 준비·경로 점검까지만 가능합니다.
- gui_manual: GUI는 사용자가 직접 실행합니다.
- manual_execution_only: VASP처럼 실행권한을 사람이 보유합니다.

Doctor의 VISIBLE은 현재 실행 프로세스가 그 경로를 읽을 수 있다는 뜻입니다. NOT_VISIBLE_IN_CURRENT_SANDBOX는 이 개발 환경의 격리 때문에 보이지 않는 경우도 포함하며, 사용자 PC에서 파일이 사라졌다는 단정이 아닙니다. 어느 상태도 물리적 결과의 타당성 또는 논문급 QA를 뜻하지 않습니다.
