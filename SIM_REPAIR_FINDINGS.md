# 계산 보고·실행 경로 정정 및 재개 기록

2026-09-30, Asia/Seoul. 인용된 Gemini 보고를 지정된 FC3·slab·흡착 경로 및 기존 감사 자료와 대조했다. 특정 모델의 성능이 원인이라는 인과관계는 입증하지 않았다. 확인한 원인은 성공 판정·재시작 조건의 결함, 서로 다른 구조의 의존관계 혼동, 근거보다 강한 확정 표현이다. 원본 계산 결과는 보존했다.

## 주장별 정정

| 기존 주장 | 확인된 근거와 정정 |
|---|---|
| CPU가 오늘 밤 반드시 완전 종료 | 18시대 확인시 217개 완료, 218번 실행. ETA는 조건부 추정이며 확정 시간이 아니다. |
| CPU 중단·재시작 0건 | `/home/aol/pc2_supervisor_cpu.log`에 9월 23일 23:02:17, 24일 00:54:13·00:56:28 restart OK 기록. 최종 성공 개수로 중간 이력을 지울 수 없다. 이것만으로 모든 개별 job이 실패했다고 단정하지도 않는다. |
| 220개 완료면 포논 물성 전체 종결 | force 생성 뒤 재사용 98개 출처, IFC 조립·순서·의사퍼텐셜·ASR/drift, cutoff·supercell·q-grid·NAC·RTA/LBTE 검증이 남는다. |
| 144원자 과거 중단은 Windows/메모리 충돌로 확정 | 옛 출력의 미완료는 확인했으나 당시 OS 사건과 연결되는 근거가 부족하다. 원인 확정은 철회한다. |
| sleep infinity가 중단을 원천 차단 | 재부팅·WSL 종료·OOM·I/O 실패를 막지 못한다. 이번 정밀 SCF 최초 systemd 실행도 18:34:08 시스템 종료 과정에서 중지된 로그를 직접 확인했다. 이는 이번 사건의 근거이며 과거 사건까지 소급 입증하지 않는다. |
| 72원자는 13:22부터 성공 실행 | launch_20260928_1326.log에는 mpirun Killed가 있고, live_status_72_restart.txt에는 중복 정리·새 scratch 실행 기록이 있다. 실제 완료본의 실행 로그는 13:59:31→16:25:37이다. 단순 경로/CRLF 수정만으로 설명하면 누락이다. |
| 두 slab 모두 완전 검증 | 144/72원자 모두 BFGS·최종좌표·이동 힘 기준은 통과했으나 SCF force 경고가 있다. 72원자 종료에는 IEEE invalid/divide-by-zero 경고도 있다. 경고만으로 NaN 결과라고 단정하지 않고 정밀 SCF로 대조한다. |
| 72원자 완료로 흡착 4종 즉시 실행 가능 | 흡착은 Al125+N1=126원자, clean parent는 125원자이며 72원자 셀과 다르다. 해당 parent/ontop 출력은 초기화 단계 기록만 존재한다. |
| 4개 흡착 작업 모두 미실행 | clean parent와 ontop은 실제 초기화 출력이 있다. 완료 아님과 실행 이력 없음은 다르다. |

## 실제 수정 및 재개

- `audit_and_collect.py`: 경고 없는 정상 relax까지 NEEDS_REVIEW로 보내던 분기 수정. IEEE invalid/divide-by-zero 경고를 명시적으로 기록. 회귀 테스트 2개가 수정 전 실패하고 수정 후 통과했다.
- 기존 `run_al111_72at_relax.sh`, `run_nitridation_adsorption_queue.sh`는 `.before_20260930_audit`로 보존하고 잘못된 자동 resume/완료 판정을 사용하는 실행 경로를 exit 78로 차단했다. 이는 새 생산용 흡착 실행기를 완성했다는 의미가 아니다.
- WSL의 `/home/aol2/campaign_144at_gpu/run_dual_gpu.sh`와 문법·환경변수 구성이 깨진 `/home/aol2/run_qe_gpu_2gpu.sh`도 동일하게 원본 백업 후 차단했다. 현재 독립 SCF 큐는 이 두 진입점을 사용하지 않는다.
- `prepare_scf_rechecks.py`로 AlN144/Al72 최종 좌표·원자 순서·고정 mask를 보존한 별도 SCF 입력을 생성했다. cutoff, k-grid, smearing, 셀 및 pseudo를 유지하고 conv_thr를 1e-10 Ry로 강화했다. 기존 wavefunction/BFGS scratch를 재사용하지 않는다. 입력과 원본, pseudo 해시는 각 provenance.json에 기록한다.
- `repair_scf_queue.sh`: 실제 존재하는 workspace GPU 래퍼, NVHPC 경로, np=2/nk=1, OMP=1, 큐 잠금, 기존 pw.x 검사, 기존 출력 보호, exit code 기록. 두 독립 SCF만 순차 실행하며 흡착/IFC/MD로 자동 연결하지 않는다. nk=1은 메모리 분산을 위한 실행 설정이며 물리 입력 변경이 아니다.
- 처음 분리한 background shell은 실행 로그를 만들지 못했다. 이후 systemd 작업은 시작됐지만 WSL 종료로 중단됐다. 해당 부분 출력·scratch는 `repair_20260930/AlN144_tight/interrupted_systemd_attempt/`에 보존했다. 이후 숨김 Windows wsl.exe(PID는 windows_wsl_pid.txt)를 전경 bash 실행 종료까지 유지하도록 재개했다. Windows/WSL 강제 종료에도 절대 끊기지 않는다고 보장하지 않는다.
- 18:38 전후 확인: Windows wsl.exe 생존, AlN144 QE 두 rank 생존, GPU 메모리 약 24.1 GB/장 및 GPU 사용 확인. 아직 SCF 결과 검증 완료가 아니다. Al72는 다음 독립 검사로 대기한다.
- 후속 확인에서 `Self-consistent Calculation`, `iteration # 1` 진입과 두 pw.x rank 생존을 확인했다. 단순히 런처가 반환한 exit 0을 계산 성공으로 간주하지 않았다.
- `verify_scf_rechecks.py`는 실제 exit code, SCF·힘, 기존/새 힘 차이, 움직이는 성분 기준, stderr IEEE 경고를 검사한다. 결과는 diagnostic으로 유지하고 물리 수렴/발표 인증으로 승격하지 않는다.
- 기존 `aln-fc3` 자동화 한 개를 GPU 검사까지 포함하도록 수정했다. 새 자동화는 만들지 않았다. CPU와 GPU 결과 수집을 모두 마친 후 중지하며, 정상 미완료·동일 해시는 반복 보고하지 않는다.

CPU의 현재 정상 실행 루프는 중단·교체하지 않았다. 그 루프의 JOB DONE 기반 성공 표시는 원자료 감사와 구별한다. 잘못된 자동 종료/체크포인트 재사용 로직을 가진 나머지 과거 진입점은 안전한 생산 실행기로 인증되지 않았으므로 사용하지 않는다.

## Exa로 확인한 부족한 입증

Exa 검색 3개 축(검색 결과 8건)과 관련 원문을 활용했다. Exa 검색 결과 자체를 물리 인증으로 취급하지 않았다.

1. [QE 입력 문서](https://www.quantum-espresso.org/Doc/INPUT_PW.html): restart는 동일 병렬 구성과 정상 중단을 전제로 한다. 파일 존재만으로 restart를 선택하지 않는다. 전자 수렴, 이온 수렴, 프로세스 종료는 각각 검사해야 한다.
2. [QE 문제 해결](https://www.quantum-espresso.org/Doc/pw_user_guide/node21.html): CRLF는 가능한 입력 문제이나 특정 실패 원인은 로그로 입증해야 한다. 메모리는 k-point pool만 늘려 해결되지 않는다. 실제 125/126원자 출력의 예상 총 RAM은 약 86.82/87.35 GB다. 이 수치를 GPU VRAM 요구량과 동일시할 수는 없지만 24GB 두 장을 하나의 48GB 공간처럼 가정해서도 안 된다.
3. [phono3py cutoff](https://phonopy.github.io/phono3py/cutoff-pair.html), [설정 문서](https://phonopy.github.io/phono3py/command-options.html): cutoff-pair는 정확도 손실을 수반할 수 있다. 특수 displacement YAML 보존, 대응 force 순서, cutoff 민감도와 supercell/q-grid 수렴이 필요하다. cutoff-pair와 cutoff-fc3를 동일한 연산으로 취급하지 않는다.
4. [LAMMPS 열전도도](https://docs.lammps.org/stable/Howto_kappa.html), [heat/flux](https://docs.lammps.org/compute_heat_flux.html): NEMD는 열원/열싱크 에너지 수지와 온도 구배, GK는 평형 열유속 상관함수·적분·부피/단위 검증이 필요하다. 현재 자료에 실제 MD 궤적과 이 검증이 없으므로 MD 완료 주장은 보류한다. 포텐셜의 실제 계면 적용성, 시간·크기·seed 반복도 별도 필요하다.

흡착 생산 계산 전에는 동일 125원자 기준 셀의 이완·수렴, 진공/두께/k-grid/cutoff/smearing, 비대칭 slab dipole 조건, N 원자/N2 기준 및 spin, 흡착 위치와 최소 원자간 거리, 실제 메모리 측정을 해결한다. 180원자·결함108원자·MD를 GPU 유휴라는 이유만으로 동시에 시작하지 않는다.

## 남은 범위

두 정밀 SCF 완료와 힘 대조는 진행 중이다. 98개 force provenance, FC3 물리 수렴, 125원자 계면 입력 및 메모리 검증, MD 포텐셜·궤적 검증은 미완료다. 전체 계산화학 연구 완료일은 아직 확정할 수 없다. 향후 pypolymlp/symfc 활용은 비교 후보이며 현재 220개를 자동으로 범용 MLIP 데이터로 간주하지 않는다.

JEV: 이번에도 Process/User/Machine TYPESAFE_API_KEY 없음. 공식 콘솔 로그인 흐름은 사용자가 진행 중이나 API 인증 성공 근거가 없어 미적용. 실제 세션 모델 설정 변경 없음.

절약 프롬프트: “종료 코드와 변경된 출력 해시만 먼저 확인하고, 새 완료 job만 원자료 검증하라. 전자·이온·물리 수렴을 분리하고 경고가 남은 작업을 자동으로 다음 생산 큐에 넘기지 말라.”
