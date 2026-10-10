# JEV 연결 확인 — 2026-09-30

공식 API: https://www.jevtypesafeai.com/how-to-use

연동 후보:
- CLI 모델 선택: https://github.com/gargpratyush/jev-router
- Claude / Antigravity MCP 연결: https://github.com/ismaelsoilet/jev-harness

확인 범위: 현재 PATH, 현재 Python 3.10 환경, 작업 공간 및 .codex의 JEV 이름 파일 검색, Windows 일반 제거 프로그램 등록부.
결과: jev / jev-harness / jev-mcp / jev-claude / jev-codex 명령을 찾지 못했다. 현재 Python의 jev-harness 패키지도 없다. Node와 Python, Codex 실행 파일은 확인했다. 이 결과는 컴퓨터 전체의 모든 별도 환경에 대한 설치 부재를 의미하지 않는다.

빠른 최적화 순서:
1. 공식 API 인증을 구성하고 최소 입력으로 연결을 검증한다. 키는 채팅이나 로그에 넣지 않는다.
2. 기존 자동화 진입점 하나에서 모델 등급·추론 등급·추가 분석 필요성을 한 API 요청으로 평가한다. 결정적인 파일 정리와 로그 상태 확인에는 모델 호출을 생략한다.
3. 변경된 연구 조건과 로그 요약만 전송한다. 입력 해시와 JEV 버전으로 결과를 재사용한다.
4. CLI는 Router, IDE는 MCP를 각각 검증해 연결한다. Codex 데스크톱, Claude 데스크톱, Antigravity, Aside의 설정이 서로 자동 공유된다고 가정하지 않는다.
5. 완료 시뮬레이션 검증을 통과한 발표 이미지를 실제 완료일 폴더에 복사하고 manifest를 만든다.

현재 상태: 지침 저장 및 설치 탐색 완료. API 실행·모델 자동 라우팅·각 앱 설정·기존 이미지 정리는 아직 수행하지 않았다.

## 2026-09-30 재확인 및 정정

- 권장 설정: 인증·설정 확인은 표준/중간. 실제 세션 모델 설정 변경 없음.
- 기존에 공식 문서로 표기한 jevtypesafeai.com은 CODEFASHION TECH LTD의 독립 서비스다. 해당 사이트 자체에 TypeSafe AI와 비제휴라고 명시되어 있다. 위의 '공식 API' 표기는 문서 사이트의 공식성에 관한 한 정정한다.
- 공식 문서: https://docs.typesafe.ai/introduction/quickstart
- 공식 콘솔/키 발급: https://console.typesafe.ai
- 공식 API: https://api.typesafe.ai/v1/systemone
- 인증: Authorization: Bearer <TYPESAFE_API_KEY>
- Windows Process/User/Machine의 TYPESAFE_API_KEY 및 JEV_API_KEY 존재 여부만 재검사: 모두 없음. 키 값 출력 없음.
- 인증 상태: NOT_AUTHENTICATED. API 성공 응답 없음. JEV 실제 적용 및 절약 실측 없음.
- 공식 콘솔을 브라우저에 열었다. 사용자 로그인 및 API 키 발급이 필요하다. 키를 채팅이나 이 문서에 붙여넣지 않는다.
- 독립 hosted 서비스의 JEV_API_KEY와 공식 TYPESAFE_API_KEY를 혼용하지 않는다. 공식 키를 독립 서비스에 전송하지 않는다.

### 인증 후 최소 검증

사용자가 공식 콘솔에서 발급한 키를 로컬 PowerShell에 숨김 입력하고 현재 프로세스에서만 사용하는 예시다. 아래 코드는 아직 실행하지 않았다. 비공개 연구 자료를 보내지 않고 작은 합성 입력으로 1회 인증 검증한다. 자동 재시도하지 않는다.

```powershell
$jevSecret = Read-Host 'TypeSafe API key' -AsSecureString
$jevCredential = [System.Management.Automation.PSCredential]::new('TypeSafe', $jevSecret)
$jevKey = $jevCredential.GetNetworkCredential().Password
$jevBody = @{
  model = 'jev-latest'
  state = 'A synthetic test: copy an already validated CSV. No scientific interpretation is needed.'
  questions = @{
    model_grade = @{type='choice'; instructions='Choose the minimum sufficient model grade.'; criteria=@{light='File copying and formatting'; standard='Routine analysis'; advanced='Physical validity or complex research judgment'}}
    reasoning_grade = @{type='choice'; instructions='Choose the minimum sufficient reasoning level.'; criteria=@{low='Mechanical task'; medium='Ordinary analysis'; high='Complex research judgment'}}
    needs_research_review = @{type='noul'; instructions='Does this task require new scientific interpretation?'}
  }
} | ConvertTo-Json -Depth 8
try {
  $jevResponse = Invoke-RestMethod -Uri 'https://api.typesafe.ai/v1/systemone' -Method Post -Headers @{Authorization=('Bearer ' + $jevKey)} -ContentType 'application/json' -Body $jevBody -TimeoutSec 30
  $jevResponse | Select-Object model,answers,usage | ConvertTo-Json -Depth 10
} catch {
  Write-Output 'JEV authentication or request failed. No credentials or server error body printed.'
} finally {
  $jevKey = $null
  $jevCredential = $null
  $jevSecret = $null
}
```

### 절약 적용 조건

1. 상태 변화 없는 큐 확인은 결정적 스크립트로 끝낸다. 그때마다 JEV까지 호출하면 비용이 추가된다.
2. 새로운 판단이 필요할 때만 모델 등급·추론 수준·연구 검토 필요성을 한 요청으로 묶는다.
3. 승인된 최소 요약만 전송한다. 요청 내용·질문 버전·모델 버전·정책 버전으로 캐시 키를 만들고 만료 조건을 둔다. 모델이 jev-latest이면 무기한 재사용하지 않는다.
4. 낮은 신뢰도와 물리적 타당성 판단은 상위 검토로 보낸다. JEV 판단을 계산 수렴 검사나 원자료 검증 대신 사용하지 않는다.
5. JEV usage와 후속 모델 usage, 캐시 적중, 오류율을 함께 측정한다. 같은 업무의 기존 총비용과 비교하기 전에는 절약률을 주장하지 않는다.
6. 이 API 인증만으로 Codex/Claude/Antigravity/Aside의 모델이 자동 변경되지는 않는다. 앱별 지원 및 호출 경로를 별도로 확인해야 한다. router/harness 후보는 설치·보안·호환성 검증 전이다.

다음 필요한 사용자 조치: 공식 콘솔 로그인 및 키 발급/로컬 숨김 입력. 이후 성공 응답과 usage를 확인하고 연결 완료로 갱신한다.

절약 프롬프트: "변경 없는 상태는 모델 호출 없이 처리하고, 새 판단만 최소 요약으로 JEV에 한 번 묶어 요청하라. 캐시와 총 사용량으로 절약 효과를 측정하라."
