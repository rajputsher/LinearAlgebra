import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# two vectors
# v1 = np.array([ 2,  4, -3 ])
# v2 = np.array([ 0, -3, -3 ])

v1 = np.array([ 16,  -2, 4 ])
v2 = np.array([ 0.5, 2, -1 ])


# compute the angle (radians) between two vectors
ang = np.arccos( np.dot(v1,v2) / (np.linalg.norm(v1)*np.linalg.norm(v2)) )


# draw them
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot([0, v1[0]],[0, v1[1]],[0, v1[2]],'b')
ax.plot([0, v2[0]],[0, v2[1]],[0, v2[2]],'r')

plt.axis((-6, 6, -6, 6))
plt.title('Angle between vectors: %s angle.' %(ang*57.29))
plt.show()