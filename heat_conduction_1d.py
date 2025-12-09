"""
1D 열전도 방정식 해결
∂T/∂t = α * ∂²T/∂x²

해석해와 수치해법(FTCS)을 모두 구현
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from font_setup import setup_korean_font

# 한글 폰트 설정
setup_korean_font()


class HeatConduction1D:
    def __init__(self, L=1.0, T0=0.0, T_left=100.0, T_right=0.0, alpha=0.01, nx=100, nt=2000, dt=0.0001):
        """
        Parameters:
        L: 막대 길이 (m)
        T0: 초기 온도 (℃)
        T_left: 왼쪽 경계 온도 (℃)
        T_right: 오른쪽 경계 온도 (℃)
        alpha: 열확산계수 (m²/s)
        nx: 공간 격자 수
        nt: 시간 스텝 수
        dt: 시간 간격 (s)
        """
        self.L = L
        self.T0 = T0
        self.T_left = T_left
        self.T_right = T_right
        self.alpha = alpha
        self.nx = nx
        self.nt = nt
        self.dt = dt
        
        # 공간 격자
        self.x = np.linspace(0, L, nx)
        self.dx = L / (nx - 1)
        
        # 안정성 조건 확인 (FTCS 방법)
        r = alpha * dt / (self.dx**2)
        if r > 0.5:
            print(f"경고: 안정성 조건 위반 (r = {r:.3f} > 0.5)")
            print(f"dt를 {0.5 * self.dx**2 / alpha:.6f} 이하로 줄이세요.")
        
        # 초기 조건
        self.T_initial = np.full(nx, T0)
        self.T_initial[0] = T_left
        self.T_initial[-1] = T_right
    
    def analytical_solution(self, t):
        """
        해석해: 경계 조건 T(0,t)=T_left, T(L,t)=T_right, 초기 조건 T(x,0)=T0
        푸리에 급수 전개 사용
        """
        T = np.zeros_like(self.x)
        
        # 정상 상태 해
        T_steady = self.T_left + (self.T_right - self.T_left) * self.x / self.L
        
        # 과도 응답 (푸리에 급수)
        n_terms = 100  # 급수 항의 개수
        for n in range(1, n_terms + 1):
            lambda_n = n * np.pi / self.L
            coeff = 2 / (n * np.pi) * (
                (self.T0 - self.T_left) * (1 - (-1)**n) +
                (self.T_right - self.T_left) * (-1)**n
            )
            T += coeff * np.sin(lambda_n * self.x) * np.exp(-self.alpha * lambda_n**2 * t)
        
        return T_steady + T
    
    def numerical_solution_ftcs(self):
        """
        수치해법: FTCS (Forward Time Central Space) 방법
        """
        T = self.T_initial.copy()
        T_history = [T.copy()]
        
        r = self.alpha * self.dt / (self.dx**2)
        
        for _ in range(self.nt):
            T_new = T.copy()
            
            # 내부 점들 업데이트
            for i in range(1, self.nx - 1):
                T_new[i] = T[i] + r * (T[i+1] - 2*T[i] + T[i-1])
            
            # 경계 조건 유지
            T_new[0] = self.T_left
            T_new[-1] = self.T_right
            
            T = T_new
            T_history.append(T.copy())
        
        return np.array(T_history)
    
    def animate_temperature(self, method='numerical', save_gif=False):
        """
        온도 프로파일 애니메이션 생성
        """
        fig, ax = plt.subplots(figsize=(10, 6))
        
        if method == 'analytical':
            # 해석해 애니메이션
            line, = ax.plot(self.x, self.T_initial, 'b-', linewidth=2, label='Analytical')
            ax.set_xlim(0, self.L)
            ax.set_ylim(min(self.T_left, self.T_right, self.T0) - 10, 
                       max(self.T_left, self.T_right, self.T0) + 10)
            ax.set_xlabel('Position x (m)', fontsize=12)
            ax.set_ylabel('Temperature T (℃)', fontsize=12)
            ax.set_title('1D Heat Conduction - Analytical Solution', fontsize=14, fontweight='bold')
            ax.grid(True, alpha=0.3)
            ax.legend()
            
            time_text = ax.text(0.02, 0.95, '', transform=ax.transAxes, fontsize=12,
                              verticalalignment='top', bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
            
            def animate(frame):
                t = frame * self.dt
                T = self.analytical_solution(t)
                line.set_ydata(T)
                time_text.set_text(f'Time t = {t:.4f} s')
                return line, time_text
            
            anim = FuncAnimation(fig, animate, frames=self.nt, interval=50, blit=True, repeat=True)
        
        else:  # numerical
            T_history = self.numerical_solution_ftcs()
            
            line, = ax.plot(self.x, T_history[0], 'r-', linewidth=2, label='Numerical (FTCS)')
            ax.set_xlim(0, self.L)
            ax.set_ylim(min(self.T_left, self.T_right, self.T0) - 10, 
                       max(self.T_left, self.T_right, self.T0) + 10)
            ax.set_xlabel('Position x (m)', fontsize=12)
            ax.set_ylabel('Temperature T (℃)', fontsize=12)
            ax.set_title('1D Heat Conduction - Numerical Method (FTCS)', fontsize=14, fontweight='bold')
            ax.grid(True, alpha=0.3)
            ax.legend()
            
            time_text = ax.text(0.02, 0.95, '', transform=ax.transAxes, fontsize=12,
                              verticalalignment='top', bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
            
            def animate(frame):
                line.set_ydata(T_history[frame])
                time_text.set_text(f'Time t = {frame * self.dt:.4f} s')
                return line, time_text
            
            anim = FuncAnimation(fig, animate, frames=len(T_history), interval=50, blit=True, repeat=True)
        
        if save_gif:
            anim.save(f'heat_conduction_1d_{method}.gif', writer='pillow', fps=20)
            print(f"애니메이션이 'heat_conduction_1d_{method}.gif'로 저장되었습니다.")
        
        plt.tight_layout()
        plt.show()
        
        return anim


if __name__ == "__main__":
    # 예제 실행
    # 안정성을 위해 dt를 충분히 작게 설정
    dx = 0.01
    dt = 0.5 * dx**2 / 0.01  # 안정성 조건: r <= 0.5
    
    # 해석해
    heat_1d_analytical = HeatConduction1D(
        L=1.0, T0=0.0, T_left=100.0, T_right=0.0,
        alpha=0.01, nx=100, nt=2000, dt=dt
    )
    print("1D 열전도 - 해석해 애니메이션 생성 중...")
    heat_1d_analytical.animate_temperature(method='analytical', save_gif=True)
    
    # 수치해법
    heat_1d_numerical = HeatConduction1D(
        L=1.0, T0=0.0, T_left=100.0, T_right=0.0,
        alpha=0.01, nx=100, nt=2000, dt=dt
    )
    print("1D 열전도 - 수치해법 애니메이션 생성 중...")
    heat_1d_numerical.animate_temperature(method='numerical', save_gif=True)
