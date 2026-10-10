# 일상 운영 흐름

## 1. 아이디어를 연구 패킷으로 바꾸기

    & 'C:\Program Files\nodejs\npm.cmd' run idea -- --title "IGZO 열처리 민감도" --topic "공정 조건과 이동도 변화의 검증 가능한 연결" --project igzo_tcad

생성된 패킷은 결과를 주장하지 않습니다. 관련 주제, 필요한 근거, 변수, 다음 검증을 분리하여 기록합니다.

## 2. 시뮬레이션을 준비만 하기

    & 'C:\Program Files\nodejs\npm.cmd' run prepare -- --title "VASP surface energy input package" --kind simulation --project aln_simulation --tool vasp --action "INCAR/KPOINTS/POSCAR 검증 목록 및 수동 실행 handoff"

이 명령은 DRAFT 작업과 approval.json만 생성합니다. VASP 실행은 하지 않습니다.

## 3. 연구 파일을 안전하게 참조하기

    & 'C:\Program Files\nodejs\npm.cmd' run manifest -- --project paper_library --path "subfolder\paper.pdf"

출력에는 경로, 크기, 수정시각, 제한 크기 이하의 SHA-256만 포함됩니다. 파일 내용은 읽어 모델에 주지 않습니다.

## 4. 로컬 모델은 명시적으로만 사용하기

    & 'C:\Program Files\nodejs\npm.cmd' run ollama:list

Ollama가 실행 중이고 설치된 모델이 있는 경우에만 모델 이름을 확인합니다. 생성 요청은 후속 단계에서 모델 이름을 명시해 호출하도록 설계할 수 있으며, API 키나 외부 전송은 포함하지 않습니다.

## 상태 의미

- DRAFT: 요청 또는 입력 초안. 외부 프로그램을 실행하지 않은 상태입니다.
- NEEDS_APPROVAL: 사람이 명령·파라미터·출력 위치를 검토해야 합니다.
- MANUAL_EXECUTION_ONLY: 사용자가 직접 실행합니다. VASP가 여기에 해당합니다.
- RESULT_MANIFEST_ONLY: 결과 파일의 provenance만 등록됐으며, 물리·논문급 QA는 아직 아닙니다.
