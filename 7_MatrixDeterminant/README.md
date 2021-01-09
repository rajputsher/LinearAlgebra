# Matrix Determinant

## Characteristics 

<img src = "images/1.png" width=500 height=250>

## Application of Determinant

<img src = "images/2.png" width=500 height=200>


## Determinant of a 2x2 matric

<img src = "images/3.png" width=300 height=100>

Examples:

<img src = "images/4.png" width=400 height=100>


Determinant of a linearly dependent colums = 0

<img src = "images/5.png" width=400 height=200>

## Determinant of 3x3 matrix

<img src = "images/6.png" width=200 height=200>


Trick1:

- augment the matrix with itself. 
- Make the right diagonals as seen below, multiply and add those
- Make the left diagonals as seen below, multiply and add those
- Determinant = right component - left component


<img src = "images/7.png" width=400 height=250>

<img src = "images/8.png" width=400 height=200>

Determinant  = (aei+bgf+cdh) - (ceg+bdi+afh)

Trick 2 

- make the right diagnonal, and multiply (aei)
- make a next make a smaller diagonal of 2 elements on the lower side of the matrix and multiply it with top right element of upper side i.e (dhc)
- make a next make a smaller diagonal of 2 elements on the upper side of the matrix and multiply it with bottom left element of lower side i.e (bfg)
- Add the three elements (aei+bgf+cdh)

<img src = "images/9.png" width=300 height=200>

Repeat the above steps by making a left diagonal, 
we get (ceg+bdi+afh)

<img src = "images/10.png" width=400 height=200>

Determinant  = (aei+bgf+cdh) - (ceg+bdi+afh)

Example: 

<img src = "images/11.png" width=300 height=200>

<img src = "images/12.png" width=400 height=200>


## Determinant of a 3x3 rank-deficient matrix

It is zero 

<img src = "images/13.png" width=400 height=200>

## Common properties : 

1. The determinant of a identity matrix is always 1.

2. Determinant of a row exchanged Matrix is negative of the original determinant of the matrix.

## Finding an unkown given a determinant

<img src = "images/14.png" width=400 height=200>

<img src = "images/15.png" width=400 height=200>

<img src = "images/16.png" width=400 height=200>