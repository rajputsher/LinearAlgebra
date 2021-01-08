import numpy as np

# Determine whether this vector 
v = np.array([[1,2,3,4]]).T
print("v:\n",v)

# is in the span of these sets
S = np.vstack(([4,3,6,2],[0,4,0,1])).T
T = np.vstack(([1,2,2,2],[0,0,1,2])).T 

# print("S: \n", S)
# print("T: \n", T)
print("Rank(S): \n", np.linalg.matrix_rank(S))
print("rank(T): \n", np.linalg.matrix_rank(T))

Sv = np.concatenate((S,v),axis=1) 
Tv = np.concatenate((T,v),axis=1)
print("Sv: \n", Sv)
print("Tv: \n", Tv)
#The axis along which the arrays will be joined. If axis is None, arrays are flattened before use. Default is 0.

print("Rank(Sv): \n", np.linalg.matrix_rank(Sv))
print("rank(Tv): \n", np.linalg.matrix_rank(Tv))

print("The matrix whose rank doesnot change after adding V it means it is in the span")