import numpy as np
import matplotlib.pyplot as plt

# create a random matrix
A = np.random.randn(14,14)

# make it symmetric (additive method) 
A = A+A.T

# diagonalize it
evals,evecs = np.linalg.eig(A)
print("Eigen Vectors", evecs)
# magnitudes of each vector
print( np.sqrt( sum(evecs**2) ) )

# and make plots
plt.subplot(131)
plt.imshow(A)
plt.axis('off')
plt.title('A')


plt.subplot(132)
plt.imshow(evecs)
plt.axis('off')
plt.title('Eigenvectors')

plt.subplot(133)
plt.imshow(evecs@evecs.T)
plt.axis('off')
plt.title('VV^T')
plt.show()
