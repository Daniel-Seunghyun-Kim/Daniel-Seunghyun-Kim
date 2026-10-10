# 공공 API & 오픈소스 도구 전략
## 논문 조사 + 시뮬레이션 무료/저비용 실행

작성일: 2026-09-25  
목표: **비용 절약형** + **고품질** 실행 가능한 도구 모음

---

## Part 1: 논문 조사 공공 API

### 1-1. 무료 학술 논문 검색

#### 1) PubMed Central (PMC) API
```
용도: 반도체 재료과학, 열관리 논문 검색
URL: https://www.ncbi.nlm.nih.gov/research/biopython/
API: RESTful (무료)
사용량: 무제한
특징:
  ✓ 10M+ 논문 DB (full text)
  ✓ 한국 저널도 포함
  ✓ 인용도 추출 가능
  
예시:
  GET https://www.ncbi.nlm.nih.gov/pmc/utils/oa/oa.fcgi?id=PMC3879371
  
결과: XML → 제목, 초록, 키워드, 저자
```

#### 2) arXiv API
```
용도: 반도체 물리, 나노재료, 시뮬레이션 preprint
URL: https://arxiv.org/help/api
API: RESTful (무료)
특징:
  ✓ Physics (cond-mat, materials)
  ✓ 전 세계 최신 preprint
  ✓ JSON 응답
  
예시:
  GET http://export.arxiv.org/api/query?search_query=
       ti:aluminum+nitride+thermal&start=0&max_results=100
```

#### 3) Semantic Scholar API (무료)
```
용도: 인용도, 관련 논문 네트워크
URL: https://www.semanticscholar.org/product/api
API: RESTful (무료, 학술용)
특징:
  ✓ 인공지능 기반 유사 논문 추천
  ✓ 인용 네트워크 시각화
  ✓ JSON 응답
  
예시:
  GET https://api.semanticscholar.org/graph/v1/paper/
       arXiv:1234.5678?fields=title,authors,citationCount
```

#### 4) CORE API
```
용도: OA(open access) 논문 full text 검색
URL: https://core.ac.uk/services/api
API: RESTful (무료 / 유료 업그레이드)
특징:
  ✓ 150M+ 논문 DB
  ✓ Full text 검색 가능
  ✓ Korea 저널 포함
```

#### 5) CrossRef API
```
용도: DOI 기반 논문 메타데이터 검색
URL: https://www.crossref.org/services/metadata-retrieval/
API: RESTful (무료)
특징:
  ✓ DOI → BibTeX 변환
  ✓ 저자, 피인용수, 출판일
  
예시:
  GET https://api.crossref.org/works/10.1038/nature12373
```

#### 6) SSRN eLibrary (Social Science Research Network)
```
용도: 학술 preprint & 워킹 페이퍼
URL: https://papers.ssrn.com/
API: 웹 스크래핑 (selenium)
특징:
  ✓ Thermal management papers
  ✓ 저자 협력 네트워크
```

#### 7) Google Scholar (간접)
```
주의: 공식 API 없음 (이용약관 위반 위험)
대안: Scholarly 라이브러리 (Python)
  pip install scholarly
  
사용:
  from scholarly import scholarly
  search = scholarly.search_pubs("aluminum nitride thermal")
```

### 1-2. 논문 조사용 Python 스크립트

#### 통합 검색 스크립트
```python
#!/usr/bin/env python3
# 논문 자동 검색 & 메타데이터 추출

import requests
import json
from datetime import datetime

# 설정
keywords = [
    "aluminum nitride thin film bonding",
    "thermal boundary conductance direct bonding",
    "thermal cycling reliability silicon",
    "microchannel cooling chiplet"
]

def search_arxiv(query, max_results=50):
    """arXiv에서 논문 검색"""
    base_url = "http://export.arxiv.org/api/query?"
    search_query = f"search_query=ti:{query}&start=0&max_results={max_results}"
    
    response = requests.get(base_url + search_query)
    return response.text  # XML 파싱 필요

def search_semantic_scholar(query, max_results=100):
    """Semantic Scholar에서 인용도 높은 논문 검색"""
    url = "https://api.semanticscholar.org/graph/v1/paper/search"
    params = {
        "query": query,
        "limit": max_results,
        "fields": "title,authors,citationCount,year,venue"
    }
    
    response = requests.get(url, params=params)
    return response.json()

def search_crossref(query, max_results=100):
    """CrossRef에서 DOI 기반 검색"""
    url = "https://api.crossref.org/works"
    params = {
        "query": query,
        "rows": max_results
    }
    
    response = requests.get(url, params=params)
    return response.json()

def main():
    print("📚 논문 자동 검색 시작\n")
    
    results = {}
    
    for keyword in keywords:
        print(f"🔍 검색: {keyword}")
        
        # Semantic Scholar (인용도 기반)
        try:
            sem_results = search_semantic_scholar(keyword, max_results=20)
            results[keyword] = {
                "semantic_scholar": sem_results,
                "timestamp": datetime.now().isoformat()
            }
            print(f"  ✓ Semantic Scholar: {len(sem_results.get('data', []))} papers found")
        except Exception as e:
            print(f"  ✗ Semantic Scholar error: {e}")
        
        print()
    
    # 결과 저장
    with open("paper_search_results.json", "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    
    print("✓ 결과 저장: paper_search_results.json")

if __name__ == "__main__":
    main()
```

---

## Part 2: 시뮬레이션 오픈소스 도구

### 2-1. COMSOL 대체 (무료 + 오픈소스)

#### 1) FEniCS / Firedrake (유한요소법)
```
용도: 열전도, 응력 분석 (COMSOL 기능의 80%)
라이선스: LGPL (무료, 오픈소스)
설치: pip install fenics 또는 docker
장점:
  ✓ 완전 무료
  ✓ Python 기반 (학습 쉬움)
  ✓ HPC 병렬화 지원
  ✓ COMSOL보다 빠른 속도 (GPU 지원)
  
예시:
  from dolfin import *
  
  # 열전도 방정식 풀이
  mesh = RectangleMesh(Point(0, 0), Point(1, 1), 100, 100)
  V = FunctionSpace(mesh, "P", 1)
  u_trial, u_test = TrialFunction(V), TestFunction(V)
  
  # Boundary conditions, 등차 방정식 정의
  # solve()
```

**비용**: **$0** (vs COMSOL $3,000–5,000/년)

#### 2) Elmer
```
용도: 다중물리 (열-유동-구조 coupling)
라이선스: LGPL (무료)
특징:
  ✓ Multi-physics coupling
  ✓ ParaView로 시각화
  ✓ HPC 지원
  
사용:
  ElmerGUI (GUI) 또는 명령행
```

#### 3) Calculix
```
용도: 구조 해석 (응력, 변형)
라이선스: LGPL (무료)
특징:
  ✓ ABAQUS 호환 입력
  ✓ Pre/post: FreeCAD + Salome
```

#### 최고 추천: **FEniCS** (우리 경우)
```
이유:
  1. COMSOL의 80% 기능
  2. 완전 무료
  3. 연구 논문 기여도 높음
  4. Python 기반 (분석 스크립트와 통합 용이)
  5. GPU 가속 (NVIDIA Tesla K80 → 100배 빠름)

예상 비용 절감: COMSOL 라이선스 제거 (매년 300만 원+)
```

### 2-2. OpenFOAM (CFD)

#### OpenFOAM v2206+ (무료, 오픈소스)
```
용도: 유동 (single-phase, multi-phase boiling)
라이선스: GPL3 (완전 무료)
설치: apt-get install openfoam11 (Linux)
또는 Docker: docker pull openfoam/openfoam

특징:
  ✓ 산업 표준 CFD (ANSYS Fluent 대체)
  ✓ 완전 무료
  ✓ Multi-phase 지원 (VOF, Eulerian)
  ✓ HPC 병렬화
  ✓ 2-phase boiling 가능

Python 인터페이스:
  pip install pythonFoam
  
비용: **$0** (vs ANSYS Fluent $10,000+/년)
```

#### 추가: Salome (Pre/Post-processor)
```
용도: 메시 생성, 결과 시각화
라이선스: LGPL (무료)
설치: https://www.salome-platform.org/

특징:
  ✓ FEniCS, OpenFOAM, Elmer 모두 지원
  ✓ CAD 임포트 (STEP, IGES)
  ✓ 자동 메싱
  ✓ VTK 기반 시각화
```

### 2-3. LAMMPS (분자동역학)

#### LAMMPS 25Mar23+ (무료, 오픈소스)
```
용도: 원자 수준 분석 (AlN-Si bonding)
라이선스: GPL (완전 무료)
설치: apt-get install lammps 또는 conda install -c conda-forge lammps

특징:
  ✓ MD 시뮬레이션
  ✓ 열전도도 (NEMD)
  ✓ 인터페이스 에너지
  ✓ 병렬화 (MPI)

Python 인터페이스:
  pip install lammps
  
비용: **$0** (vs Materials Studio $20,000+)
```

### 2-4. ASE (Atomic Simulation Environment)

```
용도: DFT, interatomic potential 관리
라이선스: LGPL (무료)
설치: pip install ase

특징:
  ✓ LAMMPS 적분 가능
  ✓ 구조 최적화
  ✓ 진동 분석
  
비용: **$0**
```

---

## Part 3: 데이터 처리 & 시각화 (모두 무료)

### 3-1. Python 과학 스택

#### 필수 라이브러리
```python
# pip install numpy scipy matplotlib pandas scikit-learn

import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import pandas as pd
from scipy.optimize import curve_fit

# 예: TDTR 데이터 분석
data = pd.read_csv("tdtr_results.csv")
plt.figure(figsize=(10, 6))
plt.plot(data['time'], data['amplitude'], 'o-')
plt.xlabel("Time (ps)")
plt.ylabel("Amplitude (mV)")
plt.savefig("tdtr_signal.png", dpi=300)
```

**비용**: **$0** (모두 오픈소스)

### 3-2. 고급 시각화

#### ParaView (3D 시각화)
```
용도: COMSOL, OpenFOAM, LAMMPS 결과 시각화
라이선스: BSD (무료)
설치: https://www.paraview.org/download/

특징:
  ✓ 대용량 데이터 (수억 셀)
  ✓ 애니메이션 생성
  ✓ Python scripting
  
비용: **$0**
```

#### Jupyter Notebook
```
용도: 분석 + 시각화 + 문서화 통합
라이선스: BSD (무료)
설치: pip install jupyter

장점:
  ✓ 코드 + 플롯 + 설명 한 파일
  ✓ 재현성 (reproducibility)
  ✓ Git 협력 가능
```

---

## Part 4: 비용 비교 (전체 프로젝트)

### 기존 계획 (상용 소프트웨어)
```
COMSOL Multiphysics:       $300만/년
ANSYS Fluent:              $1000만/년
Materials Studio (LAMMPS): $2000만/년
────────────────────────
총 예산:                   ~$3300만/년
────────────────────────
4년 (2025-2028):           ~$1.3억 원
```

### 오픈소스 대체 계획
```
FEniCS (COMSOL 대체):      $0 (무료)
OpenFOAM (Fluent 대체):    $0 (무료)
LAMMPS (MD 분석):          $0 (무료)
Salome (메싱):             $0 (무료)
ParaView (시각화):         $0 (무료)
────────────────────────
총 예산:                   $0 (무료)
────────────────────────
차액:                       -$1.3억 원 절감
```

### 추가 비용 (필수)
```
Claude API (논문 검증):    $20만/년 (논문당 $5)
HPC 서버 (대전/대구):      $0 (인하대 HPC 또는 KISTI)
────────────────────────
실제 필요 비용:            $20만/년
```

**결론: 99% 비용 절감**

---

## Part 5: 각 논문별 도구 할당

### Paper 1: L1 Synthesis
```
논문 조사:
  ├─ arXiv API (최신 논문)
  ├─ Semantic Scholar (인용도)
  └─ CrossRef (메타데이터)

시뮬레이션:
  ├─ FEniCS (선택, 보조)
  │   └─ ICP 플라즈마 깊이 프로파일
  └─ Python scipy (데이터 분석)

비용: $0
```

### Paper 2: L2 Direct Bonding
```
논문 조사:
  ├─ Semantic Scholar API
  ├─ arXiv (Materials Science)
  └─ PubMed Central (interdisciplinary)

시뮬레이션:
  ├─ FEniCS
  │   └─ Thermal-stress coupling (계면 응력)
  ├─ LAMMPS
  │   └─ AlN-Si bonding interface energy
  └─ Jupyter (결과 분석 & 공유)

비용: $0
```

### Paper 3: L2 Thermal Cycling
```
논문 조사:
  ├─ arXiv
  ├─ Semantic Scholar (인용도 기반)
  └─ CORE API (full text 검색)

시뮬레이션:
  ├─ FEniCS (Elmer)
  │   └─ Thermal-mechanical multiphysics
  │       (온도-응력 coupling)
  ├─ LAMMPS (원자 수준 공극 핵생성)
  └─ Python matplotlib (데이터 시각화)

비용: $0
```

### Paper 4: Micro-Channel Cooling ⭐
```
논문 조사:
  ├─ Semantic Scholar (2-phase boiling papers)
  ├─ arXiv (CFD preprints)
  └─ CrossRef (chiplet cooling trend)

시뮬레이션:
  ├─ OpenFOAM (primary)
  │   ├─ Single-phase laminar flow
  │   └─ 2-phase VOF/Eulerian boiling
  ├─ FEniCS (coupling)
  │   └─ Thermal-structural deformation
  ├─ ParaView (3D visualization)
  └─ Python + Jupyter (full analysis)

비용: $0
```

### 공유: Simulation_Tools
```
도구:
  ├─ FEniCS (Elmer, Calculix)
  ├─ OpenFOAM
  ├─ LAMMPS (ASE)
  ├─ Salome (meshing)
  ├─ ParaView (visualization)
  └─ Jupyter notebooks

비용: $0 (모두 오픈소스)
```

---

## Part 6: PC1에서의 설정 (설치 가이드)

### Step 1: Python 환경 (PC1, Windows)

```bash
# Conda 기본 설치
conda create -n research python=3.11 -y
conda activate research

# 과학 스택
conda install numpy scipy matplotlib pandas scikit-learn -y

# Jupyter
conda install jupyter jupyterlab -y

# ASE
pip install ase

# 선택: LAMMPS (Windows에서 WSL2 필요)
# WSL2: conda install -c conda-forge lammps
```

### Step 2: OpenFOAM (Windows)

```bash
# Option A: WSL2 (Windows Subsystem for Linux)
# WSL2 설치 후:
  wsl --install -d Ubuntu-22.04
  wsl
  sudo apt update
  sudo apt install openfoam11 -y

# Option B: Docker
  docker pull openfoam/openfoam:latest

# Option C: Pre-built (Simscale 또는 cloud)
  https://www.simscale.com/ (웹 기반, 무료 제한)
```

### Step 3: FEniCS (Windows)

```bash
# Option A: Conda
  conda install -c conda-forge fenics -y

# Option B: Docker
  docker pull dolfinproject/dolfinx
```

### Step 4: Salome (Windows)

```
다운로드: https://www.salome-platform.org/downloads
설치: salome-9.12.0-Win64.exe
```

### Step 5: ParaView (Windows)

```
다운로드: https://www.paraview.org/download/
설치: ParaView-v5.13.0-Windows-Python3.10-msvc-x86_64.exe
```

---

## Part 7: 자동 검색 스크립트 (통합)

### 저장 위치
```
C:\Users\AOL\Desktop\SH.Kim\
  └─ 02_Literature_Search_Automation.py
```

### 실행
```bash
python 02_Literature_Search_Automation.py

결과:
  ├─ paper_search_results_P1.json (논문 1)
  ├─ paper_search_results_P2.json (논문 2)
  ├─ paper_search_results_P3.json (논문 3)
  └─ paper_search_results_P4.json (논문 4)
```

---

## Part 8: 최종 요약

### 비용 절감: **1.3억 원** (4년)

| 항목 | 상용 | 오픈소스 | 절감 |
|---|---|---|---|
| COMSOL | $300만/년 | $0 | $300만 |
| OpenFOAM | $1000만/년 | $0 | $1000만 |
| LAMMPS | $2000만/년 | $0 | $2000만 |
| 기타 | $300만/년 | $0 | $300만 |
| **총계** | **$3600만/년** | **$0** | **$3600만** |

### 품질: **동등 또는 우수**

| 기준 | COMSOL | FEniCS | 우위 |
|---|---|---|---|
| 정확도 | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | 동등 |
| 속도 (GPU) | ⭐⭐⭐ | ⭐⭐⭐⭐ | FEniCS |
| 커스터마이징 | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | FEniCS |
| 학습곡선 | 가파름 | 낮음 | FEniCS |

---

## Part 9: 다음 단계

1. ✅ 자동화 스크립트 (완료)
2. ✅ 공공 API & 오픈소스 도구 (완료) ← 여기
3. → **Step 3**: PC1에서 폴더 자동 생성 & 초기화
4. → **Step 4**: 투자 타이밍 분석
5. → **Step 5**: 다기관 협력 & 창업 경로

---

## 최종 메시지

**비용 제약은 더 이상 문제가 아닙니다.**

- ✅ 모든 시뮬레이션 도구: 무료
- ✅ 모든 논문 조사 API: 무료
- ✅ 품질: 상용 수준
- ✅ 투자 준비: 완벽

**다음 주: PC1에서 FEniCS + OpenFOAM 설치하세요.**

## 🔗 지식 연결 (Knowledge Mesh)
- **Parent Hub**: [[00_AlN_Research_Hub_Master_Index]]
- **Related Master Plan**: [[통합_연구_마스터플랜_멀티스케일_반도체_열관리]]
- **Master Index**: [[Index]]
