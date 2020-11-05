import tkinter as tk

window = tk.Tk()

button_1 = tk.Button(text='qwer',
                     width=25,
                     height=5,
                     bg='green',
                     fg='red')
button_1.pack()

button_2 = tk.Button(text='asd',
                     width=30,
                     height=40,
                     bg='green',
                     fg='red')

button_2.pack()

window.mainloop()
