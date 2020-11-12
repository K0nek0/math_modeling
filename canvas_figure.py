import tkinter as tk

window = tk.Tk()
canvas = tk.Canvas()

canvas.create_arc(10,10,80,80,outline='#f11',
                   fill='#f11', width=2)
canvas.create_oval(10,10,80,80,outline='#f11',
                   fill='white', width=2)
points = [23,45,63,23,45,17]
canvas.create_polygon(points, width=5)

canvas.pack()

window.mainloop()
