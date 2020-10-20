from sympy import symbols
from sympy import sin, cos, pi, exp
from sympy import Eq, solve, solveset, linsolve, nonlinsolve

x, y, z = symbols('x y z')

expr = x**2 - 2
solve_expr = solve(expr, x)
print(solve_expr)

#expr = sin(x**2) - exp(-2*x) + cos(pi/x)
#solve_expr = solve(expr, x)
#print(solve_expr)

expr = Eq(x, y)
print(expr)

expr = Eq(3, 1)
print(expr)

expr = Eq(3, 3)
print(expr)

solve_expr = solveset(x**2 - 2, x)
print(solve_expr)

expr = sin(x**2) - exp(-2*x) + cos(pi/x)
solve_expr = solveset(expr, x)
print(solve_expr)

system = [x +y + z - 1, x + y + 2*z - 3, x - 2*y + z]
solve_system = linsolve(system, (x, y, z))
print(solve_system)

system = [x**2 + x, x - y]
solve_system = nonlinsolve(system, (x, y))
print(solve_system)

system = [x**2 + 1, y**2 + 1]
solve_system = nonlinsolve(system, [x, y])
print(solve_system)

system = [x**2 - 2*y**2 - 2, x*y - 2]
solve_system = nonlinsolve(system, [x, y])
print(solve_system)