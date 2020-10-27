from sympy import symbols
from sympy import simplify, sqrt

a = symbols('a')

simp_expr = simplify((sqrt(a) - a/sqrt(a)+1)*a-1/sqrt(a))
print(simp_expr)
