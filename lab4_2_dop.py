def fib(n):
    a = 1
    if n > 2:
        a = fib(n-1) + fib(n-2)
        
    elif n < -1:
        a = ((-1)**(n+1)) * fib(-n)
        
    return a

print(fib(-5))