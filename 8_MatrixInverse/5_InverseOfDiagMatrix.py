# Diagonal matrices and their inverses
## " the inverse of a diagonal matrix is simply all of the diagonal elements individually inverted."

# create some diagonal matrices, start with 2x2 integers, work up to larger matrices

import numpy as np

A = np.array([[2,0],[0,3]])

#A = np.diag(np.arange(1,6))

print("A:\n", A)
print("A inverse\n", np.linalg.inv(A))