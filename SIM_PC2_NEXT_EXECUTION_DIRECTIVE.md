# PC2 후속 실행 지침 — 2026-10-01 KST

상태: 실행 순서 확정. 기존 생산 입력의 즉시 실행은 보류. 이 문서는 새 계산을 실행하지 않았다. 무결점 실행이나 종료 시각은 보장하지 않는다.

## 보고 정정과 순서

1. 144/72 정밀 SCF는 이미 conv_thr=1e-10으로 각각 10월 1일 05:13, 05:20 종료했다. 1e-8 재실행은 제외한다. 수치 힘 검사는 통과했지만 stderr IEEE invalid 경고 원인은 미해결이다. 원본 stdout/stderr와 기존 validation.json을 재사용해 진단하고, 필요할 때만 원인을 구분할 수 있는 최소 비교 계산을 설계한다. 같은 설정 전체 재실행은 원인 규명이 아니다.
2. 질화 연구 우선: 125원자 clean parent 준비 및 검증 → 같은 셀/기판에서 FCC → HCP → Bridge → Ontop 순차 완화. 이 순서는 재현성을 위한 고정 순서이며 사이트 안정성 예측이 아니다. 기존 입력은 72원자 기반이 아니라 125+1=126원자다. parent의 검증된 최종 좌표로 흡착 입력을 재생성해야 한다.
3. AlN144의 경고·기준 설정을 정리한 후 180원자 두께 비교. 144와 180의 표면 종결, 면내 셀, 고정층, 진공, 전기적 경계와 수치 조건이 비교 가능해야 한다. 180 한 점 추가만으로 두께 수렴을 선언하지 않는다.
4. 흡착 결과와 자원 실측 후 128원자 Al 및 129–146원자 질화. 125/126과의 차이를 단순 면적 효과로 가정하지 않는다.

두 GPU는 우선 한 job의 MPI rank 2개로 사용한다. 두 개의 대형 job을 GPU별로 동시에 올리지 않는다. GPU 24GB 두 장을 단일 48GB 메모리로 취급하지 않는다.

CPU 완료는 220/220 최종 성공이다. 기존 supervisor 재시작 기록이 있으므로 전체 이력의 '무결점/무중단' 표현은 철회한다. IFC 물리 검증 완료를 뜻하지 않는다.

## 지금 실행 가능한 명령: 읽기 전용 사전점검

PowerShell:

```powershell
wsl.exe -d Ubuntu-24.04 -u aol2 -- python3 /mnt/c/Users/AOL/Desktop/SH.Kim/Simulation_Verification_2026-09-30/pc2_next_preflight.py
```

exit 78은 현재 생산 큐 미승인 차단이라는 의도된 결과다. QE는 호출하지 않는다. 이를 우회하거나 과거 exit 78 런처를 복원하지 않는다.

## 확인된 실행 환경

GPU distro/user: Ubuntu-24.04 / aol2. CPU 감사 환경 Ubuntu-22.04 / aol과 혼동하지 않는다.

```bash
PW=/home/aol2/qe_gpu_builds/qe-7.2-dual4090-sm89/bin/pw.x
WRAPPER=/mnt/c/Users/AOL/Desktop/SH.Kim/AlN_QE_PC2/AlN_QE_PC2_Dual4090_20260728_172441/wsl/qe_rank_gpu_wrapper.sh
export NVHPC_ROOT=/opt/nvidia/hpc_sdk/Linux_x86_64/25.3
export OPAL_PREFIX="$NVHPC_ROOT/comm_libs/openmpi4"
export PATH="$NVHPC_ROOT/compilers/bin:$OPAL_PREFIX/bin:$NVHPC_ROOT/cuda/12.8/bin:$PATH"
export LD_LIBRARY_PATH="$NVHPC_ROOT/compilers/lib:$OPAL_PREFIX/lib:$NVHPC_ROOT/math_libs/12.8/lib64:$NVHPC_ROOT/cuda/12.8/lib64:${LD_LIBRARY_PATH:-}"
export OMP_NUM_THREADS=1
```

PW와 래퍼의 존재·실행 권한을 확인했다. 래퍼는 OMPI_COMM_WORLD_LOCAL_RANK를 CUDA_VISIBLE_DEVICES에 매핑한다. 런처는 mpirun -np 2로 호출하며, MPI local rank가 0/1인지 사전 검증한다. 스킬의 Downloads 경로는 사용하지 않는다.

## 생산 런처 확정 전에 필요한 입력 계약

- 이번에 읽은 clean parent/흡착 입력: ecutwfc=55, ecutrho=440, conv_thr=1e-6. 제출된 보고와 다른 실제 입력이므로 검증된 수렴 조건을 선정하고 해시를 고정해야 한다. 값만 임의로 80/640 또는 1e-8로 바꾸지 않는다.
- 각 입력의 셀·원자 수·원자 순서·고정 mask·최소 거리·spin/charge·pseudo SHA256·k-grid·진공 및 비대칭 slab 전기적 경계를 검토한다. N 원자/N2 기준 계산도 흡착 에너지 정의에 맞게 별도 지정한다.
- 별도 실행 디렉터리, 절대 pseudo_dir/outdir, 유일한 prefix와 비어 있는 scratch를 확정한다. CRLF 제거는 원본을 덮어쓰지 않고 실행 복사본에만 적용한다. LF/ASCII와 해시를 다시 확인한다.
- 기존 출력/체크포인트가 있으면 정지한다. 파일 존재만으로 restart를 선택하지 않는다. 실패 자료의 최종 유효 좌표는 후보로 재사용 가능하지만 구조/설정 검증이 선행되어야 한다.
- flock 큐 잠금과 기존 pw.x 확인을 적용한다. 승인 입력/래퍼/검증기 해시가 바뀌면 실행을 거부한다.

## 승인된 단일 case에서 사용할 호출 형태 (현재 실행 금지)

아래는 생성 완료된 실행 디렉터리에서 런처가 사용할 명령 형태다. 현재 생산 입력과 검증기는 확정되지 않았으므로 복사하여 직접 실행하지 않는다.

```bash
mpirun -np 2 --mca btl_vader_single_copy_mechanism none --mca btl ^openib --mca pml ucx "$WRAPPER" "$PW" -nk 1 -in "$PWD/pw.in" >pw.out 2>pw.err
```

종료 직후 실제 MPI exit code를 저장한다. SCF는 exit 0 AND JOB DONE AND 최종 전자 수렴/정확도 AND 원자 수에 맞는 유한 힘이 필요하다. relax는 여기에 End of BFGS Geometry Optimization AND 최종 좌표 AND 이동 가능 성분별 힘/에너지 수렴을 추가한다. JOB DONE OR BFGS로 판정하지 않는다. 실패·SCF correction large·IEEE invalid/divide-by-zero·미완료이면 다음 생산 job을 시작하지 않고 검토 상태로 종료한다. 정밀 수치 검사와 물리 수렴/문헌 비교는 별도다.

## 백그라운드와 WSL 생존

nohup으로 Linux 부모 shell만 분리하면 WSL 생존을 보장하지 못한다. 이번에 systemd 방식의 WSL 종료 사례가 있으므로 Windows 숨김 wsl.exe가 전경 bash 런처를 끝까지 기다리는 기존 방식을 사용한다. 확정된 런처 생성 후 PowerShell Start-Process -WindowStyle Hidden과 stdout/stderr 리다이렉션, Windows PID 및 queue lock을 기록한다. 전경 유지 명령 끝에 &를 붙이지 않는다. nohup 단독 실행 또는 sleep infinity를 내구성 보장으로 안내하지 않는다. 재부팅·WSL 종료에 대한 무중단 보장은 없다.

## ETA 및 자동화

기존 AlN144 정밀 SCF 실측은 약 10.62시간이다. 제공된 1.5–2시간 및 흡착 7–8시간은 현재 입력/성능으로 검증되지 않았으므로 '오늘 16:30/자정' 확약을 사용하지 않는다. 125 parent와 첫 흡착의 SCF 반복/이온 단계/메모리 실측 후 범위 ETA를 갱신한다. 180 및 128–146의 제시 시간도 미검증이다.

기존 aln-fc3 감시는 완료 후 일시 중지된 상태다. 새 큐가 실제 시작되면 기존 감시를 해당 ledger에 맞춰 갱신하고 중복 감시를 만들지 않는다. 동일 해시 재감사는 생략한다.

JEV: Process/User/Machine TYPESAFE_API_KEY 존재 여부 재확인 결과 없음. 미적용. 추천 고성능/높음이며 실제 모델 설정 변경 없음.

참고: https://www.quantum-espresso.org/Doc/INPUT_PW.html (현재 웹 문서는 QE 7.5, 설치 바이너리는 7.2이므로 버전별 옵션 호환성 확인 필요).

절약 프롬프트: 기존 SCF 결과와 감사 해시를 재사용하라. 125원자 parent 의존성과 경고 원인을 먼저 해결하고, 검증된 입력만 단일 큐로 실행하며 변경된 job만 검사하라.
