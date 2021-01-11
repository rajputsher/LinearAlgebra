import numpy as np

# Trace(A) = sum(evals)
# det(A)= prod (evals)

m=7
A = np.random.randn(m,m) 
print("trace(A): ", np.round(np.matrix.trace(A),3))
print("Det(A): ", np.round(np.linalg.det(A),3))
evals = np.linalg.eig(A)[0]
print("Eigen Values: \n",evals)
print("sum(evals):", np.round(np.sum(evals),3))
print("prod(evals):",np.round(np.product(evals),3))


print("================ Reduced Rank ==============")
m=7
n =5

A = np.random.randn(m,n) @ np.random.randn(n,m) 
print("trace(A): ", np.round(np.trace(A),3))
print("Det(A): ", np.round(np.linalg.det(A),3))
evals = np.linalg.eig(A)[0]
print("Eigen Values: \n",evals)
print("sum(evals):", np.round(np.sum(evals),3))
print("prod(evals):",np.round(np.product(evals),3))