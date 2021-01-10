import numpy as np

m = 5
a = np.random.randn(m)
b = np.random.randn(m)

A = np.eye(m) - np.outer(a,b) # outer product
Ai = np.eye(m)+ np.outer(a,b)/(1-np.dot(a,b))
print(np.round(A@Ai,3))

# Failure condition
a =a/ np.linalg.norm(a)
b=a 
A = np.eye(m) - np.outer(a,b)
Ai = np.eye(m) + np.outer(a,b) / (1-np.dot(a,b))

#Ideally the dot product of a,a should be zero because of floating point computations , this is not seen here 
print(np.round(A@Ai,3))