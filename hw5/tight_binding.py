import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits import mplot3d


a,t = 1,1
N = 100

def epsilon(kx,ky):
    return -2*t*(np.cos(kx*a)+np.cos(ky*a))


kx,ky = np.linspace(-np.pi/a,np.pi/a,N),np.linspace(-np.pi/a,np.pi/a,N)
kx,ky = np.meshgrid(kx,ky)
z = epsilon(kx,ky)


figure = plt.figure(figsize=(10,8))
axe = plt.axes(projection='3d')
cf = axe.contourf(kx,ky,z,levels=200,cmap='binary')
axe.set_xlabel('kx')
axe.set_ylabel('ky')
axe.set_zlabel('epsilon')

plt.show()
