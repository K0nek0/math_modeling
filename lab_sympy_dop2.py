from sympy import symbols, solveset
from sympy.vector import CoordSys3D

N = CoordSys3D("N")
a, b, x = symbols("a b x")

a = 7*N.i + 2*N.j - 8*N.k
b = -4*N.i + x*N.j + 9*N.k

sol = a.dot(b)
sol_new = solveset(sol, x)
print(sol_new)
