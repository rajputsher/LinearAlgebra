# Generate  a diagonal matrix(2x2), compute its eigen values
import numpy as np

# matrix
A = np.diag([1,2,3,4,5])

# extract the eigenvalues
eigvals = np.linalg.eig(A)

# note that the eigenvalues are in the first element of eigvals:
print("A: \n", A), print('')
print("Eigen Values: ",eigvals[0])
print('===================================')

# Expand this to NxN diagonal matrices
n=10
# matrix
A = np.diag(range(1,n))

# extract the eigenvalues
eigvals = np.linalg.eig(A)

# note that the eigenvalues are in the first element of eigvals:
print("A: \n", A), print('')
print("Eigen Values: ",eigvals[0])

# triangular matrices (lower,upper)

# Upper matrix
A = np.triu([1,2,3,4,5])

# extract the eigenvalues
eigvals = np.linalg.eig(A)

# note that the eigenvalues are in the first element of eigvals:
print("A: \n", A), print('')
print("Eigen Values: ",eigvals[0])

# triangular matrices (lower,upper)
n=10
# Upper matrix
#A = np.tril(np.random.randn(n))
A = np.tril(range(1,n))

# extract the eigenvalues
eigvals = np.linalg.eig(A)

# note that the eigenvalues are in the first element of eigvals:
print("A: \n", A), print('')
print("Eigen Values: ",eigvals[0])