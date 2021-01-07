import numpy as np

# any matrix sizes
m = 13
n =  2

# ...but the two matrices must be the same size
A = np.random.randn(m,n)
B = np.random.randn(m,n)

# note the different syntax compared to @ for matrix multiplication
C1 = np.multiply( A,B )
C2 = A*B
#C3 = np.matmul( A,B ) #Error!! not allowed.

print(C1), print(' ')
print(C2), print(' ')

print(C1-C2)
