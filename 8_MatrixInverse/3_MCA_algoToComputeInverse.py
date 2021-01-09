import numpy as np
from sympy import *
import matplotlib.pyplot as plt

m = 8
A= np.random.randn(m,m)

## Minors Matrix
minors = np.zeros((m,m))
H = np.zeros((m,m))

for i in range(m):
    for j in range(m):

        #select rows and columns
        rows = [True]*m
        rows[i] = False

        cols = [True]*m
        cols[j] = False

        # compute minors matrix
        minors[i,j] = np.linalg.det(A[rows,:][:,cols])


        # compute H matrix
        H[i,j] = (-1)**(i+j)
        

# cofactors matrix

C = H * minors

# Adjugate matrix

Ainv = C.T/np.linalg.det(A)

print("A_A_{-1}$: \n", np.round( A@Ainv))

# comapte to inv function of numpy.linalg

Ainv2 = np.linalg.inv(A)
print("Ainv - Ainv2: ",np.round( Ainv-Ainv2))

# show in an image
plt.subplot(131)
plt.imshow(H)
plt.title('Matrix H: Checker board')

plt.subplot(132)
plt.imshow(A@Ainv)
plt.title('Matrix $AA^{-1}$')

plt.subplot(133)
plt.imshow(np.round( Ainv-Ainv2))
plt.title('Ainv - Ainv2:')

plt.show()