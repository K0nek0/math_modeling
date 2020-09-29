import numpy as np

N = int(input('Введите N '))
M = int(input('Введите M '))
a = np.ndarray(shape=(N, M))
b = np.ndarray(shape=(N, M))
c = np.ndarray(shape=(N, M))

for i in range (N):
    for j in range (M):
        a[i, j] = int(input('Введите элемент a {}, {}: '.format(i, j)))
        b[i, j] = int(input('Введите элемент b {}, {}: '.format(i, j)))
        
print(a)
print(b)

for i in range (N):
    for j in range (M):
        if a[i, j] > b[i, j]:
            c[i, j] = a[i, j]
        else:
            c[i, j] = b[i, j]
print(c)
