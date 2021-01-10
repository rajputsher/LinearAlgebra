# Show that A'*A == R'*R (R from QR decomposition)
# 1) Generate random matrix A
# 2) compute its QR decomp
# 3) test the claim

import numpy as np
import matplotlib.pyplot as plt
import math
from mpl_toolkits.mplot3d import Axes3D


m = 10
n= 4
A = np.random.randn(m,n)


#complete inverse via QR
Q,R = np.linalg.qr(A,"complete")

print(np.round(A.T@A-R.T@R,4))