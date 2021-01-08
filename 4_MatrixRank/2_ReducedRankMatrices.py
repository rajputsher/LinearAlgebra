# create reduced-rank matrices using matrix multiplication
import numpy as np

# create a 10x10 matrix with rank=4 (use matrix multiplication)
A = np.random.randn(10,4)
B= np.random.randn(4,10)
C = A@B

ra = np.linalg.matrix_rank(A)
print('rank A = ' + str(ra))

rb = np.linalg.matrix_rank(B)
print('rank B = ' + str(rb))

rc = np.linalg.matrix_rank(C)
print('rank C = ' + str(rc))

print("=================================================")
# generalize the procedure to create any mxn matrix with rank r

m =12
n=40
r = 8
# Here we create 2 matrices with rank 8 and using the multiplication property we can always get a rank min(rank(A),rank(B)) that would be r

A = np.random.randn(m,r) 
B= np.random.randn(r,n)

C= A@B

ra = np.linalg.matrix_rank(A)
print('rank A = ' + str(ra))

rb = np.linalg.matrix_rank(B)
print('rank B = ' + str(rb))

rc = np.linalg.matrix_rank(C)
print("Size of C= ", np.shape(C))
print('rank C = ' + str(rc))