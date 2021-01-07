import numpy as np


M = np.round( 6*np.random.randn(4,4) )
print(M), print(' ')
# extract the diagonals
d = np.diag(M)

# notice the two ways of using the diag function
d = np.diag(M) # input is matrix, output is vector
D = np.diag(d) # input is vector, output is matrix
print(d)
print(D)

# trace as sum of diagonal elements
tr = np.trace(M)
tr2 = sum( np.diag(M) )
print(tr,tr2)