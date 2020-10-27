from sympy import symbols
from sympy import sin, cos, exp

a = 3

a, p, o = symbols('a p o')

ch = (exp(a) + exp(-a))/2
sh = (exp(a) - exp(-a))/2

x = (a*sh.subs(o, p)) / ch.subs(o, p) - cos(o)
y = (a*sin(p)) / ch.subs(o, p) - cos(o)

print(x.subs(p, a))
