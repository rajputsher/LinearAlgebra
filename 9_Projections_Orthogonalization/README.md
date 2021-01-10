# Projections and Orthogonality

## Projections in $R^2$

Projecting a point on to the line.

<img src="images/1.png" width=500 height=300>

i.e Projection is defined as: 

<img src="images/2.png" width=250 height=300>

beta = mapping/magnitude

## Projections in $R^N$

Extending the above forumla from $R^2$ to $R^N$

Considering the system of equations: $Ax=b$

<img src="images/3.png" width=500 height=300>

Here we can see that $x$ is similar to $\beta$

If A is already a Full-rank matrix, then X solves to the following

<img src="images/4.png" width=300 height=200>


This equation can also be represented as:

<img src="images/5.png" width=300 height=200>

---
## Orthogonal and parallel vector components

Decompose a single vector w in to a orthgonal(w$_{\perp v}$) and parallel(w$_{||v}$) vector to a reference vector v. 

<img src="images/6.png" width=500 height=300>

Parallel component w.r.t reference vector V (w$_{||v}$)

<img src="images/7.png" width=400 height=250>

Perpendicular component w.r.t reference vector V (w$_{\perp v}$)

This can be obtained by subracting parallel compoenent from w.

<img src="images/8.png" width=500 height=250>

### Proof : Perpendicular and Parallel components of w are orthogonal

We know that the dot product of 2 vectors is zero when they are orthogonal.

Applying the same here:

<img src="images/9.png" width=500 height=250>

Example: 

Here we are swapping the letters w and v from as used above.

<img src="images/10.png" width=500 height=250>

Geometrically 

<img src="images/11.png" width=500 height=250>

---
## Orthogonal Matrices

Properties: 

<img src="images/12.png" width=400 height=100>

Formal definition

<img src="images/13.png" width=400 height=100>

This is nothing but, $Q^TQ=I$

<img src="images/14.png" width=400 height=150>

Example : 

for $\theta = \Pi/4$ : Roational matrix

<img src="images/15.png" width=500 height=300>

In 3D :

<img src="images/16.png" width=500 height=200>

### Rectangular Q matrix

<img src="images/17.png" width=500 height=200>

Here we can see that it is a one sided inverse matrix as $Q^TQ=I$ and $QQ^T\not = I$

<img src="images/18.png" width=500 height=180>
---

## Gram-Schmidt procedure to create orthogonal matrix


<img src="images/19.png" width=500 height=200>

- 1st column is same as the initial reference matrix
- 2nsd column is the orthogonal vector of the initial 2nd column w.r.t 1st column of the resulting vector
- 3rd column is the orthogonal vector of the initial 3rd column w.r.t 1st column and the 2nd column of the resulting vector
- Similarly for column 4
- Then normalize to get the orthogonal matrix


Example: 

<img src="images/20.png" width=500 height=200>

First column of the resulting vector is same as the initla column 1. To make it a unit vector we need to normalize i.e divide by magnitude ($\sqrt{1^2+3^2}= \sqrt{10}$)

<img src="images/21.png" width=200 height=100>


2nd column of the orthogonal matrix is obtained by subracting the original column2 with the parallel component of column-2 w.r.t coloumn-1

<img src="images/22.png" width=250 height=300>

Similarly for column 3

<img src="images/23.png" width=400 height=300>

All the math results to a  [0 0] vector. This should not come as a surprise because the vector that can be parallel to ${a_1}^*$ and ${a_2}^*$ could only be a zero vector.

Geometrically 

<img src="images/24.png" width=400 height=250>

green arrow --> has just become a unit vector
orange arrow --> now orthogonal to green and unit vector
yellow arrow --> at the origin

Resulting matrix :

<img src="images/25.png" width=400 height=200>

The orthogonal matrix has lost information. i.e, we cannot create the original matrix back form $A^*$. 

We can use the QR method where Q is the orthogonal matrix and R another matrix, together we can get back the original matrix.

---

## QR decomposition


<img src="images/26.png" width=300 height=150>

With this we can obtain the original matrix A. 

R--> Recidual matrix

