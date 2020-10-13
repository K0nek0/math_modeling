import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


fig, ax = plt.subplots()
ax = plt.axes(xlim=(-25, 25), ylim=(-25,25))
line, = ax.plot([], [], 'r')

xdata, ydata = [], []

t = np.arange(0, 4*np.pi, 100)
    
x = 12*np.cos(t) + 8*np.cos(1.5*t)
y = 12*np.sin(t) - 8*np.sin(1.5*t)

def star(i):
        
    time = 0.1*i
  
    X = x*np.cos(time) - y*np.sin(time)
    Y = y*np.cos(time) + x*np.sin(time)
    
    xdata.append(X)
    ydata.append(Y)
        
    line.set_data(xdata, ydata)
    
    return line,
    
anim = FuncAnimation(fig, star, frames=500, interval=20)
anim.save('star.gif')
