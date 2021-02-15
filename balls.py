import math as m
import tkinter as tk
import numpy as np

class Ball:
    
    def __init__(self, canvas, window, x1, y1, x2, y2):
        self.canvas = canvas
        self.window = window
        self.x1 = x1
        self.ball = self.canvas.create_oval(x1, y1, x2, y2)
        
    def interaction(self):
        self.onebdy.init_pos()
        self.y = np.sin(self.x)
        
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
    onebody = m.Interaction()
    ball = Ball(onebody, x1, y1, x2, y2)
    x0 = 0
    y0 = 0
    radius = 5
    
    ball = Ball(canvas, window,
                x1 = x0-radius,
                y1 = y0-radius,
                x2 = x0+radius,
                y2 = y0+radius)
    
    ball.move_ball()
    
tk.Button(window, text='Create ball', command=create_func).pack()

window.mainloop()
