#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
파일 복구 프로그램
file_organizer.py로 이동된 파일들을 원래 위치로 복구합니다.
"""

import os
import shutil
import json
from pathlib import Path
import argparse
import sys
from datetime import datetime


class FileRestorer:
    """파일을 원래 위치로 복구하는 클래스"""
    
    def __init__(self, log_file, dry_run=False):
        """
        Args:
            log_file: 이동 이력이 저장된 로그 파일 경로
            dry_run: 실제 복구 없이 시뮬레이션만 실행
        """
        self.log_file = Path(log_file).expanduser().resolve()
        self.dry_run = dry_run
        
        if not self.log_file.exists():
            raise ValueError(f"로그 파일이 존재하지 않습니다: {self.log_file}")
        
        self.stats = {
            '복구됨': 0,
            '오류': 0,
            '파일없음': 0,
            '이미존재': 0
        }
    
    def load_history(self):
        """이동 이력을 로드"""
        try:
            with open(self.log_file, 'r', encoding='utf-8') as f:
                history = json.load(f)
            return history
        except Exception as e:
            raise ValueError(f"로그 파일을 읽을 수 없습니다: {e}")
    
    def restore_file(self, entry):
        """단일 파일을 복구"""
        moved_to = Path(entry['moved_to'])
        original = Path(entry['original'])
        filename = entry.get('filename', moved_to.name)
        
        # 이동된 파일이 존재하는지 확인
        if not moved_to.exists():
            self.stats['파일없음'] += 1
            print(f"⚠ 파일 없음: {moved_to.name} (원본: {original})")
            return False
        
        # 원본 위치의 디렉토리가 없으면 생성
        original.parent.mkdir(parents=True, exist_ok=True)
        
        # 원본 위치에 이미 파일이 있는지 확인
        if original.exists():
            self.stats['이미존재'] += 1
            print(f"⚠ 이미 존재: {original} (건너뜀)")
            return False
        
        if not self.dry_run:
            try:
                shutil.move(str(moved_to), str(original))
                self.stats['복구됨'] += 1
                print(f"✓ {filename} → {original}")
                return True
            except Exception as e:
                self.stats['오류'] += 1
                print(f"✗ 오류: {filename} - {e}")
                return False
        else:
            self.stats['복구됨'] += 1
            print(f"[시뮬레이션] {filename} → {original}")
            return True
    
    def restore(self, reverse_order=True):
        """
        모든 파일을 복구
        
        Args:
            reverse_order: True면 최신 이동부터 역순으로 복구 (기본값: True)
        """
        print(f"\n{'='*60}")
        print("파일 복구 시작")
        print(f"로그 파일: {self.log_file}")
        print(f"시뮬레이션 모드: {'예' if self.dry_run else '아니오'}")
        print(f"{'='*60}\n")
        
        history = self.load_history()
        
        if not history:
            print("복구할 파일이 없습니다.")
            return
        
        print(f"총 {len(history)}개의 이동 기록을 찾았습니다.\n")
        
        # 역순으로 정렬 (최신 것부터 복구)
        if reverse_order:
            history = list(reversed(history))
        
        # 복구 실행
        for idx, entry in enumerate(history, 1):
            if idx % 10 == 0 or idx == len(history):
                progress = (idx / len(history)) * 100
                print(f"처리 중: {idx}/{len(history)} ({progress:.1f}%)", end='\r')
                sys.stdout.flush()
            
            self.restore_file(entry)
        
        print()  # 진행률 출력 후 줄바꿈
        
        # 통계 출력
        print(f"\n{'='*60}")
        print("복구 완료!")
        print(f"{'='*60}")
        for key, value in self.stats.items():
            print(f"{key}: {value}개")
        print(f"{'='*60}\n")
    
    def list_history(self):
        """이동 이력을 목록으로 표시"""
        history = self.load_history()
        
        if not history:
            print("이동 기록이 없습니다.")
            return
        
        print(f"\n{'='*60}")
        print(f"총 {len(history)}개의 이동 기록")
        print(f"{'='*60}\n")
        
        for idx, entry in enumerate(history, 1):
            timestamp = entry.get('timestamp', '알 수 없음')
            filename = entry.get('filename', Path(entry['moved_to']).name)
            original = entry['original']
            moved_to = entry['moved_to']
            
            # 파일 존재 여부 확인
            exists = "✓" if Path(moved_to).exists() else "✗"
            
            print(f"{idx}. {exists} {filename}")
            print(f"   원본: {original}")
            print(f"   이동: {moved_to}")
            print(f"   시간: {timestamp}")
            print()
    
    def clear_history(self):
        """이동 이력 파일 삭제"""
        if not self.dry_run:
            try:
                self.log_file.unlink()
                print(f"이동 이력 파일이 삭제되었습니다: {self.log_file}")
            except Exception as e:
                print(f"오류: 이력 파일 삭제 실패 - {e}")
        else:
            print(f"[시뮬레이션] 이력 파일 삭제: {self.log_file}")


def main():
    parser = argparse.ArgumentParser(
        description='file_organizer.py로 이동된 파일들을 원래 위치로 복구',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
사용 예시:
  # 이동 이력 목록 보기
  python file_restorer.py -l ~/Downloads/.file_organizer_history.json
  
  # 시뮬레이션으로 복구 확인
  python file_restorer.py ~/Downloads/.file_organizer_history.json --dry-run
  
  # 실제로 복구 실행
  python file_restorer.py ~/Downloads/.file_organizer_history.json
  
  # 자동으로 로그 파일 찾기
  python file_restorer.py --auto ~/Downloads
        """
    )
    
    parser.add_argument('log_file', nargs='?',
                       help='이동 이력 로그 파일 경로')
    parser.add_argument('--auto', '-a',
                       help='지정한 디렉토리에서 자동으로 로그 파일 찾기')
    parser.add_argument('--list', '-l', action='store_true',
                       help='이동 이력 목록만 표시 (복구하지 않음)')
    parser.add_argument('--clear', action='store_true',
                       help='복구 후 이력 파일 삭제')
    parser.add_argument('--dry-run', action='store_true',
                       help='실제 복구 없이 시뮬레이션만 실행')
    parser.add_argument('--no-reverse', action='store_true',
                       help='이동 순서대로 복구 (기본값: 역순)')
    
    args = parser.parse_args()
    
    # 자동 모드
    if args.auto:
        source_dir = Path(args.auto).expanduser().resolve()
        log_file = source_dir / '.file_organizer_history.json'
        if not log_file.exists():
            print(f"오류: 로그 파일을 찾을 수 없습니다: {log_file}", file=sys.stderr)
            sys.exit(1)
    elif args.log_file:
        log_file = args.log_file
    else:
        # 현재 디렉토리에서 자동으로 찾기
        current_dir = Path.cwd()
        log_file = current_dir / '.file_organizer_history.json'
        if not log_file.exists():
            print("오류: 로그 파일을 지정하거나 --auto 옵션을 사용하세요.", file=sys.stderr)
            parser.print_help()
            sys.exit(1)
    
    try:
        restorer = FileRestorer(log_file, dry_run=args.dry_run)
        
        if args.list:
            restorer.list_history()
        else:
            restorer.restore(reverse_order=not args.no_reverse)
            
            if args.clear and not args.dry_run:
                confirm = input("\n이동 이력 파일을 삭제하시겠습니까? (y/N): ")
                if confirm.lower() == 'y':
                    restorer.clear_history()
        
    except KeyboardInterrupt:
        print("\n\n사용자에 의해 중단되었습니다.")
        sys.exit(1)
    except Exception as e:
        print(f"\n오류 발생: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
