import numpy as np

# Create 2 symmetric matrices
m =3
A = np.random.randn(m,m)
B = np.random.randn(m,m)

AtA = A.T @ A
BtB = B.T @ B

# compute sum, multiplication and Hadamard Multiplication of the 2 matrices

Csum = AtA + BtB
Cmul = AtA @ BtB
CHmul = AtA * BtB #Hadamard Multiplication

#Determine whether result is symmetric

print(Csum -Csum.T),print('')
print(Cmul -Cmul.T),print('') # Not symmetric
print(CHmul -CHmul.T),print('')