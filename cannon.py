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


canvas = tk.Canvas(width=800, height=600)

points = [100, 250, 100, 150, 150, 250]
canvas.create_polygon(points, width=5)
canvas.create_line(100, 250, 1000, 250)

canvas.pack()

ball = canvas.create_oval(150,
                          200,
                          180,
                          230,
                          fill='blue',
                          outline='white',
                          width=4)

x_coords = x0 + vx0 * t
y_coords = y0 + vy0 * t + g*t**2/2

i = 0

def stop():
    x_coords = x0 + 0 * t
    y_coords = y0 + 0 * t + 0*t**2/2
    
    return x_coords, y_coords

button_stop = tk.Button(window, text='Сбрось силы шарика', command=stop)
button_stop.pack()

while True:
    canvas.move(ball, x_coords[i], y_coords[i])
    window.update()
    window.after(100)
    i += 1

    if y_coords[i] >= 18:
        break


window.mainloop()
