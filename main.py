"""
열전도 방정식 메인 실행 스크립트
1D 및 2D 열전도 방정식의 해석해와 수치해법을 실행하고 애니메이션을 생성합니다.
"""

import numpy as np
import matplotlib.pyplot as plt
from font_setup import setup_korean_font
from heat_conduction_1d import HeatConduction1D
from heat_conduction_2d import HeatConduction2D
from heat_conduction_semiconductor import SemiconductorHeatConduction1D, SemiconductorHeatConduction2D

# 한글 폰트 설정
setup_korean_font()


def main():
    print("=" * 60)
    print("열전도 방정식 시뮬레이션")
    print("=" * 60)
    
    # 1D 열전도 - 해석해
    print("\n[1D 열전도 - 해석해]")
    print("-" * 60)
    dx_1d = 0.01
    dt_1d = 0.4 * dx_1d**2 / 0.01  # 안정성 조건: r <= 0.5
    
    heat_1d_analytical = HeatConduction1D(
        L=1.0, T0=0.0, T_left=100.0, T_right=0.0,
        alpha=0.01, nx=100, nt=2000, dt=dt_1d
    )
    print(f"격자 크기: dx = {dx_1d:.4f} m")
    print(f"시간 간격: dt = {dt_1d:.6f} s")
    print(f"안정성 파라미터: r = {0.01 * dt_1d / (dx_1d**2):.4f}")
    print("애니메이션 생성 중...")
    heat_1d_analytical.animate_temperature(method='analytical', save_gif=True)
    
    # 1D 열전도 - 수치해법
    print("\n[1D 열전도 - 수치해법 (FTCS)]")
    print("-" * 60)
    heat_1d_numerical = HeatConduction1D(
        L=1.0, T0=0.0, T_left=100.0, T_right=0.0,
        alpha=0.01, nx=100, nt=2000, dt=dt_1d
    )
    print("애니메이션 생성 중...")
    heat_1d_numerical.animate_temperature(method='numerical', save_gif=True)
    
    # 2D 열전도 - 수치해법
    print("\n[2D 열전도 - 수치해법 (FTCS)]")
    print("-" * 60)
    dx_2d = 0.02
    dy_2d = 0.02
    dt_2d = 0.2 * min(dx_2d**2, dy_2d**2) / 0.01  # 안정성 조건
    
    heat_2d = HeatConduction2D(
        Lx=1.0, Ly=1.0, T0=0.0, T_boundary=100.0,
        alpha=0.01, nx=50, ny=50, nt=2000, dt=dt_2d
    )
    print(f"격자 크기: dx = {dx_2d:.4f} m, dy = {dy_2d:.4f} m")
    print(f"시간 간격: dt = {dt_2d:.6f} s")
    print(f"안정성 파라미터: rx = {0.01 * dt_2d / (dx_2d**2):.4f}, ry = {0.01 * dt_2d / (dy_2d**2):.4f}")
    print("컬러맵 애니메이션 생성 중...")
    heat_2d.animate_temperature(save_gif=True)
    
    # 반도체 소자 열전도 시뮬레이션 (내부 열원)
    print("\n[반도체 소자 열전도 - 내부 열원]")
    print("-" * 60)
    print("내부에서 열이 생성되고 경계에서 냉각되는 경우")
    
    # 1D 반도체 소자
    print("\n[1D 반도체 소자]")
    heat_semi_1d = SemiconductorHeatConduction1D(
        L=1.0, T0=25.0, T_cooling=25.0,
        alpha=0.01, heat_source_center=0.5, heat_source_width=0.1,
        heat_source_power=500.0, nx=100, nt=2000, dt=dt_1d
    )
    print("애니메이션 생성 중...")
    heat_semi_1d.animate_temperature(save_gif=True)
    
    # 2D 반도체 소자
    print("\n[2D 반도체 소자]")
    heat_semi_2d = SemiconductorHeatConduction2D(
        Lx=1.0, Ly=1.0, T0=25.0, T_cooling=25.0,
        alpha=0.01, heat_source_center=(0.5, 0.5), heat_source_radius=0.1,
        heat_source_power=500.0, nx=50, ny=50, nt=2000, dt=dt_2d
    )
    print("컬러맵 애니메이션 생성 중...")
    heat_semi_2d.animate_temperature(save_gif=True)
    
    print("\n" + "=" * 60)
    print("모든 애니메이션 생성 완료!")
    print("=" * 60)


if __name__ == "__main__":
    main()
