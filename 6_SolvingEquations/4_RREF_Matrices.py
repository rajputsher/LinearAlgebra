import numpy as np
from sympy import *

m = 5
n = 5
# make some random matrices (using sympy package)
A = Matrix( np.random.randn(m,n) )
# compute RREF
rrefA = A.rref()
print("Square Matrix")
print("A:\n",np.array(A))
print(' ')
print("RREF(A):\n",np.array(rrefA[0]))
print('------------------------------- ')

m = 8
n = 3
# make some random matrices (using sympy package)
A = Matrix( np.random.randn(m,n) )
# compute RREF
rrefA = A.rref()
print("Tall Matrix")
print("A:\n",np.array(A))
print(' ')
print("RREF(A):\n",np.array(rrefA[0]))
print('------------------------------- ')


m = 3
n = 8
# make some random matrices (using sympy package)
A = Matrix( np.random.randn(m,n) )
# compute RREF
rrefA = A.rref()
print("Wide Matrix")
print("A:\n",np.array(A))
print(' ')
print("RREF(A):\n",np.array(rrefA[0]))
print('------------------------------- ')

# linear dependencies

m = 5
n = 5
# make some random matrices (using sympy package)
A = Matrix( np.random.randn(m,n) )

## Add linear dependency
A[:,0] = A[:,1]

# compute RREF
rrefA = A.rref()
print("Square Matrix")
print("A:\n",np.array(A))
print(' ')
print("RREF(A):\n",np.array(rrefA[0]))
print('------------------------------- ')