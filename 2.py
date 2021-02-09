import numpy as np
from scipy.integrate import odeint
import tkinter as tk

class Planets:
    
    G = 6.67*10**(-11)
    m_center_ob = 1.99*10**30
    x_center_ob = 0
    y_center_ob = 0
    
    def __init__(self, canvas, window, x1, y1, x2, y2):
        self.canvas = canvas
        self.window = window
        self.ball = self.canvas.create_oval(x1, y1, x2, y2)
        
    def interaction(self, s):
        x, vx, y, vy = s
    
        dxdt = vx
        dvxdt = (-G * m_center_ob * (x_ob - x_center_ob) / ((x_ob - x_center_ob)**2 + (y_ob - y_center_ob)**2)**1.5)
    
        dydt = vy
        dvydt = (-G * m_center_ob * (y_ob - y_center_ob) / (((x_ob - x_center_ob)**2 + (y_ob - y_center_ob)**2)**1.5)
        
        return dxdt, dvxdt, dydt, dvydt
    
    def move_ball(self, counter=0):
        if counter < len(self.interaction()[0]):
            self.canvas.move(self.ball,
                             self.interaction()[0][counter],
                             self.interaction()[1][counter])

            self.window.after(10, lambda: self.move_ball(counter+1))
        
window = tk.Tk()
canvas = tk.Canvas(window, width=1000, height=600)
canvas.pack()

def create_func():
    x0 = randint(0, 400)
    y0 = randint(0, 400)
    radius = randint(10, 100)
    
    ball = Ball(canvas, window,
                x1 = x0-radius,
                y1 = y0-radius,
                x2 = x0+radius,
                y2 = y0+radius)
    
    ball.move_ball()
    
tk.Button(window, text='Create ball', command=create_func).pack()

window.mainloop()