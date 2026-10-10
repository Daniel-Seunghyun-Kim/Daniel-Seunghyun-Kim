# PC2 전주기 연구 실행 지침

2026-10-01 KST. 추천 고성능/높음, 실제 모델 설정 변경 없음. JEV 인증키는 Windows Process/User/Machine 모두 미확인으로 미적용. 새 DFT/BTE/MD/FEM 계산은 이번 지침 작성에서 실행하지 않았다.

## 현재 사실

- CPU force 220개 완료, 전체 물성 연구 완료 아님. 98개 재사용 force 원자료 출처와 순서 검증이 남는다. 기존 CSV의 REUSED_VERIFIED 문자열 자체를 원자료 인증으로 사용하지 않는다.
- 144/72 정밀 SCF는 이미 1e-10으로 완료. 기존 감사와 해시를 재사용한다. IEEE stderr 경고가 남아 최종 gate는 보류. 1e-8 중복 실행은 제외.
- 흡착 입력은 72가 아닌 125원자 parent와 126원자 adsorbate 구조다.
- WSL22 실측: nproc=32, RAM 총108GiB/가용106GiB. 가상 토폴로지는 실제 8P+16E 물리 코어 매핑을 제공하지 않는다. GPU 메모리는 장당24GB이며 단일48GB 공간이 아니다.
- 설치 phono3py=4.4.0. 해당 버전 --help로 아래 CLI 옵션 확인. 수치 계산 자체의 실행 검증은 아직 하지 않았다.

## 실행 우선순위와 자원

1. 기존 IEEE 경고 진단 및 98개 provenance/FC2/FC3 입력 매핑 복구를 병행한다. 기존 파일만 읽는 작업은 함께 수행 가능하다.
2. CPU: 검증된 전체 force 취합 → IFC 조립/ASR·drift·분산·NAC 검사 → 300K RTA 자원 측정 → q-grid 수렴 → 온도 스윕 → 선택 mesh/온도 LBTE 비교 → 두께/MFP 분석.
3. GPU: 125원자 parent 검증 → FCC/HCP/Bridge/Ontop → 최종 좌표로 정밀 force 확인 → 안정된 동일 셀 endpoint에 기반한 표면 확산/침투 NEB. 초기 보간 구조의 겹침과 spin 상태도 검증한다. 활성화 장벽만으로 증착 속도를 확정하지 않는다.
4. 기존 slab scratch의 완전성이 확인되면 pp.x/average.x 후처리를 먼저 수행할 수 있다. 180원자 비교는 같은 종결/면내 셀/고정층/경계 조건으로 준비한다. 대면적 128–146원자 작업은 이후다.
5. 검증된 mode-resolved BTE와 경계 모델로 박막 분석, 이후 3ω/FEM과 HBM 모델.

동시 실행은 조건부 허용 전략이다. GPU QE가 호스트 RAM/CPU/메모리 대역폭을 사용한다. 초기 CPU 프로파일은 OMP=16, BLAS=1; GPU는 MPI2×OMP1로 보수적으로 시작하도록 제안한다. 이는 측정된 최적값이 아니다. CPU 단독으로 같은 대표 작업을 16/24/32 threads에서 시간·최대RSS로 비교한 후 선택한다. 32 threads가 24보다 빠르다고 가정하지 않는다. BTE와 GPU의 최대RSS 합 및 OS/WSL 여유를 확인하기 전에는 대형 LBTE와 GPU 작업을 동시에 시작하지 않는다. 125/126 출력의 약87GB RAM 추정은 GPU VRAM과 다른 지표다.

## CPU 명령 형태: 검증된 독립 실행 폴더가 준비된 후에만 사용

현재 98개 provenance와 파일 목록이 확정되지 않아 아래는 생산 실행 승인이 아닌 버전 확인된 템플릿이다. 원래 campaign에서 실행하지 않는다. validated_forces.list는 YAML의 포함 displacement 순서와 일대일로 대응하는 절대 출력 경로 목록이어야 하며 임의 glob으로 만들지 않는다. 새220개만으로 구성하지 않는다. cutoff-pair에 의해 제외된 displacement와 포함된 displacement를 구별한다. yaml의 calculator: qe와 단위/셀도 확인한다.

```bash
export OMP_NUM_THREADS=16
export OMP_MAX_ACTIVE_LEVELS=1
export OPENBLAS_NUM_THREADS=1
export MKL_NUM_THREADS=1
export BLIS_NUM_THREADS=1
# 승인된 별도 폴더에서만:
phono3py-init --cf3-file validated_forces.list > collect.log 2>&1
# 위 단계는 FORCES_FC3 생성. IFC 조립과 다르다.
phono3py phono3py_disp.yaml --symfc > ifc.log 2>&1
# symfc 사용은 후보. cutoff/included 데이터 지원 및 기존 solver와 비교 확인 필요.
/usr/bin/time -v phono3py phono3py_disp.yaml --br --mesh 15 15 8 --ts 300 > rta_300.log 2> rta_300.resource.log
```

FC2/FC3 HDF5 재사용 시 정확한 입력/단위/초격자/primitive cell 대응을 확인한다. 기존 같은 이름 HDF5를 다른 계산에서 가져오지 않는다. FC2에 별도 초격자를 썼다면 해당 FORCES_FC2/설정이 필요하다. AlN NAC에 필요한 Born 유효전하와 유전텐서 및 그 셀/순서를 검증하며, 파일이 없다고 묵시적으로 NAC를 생략하지 않는다.

각 mesh는 별도 폴더: 15x15x8 → 21x21x12 → 27x27x15 및 c축 짝수 mesh 민감도. 끝 mesh를 자동으로 수렴이라고 지정하지 않는다. 동일 온도/solver/IFC에서 kxx, kzz, 저주파 및 MFP 꼬리를 비교한다. 허용오차는 비교 전에 고정한다.

```bash
# 수렴 mesh 확정 후 예시 온도 목록(100K 간격 제안):
phono3py phono3py_disp.yaml --br --mesh 27 27 15 --ts 100 200 300 400 500 600 700 800 > rta_T.log 2>&1
# LBTE는 먼저 별도 폴더에서 충돌행렬 메모리 예측:
phono3py phono3py_disp.yaml --lbte --mesh 15 15 8 --ts 300 --wgp > lbte_memory.log 2>&1
```

LBTE 예측에는 고유값 풀이 workspace 등 추가 메모리 여유가 필요하다. 한 온도씩 평가하며 `--write-pp` 같은 큰 저장 옵션을 기본으로 켜지 않는다. phono3py에 mpirun -np 24를 단순히 씌우지 않는다. 설치 backend가 OpenMP 설정을 실제 사용하는지 대표 작업으로 확인한다.

## 단계별 종료 판정

| 단계 | 통과 근거 |
|---|---|
| force 취합 | exit0, 포함 displacement 전수 대응, 원자 수/순서/유한값/단위, 원출력 및 pseudo 해시 |
| IFC | FC2/FC3 shape/원자매핑/유한값, drift·병진 불변성 잔차, 분산 안정성; symmetrization 전후 비교 |
| RTA/LBTE | exit0, HDF5 온도/mesh/IFC 일치, 텐서 유한성과 대칭·물리성, q-grid/solver/절단거리/초격자 수렴 별도 |
| slab relax | exit0 AND JOB DONE AND BFGS 종료 AND 최종좌표/이동 힘/에너지 수렴, 경고 검토 |
| NEB | 모든 이미지/endpoint 일관성, NEB 힘 오차 수렴, 이미지 수/경로·장벽 안정성; JOB DONE만으로 통과 불가 |
| V(z) | scratch 출처 일치, 포텐셜 정의/단위/축 및 smoothing 창 명시, 진공 plateau와 내부 선형 fit 구간 검증 |
| FEM | mesh/time/frequency 수렴, 에너지 보존, 경계/재료/히터 조건, 측정 독립 검증과 불확도 |

## GPU 실행 경로와 내구성

구체 환경·명령은 PC2_NEXT_EXECUTION_DIRECTIVE.md를 따른다. 확정된 wrapper:
`/mnt/c/Users/AOL/Desktop/SH.Kim/AlN_QE_PC2/AlN_QE_PC2_Dual4090_20260728_172441/wsl/qe_rank_gpu_wrapper.sh`

실행 복사본만 LF/ASCII로 만들고 해시 고정, 원본 보존. 기존 흡착5입력은 CRLF 없음이 확인됐다. 큐 잠금·기존 pw.x 차단·독립 scratch·실제 exit code 기록이 필수다. Windows 숨김 wsl.exe가 전경 bash를 유지한다. nohup 단독이나 systemd만으로 WSL 생존을 보장하지 않는다. 현 입력은 미검증이므로 생산 런처를 확정했다고 보고하지 않는다.

## 연구 해석에서 보완할 점

- Vermeersch 박막 억제는 mode별 cross-plane 속도/수명/기여도와 모델 경계조건이 필요하다. bulk kzz 숫자 하나나 임의 평균 MFP만으로 대체하지 않는다. 다른 형상/계면 산란을 자동 포함하지 않는다.
- average.x는 평면 평균이다. V(z) 기울기에서 얻는 내부 전기장과 자발 분극은 다르다. 전자 퍼텐셜 에너지의 부호/단위를 전위로 변환할 때 명시한다. 자발 분극에는 벌크 절연체의 Berry-phase/이온 기여, 기준 상태와 polarization branch가 별도 필요하다. dipole correction을 후처리에서 추가한 척하지 않는다.
- 극성 비대칭 slab 두께2개로 개별 표면 에너지를 단순 확정할 수 없다. 양면 종결/화학퍼텐셜/전기적 경계를 지정한다.
- 3ω 전류 주파수 f에서 Joule heating은 2f이고 전압 신호가 3f다. 10Hz–100kHz가 어떤 주파수인지 먼저 명시한다. 히터 폭/길이/두께, 저항 온도계수, 층두께·열용량·기판, 복소 V3ω 측정과 오차가 없으면 TBR 역해석을 확정할 수 없다. k와 TBR의 식별 가능성도 평가한다.
- HBM16단은 실제 형상·층별 재료·전력 분포·냉각 경계·계면저항이 필요하다. BTE 텐서를 실제 결정 방향에 맞춰 회전하고, 이미 억제된 유효k와 추가 경계 산란을 이중 적용하지 않는다. 가정 기반 민감도 결과와 실측 검증 예측을 분리한다.

## 자동화와 결과

기존 완료 ledger와 해시를 재사용한다. 추가 계산이 시작되기 전 시간 ETA를 확정하지 않는다. 첫 대표 계산의 wall/RSS/반복 수로 갱신한다. 완료된 기존 감시를 불필요하게 재개하거나 중복 생성하지 않는다. 수치 검증·물리 수렴·문헌/실측 일치의 세 상태를 독립 기록한다. 검증된 결과만 실제완료일(Asia/Seoul) 폴더와 manifest로 수집한다.

## 근거

- https://phonopy.github.io/phono3py/command-options.html
- https://phonopy.github.io/phono3py/direct-solution.html
- https://arxiv.org/abs/1512.01354
- https://www.quantum-espresso.org/Doc/pp_user_guide/node6.html
- https://www.quantum-espresso.org/Doc/pw_user_guide/node10.html

절약 프롬프트: 새220개·재사용98개의 입력 매핑과 기존 ledger를 재사용하라. 자원 실측으로 동시 실행 여부를 정하고, 변경 job만 검증하며 수치·물리·실측 게이트를 분리하라.
