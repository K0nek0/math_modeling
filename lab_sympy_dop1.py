from sympy import symbols, acos
from sympy.vector import CoordSys3D

a, b, c = symbols('a b c')
N = CoordSys3D('N')

a = 4*N.i + 3*N.j + 8*N.k
b = -2*N.i + 8*N.j + 7*N.k
c = -5*N.i + 6*N.j + 12*N.k

a_mod = a.dot(a)
b_mod = b.dot(b)
c_mod = c.dot(c)

alpha_1 = acos(a.dot(b) / (a_mod*b_mod))
print(alpha_1.evalf())

alpha_2 = acos(a.dot(c) / (a_mod*c_mod))
print(alpha_2.evalf())

alpha_3 = acos(b.dot(c) / (b_mod*c_mod))
print(alpha_3.evalf())
