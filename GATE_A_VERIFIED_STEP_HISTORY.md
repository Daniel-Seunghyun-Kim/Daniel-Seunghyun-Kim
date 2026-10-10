# Gate A (144-atom AlN Slab) 전수 스텝 이완 히스토리 감사 보고서
**작성일**: 2026-09-24 07:28 KST  
**검증 대상 원본 파일**: WSL2 `Ubuntu-24.04` `/home/aol2/campaign_144at_gpu/pw.out` (총 24,000+ 라인 전수 분석)  
**체크포인트 파일**: `/home/aol2/campaign_144at_gpu/scratch/aln_002_sc.bfgs` (5.1 MB), `charge-density.dat` (149 MB)  
**결론 요약**: **초기화(From scratch)된 적이 전혀 없으며, 9월 8일 첫 시작 이후 현재까지 모든 스텝의 원자 좌표, 에너지, 힘이 100% 누적 보존되어 Step 8에서 이어서 가동 중입니다.**

---

## 1. 전수 스텝별 수렴 내역 (Step 0 ~ 현재 진행 중)

| BFGS Step | 라인 번호 (pw.out) | 원자간 최대 잔여 힘 (`Total force`) | SCF 보정량 (`SCF correction`) | 총에너지 (`Total Energy`) | 완료/진행 일자 | 상태 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Step 0** | Line 4,185 | **`0.093456 Ry/au`** | 0.000149 Ry/au | -4885.232184 Ry | 2026-09-08 21:17 (최초 착수) | **완료** |
| **Step 1** | Line 6,369 | **`0.041163 Ry/au`** | 0.000183 Ry/au | -4885.238340 Ry | 2026-09-11 07:48 | **완료** |
| **Step 2** | Line 8,575 | **`0.021328 Ry/au`** | 0.000100 Ry/au | -4885.240150 Ry | 2026-09-13 15:30 | **완료** |
| **Step 3** | Line 10,508 | **`0.019144 Ry/au`** | 0.000056 Ry/au | -4885.240652 Ry | 2026-09-16 19:11 | **완료** |
| **Step 4** | Line 13,456 | **`0.016312 Ry/au`** | 0.000124 Ry/au | -4885.241162 Ry | 2026-09-17 22:15 | **완료** |
| **Step 5** | Line 15,473 | **`0.014855 Ry/au`** | 0.000061 Ry/au | -4885.241769 Ry | 2026-09-18 20:40 | **완료** |
| **Step 6** | Line 17,810 | **`0.017849 Ry/au`** | 0.000134 Ry/au | -4885.242370 Ry | 2026-09-20 18:22 | **완료** |
| **Step 7** | Line 19,848 | **`0.017833 Ry/au`** | 0.000115 Ry/au | -4885.242778 Ry | 2026-09-21 17:05 | **완료** |
| **Step 8** | Line 21,970 | **`0.013377 Ry/au`** | 0.000119 Ry/au | -4885.243284 Ry | 2026-09-22 19:10 (크래시 직전) | **완료** |
| **Step 9 (현)** | Line 23,865~ | *계산 중 (수렴 시 출력)* | *계산 중* | **`-4885.243876 Ry`** | **2026-09-24 07:28 (현재 가동 중)** | **진행 중 (Iter #20)** |

> [!NOTE]
> `0.093456 Ry/au`는 9월 8일 21:17 첫 실행 시의 초기 구조(Step 0)에서만 딱 한 번 측정된 값이며, 이후 재부팅이나 재개 시 다시 나타난 적이 단 한 번도 없습니다.

---

## 2. 9월 24일 재개 시 체크포인트 복구 로그 실측 증거

9월 24일 00:56에 재개될 당시 Quantum ESPRESSO가 화면과 로그(`pw.out` 23865~23875 라인)에 출력한 실제 문자열입니다:

```text
     Atomic positions and unit cell read from directory:
     /home/aol2/campaign_144at_gpu/scratch/aln_002_sc.save/
     Atomic positions from file used, from input discarded
 
     The initial density is read from file :
     /home/aol2/campaign_144at_gpu/scratch/aln_002_sc.save/charge-density
```

- **`Atomic positions from file used, from input discarded`**: 입력 파일의 초기 원자 좌표는 완전히 버리고(`discarded`), 디스크에 저장되어 있던 **Step 8의 이완된 원자 좌표를 그대로 읽어들여 복구**했습니다.
- **`The initial density is read from file: charge-density`**: 처음부터 전하 밀도를 계산한 것이 아니라, **Step 8에서 수렴된 149 MB짜리 전자 밀도를 그대로 이어받았습니다.**

---

## 3. 원시 데이터 파일 링크
- CSV 전체 내역: [GATE_A_VERIFIED_STEP_HISTORY.csv](file:///c:/Users/AOL/Desktop/SH.Kim/GATE_A_VERIFIED_STEP_HISTORY.csv)
- 원본 로그 파일: `/home/aol2/campaign_144at_gpu/pw.out`
- 이완 히스토리 헤시안 파일: `/home/aol2/campaign_144at_gpu/scratch/aln_002_sc.bfgs`
