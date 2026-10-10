# 데이터 검증 프로토콜 | AlN 연구 업로드 및 정합성

**최종 업데이트**: 2026-06-12  
**범위**: 실험 데이터 업로드, 품질 검증, 파이프라인 통합  
**목표**: Phase 9.x (사용자 데이터 입수 후) 자동 검증

---

## 📌 개요

### 상황
- **현재**: 11논문 문헌 데이터만 사용 (92행)
- **예정**: 사용자가 실제 실험 데이터 업로드 (시기 미정)
- **목표**: 스키마 무관 검증 → ML 파이프라인 통합

### 검증 스코프
```
수락 기준:
  ✅ 형식: .xlsx, .csv, 원시 텍스트 모두 가능
  ✅ 스키마: 컬럼명 일치 필수 아님 (키워드 기반 감지)
  ✅ 단위: Pa vs mTorr 자동 감지 + 경고
  ✅ 범위: 물리 타당성 검증 (T > 100K, P > 0 등)
  
거절 기준:
  ❌ 결측값: 임의 보간 금지 (규칙 1/8)
  ❌ 합성값: 가상 k 데이터 금지
  ❌ 중복 행: 동일 조건 반복 → 통합
```

---

## 🔍 검증 단계

### Step 1: 파일 포맷 인식

```python
# 위치: 01_ACTUAL_EXPERIMENT_DATA/validate_uploaded_data.py

def detect_format(filepath):
    """
    파일 형식 자동 감지
    """
    if filepath.endswith('.xlsx'):
        return 'xlsx'
    elif filepath.endswith('.csv'):
        return 'csv'
    else:
        return 'raw_text'  # .txt, .dat 등

def load_data(filepath):
    """
    형식별 로드
    """
    fmt = detect_format(filepath)
    
    if fmt == 'xlsx':
        import openpyxl
        wb = openpyxl.load_workbook(filepath)
        ws = wb.active
        # 시트 헤더 + 행 추출
        
    elif fmt == 'csv':
        import csv
        with open(filepath, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            # 행 반복
            
    elif fmt == 'raw_text':
        # 정규식으로 값 추출
        # 예: "T=300°C, P=1 mTorr, ..." 파싱
        pass
    
    return dataframe

# 출력: pandas DataFrame
# 컬럼: 원본 그대로 (키워드 매칭 후)
```

### Step 2: 컬럼 키워드 매칭

```python
def detect_columns(df):
    """
    헤더 컬럼명을 표준 이름으로 매핑
    """
    
    COLUMN_KEYWORDS = {
        'temperature': ['T', 'temp', 'Temperature', '온도'],
        'pressure': ['P', 'Pressure', 'mTorr', 'Pa', '압력'],
        'ts_distance': ['S', 'TS distance', 'Target-Substrate', '거리'],
        'k_thermal': ['k', 'conductivity', 'thermal', 'k_W_mK', '열전도도'],
        'xrd_index': ['XRD', 'Miller', 'hkl', '회절'],
    }
    
    detected = {}
    for std_name, keywords in COLUMN_KEYWORDS.items():
        for col in df.columns:
            for kw in keywords:
                if kw.lower() in col.lower():
                    detected[std_name] = col
                    break
    
    return detected  # 매핑 결과

# 결과:
# {
#   'temperature': '온도_C',
#   'pressure': 'P_mTorr',
#   'ts_distance': 'S_cm',
#   'k_thermal': 'k실험',
#   'xrd_index': 'XRD_peaks'
# }
```

### Step 3: 물리 타당성 검증

```python
def validate_physical_bounds(df, detected_cols):
    """
    각 행의 물리적 타당성 확인
    """
    
    errors = []
    warnings = []
    
    # 온도 범위 (절대영도 이상)
    if 'temperature' in detected_cols:
        col_T = detected_cols['temperature']
        for idx, T in enumerate(df[col_T]):
            if T < -273.15:
                errors.append(f"Row {idx}: T={T}K (절대영도 미만)")
            elif T > 1000:
                warnings.append(f"Row {idx}: T={T}°C (문헌 범위 초과, 물리 가능하나 검증 필요)")
    
    # 압력 범위
    if 'pressure' in detected_cols:
        col_P = detected_cols['pressure']
        for idx, P in enumerate(df[col_P]):
            if P <= 0:
                errors.append(f"Row {idx}: P={P} (음수 또는 0 불가)")
            elif P > 100:  # Pa로 정규화 후 확인
                warnings.append(f"Row {idx}: P={P} Pa (고진공, 확인 권장)")
    
    # T-S 거리
    if 'ts_distance' in detected_cols:
        col_S = detected_cols['ts_distance']
        for idx, S in enumerate(df[col_S]):
            if S <= 0:
                errors.append(f"Row {idx}: S={S} (음수 불가)")
    
    # k 열전도도
    if 'k_thermal' in detected_cols:
        col_k = detected_cols['k_thermal']
        for idx, k in enumerate(df[col_k]):
            if k < 0:
                errors.append(f"Row {idx}: k={k} W/m·K (음수 불가)")
            elif pd.isna(k):
                # 결측은 경고만 (보간 금지)
                warnings.append(f"Row {idx}: k 결측값 (보간하지 않음)")
    
    return {
        'errors': errors,
        'warnings': warnings,
        'valid_rows': len(df) - len(errors)
    }
```

### Step 4: 단위 자동 감지 및 정정

```python
def detect_and_convert_units(df, detected_cols):
    """
    압력 단위 (Pa vs mTorr) 자동 감지 + 변환
    """
    
    if 'pressure' not in detected_cols:
        return df, []
    
    col_P = detected_cols['pressure']
    detected_unit = None
    ambiguous = []
    
    # 통계 기반 감지
    P_values = df[col_P].dropna()
    P_mean = P_values.mean()
    P_max = P_values.max()
    
    if P_mean > 10:  # 전형적인 Pa 범위
        detected_unit = 'Pa'
    elif P_mean < 10:  # 전형적인 mTorr 범위
        detected_unit = 'mTorr'
    else:
        ambiguous.append(f"압력 단위 모호 (평균 {P_mean}, 0.1-100 범위)")
    
    # 변환 (Pa 기준으로)
    CONVERSION = 0.13332237  # 1 mTorr = 0.13332237 Pa
    
    if detected_unit == 'mTorr':
        df[col_P] = df[col_P] * CONVERSION
        warnings = [f"⚠️ 압력을 mTorr → Pa로 변환 (계수: {CONVERSION})"]
        return df, warnings + ambiguous
    else:
        return df, ambiguous

# 출력:
# df[col_P]: Pa로 정규화
# warnings: ["⚠️ 압력을 mTorr → Pa로 변환..."]
```

### Step 5: XRD 라벨 정규화

```python
def normalize_xrd_labels(df, detected_cols):
    """
    XRD 회절지수 표기 정규화
    Ishihara 1998 표기법 기준
    """
    
    if 'xrd_index' not in detected_cols:
        return df
    
    col_XRD = detected_cols['xrd_index']
    
    NORMALIZATION_MAP = {
        # 입력 형식 → 표준 형식
        '0001': '(0001)',
        '001': '(001)',
        '002': '(002)',
        '004': '(004)',
        '100': '(100)',
        '101': '(101)',
        '200': '(200)',
        'c축': '(0001)',  # 한글 입력
        'basal': '(0001)',
        'nonoriented': 'OTHER',
        'random': 'OTHER',
    }
    
    normalized = []
    for idx, xrd_val in enumerate(df[col_XRD]):
        if pd.isna(xrd_val):
            normalized.append(None)
        else:
            xrd_str = str(xrd_val).strip()
            if xrd_str in NORMALIZATION_MAP:
                normalized.append(NORMALIZATION_MAP[xrd_str])
            else:
                # 미등록 지수 → 경고
                normalized.append(None)
                print(f"⚠️ Row {idx}: XRD 지수 미인식 '{xrd_str}' → None 처리")
    
    df[col_XRD] = normalized
    return df

# 참고: aln_common.py의 label_c_axis() 함수와 일치
```

### Step 6: 결측값 정책

```python
def validate_missing_values(df, detected_cols):
    """
    결측값 정책: 절대 보간 금지
    """
    
    missing_report = {}
    
    for std_name, col in detected_cols.items():
        n_missing = df[col].isna().sum()
        pct_missing = 100 * n_missing / len(df)
        
        missing_report[std_name] = {
            'count': n_missing,
            'percent': pct_missing,
        }
        
        if n_missing > 0:
            if std_name in ['temperature', 'pressure', 'ts_distance']:
                # 필수 피처
                print(f"❌ 오류: {std_name} {n_missing}개 결측 (필수, 보간 불가)")
                return False  # 거절
            else:
                # 선택 피처 (k, xrd 등)
                print(f"⚠️ 경고: {std_name} {n_missing}개 결측 (보간하지 않음, 그대로 사용)")
    
    return True  # 허용

# 규칙:
# - 필수 피처 (T, P, S): 0% 결측만 허용
# - 선택 피처 (k, XRD): 최대 30% 결측 허용 (보간 안 함)
```

### Step 7: 중복 행 제거 (선택)

```python
def detect_and_merge_duplicates(df, detected_cols):
    """
    동일 (T, P, S) 조건의 중복 제거
    """
    
    key_cols = [detected_cols[c] for c in ['temperature', 'pressure', 'ts_distance'] 
                if c in detected_cols]
    
    if not key_cols:
        return df, []
    
    duplicates = df.duplicated(subset=key_cols, keep=False)
    n_dup = duplicates.sum()
    
    if n_dup > 0:
        print(f"🔍 중복 발견: {n_dup}행 (통합 권장)")
        
        # 통합 전략: 평균값 사용 (선택적)
        df_merged = df.groupby(key_cols, as_index=False).agg({
            'k_thermal': 'mean' if 'k_thermal' in df.columns else 'first',
            'xrd_index': 'first',  # 범주형은 첫 값
        })
        
        print(f"✅ 통합 완료: {len(df)} → {len(df_merged)}행")
        return df_merged, [f"중복 {n_dup}행 통합"]
    
    return df, []
```

---

## ✅ 검증 체크리스트 (전체)

### 입력 검증
```
□ 파일 로드 성공 (형식 감지)
□ 컬럼 키워드 매칭 성공
□ 필수 컬럼 모두 인식
□ 행 수 확인 (최소 5행 이상 권장)
```

### 데이터 품질
```
□ 결측값 정책 확인
  └─ 필수: T, P, S (0% 결측)
  └─ 선택: k, XRD (≤30% 허용)

□ 물리 범위 확인
  └─ 온도: -273.15°C < T < 1000°C
  └─ 압력: 0 < P < 1e6 Pa
  └─ T-S거리: S > 0

□ 단위 정정 확인
  └─ mTorr → Pa 변환 (0.13332237)
  └─ °C vs K 명확화 (기본값: °C)

□ 라벨 정규화 확인
  └─ XRD 지수: (0001), (001), (002) 등
  └─ 미인식 라벨: KNOWN_OTHER_INDICES 가드
```

### 통합 준비
```
□ 정제 데이터 CSV 생성
  └─ 경로: 01_ACTUAL_EXPERIMENT_DATA/cleaned_*.csv
  └─ 컬럼: 표준명 (temperature, pressure, ts_distance, k_thermal, xrd_index)

□ 검증 보고서 생성
  └─ 경로: 01_ACTUAL_EXPERIMENT_DATA/validation_report_*.json
  └─ 내용: 오류/경고/통계

□ ML 파이프라인 준비
  └─ v2 분류기 재훈련 (문헌 데이터 + 사용자 데이터)
  └─ 새 LOPO 교차검증
```

---

## 📊 출력 형식

### 검증 보고서 (JSON)

```json
{
  "validation_timestamp": "2026-10-05T14:30:00Z",
  "input_file": "experiment_data_2026-10.xlsx",
  "format_detected": "xlsx",
  "statistics": {
    "total_rows": 45,
    "valid_rows": 43,
    "rejected_rows": 2,
    "warnings": 3
  },
  "column_mapping": {
    "temperature": "온도_C",
    "pressure": "P_mTorr",
    "ts_distance": "거리_cm",
    "k_thermal": "k측정",
    "xrd_index": "XRD_peaks"
  },
  "unit_conversions": [
    "압력: mTorr → Pa (계수 0.13332237)"
  ],
  "errors": [
    "Row 5: T = -50°C (물리 불가능)",
    "Row 12: P = -0.5 mTorr (음수)"
  ],
  "warnings": [
    "Row 3: k 결측 (보간하지 않음)",
    "Row 8: T = 950°C (범위 초과, 검증 권장)",
    "압력 단위 모호 (통계: 평균 2.5, mTorr로 가정)"
  ],
  "cleaned_data_path": "01_ACTUAL_EXPERIMENT_DATA/cleaned_2026-10.csv",
  "status": "ACCEPTED_WITH_WARNINGS"
}
```

### 정제 데이터 CSV

```csv
temperature_C,pressure_pa,ts_distance_cm,k_thermal_w_mk,xrd_index,source
300,0.13332,5,85,(0001),experiment_2026-10
320,0.13332,5,82,(0001),experiment_2026-10
280,0.26664,3,92,(0002),experiment_2026-10
...
```

---

## 🚀 자동화 스크립트

### 전체 파이프라인

```python
# 위치: 01_ACTUAL_EXPERIMENT_DATA/validate_uploaded_data.py

def main(filepath):
    """
    전체 검증 파이프라인
    """
    
    print("=" * 60)
    print("AlN 실험 데이터 검증 파이프라인")
    print("=" * 60)
    
    # Step 1
    df = load_data(filepath)
    print(f"✅ 파일 로드: {len(df)}행")
    
    # Step 2
    detected_cols = detect_columns(df)
    print(f"✅ 컬럼 매칭: {detected_cols}")
    
    # Step 3
    validation = validate_physical_bounds(df, detected_cols)
    if validation['errors']:
        print(f"❌ 오류 {len(validation['errors'])}건 (거절)")
        return False
    print(f"✅ 물리 검증: {len(validation['warnings'])}건 경고")
    
    # Step 4
    df, unit_warnings = detect_and_convert_units(df, detected_cols)
    print(f"✅ 단위 정정: {len(unit_warnings)}건")
    
    # Step 5
    df = normalize_xrd_labels(df, detected_cols)
    print(f"✅ XRD 정규화 완료")
    
    # Step 6
    if not validate_missing_values(df, detected_cols):
        return False
    print(f"✅ 결측값 정책 확인")
    
    # Step 7
    df, dup_report = detect_and_merge_duplicates(df, detected_cols)
    print(f"✅ 중복 처리: {dup_report}")
    
    # 저장
    output_path = filepath.replace('.xlsx', '_cleaned.csv')
    df.to_csv(output_path, index=False)
    print(f"\n✅ 정제 데이터 저장: {output_path}")
    
    # 보고서
    report = {
        'status': 'ACCEPTED',
        'total_rows': len(df),
        'cleaned_path': output_path,
    }
    
    print("\n" + "=" * 60)
    print("검증 완료")
    print("=" * 60)
    return True

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print("사용법: python validate_uploaded_data.py <파일경로>")
    else:
        main(sys.argv[1])
```

---

## ⚠️ 주의사항

### 절대 규칙 (반복)

1. **결측값 보간 금지** (규칙 1/8)
   - 수치 보간 (interpolation) 불가
   - 이유: 데이터 신뢰성 오염

2. **합성값 생성 금지**
   - 측정하지 않은 k를 가정으로 채우기 불가
   - 예: "실험 대기 중이므로 예상값 80 W/m·K 입력" ❌

3. **출처 명시 필수**
   - 모든 행에 source 컬럼 추가
   - 예: source = "실험_20261005" 또는 논문명

4. **단위 명확화**
   - 온도: °C 기본값 (K는 명시 필요)
   - 압력: Pa 기본값 (다른 단위는 감지 후 변환)

---

## 📋 프로비넌스 체크리스트 (Phase 9.x)

### 데이터 입수 후 필수 확인

```
□ 1단계: 파일 포맷 & 로드
  └─ validate_uploaded_data.py 실행
  └─ cleaned_*.csv 생성 확인

□ 2단계: 품질 점검
  └─ 검증 보고서 검토 (JSON)
  └─ 오류/경고 목록 확인

□ 3단계: 출처 확인
  └─ source 컬럼 채우기
  └─ 실험실, 날짜, 측정기기 기록

□ 4단계: ML 파이프라인 준비
  └─ 정제 데이터를 aln_common.py에 로드
  └─ 데이터셋 통합 (문헌 + 실험)
  └─ v2/v4 모델 재훈련

□ 5단계: 결과 검증
  └─ LOPO 교차검증 성능 확인
  └─ 새로운 데이터가 성능을 향상시키는지 확인

□ 6단계: 문서 업데이트
  └─ RESUME_CHECKPOINT.md 갱신 (Phase 10.0)
  └─ 새로운 앵커 및 검증 항목 추가
```

---

**생성일**: 2026-10-05  
**기반**: 01_ACTUAL_EXPERIMENT_DATA/validate_uploaded_data.py + 규칙  
**상태**: ✅ 프로토콜 완성 (실행 대기)

**다음 세션**: 사용자 데이터 업로드 → validate 스크립트 실행 → 결과 검증
