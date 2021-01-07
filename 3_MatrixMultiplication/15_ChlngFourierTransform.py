import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft


n = 52
F = np.zeros((n, n), dtype="complex")
w = np.exp(-2*np.pi*np.complex(0,1)/n)
 
for i in range(n):
    for k in range(n):
        m = (i)*(k) # (j - 1)*(k - 1), but python is 0 indexed
        F[i, k] = w**m 
 
fig, ax = plt.subplots(1,3)
ax[0].imshow(np.real(F)); ax[1].imshow(np.imag(F)); ax[2].imshow(np.abs(F))          
 
#x = np.random.randn(n, 1)
x = np.random.randn(n)
x1 = np.matmul(F, x)
 

x2 = fft(x)

fig, ax2 = plt.subplots(1,1)
ax2.plot(range(n), np.abs(x1))
ax2.scatter(range(n), np.abs(x2), s=50, marker='o', facecolors='none', edgecolors='r', label='fft on x')
ax2.scatter(range(n), np.abs(fft(x1)), s=50, marker='o', facecolors='none', edgecolors='g', label='fft on x1')
ax2.legend(loc=1)
plt.show()