import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d


a = 1
U0,U1 = 1,1

def U(x,y):
    return 2*U0*(np.cos(2*np.pi*x/a)+np.cos(2*np.pi*y/a))+4*U1*np.cos(2*np.pi*x/a)*np.cos(2*np.pi*y/a)



x = np.linspace(0.,3.,100,endpoint=True)
y = np.linspace(0.,3.,100,endpoint=True)
x,y = np.meshgrid(x,y)
z = U(x,y)

figure = plt.figure(figsize=(10,8))
axe = plt.axes(projection='3d')
cf = axe.contourf(x,y,z,levels=200,cmap='binary')
axe.set_xlabel('x')
axe.set_ylabel('y')
axe.set_zlabel('potential')



plt.show()




