import numpy as np
import matplotlib.pyplot as plt
import math
from mpl_toolkits.mplot3d import Axes3D
from IPython import display
import time 



# 3 these are the coefficients of the equation:
# ay = bx + c;
eq1o = [1., 2, 1] # [a b c]
eq2o = [2., 1, 3]


for i in range(10):
    
    # clear plot
    plt.cla()
    
    # randomly update equations
    eq1 = np.add(eq2o,np.random.randn(1)*eq1o)
    eq2 = np.add(eq1o,np.random.randn(1)*eq2o)
    
    # plot new lines (solutions)
    y = ([eq1[1]*-3, eq1[1]*3] + eq1[2])/eq1[0]
    plt.plot([-3,3],y)
    
    y = ([eq2[1]*-3, eq2[1]*3] + eq2[2])/eq2[0]
    plt.plot([-3,3],y)
    plt.axis([-3,3,-3,6])
    plt.show(block = False)
    plt.pause(2)
    # pause to allow inspection
    display.clear_output(wait=True)
    display.display(plt.gcf())
    time.sleep(.1)