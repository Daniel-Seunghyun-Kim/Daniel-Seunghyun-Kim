"""
반도체 소자 열전도 시뮬레이션
내부에서 열이 생성되고 외부로 방출되는 경우

방정식: ∂T/∂t = α * ∇²T + S
여기서 S는 내부 열 생성률 (K/s)
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib import cm
from font_setup import setup_korean_font

# 한글 폰트 설정
setup_korean_font()


class SemiconductorHeatConduction1D:
    """
    1D 반도체 소자 열전도
    내부 열원이 있고 경계에서 냉각됨
    """
    def __init__(self, L=1.0, T0=25.0, T_cooling=25.0, alpha=0.01, 
                 heat_source_func=None, heat_source_center=None, heat_source_width=None,
                 heat_source_power=100.0, nx=100, nt=2000, dt=0.0001):
        """
        Parameters:
        L: 소자 길이 (m)
        T0: 초기 온도 (℃)
        T_cooling: 냉각 경계 온도 (℃)
        alpha: 열확산계수 (m²/s)
        heat_source_func: 열원 함수 (x) -> 열 생성률 (K/s), None이면 기본 가우시안 사용
        heat_source_center: 열원 중심 위치 (m)
        heat_source_width: 열원 폭 (m)
        heat_source_power: 최대 열 생성률 (K/s)
        nx: 공간 격자 수
        nt: 시간 스텝 수
        dt: 시간 간격 (s)
        """
        self.L = L
        self.T0 = T0
        self.T_cooling = T_cooling
        self.alpha = alpha
        self.nx = nx
        self.nt = nt
        self.dt = dt
        
        # 공간 격자
        self.x = np.linspace(0, L, nx)
        self.dx = L / (nx - 1)
        
        # 열원 설정
        if heat_source_center is None:
            heat_source_center = L / 2
        if heat_source_width is None:
            heat_source_width = L / 10
        
        if heat_source_func is None:
            # 기본 가우시안 열원
            def default_heat_source(x):
                return heat_source_power * np.exp(-((x - heat_source_center) / heat_source_width)**2)
            self.heat_source = np.array([default_heat_source(xi) for xi in self.x])
        else:
            self.heat_source = np.array([heat_source_func(xi) for xi in self.x])
        
        # 안정성 조건 확인
        r = alpha * dt / (self.dx**2)
        if r > 0.5:
            print(f"경고: 안정성 조건 위반 (r = {r:.3f} > 0.5)")
            print(f"dt를 {0.5 * self.dx**2 / alpha:.6f} 이하로 줄이세요.")
        
        # 초기 조건
        self.T_initial = np.full(nx, T0)
    
    def numerical_solution_ftcs(self):
        """
        수치해법: FTCS 방법 (내부 열원 포함)
        """
        T = self.T_initial.copy()
        T_history = [T.copy()]
        
        r = self.alpha * self.dt / (self.dx**2)
        
        for _ in range(self.nt):
            T_new = T.copy()
            
            # 내부 점들 업데이트 (열전도 + 열원)
            for i in range(1, self.nx - 1):
                # 열전도 항
                conduction = r * (T[i+1] - 2*T[i] + T[i-1])
                # 열원 항
                source = self.dt * self.heat_source[i]
                T_new[i] = T[i] + conduction + source
            
            # 경계 조건: 냉각 (고정 온도)
            T_new[0] = self.T_cooling
            T_new[-1] = self.T_cooling
            
            T = T_new
            T_history.append(T.copy())
        
        return np.array(T_history)
    
    def animate_temperature(self, save_gif=False):
        """
        온도 프로파일 애니메이션 생성
        """
        T_history = self.numerical_solution_ftcs()
        
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10))
        
        # 온도 프로파일
        line, = ax1.plot(self.x, T_history[0], 'r-', linewidth=2, label='Temperature')
        ax1.set_xlim(0, self.L)
        ax1.set_ylim(self.T_cooling - 5, max(T_history.max(), self.T_cooling + 50))
        ax1.set_xlabel('Position x (m)', fontsize=12)
        ax1.set_ylabel('Temperature T (℃)', fontsize=12)
        ax1.set_title('1D Semiconductor Heat Conduction - Internal Heat Source', fontsize=14, fontweight='bold')
        ax1.grid(True, alpha=0.3)
        ax1.legend()
        
        time_text1 = ax1.text(0.02, 0.95, '', transform=ax1.transAxes, fontsize=12,
                             verticalalignment='top', bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
        
        # 열원 분포
        heat_line, = ax2.plot(self.x, self.heat_source, 'b-', linewidth=2, label='Heat Source')
        ax2.set_xlim(0, self.L)
        ax2.set_xlabel('Position x (m)', fontsize=12)
        ax2.set_ylabel('Heat Generation Rate (K/s)', fontsize=12)
        ax2.set_title('Internal Heat Source Distribution', fontsize=12)
        ax2.grid(True, alpha=0.3)
        ax2.legend()
        
        def animate(frame):
            line.set_ydata(T_history[frame])
            time_text1.set_text(f'Time t = {frame * self.dt:.4f} s\nMax Temp = {T_history[frame].max():.2f} ℃')
            return line, time_text1
        
        anim = FuncAnimation(fig, animate, frames=len(T_history), interval=50, blit=True, repeat=True)
        
        if save_gif:
            anim.save('heat_conduction_semiconductor_1d.gif', writer='pillow', fps=20)
            print("애니메이션이 'heat_conduction_semiconductor_1d.gif'로 저장되었습니다.")
        
        plt.tight_layout()
        plt.show()
        
        return anim


class SemiconductorHeatConduction2D:
    """
    2D 반도체 소자 열전도
    내부 열원이 있고 경계에서 냉각됨
    """
    def __init__(self, Lx=1.0, Ly=1.0, T0=25.0, T_cooling=25.0, alpha=0.01,
                 heat_source_func=None, heat_source_center=None, heat_source_radius=None,
                 heat_source_power=100.0, nx=50, ny=50, nt=2000, dt=0.0001):
        """
        Parameters:
        Lx, Ly: 소자 크기 (m)
        T0: 초기 온도 (℃)
        T_cooling: 냉각 경계 온도 (℃)
        alpha: 열확산계수 (m²/s)
        heat_source_func: 열원 함수 (x, y) -> 열 생성률 (K/s), None이면 기본 가우시안 사용
        heat_source_center: 열원 중심 위치 (x, y) (m)
        heat_source_radius: 열원 반경 (m)
        heat_source_power: 최대 열 생성률 (K/s)
        nx, ny: 공간 격자 수
        nt: 시간 스텝 수
        dt: 시간 간격 (s)
        """
        self.Lx = Lx
        self.Ly = Ly
        self.T0 = T0
        self.T_cooling = T_cooling
        self.alpha = alpha
        self.nx = nx
        self.ny = ny
        self.nt = nt
        self.dt = dt
        
        # 공간 격자
        self.x = np.linspace(0, Lx, nx)
        self.y = np.linspace(0, Ly, ny)
        self.X, self.Y = np.meshgrid(self.x, self.y)
        self.dx = Lx / (nx - 1)
        self.dy = Ly / (ny - 1)
        
        # 열원 설정
        if heat_source_center is None:
            heat_source_center = (Lx / 2, Ly / 2)
        if heat_source_radius is None:
            heat_source_radius = min(Lx, Ly) / 10
        
        if heat_source_func is None:
            # 기본 가우시안 열원
            def default_heat_source(x, y):
                dist_sq = (x - heat_source_center[0])**2 + (y - heat_source_center[1])**2
                return heat_source_power * np.exp(-dist_sq / (2 * heat_source_radius**2))
            self.heat_source = np.array([[default_heat_source(self.X[i, j], self.Y[i, j]) 
                                        for j in range(nx)] for i in range(ny)])
        else:
            self.heat_source = np.array([[heat_source_func(self.X[i, j], self.Y[i, j]) 
                                        for j in range(nx)] for i in range(ny)])
        
        # 안정성 조건 확인
        rx = alpha * dt / (self.dx**2)
        ry = alpha * dt / (self.dy**2)
        if rx > 0.25 or ry > 0.25:
            print(f"경고: 안정성 조건 위반 (rx = {rx:.3f}, ry = {ry:.3f})")
            print(f"dt를 {0.25 * min(self.dx**2, self.dy**2) / alpha:.6f} 이하로 줄이세요.")
        
        # 초기 조건
        self.T = np.full((ny, nx), T0)
    
    def numerical_solution_ftcs(self):
        """
        수치해법: FTCS 방법 (내부 열원 포함)
        """
        T = self.T.copy()
        T_history = [T.copy()]
        
        rx = self.alpha * self.dt / (self.dx**2)
        ry = self.alpha * self.dt / (self.dy**2)
        
        for _ in range(self.nt):
            T_new = T.copy()
            
            # 내부 점들 업데이트 (열전도 + 열원)
            for i in range(1, self.ny - 1):
                for j in range(1, self.nx - 1):
                    # 열전도 항
                    conduction = rx * (T[i, j+1] - 2*T[i, j] + T[i, j-1]) + \
                                ry * (T[i+1, j] - 2*T[i, j] + T[i-1, j])
                    # 열원 항
                    source = self.dt * self.heat_source[i, j]
                    T_new[i, j] = T[i, j] + conduction + source
            
            # 경계 조건: 냉각 (고정 온도)
            T_new[0, :] = self.T_cooling
            T_new[-1, :] = self.T_cooling
            T_new[:, 0] = self.T_cooling
            T_new[:, -1] = self.T_cooling
            
            T = T_new
            T_history.append(T.copy())
        
        return np.array(T_history)
    
    def animate_temperature(self, save_gif=False):
        """
        2D 온도 프로파일 애니메이션 생성
        """
        T_history = self.numerical_solution_ftcs()
        
        fig, ax = plt.subplots(figsize=(10, 8))
        
        # 초기 컬러맵 (저온=청색, 고온=적색)
        vmin = self.T_cooling
        vmax = max(T_history.max(), self.T_cooling + 50)
        im = ax.imshow(T_history[0], extent=[0, self.Lx, 0, self.Ly], 
                      origin='lower', cmap='coolwarm', interpolation='bilinear',
                      vmin=vmin, vmax=vmax)
        
        ax.set_xlabel('x (m)', fontsize=12)
        ax.set_ylabel('y (m)', fontsize=12)
        ax.set_title('2D Semiconductor Heat Conduction - Internal Heat Source', fontsize=14, fontweight='bold')
        
        cbar = plt.colorbar(im, ax=ax)
        cbar.set_label('Temperature T (℃)', fontsize=12)
        
        time_text = ax.text(0.02, 0.95, '', transform=ax.transAxes, fontsize=12,
                          verticalalignment='top', bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
        
        def animate(frame):
            im.set_array(T_history[frame])
            time_text.set_text(f'Time t = {frame * self.dt:.4f} s\nMax Temp = {T_history[frame].max():.2f} ℃')
            return [im, time_text]
        
        anim = FuncAnimation(fig, animate, frames=len(T_history), interval=50, blit=True, repeat=True)
        
        if save_gif:
            anim.save('heat_conduction_semiconductor_2d.gif', writer='pillow', fps=20)
            print("애니메이션이 'heat_conduction_semiconductor_2d.gif'로 저장되었습니다.")
        
        plt.tight_layout()
        plt.show()
        
        return anim
    
    def animate_3d_surface(self, save_gif=False):
        """
        3D 표면 플롯 애니메이션 생성
        """
        T_history = self.numerical_solution_ftcs()
        
        fig = plt.figure(figsize=(12, 8))
        ax = fig.add_subplot(111, projection='3d')
        
        vmin = self.T_cooling
        vmax = max(T_history.max(), self.T_cooling + 50)
        
        # 초기 표면 (저온=청색, 고온=적색)
        surf = ax.plot_surface(self.X, self.Y, T_history[0], cmap='coolwarm', 
                              linewidth=0, antialiased=True, vmin=vmin, vmax=vmax)
        
        ax.set_xlabel('x (m)', fontsize=12)
        ax.set_ylabel('y (m)', fontsize=12)
        ax.set_zlabel('Temperature T (℃)', fontsize=12)
        ax.set_title('2D Semiconductor Heat Conduction - 3D Surface', fontsize=14, fontweight='bold')
        ax.set_zlim(vmin, vmax)
        
        fig.colorbar(surf, ax=ax, shrink=0.5, aspect=5)
        
        time_text = ax.text2D(0.02, 0.95, '', transform=ax.transAxes, fontsize=12,
                             bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
        
        def animate(frame):
            ax.clear()
            surf = ax.plot_surface(self.X, self.Y, T_history[frame], cmap='coolwarm',
                                  linewidth=0, antialiased=True, vmin=vmin, vmax=vmax)
            ax.set_xlabel('x (m)', fontsize=12)
            ax.set_ylabel('y (m)', fontsize=12)
            ax.set_zlabel('Temperature T (℃)', fontsize=12)
            ax.set_title('2D Semiconductor Heat Conduction - 3D Surface', fontsize=14, fontweight='bold')
            ax.set_zlim(vmin, vmax)
            time_text = ax.text2D(0.02, 0.95, f'Time t = {frame * self.dt:.4f} s\nMax Temp = {T_history[frame].max():.2f} ℃', 
                                 transform=ax.transAxes, fontsize=12,
                                 bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
            return [surf]
        
        anim = FuncAnimation(fig, animate, frames=len(T_history), interval=50, blit=False, repeat=True)
        
        if save_gif:
            anim.save('heat_conduction_semiconductor_2d_3d.gif', writer='pillow', fps=20)
            print("애니메이션이 'heat_conduction_semiconductor_2d_3d.gif'로 저장되었습니다.")
        
        plt.tight_layout()
        plt.show()
        
        return anim


if __name__ == "__main__":
    # 예제 실행
    dx_1d = 0.01
    dt_1d = 0.4 * dx_1d**2 / 0.01
    
    print("=" * 60)
    print("반도체 소자 열전도 시뮬레이션")
    print("=" * 60)
    
    # 1D 반도체 소자
    print("\n[1D 반도체 소자 - 내부 열원]")
    print("-" * 60)
    heat_1d = SemiconductorHeatConduction1D(
        L=1.0, T0=25.0, T_cooling=25.0,
        alpha=0.01, heat_source_center=0.5, heat_source_width=0.1,
        heat_source_power=500.0, nx=100, nt=2000, dt=dt_1d
    )
    print("애니메이션 생성 중...")
    heat_1d.animate_temperature(save_gif=True)
    
    # 2D 반도체 소자
    print("\n[2D 반도체 소자 - 내부 열원]")
    print("-" * 60)
    dx_2d = 0.02
    dy_2d = 0.02
    dt_2d = 0.2 * min(dx_2d**2, dy_2d**2) / 0.01
    
    heat_2d = SemiconductorHeatConduction2D(
        Lx=1.0, Ly=1.0, T0=25.0, T_cooling=25.0,
        alpha=0.01, heat_source_center=(0.5, 0.5), heat_source_radius=0.1,
        heat_source_power=500.0, nx=50, ny=50, nt=2000, dt=dt_2d
    )
    print("컬러맵 애니메이션 생성 중...")
    heat_2d.animate_temperature(save_gif=True)
    
    print("\n3D 표면 애니메이션 생성 중...")
    heat_2d.animate_3d_surface(save_gif=True)
