# 로컬 MCP 연결

이 프로젝트의 MCP 서버는 읽기 전용입니다. 경로 상태, 정책, 모델 라우팅, 등록된 연구 루트 안의 파일 manifest만 제공합니다. 시뮬레이터 실행이나 파일 내용 반환은 하지 않습니다.

## 서버 실행 파일

    C:\Program Files\nodejs\node.exe

## 서버 스크립트

    <RESEARCH_OS_ROOT>\src\mcp-server.mjs

## Claude Code에 수동 등록하는 예시

아래 명령은 사용자 전역 Claude 설정을 변경합니다. 현재 구성과 충돌하지 않는지 확인한 뒤 사용자가 직접 실행해야 합니다.

    $root = (Resolve-Path .).Path
    & 'C:\Users\effec\AppData\Roaming\npm\claude.cmd' mcp add --scope user research-os -- 'C:\Program Files\nodejs\node.exe' (Join-Path $root 'src\mcp-server.mjs')

등록 후에는 Claude Code에서 research_status, research_route, research_policy, research_file_manifest만 보여야 합니다. 쓰기나 실행 도구가 보이면 설정을 중지하고 이 프로젝트의 정책과 비교해야 합니다.

## 안전성 검증

    $requests = @(
      '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2025-03-26"}}',
      '{"jsonrpc":"2.0","id":2,"method":"tools/list","params":{}}'
    )
    $requests | & 'C:\Program Files\nodejs\node.exe' 'src\mcp-server.mjs'

응답에는 네 개의 읽기 전용 도구만 포함되어야 합니다.
