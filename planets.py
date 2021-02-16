import interaction as m
import tkinter as tk
import numpy as np

class Ball:
    
    def __init__(self, canvas, window, t_end, x0, vx0, y0, vy0, m_c, r):
        self.canvas = canvas
        self.window = window
        self.ball = self.canvas.create_oval(x0/m.Interaction.ae-r, 
                                            y0/m.Interaction.ae-r,
                                            x0/m.Interaction.ae+r,
                                            y0/m.Interaction.ae+r)
        
        self.interect = m.Interaction(t_end, 
                                      x0*m.Interaction.ae,
                                      vx0,
                                      y0*m.Interaction.ae,
                                      vy0,
                                      m_c)
        
    def interaction(self):

        self.x = self.interect.solve_func()[0]*200
        self.y = self.interect.solve_func()[1]*180
        
        return self.x, self.y
    
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
    x0 = 149*10**9
    y0 = 0
    radius = 5
    
    ball = Ball(canvas, window,
                t_end=24*3600*365,
                x0 = x0,
                vx0 = 0,
                y0 = y0,
                vy0 = 30000,
                m_c = 1.9885*10**30,
                r = radius)
    
    ball.move_ball()
    
tk.Button(window, text='Create ball', command=create_func).pack()

window.mainloop()
