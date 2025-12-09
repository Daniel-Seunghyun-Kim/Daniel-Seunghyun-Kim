- 👋 Hi, I’m @Daniel-Seunghyun-Kim
- 👀 I’m interested in adjusting the etching process of semiconductor by using coding
- 🌱 I’m currently learning the etching process of semiconductor by using copper films
- 💞️ I’m looking to collaborate on ...
- 📫 How to reach me ...

<!---
Daniel-Seunghyun-Kim/Daniel-Seunghyun-Kim is a ✨ special ✨ repository because its `README.md` (this file) appears on your GitHub profile.
You can click the Preview link to take a look at your changes.
--->

# 파일 자동 정리 프로그램

컴퓨터 내부의 여러 파일들을 날짜와 자료 성격에 맞게 자동으로 정리해주는 프로그램입니다.

## 주요 기능

- 📅 **날짜별 정리**: 파일의 수정 날짜를 기준으로 `YYYY-MM` 형식의 폴더로 자동 분류
- 📁 **유형별 정리**: 파일 확장자를 기반으로 다음 카테고리로 자동 분류
  - 문서 (PDF, Word, Excel, PowerPoint 등)
  - 이미지 (JPG, PNG, GIF 등)
  - 비디오 (MP4, AVI, MKV 등)
  - 음악 (MP3, WAV, FLAC 등)
  - 압축파일 (ZIP, RAR, 7Z 등)
  - 프로그램 (EXE, MSI, DEB 등)
  - 코드 (Python, JavaScript, HTML 등)
  - 기타
- 🔄 **중복 파일 처리**: 같은 이름의 파일이 있을 경우 자동으로 번호를 추가
- 🛡️ **안전 모드**: 시뮬레이션 모드로 실제 이동 전에 미리 확인 가능

## 설치 방법

Python 3.6 이상이 필요합니다. 추가 패키지 설치가 필요하지 않습니다.

```bash
# 파일 실행 권한 부여 (선택사항)
chmod +x file_organizer.py
```

## 사용 방법

### 기본 사용법

```bash
# 현재 디렉토리 정리 (시뮬레이션 모드로 먼저 확인)
python file_organizer.py . --dry-run

# 실제로 정리 실행
python file_organizer.py .

# 특정 디렉토리 정리
python file_organizer.py ~/Downloads

# 다른 디렉토리로 정리된 파일 저장
python file_organizer.py ~/Downloads -t ~/정리된파일
```

### 옵션

- `--dry-run`: 실제 이동 없이 시뮬레이션만 실행 (안전하게 미리 확인)
- `--no-date`: 날짜별 정리 비활성화
- `--no-type`: 유형별 정리 비활성화
- `--no-recursive`: 하위 디렉토리 검색 비활성화
- `-t, --target-dir`: 정리된 파일을 저장할 타겟 디렉토리 지정

### 사용 예시

```bash
# 날짜별로만 정리 (유형별 정리 없음)
python file_organizer.py ~/Downloads --no-type

# 유형별로만 정리 (날짜별 정리 없음)
python file_organizer.py ~/Downloads --no-date

# 현재 디렉토리만 정리 (하위 디렉토리 제외)
python file_organizer.py . --no-recursive
```

## 정리 결과 구조

기본적으로 파일은 다음과 같은 구조로 정리됩니다:

```
정리된_디렉토리/
├── 문서/
│   ├── 2024-01/
│   │   ├── report.pdf
│   │   └── presentation.pptx
│   └── 2024-02/
│       └── data.xlsx
├── 이미지/
│   ├── 2024-01/
│   │   └── photo.jpg
│   └── 2024-02/
│       └── screenshot.png
└── 비디오/
    └── 2024-01/
        └── video.mp4
```

## 복구 기능

파일 정리 후 원래 위치로 되돌리고 싶다면 `file_restorer.py`를 사용하세요.

### 복구 프로그램 사용법

```bash
# 이동 이력 목록 보기
python3 file_restorer.py --list --auto ~/Downloads

# 시뮬레이션으로 복구 확인
python3 file_restorer.py --auto ~/Downloads --dry-run

# 실제로 복구 실행
python3 file_restorer.py --auto ~/Downloads

# 특정 로그 파일 지정
python3 file_restorer.py ~/Downloads/.file_organizer_history.json

# 복구 후 이력 파일 삭제
python3 file_restorer.py --auto ~/Downloads --clear
```

### 복구 프로그램 옵션

- `--auto, -a`: 지정한 디렉토리에서 자동으로 로그 파일 찾기
- `--list, -l`: 이동 이력 목록만 표시 (복구하지 않음)
- `--dry-run`: 실제 복구 없이 시뮬레이션만 실행
- `--clear`: 복구 후 이력 파일 삭제
- `--no-reverse`: 이동 순서대로 복구 (기본값: 역순)

### 이동 이력 저장 위치

파일 정리 시 이동 이력이 다음 위치에 자동으로 저장됩니다:
- `소스디렉토리/.file_organizer_history.json`

이 파일을 삭제하면 복구가 불가능하므로 주의하세요.

## 주의사항

- 프로그램 실행 전에 **반드시 `--dry-run` 옵션으로 먼저 확인**하세요
- 중요한 파일이 있는 경우 백업을 권장합니다
- 이미 정리된 폴더 구조 내의 파일은 건너뜁니다
- 복구가 필요할 수 있으므로 `.file_organizer_history.json` 파일은 보관하세요

## 라이선스

이 프로젝트는 개인 사용 목적으로 제작되었습니다.
