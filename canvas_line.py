import tkinter as tk

window = tk.Tk()
canvas = tk.Canvas()

canvas.create_line(15, 25, 200, 25, dash=(2,5))
canvas.create_line(25, 35, 200, 250, 300, 110)

canvas.pack()

window.mainloop()
