# Step A3: 자율 복구 관리자 감시 프로토콜 (Autonomous Supervisor Recovery Protocol)

**기반 도구**: `adaptive_recovery_supervisor.py`  
**플랫폼**: PC2 Dual RTX 4090 무중단 상시 가동 시스템  
**작성일**: 2026-10-10 (Asia/Seoul)

---

## 1. 감시 프로토콜 개요
126원자 대형 흡착 시스템의 BFGS 완화 계산 중 발생 가능한 모든 비정상 상태(Process Crash, Charge Sloshing, Davidson Eig Unconverged, GPU VRAM Out-of-Memory)를 **인간 개입 없이 10초 주기 폴링**으로 자동 진단하고 즉각 교정하여 재실행합니다.

```mermaid
graph TD
    A[Start pw.x Dual RTX 4090] --> B[Supervisor Polling Loop (10s)]
    B --> C{State Analysis}
    C -->|JOB DONE| D[Archive Final Coordinates & Calculate E_ads]
    C -->|Normal Convergence| B
    C -->|SCF Sloshing Detected| E[Damp mixing_beta: 0.05 -> 0.025]
    C -->|Unexpected Crash| F[Validate Checkpoint & Relaunch restart]
    C -->|Davidson Divergence| G[Switch diagonalization to CG]
    E --> H[Graceful Restart pw_restart.in]
    F --> H
    G --> H
    H --> B
```

---

## 2. 이상 징후 판정 기준 및 자동 대응 매트릭스

| 감지 항목 | 감지 조건 (Regex/Threshold) | 자동 교정 조치 (Action) |
| :--- | :--- | :--- |
| **전하 진동 (SCF Sloshing)** | SCF Accuracy가 4회 연속 단조 증가 (`acc[i] > acc[i-1]`) | 프로세스 정상 종료 (`SIGTERM`) 후 `mixing_beta = mixing_beta / 2` 수정 후 재개 |
| **비정상 프로세스 종료** | PIDs가 소멸하고 `JOB DONE` 플래그 미존재 | 최신 `scratch/*.save` 체크포인트 무결성 검증 후 `restart_mode='restart'`로 자동 재개 |
| **고유치 미수렴 (Davidson)** | `c_bands: N eigenvalues not converged` 연속 발생 | `diagonalization = 'cg'` 강제 전환 및 `electron_maxstep = 200` 확장 |
| **VRAM 임계치 초과** | VRAM 여유분 $< 500\ \text{MB}$ 감지 | Rank 바인딩 재설정 및 일시 대기 후 슬랩 분할 최적화 |
| **열 마진 경고** | GPU 온도 $> 75^\circ\text{C}$ 또는 수랭 스로틀링 발생 | 팬 프로파일 강제 상향 및 30초 쿨다운 후 연산 지속 |

---

## 3. 무중단 연속 큐 관리자 연계
- 4개 상태(`ontop` $\to$ `bridge` $\to$ `fcc` $\to$ `hcp`) 중 이전 상태가 `JOB DONE`을 달성하면, 관리자는 즉시 에너지 및 힘을 추출하여 검증 보고서를 남긴 뒤, **대기 중인 다음 마이크로스테이트를 자동으로 큐에서 인출하여 Dual RTX 4090에 로드**합니다.
