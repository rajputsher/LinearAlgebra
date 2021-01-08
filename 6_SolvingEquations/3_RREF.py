
import numpy as np
from sympy import *

# make some random matrices (using sympy package)
A = Matrix( np.random.randn(4,4) )
B = Matrix( np.random.randn(4,3) )

# compute RREF
rrefA = A.rref()
rrefB = B.rref()

# print out the matrix and its rref
print(np.array(rrefA[0]))
print(' ')
print(np.array(rrefB[0]))
