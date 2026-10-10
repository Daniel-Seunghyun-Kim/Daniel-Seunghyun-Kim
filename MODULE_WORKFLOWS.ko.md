# 다섯 모듈의 로컬 시작 워크플로

모든 명령은 이 저장소의 state 폴더에 DRAFT 작업만 만듭니다. 등록된 연구 폴더, 상용 프로그램, 원고 원본에는 쓰지 않습니다.

## 1. Literature Agent

목표는 논문 내용의 자동 결론이 아니라, 근거가 필요한 질문을 명확히 하고 파일 provenance를 확보하는 것입니다.

    & 'C:\Program Files\nodejs\npm.cmd' run idea -- --title "AlN literature gap" --topic "순수 AlN 관련 주장에 필요한 직접 근거와 반증 문헌" --project paper_library
    & 'C:\Program Files\nodejs\npm.cmd' run prepare -- --title "AlN source map" --kind literature --project paper_library --tool literature_workspace --action "PDF manifest, citation map, direct evidence와 inference 분리"

## 2. Simulation Agent

입력 초안, 파라미터 차이, validation checklist를 만들지만 실행 권한은 가져가지 않습니다.

    & 'C:\Program Files\nodejs\npm.cmd' run prepare -- --title "IGZO TCAD draft" --kind simulation --project igzo_tcad --tool silvaco_deckbuild --action "deck 초안, units, path, expected output 검토"
    & 'C:\Program Files\nodejs\npm.cmd' run prepare -- --title "COMSOL model handoff" --kind simulation --project aln_workspace --tool comsol_batch --action "assumptions, mesh/BC checklist, human-approved batch handoff"
    & 'C:\Program Files\nodejs\npm.cmd' run prepare -- --title "VASP manual handoff" --kind simulation --project aln_simulation --tool vasp --action "input validation과 수동 실행 package"

## 3. Experiment Agent

실험 데이터의 결측값을 채우거나 자동 PASS하지 않습니다. 계획, 체크리스트, provenance를 정리합니다.

    & 'C:\Program Files\nodejs\npm.cmd' run prepare -- --title "RF sputtering DOE" --kind experiment --project aln_hub --tool experiment_review --action "변수표, 대조군, 장비 조건 기록, 원시 데이터 manifest"

## 4. Writing Agent

원고 원본을 수정하지 않고, review 가능한 초안과 claims-to-evidence 표를 만듭니다.

    & 'C:\Program Files\nodejs\npm.cmd' run prepare -- --title "Discussion draft" --kind writing --project aln_workspace --tool writing_staging --action "주장-근거 표, figure caption, reviewer response 초안"

## 5. Project Manager

프로젝트 진행률은 결과가 아닌 결정과 실패 원인을 포함해 기록합니다.

    & 'C:\Program Files\nodejs\npm.cmd' run prepare -- --title "Weekly research review" --kind project --project aln_hub --tool project_log --action "다음 작업, 차단 요인, 실패 원인, 승인 지점 기록"

## 결과를 모델과 비교할 때

1. 먼저 local_ollama 또는 사용자가 선택한 수동 모델 경로를 정합니다.
2. 각 모델의 결과는 서로 덮어쓰지 않는 별도 draft로 저장합니다.
3. 모델 간 불일치는 자동 다수결 대신, 근거 확인이 필요한 질문으로 작업 패킷에 기록합니다.
4. 소비자 구독 한도 오류는 자동 failover가 아니라 NEEDS_MODEL_SELECTION으로 처리합니다.
