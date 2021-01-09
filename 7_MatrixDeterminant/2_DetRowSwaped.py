import numpy as np

# Generate a 6x6 matrix: 

m =6
A = np.random.randn(m,m)
# compute the determinant 
print("Det(A) before swaping: \n", np.linalg.det(A))
# Swap one row, compute determinant
# Swap row 1 and 2
As = A[[1,0,2,3,4,5],:]
print("Det(A) after 1 row swap: \n", np.linalg.det(As))

# Swap two rows, compute determinant
# swap row 1 and 2, and 4 and 5
As2 = A[[1,0,2,4,3,5],:]
print("Det(A) after 2 row swaps: \n", np.linalg.det(As2))