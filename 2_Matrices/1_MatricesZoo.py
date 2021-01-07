import numpy as np

# square vs. rectangular
S = np.random.randn(5,5)
R = np.random.randn(5,2) # 5 rows, 2 columns
print("square matrix")
print(S), print(' ')
print("Rectangle matrix")
print(R)

# identity
I = np.eye(3)
print("Identity Matrix")
print(I), print(' ')

# zeros
Z = np.zeros((4,4))
print("Zero Matrix")
print(Z), print(' ')

# diagonal
D = np.diag([ 1, 2, 3, 5, 2 ])
print("Diagonal Matrix")
print(D), print(' ')

# create triangular matrix from full matrices
S = np.random.randn(5,5)
U = np.triu(S)
L = np.tril(S)
print("Triangular Matrix")
print(L), print(' ')

# concatenate matrices (sizes must match!)
A = np.random.randn(3,2)
B = np.random.randn(3,4)
C = np.concatenate((A,B),axis=1)
print("Concatenate Matrix")
print(C)