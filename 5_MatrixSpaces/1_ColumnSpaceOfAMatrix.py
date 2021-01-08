import numpy as np
import matplotlib.pyplot as plt
import math
from mpl_toolkits.mplot3d import Axes3D


# matrix S
S = np.array( [ [3,0],
                [5,2],
                [1,2] ] )

# vector v
#v = np.array([[-3], [1], [5]]) # in the column space
v = np.array([[1], [7], [3]]) # not in the column space


fig = plt.figure()
ax = fig.gca(projection='3d')

# draw plane corresponding to the column space
xx, yy = np.meshgrid(np.linspace(-5,5,10),np.linspace(-5,5,10))
## This is done to plot the plane 
cp = np.cross(S[:,0],S[:,1])
z1 = (-cp[0]*xx - cp[1]*yy)/cp[2]
ax.plot_surface(xx,yy,z1,alpha=.2)


## plot the two vectors from matrix S
ax.plot([0, S[0,0]],[0, S[1,0]],[0, S[2,0]],'k')
ax.plot([0, S[0,1]],[0, S[1,1]],[0, S[2,1]],'k')

# and the vector v
ax.plot([0, v[0]],[0, v[1]],[0, v[2]],'r')


ax.view_init(elev=150,azim=0)
plt.show()
