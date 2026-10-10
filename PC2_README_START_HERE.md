# PC2 (다른 컴퓨터) - 11일 Fabel 테스트 시작 가이드

**이 문서부터 읽으세요!**

---

## 🎯 당신의 미션 (11일)

```
옵션 A: 순수 실험 논문 초안 완성
  └─ 투고 준비 완료
  
+ 옵션 C: 메커니즘 논문 토대 구축
  └─ 3개월 실험 설계 완료
  
+ Fabel 5 신뢰도 객관적 측정
  └─ 할루시네이션 위험도 정량화
  
+ 선행연구 데이터베이스 통합
  └─ 10개 논문 분석 완료
```

---

## 📁 핵심 파일 3개 (이 순서대로 열기)

### 1️⃣ 먼저 읽기 (지금)
```
11Day_Fable_Test_Protocol.md
└─ 11일 상세 일정 + 매일 할일 + 템플릿
```

### 2️⃣ Day 2에서 사용
```
Literature_Database_Template.md
└─ 선행연구 수집 및 기록 양식
└─ 10개 논문을 이 형식으로 정리
```

### 3️⃣ Day 9-10에서 사용
```
Fabel_Reliability_Scoring_Sheet.csv
└─ Fabel 신뢰도 11개 항목 채점
└─ Excel 또는 Google Sheets에서 열기
```

---

## ✅ 시작 전 체크리스트

### 환경 확인
```
[ ] Fabel 5 접근 가능? (또는 최신 Claude Fable)
[ ] 선행연구 논문 폴더 확인 (로컬 또는 온라인 접근)
[ ] n=28 데이터 완전? (공정조건 + XRD + SEM + TDTR)
[ ] 매일 2-3시간 작업 시간 확보?
[ ] 클라우드 동기화 (Google Drive/Dropbox) 준비?
```

### 파일 준비
```
[ ] AlN_Thermal_Transport_Master_Guide.md (PC1에서 다운로드)
[ ] 11Day_Fable_Test_Protocol.md (이 폴더)
[ ] Literature_Database_Template.md (이 폴더)
[ ] Fabel_Reliability_Scoring_Sheet.csv (이 폴더)
```

### 데이터 준비
```
[ ] 공정 파라미터 정리 (n=28, 모든 샘플)
[ ] XRD 측정값 (intensity, FWHM, texture coefficient)
[ ] SEM 측정값 (두께, columnar score, void fraction)
[ ] TDTR 측정값 (k, uncertainty, 가능하면 TBC)
```

---

## 🚀 Day 1 시작하기

### 1단계: 이 폴더 구조 만들기

```
AlN_11Day_Project/
├─ Day01_Results/
│  ├─ 01_Data_Summary.md
│  └─ 02_Paper_Methods.md
├─ Day02_Results/
├─ Day03-04_Results/
├─ ...
├─ Day11_Results/
│  ├─ Final_Report.md
│  └─ Fabel_Score.csv
└─ Shared/
   ├─ 11Day_Fable_Test_Protocol.md
   ├─ Literature_Database_Template.md
   └─ Fabel_Reliability_Scoring_Sheet.csv
```

### 2단계: Day 1 할일

```
1. 현재 마크다운 에디터 열기 (VS Code, Obsidian 등)
2. 11Day_Fable_Test_Protocol.md → Day 1 섹션 읽기
3. Day01_Results/01_Data_Summary.md 작성 시작
   (n=28 샘플 데이터 정리)
4. Day01_Results/02_Paper_Methods.md 작성
   (옵션 A 논문 Methods 섹션 초안)
5. 파일 클라우드에 백업
```

### 3단계: 매일 로그 남기기

```
각 날 끝나고:

[Day N 완료]
✅ 했던 것:
- [ ] 작업 1
- [ ] 작업 2
- [ ] 작업 3

⚠️ 문제점:
- [문제명]

📊 통계:
- Fabel 사용: __분
- 문헌 조사: __개

💾 파일 저장:
- [ ] DayN_Results/ 에 저장
- [ ] PC1로 진행상황 보고 (하루 1회)
```

---

## 🔄 PC1과 동기화 방법

### 매일 저녁 (5분)

```
1. PC2: 당일 작업 완료 → DayN_Results/ 저장
2. PC2: 클라우드에 업로드 (Ctrl+S)
   ├─ Google Drive
   ├─ Dropbox
   ├─ OneDrive
   └─ GitHub (가능하면)

3. PC1: 매일 오전에 다운로드
   └─ 진행상황 확인 + 필요시 피드백

4. PC1 피드백 (있으면)
   └─ 클라우드 공유 폴더에 "Feedback.md" 저장
   └─ PC2가 아침에 확인
```

### 권장 공유 방식

```
Google Drive:
├─ AlN_11Day_Project/ 공유 폴더
├─ 누구와 공유: PC1 사용자 (또는 본인 Gmail 2개)
├─ 권한: 편집 가능
└─ 동기화: Google Drive 데스크톱 앱

또는

GitHub Private Repo:
├─ 매일 git commit
├─ PC1도 clone 가능
└─ 버전 관리 + 동기화
```

---

## ⏰ 11일 타임라인

```
Day 1-2 (금요일)    : 기초 준비 + 옵션 A 논문 틀
Day 3-4 (토-일)     : Fabel 공정 분석 테스트 + 비교
Day 5-6 (월-화)     : Fabel 메커니즘 테스트 + 문헌 검증
Day 7-8 (수-목)     : Discussion 작성 (Fabel + 검증)
Day 9-10 (금-토)    : Fabel 신뢰도 채점 (11개 항목)
Day 11 (일요일)     : 최종 보고서 + 다음 계획 수립
```

---

## 🔑 핵심 규칙 (꼭 지키기)

### ✅ 반드시 해야 할 것

```
1. 매일 Fabel의 예측/조언을 기록하기
   "Fabel Query #N: [질문]"
   "Fabel Response: [답변]"
   
2. 같은 날에 실제 데이터/문헌과 비교하기
   "비교 분석: [실제] vs [Fabel 예측]"
   "일치도: __% / 신뢰도: ⭐⭐⭐"
   
3. 매일 로그 남기기
   "Day N 완료: [날짜], 완료도: __%"
   
4. 의문점 추출하기
   "[의문점] → Day 5-6 검증 항목"
```

### ❌ 절대 하면 안 될 것

```
❌ Fabel을 "정답"처럼 사용
   대신: "가설/예측으로 기록, 데이터로 검증"

❌ 검증 없이 Fabel의 예측을 논문에 넣기
   대신: "Fabel 의견 + 우리 데이터 + 문헌 확인 후"

❌ 날마다 로그 안 남기기
   대신: "매일 저녁 15분 로그 기록"

❌ PC1에 보고 안 하기
   대신: "매일 1회, 진행상황 클라우드에 저장"
```

---

## 📞 PC1과 소통 (문제 발생 시)

### 빠른 결정 필요?

```
Fabel 테스트 중 "이게 맞나?" 의문이 생기면:

1. 일단 계속 진행 (로그에 기록)
2. 하루 끝나고 "의문사항.md" 작성
3. PC1으로 클라우드 공유
4. PC1이 다음날 오전에 피드백
5. PC2가 피드백 반영해서 진행
```

### 예상 질문

```
Q: Fabel이 이 부분 이상한데?
A: 로그에 기록 → PC1 검토 → 다음날 피드백

Q: 선행연구 논문을 찾을 수 없어
A: 클라우드에 "논문_검색_도움요청.md" 저장 → PC1이 링크 제공

Q: 데이터가 부족한데?
A: Day 2 때 PC1과 협의 (추가 측정 필요 여부)
```

---

## 🎓 Fabel 사용 팁

### 효과적인 쿼리 작성

**❌ 나쁜 예**:
```
"AlN 열전도도에 대해 설명해줄래?"
→ 너무 일반적, 우리 데이터와 관계 없음
```

**✅ 좋은 예**:
```
"우리는 RF=200W, N2/Ar=0.5, T=300°C일 때 
 TC=0.88, k=45 W/m·K를 얻었다.
 
 그런데 N2/Ar을 0.7로 높이면 TC가 0.45로 떨어진다.
 
 이것을 설명할 수 있는 물리 메커니즘은?
 
 (참고: 이것은 예측입니다. 실제 데이터와 비교할 예정입니다.)"
```

### 데이터와 함께 제시

```
"우리 데이터:
  RF 150W → TC 0.72
  RF 200W → TC 0.88  
  RF 250W → TC 0.92

이 트렌드를 설명하려면
RF power의 어떤 물리 효과가 가장 중요한가?"
```

---

## 📊 예상 결과

### Day 11 후

```
✅ 옵션 A:
- 논문 초안 70-80% 완성
- 투고 준비 가능 (1주 추가 필요)

✅ 옵션 C:
- Discussion의 메커니즘 부분 초안 완성
- 3개월 실험 계획 수립

✅ Fabel 신뢰도:
- 객관적 점수 (11개 항목)
- 사용 가이드라인 확정
- "이 정도면 신뢰할 수 있다" 판정 완료

✅ 선행연구:
- 10개 논문 데이터베이스화
- 메타분석 완료
- 우리 vs 문헌 일치도 평가
```

---

## 🆘 문제 해결

### 시간이 부족하면?

```
Day N을 완성할 수 없으면:
1. 절대 스킵하지 말 것
2. 대신 "Day N (연장)" 로그 남기기
3. 다음 Day로 넘기지 말 것 (누적되면 망함)
4. PC1에 "연장 필요" 보고
```

### Fabel이 이상한 답변을 주면?

```
1. 일단 받아들이기 (이것도 테스트 데이터)
2. 로그에 명시: "[의문점] Fabel 답변이 ___와 다름"
3. 계속 진행 (Day 5-6에서 문헌으로 검증)
4. 신뢰도 채점표에 반영
```

### 선행연구 논문이 없으면?

```
1. 먼저 확인: Google Scholar, ResearchGate
2. 저자에게 직접 요청 (이메일)
3. 대학 라이브러리 VPN
4. 없으면 PC1에 보고 (대체 논문 찾기)
```

---

## 🎯 최종 목표 (Day 12부터)

```
Day 12-14 (3일):
└─ 옵션 A 논문 최종 마무리 + 투고

Day 15-30 (2주):
└─ 옵션 C 메커니즘 실험 설계 + 수행

Month 2-3 (2개월):
└─ 옵션 C 메커니즘 논문 작성

Month 4-9 (6개월):
└─ 옵션 B 데이터 수집 (n → 100)

Month 10-12 (3개월):
└─ 옵션 B 예측 모델 개발 + 검증

결과:
✅ 11일 후 옵션 A 투고
✅ 4개월 후 옵션 C 투고
✅ 1년 후 옵션 B 투고
```

---

## 💻 기술 팁

### 좋은 마크다운 에디터

```
추천:
1. VS Code (무료, 강력)
2. Obsidian (노트 관리)
3. Typora (깔끔한 UI)
4. Notion (협업)
```

### 파일 관리

```
명명 규칙:
Day01_공정분석.md
Day02_선행연구.md
Day03_Fabel_Query1.md
Day03_Fabel_Response1.md
Day03_비교분석.md
```

### 백업

```
로컬: PC2 로컬 폴더
클라우드: Google Drive / Dropbox (동기화)
버전관리: GitHub (선택)

3중 백업 = 안전
```

---

## 📋 체크리스트 (Day 1 아침)

```
[ ] 이 파일 읽음
[ ] 11Day_Fable_Test_Protocol.md 읽음
[ ] 폴더 구조 만듦 (Day01_Results/ 등)
[ ] n=28 데이터 정리 시작
[ ] 클라우드 동기화 설정 완료
[ ] PC1에 "11일 시작합니다" 보고
[ ] Fabel 접근 테스트 (간단한 질문)
[ ] 오늘 로그 첫 줄 작성: "Day 1: [날짜], 시작"
```

---

**이제 준비가 되었습니다!**

**Day 1을 시작하세요. 화이팅! 💪**

---

**PC1에게**: "PC2 준비 완료. 11일 시작합니다."
**PC2에서**: 11Day_Fable_Test_Protocol.md → Day 1 섹션으로 이동
