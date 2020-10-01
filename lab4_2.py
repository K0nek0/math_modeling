def fib(n):
    a = 1
    if n > 2:
        a = fib(n-1) + fib(n-2)
    return a
print(fib(7))
