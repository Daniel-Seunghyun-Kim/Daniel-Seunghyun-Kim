# Discord 연결: 마지막 단계에 붙이는 안전한 요청 창구

Discord는 연구 데이터나 프로그램 실행 권한을 갖는 곳이 아니라, 로컬 Research OS에 요청을 전달하는 창구입니다.

이 PC의 시작 메뉴 바로가기는 C:\Users\effec\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Discord Inc\Discord.lnk이며, 실제 대상은 C:\Users\effec\AppData\Local\Discord\Update.exe --processStart Discord.exe입니다. 이 정보는 로컬 tool registry에 반영했습니다.

## 연결 전에 필요한 것

- 사용자가 만든 Discord Application/Bot의 토큰
- 허용할 Discord 사용자 ID와 서버/채널 ID
- 공개 엔드포인트를 쓸 경우 서명 검증과 HTTPS
- 로컬 PC가 꺼져 있을 때의 동작 정책

토큰은 .env에만 보관하고 저장소·MCP 응답·작업 로그에 절대 기록하지 않습니다.

## 허용할 명령의 최소 범위

| 명령 | 로컬 동작 |
| --- | --- |
| /idea | 연구 아이디어 패킷 초안 생성 |
| /route | 편집 가능한 모델 우선순위 제시 |
| /status | 로컬 registry/job 상태 읽기 |
| /manifest | 허용된 프로젝트 루트 내부 파일의 메타데이터/해시만 조회 |
| /prepare | 외부 실행 없이 작업 요청/승인 초안 생성 |

## 절대 제공하지 않을 명령

- 임의 셸 명령 또는 임의 파일 경로 실행
- VASP·Silvaco·COMSOL 자동 실행
- 외부 연구 폴더 삭제/덮어쓰기
- Discord 첨부파일을 자동으로 연구 원본에 반영
- 브라우저 로그인 세션/쿠키를 이용한 ChatGPT·Claude·Gemini 자동화

## 실제 봇 구현 시 원칙

1. Discord 명령은 이 프로젝트의 CLI 또는 읽기 전용 MCP 도구로만 변환합니다.
2. prepare 결과는 DRAFT 상태로 남기고, 승인과 외부 실행은 로컬 CLI/대시보드에서 합니다.
3. 모델 결과는 model-provider.md로 staging에 저장할 수 있지만, 원고·원시 데이터에는 자동 반영하지 않습니다.
4. 공식 API를 쓸 경우 provider별 키와 월 한도를 분리하고, 키는 Discord에 절대 보내지 않습니다.

이 저장소에는 공식 Bot API 골격이 포함되어 있지만, 토큰이 없으면 시작되지 않습니다.

## 로컬 활성화

1. Discord Developer Portal에서 Application과 Bot을 만들고, 봇을 테스트 서버에 초대합니다.
2. 이 프로젝트에서 .env.example을 .env로 복사한 뒤 토큰·Application ID·테스트 Guild ID·허용 사용자 ID를 **사용자 로컬 파일에만** 입력합니다.
3. 먼저 테스트 Guild에 명령을 등록합니다.

       & 'C:\Program Files\nodejs\npm.cmd' run discord:register

4. 명령 표면을 다시 확인합니다.

       & 'C:\Program Files\nodejs\npm.cmd' run discord:check

5. 로컬 PC에서 봇을 시작합니다.

       & 'C:\Program Files\nodejs\npm.cmd' run discord:start

이 단계는 Discord와 통신하므로 사용자가 본인 토큰을 로컬 .env에 넣은 뒤에만 실행해야 합니다. 토큰을 채팅에 보내지 마세요.
