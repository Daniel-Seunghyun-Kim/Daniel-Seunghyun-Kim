# Connect AI 전수 브리프

작성일: 2026-09-29T05:11:10.052Z  
대상 앱: C:\Program Files\Connect AI\Connect AI.exe  
확인된 설치 정보: EZER AI Connect AI v0.5.12, "100% 로컬·무료" 설명

## 1. 핵심 결론
Connect AI는 외부 클라우드 모델 라우터가 아니라 로컬 모델 중심 앱으로 쓰는 것이 맞다. Aside에서 쌓은 교훈은 다음 형태로 옮긴다.

1. 로컬 우선: Ollama 또는 LM Studio 모델을 기본 실행 엔진으로 둔다.
2. 외부 Provider는 직접 호출하지 말고 잔량/리셋 확인 장부로만 관리한다.
3. 모든 작업은 기존 근거 재사용, 최소 컨텍스트, 짧은 출력, 필요한 경우만 고급 모델 사용 원칙을 따른다.
4. 수치/주장은 반드시 MEASURED, COMPUTED, LITERATURE, ASSUMED_EXAMPLE, UNVERIFIED 중 하나로 라벨링한다.
5. 검증 안 된 숫자(예: 423nm, 58.8%, 158개 PPTX 감사, 12노드)는 보고자료에 넣지 않는다.

## 2. Aside에서 확인된 Provider 현황
- Aside Pro: 0 credits / 0%, 2026-10-23에 1,800 credits 갱신
- Claude Subscription: 연결됨, Aside 화면에서 리셋 미노출
- ChatGPT Subscription: 연결됨, Aside 화면에서 리셋 미노출
- Ollama API: 연결됨, 로컬/클라우드 여부는 별도 확인 필요
- Google API: 연결됨, 쿼터/리셋은 Google 대시보드에서 확인 필요
- Perplexity API: Aside에는 미연결
- Liner API: Aside에는 미연결
- TypeSafe JEV: 이번 전수 대상에서 제외

## 3. Connect AI에 넣을 운영 지침
### 기본 라우팅
- 단순 요약/분류/초안: 가장 작은 로컬 모델
- 코드/파일 수정: 코딩 성능이 검증된 로컬 모델(Qwen Coder 계열 권장 후보)
- 긴 문서 분석: 컨텍스트가 큰 로컬 모델 또는 청크 처리
- 외부 최신 정보 검색: 브라우저/웹검색 결과만 근거로 사용, 모델 기억에 의존 금지

### 금지
- Provider명만 보고 잔량/리셋 시각 추정 금지
- 자동 유료 fallback 금지
- 로그인·API 키·토큰을 프롬프트에 복사 금지
- 긴 대화 전체를 다른 모델에 통째로 전달 금지
- 검증되지 않은 수치를 확정 결과로 표현 금지

### 필수 출력 규칙
- 무엇을 확인했는지, 무엇이 미확인인지 구분
- 출처/파일/화면이 있는 내용만 확정
- PPT/보고서에는 실제 근거가 있는 내용만 포함

## 4. AlN 연구 전수 요약
- 리뷰논문 내용은 제외한다. 수정본은 이미 제출됨.
- 교수님 보고용 자료는 AlN 실험/시뮬레이션 중심.
- 포함 가능한 검증 내용: AlN(002) 배향 최적화, GI-XRD 확인, RF sputtering 조건, TDTR 준비, 양면 폴리싱 Si wafer 견적, 아주대 TDTR 가능성, 기판 온도 직접 측정 공백, WP0-WP8 시뮬레이션 현황, 6개 blocked node.
- 제외/보류: 423nm crossover, 58.8% Rth 감소, 158 PPTX 감사, HBF/CBA/Selective AlN/Malik/Rebhan/96 W/mK 등 근거 미확인 항목.
- 안전 표현: "의도적인 기판 가열 없이 진행한 증착". "상온 RF 증착"은 직접 측정값 확보 전 보류.

## 5. Connect AI 시작 후 확인할 항목
1. 설정에서 엔진이 Ollama 또는 LM Studio로 되어 있는지 확인
2. Ollama: http://localhost:11434/v1/models 또는 /api/tags 모델 자동 감지 확인
3. LM Studio 사용 시 Developer server가 켜져 있는지 확인
4. 기본 모델, 코딩 모델, 요약 모델을 분리할 수 있으면 분리
5. 위 운영 지침을 Connect AI의 시스템 지침/메모리/프로젝트 지침에 붙여넣기

## 6. 권장 첫 프롬프트
아래 지침을 내 기본 운영 원칙으로 기억하고, 이후 작업에서 항상 적용해라.

- 로컬 모델 우선, 외부 Provider/API는 잔량·리셋 확인 전 사용 금지.
- 기존 근거와 파일을 먼저 재사용하고, 필요한 변경분만 읽어라.
- 긴 출력보다 요약/차이/결정사항 위주로 답하라.
- 모든 수치와 주장을 MEASURED/COMPUTED/LITERATURE/ASSUMED_EXAMPLE/UNVERIFIED로 라벨링하라.
- 검증되지 않은 연구 수치는 보고자료에 넣지 마라.
- 불확실하면 추정하지 말고 [blocked]와 필요한 다음 확인 항목을 적어라.


## Ollama 현재 감지 결과 (2026-09-29T05:11:58.161Z)

### 로컬 모델 후보(리셋 없음, 로컬 자원 사용)
- qwen3.5:9b-64k: 9.7B, Q4_K_M, context 262144, capabilities completion/vision/tools/thinking
- qwen3.5:9b: 9.7B, Q4_K_M, context 262144, capabilities completion/vision/tools/thinking
- granite4.1:3b: 3.4B, Q4_K_M, context 131072, capabilities completion/tools

### Ollama Cloud 모델(로컬 무료로 취급 금지)
- gemma4:31b-cloud: remote_host=https://ollama.com, context 262144, capabilities completion/thinking/tools/vision
- deepseek-v4.1-flash:cloud: remote_host=https://ollama.com, context 1048576, capabilities completion/thinking/tools/vision
- glm-5.3:cloud: remote_host=https://ollama.com, context 1048576, capabilities completion/thinking/tools
- glm-5.3-flash:cloud: remote_host=https://ollama.com, context 1048576, capabilities completion/thinking/tools/vision

### Connect AI 권장 매핑
- 기본/긴 컨텍스트: qwen3.5:9b-64k
- 일반 도구/추론: qwen3.5:9b
- 초경량 단순 작업: granite4.1:3b
- cloud 접미사 모델은 유료/원격 가능성이 있으므로 자동 기본값 금지
