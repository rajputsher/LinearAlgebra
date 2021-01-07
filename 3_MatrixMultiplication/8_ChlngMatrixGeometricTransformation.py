import numpy as np
import matplotlib.pyplot as plt
import math

# generate XY coordinates for circle
x = np.linspace(-np.pi,np.pi,100)
xy = np.vstack((np.cos(x),np.sin(x))).T # stacks the cordinates vertically
print(np.shape(xy))

# plot the circle
plt.plot(xy[:,0],xy[:,1],'-o')


#create a 2x2 matrix (starting with 1)
# T = np.array([ [1,2], [2,1] ])
#T = np.array([ [1,0], [0,1] ])
#T = np.array([ [1,3], [2,1] ])
#T = np.array([ [1,0], [0,4] ])


#try with a singular matrix (columns form  a linearly dependent set)
T = np.array([ [1,2], [2,4] ])


# multiply matrix by coordinates
newxy = xy@T

# plot the new coordinates
plt.plot(newxy[:,0],newxy[:,1],'-o')
plt.axis('square')
plt.show()

