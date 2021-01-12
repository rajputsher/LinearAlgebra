import numpy as np
import matplotlib.pyplot as plt
from sympy import *
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from scipy import linalg


# compute and visualize the normalized quadratic form

#A = np.array([[-2,3],[2,8]])
A = np.array([[-3,3],[-5,7]])

n = 30
xi = np.linspace(-2,2,n)

# for the visualization
X,Y = np.meshgrid(xi,xi)

# initialize
qf  = np.zeros((n,n))
qfN = np.zeros((n,n))

for i in range(n):
    for j in range(n):
        
        # create x (coordinate) vector
        x = np.transpose([ xi[i],xi[j] ])

        # compute the quadratic forms
        qf[i,j]  = x.T@A@x
        qfN[i,j] = qf[i,j] / (x.T@x)

mycmap = plt.get_cmap('gist_earth')

fig = plt.figure(figsize=(5,5))
ax1 = fig.add_subplot(111, projection='3d')
surf1 = ax1.plot_surface(X, Y, qf.T, cmap=mycmap)
ax1.view_init(azim=-30, elev=30)
ax1.set_title('Non-normalized quadratic form')

fig = plt.figure(figsize=(5,5))
ax1 = fig.add_subplot(111, projection='3d')
surf1 = ax1.plot_surface(X, Y, qfN.T, cmap=mycmap, antialiased=False)
ax1.view_init(azim=-30, elev=30)
ax1.set_title('Normalized quadratic form')

plt.show()