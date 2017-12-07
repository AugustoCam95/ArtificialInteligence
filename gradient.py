import numpy as np

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

from sympy import *
init_printing()
x,y = symbols('x y')
def f(x,y): return ((4-((2.1)*(x**2))+((1/3)*(x**4)))*(x**2))+(x*y)-((4*(1-(y**2)))*(y**2))
def gx(x,y): return (8*x-8.4*(x**3)+2*(x**5)+y)
def gy(x,y): return (x+16*(y**3)-8*y)
def hesssx(x,y): return	(8-25.2*(x**2)+10*(x**4))
def hesssy(x,y): return (48*(y**2)-8)

def fun(x,y):
    return ((4-((2.1)*(x**2))+((1/3)*(x**4)))*(x**2))+(x*y)-((4*(1-(y**2)))*(y**2))

def gradx(x,y):
	return 8*x-8.4*(x**3)+2*(x**5)+y

def grady(x,y):
	return x+16*(y**3)-8*y

def hessxx(x):
	return 8-25.2*(x**2)+10*(x**4)

def hessyy(y):
	return 48*(y**2)-8

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

print("\n")
print("-------------Método gradiente---------------")
maxiter = int(input("Máximo de iterações: "))
a = float(input("Valor do alfa: "))
b = float(input("Valor inicial do x: ")) 
c = float(input("Valor inicial do y: "))
tol = 0.000001

iterações = 0 #iterações inicializa com zero.

p = np.array([gradx(b,c),grady(b,c)])
old = np.array([b,c])
d = -p

while True:
	new = old + a*d
	err = np.abs(fun(old[0],old[1])-fun(new[0],new[1]))
	iterações = iterações + 1
	print("passo:",iterações)
	print("Novo x:")
	print(new)
	print("valor de f(x,y):")
	print(fun(new[0],new[1]))
	old = new
	p = np.array([gradx(old[0],old[1]),grady(old[0],old[1])])
	d = -p 
	print("\n")
	if iterações == maxiter or err < tol:
		break;


eixox = np.arange(-5,5, 0.25)
eixoy = np.arange(-5,5, 0.25)
eixox,eixoy = np.meshgrid(eixox,eixoy)
function = ((4-((2.1)*(x**2))+((1/3)*(x**4)))*(x**2))+(x*y)-((4*(1-(y**2)))*(y**2))

fig = plt.figure()
ax = Axes3D(fig)
ax.plot_surface(eixox,eixoy,function, rstride = 1, cstride = 1, cmap=cm.viridis)

plt.show()
