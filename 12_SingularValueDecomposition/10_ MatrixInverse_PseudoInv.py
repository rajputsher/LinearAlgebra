import numpy as np


# the matrix
A = [ [1,2,3],
      [1,2,4], # hint: change 2->0 for invertible matrix to test
      [1,2,5]  ]
  
# SVD
U,S,V = np.linalg.svd(A)

# pseudoinvert S
nonzeroels = S>10**-14 # find nonzero elements (>rounding errors)
S[nonzeroels] = 1/S[nonzeroels] # invert only those elements

# now pseudoinvert A
Ai = V.T@np.diag(S)@U.T

# it's sortof close to I...?
print("A* A: \n ", np.round(Ai@A,3) ), print(' ')

# compute with pinv function
print("A* A: \n", np.round(np.linalg.pinv(A)@A,3) )

import inspect
lines = inspect.getsource(np.linalg.pinv)
print(lines)