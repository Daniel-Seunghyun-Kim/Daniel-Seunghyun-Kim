# Handoff

- state_revision: 0
- state_sha256: null
- current status: NOT_STARTED
- trusted inventory: none
- trusted execution probes: none
- committed research ideas: none
- active model-specific work: none

이 번들은 운영 계약과 빈 상태만 갖는다. 실제 파일·폴더·프로그램 경로, 실행 가능성, 연구 아이디어, PC 사양 값은 아직 기록되지 않았다.

새 모델은 BOOTSTRAP.md와 state.json을 먼저 읽고, 정책에 맞는 읽기 전용 인벤토리부터 시작한다. state.json의 revision 또는 hash와 이 문서가 어긋나면 이 문서를 신뢰하지 않고 controller가 새 handoff를 발행할 때까지 멈춘다.
