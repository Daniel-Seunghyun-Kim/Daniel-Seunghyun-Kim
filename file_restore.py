#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
파일 분류 복구 프로그램
파일 분류 전 상태로 복구하는 프로그램입니다.
Git 히스토리를 사용하여 이전 상태로 복구합니다.
"""

import os
import shutil
import subprocess
from pathlib import Path
from datetime import datetime
import argparse
import sys


class FileRestorer:
    """파일 분류 전 상태로 복구하는 클래스"""
    
    def __init__(self, target_dir='.', commit_hash=None, dry_run=False):
        """
        Args:
            target_dir: 복구할 디렉토리 (기본값: 현재 디렉토리)
            commit_hash: 복구할 커밋 해시 (None이면 파일 분류 전 커밋 자동 탐지)
            dry_run: 실제 복구 없이 시뮬레이션만 실행
        """
        self.target_dir = Path(target_dir).expanduser().resolve()
        self.commit_hash = commit_hash
        self.dry_run = dry_run
        
        if not self.target_dir.exists():
            raise ValueError(f"디렉토리가 존재하지 않습니다: {self.target_dir}")
        
        # 통계 정보
        self.stats = {
            '복구됨': 0,
            '오류': 0,
            '변경없음': 0,
            '시뮬레이션': 0
        }
    
    def is_git_repo(self):
        """현재 디렉토리가 Git 저장소인지 확인"""
        try:
            result = subprocess.run(
                ['git', 'rev-parse', '--git-dir'],
                cwd=self.target_dir,
                capture_output=True,
                text=True,
                check=False
            )
            return result.returncode == 0
        except FileNotFoundError:
            return False
    
    def find_pre_organize_commit(self):
        """파일 분류 전 커밋 찾기"""
        try:
            # 파일 분류 관련 커밋 찾기
            result = subprocess.run(
                ['git', 'log', '--all', '--oneline', '--grep=organize', '-i'],
                cwd=self.target_dir,
                capture_output=True,
                text=True,
                check=True
            )
            
            if result.stdout.strip():
                # 파일 분류 커밋 찾기
                lines = result.stdout.strip().split('\n')
                if lines:
                    # 첫 번째 파일 분류 커밋의 부모 커밋 찾기
                    organize_commit = lines[0].split()[0]
                    result = subprocess.run(
                        ['git', 'rev-parse', f'{organize_commit}^'],
                        cwd=self.target_dir,
                        capture_output=True,
                        text=True,
                        check=True
                    )
                    return result.stdout.strip()
            
            # 파일 분류 커밋을 찾지 못한 경우, HEAD의 부모 또는 최근 커밋 사용
            result = subprocess.run(
                ['git', 'log', '--oneline', '-10'],
                cwd=self.target_dir,
                capture_output=True,
                text=True,
                check=True
            )
            
            if result.stdout.strip():
                # 두 번째 커밋 사용 (현재 HEAD가 파일 분류 후라면)
                lines = result.stdout.strip().split('\n')
                if len(lines) > 1:
                    return lines[1].split()[0]
                elif len(lines) == 1:
                    return lines[0].split()[0]
            
            return None
            
        except subprocess.CalledProcessError:
            return None
    
    def get_commit_file_list(self, commit_hash):
        """특정 커밋의 파일 목록 가져오기"""
        try:
            result = subprocess.run(
                ['git', 'ls-tree', '-r', '--name-only', commit_hash],
                cwd=self.target_dir,
                capture_output=True,
                text=True,
                check=True
            )
            
            files = []
            for line in result.stdout.strip().split('\n'):
                if line.strip():
                    files.append(Path(line.strip()))
            
            return files
            
        except subprocess.CalledProcessError:
            return []
    
    def restore_file_from_commit(self, file_path, commit_hash):
        """커밋에서 파일 복구"""
        try:
            # Git에서 파일 내용 가져오기
            result = subprocess.run(
                ['git', 'show', f'{commit_hash}:{file_path}'],
                cwd=self.target_dir,
                capture_output=True,
                text=False,
                check=True
            )
            
            target_path = self.target_dir / file_path
            
            if not self.dry_run:
                # 디렉토리 생성
                target_path.parent.mkdir(parents=True, exist_ok=True)
                
                # 파일 쓰기
                with open(target_path, 'wb') as f:
                    f.write(result.stdout)
                
                self.stats['복구됨'] += 1
                print(f"✓ 복구: {file_path}")
                return True
            else:
                self.stats['시뮬레이션'] += 1
                print(f"[시뮬레이션] 복구: {file_path}")
                return True
                
        except subprocess.CalledProcessError:
            # 파일이 해당 커밋에 없을 수 있음
            self.stats['오류'] += 1
            print(f"✗ 오류: {file_path} (커밋에 없음)")
            return False
        except Exception as e:
            self.stats['오류'] += 1
            print(f"✗ 오류: {file_path} - {e}")
            return False
    
    def restore_directory_structure(self, commit_hash):
        """디렉토리 구조 복구"""
        files = self.get_commit_file_list(commit_hash)
        
        if not files:
            print("복구할 파일이 없습니다.")
            return
        
        print(f"\n총 {len(files)}개의 파일을 복구합니다.\n")
        
        # 파일 복구
        total = len(files)
        for idx, file_path in enumerate(files, 1):
            if idx % 10 == 0 or idx == total:
                progress = (idx / total) * 100
                print(f"처리 중: {idx}/{total} ({progress:.1f}%)", end='\r')
                sys.stdout.flush()
            
            self.restore_file_from_commit(file_path, commit_hash)
        
        print()  # 진행률 출력 후 줄바꿈
    
    def restore_using_git_checkout(self, commit_hash):
        """Git checkout을 사용하여 전체 복구"""
        if self.dry_run:
            print(f"[시뮬레이션] Git checkout으로 복구: {commit_hash}")
            print(f"[시뮬레이션] 명령어: git checkout {commit_hash} -- .")
            return
        
        try:
            # 작업 디렉토리의 변경사항 확인
            result = subprocess.run(
                ['git', 'status', '--porcelain'],
                cwd=self.target_dir,
                capture_output=True,
                text=True,
                check=True
            )
            
            if result.stdout.strip():
                print("경고: 작업 디렉토리에 변경사항이 있습니다.")
                response = input("계속하시겠습니까? (y/N): ")
                if response.lower() != 'y':
                    print("취소되었습니다.")
                    return
            
            # 특정 커밋의 파일들로 복구
            result = subprocess.run(
                ['git', 'checkout', commit_hash, '--', '.'],
                cwd=self.target_dir,
                capture_output=True,
                text=True,
                check=True
            )
            
            print(f"✓ Git checkout으로 복구 완료: {commit_hash}")
            self.stats['복구됨'] = 1  # 전체 복구로 카운트
            
        except subprocess.CalledProcessError as e:
            print(f"✗ 오류 발생: {e.stderr}")
            self.stats['오류'] += 1
        except KeyboardInterrupt:
            print("\n\n사용자에 의해 중단되었습니다.")
            sys.exit(1)
    
    def restore(self, use_git_checkout=True):
        """파일 복구 실행"""
        if not self.is_git_repo():
            print("오류: 현재 디렉토리가 Git 저장소가 아닙니다.")
            print("Git 저장소에서만 파일 복구가 가능합니다.")
            return
        
        # 복구할 커밋 결정
        if not self.commit_hash:
            print("파일 분류 전 커밋을 찾는 중...")
            self.commit_hash = self.find_pre_organize_commit()
            
            if not self.commit_hash:
                print("오류: 복구할 커밋을 찾을 수 없습니다.")
                print("--commit 옵션으로 커밋 해시를 직접 지정해주세요.")
                return
        
        print(f"\n{'='*60}")
        print(f"파일 복구 시작")
        print(f"대상 디렉토리: {self.target_dir}")
        print(f"복구 커밋: {self.commit_hash}")
        print(f"시뮬레이션 모드: {'예' if self.dry_run else '아니오'}")
        print(f"{'='*60}\n")
        
        # 커밋 정보 확인
        try:
            result = subprocess.run(
                ['git', 'show', '--oneline', '-s', self.commit_hash],
                cwd=self.target_dir,
                capture_output=True,
                text=True,
                check=True
            )
            print(f"커밋 정보: {result.stdout.strip()}\n")
        except subprocess.CalledProcessError:
            print(f"경고: 커밋 {self.commit_hash}을 찾을 수 없습니다.")
            return
        
        if use_git_checkout:
            self.restore_using_git_checkout(self.commit_hash)
        else:
            self.restore_directory_structure(self.commit_hash)
        
        # 통계 출력
        print(f"\n{'='*60}")
        print("복구 완료!")
        print(f"{'='*60}")
        for key, value in self.stats.items():
            if value > 0:
                print(f"{key}: {value}개")
        print(f"{'='*60}\n")


def main():
    parser = argparse.ArgumentParser(
        description='파일 분류 전 상태로 복구하는 프로그램',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
사용 예시:
  # 현재 디렉토리를 파일 분류 전 상태로 복구 (시뮬레이션)
  python file_restore.py . --dry-run
  
  # 특정 디렉토리 복구
  python file_restore.py ~/Documents
  
  # 특정 커밋으로 복구
  python file_restore.py . --commit 9b36c09
  
  # Git checkout 대신 파일별 복구
  python file_restore.py . --no-git-checkout
        """
    )
    
    parser.add_argument('target_dir', nargs='?', default='.',
                       help='복구할 디렉토리 경로 (기본값: 현재 디렉토리)')
    parser.add_argument('-c', '--commit',
                       help='복구할 커밋 해시 (기본값: 파일 분류 전 커밋 자동 탐지)')
    parser.add_argument('--no-git-checkout', action='store_true',
                       help='Git checkout 대신 파일별로 복구')
    parser.add_argument('--dry-run', action='store_true',
                       help='실제 복구 없이 시뮬레이션만 실행')
    
    args = parser.parse_args()
    
    try:
        restorer = FileRestorer(
            target_dir=args.target_dir,
            commit_hash=args.commit,
            dry_run=args.dry_run
        )
        
        restorer.restore(use_git_checkout=not args.no_git_checkout)
        
    except KeyboardInterrupt:
        print("\n\n사용자에 의해 중단되었습니다.")
        sys.exit(1)
    except Exception as e:
        print(f"\n오류 발생: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
