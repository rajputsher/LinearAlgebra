# create a matrix (3X6)

import numpy as np

m = 3
n = 6
A = np.random.randn(m,n)

# full SVD (variables Us,Ss,Vs)
Us,Ss,Vs = np.linalg.svd(A)

# eig of A'A

L,V = np.linalg.eig(A.T@A)

#sort eigen solution
sidx = np.argsort(L)[::-1]
L = L[sidx]
V = V[:,sidx]

# confirm that V=Vs
print("V==Vs: ",np.round(Vs.T-V,2))

# check the relation between Ss and L 

print(L),print('')
print(Ss**2)

## Create U using only A,V,L

U = np.zeros((m,m))
for i in range(m):
    U[:,i] = A@V[:,i].T/np.sqrt(L[i])

#conform U==Us

print(np.round(U-Us,2))