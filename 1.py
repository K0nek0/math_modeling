import tkinter as tk
import numpy as np
from scipy.integrate import odeint

t = np.arange(0, 10, 0.01)


def func(s, t):
    x, vx, y, vy = s
     
    dxdt = vx
    dvxdt = (-G * m_object * (x - x_object) / ((x - x_object)**2 + (y - y_object)**2)**1.5)
    
    dydt = vy
    dvydt = (-G * m_object * (y - y_object) / ((x - x_object)**2 + (y - y_object)**2)**1.5)

    return dxdt, dvxdt, dydt, dvydt


    
G = 6.67*10**(-11)

x0 = 0
vx0 = 0
y0 = 0   
vy0 = 0
    
x0_object = 1
vx0_object = 1
y0_object = 1   
vy0_object = 1

s0 = (x0, vx0, y0, vy0,
      x0_object, vx0_object, y0_object, vy0_object)

entry_1 = tk.Entry(fg='yellow',
                   bg='black',
                   width='50')

entry_2 = tk.Entry(fg='yellow',
                   bg='black',
                   width='50')

m = entry_1.get()
m_object = entry_2.get()

entry_1.pack()
entry_2.pack()


def create():    
    sol = odeint(func, s0, t)
    

    
    i = 0
    
    while True:
        canvas.move(sol, x[i], y[i])
        window.update()
        window.after(50)
        i += 1

button_create = tk.Button(window, text='Создать планеты', command=create)
button_create.pack()



window.mainloop()