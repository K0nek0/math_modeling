import tkinter as tk

window = tk.Tk()

frame = tk.Frame(master=window, width=150, height=150)
frame.pack()

label_1 = tk.Label(master=frame, text='qwer', bg='red')
label_1.place(x=0, y=0)

label_2 = tk.Label(master=frame, text='asd', bg='blue')
label_2.place(x=100, y=100)

button = tk.Button(bg='black')
button.place(x=100, y=100)

window.mainloop()
