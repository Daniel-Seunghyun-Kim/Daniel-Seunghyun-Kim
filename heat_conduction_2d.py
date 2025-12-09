"""
2D 열전도 방정식 해결
∂T/∂t = α * (∂²T/∂x² + ∂²T/∂y²)

수치해법(FTCS) 사용
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib import cm
from font_setup import setup_korean_font

# 한글 폰트 설정
setup_korean_font()


class HeatConduction2D:
    def __init__(self, Lx=1.0, Ly=1.0, T0=0.0, T_boundary=100.0, alpha=0.01, 
                 nx=50, ny=50, nt=2000, dt=0.0001):
        """
        Parameters:
        Lx, Ly: 영역 크기 (m)
        T0: 초기 온도 (℃)
        T_boundary: 경계 온도 (℃)
        alpha: 열확산계수 (m²/s)
        nx, ny: 공간 격자 수
        nt: 시간 스텝 수
        dt: 시간 간격 (s)
        """
        self.Lx = Lx
        self.Ly = Ly
        self.T0 = T0
        self.T_boundary = T_boundary
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
        
        # 안정성 조건 확인
        rx = alpha * dt / (self.dx**2)
        ry = alpha * dt / (self.dy**2)
        if rx > 0.25 or ry > 0.25:
            print(f"경고: 안정성 조건 위반 (rx = {rx:.3f}, ry = {ry:.3f})")
            print(f"dt를 {0.25 * min(self.dx**2, self.dy**2) / alpha:.6f} 이하로 줄이세요.")
        
        # 초기 조건
        self.T = np.full((ny, nx), T0)
        
        # 경계 조건 설정
        self.T[0, :] = T_boundary      # 상단
        self.T[-1, :] = T_boundary     # 하단
        self.T[:, 0] = T_boundary      # 왼쪽
        self.T[:, -1] = T_boundary     # 오른쪽
    
    def numerical_solution_ftcs(self):
        """
        수치해법: FTCS (Forward Time Central Space) 방법
        """
        T = self.T.copy()
        T_history = [T.copy()]
        
        rx = self.alpha * self.dt / (self.dx**2)
        ry = self.alpha * self.dt / (self.dy**2)
        
        for _ in range(self.nt):
            T_new = T.copy()
            
            # 내부 점들 업데이트 (2D 라플라시안)
            for i in range(1, self.ny - 1):
                for j in range(1, self.nx - 1):
                    T_new[i, j] = T[i, j] + rx * (T[i, j+1] - 2*T[i, j] + T[i, j-1]) + \
                                  ry * (T[i+1, j] - 2*T[i, j] + T[i-1, j])
            
            # 경계 조건 유지
            T_new[0, :] = self.T_boundary
            T_new[-1, :] = self.T_boundary
            T_new[:, 0] = self.T_boundary
            T_new[:, -1] = self.T_boundary
            
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
        im = ax.imshow(T_history[0], extent=[0, self.Lx, 0, self.Ly], 
                      origin='lower', cmap='coolwarm', interpolation='bilinear',
                      vmin=self.T0, vmax=self.T_boundary)
        
        ax.set_xlabel('x (m)', fontsize=12)
        ax.set_ylabel('y (m)', fontsize=12)
        ax.set_title('2D Heat Conduction - Numerical Method (FTCS)', fontsize=14, fontweight='bold')
        
        cbar = plt.colorbar(im, ax=ax)
        cbar.set_label('Temperature T (℃)', fontsize=12)
        
        time_text = ax.text(0.02, 0.95, '', transform=ax.transAxes, fontsize=12,
                          verticalalignment='top', bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
        
        def animate(frame):
            im.set_array(T_history[frame])
            time_text.set_text(f'Time t = {frame * self.dt:.4f} s')
            return [im, time_text]
        
        anim = FuncAnimation(fig, animate, frames=len(T_history), interval=50, blit=True, repeat=True)
        
        if save_gif:
            anim.save('heat_conduction_2d.gif', writer='pillow', fps=20)
            print("애니메이션이 'heat_conduction_2d.gif'로 저장되었습니다.")
        
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
        
        # 초기 표면 (저온=청색, 고온=적색)
        surf = ax.plot_surface(self.X, self.Y, T_history[0], cmap='coolwarm', 
                              linewidth=0, antialiased=True, vmin=self.T0, vmax=self.T_boundary)
        
        ax.set_xlabel('x (m)', fontsize=12)
        ax.set_ylabel('y (m)', fontsize=12)
        ax.set_zlabel('Temperature T (℃)', fontsize=12)
        ax.set_title('2D Heat Conduction - 3D Surface', fontsize=14, fontweight='bold')
        ax.set_zlim(self.T0, self.T_boundary)
        
        fig.colorbar(surf, ax=ax, shrink=0.5, aspect=5)
        
        time_text = ax.text2D(0.02, 0.95, '', transform=ax.transAxes, fontsize=12,
                             bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
        
        def animate(frame):
            ax.clear()
            surf = ax.plot_surface(self.X, self.Y, T_history[frame], cmap='coolwarm',
                                  linewidth=0, antialiased=True, vmin=self.T0, vmax=self.T_boundary)
            ax.set_xlabel('x (m)', fontsize=12)
            ax.set_ylabel('y (m)', fontsize=12)
            ax.set_zlabel('Temperature T (℃)', fontsize=12)
            ax.set_title('2D Heat Conduction - 3D Surface', fontsize=14, fontweight='bold')
            ax.set_zlim(self.T0, self.T_boundary)
            time_text = ax.text2D(0.02, 0.95, f'Time t = {frame * self.dt:.4f} s', 
                                 transform=ax.transAxes, fontsize=12,
                                 bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
            return [surf]
        
        anim = FuncAnimation(fig, animate, frames=len(T_history), interval=50, blit=False, repeat=True)
        
        if save_gif:
            anim.save('heat_conduction_2d_3d.gif', writer='pillow', fps=20)
            print("애니메이션이 'heat_conduction_2d_3d.gif'로 저장되었습니다.")
        
        plt.tight_layout()
        plt.show()
        
        return anim


if __name__ == "__main__":
    # 예제 실행
    dx = 0.02
    dy = 0.02
    dt = 0.25 * min(dx**2, dy**2) / 0.01  # 안정성 조건
    
    heat_2d = HeatConduction2D(
        Lx=1.0, Ly=1.0, T0=0.0, T_boundary=100.0,
        alpha=0.01, nx=50, ny=50, nt=2000, dt=dt
    )
    
    print("2D 열전도 - 컬러맵 애니메이션 생성 중...")
    heat_2d.animate_temperature(save_gif=True)
    
    print("2D 열전도 - 3D 표면 애니메이션 생성 중...")
    heat_2d.animate_3d_surface(save_gif=True)
