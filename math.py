import numpy as np
from scipy.integrate import odeint

class Interaction:
    
    def __init__(self):
        
        seconds_in_year = 365*24*3600
        seconds_in_day = 24*3600
        self.t = np.arange(0, 3*seconds_in_year, 0.1*seconds_in_day)
        
        self.G = 6.67*10**(-11)
        self.ae = 149.6*10**9
        self.m_cob = 1.9885*10**30
        self.x_cob = 0
        self.y_cob = 0
        
    def init_pos(self):
        x10 = 0
        vx10 = 0
        y10 = 0 
        vy10 = 0

        self.s0 = x10, vx10, y10, vy10
    
    def _func(self, s, t):
        x1, vx1, y1, vy1 = s
    
        dxdt1 = vx1
        dvxdt1 = -self.G * self.m_cob * (x1 - self.x_cob) / ((x1 - self.x_cob)**2 + (y1 - self.y_cob)**2)**1.5
    
        dydt1 = vy1
        dvydt1 = -self.G * self.m_cob * (y1 - self.y_cob) / ((x1 - self.x_cob)**2 + (y1 - self.y_cob)**2)**1.5
    
        return dxdt1, dvxdt1, dydt1, dvydt1
    
    def _solve_func(self):
       
        sol = odeint(Interaction.func(self.s, self.t), self.s0, self.t)
    
        self.x1 = sol[:, 0]
        self.y1 = sol[:, 2]
    
        return self.x1/self.ae, self.y1/self.ae
    