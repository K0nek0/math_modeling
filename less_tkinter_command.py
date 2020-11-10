import tkinter as tk

window = tk.Tk()

window.rowconfigure(0, minsize=50, weight=1)
window.columnconfigure([0, 1, 2], minsize=50, weight=1)

label_1 = tk.Label(master=window, text='0')

label_1.grid(row=0, column=1)

def increase():
    value = int(label_1['text'])
    label_1['text'] = '{}'.format(value + 1)
    
def decrease():
    value = int(label_1['text'])
    label_1['text'] = '{}'.format(value - 1)
    

button_increase = tk.Button(master=window, text='+', command=increase)
button_decrease = tk.Button(master=window, text='-', command=decrease)

button_increase.grid(row=0, column=2, sticky='nsew')
button_decrease.grid(row=0, column=0, sticky='nsew')

window.mainloop()
