from sympy import symbols, sqrt
from sympy.vector import CoordSys3D

x, y, z = symbols('x y z')
N = CoordSys3D('N')
q1 = 1
q2 = -0.5

E1_v = q1*x*N.i/sqrt(x**2+y**2+z**2)**3 + \
       q1*y*N.j/sqrt(x**2+y**2+z**2)**3 + \
       q1*z*N.k/sqrt(x**2+y**2+z**2)**3

E2_v = q2*(x-1)*N.i/sqrt((x-1)**2+(y-1)**2+(z-1)**2)**3 + \
       q2*(y-1)*N.j/sqrt((x-1)**2+(y-1)**2+(z-1)**2)**3 + \
       q2*(z-1)*N.k/sqrt((x-1)**2+(y-1)**2+(z-1)**2)**3

E = E1_v + E2_v
E_subs = E.subs([(x, 3), (y, 4), (z, 5)])
print(E_subs.evalf())
