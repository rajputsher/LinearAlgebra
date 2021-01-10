import numpy as np
import matplotlib.pyplot as plt
import math
from mpl_toolkits.mplot3d import Axes3D

# Vector w, to be decompose
w = np.array([2 ,3])

# vector v, the reference
v = np.array([4,0])

# compute w-parallel-to-v
beta = np.dot(v,w)/(np.dot(v,v))
w_par_v = beta*v

# compute  w-orthogonal-to-v
w_perp_v = w - w_par_v

# Confirm results algrebraically (both parallel and perpendicular compoenets sum to w)

print((w_par_v + w_perp_v) - w)
print(np.dot(w_par_v,w_perp_v))

## Plotting all 4 vectors 

plt.plot([0,w[0]],[0,w[1]],'r',linewidth=3)
plt.plot([0,v[0]],[0,v[1]],'b',linewidth=2)
plt.plot([0,w_par_v[0]],[0,w_par_v[1]],'r--',linewidth=3)
plt.plot([0,w_perp_v[0]],[0,w_perp_v[1]],'r--',linewidth=3)

plt.legend(['w','v','w$_{||v}$','w$_{\perp v}$'])
plt.axis('square')
plt.grid()
plt.axis([-5,5,-5,5])
plt.show()
