import numpy as np

# size of matrices
n = 4

# create the matrices
A = np.round( 10*np.random.randn(n,n) )
I = np.eye(n)
Z = np.zeros((n,n))

# test both identities
print(np.array_equal( A@I , A )) 
print(np.array_equal( A   , A@I ))
print(np.array_equal( A   , A+I ))

print(np.array_equal( A   , A+I ))
print(np.array_equal( A+Z , A@I ))