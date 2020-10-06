import matplotlib.pyplot as plt
import numpy as np

def func(a, b, A, B):
    
    x = np.arange(A, B, 1)
    y = np.zeros(len(x))

    for i in range(len(x)):
        
        if x[i] < a:
            y[i] = a**2
            
        elif a <= i <= b:
            y[i] = x**2
            
        elif x[i] > b:
            y[i] = b**2
    
    plt.plot(x, y)
    plt.xlim(A, B)
    plt.ylim(A, B)
    plt.show()
    
func(3, 7, -7, 17)
