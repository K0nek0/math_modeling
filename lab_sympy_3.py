from sympy import symbols
from sympy import sin, cos, pi, exp
from sympy import Eq, solve, solveset, linsolve, nonlinsolve

x, y, z, E = symbols('x y z E')

expr = x**2 + x + 1/x + 1/x**2 - 4
solve_expr = solve(expr, x)
print(solve_expr)

e = 0.8
M = 9
expr = E - e*sin(E - M)
solve_expr = solveset(expr, E)
print(solve_expr)
