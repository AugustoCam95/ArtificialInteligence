import numpy as np
from sympy import *
init_printing()
x,y = symbols('x y')

def f(x,y): return ((4-((2.1)*(x**2))+((1/3)*(x**4)))*(x**2))+(x*y)-((4*(1-(y**2)))*(y**2))
def gx(x,y): return (8*x-8.4*(x**3)+2*(x**5)+y)
def gy(x,y): return (x+16*(y**3)-8*y)
def hesssx(x,y): return	(8-25.2*(x**2)+10*(x**4))
def hesssy(x,y): return (48*(y**2)-8)



print("Função a ser otimizada:")
print(f(x,y))
print("\n")

gradiente = np.array([gx(x,y), gy(x,y)])
hessiana = np.array([[hesssx(x,y), 1.],
					 [1., hesssy(x,y)]])

print("Vetor gradiente:")
print(gradiente)
print("\n")
print("Matriz hessiana:")
print(hessiana)