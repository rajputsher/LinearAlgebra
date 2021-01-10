# Generate a large matrix and invert using QR and inv()

import numpy as np
import matplotlib.pyplot as plt
import math
from mpl_toolkits.mplot3d import Axes3D


m = 100
O = np.random.randn(m,m)

# inverse using inverse function

Oi = np.linalg.inv(O)

#complete inverse via QR

Q,R = np.linalg.qr(O,"complete")

plt.imshow(R)
plt.show()

OiQR1 = np.linalg.inv(R) @ Q.T 
OiQR2 = np.linalg.solve(R,Q.T) 

plt.subplot(1,2,1)
plt.imshow(OiQR1)
plt.title('O$^{-1}$ from inv')

plt.subplot(1,2,2)
plt.imshow(OiQR2)
plt.title('O$^{-1}$ from solve')

plt.show()

print("correlation of three matrix: \n ",np.corrcoef((OiQR1.flatten(), OiQR2.flatten(), Oi.flatten())))

# plt.imshow(np.corrcoef((OiQR1.flatten(), OiQR2.flatten(), Oi.flatten())))
# plt.show()