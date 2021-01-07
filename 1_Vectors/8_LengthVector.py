import numpy as np

# a vector
v1 = np.array([ 1, 2, 3, 4, 5, 6 ])

# methods 1-4, just like with the regular dot product, e.g.:
vl1 = np.sqrt( sum( np.multiply(v1,v1)) )

# method 5: take the norm(norm is the length directly)
vl2 = np.linalg.norm(v1)

print(vl1,vl2)