import numpy as np

M = np.array([ [1,2,3],
               [2,3,4] ])

print(M), print('')
print(M.T), print('') # one transpose
print(M.T.T), print('') # double-transpose returns the original matrix

# can also use the function transpose
print(np.transpose(M))


# warning! be careful when using complex matrices
C = np.array([ [4+1j , 3 , 2-4j] ])

print(C), print('')
print(C.T), print('')
print(np.transpose(C)), print('')

# Note: In MATLAB, the transpose is the Hermitian transpose; 
#       in Python, you need to call the Hermitian explicitly by first converting from an array into a matrix
print(np.matrix(C).H) # note the sign flips!
