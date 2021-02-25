import numpy as np
from scipy.integrate import odeint


class Interaction:

    G = 6.67 * 10**(-11)
    ae = 149.6 * 10**9
    seconds_in_day = 24 * 3600

    def __init__(self, t_end, x0, vx0, y0, vy0, m_c, x_c, y_c):

        self.t = np.arange(0, t_end, 2 * Interaction.seconds_in_day)

        self.x0 = x0
        self.vx0 = vx0
        self.y0 = y0
        self.vy0 = vy0

        self.m_c = m_c
        self.x_c = x_c
        self.y_c = y_c

    def _func(self, s, t):
        x, vx, y, vy = s

        dxdt = vx
        dvxdt = (-Interaction.G * self.m_c * (x - self.x_c) /
                 ((x - self.x_c)**2 + (y - self.y_c)**2)**1.5)

        dydt = vy
        dvydt = (-Interaction.G * self.m_c * (y - self.y_c) /
                 ((x - self.x_c)**2 + (y - self.y_c)**2)**1.5)

        return dxdt, dvxdt, dydt, dvydt

    def solve_func(self):

        _s0 = self.x0, self.vx0, self.y0, self.vy0
        sol = odeint(self._func, _s0, self.t)

        self.x = sol[:, 0]
        self.y = sol[:, 2]

        return self.x / Interaction.ae, self.y / Interaction.ae
