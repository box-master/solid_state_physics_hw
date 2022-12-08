import numpy as np
import matplotlib.pyplot as plt

a,t = 1,1
N,n = 400,300


def epsilon(kx,ky,kz):
    return -2*t*(np.cos(kx*a)+np.cos(ky*a)+np.cos(kz*a))

kx,ky,kz = np.linspace(-np.pi/a,np.pi/a,N),np.linspace(-np.pi/a,np.pi/a,N),np.linspace(-np.pi/a,np.pi/a,N)
kx,ky,kz = np.meshgrid(kx,ky,kz)


z = epsilon(kx,ky,kz)
counts,bins = np.histogram(z,bins=n)

figure = plt.figure(figsize=(10,8))
axe = plt.axes()
axe.plot(bins[:-1],counts/N**3*n)
plt.xlabel("epsilon")
plt.ylabel("DOS")
plt.title("density of states")

plt.show()

