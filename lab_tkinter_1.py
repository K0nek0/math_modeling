import tkinter as tk
import random

window = tk.Tk()

button_1 = tk.Button(text='Бросить',
                     width=20,
                     height=10,
                     bg='green',
                     fg='red')
button_1.pack()

label_1 = tk.Label(master=window, text='0')
label_1.pack()

def click_left_mouse(event):
    value = random.randint(1, 6)
    label_1['text'] = '{}'.format(value)

button_1.bind('<Button-1>', click_left_mouse)

window.mainloop()
