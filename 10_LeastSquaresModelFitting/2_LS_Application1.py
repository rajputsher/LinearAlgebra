## Least square application: Average of set of numbers formulated as a least square problem

import numpy as np
import matplotlib.pyplot as plt
from sympy import *
import scipy.io as sio
from mpl_toolkits.mplot3d import Axes3D

# data
data = np.array([[-4,0,-3,1,2,8,5,8]]).T
N    = len(data)

# design matrix
X = np.ones([N,1])
# fit the model
b = np.linalg.solve(X.T@X,X.T@data)

# compare against the mean
m = np.mean(data)

# print the results
print(b,m)

# compute the model-predicted values
yHat = X@b

# plot data and model prediction
plt.plot(np.arange(1,N+1),data,'bs-',label='Data')
plt.plot(np.arange(1,N+1),yHat,'ro--',label='Model pred.')

plt.legend()
plt.show()

#####################################################
# new design matrix
X = np.array([np.arange(0,N)]).T

# fit the model
b = np.linalg.solve(X.T@X,X.T@data)

# compute the model-predicted values
yHat = X@b

# plot data and model prediction
plt.plot(np.arange(1,N+1),data,'bs-',label='Data')
plt.plot(np.arange(1,N+1),yHat,'ro--',label='Model pred.')

plt.legend()
plt.show()

#####################################################
# design matrix
X = np.concatenate( [np.ones([N,1]),np.array([np.arange(0,N)]).T],axis=1) ## Adding intercept term to the design matrix
# fit the model
b = np.linalg.solve(X.T@X,X.T@data)

# compute the model-predicted values
yHat = X@b

# plot data and model prediction
plt.plot(np.arange(1,N+1),data,'bs-',label='Data')
plt.plot(np.arange(1,N+1),yHat,'ro--',label='Model pred.')

plt.legend()
plt.show()

#####################################################
## now with nonlinearity in the design matrix

# design matrix
X = np.concatenate( [np.ones([N,1]),np.array([np.arange(0,N)**2]).T],axis=1) ## Adding non linearity by squaring the model.
# fit the model
b = np.linalg.solve(X.T@X,X.T@data)

# compute the model-predicted values
yHat = X@b

# plot data and model prediction
plt.plot(np.arange(1,N+1),data,'bs-',label='Data')
plt.plot(np.arange(1,N+1),yHat,'ro--',label='Model pred.')

plt.legend()
plt.show()

