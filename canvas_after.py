import tkinter as tk

window = tk.Tk()
canvas = tk.Canvas()

def move_func():
    x = 10
    y = 10
    canvas.move(circle, x, y)
    window.after(50)

circle = canvas.create_oval(10,10,80,80, fill='white', width=2)
#canvas.after_idle(move_func)
canvas.pack()

button_update = tk.Button(window, text='Update', command=move_func)
button_update.pack()

window.mainloop()
