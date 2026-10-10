# Local Semiconductor Research OS

이 프로젝트는 여러 AI를 무작정 연결하는 봇이 아니라, 연구 질문·근거·시뮬레이션·실험·원고를 추적하는 로컬 제어 평면입니다.

현재 구현은 다음을 보장합니다.

- 기존 연구 폴더와 상용 프로그램을 이동·수정하지 않습니다.
- 외부 연구 루트는 읽기 전용으로만 등록합니다.
- VASP는 manual_execution_only입니다. 입력 패키지 작성·검증까지만 지원하고 실행하지 않습니다.
- Silvaco와 COMSOL은 첫 단계에서 prepare/validate용 작업 요청만 기록합니다. 외부 프로그램을 실행하지 않습니다.
- ChatGPT/Claude/Gemini 소비자 구독을 브라우저 세션으로 자동화하지 않습니다. 클라우드 모델 결과는 기본적으로 manual_import이며, 공식 API는 별도 승인과 예산 설정 후에만 켤 수 있습니다.
- MCP 서버는 기본적으로 읽기 전용 상태·라우팅·파일 메타데이터/해시만 제공합니다. 임의 셸 실행·파일 내용 전송·외부 프로그램 실행 기능은 없습니다.

## 바로 사용할 명령

PowerShell에서 이 폴더를 연 뒤 다음을 실행합니다.

    & 'C:\Program Files\nodejs\npm.cmd' run doctor
    & 'C:\Program Files\nodejs\npm.cmd' run status
    & 'C:\Program Files\nodejs\npm.cmd' run route -- --task pdf_analysis
    & 'C:\Program Files\nodejs\npm.cmd' run idea -- --title "AlN 계면 가설" --topic "AlN 박막의 계면과 강유전성 검증" --project aln_hub
    & 'C:\Program Files\nodejs\npm.cmd' run prepare -- --title "IGZO Vg-VD 초안" --kind simulation --project igzo_tcad --tool silvaco_deckbuild --action "deck 초안과 경로 검증"

idea와 prepare는 이 프로젝트의 state 폴더에만 파일을 만들며, 등록된 연구 루트에는 쓰지 않습니다.

## 구성 파일

- config/tool-registry.local.json: 이 컴퓨터에서 확인한 프로그램·연구 폴더 경로입니다. Git에서 제외됩니다.
- config/policy.json: 데이터·실행·모델 연결 정책입니다.
- config/model-profiles.json: 모델별 연결 방식과 수동 전환 정책입니다.
- docs/ARCHITECTURE.ko.md: 다섯 연구 모듈과 데이터 흐름입니다.
- docs/MODULE_WORKFLOWS.ko.md: Literature, Simulation, Experiment, Writing, Project 모듈의 실제 시작 명령입니다.
- docs/IDEA_BACKLOG.ko.md: AlN/IGZO/DFT/실험/원고를 연결하는 확장 아이디어입니다.
- docs/DISCORD_SETUP.ko.md: Discord는 나중에 공식 Bot API로만 연결하는 절차입니다.

## 다음 연결 순서

1. npm run doctor로 경로 상태를 확인합니다.
2. Literature/Simulation/Experiment/Writing/Project 작업을 idea, prepare, manifest로 로컬에 기록합니다.
3. 로컬 Ollama 모델이 필요하면 npm run ollama:list로 설치된 모델만 확인합니다.
4. Discord는 봇 토큰과 허용 사용자 ID를 준비한 뒤, 이 프로젝트의 읽기 전용 MCP/CLI 명령만 호출하도록 붙입니다.
5. 공식 API를 쓰기로 결정한 경우에만 별도 키, 월 예산, 전송 가능한 데이터 등급을 승인합니다.

자세한 운영 규칙은 docs/ARCHITECTURE.ko.md, docs/MODULE_WORKFLOWS.ko.md, docs/OPERATIONS.ko.md를 참조하세요.
