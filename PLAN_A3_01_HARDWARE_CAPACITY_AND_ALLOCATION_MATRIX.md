# PC2 하드웨어 성능 제약 및 자원 할당 매트릭스 (Hardware Capacity & Allocation Matrix)

**노드 명칭**: PC2 Dedicated Compute & 3D Rendering Hub  
**OS 환경**: Windows 11 Pro + WSL2 (`Ubuntu-24.04`)  
**작성일**: 2026-10-10 (Asia/Seoul)

---

## 1. 하드웨어 스펙 및 제약 조건 정량화

| 하드웨어 항목 | 물리 사양 | WSL2 가용 사양 | 실측 피크 안전 한계 | Step A3 운영 방침 |
| :--- | :---: | :---: | :---: | :--- |
| **GPU 0** | RTX 4090 (24 GB) | 24,564 MiB | 23.5 GB (95%) | Rank 0 바인딩 (`CUDA_VISIBLE_DEVICES=0`) |
| **GPU 1** | RTX 4090 (24 GB) | 24,564 MiB | 23.5 GB (95%) | Rank 1 바인딩 (`CUDA_VISIBLE_DEVICES=1`) |
| **합산 VRAM** | 48 GB GDDR6X | 48 GB | 47 GB | `np=2, nk=1` 분할 실행 시 126원자 슬랩 VRAM 점유 약 22~23 GB/GPU |
| **시스템 RAM** | 128 GB DDR5 | 108 GiB + 32GB Swap | 75 GB 동적 메모리 | 모체 슬랩(125at) 기준 76.9 GB 동적 메모리 실측, 108 GiB 내에서 안전 동작 |
| **CPU 코어** | i9-13900K (24C/32T)| 32 vCPU | **16 Threads** | **`OMP_NUM_THREADS=4` (Rank당)** $\times 2$ Ranks = 8코어 또는 단독 16스레드 제한 준수 |
| **쿨링 솔루션** | 일체형 수랭 쿨러 | - | `cur_state=0` 유지 | GPU 풀로드 시 46~63°C, 175~185W로 이상적 열 마진 유지 확인 |

---

## 2. 병렬화 분할 아키텍처 (`np=2, nk=1`)

125원자 Al + 1원자 N = **총 126원자** 대형 슬랩 시스템은 단일 노드 다중 GPU 환경에서 다음과 같이 바인딩합니다:

```bash
# GPU Rank Wrapper Script를 통한 독점 바인딩
/mnt/c/Users/AOL/Downloads/AlN_QE_PC2/AlN_QE_PC2_Dual4090_20260728_172441/wsl/qe_rank_gpu_wrapper.sh
```

- **MPI 분할**: `-np 2` (GPU 0에 1개 프로세스, GPU 1에 1개 프로세스)
- **K-Point 분할**: `-nk 1` (k-point 풀을 분할하지 않고 대형 FFT 그리드 및 Davidson 대각화를 두 GPU가 긴밀히 분담)
- **스레드 분할**:
  ```bash
  export OMP_NUM_THREADS=8
  export MKL_NUM_THREADS=8
  export OPENBLAS_NUM_THREADS=8
  ```
  Rank당 8스레드를 할당하여 2개 Rank가 총 16스레드를 균등하게 점유하도록 하여 Core i9-13900K의 열 마진을 완벽하게 보호합니다.

---

## 3. 동시 실행 vs 순차 큐잉 전략 (Scheduling Policy)

로컬 `@local` 모델의 자원 분석 결과에 기반한 최적 실행 전략:

1. **VRAM 안전 마진 확보를 위한 `순차 큐잉(Sequential Batch Queue)` 채택**:
   - 126원자 슬랩은 단일 상태만으로도 각 GPU VRAM의 ~23 GB(94%)를 점유합니다.
   - 따라서 4개 상태를 동시에 실행하면 VRAM OOM(Out of Memory)이 발생할 수 있습니다.
   - **결론**: **4대 마이크로스테이트는 Dual RTX 4090 전체 자원(`np=2, nk=1`)을 100% 투입하여 `ontop` $\to$ `bridge` $\to$ `fcc` $\to$ `hcp` 순서로 순차 자동 연속 실행**하는 파이프라인이 가장 빠르고 안전합니다.
