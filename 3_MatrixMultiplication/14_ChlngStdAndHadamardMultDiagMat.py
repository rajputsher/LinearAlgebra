# Create 2 matrices (4x4) and diagonal matrix
import numpy as np
A =np.random.randn(4,4) # Full matrix
D= np.diag(np.random.randn(4)) # Diag matrix

# Multiply each matrix by itself : Standard and Hadamard Multiplication

print("AxA standard: "), print(A@A),print('')
print("AxA Hadamard: "), print(A*A),print('')
print("Are they Same? : \n")


print("Diag Matrix: "), print(D), print('')
print("DxD standard: "), print(D@D),print('')
print("DxD Hadamard: "), print(D*D),print('')
print("Are they Same? : \n")