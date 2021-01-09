# Singular mmatrix has a determinant of 0
import numpy as np


# generate a 2x2 matrix of integers and with linear dependencies
A = np.array([[1,3],[1,3]])
print("A:\n",A)
print("Det(A): ", np.linalg.det(A))


# generate a mxm matrix of integers and with linear dependencies, compute tank again.
# small m and large m

m = 30
A = np.random.randn(m,m)
A[:,0] = A[:,1]
print("Det(A): ", np.linalg.det(A))