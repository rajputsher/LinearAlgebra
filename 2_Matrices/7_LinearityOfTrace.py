import numpy as np

# topic: linearity of trace 

#Determine the relationship between tr(A)+tr(B) and tr(A+B)
m=4
n=m

#create random matrices
A= np.random.randn(m,n)
B= np.random.randn(m,n)

print("Trace(A): \n",np.trace(A))
print("Trace(B): \n",np.trace(B))
print("Trace(A)+Trace(B): \n",np.trace(A)+np.trace(B))
print("Trace(A+B): \n",np.trace(A+B))
print("")
a1=np.random.randn()

print("tr(a1*A):\n",np.trace(a1*A))
print("a1*tr(A):\n",a1*np.trace(A))


#Determine the relationship between tr(a1*A) and 1*tr(A)