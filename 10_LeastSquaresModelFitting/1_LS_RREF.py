import numpy as np
# import matplotlib.pyplot as plt
from sympy import *
# import scipy.io as sio
# from mpl_toolkits.mplot3d import Axes3D


m = 10
n = 3

# create data
X = np.random.randn(m,n) # "design matrix"
y = np.random.randn(m,1) # "outcome measures (data)"

np.shape(y)

# try directly applying RREF
Xy = Matrix( np.concatenate([X,y],axis=1) ) # augmentation
print( Xy.rref() )


# now reapply to the normal equations
XtX = X.T@X
Xty = X.T@y
normEQ = Matrix( np.concatenate( [XtX,Xty],axis=1 ) )

Xsol = normEQ.rref()
Xsol = Xsol[0]
beta = Xsol[:,-1]

print(np.array(Xsol)), print(' ')
print(beta), print(' ')

# compare to left-inverse
beta2 = np.linalg.inv(XtX) @ Xty
print(beta2), print(' ')

# and with the python solver
beta3 = np.linalg.solve(XtX,Xty)
print(beta3) 