import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

x = np.arange(-5,5, 0.25)
y = np.arange(-5,5, 0.25)
x,y = np.meshgrid(x,y)
function = ((4-((2.1)*(x**2))+((1/3)*(x**4)))*(x**2))+(x*y)-((4*(1-(y**2)))*(y**2))

fig = plt.figure()
ax = Axes3D(fig)
ax.plot_surface(x,y,function, rstride = 1, cstride = 1, cmap=cm.viridis)

plt.show()
