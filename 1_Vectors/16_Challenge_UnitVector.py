import numpy as np

# create two random-integer vectors(R4)
n = 4
a=np.round(20*np.random.randn(n))
b=np.round(20*np.random.randn(n))


#compute the lengths of the individual vectors, and the magnitude of their dot product

mag_a = np.sqrt(np.dot(a,a))
mag_b = np.sqrt(np.dot(b,b))
dp_mag = np.abs(np.dot(a,b))

print("Magnitude of a: ", mag_a)
print("Magnitude of b: ", mag_b)
print("Mag of dot product ab: ",dp_mag)
print('')


len_a = np.linalg.norm(a)
len_b = np.linalg.norm(b)
print('Similar to above approach')
print("length of a: ", len_a)
print("length of b: ", len_b)
print('')

# Normalize the vectors , i.e create unit vectors 
au= a/mag_a
bu= b/mag_b

print("a unit vector: ", au)
print("b unit vector: ", bu)
print('')
# compute the magnitude of dot product of unit vectors
dp_mag = np.abs(np.dot(au,bu))
print("Unit vector dot products magnitude:", dp_mag)