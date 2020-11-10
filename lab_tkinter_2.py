import tkinter as tk

window = tk.Tk()

window.rowconfigure(0, minsize=50, weight=1)
window.columnconfigure([0, 1, 2], minsize=50, weight=1)

label_1 = tk.Label(master=window)
label_1.grid(row=0, column=1)

label_2 = tk.Label(master=window,
                   text='Введите в градусах C')
label_2.grid()

entry_1 = tk.Entry(master=window, 
                   fg='black')

name = entry_1.get()
entry_1.insert(0, '')

entry_1.grid()


def cels():
    value = int(entry_1.get())
    label_1['text'] = '{}'.format(value)
    
def kelv():
    value = int(entry_1.get())
    label_1['text'] = '{}'.format(value + 273.15)
    
button_cels = tk.Button(master=window, text='Конвертировать в C', command=cels)
button_kelv = tk.Button(master=window, text='Конвертировать в K', command=kelv)

button_cels.grid(row=0, column=0, sticky='nsew')
button_kelv.grid(row=0, column=2, sticky='nsew')

window.mainloop()
