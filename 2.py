import tkinter as tk
import numpy as np

window = tk.Tk()

t = np.arange(0, 100, 0.1)

x0 = 0
y0 = 0
vx0 = 10
vy0 = -10

radius = 15
g = 10


canvas = tk.Canvas(width=600, height=600)
canvas.pack()

points = [100, 250, 100, 150, 150, 250]
canvas.create_polygon(points, width=5)

#def move_func():
    

ball = canvas.create_oval(150,
                          200,
                          180,
                          230,
                          fill='blue',
                          outline='white',
                          width=4)

#button_1 = tk.Button(window,
#                     text='Update',
#                     command=move_func)
#
#button_1.pack()

x_coords = x0 + vx0 * t
y_coords = y0 + vy0 * t + g*t**2/2

i = 0

while True:
    canvas.move(ball, x_coords[i], y_coords[i])
    window.update()
    window.after(100)
    i += 1
    
    if i == 200:
        break
