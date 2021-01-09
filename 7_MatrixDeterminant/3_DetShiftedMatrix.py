import numpy as np
import matplotlib.pyplot as plt

# Generate a square random matrix (20x20)
# impose a linear dependence
# 'Shift' the matrix (0->0.1 times the identity matrix)(lamda)
# compute the abs(determinant) of the shifted matrix
# repeat 1000 times, take the average abs(det)
# plot of det as a function of lamda

lambdas = np.linspace(0,0.1,30)

# initialize
tmp = np.zeros(1000)
dets = np.zeros(len(lambdas))

for deti in range(len(lambdas)):
    # run 1000 iterations
    for i in range(1000):

        #generate a matrix
        M = np.random.randn(20,20)
        M[:,0] = M[:,1]
        #compute the determinant
        tmp[i] = abs(np.linalg.det(M + lambdas[deti]*np.eye(20)))

    # compute average determinant
    dets[deti] = np.mean(tmp)

plt.plot(lambdas, dets, 's-')
plt.xlabel('Fraction of identity for shifting')
plt.ylabel('determinant')
plt.show()

