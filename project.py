import numpy as np
from scipy.integrate import odeint
import tkinter as tk

window = tk.Tk()
canvas = tk.Canvas()

seconds_in_year = 365*24*3600
seconds_in_day = 24*3600
week = seconds_in_day*7
t = np.arange(0, 4*seconds_in_year, week)
R = 0

def func(s, t):
    (x1, vx1, y1, vy1,
     x2, vx2, y2, vy2,
     x3, vx3, y3, vy3) = s
     
    dxdt1 = vx1
    dvxdt1 = (-G * m2 * (x1 - x2) / ((x1 - x2)**2 + (y1 - y2)**2)**1.5
              -G * m3 * (x1 - x3) / ((x1 - x3)**2 + (y1 - y3)**2)**1.5)
   
    dydt1 = vy1
    dvydt1 = (-G * m2 * (y1 - y2) / ((x1 - x2)**2 + (y1 - y2)**2)**1.5
              -G * m3 * (y1 - y3) / ((x1 - x3)**2 + (y1 - y3)**2)**1.5)
    
    dxdt2 = vx2
    dvxdt2 = (-G * m1 * (x2 - x1) / ((x2 - x1)**2 + (y2 - y1)**2)**1.5
              -G * m3 * (x2 - x3) / ((x2 - x3)**2 + (y2 - y3)**2)**1.5)
    
    dydt2 = vy2
    dvydt2 = (-G * m1 * (y2 - y1) / ((x2 - x1)**2 + (y2 - y1)**2)**1.5
              -G * m3 * (y2 - y3) / ((x2 - x3)**2 + (y2 - y3)**2)**1.5)
    
    dxdt3 = vx3
    dvxdt3 = (-G * m1 * (x3 - x1) / ((x3 - x1)**2 + (y3 - y1)**2)**1.5
              -G * m2 * (x3 - x2) / ((x3 - x2)**2 + (y3 - y2)**2)**1.5)
    
    dydt3 = vy3
    dvydt3 = (-G * m1 * (y3 - y1) / ((x3 - x1)**2 + (y3 - y1)**2)**1.5
              -G * m2 * (y3 - y2) / ((x3 - x2)**2 + (y3 - y2)**2)**1.5)
    
    return (dxdt1, dvxdt1, dydt1, dvydt1,
            dxdt2, dvxdt2, dydt2, dvydt2,
            dxdt3, dvxdt3, dydt3, dvydt3)
    
G = 6.67*10**(-11)
ае = 149.6*10**9
mc = 2 * 10**30
ma = 1.06*mc+0.6*mc+0.3*mc

m1 = 1.06*mc
m2 = 0.6*mc
m3 = 0.3*mc


def solve_func():

    x10 = 3*ае
    vx10 = 0
    y10 = 0   
    vy10 = -np.sqrt(G*ma/(8.3*ае))
    
    x20 = 5*ае
    vx20 = 0
    y20 = 0   
    vy20 = np.sqrt(G*ma/(8.3*ае))
    
    x30 = 7*ае
    vx30 = 0
    y30 = 0   
    vy30 = np.sqrt(G*ma/(8.3*ае))
    
    s0 = (x10, vx10, y10, vy10,
          x20, vx20, y20, vy20,
          x30, vx30, y30, vy30)


    sol = odeint(func, s0, t)

    return sol, x10, y10, x20, y20, x30, y30

def create_func(): 
    ball_1 = canvas.create_oval(solve_func()[1] - R,
                                solve_func()[2] - R,
                                solve_func()[1] + R,
                                solve_func()[2] + R,
                                fill='blue',
                                outline='white',
                                width=4)
    return ball_1

def move_func():
    ball_1 = create_func()
    ball_2 = create_func()
    ball_3 = create_func()

    coords = solve_func()

    x1 = coords[:, 0]
    y1 = coords[:, 2]

    x2 = coords[:, 4]
    y2 = coords[:, 6]

    x3 = coords[:, 8]
    y3 = coords[:, 10]

    while True:
        canvas.move(ball_1, x1, y1)
        canvas.move(ball_2, x2, y2)
        canvas.move(ball_3, x3, y3)
        window.update()


button_start = tk.Button(window, text='Начать', command=move_func)
button_start.pack()
