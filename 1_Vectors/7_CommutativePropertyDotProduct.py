# Is the dot product commutative?
# a'*b == b'*a

# 1. Generate two 100-element random row vectors, compute dot product a with b, b with a
import numpy as np

m=100
# create random vectors
A = np.random.randn(m)
B = np.random.randn(m)

dp_AB= np.dot(A,B)

dp_BA= np.dot(B,A)

print("A.B= \n",dp_AB)
print("B.A= \n",dp_BA)


# 2. Generate two 2-element integer row vectors, repeat
v = [2,5]
w = [4,8]

dp_vw= np.dot(v,w)

dp_wv= np.dot(w,v)

print("v.w= \n",dp_vw)
print("w.v= \n",dp_wv)
print("\nDot product is commutative")
