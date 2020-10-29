from sympy import symbols
from sympy.vector import CoordSys3D
from sympy import sin, cos, trigsimp

x, y, z = symbols('x y z')
N = CoordSys3D('N')
a, b, c = symbols('a b c')

v = N.i - 2*N.j
print(v/3)

v1 = 2*N.i + 3*N.j - N.k
v2 = N.i - 4*N.j + N.k

sol = v1.dot(v2)
print(sol)

v = (a*b + a*c + b**2 + b*c)*N.i +N.j
sol = v.factor()
print(sol)

v = (sin(a)**2 + cos(a)**2)*N.i - (2*cos(b)**2 -1)*N.k
sol = trigsimp(v)
print(sol)
