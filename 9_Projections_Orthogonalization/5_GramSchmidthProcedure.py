# Implement G-S procedure
# Start with a square matrix
# Check Q'*Q = I 
# Check qr

import numpy as np
import matplotlib.pyplot as plt
import math
from mpl_toolkits.mplot3d import Axes3D

m =4  
n =4
A = np.random.randn(m,n)
Q = np.zeros((m,n)) 

for i in range(n):

    Q[:,i] = A[:,i]
    a = A[:,i]

    # step1 : orthogonalize the ith column in Q relative to the previous columns in A

    for j in range(i):
        q = Q[:,j]
        Q[:,i] = Q[:,i] - np.dot(a,q)/np.dot(q,q)*q

    # step2 : normalize ith column of Q
    Q[:,i] = Q[:,i]/np.linalg.norm(Q[:,i])

#check 1: 

print(np.round(Q.T@Q,3))
plt.imshow(Q.T@Q)
plt.show()

#check2: 

Q2,R = np.linalg.qr(A,"complete")
print(np.round(Q,3)),print('')
print(np.round(Q2,3))
# plt.imshow(np.round(Q,3) - np.round(Q2,3))
# plt.show()