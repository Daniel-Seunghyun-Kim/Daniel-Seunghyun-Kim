"""
한글 폰트 설정 유틸리티
"""

import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import platform

def setup_korean_font():
    """
    한글 폰트를 설정합니다.
    시스템에 한글 폰트가 없으면 영어로 표시됩니다.
    """
    system = platform.system()
    
    # 기본 설정
    plt.rcParams['axes.unicode_minus'] = False
    
    # 시스템별 한글 폰트 목록
    if system == 'Linux':
        font_candidates = [
            'NanumGothic',
            'NanumBarunGothic', 
            'Noto Sans CJK KR',
            'Noto Sans KR',
            'DejaVu Sans'
        ]
    elif system == 'Darwin':  # macOS
        font_candidates = [
            'AppleGothic',
            'NanumGothic',
            'NanumBarunGothic',
            'Arial Unicode MS'
        ]
    elif system == 'Windows':
        font_candidates = [
            'Malgun Gothic',
            'NanumGothic',
            'NanumBarunGothic',
            'Gulim'
        ]
    else:
        font_candidates = ['DejaVu Sans']
    
    # 사용 가능한 폰트 찾기
    available_fonts = [f.name for f in fm.fontManager.ttflist]
    
    for font in font_candidates:
        if font in available_fonts:
            plt.rcParams['font.family'] = font
            print(f"한글 폰트 설정: {font}")
            return font
    
    # 한글 폰트를 찾지 못한 경우
    plt.rcParams['font.family'] = 'DejaVu Sans'
    print("한글 폰트를 찾을 수 없습니다. 영어로 표시됩니다.")
    print("한글 폰트 설치 방법:")
    if system == 'Linux':
        print("  sudo apt-get install fonts-nanum fonts-noto-cjk")
    return None

if __name__ == "__main__":
    setup_korean_font()
