# Ubuntu CPU/GPU 병렬 실행 진단

점검: 2026-08-31, WSL2 Ubuntu-24.04, 사용자 nano.

## 결론

CPU/GPU 하드웨어 전체가 고장 난 상황이라는 증거는 없다. 기존 설치본 선택과 런타임 라이브러리 연결에 문제가 확인됐다. 첨부는 설정 파일이 아니라 2,516개 메시지의 세션 내보내기이며, 그 안의 지시나 성공 주장은 검증된 설정으로 취급하면 안 된다. 적용 전후 상태 전체가 없으므로 첨부 적용이 모든 장애를 새로 만들었다는 인과관계까지 확정할 수는 없다.

시스템 설정, 설치본, 연구 입력 및 결과를 변경하지 않았다. 환경 변수 비교는 진단 자식 프로세스에만 적용했다. 실제 SCF/relax/MD 계산은 실행하지 않았다. QE에는 빈 입력만 제공하여 초기화 경계를 확인했고, LAMMPS에는 -h를 사용했다.

## 확인 결과

| 항목 | 실제 관찰 | 판단 범위 |
|---|---|---|
| CPU | nproc=24; mpirun -np 2 hostname 두 프로세스 실행, 반환 코드 0 | MPI 프로세스 기동 성공. 계산 정확도나 성능 검증은 아님 |
| GPU | RTX 4070 Ti, VRAM 12282 MiB, Windows driver 581.29 인식 | 장치 인식 성공. 계산 성공은 아님 |
| 메모리 | WSL 약 23 GiB, swap 32 GiB; .wslconfig memory=24GB | 무거운 계산의 별도 메모리 한계는 남음 |
| 시스템 QE | /usr/bin/pw.x, apt quantum-espresso 6.7-2build4 | 기존 QE_first_run.log에서 MPI 4개 기동 후 buffer overflow / SIGABRT |
| 기존 CPU QE | /home/nano/.local/qe-7.2-openmpi/bin/pw.x, v7.2 | MPI 2개 초기화 후 의도한 빈 입력 오류, 반환 코드 1. 정상 계산 완료 아님 |
| 기존 GPU QE | /home/nano/qe_gpu_builds/qe-7.2-rtx4070ti-sm89/bin/pw.x | CUDA/NVHPC 라이브러리가 연결되어 있음. 기본 실행은 MPI 초기화 실패 |
| GPU QE MPI 경로 | 존재하지 않는 /proj/nv/... 경로의 도움말 및 실행 구성요소를 찾음 | NVHPC MPI 설치 prefix 연결 문제 |
| GPU QE 경로 보정 비교 | 자식 프로세스 OPAL_PREFIX와 해당 MPI mpirun --prefix 적용 | 원래 MPI 경로 오류 대신 libgomp: TODO, 반환 코드 1. 아직 미해결 |
| LAMMPS 기본 실행 | GPU 설치 폴더의 lmp가 /lib/x86_64-linux-gnu/liblammps.so.0 로딩 | 2024 버전 / OPENMP, GPU package 없음 |
| LAMMPS 라이브러리 지정 비교 | 자식 프로세스 LD_LIBRARY_PATH=/home/nano/lammps_gpu_install/lib | 2025 버전 / GPU package API: CUDA / Compatible GPU present: yes, 도움말 반환 코드 0 |

GPU QE의 libgomp: TODO는 GNU OpenMP/OpenACC와 NVIDIA 런타임의 심볼 충돌이 의심된다. 실제 ldd에 libgomp와 libnvomp/libacc 계열이 함께 있고 CMakeCache가 시스템 libfftw3_omp를 선택한다. 단, 이것만으로 정확한 호출 심볼이나 최종 해결책을 확정하지 않았다. NVIDIA 기술 포럼에도 유사 런타임 심볼 문제 설명이 있다: https://forums.developer.nvidia.com/t/problem-with-nvfortran-and-r/155366

LAMMPS는 라이브러리 탐색 경로만 바꾼 비교에서 GPU 기능 노출이 회복됐다. 다만 이 GPU 설치본의 패키지는 GPU/KSPACE/MOLECULE이므로, 기존 연구 입력에서 요구하는 다른 패키지나 potential style까지 제공한다고 볼 수 없다. 공식 라이브러리 연결 문서: https://docs.lammps.org/Build_link.html

## 첨부 기록에서 바로잡을 내용

- 메시지 5543/5549 등은 /usr/bin/pw.x를 고정 호출하여 이미 존재하는 QE 7.2 설치본을 사용하지 않았다. 현재 로그인 셸에서는 pw.x가 /home/nano/.local/bin/pw.x -> CPU QE 7.2를 가리킨다. 비로그인/초기화 없는 셸에서는 /usr/bin/pw.x가 선택되어 실행 환경에 따라 버전이 달라진다.
- 기존 QE_first_run.log는 'Parallel version (MPI), running on 4 processors'를 명시한다. 따라서 'CPU 병렬 기능 자체가 없다' 또는 'serial-only'라는 설명은 맞지 않는다.
- 기존 buffer overflow / __snprintf_chk / SIGABRT는 실제 로그에 있다. 그러나 이것만으로 glibc가 유일한 원인이라고 단정하거나 보안 검사를 끄는 것이 유일한 해결이라고 말할 수 없다.
- setarch -R은 ASLR 제어이며 FORTIFY를 끄는 명령이 아니다. hostname을 아키텍처 인자로 넘긴 것은 잘못된 명령이다.
- 첨부의 'Aborted'와 'QC_EXIT=0'는 서로 모순된다. 여러 셸을 거치는 변수 확장과 마지막 cat의 종료 코드로 실패가 가려지는 문제가 있다. 실제 /home/nano/qe_probe.sh에도 p= 및 빈 변수 자리로 훼손된 점검 코드가 남아 있다. 이번 증거 파일은 Python subprocess가 직접 수집한 반환 코드를 사용한다.
- /usr/bin/pw.x만 검사해 'GPU QE가 없다'고 결론 내린 것은 설치 목록 누락이다. 별도 CUDA/NVHPC QE 실행 파일이 실제 존재한다.
- 'GPU 사용률 13%이므로 대기이며 이전 GPU 계산은 착각'이라는 설명은 근거가 부족하다. 이번 점검으로 과거 GPU 계산 결과의 유효성을 판정하지 않았다.
- 현재 /usr/bin/nvcc는 CUDA 12.0이며 /usr/local/cuda는 없다. GPU QE는 별도 홈 디렉터리의 NVHPC CUDA 12.8 라이브러리에 연결되어 있다. 하나의 CUDA 버전으로 전체 환경을 설명하면 안 된다.

## 후속 복구 순서

1. 기존 설치를 보존하고 CPU QE, GPU QE, LAMMPS별 실행기와 라이브러리 환경을 분리한다. 전역 .bashrc나 LD_LIBRARY_PATH를 일괄 변경하지 않는다.
2. CPU QE는 기존 7.2와 시스템 OpenMPI 조합을 우선 사용하되, 승인된 작은 실제 입력의 별도 scratch에서 수렴 및 반환 코드를 확인한다.
3. LAMMPS는 검증한 전용 라이브러리 경로를 실행기 안으로 한정하고, 연구 입력에 필요한 package/potential 지원부터 확인한다. 그 후 CPU/GPU 동일 입력 비교를 한다.
4. GPU QE는 NVHPC MPI prefix와 libgomp 충돌을 해결한 뒤 GPU 초기화 및 작은 실제 계산을 검증한다. 재빌드가 필요하면 기존 빌드를 덮어쓰지 않는 별도 위치에서 진행한다. FORTIFY 비활성화부터 시작하지 않는다.

현재 상태는 '원인 분리 및 일부 초기화 확인'이다. CPU/GPU 계산 정상화 완료 또는 과학적 결과 PASS가 아니다.

원시 증거: parallel_diagnostic_evidence.json
