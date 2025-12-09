#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
파일 분류 복구 프로그램
파일 분류 전 상태로 복구하는 프로그램입니다.
Git 히스토리 또는 분류된 폴더 구조를 역으로 추적하여 복구합니다.
"""

import os
import shutil
import subprocess
import json
from pathlib import Path
from datetime import datetime
import re
import argparse
import sys


class FileRestorer:
    """파일 분류 전 상태로 복구하는 클래스"""
    
    # 파일 분류 프로그램에서 사용하는 카테고리 목록
    FILE_CATEGORIES = [
        '문서', '이미지', '비디오', '음악', '압축파일', 
        '프로그램', '코드', '기타'
    ]
    
    def __init__(self, target_dir='.', commit_hash=None, restore_dir=None, dry_run=False):
        """
        Args:
            target_dir: 복구할 디렉토리 (기본값: 현재 디렉토리)
            commit_hash: 복구할 커밋 해시 (Git 저장소인 경우)
            restore_dir: 파일을 복구할 디렉토리 (None이면 target_dir의 루트로)
            dry_run: 실제 복구 없이 시뮬레이션만 실행
        """
        self.target_dir = Path(target_dir).expanduser().resolve()
        self.commit_hash = commit_hash
        self.restore_dir = Path(restore_dir).expanduser().resolve() if restore_dir else self.target_dir
        self.dry_run = dry_run
        
        if not self.target_dir.exists():
            raise ValueError(f"디렉토리가 존재하지 않습니다: {self.target_dir}")
        
        # 통계 정보
        self.stats = {
            '복구됨': 0,
            '오류': 0,
            '변경없음': 0,
            '시뮬레이션': 0,
            '빈폴더삭제': 0
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
    
    def is_organized_folder(self, folder_name):
        """폴더 이름이 분류된 폴더인지 확인"""
        # 카테고리 폴더인지 확인
        if folder_name in self.FILE_CATEGORIES:
            return True
        
        # 날짜 형식인지 확인 (YYYY-MM)
        date_pattern = re.compile(r'^\d{4}-\d{2}$')
        if date_pattern.match(folder_name):
            return True
        
        return False
    
    def find_organized_files(self):
        """분류된 파일들을 찾기"""
        organized_files = []
        
        # 모든 파일 찾기
        for item in self.target_dir.rglob('*'):
            if not item.is_file():
                continue
            
            # 상대 경로 가져오기
            try:
                relative_path = item.relative_to(self.target_dir)
                parts = relative_path.parts
                
                # 분류된 폴더 구조인지 확인
                # 형식: 카테고리/YYYY-MM/파일명 또는 카테고리/파일명 또는 YYYY-MM/파일명
                if len(parts) >= 2:
                    first_part = parts[0]
                    if self.is_organized_folder(first_part):
                        organized_files.append((item, relative_path, parts))
                    elif len(parts) >= 3:
                        # 카테고리/날짜/파일명 형식
                        second_part = parts[1]
                        if (first_part in self.FILE_CATEGORIES and 
                            self.is_organized_folder(second_part)):
                            organized_files.append((item, relative_path, parts))
            
            except ValueError:
                # 상대 경로를 만들 수 없는 경우 (심볼릭 링크 등)
                continue
        
        return organized_files
    
    def load_organize_log(self):
        """파일 분류 로그 파일 로드"""
        log_file = self.target_dir / '.file_organizer_log.json'
        
        if not log_file.exists():
            return None
        
        try:
            with open(log_file, 'r', encoding='utf-8') as f:
                log_data = json.load(f)
            return log_data
        except (json.JSONDecodeError, IOError) as e:
            print(f"경고: 로그 파일을 읽을 수 없습니다: {e}")
            return None
    
    def restore_from_log(self):
        """로그 파일을 사용하여 원래 위치로 복구"""
        print("이동 로그 파일을 찾는 중...")
        log_data = self.load_organize_log()
        
        if not log_data:
            print("이동 로그 파일을 찾을 수 없습니다.")
            print("파일 분류 프로그램이 로그를 생성하지 않았거나 이미 삭제되었을 수 있습니다.")
            return False
        
        if not isinstance(log_data, list):
            print("경고: 로그 파일 형식이 올바르지 않습니다.")
            return False
        
        print(f"총 {len(log_data)}개의 이동 기록을 찾았습니다.\n")
        
        # 역순으로 처리 (최신부터)
        log_data.reverse()
        
        # 파일 복구
        total = len(log_data)
        restored_count = 0
        
        for idx, log_entry in enumerate(log_data, 1):
            if idx % 10 == 0 or idx == total:
                progress = (idx / total) * 100
                print(f"처리 중: {idx}/{total} ({progress:.1f}%)", end='\r')
                sys.stdout.flush()
            
            try:
                moved_to = log_entry.get('moved_to')
                original = log_entry.get('original')
                
                if not moved_to or not original:
                    continue
                
                # 현재 파일 경로 (분류된 위치)
                current_path = self.target_dir / moved_to
                
                # 원래 경로
                original_path = self.target_dir / original
                
                # 파일이 존재하는지 확인
                if not current_path.exists():
                    # 파일이 이미 이동되었거나 삭제된 경우
                    continue
                
                # 원래 위치로 복구
                if not self.dry_run:
                    try:
                        # 원래 디렉토리 생성
                        original_path.parent.mkdir(parents=True, exist_ok=True)
                        
                        # 파일이 이미 원래 위치에 있는지 확인
                        if current_path == original_path:
                            self.stats['변경없음'] += 1
                            continue
                        
                        # 중복 파일 처리
                        final_path = original_path
                        if final_path.exists():
                            stem = final_path.stem
                            suffix = final_path.suffix
                            counter = 1
                            while final_path.exists():
                                new_name = f"{stem}_복구_{counter}{suffix}"
                                final_path = final_path.parent / new_name
                                counter += 1
                        
                        # 파일 이동
                        shutil.move(str(current_path), str(final_path))
                        self.stats['복구됨'] += 1
                        restored_count += 1
                        
                        if final_path != original_path:
                            print(f"✓ 복구: {moved_to} → {final_path.relative_to(self.target_dir)} (중복으로 이름 변경)")
                        else:
                            print(f"✓ 복구: {moved_to} → {original}")
                            
                    except Exception as e:
                        self.stats['오류'] += 1
                        print(f"✗ 오류: {moved_to} → {original} - {e}")
                else:
                    self.stats['시뮬레이션'] += 1
                    print(f"[시뮬레이션] 복구: {moved_to} → {original}")
                    restored_count += 1
            
            except Exception as e:
                self.stats['오류'] += 1
                print(f"✗ 로그 항목 처리 오류: {e}")
        
        print()  # 진행률 출력 후 줄바꿈
        
        if restored_count > 0:
            print(f"\n{restored_count}개의 파일이 원래 위치로 복구되었습니다.")
        
        # 빈 폴더 정리
        if not self.dry_run:
            self.cleanup_empty_folders()
        
        return True
    
    def restore_from_organized_structure(self):
        """분류된 폴더 구조에서 파일 복구 (로그가 없는 경우)"""
        print("분류된 파일들을 찾는 중...")
        organized_files = self.find_organized_files()
        
        if not organized_files:
            print("분류된 파일을 찾을 수 없습니다.")
            print("이미 복구되었거나 분류되지 않은 디렉토리일 수 있습니다.")
            return
        
        print(f"총 {len(organized_files)}개의 분류된 파일을 찾았습니다.\n")
        print("경고: 이동 로그가 없어 원래 위치를 알 수 없습니다.")
        print("파일들을 루트 디렉토리로 이동합니다.\n")
        
        # 파일 복구
        total = len(organized_files)
        for idx, (file_path, relative_path, parts) in enumerate(organized_files, 1):
            if idx % 10 == 0 or idx == total:
                progress = (idx / total) * 100
                print(f"처리 중: {idx}/{total} ({progress:.1f}%)", end='\r')
                sys.stdout.flush()
            
            # 파일명만 추출
            file_name = parts[-1]
            
            # 복구할 경로 결정
            restore_path = self.restore_dir / file_name
            
            # 중복 파일 처리
            if restore_path.exists() and restore_path != file_path:
                stem = restore_path.stem
                suffix = restore_path.suffix
                counter = 1
                while restore_path.exists():
                    new_name = f"{stem}_복구_{counter}{suffix}"
                    restore_path = self.restore_dir / new_name
                    counter += 1
            
            if not self.dry_run:
                try:
                    # 디렉토리 생성
                    restore_path.parent.mkdir(parents=True, exist_ok=True)
                    
                    # 파일 이동
                    if file_path != restore_path:
                        shutil.move(str(file_path), str(restore_path))
                        self.stats['복구됨'] += 1
                        print(f"✓ 복구: {relative_path} → {restore_path.name}")
                    else:
                        self.stats['변경없음'] += 1
                        
                except Exception as e:
                    self.stats['오류'] += 1
                    print(f"✗ 오류: {relative_path} - {e}")
            else:
                self.stats['시뮬레이션'] += 1
                print(f"[시뮬레이션] 복구: {relative_path} → {restore_path.name}")
        
        print()  # 진행률 출력 후 줄바꿈
        
        # 빈 폴더 정리
        if not self.dry_run:
            self.cleanup_empty_folders()
    
    def cleanup_empty_folders(self):
        """빈 폴더 정리"""
        print("\n빈 폴더 정리 중...")
        
        # 하위 디렉토리부터 역순으로 정렬 (깊은 폴더부터)
        all_dirs = sorted(
            [d for d in self.target_dir.rglob('*') if d.is_dir()],
            key=lambda x: len(x.parts),
            reverse=True
        )
        
        for dir_path in all_dirs:
            # 루트 디렉토리는 제외
            if dir_path == self.target_dir:
                continue
            
            try:
                # 디렉토리가 비어있는지 확인
                if not any(dir_path.iterdir()):
                    dir_path.rmdir()
                    self.stats['빈폴더삭제'] += 1
                    print(f"✓ 빈 폴더 삭제: {dir_path.relative_to(self.target_dir)}")
            except OSError:
                # 삭제할 수 없는 경우 (권한 문제 등)
                pass
    
    def restore(self, use_git_checkout=True):
        """파일 복구 실행"""
        is_git = self.is_git_repo()
        
        # Git 저장소이고 커밋 해시가 제공된 경우
        if is_git and self.commit_hash:
            print(f"\n{'='*60}")
            print(f"파일 복구 시작 (Git 모드)")
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
        
        # Git 저장소이지만 커밋 해시가 없는 경우 - 자동 탐지 시도
        elif is_git and not self.commit_hash:
            print("파일 분류 전 커밋을 찾는 중...")
            self.commit_hash = self.find_pre_organize_commit()
            
            if self.commit_hash:
                print(f"\n{'='*60}")
                print(f"파일 복구 시작 (Git 모드)")
                print(f"대상 디렉토리: {self.target_dir}")
                print(f"복구 커밋: {self.commit_hash}")
                print(f"시뮬레이션 모드: {'예' if self.dry_run else '아니오'}")
                print(f"{'='*60}\n")
                
                if use_git_checkout:
                    self.restore_using_git_checkout(self.commit_hash)
                else:
                    self.restore_directory_structure(self.commit_hash)
            else:
                # Git 커밋을 찾지 못한 경우 폴더 구조 기반 복구 시도
                print("Git 커밋을 찾을 수 없습니다. 폴더 구조 기반 복구를 시도합니다.\n")
                self.restore_from_organized_structure()
        
        # Git 저장소가 아닌 경우 - 로그 파일 또는 폴더 구조 기반 복구
        else:
            print(f"\n{'='*60}")
            print(f"파일 복구 시작")
            print(f"대상 디렉토리: {self.target_dir}")
            print(f"복구 위치: {self.restore_dir}")
            print(f"시뮬레이션 모드: {'예' if self.dry_run else '아니오'}")
            print(f"{'='*60}\n")
            
            # 먼저 로그 파일로 복구 시도
            if not self.restore_from_log():
                # 로그가 없으면 폴더 구조 기반 복구
                print("\n로그 파일 기반 복구 실패. 폴더 구조 기반 복구를 시도합니다.\n")
                self.restore_from_organized_structure()
        
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
  python3 file_restore.py . --dry-run
  
  # 특정 디렉토리 복구 (Git 저장소가 아니어도 가능)
  python3 file_restore.py ~/Downloads
  
  # 특정 커밋으로 복구 (Git 저장소인 경우)
  python3 file_restore.py . --commit 9b36c09
  
  # 파일을 특정 디렉토리로 복구
  python3 file_restore.py . --restore-dir ~/RestoredFiles
  
  # Git checkout 대신 파일별 복구
  python3 file_restore.py . --no-git-checkout
        """
    )
    
    parser.add_argument('target_dir', nargs='?', default='.',
                       help='복구할 디렉토리 경로 (기본값: 현재 디렉토리)')
    parser.add_argument('-c', '--commit',
                       help='복구할 커밋 해시 (Git 저장소인 경우, 기본값: 파일 분류 전 커밋 자동 탐지)')
    parser.add_argument('-r', '--restore-dir',
                       help='파일을 복구할 디렉토리 (기본값: target_dir의 루트)')
    parser.add_argument('--no-git-checkout', action='store_true',
                       help='Git checkout 대신 파일별로 복구')
    parser.add_argument('--dry-run', action='store_true',
                       help='실제 복구 없이 시뮬레이션만 실행')
    
    args = parser.parse_args()
    
    try:
        restorer = FileRestorer(
            target_dir=args.target_dir,
            commit_hash=args.commit,
            restore_dir=args.restore_dir,
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
