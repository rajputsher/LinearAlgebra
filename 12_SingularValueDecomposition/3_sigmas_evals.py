import numpy as np

# case 1: eig(A'A) vs. svd(A)
print("case 1: eig(A'A) vs. svd(A)")
A = np.array([ [3,1,0], [1,1,0] ])

print("Eigen Value: " ,np.sort(np.linalg.eig(A.T@A)[0]) )
print("Sigma in SVD: ",np.sort(np.linalg.svd(A)[1])**2 )
print("===============================")
# case 2: eig(A'A) vs. svd(A'A)
print("case 2: eig(A'A) vs. svd(A'A)")
print("Eigen Value: " ,np.sort(np.linalg.eig(A.T@A)[0]))
print("Sigma in SVD: ",np.sort(np.linalg.svd(A.T@A)[1]))
print("===============================")

# case 3a: eig(A) vs. svd(A), real-valued eigs

# need a square matrix for eig
A = [ [3,1,0], [1,1,0], [1,1,1]]
print("case 3a: eig(A) vs. svd(A), real-valued eigs")
print("Eigen Value: " ,np.sort(np.linalg.eig(A)[0]))
print("Sigma in SVD: ",np.sort(np.linalg.svd(A)[1]))
print("===============================")
# case 3b: eig(A) vs. svd(A), complex eigs
print("case 3b: eig(A) vs. svd(A), random matrix, complex eigs")
# random matrices are likely to give complex eigenvalues
A = np.random.randn(3,3)

print("Eigen Value: " ,np.sort(np.linalg.eig(A)[0]))
print("Sigma in SVD: ",np.sort(np.linalg.svd(A)[1]))