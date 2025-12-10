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
from collections import defaultdict, Counter
import argparse
import sys
import json
import re
import hashlib
from difflib import SequenceMatcher


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
                 organize_by_type=False, preserve_structure=True, 
                 content_based=True, similarity_threshold=0.3, dry_run=False, log_file=None):
        """
        Args:
            source_dir: 정리할 소스 디렉토리
            target_dir: 정리된 파일을 저장할 타겟 디렉토리 (None이면 source_dir 내에 정리)
            organize_by_date: 날짜별로 정리할지 여부
            organize_by_type: 파일 유형별로 정리할지 여부 (기본값: False, 연관 파일 보존을 위해)
            preserve_structure: 원본 폴더 구조를 보존할지 여부 (기본값: True)
            content_based: 파일 내용 기반 분류 사용 여부 (기본값: True)
            similarity_threshold: 파일 유사도 임계값 (0.0-1.0, 기본값: 0.3)
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
        self.content_based = content_based
        self.similarity_threshold = similarity_threshold
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
    
    def extract_keywords_from_text(self, text, max_keywords=30):
        """텍스트에서 키워드 추출"""
        if not text:
            return []
        
        # 한글, 영문, 숫자만 추출
        words = re.findall(r'[가-힣a-zA-Z0-9]+', text.lower())
        
        # 불용어 제거 (너무 짧은 단어, 일반적인 단어)
        stopwords = {'the', 'is', 'at', 'of', 'on', 'and', 'a', 'an', 'as', 'are', 
                    'was', 'were', 'been', 'be', 'have', 'has', 'had', 'do', 'does',
                    'did', 'will', 'would', 'could', 'should', 'may', 'might', 'must',
                    'can', 'this', 'that', 'these', 'those', 'i', 'you', 'he', 'she',
                    'it', 'we', 'they', 'what', 'which', 'who', 'when', 'where', 'why',
                    'how', 'all', 'each', 'every', 'both', 'few', 'more', 'most', 'other',
                    'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so',
                    'than', 'too', 'very', 'just', 'now', 'file', 'files', 'data', 'date',
                    'time', 'name', 'type', 'size', 'path', 'dir', 'folder', 'directory'}
        
        # 한글 불용어
        korean_stopwords = {'그', '것', '수', '있', '없', '하', '되', '되다', '이', '가',
                           '을', '를', '에', '의', '로', '으로', '와', '과', '도', '만',
                           '은', '는', '에서', '까지', '부터', '한', '두', '세', '네',
                           '다', '들', '등', '및', '또', '또한', '또는', '또한', '또는'}
        
        # 단어 길이 필터링 및 불용어 제거
        # 한글은 2자 이상, 영문은 3자 이상
        filtered_words = []
        for w in words:
            if len(w) >= 2:
                # 한글 단어는 2자 이상
                if any(ord(c) >= 0xAC00 and ord(c) <= 0xD7A3 for c in w):
                    if len(w) >= 2 and w not in korean_stopwords:
                        filtered_words.append(w)
                # 영문 단어는 3자 이상
                elif w.isalpha() and len(w) >= 3 and w not in stopwords:
                    filtered_words.append(w)
                # 숫자 포함 단어는 허용
                elif any(c.isdigit() for c in w) and len(w) >= 2:
                    filtered_words.append(w)
        
        # 빈도 계산
        word_freq = Counter(filtered_words)
        
        # 상위 키워드 반환 (최소 2회 이상 등장한 단어 우선)
        keywords = []
        for word, count in word_freq.most_common(max_keywords * 2):
            if count >= 2 or len(keywords) < max_keywords:
                keywords.append(word)
            if len(keywords) >= max_keywords:
                break
        
        return keywords
    
    def extract_file_content_features(self, file_path):
        """파일에서 내용 특징 추출 (키워드, 메타데이터 등)"""
        features = {
            'keywords': [],
            'filename_words': [],
            'path_words': [],
            'size': 0,
            'extension': file_path.suffix.lower()
        }
        
        try:
            # 파일명에서 키워드 추출
            stem = file_path.stem.lower()
            filename_words = re.findall(r'[가-힣a-zA-Z0-9]+', stem)
            features['filename_words'] = filename_words
            
            # 경로에서 키워드 추출
            path_parts = [p.lower() for p in file_path.parts[:-1]]
            path_text = ' '.join(path_parts)
            path_words = re.findall(r'[가-힣a-zA-Z0-9]+', path_text)
            features['path_words'] = path_words
            
            # 파일 크기
            features['size'] = file_path.stat().st_size
            
            # 텍스트 파일 내용 읽기 (더 많은 형식 지원)
            text_extensions = ['.txt', '.md', '.log', '.csv', '.json', '.xml', 
                            '.py', '.js', '.html', '.css', '.java', '.cpp', '.c',
                            '.sh', '.bat', '.ps1', '.yml', '.yaml', '.rtf',
                            '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx']
            
            if file_path.suffix.lower() in text_extensions:
                try:
                    # 작은 파일만 읽기 (2MB 이하로 확대)
                    if features['size'] <= 2 * 1024 * 1024:
                        # 여러 인코딩 시도
                        encodings = ['utf-8', 'cp949', 'euc-kr', 'latin-1']
                        content = None
                        for encoding in encodings:
                            try:
                                with open(file_path, 'r', encoding=encoding, errors='ignore') as f:
                                    content = f.read(100000)  # 최대 100KB로 확대
                                break
                            except:
                                continue
                        
                        if content:
                            features['keywords'] = self.extract_keywords_from_text(content)
                except:
                    pass
        
        except Exception as e:
            pass
        
        return features
    
    def calculate_similarity(self, features1, features2):
        """두 파일의 특징 간 유사도 계산 (0.0-1.0)
        가중치: 내용 70%, 파일명 30%
        """
        similarity_scores = []
        weights = []
        
        # 파일명 키워드 유사도 (30%)
        if features1['filename_words'] and features2['filename_words']:
            common_filename = set(features1['filename_words']) & set(features2['filename_words'])
            total_filename = set(features1['filename_words']) | set(features2['filename_words'])
            if total_filename:
                filename_sim = len(common_filename) / len(total_filename)
                similarity_scores.append(filename_sim)
                weights.append(0.3)
        
        # 내용 키워드 유사도 (70%)
        if features1['keywords'] and features2['keywords']:
            common_keywords = set(features1['keywords']) & set(features2['keywords'])
            total_keywords = set(features1['keywords']) | set(features2['keywords'])
            if total_keywords:
                keyword_sim = len(common_keywords) / len(total_keywords)
                similarity_scores.append(keyword_sim)
                weights.append(0.7)
        
        # 가중 평균 계산
        if similarity_scores and weights:
            # 가중치 정규화
            total_weight = sum(weights)
            if total_weight > 0:
                weighted_sum = sum(score * weight for score, weight in zip(similarity_scores, weights))
                total_similarity = weighted_sum / total_weight
            else:
                total_similarity = 0.0
        else:
            # 키워드가 없는 경우 파일명만으로 비교
            if features1['filename_words'] and features2['filename_words']:
                common = set(features1['filename_words']) & set(features2['filename_words'])
                total = set(features1['filename_words']) | set(features2['filename_words'])
                total_similarity = len(common) / len(total) if total else 0.0
            else:
                total_similarity = 0.0
        
        return total_similarity
    
    def cluster_files_by_content(self, files):
        """파일 내용 기반으로 클러스터링"""
        if not files:
            return {}
        
        print("파일 내용 분석 중...")
        sys.stdout.flush()
        
        # 모든 파일의 특징 추출
        file_features = {}
        for idx, file_path in enumerate(files):
            if idx % 50 == 0:
                print(f"  분석 중... {idx}/{len(files)}", end='\r')
                sys.stdout.flush()
            file_features[file_path] = self.extract_file_content_features(file_path)
        
        print(f"\n파일 간 유사도 계산 중...")
        sys.stdout.flush()
        
        # 클러스터링 (간단한 그룹화 알고리즘)
        clusters = {}
        cluster_id = 0
        
        for idx, file1 in enumerate(files):
            if idx % 20 == 0:
                print(f"  클러스터링 중... {idx}/{len(files)}", end='\r')
                sys.stdout.flush()
            
            assigned = False
            features1 = file_features[file1]
            
            # 기존 클러스터와 유사도 확인
            for cluster_name, cluster_files in clusters.items():
                if not cluster_files:
                    continue
                
                # 클러스터의 대표 파일과 비교
                representative = cluster_files[0]
                features2 = file_features[representative]
                similarity = self.calculate_similarity(features1, features2)
                
                if similarity >= self.similarity_threshold:
                    clusters[cluster_name].append(file1)
                    assigned = True
                    break
            
            # 기존 클러스터에 할당되지 않으면 새 클러스터 생성
            if not assigned:
                # 클러스터 이름 생성 (내용 키워드 우선, 없으면 파일명 키워드)
                keywords = []
                
                # 내용 키워드 우선 사용
                if features1['keywords']:
                    keywords = features1['keywords'][:3]  # 상위 3개 키워드
                
                # 내용 키워드가 없으면 파일명 키워드 사용
                if not keywords and features1['filename_words']:
                    keywords = features1['filename_words'][:3]
                
                # 둘 다 없으면 경로 키워드 사용
                if not keywords and features1['path_words']:
                    keywords = features1['path_words'][:3]
                
                # 모두 없으면 기본값
                if not keywords:
                    keywords = ['기타']
                
                # 클러스터 이름 생성 (최대 2개 키워드 조합)
                cluster_name = '_'.join(keywords[:2]) if len(keywords) >= 2 else keywords[0]
                cluster_name = cluster_name[:30]  # 이름 길이 제한
                
                # 특수문자 제거 및 정리
                cluster_name = re.sub(r'[^\w가-힣_-]', '_', cluster_name)
                cluster_name = cluster_name.strip('_')
                
                # 중복 방지
                base_name = cluster_name
                counter = 1
                while cluster_name in clusters:
                    cluster_name = f"{base_name}_{counter}"
                    counter += 1
                
                clusters[cluster_name] = [file1]
        
        print()  # 줄바꿈
        
        return clusters
    
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
    
    def generate_target_path(self, file_path, cluster_name=None, all_files=None):
        """파일의 목적지 경로를 생성 (내용 기반 클러스터링 또는 연관 파일 보존)"""
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
        
        # 내용 기반 클러스터링 모드 (우선순위 최상위)
        if self.content_based and cluster_name:
            target_parts.append(cluster_name)
        # 연관 파일 보존 모드
        elif self.preserve_structure:
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
    
    def organize_file(self, file_path, cluster_name=None, all_files=None):
        """단일 파일을 정리"""
        if file_path.is_dir():
            return
        
        target_path = self.generate_target_path(file_path, cluster_name, all_files)
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
        print(f"내용 기반 분류: {'예' if self.content_based else '아니오'}")
        if self.content_based:
            print(f"유사도 임계값: {self.similarity_threshold}")
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
        
        # 내용 기반 클러스터링
        file_to_cluster = {}
        if self.content_based:
            clusters = self.cluster_files_by_content(files)
            print(f"\n{len(clusters)}개의 클러스터를 생성했습니다.\n")
            
            # 파일별 클러스터 매핑 생성
            for cluster_name, cluster_files in clusters.items():
                for file_path in cluster_files:
                    file_to_cluster[file_path] = cluster_name
            
            # 클러스터 정보 출력
            print("생성된 클러스터 (폴더) 정보:")
            for cluster_name, cluster_files in list(clusters.items())[:15]:  # 상위 15개만 표시
                print(f"  📁 {cluster_name}/ ({len(cluster_files)}개 파일)")
                if not self.dry_run and len(cluster_files) <= 5:
                    # 작은 클러스터는 파일 목록도 표시
                    for f in cluster_files[:3]:
                        print(f"      - {f.name}")
                    if len(cluster_files) > 3:
                        print(f"      ... 외 {len(cluster_files) - 3}개")
            if len(clusters) > 15:
                print(f"  ... 외 {len(clusters) - 15}개 클러스터")
            print()
        
        # 파일 처리 (진행률 표시)
        total = len(files)
        for idx, file_path in enumerate(files, 1):
            # 10개마다 또는 마지막 파일일 때 진행률 출력
            if idx % 10 == 0 or idx == total:
                progress = (idx / total) * 100
                print(f"처리 중: {idx}/{total} ({progress:.1f}%)", end='\r')
                sys.stdout.flush()
            
            cluster_name = file_to_cluster.get(file_path)
            self.organize_file(file_path, cluster_name=cluster_name, all_files=files)
        
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
    parser.add_argument('--no-content', action='store_true',
                       help='파일 내용 기반 분류 비활성화 (기본값: 활성화)')
    parser.add_argument('--similarity', type=float, default=0.3,
                       help='파일 유사도 임계값 (0.0-1.0, 기본값: 0.3)')
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
            content_based=not args.no_content,
            similarity_threshold=args.similarity,
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
