# Step A3: DFT 입력 덱 구성 가이드 (DFT Deck Configuration Guide)

**솔버**: Quantum ESPRESSO v7.2 (NVIDIA HPC SDK 25.3 GPU 가속 빌드 `pw.x`)  
**기저 구조**: 125원자 완결 수렴 Al(111) 모체 슬랩 좌표  
**작성일**: 2026-10-10 (Asia/Seoul)

---

## 1. 4대 흡착 사이트 좌표 생성 규격

Al(111) 표면 최상층 원자간 거리 $d_{\text{Al-Al}} \approx 2.856\ \text{Å}$ 기준, 질소 원자(N)의 초기 수직 높이($z$)는 파울링 반경을 고려하여 표면 위 약 $1.20 \sim 1.85\ \text{Å}$에 배치합니다.

1. **`ontop` (1-fold Coordination)**:
   - 최상층 특정 Al 원자 바로 위 ($x_0, y_0, z_0 + 1.85\ \text{Å}$)
   - 배위수: 1 (Al-N 단일 결합)
2. **`bridge` (2-fold Coordination)**:
   - 인접한 두 Al 원자의 정중앙 ($x_{\text{mid}}, y_{\text{mid}}, z_{\text{surf}} + 1.45\ \text{Å}$)
   - 배위수: 2 (Al-N-Al 브릿지 결합)
3. **`fcc hollow` (3-fold Coordination, Pseudo Bulk Stacking)**:
   - 최상층 Al 3원자가 이루는 삼각형 중심, 2층 Al 원자가 없는 3층 정렬 자리 ($x_{\text{fcc}}, y_{\text{fcc}}, z_{\text{surf}} + 1.25\ \text{Å}$)
   - 배위수: 3
4. **`hcp hollow` (3-fold Coordination, Faulted Stacking)**:
   - 최상층 Al 3원자가 이루는 삼각형 중심 중, 바로 아래 2층 Al 원자가 직하방에 위치하는 자리 ($x_{\text{hcp}}, y_{\text{hcp}}, z_{\text{surf}} + 1.25\ \text{Å}$)
   - 배위수: 3

---

## 2. 수렴 가속 및 전하 진동(Sloshing) 방지 파라미터 표준

모체 슬랩 계산에서 입증된 자율 복구 파라미터를 초기 덱에 전면 적용합니다:

```fortran
&CONTROL
    calculation   = 'relax'
    restart_mode  = 'from_scratch'
    prefix        = 'Al125_N_adsorption'
    outdir        = './scratch'
    pseudo_dir    = '/home/aol2/qe_gpu_builds/pseudo'
    nstep         = 100
    tprnfor       = .true.
    tstress       = .true.
    etot_conv_thr = 1.0D-5
    forc_conv_thr = 1.0D-4
/
&SYSTEM
    ibrav       = 0
    nat         = 126
    ntyp        = 2
    ecutwfc     = 55.0
    ecutrho     = 450.0
    occupations = 'smearing'
    smearing    = 'marzari-vanderbilt'
    degauss     = 0.01
/
&ELECTRONS
    conv_thr         = 1.0D-6
    electron_maxstep = 150
    mixing_mode      = 'plain'
    mixing_beta      = 0.05       ! 핵심: 0.2 대신 0.05로 전하 진동 원천 차단
    diagonalization  = 'cg'          ! 대형 시스템 안정적 CG 대각화
/
&IONS
    ion_dynamics = 'bfgs'
    bfgs_ndim    = 1
    trust_radius_max = 0.5
    trust_radius_min = 1.0D-4
/
ATOMIC_SPECIES
  Al  26.981538  Al.pbe-n-kjpaw_psl.1.0.0.UPF
  N   14.0067    N.pbe-n-kjpaw_psl.1.0.0.UPF
```

---

## 3. 원자 위치 고정 규격 (Selective Dynamics)
- 하부 2개 층 (50개 Al 원자): `0 0 0` 고정 (벌크 특성 유지)
- 상부 3개 층 (75개 Al 원자): `1 1 1` 자유 이완 (계면 변형 흡수)
- 흡착 N 원자 (1개 원자): `1 1 1` 자유 이완
