import matplotlib.pyplot as plt
import numpy as np

def ellips(e, p):
    
    alpha = np.arange(-2*np.pi, 2*np.pi, 0.1)
    
    r = p/(1 + e*np.cos(alpha))
    
    x = r*np.cos(alpha)
    y = r*np.sin(alpha)
    
    plt.plot(x, y)
    plt.show()
    
ellips(0.3, 3)
