import numpy as np

# size of square matrix
m = 3

# generate random matrix
A = np.random.randn(m,m)
print("A: \n",A)
# compute its inverse
Ainv = np.linalg.inv(A)
print("Ainv: \n",Ainv)
# and check the multiplication
idm = A@Ainv


# print the matrix. Note the computer rounding errors on the off-diagonals
print("Identity Matrix:\n",idm)