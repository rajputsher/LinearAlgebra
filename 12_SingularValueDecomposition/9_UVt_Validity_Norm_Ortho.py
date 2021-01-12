import numpy as np

# What is the condition on Matrix A such that U@V.T is a valid operation
# we know that U and V.T are orthogonal basis matrices for Column space of A and Row space of A respectively. Hence there norm is 1.
# What would be the norm of U@V.T ?? 

## U@V.T is a valid operation only when the matrix A is a square.

m =5
A = np.random.randn(m,m)

U,S,V = np.linalg.svd(A) # here in python V is already a V.T

print("Norm of U: ", np.linalg.norm(U,2))
print("Norm of V: ",np.linalg.norm(V,2)) ## induced 2 norm

# norm of U@V

print(np.linalg.norm(U@V,2))

# Compute U@U', V@V', U@V

print("U@U': \n", np.round(U@U.T,3)),print("")
print("V.T@V': \n", np.round(V.T@V,3)),print("")

print("U@V:\n", np.round(U@V,3)),print("")

C = U@V
print("C@C.T: \n",np.round(C@C.T,3))
