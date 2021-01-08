import numpy as np

# size of matrix
m = 30

# create the square symmetric matrix
A = np.random.randn(m,m)
A = np.round( 10*A.T@A )

# reduce the rank
A[:,0] = A[:,1]

# shift amount (l=lambda)
l = .01

# new matrix
B = A + l*np.eye(m,m)

# print information
print('rank(w/o shift) = %d' %np.linalg.matrix_rank(A))
print('rank(with shift) = %d' %np.linalg.matrix_rank(B))