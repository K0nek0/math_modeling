import tkinter as tk

window = tk.Tk()

text_1 = tk.Label(text='qwer')
label_1 = tk.Label(text='asd',
                   bg='black',
                   fg='green',
                   width='20',
                   height='10')

text_1.pack()
label_1.pack()

window.mainloop()
