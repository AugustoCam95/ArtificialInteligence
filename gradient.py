
import numpy as np

iter = 0

maxiter = int(input("Máximo de iterações: "))
a = float(input("Valor do alfa: "))
x = float(input("Valor inicial do x: ")) 
y = float(input("Valor inicial do y: "))

p = np.array([8*x-8.4*(x**3)+2*(x**5)+y,x-4*(2*(y**2)-4*(y**3))])
d = -p
old = np.array([x,y])

while iter < maxiter:
	new = old + a*d
	
	
	iter=iter+1
	print("passo:")
	print(iter)
	print("f(x,y):")
	print(new)
	print("\n")
	
	print("\n")
	
	old = new
	r = np.array([8*new[0]-8.4*(new[0]**3)+2*(new[0]**5)+new[1],new[0]-4*(2*(new[1]**2)-4*(new[1]**3))]) 
	d = -r