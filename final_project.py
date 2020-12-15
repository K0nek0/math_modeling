import numpy as np
from scipy.integrate import odeint
import tkinter as tk

window = tk.Tk()
canvas = tk.Canvas()
window.geometry(f'{800}x{600}')
canvas.configure(bg='black')
canvas.pack(fill='both', expand=True)

seconds_in_year = 365*24*3600
seconds_in_day = 24*3600
t = np.arange(0, 4*seconds_in_year, seconds_in_day)

G = 6.67*10**(-11)
ae = 149.6*10**9
mc = 2 * 10**30
ma = 1.06*mc+0.6*mc+0.3*mc

m1 = 1.06*mc
m2 = 0.6*mc
m3 = 0.3*mc

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
    
def solve_func():
    x10 = 3*ae
    vx10 = 0
    y10 = 0   
    vy10 = -np.sqrt(G*ma/(8*ae))
    
    x20 = 5*ae
    vx20 = 0
    y20 = 0   
    vy20 = np.sqrt(G*ma/(8*ae))
    
    x30 = 7*ae
    vx30 = 0
    y30 = 0   
    vy30 = np.sqrt(G*ma/(8*ae))
    
    s0 = (x10, vx10, y10, vy10,
          x20, vx20, y20, vy20,
          x30, vx30, y30, vy30)


    sol = odeint(func, s0, t)

    x1 = sol[:, 0]
    y1 = sol[:, 2]
    x2 = sol[:, 4]
    y2 = sol[:, 6]
    x3 = sol[:, 8]
    y3 = sol[:, 10]

    return x1/ae, y1/ae, x2/ae, y2/ae, x3/ae, y3/ae

def create_func(): 
    x0_1 = 300
    y0_1 = 300
    x0_2 = 500
    y0_2 = 300
    x0_3 = 700
    y0_3 = 300
    R = 20

    ball_1 = canvas.create_oval(x0_1-R,
                                y0_1-R,
                                x0_1+R,
                                y0_1+R,
                                fill='red')

    ball_2 = canvas.create_oval(x0_2-R,
                                y0_2-R,
                                x0_2+R,
                                y0_2+R,
                                fill='green')

    ball_3 = canvas.create_oval(x0_3-R,
                                y0_3-R,
                                x0_3+R,
                                y0_3+R,
                                fill='blue')

    return ball_1, ball_2, ball_3

def move_func():
    ball = create_func()

    x1 = solve_func()[0] * 80
    y1 = solve_func()[1] * 60
    x2 = solve_func()[2] * 80
    y2 = solve_func()[3] * 60
    x3 = solve_func()[4] * 80
    y3 = solve_func()[5] * 60

    i = 0

    while i < len(t)-1:
        canvas.move(ball[0], x1[i+1]-x1[i], y1[i+1]-y1[i])   
        canvas.move(ball[1], x2[i+1]-x2[i], y2[i+1]-y2[i])
        canvas.move(ball[2], x3[i+1]-x3[i], y3[i+1]-y3[i])

        window.update()
        window.after(25)
        i += 1

button_start = tk.Button(window, text='Начать', command=move_func)
button_start.pack()

window.mainloop()
