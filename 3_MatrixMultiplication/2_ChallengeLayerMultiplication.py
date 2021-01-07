# implement matrix multiplication
import numpy as np
# gerenate two matrices
n = 4
m = 6
A= np.random.randn(m,n)
B = np.random.randn(n,m)

# build the product matrix layer-wise (for-loop)
C1 = np.zeros((m,m))
for i in range(n):
    C1 += np.outer(A[:,i],B[i,:])

# implement matrix multiplication directly
C2 = np.matmul(A,B)
# C2 = A @ B

# compare the results
print(C1-C2)