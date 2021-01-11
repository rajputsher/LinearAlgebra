import numpy as np

m =4
A =np.random.randn(m,m)
AtA = A.T @ A
AAt = A @ A.T

U,S,V = np.linalg.svd(AtA)

diffs = np.zeros(m)
for i in range(m):
    diffs[i] = sum((AAt@A@U[:,i] - A@U[:,i]*S[i] ))

print(np.round(diffs,4))