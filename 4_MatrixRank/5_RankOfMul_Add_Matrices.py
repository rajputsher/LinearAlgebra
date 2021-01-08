import numpy as np

# rules: rank of AB <= min(rank(A),rank(B))
#        rank of A+B<= rank(A)+rank(B)

# generate 2 matrices A , B
m=3
n=5 

A= np.random.randn(m,n) # expected rank <=  min(m,n)
B = np.random.randn(m,n) # expected rank < = min(m,n)
# compute AtA and BtB

AtA = A @ A.T # expected rank = rank(A)
BtB = B @ B.T # expected rank = rank(B)


# find their ranks
rA= np.linalg.matrix_rank(A)
print("rank(A): ", rA)
rB= np.linalg.matrix_rank(B)
print("rank(B): ", rB)

# find ranks of AtA and BtB
rAtA= np.linalg.matrix_rank(AtA)
print("rank(AtA): ", rAtA)
rBtB= np.linalg.matrix_rank(BtB)
print("rank(BtB): ", rBtB)


rAtAMBtB= np.linalg.matrix_rank(AtA@BtB)
print("rank(AtA * BtB): ", rAtAMBtB)

rAtASBtB= np.linalg.matrix_rank(AtA + BtB)
print("rank(AtA + BtB): ", rAtASBtB)

