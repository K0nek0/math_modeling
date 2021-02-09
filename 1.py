import numpy as np
from scipy.integrate import odeint
import tkinter as tk

class Interaction:
    
    def __init__(self):
        
        seconds_in_year = 365*24*3600
        seconds_in_day = 24*3600
        t = np.arange(0, 3*seconds_in_year, 0.1*seconds_in_day)
        
        G = 6.67*10**(-11)
        ae = 149.6*10**9
        mc = 1.9885*10**30
        
        m1 = 1.2*mc
        m2 = 0.9*mc
        m3 = 0.7*mc
        m4 = 1.4*mc
        
        ma = m1+m2+m3+m4
        
    def inint_pos(self):
         x10 = float(entry_x1.get())*ae
        vx10 = 0
        y10 = float(entry_y1.get())*ae 
        vy10 = np.sqrt(G*ma/(10*ae))
    
        x20 = float(entry_x2.get())*ae
        vx20 = 0
        y20 = float(entry_y2.get())*ae 
        vy20 = -np.sqrt(G*ma/(10*ae))
    
        x30 = float(entry_x3.get())*ae
        vx30 = 0
        y30 = float(entry_y3.get())*ae    
        vy30 = np.sqrt(G*ma/(10*ae))
    
        x40 = float(entry_x4.get())*ae
        vx40 = 0
        y40 = float(entry_y4.get())*ae 
        vy40 = -np.sqrt(G*ma/(10*ae))
    
        s0 = (x10, vx10, y10, vy10,
              x20, vx20, y20, vy20,
              x30, vx30, y30, vy30,
              x40, vx40, y40, vy40)
        
    def func(s, t):
        (x1, vx1, y1, vy1,
         x2, vx2, y2, vy2,
         x3, vx3, y3, vy3,
         x4, vx4, y4, vy4) = s
    
        dxdt1 = vx1
        dvxdt1 = (-G * m2 * (x1 - x2) / ((x1 - x2)**2 + (y1 - y2)**2)**1.5
                  -G * m3 * (x1 - x3) / ((x1 - x3)**2 + (y1 - y3)**2)**1.5
                  -G * m4 * (x1 - x4) / ((x1 - x4)**2 + (y1 - y4)**2)**1.5)
    
        dydt1 = vy1
        dvydt1 = (-G * m2 * (y1 - y2) / ((x1 - x2)**2 + (y1 - y2)**2)**1.5
                  -G * m3 * (y1 - y3) / ((x1 - x3)**2 + (y1 - y3)**2)**1.5
                  -G * m4 * (y1 - y4) / ((x1 - x4)**2 + (y1 - y4)**2)**1.5)
    
        dxdt2 = vx2
        dvxdt2 = (-G * m1 * (x2 - x1) / ((x2 - x1)**2 + (y2 - y1)**2)**1.5
                  -G * m3 * (x2 - x3) / ((x2 - x3)**2 + (y2 - y3)**2)**1.5
                  -G * m4 * (x2 - x4) / ((x2 - x4)**2 + (y2 - y4)**2)**1.5)
    
        dydt2 = vy2
        dvydt2 = (-G * m1 * (y2 - y1) / ((x2 - x1)**2 + (y2 - y1)**2)**1.5
                  -G * m3 * (y2 - y3) / ((x2 - x3)**2 + (y2 - y3)**2)**1.5
                  -G * m4 * (y2 - y4) / ((x2 - x4)**2 + (y2 - y4)**2)**1.5)
    
        dxdt3 = vx3
        dvxdt3 = (-G * m1 * (x3 - x1) / ((x3 - x1)**2 + (y3 - y1)**2)**1.5
                  -G * m2 * (x3 - x2) / ((x3 - x2)**2 + (y3 - y2)**2)**1.5
                  -G * m4 * (x3 - x4) / ((x3 - x4)**2 + (y3 - y4)**2)**1.5)
    
        dydt3 = vy3
        dvydt3 = (-G * m1 * (y3 - y1) / ((x3 - x1)**2 + (y3 - y1)**2)**1.5
                  -G * m2 * (y3 - y2) / ((x3 - x2)**2 + (y3 - y2)**2)**1.5
                  -G * m4 * (y3 - y4) / ((x3 - x4)**2 + (y3 - y4)**2)**1.5)
    
        dxdt4 = vx4
        dvxdt4 = (-G * m1 * (x4 - x1) / ((x4 - x1)**2 + (y4 - y1)**2)**1.5
                  -G * m2 * (x4 - x2) / ((x4 - x2)**2 + (y4 - y2)**2)**1.5
                  -G * m3 * (x4 - x3) / ((x4 - x3)**2 + (y4 - y3)**2)**1.5)
    
        dydt4 = vy4
        dvydt4 = (-G * m1 * (y4 - y1) / ((x4 - x1)**2 + (y4 - y1)**2)**1.5
                  -G * m2 * (y4 - y2) / ((x4 - x2)**2 + (y4 - y2)**2)**1.5
                  -G * m3 * (y4 - y3) / ((x4 - x3)**2 + (y4 - y3)**2)**1.5)
    
        return (dxdt1, dvxdt1, dydt1, dvydt1,
                dxdt2, dvxdt2, dydt2, dvydt2,
                dxdt3, dvxdt3, dydt3, dvydt3,
                dxdt4, dvxdt4, dydt4, dvydt4)
    
    def solve_func():
       
    
        sol = odeint(func, s0, t)
    
        x1 = sol[:, 0]
        y1 = sol[:, 2]
        x2 = sol[:, 4]
        y2 = sol[:, 6]
        x3 = sol[:, 8]
        y3 = sol[:, 10]
        x4 = sol[:, 12]
        y4 = sol[:, 14]
    
        return x1/ae, y1/ae, x2/ae, y2/ae, x3/ae, y3/ae, x4/ae, y4/ae
    
    
