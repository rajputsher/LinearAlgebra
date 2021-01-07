import numpy as np
import matplotlib.pyplot as plt
import math

## rules for multiplication validity

m = 4
n = 3
k = 6

# make some matrices
A = np.random.randn(m,n)
B = np.random.randn(n,k)
C = np.random.randn(m,k)

# test which multiplications are valid.
# Think of your answer first, then test.
np.matmul(A,B) # mXn nXk = mXk
#np.matmul(A,A) # mXn mXn  not valid
np.matmul(A.T,C) # nXm  mXk = nXk
np.matmul(B,B.T) # valid
np.matmul(np.matrix.transpose(B),B)# valid
#np.matmul(B,C) #not valid
#np.matmul(C,B) #not valid
#np.matmul(C.T,B) #not valid
np.matmul(C,B.T) #valid