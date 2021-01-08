import numpy as np
import matplotlib.pyplot as plt
import math
from mpl_toolkits.mplot3d import Axes3D
from IPython import display
import time

# these are the coefficients of the equation:
# az = bx + cy + d
eq1o = [1, 2, 3, -1] # [a b c d]
eq2o = [2, 1, 3,  3]

# set up for 3D plot
fig = plt.figure()
ax = fig.gca(projection='3d')
#fig.show()

for i in range(0,10):
    
#     plt.cla()
    #fig.clf()
    # randomly update equations
    eq1 = np.add(eq2o,np.random.randn(1)*eq1o)
    eq2 = np.add(eq1o,np.random.randn(1)*eq2o)
    
    # plot new lines (solutions)
    y = ([eq1[1]*-3, eq1[1]*3] + eq1[3])/eq1[0]
    z = ([eq1[2]*-3, eq1[2]*3] + eq1[3])/eq1[0]
    ax.plot([-3,3],y,z)
    
    # plot new lines (solutions)
    y = ([eq2[1]*-3, eq2[1]*3] + eq2[3])/eq2[0]
    z = ([eq2[2]*-3, eq2[2]*3] + eq2[3])/eq2[0]
    ax.plot([-3,3],y,z)
    
    # axis limits
    ax.set_xlim3d(-3,6)
    ax.set_ylim3d(-3,6)
    ax.set_zlim3d(-1,10)
    
    

    # pause to allow inspection
    display.clear_output(wait=True)
    display.display(plt.gcf())
    time.sleep(.1)
    