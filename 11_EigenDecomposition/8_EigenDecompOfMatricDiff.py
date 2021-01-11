import numpy as np

m =5
A = np.random.randn(m,m) # Without symmetric matrix eigen values and vectors have complex values
A = A.T @ A # Making it symmetric


B = np.random.randn(m,m)
B = B@B.T 

D1,V1 = np.linalg.eig(A-B)
D2,V2 = np.linalg.eig(A@A - A@B - B@A + B@B)

print("D1:\n",np.round(D1,3))

print("D2:\n",np.round(D2,3))

print("D1^2:\n",np.round(D1**2,3))


## sort eigenvalues:

sidx1 = np.argsort(abs(D1))
sidx2 = np.argsort(abs(D2))

print("Sorted D1:\n",np.round(sidx1,3))

print("Sorted D2:\n",np.round(sidx2,3))

## For actual sorting : 

D1 = D1[sidx1]
D2 = D2[sidx2]
print("D1:\n",np.round(D1,3))

print("D2:\n",np.round(D2,3))

V1 = V1[:,sidx1]
V2 = V2[:,sidx2]

print("V1-V2: ", np.round(V1-V2,3))

print("V1:\n",np.round(V1,3))

print("V2:\n",np.round(V2,3))