현재 확인 가능한 기준은 `Node 2`뿐입니다. 이 머신에서는 `COMSOL 6.2`, `COMSOL+MATLAB`, `COMSOL+Simulink`, `BIOVIA Materials Studio`, `Blender`, `VASP`, `Quantum ESPRESSO`, `Phono3py`, `ShengBTE`, `LAMMPS`, `MATLAB`, `Java`가 잡혀 있습니다([tooling_status.json](/C:/Users/effec/Downloads/Automation/outputs/simulations/tooling_status.json), [thermal_research_pipeline_manifest.json](/C:/Users/effec/Downloads/Automation/outputs/simulations/thermal_research_pipeline_manifest.json)). 하드웨어 기준 역할은 이미 [`research-program.json`](/C:/Users/effec/Downloads/Automation/automation/config/research-program.json) 에 이렇게 잡혀 있습니다: Node 1은 `GPU-accelerated MD / visualization`, Node 2는 `post-processing / unit-cell optimization / prototyping`, Node 3은 `main DFT / phonon / large convergence`입니다.

**노드별로 어디까지 맡기는 게 맞는가**
- `Node 2`에서 바로 가능한 것
  - 구조 전처리: unit cell 정리, slab/supercell 생성, vacuum/Selective Dynamics 설정
  - 입력 파일 생성: `POSCAR/INCAR/KPOINTS/POTCAR` 준비, LAMMPS data/input 생성, Materials Studio 기반 초기 구조 정리
  - 소규모 파일럿 계산: 작은 bulk/primitive cell 최적화, 낮은 k-mesh 테스트, 짧은 single-point, 작은 DOS dry run
  - MD 파일럿: 원자 겹침 점검, 짧은 equilibration, 작은 NEMD/VACF 테스트
  - COMSOL/Blender: geometry, deck, contour, GIF, 보고서, 이미지 후처리
  - MATLAB/Simulink 후처리
- `Node 3`로 보내야 하는 것
  - AlN-AlN direct bonding의 본 계산: 여러 termination/registry/slab 두께를 포함한 `W_sep`, charge redistribution
  - OH termination 비교 세트
  - Berry phase `Ps`, Born effective charge, double-well energy landscape
  - 고정밀 DOS/band-related runs
  - phonon dispersion, IFC, Phono3py/ShengBTE 기반 BTE
  - 큰 convergence sweep
- `Node 1`로 보내야 하는 것
  - 큰 MD: roughness 포함 pull-off, `>10^5` atoms 급 adhesion/pull-off
  - large-scale `NEMD/EMD/VACF`
  - ReaxFF 또는 ML-IP 학습/추론을 쓰는 경우
  - Blender 대량 렌더링
- 보조 판단
  - `Node 2`는 “초기 설정 + 파일럿 + 후처리”에는 충분합니다.
  - `Node 2`의 32 GB 메모리는 production DFT와 큰 MD에서 병목이 됩니다.
  - `Node 3`는 CPU/메모리형 DFT에 가장 적합합니다.
  - `Node 1`은 GPU 이점이 있는 MD/시각화에 가장 적합합니다.

**사용자 항목별 권장 배치**
- `AlN-AlN 원본 접착성`, `OH termination 효과`
  - 시작: Node 2
  - 본 계산: Node 3
- `Berry phase`, `Z*`, `double-well`, `DOS`
  - 시작: Node 2
  - 본 계산: Node 3
- `BTE`, `phonon dispersion`, `vDOS(DFT 계열)`
  - 시작: Node 2
  - 본 계산: Node 3
- `MD pull-off`
  - 시작: Node 2
  - 본 계산: Node 1
- `MD VACF / NEMD / EMD`
  - 시작: Node 2
  - 본 계산: Node 1
- `COMSOL / Blender / GIF / 이미지 적용`
  - 주 노드: Node 2
  - Blender 대량 렌더만 Node 1 선택 가능

**다른 노드에 필요한 설치**
- `Node 1` 필수
  - VASP: 이미 설치됨
  - LAMMPS
  - Python 3 scientific stack: `numpy`, `scipy`, `pandas`, `matplotlib`
  - MD/atomistic 유틸: `ase`, `pymatgen`
  - WSL Ubuntu 또는 Linux 실행 환경
  - Blender
- `Node 1` 권장
  - Materials Studio Server 또는 동일한 구조 준비 도구
  - COMSOL: 이 노드에서도 직접 contour/export를 돌릴 계획이 있을 때만
  - CUDA/KOKKOS 지원 LAMMPS 빌드: GPU MD를 실제로 쓸 경우
- `Node 3` 필수
  - VASP: 이미 설치됨
  - Quantum ESPRESSO
  - Phono3py
  - ShengBTE
  - Python 3 scientific stack
  - `phonopy`, `spglib` 계열 의존성
  - WSL 또는 Linux 실행 환경
- `Node 3` 권장
  - `ase`, `pymatgen` for slab/charge-density post-processing
  - Bader analysis tool: charge redistribution를 정량화할 경우
- `Node 2`
  - 이미 현재 자동화 기준 핵심 툴은 준비된 상태입니다([tooling_status.json](/C:/Users/effec/Downloads/Automation/outputs/simulations/tooling_status.json)).

실무적으로는 이렇게 가는 게 가장 효율적입니다.
1. Node 2에서 구조/입력/파일럿/COMSOL-Blender 후처리
2. Node 3에서 production DFT/BTE
3. Node 1에서 production MD와 대형 렌더링

중요한 점 하나는, 지금 자동화는 `Node 2에서 체인 준비`는 가능하지만 `다른 노드로 job dispatch`까지는 아직 자동으로 분리되어 있지 않다는 점입니다. 다음 단계는 `Node 2에서 deck 생성 -> Node 1/3 전송용 run profile 분리`를 넣는 것입니다. 원하면 바로 그 설계까지 이어서 정리하겠습니다.