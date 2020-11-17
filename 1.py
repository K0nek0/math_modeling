import tkinter as tk
import numpy as np

window = tk.Tk()

x0 = 50
y0 = 50
radius = 30

canvas = tk.Canvas()
canvas.pack(fill='both', expand='True')

window.geometry(f'{800}x{800}')
window.configure(bg='black')


def move_func(x=-10, y=-10):
    canvas.move(ball, x, y)

ball = canvas.create_oval(x0-radius,
                          y0-radius,
                          x0+radius,
                          y0+radius,
                          fill='blue',
                          outline='white',
                          width=4)

button_1 = tk.Button(window,
                     text='Update',
                     command=move_func)

button_1.pack()

x_coords = np.arange(0, 100, 0.1)
y_coords = x_coords**2

i = 0

while True:
    canvas.move(ball, x_coords[i], y_coords[i])
    window.update()
    window.after(100)
    i += 1
    
    if i == 200:
        break
    