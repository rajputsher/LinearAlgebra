import numpy as np
import matplotlib.pyplot as plt
import math

# 2D input vector
v = np.array([ 3, -2 ])

thetas = np.linspace(0,2*np.pi,100)

vec_mags= np.zeros((len(thetas),2))

for i in range(len(thetas)):
    th = thetas[i]
    A_pure = np.array([ [math.cos(th),-math.sin(th)], [math.sin(th),math.cos(th)] ])
    A_impure = np.array([ [2*math.cos(th),-math.sin(th)], [math.sin(th),math.cos(th)] ])

    # compute vector magnitudes
    vec_mags[i,0]=np.linalg.norm(A_pure@v.T)
    vec_mags[i,1]= np.linalg.norm(A_impure@v.T)


plt.plot(thetas,vec_mags,'o-')
plt.xlabel('Roatation angle (rad.)')
plt.ylabel('Av magnitude')
plt.title(['pure rotation','impure rotation'])
plt.show()