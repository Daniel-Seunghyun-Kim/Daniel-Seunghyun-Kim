from __future__ import annotations

import csv
import hashlib
import json
import re
import shutil
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parent
STAMP = "2026-10-09"
DEST = ROOT / f"주제별_마크다운_모음_{STAMP}"


def category_for(path: Path) -> str:
    parts = [p.lower() for p in path.relative_to(ROOT).parts]
    text = "/".join(parts)
    if "00_raw/ingested_markdowns" in text:
        return "raw_imports"
    if "curated_papers" in text:
        if "aln" in text or "sputter" in text:
            return "aln_sputtering"
        if "thermal" in text or "phonon" in text:
            return "thermal_phonon_literature"
        if "packag" in text or "bond" in text:
            return "packaging_bonding_literature"
        if "quantum" in text or "molecular" in text or "dft" in text:
            return "dft_md_literature"
        return "curated_literature_other"
    topic_map = {
        "01_pvd_sputtering": "pvd_sputtering",
        "02_etch_chemistry": "etch_chemistry",
        "03_quantum_phonon": "quantum_phonon",
        "04_transport_cooling": "transport_cooling",
        "05_packaging_bonding": "packaging_bonding",
        "06_multiscale_sim": "multiscale_simulation",
        "07_digitaltwin_ai": "digital_twin_ai",
        "projects": "projects",
        "decisions": "decisions",
        "skills": "skills",
    }
    for key, value in topic_map.items():
        if key in text:
            return value
    if path.parent == ROOT:
        return "project_root"
    if "research_reviews" in text:
        return "research_reviews"
    if "20_meta" in text:
        return "metadata_policy"
    return "other_workspace_markdown"


def safe_name(name: str) -> str:
    name = re.sub(r"[<>:\"/\\|?*\x00-\x1f]", "_", name)
    return name[:180]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def main() -> None:
    DEST.mkdir(exist_ok=True)
    source_files = sorted(
        p for p in ROOT.rglob("*.md")
        if DEST not in p.parents and ".git" not in p.parts
    )
    rows: list[dict[str, object]] = []
    used: set[tuple[str, str]] = set()
    for source in source_files:
        rel = source.relative_to(ROOT)
        category = category_for(source)
        digest = sha256(source)
        base = safe_name(source.stem)
        target_name = f"{digest[:10]}__{base}{source.suffix.lower()}"
        key = (category, target_name.lower())
        if key in used:
            relative_tag = hashlib.sha256(str(rel).encode("utf-8")).hexdigest()[:10]
            target_name = f"{digest[:16]}_{relative_tag}__{base}{source.suffix.lower()}"
        used.add((category, target_name.lower()))
        target_dir = DEST / category
        target_dir.mkdir(parents=True, exist_ok=True)
        target = target_dir / target_name
        shutil.copy2(source, target)
        rows.append({
            "category": category,
            "source_relative": str(rel),
            "source_absolute": str(source),
            "copied_relative": str(target.relative_to(DEST)),
            "bytes": source.stat().st_size,
            "sha256": digest,
            "source_mtime": datetime.fromtimestamp(source.stat().st_mtime).isoformat(),
        })

    manifest = DEST / "manifest.json"
    manifest.write_text(json.dumps({
        "created_at": datetime.now().astimezone().isoformat(),
        "requested_date": STAMP,
        "scope": "All Markdown files present below D:\\PS\\PreviousTheme at collection time, excluding the output directory and .git.",
        "chat_scope": "ChatGPT/Codex account conversations are indexed separately; this filesystem collector cannot bulk-export chat originals.",
        "file_count": len(rows),
        "categories": {k: sum(1 for row in rows if row["category"] == k) for k in sorted({str(r["category"]) for r in rows})},
        "files": rows,
    }, ensure_ascii=False, indent=2), encoding="utf-8")
    with (DEST / "manifest.csv").open("w", newline="", encoding="utf-8-sig") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()) if rows else ["category"])
        writer.writeheader()
        writer.writerows(rows)

    readme = DEST / "README.md"
    readme.write_text(f"""# 주제별 Markdown 모음 ({STAMP})

이 폴더는 `{ROOT}` 아래에 있던 Markdown 파일을 원본 경로와 SHA-256으로 기록한 뒤 주제별로 복사한 보관본이다.

- 수집 파일 수: **{len(rows)}**
- 원본 보존: 원본 파일은 이동·삭제하지 않았다.
- 검증: 각 파일의 SHA-256은 `manifest.json`과 `manifest.csv`에 기록했다.
- 채팅 범위: Codex/ChatGPT 전체 계정 대화 원문은 이 환경의 bulk-export API가 없어 자동 다운로드할 수 없다. 접근 가능한 채팅 목록과 확인된 제목/요약은 별도 색인에 기록한다.
- `raw_imports`는 원시 import/vendor Markdown을 분리한 것이다. 연구 주제 파일만 보려면 다른 주제 폴더를 사용한다.

## 폴더

각 폴더의 파일명 앞 10자리 해시는 이름 충돌을 피하기 위한 식별자이며, 원래 경로는 manifest에서 확인한다.
""", encoding="utf-8")


if __name__ == "__main__":
    main()
