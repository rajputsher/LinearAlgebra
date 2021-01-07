import numpy as np

# create a complex number
z = np.complex(3,4)

# magnitude
print("magnitude: ",np.linalg.norm(z) )

# by transpose?
print("by transpose: ", np.transpose(z)*z )

# by Hermitian transpose
print("by hermitian transpose: ", np.transpose(z.conjugate())*z )


# complex vector
v = np.array( [ 3, 4j, 5+2j, np.complex(2,-5) ] )
print("Vector Transpose: ", v.T )
print( "Vector numpy Transpose: ",np.transpose(v) )
print("Hermitian Transpose: ", np.transpose(v.conjugate()) )