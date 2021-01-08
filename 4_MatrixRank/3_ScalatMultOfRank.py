import numpy as np

# check whether the matrix rank is invariant to scalar multiplication

# create two matrices: full-rank and reduced-rank matrices
m=6
n=4

F = np.random.randn(m,n) @ np.random.randn(n)
R = np.random.randn(m,n-1) @ np.random.randn(n-1,n)



# create some scalar
l = 24

# print ranks of F ,R , l*F, l*R
rF = np.linalg.matrix_rank(F)
print('rank(F) = ' + str(rF))

rR = np.linalg.matrix_rank(R)
print('rank(R) = ' + str(rR))

lF= l * F
l_rF = np.linalg.matrix_rank(lF)
print('rank(l*F) = ' + str(l_rF))

lR= l * R
l_rR = np.linalg.matrix_rank(lR)
print('rank(l*R) = ' + str(l_rR))

# check whether rank(l*F) == l*rank(F) no sensible to check this as it will not be equal
rlF = l*rF