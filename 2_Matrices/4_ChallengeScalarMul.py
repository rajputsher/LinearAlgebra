import numpy as np

m=7
n=5

#create random matrices
A= np.random.randn(m,n)
B= np.random.randn(m,n)

# scalar
s = np.random.randn()

# compute both sides of equation s*(A+B) = s*A +s*B

resL = s * (A+B)
resR = s*A + s*B

print(resL), print("")
print(resR), print("")

print(resL-resR)