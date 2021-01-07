# Matrix Multiplication

<img src='images/4PerspectiveOfMultiplication.png' width=500 height=400>

## Element perspective

<img src='images/Element.png' width=500 height=200>

## Layer perspective

<img src='images/Layer.png' width=500 height=300>


## Column perspective

<img src='images/Column.png' width=500 height=300>

## Row perspective

<img src='images/Row.png' width=500 height=300>

---

# Order of Operation

LIVE EVIL rule: simply means that when multiplying matrices and then transposing is equal to taking transpose of individual matrices and then multiplying.
<img src='images/OrderofOperation1.png' width=500 height=50>

Example

<img src='images/OrderOfOperation2.png' width=500 height=150>

# Matrix vector multiplication

Graphical representation

<img src='images/MatrixVectorMultiplication1.png' width=500 height=200>

## Matrix vector multiplication with Symmetric and Non-Symmetric

<img src='images/MultiplicationSymmetricNonSymmetric.png' width=500 height=250>

---
# Matrix 2D Transformation

Multiplying a vector with a matrix: 
The vector will be rotated and scaled.

<img src='images/Transformation1.png' width=500 height=250>

Pure rotation matrix just rotates the vector but does not scale.

<img src='images/Transformation2.png' width=500 height=250>


Here in the below example it is a case where a matrix multiplication just scales the vector and does not roate.
In this example the scaling is 4 times and hence it is similar to multiplying a vector by a scalar

Such vectors are called Eigen vector of the matrix and scalar as Eigen value of the matrix.

This can be represented by Eigen value Equation **Av = l v**

<img src='images/Transformation3.png' width=500 height=250>

---
# Additive and Multiplicative Identity Matrix


Additive Identity Matrix is a zero matrix
Multiplicative Identiy Matrix is a Identity(eye) matrix

<img src='images/IdentityMatrix.png' width=500 height=300>

---
# Additive and Multiplicative Symmetric Matrix

Creating symmetric matrix from non symmetric matrix.
1. Additive Symmetric Matrix Creation

<img src='images/AddSymmetric.png' width=500 height=200>

Example:

<img src='images/AddSymEx.png' width=500 height=200>

This does not work if the matrix is not square.

2. Multiplicative  Symmetric Matrix

<img src='images/MulSymmetric.png' width=500 height=300>

This will always give a symmetric Matrix irrespective of it is a sqaure or a rectangular matrix.

Proof-1: Here it is showing A A.T is symmetric by taking its transponse and arriving again at A A.T

<img src='images/proof1.png' width=500 height=200>


Proof-2:

<img src='images/proof2.png' width=500 height=200>

Example: 
Getting a symmetric square matric from a non symmetric rectangular matrix

<img src='images/MulSymExample.png' width=500 height=200>

## Application of Multiplicative Symmetry

This method is used Statistics and signal processing.
To find the variances and co-variances.
The Diagonal elements gives the variances and the off-diagonal elements give the co-variances .

## Matrix multiplication of two Symmetric matrices

Matrix multiplication of two symmetric matrices are not symmetric. This can be made symmetric with a constraint as shown below.

<img src='images/SymMatrixMul.png' width=500 height=250>

Example:

<img src='images/SymMatricMulEx.png' width=500 height=200>

> This is only true for 2x2 matrix

In general **Multiplication of two Symmetric matrices is not symmetric**

---
## Fourier Transform via Matrix Multiplication


<img src='images/FourierTrans.png' width=500 height=200>

Not a efficient way of creating Fourier transform. Fast fourier transform is.

---

## Frobenius dot product

Vectorization of Matrix:

<img src='images/VectorizationOfMatrix.png' width=500 height=200>

Different methods of computing Frobenius product
Method-1: 

<img src='images/FrobeniusDotProduct1.png' width=500 height=200>

Method-2: 

<img src='images/FrobeniusDotProduct2.png' width=500 height=200>

Method-3: 
Using trace of the matrix:

<img src='images/FrobeniusDotProductFromTrace.png' width=500 height=100>

Heres the trick

<img src='images/FrobeniusDotFroductTrick.png' width=500 height=200>

Frobenius Norm or Norm of a matrix is computed as:

<img src='images/NormOfAMatrix.png' width=500 height=150>

---

## Matrix norms

There are many number of matrix norms. Some of the main ones are:

1. Forbenius norm

<img src='images/NormForbenius.png' width=500 height=150>

2. Induced Norm

Here x =2

<img src='images/NormInduced.png' width=500 height=150>

3. Schatten p-norm

<img src='images/NormSchatten.png' width=500 height=150>

Example:

```python
import numpy as np

# Create a matrix
A = np.array([ [1,2,3], [4,5,6], [7,7,9] ])

# optional orthogonal matrix to show that 2-norm is 1
Q,R = np.linalg.qr(np.random.randn(5,5))
# A = Q

# Frobenius norm
normFrob = np.linalg.norm(A,'fro')

# induced 2-norm
normInd2 = np.linalg.norm(A,2)
# note: computed as below
lamb = np.sqrt( np.max(np.linalg.eig(A.T@A)[0]) )

# schatten p-norm
p = 2
s = np.linalg.svd(A)[1] # get singular values
normSchat = np.sum(s**p)**(1/p)

```
Output: We can see that each of them comput norm which are nearly equal
```bash
Frobenius norm:  16.431676725154983 

Schatten p-norm:  16.431676725154986 

Inuced 2-norm:  16.392007827749776 
```

---
## Conditions and proof of self-adjoint operator

inside <> angle brackets means dot product.
<img src='images/SACondProof.png' width=500 height=250>

---

## Matrix Division

1. Element-wise division 
with the constraint that the second matrix has no 0 element in it.

<img src='images/DivElementWise.png' width=500 height=200>

2. Inverse
This is not exactly division and not all matrices will have an iverse

<img src='images/DivInverse.png' width=500 height=100>

