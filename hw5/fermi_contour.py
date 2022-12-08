import matplotlib.pyplot as plt
import numpy as np

a,t = 1,1
N = 1000

def epsilon(kx,ky):
    return -2*t*(np.cos(kx*a)+np.cos(ky*a))


kx,ky = np.linspace(-np.pi/a,np.pi/a,N),np.linspace(-np.pi/a,np.pi/a,N)
kx,ky = np.meshgrid(kx,ky)
z = epsilon(kx,ky)


figure = plt.figure(figsize=(10,8))
axe = plt.axes()
cs = axe.contour(kx,ky,z,levels=10)
axe.clabel(cs,cs.levels,inline=True)
plt.title("epsilon")

plt.show()



