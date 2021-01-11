import numpy as np
import scipy.linalg as slalg
import matplotlib.pyplot as plt 
from scipy.io import loadmat

# Goal: compare eig(S,R) with eig(inv(R) * S)

# part1: GED on 2x2 matrices
m = 2
n = 2
S = np.random.randn(m,n)
R = np.random.randn(m,n)

Ls,Ws = slalg.eig(S,R)
Li,Wi = slalg.eig(np.linalg.inv(R)@S)

print(Ls)
print(Li)

# plot eigenvectors 

plt.plot([0,Ws[0,0]],[0,Ws[1,0]],'k')
plt.plot([0,Ws[0,1]],[0,Ws[1,1]],'k--')
plt.plot([0,Wi[0,0]],[0,Wi[1,0]],'r')
plt.plot([0,Wi[0,1]],[0,Wi[1,1]],'r--')
plt.axis('square')
plt.grid()
plt.axis([-1,1,-1,1])
plt.show()

data = loadmat('real_matrices.mat') # Use complete path

S= data['S']
R= data['R']

fig,ax = plt.subplots(1,2,figsize=(8,5))
ax[0].imshow(S)
ax[0].set_title("S matrix")

ax[1].imshow(R)
ax[1].set_title("R matrix")

plt.show()

print(np.shape(R))
print(np.linalg.matrix_rank(R))

Ls,Ws = slalg.eigh(S,R) # Eigen hermitian/ symmetric
Li,Wi = slalg.eigh(np.linalg.inv(R)@S)

plt.plot(Ls,'s-',label='S,R')
plt.plot(Li,'s-',label='R${-1}$S')
plt.legend()
plt.show()


