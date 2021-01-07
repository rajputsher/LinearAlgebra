import numpy as np

m=5

A= np.random.randn(m,m)
A = A@A.T 

v=np.random.randn(m)
w=np.random.randn(m)

print(np.dot(A@v,w) - np.dot(v,A@w))