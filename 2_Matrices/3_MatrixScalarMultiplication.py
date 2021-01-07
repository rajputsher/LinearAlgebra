import numpy as np

# define matrix and scalar
M = np.array([ [1, 2], [2, 5] ])
s = 2

# pre- and post-multiplication is the same:
print( M*s )
print( s*M )