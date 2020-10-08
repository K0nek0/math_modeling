import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
line, = ax.plot([], [], 'o')
xdata, ydata = [], []
n = 100
x = np.zeros(n)
y = np.zeros(n)
C = 0.3
D = 0.33
for i in range(1, n, 1):
    x[i] = x[i-1]**2 - y[i-1]**2 + C
    y[i] = 2*x[i-1] * y[i-1] + D

def anim(i):
    xdata.append(x[i])
    ydata.append(y[i])
    line.set_data(xdata, ydata)
    return line,

plt.xlim(-0.5, 0.5)
plt.ylim(-0.5, 0.8)
anim = FuncAnimation(fig, anim, frames=500, interval=20)
anim.save('point.gif')
