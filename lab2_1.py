a=int(input("Ведите а "))
b=int(input('Веедите b '))
c=int(input('Введите c '))

#x**2 + b*x + c 
D=b**2-4*a*c

if D > 0:
    x1 = -b + D**1/2 / 2*a
    x2 = -b - D**1/2 / 2*a
    print("Ответ", x1)
    
elif D == 0:
    x1 = -b / 2*a
    print("Ответ", x1)
    
elif D < 0:
    print("Нет действительных корней")
