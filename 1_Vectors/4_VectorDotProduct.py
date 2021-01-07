import numpy as np

## many ways to compute the dot product

v1 = np.array([ 1, 2, 3, 4, 5, 6 ])
# v2 = np.array([ 0, -4,  -3, 6, 5 ])
v2 = np.array([ 0, -4,  -3, 6, 5,0 ])

# method 1
dp1 = sum( np.multiply(v1,v2) )

# method 2 # Preffered
dp2 = np.dot( v1,v2 )

# method 3
dp3 = np.matmul( v1,v2 )

# method 4
dp4 = 0  # initialize

# loop over elements
for i in range(len(v1)):
    
    # multiply corresponding element and sum
    dp4 = dp4 + v1[i]*v2[i]


print(dp1,dp2,dp3,dp4)