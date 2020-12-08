import tkinter as tk
import numpy as np

window = tk.Tk()

t = np.arange(0, 100, 0.1)

x0 = 0
y0 = 0
vx0 = 10
vy0 = -10

g = 10
R = 50

canvas = tk.Canvas(width=800, height=600)
canvas.pack()

def create():
    
    ball = canvas.create_oval(400-R,
                              300-R,
                              400+R,
                              300+R,
                              fill='blue',
                              width=4)

    return ball

def start():
    ball = create()

    
    x = 1
    y = 0
    
    i = 0

    while True:
        canvas.move(ball, x, y)
        window.update()
        window.after(50)
        i += 1
        

button_stop = tk.Button(window, text='Запустить шарик', command=start)
button_stop.pack()

window.mainloop()
