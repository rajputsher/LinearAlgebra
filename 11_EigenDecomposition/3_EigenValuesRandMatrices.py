import numpy as np
import matplotlib.pyplot as plt


# # matrix
# A = np.random.randn(m,m)

# # extract the eigenvalues
# eigvals = np.linalg.eig(A)

# # note that the eigenvalues are in the first element of eigvals:
# print("Eigen Values: ",eigvals[0])

m = 41
itern = 200
evals = np.zeros(itern)
for i in range(itern):
    A = np.random.randn(m,m)
    evals= np.linalg.eig(A)[0]
    plt.plot(np.real(evals),np.imag(evals),'s',markersize=1)

plt.axis('square')
plt.show()