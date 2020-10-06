import matplotlib.pyplot as plt
import numpy as np

def lissag(a, b, A, B):
    
    t = np.linspace(0, np.pi*12, 100)
    p = np.pi/2
    
    x = A * np.sin(a*t + p)
    y = B * np.sin(p*t)

    plt.plot(x, y)    
    plt.show()

lissag(1, 2, 1, 7)
