def stepen_func(a, n):  
    i = 1
    c = a
    n_old = n
    if n < 0:
        n = - n
        while i < n:
            x = a*c
            i += 1
            a = x
    if n_old < 0:
        x = 1 / x
        
    if n > 0:
        n = n
        while i < n:
            x = a*c
            i += 1
            a = x
    if n_old > 0:
        a = x
        
    return x

print(stepen_func(2, -2))
