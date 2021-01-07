import numpy as np

m=4; n=6
# create random vectors
A = np.random.randn(m,n)
B = np.random.randn(m,n)

print(A)
print(' ')
print(B)

#method 1
dp_result = np.zeros(6)
for i in range(n):
    dp_result[i] = np.dot(A[:,i],B[:,i])

print("method1")
print(dp_result)
print("\n")

#method 2
dp_result = np.zeros(6)
for i in range(n):
    dp_result[i] = np.matmul(A[:,i],B[:,i])

print("method2")
print(dp_result)
print("\n")


#method 3
dp_result = np.zeros(6)
for i in range(n):
    dp_result[i] = sum(np.multiply(A[:,i],B[:,i]))

print("method3")
print(dp_result)
print("\n")

#method 4
dp_result = np.zeros(6)
for i in range(n):
    for j in range(m):
        dp_result[i] = dp_result[i] + (A[j,i]*B[j,i])

print("method4")
print(dp_result)
print("\n")