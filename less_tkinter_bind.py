import tkinter as tk

window = tk.Tk()

button_1 = tk.Button(text='Najmi',
                     width=50,
                     height=25,
                     bg='green',
                     fg='red')
button_1.pack()


def click_left_mouse(event):
    print('Molodec, najal left button')
    
def click_right_mouse(event):
    print('Toje molodec, najal right button')
    
    
button_1.bind('<Button-1>', click_left_mouse)
button_1.bind('<Button-3>', click_right_mouse)

window.mainloop()
