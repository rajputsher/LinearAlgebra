# Create a random matrix with a specified condition number
import numpy as np
import matplotlib.pyplot as plt

m = 6
n =16
condnum = 50

#Create singular vectors matrices
# Q of QR decomp is always a singular vectors matrix
U,junk = np.linalg.qr(np.random.rand(m,m))
V,junk = np.linalg.qr(np.random.rand(n,n))

s = np.linspace(condnum,1,np.min([m,n])) ## sig_max = condnum ,sig_min=1
S = np.zeros((m,n))

for i in range(len(s)):
    S[i,i] =s[i]

# create A
A = U@S@V.T
condnum = np.linalg.cond(A)

print("A:\n",A)
print("Condition number: ",np.round(condnum,3))

## Plotting

fig = plt.subplots(1,figsize=(8,5))

plt.subplot(231)
plt.imshow(U)
plt.title("U")

plt.subplot(232)
plt.title("$\Sigma$")
plt.imshow(S)

plt.subplot(233)
plt.imshow(V)
plt.title("$V^T$")

plt.subplot(235)
plt.imshow(A)
plt.title("A,cond=%g" %condnum)

plt.show()
