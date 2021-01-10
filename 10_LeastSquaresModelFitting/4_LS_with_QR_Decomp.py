# Generate random data (Design matrix x , data y)
import numpy as np

m = 10
n=3

X = np.random.randn(m,n)
y = np.random.randn(m,1)

# solve for beta using QR decomposition
Q,R = np.linalg.qr(X)
beta1= np.linalg.solve(R.T@R, (Q@R).T@y)

# compare against standard left inverse method

beta2 = np.linalg.solve(X.T@X,X.T@y)
beta2 = np.linalg.lstsq(X,y,rcond=None)[0]

print("beta with QR decomposition: \n", beta1), print('')

print("beta with left inverse method: \n", beta2), print('')
