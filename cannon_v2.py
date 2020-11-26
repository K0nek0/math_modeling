import tkinter as tk
import numpy as np

window = tk.Tk()

t = np.arange(0, 100, 0.1)

x0 = 0
y0 = 0
vx0 = 10
vy0 = -10

g = 10


canvas = tk.Canvas(width=800, height=600)

points = [100, 250, 100, 150, 150, 250]
canvas.create_polygon(points, width=5)
canvas.create_line(100, 250, 1000, 250)

canvas.pack()

def create(): 
    ball = canvas.create_oval(150,
                              200,
                              180,
                              230,
                              fill='blue',
                              outline='white',
                              width=4)
    return ball

def start():
    ball = create

    x = x0 + vx0 * t
    y = y0 + vy0 * t + g*t**2/2
    i = 0

    while True:
        canvas.move(ball, x[i], y[i])
        window.update()
        window.after(50)
        i += 1

        if y[i] >= 18:
          x = x0 + vx0 * t
          y = y0 + vy0 * t + g*t**2/2
          i = 0
          
          while True:
              canvas.move(ball, x[i], y[i])
              window.update()
              window.after(50)
              i += 1

              if y[i] >=0:
                  break

button_stop = tk.Button(window, text='Запустить шарик', command=start)
button_stop.pack()

window.mainloop()
