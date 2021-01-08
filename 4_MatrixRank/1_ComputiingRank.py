import numpy as np
import matplotlib.pyplot as plt
import math

# make a matrix
m = 5
n = 3

# create a random matrix
A = np.random.randn(m,n)

# what is the largest possible rank?
ra = np.linalg.matrix_rank(A)
print('rank = ' + str(ra))

# set last column to be repeat of penultimate column
B = A
B[:,-1] = B[:,-2]

rb = np.linalg.matrix_rank(B)
print('rank = ' + str(rb))

## adding noise to a rank-deficient matrix

print('+++++++++++++++++++++++')
# square for convenience
A = np.round( 10*np.random.randn(m,m) )

# reduce the rank
A[:,-1] = A[:,-2]

# noise level
noiseamp = .001

# add the noise
B = A + noiseamp*np.random.randn(m,m)

print('rank (w/o noise) = ' + str(np.linalg.matrix_rank(A)))
print('rank (with noise) = ' + str(np.linalg.matrix_rank(B)))