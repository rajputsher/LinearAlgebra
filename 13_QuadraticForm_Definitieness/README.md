# Quadratic Form and Definiteness

## Algebraic perspective

<img src="images/1.png" width=300 height=200>

Example:

<img src="images/2.png" width=400 height=250>

interpretation: The result 9 is the energy of the matrix S at co-ordinated [3 -1]

General form : 

<img src="images/3.png" width=400 height=150>

What if we have one matrix and many vectors: 

<img src="images/4.png" width=400 height=250>


The rate at which the terms $x^2$ and $y^2$ goes to $\infty$ is different from the term $xy$ going to $\infty$ .

<img src="images/5.png" width=400 height=150>

For a Symmetric matrix S 

<img src="images/6.png" width=300 height=150>

The Transpose of a quatratic form of a symmetric matrix is the same quadratic form.

In this case the equation becomes: 


<img src="images/7.png" width=400 height=150>

Quadratic form of a Identiy matrix: 

<img src="images/9.png" width=400 height=150>


For a 3X3 matrix: 

<img src="images/8.png" width=500 height=250>


## Geometric perspective

Quadratic form can be represented as function of Matrix S and vector w as : $f(S,w)=w^TSw=\epsilon$


<img src="images/10.png" width=400 height=200>

for number of different w's we  get a surface.

<img src="images/11.png" width=400 height=200>

Examples of surfaces for different S.

<img src="images/12.png" width=400 height=250>

The signs of these energy landscapes are related to what is called the definiteness of the matrix.

## Normalized Quadratic form

Non-normalized

<img src="images/13.png" width=400 height=250>

In the above figure we can see that the energy of S increases in all directions as x and y increases to infinity.


Normalized
To get the normalized form

<img src="images/14.png" width=400 height=200>

## Eigen vectors and the quadratic form surfaces

<img src="images/15.png" width=400 height=200>

The eigenvector associated with the larger eigenvalue points in the direction along the **ridge** and the eigenvector associated with these smaller eigenvalue points along the direction of the **valley**.

### Application of normalized quadratic form : PCA

PCA: Principle component analysis

<img src="images/16.png" width=400 height=200>

Here $AA^T$ is the covariance matrix.

The goal of principal components analysis is to find a linear weighted combination of all the channels such that the linear combination maximizes the covariance of the data set.

<img src="images/17.png" width=400 height=200>

How to find the weights ? 

<img src="images/18.png" width=400 height=200>

This is the eigenvalue equation in matrix form. So that means that finding the solution to the problem of the vector that maximizes the normalized quadratic form of a covariance matrix is exactly the Eigen vectors of that matrix.

<img src="images/19.png" width=300 height=150>

## Quadratic form of generalized eigen decomposition

<img src="images/20.png" width=400 height=150>

This is same as below with introduction of a identity matrix.

<img src="images/21.png" width=400 height=150>

Now instead of I we can introduct R .

<img src="images/22.png" width=400 height=150>

Here the assumption is that both S and R are symmetric matrices.


We know from GED is that the eigenvectors matrix of a GED is not an orthogonal matrix. However introducting R we can make it identity matrix.
i.e 

<img src="images/23.png" width=200 height=100>

---
## Matrix definiteness

Definiteness refers to the sign of its energy landscape.

Characteristics of definiteness 

<img src="images/24.png" width=500 height=300>


### Proof : A^T A is always positive (semi) definite

<img src="images/25.png" width=300 height=100>

A transpose A is always positive semi definite or semi definite.

- $A^TA$ is positive definite when A transpose A is invertible, meaning full rank 
- it is positive semi definite when A transpose A is reduced rank or non-invertible or singular.

This is also true for $AA^T$

<img src="images/26.png" width=300 height=100>


Not all symmeteric matrices are positive (semi) definite.

<img src="images/27.png" width=400 height=200>

## Proof: Eigenvalues and matrix definiteness

<img src="images/28.png" width=400 height=250>

<img src="images/29.png" width=400 height=250>

<img src="images/30.png" width=400 height=250>
