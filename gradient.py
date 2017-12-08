import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

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

print("\n")
print("-------------Método gradiente---------------")
maxiter = int(input("Máximo de iterações: "))
a = float(input("Valor do alfa: "))
b = float(input("Valor inicial do x: ")) 
c = float(input("Valor inicial do y: "))
tol = 0.00000001

iterações = 0 #iterações inicializa com zero.

p = np.array([gradx(b,c),grady(b,c)])
old = np.array([b,c])
d = -p
viter = [old]

while True:
	new = old + a*d
	viter.append(new)
	err = np.abs(fun(old[0],old[1])-fun(new[0],new[1]))
	iterações = iterações + 1
	print("passo:",iterações)
	print("Novo [x,y]:")
	print(new)
	print("valor de f(x,y):")
	print(fun(new[0],new[1]))
	old = new
	p = np.array([gradx(old[0],old[1]),grady(old[0],old[1])])
	d = -p 
	print("\n")
	if iterações == maxiter or err < tol:
		break;


xx = []
yy = []
z = []

for i in range(len(viter)):
	xx.append(viter[i][0])
	yy.append(viter[i][1])
	z.append(fun(viter[i][0],viter[i][1]))

x = np.arange(-3,3, 0.25)
y = np.arange(-2,2, 0.25)
x,y = np.meshgrid(x,y)
function = ((4-((2.1)*(x**2))+((1/3)*(x**4)))*(x**2))+(x*y)-((4*(1-(y**2)))*(y**2))

fig = plt.figure()
ax = Axes3D(fig)
ax.plot_surface(x,y,function, rstride = 1, cstride = 1, cmap=cm.viridis)
ax.plot(xx,yy,z)
ax.scatter(xx,yy,z, c = 'r', marker = 'o', alpha = 1)
ax.set_xlabel("x1")
ax.set_ylabel("x2")
ax.set_zlabel("f(x1,x2)")

plt.show()
