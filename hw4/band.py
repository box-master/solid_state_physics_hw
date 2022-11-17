import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

a,U0,U1 = 1,5,5
step_numbers = 100

def energy(kx,ky):
    A = np.array([[(kx-2*np.pi)**2+(ky-2*np.pi)**2,0,U0,U0,U1,0,0,0,0],[0,(kx-2*np.pi)**2+(ky+2*np.pi)**2,0,U0,U1,0,U0,0,0],[U0,0,kx**2+(ky-2*np.pi)**2,U1,U0,U1,0,U0,0],[U0,U0,U1,(kx-2*np.pi)**2+ky**2,U0,0,U1,0,0],[U1,U1,U0,U0,kx**2+ky**2,U0,U0,U1,U1],[0,0,U1,0,U0,(kx+2*np.pi)**2+ky**2,U1,U0,U0],[0,U0,0,U1,U0,U1,kx**2+(ky+2*np.pi)**2,0,U0],[0,0,U0,0,U1,U0,0,(kx+2*np.pi)**2+(ky-2*np.pi)**2,0],[0,0,0,0,U1,U0,U0,0,(kx+2*np.pi)**2+(ky+2*np.pi)**2]])
    return sorted(np.linalg.eigvals(A))

first_brillouin_zone_x,first_brillouin_zone_y = np.linspace(-np.pi,np.pi,step_numbers),np.linspace(-np.pi,np.pi,step_numbers)
epsilon = [[] for i in range(9)]


i = 0
for a in epsilon:
    j = 0
    for kx in first_brillouin_zone_x:
        a.append([])
        for ky in first_brillouin_zone_y:
            a[j].append(energy(kx,ky)[i])
        j+=1
    i+= 1


# 3Dplot
figure = plt.figure(figsize=(10,8))
axe = plt.axes(projection='3d')
for a in epsilon:
    axe.contour3D(first_brillouin_zone_x,first_brillouin_zone_y,a,100,cmap='binary')
axe.set_xlabel('kx')
axe.set_ylabel('ky')
axe.set_zlabel('energy');
plt.show()


 # contour plot
 figure,axes = plt.subplots(3,3,figsize=(14,8.5))
 axes = axes.flatten()

 i = 0
 for axe in axes:
     cf = axe.contourf(first_brillouin_zone_x,first_brillouin_zone_y,epsilon[i],levels
             =100,cmap='jet')
     figure.colorbar(cf)
     i+=1

axe.set_xlabel('kx')
axe.set_ylabel('ky')
plt.show()




