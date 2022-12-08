import matplotlib.pyplot as plt
import numpy as np


a,t = 1,1
N = 7000

def epsilon(kx,ky):
    return -2*t*(np.cos(kx*a)+np.cos(ky*a))


kx,ky = np.linspace(-np.pi/a,np.pi/a,N),np.linspace(-np.pi/a,np.pi/a,N)
kx,ky = np.meshgrid(kx,ky)
z = epsilon(kx,ky)
counts,bins = np.histogram(z,bins=1000,range=(-5,5))


figure = plt.figure(figsize=(10,8))
axe = plt.axes()
axe.plot(bins[:-1],counts/N**2*len(bins),)
plt.xlabel("epsilon")
plt.ylabel("DOS")
plt.title("density of states")

plt.show()







