#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
파일 자동 정리 프로그램
날짜와 파일 유형에 따라 파일을 자동으로 정리합니다.
"""

import os
import shutil
from pathlib import Path
from datetime import datetime
from collections import defaultdict
import argparse
import sys
import json


class FileOrganizer:
    """파일을 날짜와 유형별로 자동 정리하는 클래스"""
    
    # 파일 유형별 카테고리 정의
    FILE_CATEGORIES = {
        '문서': ['.pdf', '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx', 
                '.txt', '.rtf', '.odt', '.ods', '.odp', '.csv'],
        '이미지': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.webp', 
                  '.ico', '.tiff', '.tif', '.heic', '.heif'],
        '비디오': ['.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv', '.webm', 
                 '.m4v', '.mpg', '.mpeg', '.3gp'],
        '음악': ['.mp3', '.wav', '.flac', '.aac', '.ogg', '.wma', '.m4a'],
        '압축파일': ['.zip', '.rar', '.7z', '.tar', '.gz', '.bz2', '.xz'],
        '프로그램': ['.exe', '.msi', '.deb', '.rpm', '.dmg', '.pkg', '.app'],
        '코드': ['.py', '.js', '.html', '.css', '.java', '.cpp', '.c', '.h',
                '.php', '.rb', '.go', '.rs', '.ts', '.jsx', '.tsx', '.json',
                '.xml', '.yaml', '.yml', '.sh', '.bat', '.ps1'],
        '기타': []  # 위에 해당하지 않는 모든 파일
    }
    
    def __init__(self, source_dir, target_dir=None, organize_by_date=True, 
                 organize_by_type=False, preserve_structure=True, dry_run=False, log_file=None):
        """
        Args:
            source_dir: 정리할 소스 디렉토리
            target_dir: 정리된 파일을 저장할 타겟 디렉토리 (None이면 source_dir 내에 정리)
            organize_by_date: 날짜별로 정리할지 여부
            organize_by_type: 파일 유형별로 정리할지 여부 (기본값: False, 연관 파일 보존을 위해)
            preserve_structure: 원본 폴더 구조를 보존할지 여부 (기본값: True)
            dry_run: 실제 이동 없이 시뮬레이션만 실행
            log_file: 이동 이력을 저장할 로그 파일 경로 (None이면 자동 생성)
        """
        self.source_dir = Path(source_dir).expanduser().resolve()
        if target_dir:
            self.target_dir = Path(target_dir).expanduser().resolve()
        else:
            self.target_dir = self.source_dir
        
        self.organize_by_date = organize_by_date
        self.organize_by_type = organize_by_type
        self.preserve_structure = preserve_structure
        self.dry_run = dry_run
        
        if not self.source_dir.exists():
            raise ValueError(f"소스 디렉토리가 존재하지 않습니다: {self.source_dir}")
        
        # 통계 정보
        self.stats = defaultdict(int)
        
        # 이동 이력 저장
        if log_file:
            self.log_file = Path(log_file).expanduser().resolve()
        else:
            # 기본 로그 파일 위치: 소스 디렉토리의 .file_organizer_history.json
            self.log_file = self.source_dir / '.file_organizer_history.json'
        
        self.move_history = []
    
    def get_file_category(self, file_path):
        """파일 확장자를 기반으로 카테고리를 반환"""
        ext = file_path.suffix.lower()
        for category, extensions in self.FILE_CATEGORIES.items():
            if ext in extensions:
                return category
        return '기타'
    
    def get_file_date(self, file_path):
        """파일의 수정 날짜를 반환 (YYYY-MM 형식)"""
        try:
            mtime = os.path.getmtime(file_path)
            date = datetime.fromtimestamp(mtime)
            return date.strftime('%Y-%m')
        except OSError:
            return '날짜없음'
    
    def get_related_files_group(self, file_path, all_files):
        """연관된 파일들을 찾아 그룹명을 반환 (파일명 기반)"""
        stem = file_path.stem.lower()
        
        # 같은 이름의 다른 확장자 파일들 찾기
        related_count = 0
        for other_file in all_files:
            if other_file.stem.lower() == stem and other_file != file_path:
                related_count += 1
        
        # 연관 파일이 있으면 그룹명 반환
        if related_count > 0:
            # 파일명의 공통 부분을 그룹명으로 사용
            # 숫자나 특수문자 제거하여 깔끔한 그룹명 생성
            group_name = stem
            # 너무 긴 이름은 자르기
            if len(group_name) > 30:
                group_name = group_name[:30]
            return group_name
        
        return None
    
    def get_original_folder_name(self, file_path):
        """원본 폴더 이름을 반환 (연관 파일 보존용)"""
        relative_path = file_path.relative_to(self.source_dir)
        if len(relative_path.parts) > 1:
            # 원본 폴더 이름 반환
            return relative_path.parts[0]
        return None
    
    def generate_target_path(self, file_path, all_files=None):
        """파일의 목적지 경로를 생성 (연관 파일 보존)"""
        relative_path = file_path.relative_to(self.source_dir)
        
        # 이미 정리된 폴더 구조 내에 있으면 건너뛰기
        parts = relative_path.parts
        if len(parts) > 1:
            # 날짜 폴더나 카테고리 폴더 안에 있으면 건너뛰기
            if parts[0] in self.FILE_CATEGORIES.keys() or \
               (len(parts[0]) == 7 and parts[0].count('-') == 1):  # YYYY-MM 형식
                return None
        
        target_parts = []
        
        # 날짜별 정리
        if self.organize_by_date:
            date = self.get_file_date(file_path)
            target_parts.append(date)
        
        # 연관 파일 보존 모드
        if self.preserve_structure:
            # 원본 폴더 구조 보존
            original_folder = self.get_original_folder_name(file_path)
            if original_folder:
                target_parts.append(original_folder)
            else:
                # 같은 폴더에 없으면 파일명 기반 그룹화
                if all_files:
                    group_name = self.get_related_files_group(file_path, all_files)
                    if group_name:
                        target_parts.append(group_name)
        elif self.organize_by_type:
            # 유형별 정리 (기본값은 비활성화)
            category = self.get_file_category(file_path)
            target_parts.append(category)
        
        if target_parts:
            target_path = self.target_dir / Path(*target_parts) / file_path.name
        else:
            target_path = self.target_dir / file_path.name
        
        return target_path
    
    def handle_duplicate(self, source_path, target_path):
        """중복 파일 처리 (이름에 번호 추가)"""
        if not target_path.exists():
            return target_path
        
        stem = target_path.stem
        suffix = target_path.suffix
        parent = target_path.parent
        counter = 1
        
        while True:
            new_name = f"{stem}_{counter}{suffix}"
            new_path = parent / new_name
            if not new_path.exists():
                return new_path
            counter += 1
    
    def organize_file(self, file_path, all_files=None):
        """단일 파일을 정리"""
        if file_path.is_dir():
            return
        
        target_path = self.generate_target_path(file_path, all_files)
        if target_path is None:
            return  # 이미 정리된 파일
        
        # 중복 처리
        target_path = self.handle_duplicate(file_path, target_path)
        
        # 타겟 디렉토리 생성
        target_path.parent.mkdir(parents=True, exist_ok=True)
        
        if not self.dry_run:
            try:
                # 원본 경로 저장 (복구용)
                original_path = str(file_path)
                target_path_str = str(target_path)
                
                shutil.move(original_path, target_path_str)
                self.stats['이동됨'] += 1
                print(f"✓ {file_path.name} → {target_path.relative_to(self.target_dir)}")
                
                # 이동 이력 기록
                self.move_history.append({
                    'original': original_path,
                    'moved_to': target_path_str,
                    'timestamp': datetime.now().isoformat(),
                    'filename': file_path.name
                })
            except Exception as e:
                self.stats['오류'] += 1
                print(f"✗ 오류: {file_path.name} - {e}")
        else:
            self.stats['시뮬레이션'] += 1
            print(f"[시뮬레이션] {file_path.name} → {target_path.relative_to(self.target_dir)}")
    
    def organize(self, recursive=True):
        """디렉토리 내의 모든 파일을 정리"""
        print(f"\n{'='*60}")
        print(f"파일 정리 시작")
        print(f"소스 디렉토리: {self.source_dir}")
        print(f"타겟 디렉토리: {self.target_dir}")
        print(f"날짜별 정리: {'예' if self.organize_by_date else '아니오'}")
        print(f"유형별 정리: {'예' if self.organize_by_type else '아니오'}")
        print(f"구조 보존: {'예' if self.preserve_structure else '아니오'}")
        print(f"시뮬레이션 모드: {'예' if self.dry_run else '아니오'}")
        print(f"{'='*60}\n")
        
        # 파일 스캔 중 진행 상황 표시
        print("파일 스캔 중... (시간이 걸릴 수 있습니다)")
        sys.stdout.flush()
        
        files = []
        file_count = 0
        
        if recursive:
            # 재귀적으로 파일 찾기 (진행 상황 표시)
            for item in self.source_dir.rglob('*'):
                if item.is_file():
                    files.append(item)
                    file_count += 1
                    # 100개마다 진행 상황 출력
                    if file_count % 100 == 0:
                        print(f"  스캔 중... {file_count}개 파일 발견", end='\r')
                        sys.stdout.flush()
        else:
            # 현재 디렉토리만
            for item in self.source_dir.iterdir():
                if item.is_file():
                    files.append(item)
                    file_count += 1
        
        print(f"\n총 {len(files)}개의 파일을 찾았습니다.\n")
        
        if not files:
            print("정리할 파일이 없습니다.")
            return
        
        # 파일 처리 (진행률 표시)
        total = len(files)
        for idx, file_path in enumerate(files, 1):
            # 10개마다 또는 마지막 파일일 때 진행률 출력
            if idx % 10 == 0 or idx == total:
                progress = (idx / total) * 100
                print(f"처리 중: {idx}/{total} ({progress:.1f}%)", end='\r')
                sys.stdout.flush()
            
            self.organize_file(file_path, all_files=files)
        
        print()  # 진행률 출력 후 줄바꿈
        
        # 이동 이력 저장
        if not self.dry_run and self.move_history:
            self._save_history()
        
        # 통계 출력
        print(f"\n{'='*60}")
        print("정리 완료!")
        print(f"{'='*60}")
        for key, value in self.stats.items():
            print(f"{key}: {value}개")
        if not self.dry_run and self.move_history:
            print(f"이동 이력 저장: {self.log_file}")
        print(f"{'='*60}\n")
    
    def _save_history(self):
        """이동 이력을 파일에 저장"""
        try:
            # 기존 이력이 있으면 불러오기
            if self.log_file.exists():
                with open(self.log_file, 'r', encoding='utf-8') as f:
                    existing_history = json.load(f)
            else:
                existing_history = []
            
            # 새 이력 추가
            existing_history.extend(self.move_history)
            
            # 저장
            with open(self.log_file, 'w', encoding='utf-8') as f:
                json.dump(existing_history, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"경고: 이동 이력 저장 실패 - {e}")


def main():
    parser = argparse.ArgumentParser(
        description='파일을 날짜와 유형별로 자동 정리하는 프로그램',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
사용 예시:
  # 현재 디렉토리 정리 (시뮬레이션)
  python file_organizer.py . --dry-run
  
  # 특정 디렉토리 정리
  python file_organizer.py ~/Downloads
  
  # 날짜별로만 정리
  python file_organizer.py ~/Downloads --no-type
  
  # 유형별로만 정리
  python file_organizer.py ~/Downloads --no-date
        """
    )
    
    parser.add_argument('source_dir', nargs='?', default='.',
                       help='정리할 소스 디렉토리 경로 (기본값: 현재 디렉토리)')
    parser.add_argument('-t', '--target-dir',
                       help='정리된 파일을 저장할 타겟 디렉토리 (기본값: 소스 디렉토리)')
    parser.add_argument('--no-date', action='store_true',
                       help='날짜별 정리 비활성화')
    parser.add_argument('--no-type', action='store_true',
                       help='유형별 정리 비활성화 (기본값: 비활성화, 연관 파일 보존)')
    parser.add_argument('--type', action='store_true',
                       help='유형별 정리 활성화 (확장자 기반 분류)')
    parser.add_argument('--no-preserve', action='store_true',
                       help='원본 폴더 구조 보존 비활성화 (기본값: 보존)')
    parser.add_argument('--no-recursive', action='store_true',
                       help='하위 디렉토리 검색 비활성화')
    parser.add_argument('--dry-run', action='store_true',
                       help='실제 이동 없이 시뮬레이션만 실행')
    
    args = parser.parse_args()
    
    try:
        # 유형별 정리: --type 옵션이 있으면 활성화, --no-type이 있으면 비활성화
        # 기본값은 False (연관 파일 보존을 위해)
        organize_by_type = args.type if args.type else (not args.no_type if args.no_type else False)
        
        organizer = FileOrganizer(
            source_dir=args.source_dir,
            target_dir=args.target_dir,
            organize_by_date=not args.no_date,
            organize_by_type=organize_by_type,
            preserve_structure=not args.no_preserve,
            dry_run=args.dry_run
        )
        
        organizer.organize(recursive=not args.no_recursive)
        
    except KeyboardInterrupt:
        print("\n\n사용자에 의해 중단되었습니다.")
        sys.exit(1)
    except Exception as e:
        print(f"\n오류 발생: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
