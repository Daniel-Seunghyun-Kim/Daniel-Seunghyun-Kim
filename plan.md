# VASP 수동 실행 handoff 기준

- Job: JOB-20260731225010-SRJ6L
- Kind: simulation
- Project: AlN simulation workspace (read_only)
- Tool: VASP
- Requested action: 입력 파일 점검표, 수렴 조건, 수동 실행 및 결과 provenance 기록

## Allowed now

- Prepare an input/checklist in this job staging area.
- Validate paths, units, syntax, and provenance where applicable.
- Record assumptions and expected outputs.

## Not allowed now

- Start the external tool.
- Write to the external project root.
- Treat a generated draft as validated scientific evidence.

## Human approval required before external execution

Review request.json, specify exact command/parameters and output location in approval.json, then run the simulator manually.
