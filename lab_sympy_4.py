from sympy import symbols
from sympy.solvers.inequalities import reduce_abs_inequality
from sympy import Abs

x = symbols('x')

sol = reduce_abs_inequality(Abs(x**2+2*x-3)+3*(x+1), '<', x)
print(sol)
