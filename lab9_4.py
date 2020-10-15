import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

t = np.arange(0, 20, 0.1)

def dif_func(h, t):
#    dh_dt = nu*(2*g*h)**1/2 * (S/np.pi*D**2)
    dh_dt = - nu*(2*g*h)**1/2 * ((np.pi*d**2/4)/3*h**2*D)
    return dh_dt

g = 9.8
h0 = 0.11
D = 0.08
d = 0.03
nu = 0.97
S = 0.03

sol = odeint(dif_func, h0, t)

plt.plot(t, sol[:,0])
plt.show()
