import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

a,U0,U1 = 1,5,5
step_numbers = 100

def energy(kx,ky):
    A = np.array([[(kx-2*np.pi)**2+(ky-2*np.pi)**2,0,U0,U0,U1,0,0,0,0],[0,(kx-2*np.pi)**2+(ky+2*np.pi)**2,0,U0,U1,0,U0,0,0],[U0,0,kx**2+(ky-2*np.pi)**2,U1,U0,U1,0,U0,0],[U0,U0,U1,(kx-2*np.pi)**2+ky**2,U0,0,U1,0,0],[U1,U1,U0,U0,kx**2+ky**2,U0,U0,U1,U1],[0,0,U1,0,U0,(kx+2*np.pi)**2+ky**2,U1,U0,U0],[0,U0,0,U1,U0,U1,kx**2+(ky+2*np.pi)**2,0,U0],[0,0,U0,0,U1,U0,0,(kx+2*np.pi)**2+(ky-2*np.pi)**2,0],[0,0,0,0,U1,U0,U0,0,(kx+2*np.pi)**2+(ky+2*np.pi)**2]])
    return sorted(np.linalg.eigvals(A))

first_brillouin_zone_x,first_brillouin_zone_y = np.linspace(-np.pi,np.pi,step_numbers),np.linspace(-np.pi,np.pi,step_numbers)
epsilon1,epsilon2,epsilon3 = [],[],[]

i = 0
for kx in first_brillouin_zone_x:
    epsilon1.append([])
    epsilon2.append([])
    epsilon3.append([])
    for ky in first_brillouin_zone_y:
        epsilon1[i].append(energy(kx,ky)[0])
        epsilon2[i].append(energy(kx,ky)[1])
        epsilon3[i].append(energy(kx,ky)[2])
    i+=1

#plot
figure = plt.figure(figsize=(10,8))
axe = plt.axes(projection='3d')
axe.contour3D(first_brillouin_zone_x,first_brillouin_zone_y,epsilon1,100,cmap='binary')
axe.contour3D(first_brillouin_zone_x,first_brillouin_zone_y,epsilon2,100,cmap='binary')
axe.contour3D(first_brillouin_zone_x,first_brillouin_zone_y,epsilon3,100,cmap='binary')
axe.set_xlabel('kx')
axe.set_ylabel('ky')
axe.set_zlabel('energy');
plt.show()

figure = plt.figure(figsize=(10,8))
axe = figure.gca()
cf = axe.contourf(first_brillouin_zone_x,first_brillouin_zone_y,epsilon3,levels=100,cmap='jet')
axe.set_xlabel('kx')
axe.set_ylabel('ky')
clb = figure.colorbar(cf)
clb.set_label("energy")
plt.show()




