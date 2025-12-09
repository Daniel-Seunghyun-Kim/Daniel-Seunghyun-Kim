# 열전도 방정식 시뮬레이션

1D 및 2D 단순 열전도 방정식의 해석해와 수치해법을 구현하고, 시간에 따른 온도 프로파일을 애니메이션으로 시각화합니다.

## 방정식

### 1D 열전도 방정식
```
∂T/∂t = α * ∂²T/∂x²
```

### 2D 열전도 방정식
```
∂T/∂t = α * (∂²T/∂x² + ∂²T/∂y²)
```

여기서:
- `T`: 온도 (℃)
- `t`: 시간 (s)
- `α`: 열확산계수 (m²/s)
- `x, y`: 공간 좌표 (m)

## 설치

필요한 패키지를 설치합니다:

```bash
pip install -r requirements.txt
```

## 사용법

### 전체 시뮬레이션 실행

```bash
python main.py
```

이 명령은 다음을 생성합니다:
- 1D 열전도 해석해 애니메이션
- 1D 열전도 수치해법 애니메이션
- 2D 열전도 수치해법 애니메이션

### 개별 실행

#### 1D 열전도 - 해석해
```bash
python heat_conduction_1d.py
```

#### 2D 열전도
```bash
python heat_conduction_2d.py
```

## 구현 내용

### 1D 열전도 (`heat_conduction_1d.py`)
- **해석해**: 푸리에 급수 전개를 사용한 정확한 해
- **수치해법**: FTCS (Forward Time Central Space) 방법
- 경계 조건: Dirichlet 경계 조건 (고정 온도)

### 2D 열전도 (`heat_conduction_2d.py`)
- **수치해법**: FTCS 방법
- 시각화:
  - 2D 컬러맵 애니메이션
  - 3D 표면 플롯 애니메이션

## 파라미터 설정

코드에서 다음 파라미터를 조정할 수 있습니다:

- `L`, `Lx`, `Ly`: 영역 크기 (m)
- `T0`: 초기 온도 (℃)
- `T_left`, `T_right`, `T_boundary`: 경계 온도 (℃)
- `alpha`: 열확산계수 (m²/s)
- `nx`, `ny`: 공간 격자 수
- `nt`: 시간 스텝 수
- `dt`: 시간 간격 (s)

## 안정성 조건

수치해법의 안정성을 위해 다음 조건을 만족해야 합니다:

- **1D FTCS**: `r = α * dt / dx² ≤ 0.5`
- **2D FTCS**: `rx = α * dt / dx² ≤ 0.25`, `ry = α * dt / dy² ≤ 0.25`

## 출력 파일

애니메이션은 다음 형식으로 저장됩니다:
- `heat_conduction_1d_analytical.gif`
- `heat_conduction_1d_numerical.gif`
- `heat_conduction_2d.gif`
- `heat_conduction_2d_3d.gif`

## 예제

기본 예제는 다음과 같은 조건으로 실행됩니다:

**1D:**
- 막대 길이: 1.0 m
- 초기 온도: 0℃
- 왼쪽 경계: 100℃
- 오른쪽 경계: 0℃
- 열확산계수: 0.01 m²/s

**2D:**
- 영역 크기: 1.0 m × 1.0 m
- 초기 온도: 0℃
- 경계 온도: 100℃
- 열확산계수: 0.01 m²/s
