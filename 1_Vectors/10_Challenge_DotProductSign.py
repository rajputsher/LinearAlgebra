import numpy as np
# test whether the dot product sign is invariant to scalar multiplication

# generate 2 vectors (R3)
A = np.random.randn(3)
B = np.random.randn(3)
# generate two scalars
alpha = 2
beta = -3

# compute the dot product between the vectors
dot_AB = np.dot(A,B)
print("dot product AB: ", dot_AB)
#compute the dot product between the scaled vectors

dot_alphaA_betaB = np.dot(alpha*A,beta*B)
print("scaled dot productAB: ",dot_alphaA_betaB)