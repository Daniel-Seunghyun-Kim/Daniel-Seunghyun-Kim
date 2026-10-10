# 새 모델용 Bootstrap 계약

이 Research State Pack을 사용하는 모델은 다음 순서를 바꾸지 않는다.

1. 00_control/state.json을 읽어 status, checkpoint, state_revision, active_manifest_sha256, next_allowed_actions를 확인한다.
2. 00_control/HANDOFF.md가 있으면 그 state_revision과 state_sha256이 state.json과 일치하는지 확인한다. 불일치하면 HANDOFF_MISMATCH로 기록하고 실행하지 않는다.
3. 00_control/policy.yaml을 읽고 쓰기 경계, 증거 분류, 실행 probe, 토큰 중단 규칙을 적용한다.
4. 새 PC이면 01_inventory/roots.yaml의 root alias를 새 절대경로로 해석하고, 파일 hash와 safe probe를 다시 수행할 필요가 있는지 판단한다. 이전 PC의 성공 상태는 RECHECK_REQUIRED다.
5. 현재 checkpoint가 PREPARED, VALIDATING, ABORTING, STOP_TOKEN_BUDGET, BUDGET_UNVERIFIABLE, HALTED_INSUFFICIENT_TOKENS 중 하나이면, controller의 명시적 재개 전에는 새 worker·외부 모델·프로그램을 시작하지 않는다.
6. 아이디어를 낼 때는 03_ideas/proposals/<run_id>/<worker_id>.jsonl에만 append한다. 다른 모델의 proposal을 사실 또는 직접 근거로 승격하지 않는다.
7. 각 아이디어마다 다음을 분리한다.

   - DIRECT_EVIDENCE: 실제 파일 hash, 실행 log, 측정값, 검증된 출처처럼 직접 확인된 사실
   - INFERENCE: 자산 조합으로부터 도출한 가설·가능성
   - NOT_VERIFIED: 누락 데이터, 라이선스, 물리 검증, 새 PC에서의 재검증 등

8. 원본 자산·실행 파일·실험 입력은 수정하지 않는다. 생성물은 05_runs/<run_id>/ 아래에만 쓴다.

안전 중단 원칙: 예산이 불충분하거나 검증 불가능하면, 더 적은 범위로 조용히 계속하지 않는다. STOP_TOKEN_BUDGET 또는 BUDGET_UNVERIFIABLE을 기록하고 사용자 또는 controller가 새 범위를 동결할 때까지 멈춘다.
