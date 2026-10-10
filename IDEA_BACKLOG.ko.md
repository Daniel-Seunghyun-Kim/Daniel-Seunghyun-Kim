# 반도체 연구 운영체제: 확장 아이디어 백로그

아래 항목은 연구 결과나 문헌 사실을 주장하지 않는 작업 설계안입니다. 각 항목은 실제 근거와 입력을 확인한 뒤 독립된 IDEA 또는 JOB 패킷으로 전환합니다.

| 우선순위 | 연구 패킷 | 연결되는 주제 | 산출물 | 로컬 도구 경계 |
| --- | --- | --- | --- | --- |
| 1 | Evidence-first literature loop | AlN, IGZO, ferroelectricity, thin-film process | source map, 직접/추론 분리 노트, 인용 점검표 | PDF는 manifest/사용자 검토 후에만 외부 모델로 전송 |
| 2 | Process-structure-property map | sputtering/anneal/etch, microscopy, electrical measurement | 변수표, 제어군, 측정 체크리스트 | 실험 원본은 읽기·해시·사람 검토만 |
| 3 | TCAD handoff packet | IGZO device, contact/gate stack, Vg-VD studies | DeckBuild 입력 초안, parameter diff, validation checklist | Silvaco는 launcher 경로 점검과 준비까지만 |
| 4 | DFT manual handoff | AlN surface/interface/defect hypotheses | POSCAR/INCAR/KPOINTS checklist, convergence plan, result manifest | VASP 실행·재시작·삭제는 항상 사용자가 수동 수행 |
| 5 | Multiphysics bridge | thermal/mechanical/electrical hypotheses | COMSOL model assumptions, mesh/BC checklist, output location plan | COMSOL batch는 승인 전에는 실행하지 않음 |
| 6 | Figure-to-manuscript chain | Origin graphs, captions, discussion | figure provenance, caption draft, claims-to-evidence table | Origin은 GUI 수동 작업; 원고 원본 자동 덮어쓰기 금지 |
| 7 | Failure knowledge base | TCAD/DFT/experiment unsuccessful runs | failure manifest, suspected cause, next discriminating check | 실패는 자동 수정·PASS가 아닌 재현 가능한 기록 |
| 8 | Model review loop | code, writing, search, peer-style critique | provider-separated drafts and comparison note | 구독 서비스는 manual_import; 자동 failover 없음 |

## 권장 첫 세 개

1. AlN evidence packet: 연구 질문 하나를 정하고, source map과 가정/반증 조건을 붙입니다.
2. IGZO TCAD packet: 기존 deck을 수정하지 않고 prepare 작업으로 입력 diff·검증 기준·예상 출력만 기록합니다.
3. VASP manual handoff: 실행 스크립트를 자동화하지 않고, 필요한 입력 세트·수렴 조건·결과 provenance만 표준화합니다.

## 매 패킷의 공통 질문

- 무엇이 직접 근거이고 무엇이 가설인가?
- 어떤 입력 파일과 버전을 썼는가?
- 어떤 결과가 가설을 반증하는가?
- 사람이 승인해야 할 외부 실행/전송 지점은 어디인가?
- 다음 단계가 문헌, 시뮬레이션, 실험, 그림, 원고 중 어디로 이어지는가?

이 구조를 쓰면 AI가 답변을 늘리는 대신, 시간이 지나도 재사용 가능한 연구 결정과 근거가 축적됩니다.
