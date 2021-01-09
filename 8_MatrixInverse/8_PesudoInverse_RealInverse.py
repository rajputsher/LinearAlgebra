#check if pseudo inverse is the same as the "real inverse" for an invertible matrix

import numpy as np
m = 5
A = np.random.randn(m,m) 

AinvF = np.linalg.inv(A)

AinvP = np.linalg.pinv(A)

print("Real inverse: \n",np.round(AinvF,3))

print("Pseudo inverse: \n",np.round(AinvP,3))

print("\nFor a full rank matrix, Real inverse and Pseudo inverse are the same")