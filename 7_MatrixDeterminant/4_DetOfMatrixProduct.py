# illustrate that det(AB) = det(A)*det(B)
# 1) for a random 3x3 matrix
# 2) in a loop over random matrix sizes upto 40x40

import numpy as np
import matplotlib.pyplot as plt

m = 3
A = np.random.randn(m,m)
B = np.random.randn(m,m)
AB  = A @ B

print("Det(A): ", np.linalg.det(A))
print("Det(B): ", np.linalg.det(B))
print("Det(A)*Det(B): ", np.linalg.det(A) * np.linalg.det(B))
print("Det(AB): ", np.linalg.det(AB))
print("Det(A)*Det(B)-Det(AB): ", ( np.linalg.det(A) * np.linalg.det(B)) - np.linalg.det(AB))

n=40
dets = np.zeros((n,2))

for k in range(n):
    A = np.random.randn(k,k)
    B = np.random.randn(k,k)
    AB  = A @ B
    dets[k,0] = np.linalg.det(A) * np.linalg.det(B)
    dets[k,1] =  np.linalg.det(AB)

plt.plot(dets[:,0]-dets[:,1],'s-')
plt.ylim([-1,1])
plt.show()

