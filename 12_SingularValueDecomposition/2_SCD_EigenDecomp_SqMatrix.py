# what is the relationship between eig and SVD for a square symmetric matrix?

# create a symmetric matrix (5X5)
# eig (W,L)
# svd(U,S,V)

# images of all matrices
# compare U and V, and between U and W
import numpy as np
import matplotlib.pyplot as plt 


m=5
A = np.random.randn(m,m) 
A = A.T@A

# Eigen decomp

L,W = np.linalg.eig(A)

# S is vector, V is V.T
U,S,V = np.linalg.svd(A)

print("U: \n",U), print(' ')
print("S: \n",S), print(' ')
print("V: \n",V)


#sort eig outputs 

sidx = np.argsort(L)[::-1] # Gets sort index
L = L[sidx]
W = W[:,sidx]


# images of all matrices

fig,ax = plt.subplots(2,3,figsize=(10,7))
ax[0,0].imshow(W)
ax[0,0].set_title('W (eig)')
ax[0,1].imshow(np.diag(L))
ax[0,1].set_title('L (eig)')
ax[0,2].imshow(np.zeros((1,1)))

ax[1,0].imshow(U)
ax[1,0].set_title('U (svd)')
ax[1,1].imshow(np.diag(S))
ax[1,1].set_title('$\Sigma$ (svd)')
ax[1,2].imshow(V) # This is V.T in python the way it ouputs this value.
ax[1,2].set_title('V$^T$ (svd)')

plt.show()

# compare U and W
print("U-W: \n", np.round(U-W,4)) ## some columns might not be zero that is because of sign flipping , we can verify that by changing U-W to U+W

# compare U and V 
print("U-V: \n", np.round(U-V.T,4))

