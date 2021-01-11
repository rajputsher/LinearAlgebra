import numpy as np

## Create a nxn Symmetric matrix, take its eigendecomposition 
m = 5
A = np.random.randn(5,5)
A = np.round(10*A.T@A) # Create Symmetric Matrix

D,V = np.linalg.eig(A)

# convert to column vector
v = V[:,2]
print("Eigen Vectors: \n",v)
print("Column Vec: \n", np.reshape(V[:,2],(m,1)))

# show that the norm of the outer product of v_i = 1
op = np.outer(v,v)
print("Outer product: \n",op),print("")

v=np.reshape(V[:,2],(m,1))
print('v*v.T: \n', v*v.T), print('') # with orientation, can use *
print("Norm of outerproduct: ",np.linalg.norm(op))


print("=====================================")

# create one layer of A as lvv', compute its norm
print(v*D[2]*v.T)
print(np.linalg.norm(v*D[2]*v.T))
print(D[2])



# reconstruct A by summing over the eigen layers (outer products)
Arecon = np.zeros((m,m))

for i in range(m):
    v = np.reshape(V[:,i],(m,1))
    Arecon += v*D[i]*v.T
    print(np.linalg.matrix_rank(Arecon))

print("A: \n",A),print('')
print("A reconstructed: \n",Arecon),print("")
print("Are they equal? : \n",np.round(A-Arecon,4)),print("")