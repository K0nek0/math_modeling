import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
ax = plt.axes(xlim=(-5, 5), ylim=(-5,5))
line, = ax.plot([], [])

xdata, ydata = [], []

def babochka(i):
    
    t = 0.1 * i
     
    x = np.sin(t) * (np.exp(np.cos(t)) - 2*np.cos(4*t) + np.sin(t/12)**5)
    y = np.cos(t) * (np.exp(np.cos(t)) - 2*np.cos(4*t) + np.sin(t/12)**5)
    
    xdata.append(x)
    ydata.append(y)
    line.set_data(xdata, ydata)
    
    return line,


anim = FuncAnimation(fig, babochka, frames=500, interval=20)
anim.save('butterfly.gif')
