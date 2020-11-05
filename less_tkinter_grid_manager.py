import tkinter as tk

window = tk.Tk()

for i in range(3):
    window.columnconfigure(i, weight=1, minsize=75)
    window.rowconfigure(i, weight=1, minsize=50)
    for j in range(3):
        frame = tk.Frame(master=window,
                         relief=tk.SUNKEN,
                         borderwidth=1)
        frame.grid(row=i, column=j)
        label = tk.Label(master=frame, text=f'row {i} \n Col {j}')
        label.pack()


window.mainloop()
