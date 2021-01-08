import numpy as np

# matrix sizes
m = 14
n =  3

# create matrices
A = np.round( 10*np.random.randn(m,n) )

AtA = A.T@A
#print("AtA:\n",AtA)
AAt = A@A.T
#print("AAt:\n",AAt)

# get matrix sizes
sizeAtA = AtA.shape
sizeAAt = AAt.shape

# print info!
print('AtA: %dx%d, rank=%d' %(sizeAtA[0],sizeAtA[1],np.linalg.matrix_rank(AtA)))
print('AAt: %dx%d, rank=%d' %(sizeAAt[0],sizeAAt[1],np.linalg.matrix_rank(AAt)))
